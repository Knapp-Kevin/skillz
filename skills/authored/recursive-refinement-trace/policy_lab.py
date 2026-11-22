#!/usr/bin/env python3
"""Bounded, read-only, observed-path exploration policy laboratory.

Consumes explicitly host-cleared synthetic/public trace exports only.
Never runs tests or commands, changes skills, writes files, or promotes policy.
A valid self-reported trace is not authenticated execution evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

# Imports must not leave unapproved bytecode files in a standalone copy.
sys.dont_write_bytecode = True

import replay

CASE_KEYS = frozenset({"case_id", "split", "task_family", "source", "state",
                       "required_actions", "trace"})
MANIFEST_KEYS = frozenset({"schema_version", "evaluator_sha256", "evaluator_id",
                           "evaluation_context_id", "budget", "candidate", "cases"})
POLICY_KEYS = frozenset({"schema_version", "policy_id", "branch_priority",
                         "verify_lane", "max_attempts", "stop_on"})
REQUIRED_ACTIONS = frozenset({"preservation-check", "run-targeted-verification"})
SPLITS = frozenset({"development", "heldout"})
MAX_CASES = 48
MAX_BYTES = 1_048_576
INDETERMINATE = frozenset({"UNKNOWN_BRANCH", "UNKNOWN_STATE", "STEP_LIMIT",
                           "BUDGET_EXHAUSTED", "RECORDED_BLOCKED", "NO_OBSERVED_BRANCH"})


class LabError(ValueError):
    """Invalid input or unsound proposed policy decision."""


def require(ok, reason):
    if not ok:
        raise LabError(reason)


def exact(obj, keys, what):
    require(type(obj) is dict and set(obj) == keys,
            what + ": missing or unsupported fields")


def digest(value):
    body = json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False).encode("ascii")
    return "sha256:" + hashlib.sha256(body).hexdigest()


def strict_pairs(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, "Duplicate JSON key")
        out[k] = v
    return out


def reject_constant(_):
    raise LabError("Nonfinite JSON number")


def validate_policy(obj, budget):
    exact(obj, POLICY_KEYS, "policy")
    require(type(obj["schema_version"]) is int and obj["schema_version"] == 1,
            "Unsupported policy schema")
    replay.ident(obj["policy_id"], "policy id")
    require(obj["branch_priority"] in replay.POLICIES,
            "Unsupported branch priority")
    require(obj["verify_lane"] in REQUIRED_ACTIONS,
            "Unsupported verification lane")
    require(type(obj["max_attempts"]) is int and
            1 <= obj["max_attempts"] <= min(budget, replay.MAX),
            "Unbounded or invalid attempt cap")
    require(obj["stop_on"] == "recorded-blocked",
            "Stop rule cannot bypass blocked observations")
    # The candidate cannot declare permissions, evaluator, shell, scripts,
    # network, output paths, scoring weights, or approvals.
    return obj


def evaluate(data):
    """Compare frozen incumbent against one declarative proposal.

    This judges only structurally recorded behavior, never live value.
    The caller is responsible for real source clearance, execution receipts
    and authority before even reading the supplied manifest.
    """
    exact(data, MANIFEST_KEYS, "manifest")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1,
            "Unsupported manifest version")
    replay.ident(data["evaluator_id"], "evaluator")
    replay.fingerprint(data["evaluator_sha256"], replay.SHA256, "evaluator source")
    replay.ident(data["evaluation_context_id"], "evaluation context")
    budget = data["budget"]
    require(type(budget) is int and 1 <= budget <= replay.MAX, "Invalid shared budget")
    candidate = validate_policy(data["candidate"], budget)
    cases = data["cases"]
    require(type(cases) is list and 4 <= len(cases) <= MAX_CASES,
            "Insufficient or excessive cases")
    seen_ids, seen_experiments = set(), set()
    families = {split: set() for split in SPLITS}
    results = []
    for c in cases:
        exact(c, CASE_KEYS, "case")
        replay.ident(c["case_id"], "case id")
        require(c["case_id"] not in seen_ids, "Duplicate case id")
        seen_ids.add(c["case_id"])
        require(c["split"] in SPLITS, "Invalid partition")
        require(c["task_family"] in replay.capture.TASKS,
                "Unsupported task family")
        families[c["split"]].add(c["task_family"])
        require(type(c["required_actions"]) is list and
                bool(c["required_actions"]) and
                len(set(c["required_actions"])) == len(c["required_actions"]) and
                all(type(a) is str and a in REQUIRED_ACTIONS
                    for a in c["required_actions"]),
                "Invalid protected verification actions")
        trace = c["trace"]
        root, nodes, _, _ = replay.validate_export(trace)
        require(trace["experiment_id"] not in seen_experiments,
                "Training/holdout experiment reused")
        seen_experiments.add(trace["experiment_id"])
        require(trace["evaluator_id"] == data["evaluator_id"] and
                trace["evaluation_context_id"] == data["evaluation_context_id"],
                "Evaluator/context drift")
        require(nodes[root]["task_family"] == c["task_family"],
                "Case/trace task-family mismatch")
        require(any(n["record_type"] == "observation" and
                    n["action"] in c["required_actions"] for n in nodes.values()),
                "No recorded protected verifier")
        opts = {"budget": budget, "source": c["source"], "state": c["state"],
                "evaluator": data["evaluator_id"],
                "context": data["evaluation_context_id"]}
        baseline = replay.replay(trace, policy="recorded-order",
                                 max_steps=budget, **opts)
        proposed = replay.replay(trace, policy=candidate["branch_priority"],
                                 max_steps=candidate["max_attempts"], **opts)

        def seen_actions(path):
            return {nodes[n]["action"] for n in path["visited_node_ids"]}

        must = set(c["required_actions"]) | {candidate["verify_lane"]}
        base_missing = sorted(must - seen_actions(baseline))
        candidate_missing = sorted(must - seen_actions(proposed))
        # A protected preservation/verification action must have recorded
        # PASS, not merely appear as a selected node. A failing protected
        # action is a veto even if a separate adversarial probe found a bug.
        def protected_failed(path):
            return any(nodes[n]["action"] in must and
                       nodes[n]["outcome"] != "OBSERVED_PASS"
                       for n in path["visited_node_ids"])
        reasons = []
        if candidate_missing or protected_failed(proposed):
            reasons.append("PROTECTED_VERIFIER_SKIPPED_OR_FAILED")
        if (baseline["terminal_status"] in INDETERMINATE or base_missing
                or protected_failed(baseline)):
            reasons.append("BASELINE_INSUFFICIENT")
        if proposed["terminal_status"] in INDETERMINATE:
            reasons.append("CANDIDATE_INDETERMINATE")
        if proposed["observed_outcomes"].get("OBSERVED_PASS", 0) < baseline["observed_outcomes"].get("OBSERVED_PASS", 0):
            reasons.append("PRESERVATION_REGRESSION")
        detected_delta = (proposed["observed_outcomes"].get("OBSERVED_FAIL", 0) -
                          baseline["observed_outcomes"].get("OBSERVED_FAIL", 0))
        results.append({
            "case_id": c["case_id"], "split": c["split"],
            "task_family": c["task_family"],
            "baseline": {"terminal": baseline["terminal_status"],
                         "visited": baseline["visited_node_ids"],
                         "test_calls": baseline["test_invocations"],
                         "recorded_wall_ms": baseline["wall_ms"]},
            "candidate": {"terminal": proposed["terminal_status"],
                          "visited": proposed["visited_node_ids"],
                          "test_calls": proposed["test_invocations"],
                          "recorded_wall_ms": proposed["wall_ms"]},
            "recorded_failure_detection_delta": detected_delta,
            "veto_reasons": reasons,
        })
    require(len(families["development"]) >= 2 and len(families["heldout"]) >= 2,
            "Need development and heldout examples from two task families")
    require(families["heldout"].issubset(families["development"]),
            "Heldout family has no development comparator")
    veto = sorted({r for c in results for r in c["veto_reasons"]})
    dev = [c for c in results if c["split"] == "development"]
    holdout = [c for c in results if c["split"] == "heldout"]
    improvement = (all(c["recorded_failure_detection_delta"] > 0 for c in dev)
                   and all(c["recorded_failure_detection_delta"] > 0 for c in holdout))
    if veto and any(v in veto for v in ("PROTECTED_VERIFIER_SKIPPED_OR_FAILED",
                                       "PRESERVATION_REGRESSION")):
        decision = "REJECT_CANDIDATE"
    elif veto or not improvement:
        decision = "HOLD_INCUMBENT"
    else:
        decision = "PROPOSE_BOUNDED_LIVE_PILOT"
    return {
        "schema_version": 1, "decision": decision,
        "incumbent": "recorded-order",
        "candidate_policy_id": candidate["policy_id"],
        "candidate_policy_sha256": digest(candidate),
        "manifest_sha256": digest(data),
        "evaluator_id": data["evaluator_id"],
        "evaluator_sha256": data["evaluator_sha256"],
        "evaluation_context_id": data["evaluation_context_id"],
        "common_test_call_budget": budget, "veto_reasons": veto,
        "development_case_count": len(dev),
        "heldout_case_count": len(holdout),
        "heldout_families": sorted(families["heldout"]),
        "cases": results, "automatic_activation": False,
        "actual_host_execution_authenticated": False,
        "only_realized_branches_evaluated": True,
        "real_user_effectiveness_verified": False,
        "next_gate": "OWNER_AUTHORIZED_BOUNDED_LIVE_PILOT",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True,
                        help="Authorized public/synthetic manifest, <=1 MiB")
    parser.add_argument("--approved-public", action="store_true",
                        help="Guard only; caller must independently establish clearance")
    args = parser.parse_args(argv)
    try:
        require(args.approved_public, "Public/synthetic clearance must be established by host")
        # Reject a linked file OR linked parent before any read/stat.
        # Lexical inspection does not prevent concurrent filesystem races.
        path = Path(args.manifest).absolute()
        require(not any(part.is_symlink() for part in (path, *path.parents)),
                "Symlinked manifest or ancestor refused")
        require(path.is_file() and path.stat().st_size <= MAX_BYTES,
                "Invalid manifest path or size")
        manifest = json.loads(path.read_text(encoding="utf-8"),
                              object_pairs_hook=strict_pairs,
                              parse_constant=reject_constant)
        print(json.dumps(evaluate(manifest), sort_keys=True))
    except (LabError, replay.ReplayError, OSError, UnicodeError,
            ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)},
                         sort_keys=True), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
