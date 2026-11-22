#!/usr/bin/env python3
"""Audit an analyst-expanded, repository-neutral CI execution graph.

This is a deterministic overlap *candidate* finder, not a YAML interpreter,
semantic-equivalence oracle, trusted receipt verifier, or GitHub cost source.
"""
import argparse
import itertools
import json
import sys
from pathlib import Path

DISPOSITIONS = {"CONSOLIDATE", "KEEP", "RELOCATE", "VERIFY"}


def no_duplicate_keys(pairs):
    obj = {}
    for k, v in pairs:
        if k in obj:
            raise ValueError("duplicate JSON key")
        obj[k] = v
    return obj


def required(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: nonempty string required")
    return value


def audit(graph):
    """Return terminal-command overlaps between comparable entrypoints.

    Input schema:
      nodes: {node_id: {calls: [node_id]} OR
                       {command: str, obligation: str, inputs: str}}
      entrypoints: [{id, cohort, environment, trust_boundary,
                     invokes: [node_id], independence?: {reason, evidence}}]
      decisions: {"alpha|beta": {disposition, evidence}}
    Caller must establish that a cohort represents the same candidate
    revision and event purpose. Different runs may be incomparable.
    """
    nodes = graph.get("nodes")
    entries = graph.get("entrypoints")
    if not isinstance(nodes, dict) or not isinstance(entries, list):
        raise ValueError("nodes must be an object and entrypoints an array")
    if not isinstance(graph.get("decisions", {}), dict):
        raise ValueError("decisions must be an object")
    seen = set()

    def expand(name, trail=()):
        required(name, "node ID")
        if name not in nodes:
            raise ValueError(f"unresolved invocation: {name}")
        if name in trail:
            raise ValueError(f"invocation cycle: {' -> '.join((*trail, name))}")
        node = nodes[name]
        if not isinstance(node, dict):
            raise ValueError(f"invalid node: {name}")
        if "calls" in node:
            if ("command" in node or not isinstance(node["calls"], list)
                    or not node["calls"]):
                raise ValueError(f"invalid nonterminal: {name}")
            return [leaf for child in node["calls"]
                    for leaf in expand(child, (*trail, name))]
        terminal = tuple(required(node.get(field), f"{name}.{field}")
                         for field in ("command", "obligation", "inputs"))
        return [(terminal, (*trail, name))]

    expanded = []
    for e in entries:
        if not isinstance(e, dict):
            raise ValueError("invalid entrypoint")
        for field in ("id", "cohort", "environment", "trust_boundary"):
            required(e.get(field), f"entrypoint.{field}")
        if e["id"] in seen:
            raise ValueError(f"duplicate entrypoint ID: {e['id']}")
        seen.add(e["id"])
        if not isinstance(e.get("invokes"), list) or not e["invokes"]:
            raise ValueError(f"entrypoint {e['id']}: invokes must be nonempty")
        resolved_paths = [leaf for root in e["invokes"] for leaf in expand(root)]
        leaves = set(leaf[0] for leaf in resolved_paths)
        paths = [{"command": leaf[0][0], "obligation": leaf[0][1],
                  "inputs": leaf[0][2],
                  "path": " -> ".join((e["id"], *leaf[1]))}
                 for leaf in resolved_paths]
        ind = e.get("independence") or {}
        if not isinstance(ind, dict):
            raise ValueError(f"entrypoint {e['id']}: independence must be object")
        expanded.append((e, leaves, ind, paths))

    findings = []
    for (a, aa, a_ind, a_paths), (b, bb, b_ind, b_paths) in itertools.combinations(expanded, 2):
        # A retired path remains in the inventory but no longer executes.
        # Strict cutover independently demands exact-revision retirement proof.
        if a.get("active") is False or b.get("active") is False:
            continue
        if a["cohort"] != b["cohort"]:
            continue
        ac = {(cmd, obligation) for cmd, obligation, _ in aa}
        bc = {(cmd, obligation) for cmd, obligation, _ in bb}
        common = ac & bc
        if not common:
            continue
        same_boundary = (a["environment"] == b["environment"]
                         and a["trust_boundary"] == b["trust_boundary"]
                         and "UNKNOWN" not in (a["environment"],
                                               b["environment"],
                                               a["trust_boundary"],
                                               b["trust_boundary"]))
        common_a = {x for x in aa if x[:2] in common}
        common_b = {x for x in bb if x[:2] in common}
        same_inputs = (common_a == common_b
                       and all(x[2] != "UNKNOWN" for x in common_a))
        independence_claim = any(
            isinstance(ind.get("reason"), str) and ind["reason"].strip()
            and isinstance(ind.get("evidence"), str) and ind["evidence"].strip()
            for ind in (a_ind, b_ind)
        )
        if independence_claim:
            classification = "JUSTIFIED_REPETITION_CLAIM"
        elif not (same_boundary and same_inputs):
            classification = "UNPROVEN"
        elif aa == bb:
            classification = "EXACT_DUPLICATE_CANDIDATE"
        else:
            classification = "PARTIAL_OVERLAP"
        pair = "|".join(sorted((a["id"], b["id"])))
        decision = graph.get("decisions", {}).get(pair, {})
        if not isinstance(decision, dict):
            raise ValueError(f"{pair}: decision must be object")
        disposition = decision.get("disposition")
        evidence = decision.get("evidence")
        resolved = (disposition in DISPOSITIONS
                    and isinstance(evidence, str) and bool(evidence.strip()))
        # An unsupported equivalence cannot authorize deleting a control.
        if classification == "UNPROVEN" and disposition == "CONSOLIDATE":
            resolved = False
        findings.append({
            "pair": pair,
            "cohort": a["cohort"],
            "classification": classification,
            "normalized_class": {"EXACT_DUPLICATE_CANDIDATE": "EXACT_DUPLICATE",
                                 "JUSTIFIED_REPETITION_CLAIM": "JUSTIFIED_REPETITION"}.get(
                                     classification, classification),
            "terminal_commands": sorted(cmd for cmd, _ in common),
            "invocation_paths": [row for row in (*a_paths, *b_paths)
                                 if (row["command"], row["obligation"]) in common],
            "disposition": disposition if resolved else "UNDISPOSED",
            "evidence": evidence if resolved else None,
            "resolved": resolved,
        })
    return {
        "status": "ANALYST_GRAPH_ONLY_NOT_HOST_VERIFIED",
        "entrypoints": len(entries),
        "findings": findings,
        "unresolved": sum(not finding["resolved"] for finding in findings),
        "entrypoint_terminals": [
            {"id": e["id"], "stage": e.get("stage", "NOT_DECLARED"),
             "active": e.get("active", True),
             "obligations": sorted({t[1] for t in leaves}),
             "invocation_paths": paths}
            for e, leaves, _, paths in expanded
        ],
        "optimization_complete": False,
        "observed_runner_minutes_delta": "NOT_MEASURED",
        "observed_critical_path_delta": "NOT_MEASURED",
    }



def qualify_cutover(graph, report):
    """Conservative source-graph cutover gate, not authenticated CI assurance.

    Requires explicit draft/candidate/release dispatch and exact-revision
    terminal receipts. Reuses audit() expansions rather than a second
    verification graph interpreter. Never asserts observed savings.
    """
    issues = []
    policy = graph.get("post_cutover")
    if not isinstance(policy, dict):
        return {"status": "FAIL", "issues": ["CUTOVER_POLICY_MISSING"],
                "host_authenticated": False, "optimization_complete": False}
    source = policy.get("source_revision")
    if not isinstance(source, str) or not source.strip() or source == "UNKNOWN":
        issues.append("SOURCE_REVISION_UNBOUND")
    if policy.get("inventory_complete") is not True:
        issues.append("INVENTORY_NOT_COMPLETE")
    if report["unresolved"]:
        issues.append("UNDISPOSED_OVERLAP")
    for finding in report["findings"]:
        # Even a documented plan to consolidate is unfinished while BOTH
        # paths still execute. An alleged KEEP does not justify a repeated
        # terminal without distinct observed failure assurance.
        if finding["classification"] in {"EXACT_DUPLICATE_CANDIDATE", "PARTIAL_OVERLAP"}:
            issues.append("REDUNDANT_ACTIVE_INVOCATION:" + finding["pair"])
        elif finding["classification"] == "UNPROVEN":
            issues.append("EQUIVALENCE_NOT_PROVEN:" + finding["pair"])
        elif (finding["classification"] == "JUSTIFIED_REPETITION_CLAIM"
              and (finding["disposition"] != "KEEP" or not finding["resolved"])):
            issues.append("REPETITION_NOT_QUALIFIED:" + finding["pair"])

    current = graph.get("entrypoints", [])
    terminals = {record["id"]: record for record in report["entrypoint_terminals"]}
    active = {"candidate": set(), "release": set()}
    for entry in current:
        if not isinstance(entry, dict):
            issues.append("INVALID_ENTRYPOINT")
            continue
        eid = entry.get("id", "")
        if entry.get("active") is False:
            proof = entry.get("retirement_proof")
            if (not isinstance(proof, dict) or
                proof.get("revision") != source or
                not isinstance(proof.get("evidence"), str) or
                not proof["evidence"].strip()):
                issues.append("DISABLED_PATH_UNVERIFIED:" + str(eid))
            continue
        if entry.get("active", True) is not True:
            issues.append("ACTIVITY_UNKNOWN:" + str(eid))
            continue
        if (entry.get("matrix_expanded") is not True or
            not isinstance(entry.get("event"), str) or
            not entry["event"].strip() or entry["event"] == "UNKNOWN" or
            not isinstance(entry.get("condition"), str) or
            not entry["condition"].strip() or entry["condition"] == "UNKNOWN"):
            issues.append("TRIGGER_OR_MATRIX_UNPROVEN:" + str(eid))
        if entry.get("revision") != source:
            issues.append("ENTRYPOINT_REVISION_STALE:" + str(eid))
        stage = entry.get("stage")
        if stage == "draft":
            if entry.get("expensive") is not False:
                issues.append("DRAFT_EXPENSIVE_PATH:" + str(eid))
        elif stage in active:
            active[stage].update(terminals[eid]["obligations"])
        else:
            issues.append("STAGE_NOT_DECLARED:" + str(eid))

    if policy.get("draft_status") != "DRAFT_DEFERRED_NOT_QUALIFIED":
        issues.append("DRAFT_FALSE_QUALIFICATION")
    required = policy.get("required")
    receipt_set = policy.get("receipts")
    if not isinstance(required, dict) or not isinstance(receipt_set, dict):
        issues.append("QUALIFICATION_EVIDENCE_MISSING")
    else:
        for stage in ("candidate", "release"):
            stage_required = required.get(stage)
            receipts = receipt_set.get(stage)
            if (not isinstance(stage_required, list) or not stage_required or
                len(set(stage_required)) != len(stage_required) or
                not all(isinstance(x, str) and x for x in stage_required)):
                issues.append("REQUIRED_POLICY_MISSING:" + stage)
                continue
            if not isinstance(receipts, list):
                issues.append("QUALIFICATION_RECEIPTS_MISSING:" + stage)
                continue
            observed = {}
            for row in receipts:
                if (not isinstance(row, dict) or
                    not isinstance(row.get("obligation"), str)):
                    issues.append("RECEIPT_INVALID:" + stage)
                    continue
                key = row["obligation"]
                if key in observed:
                    issues.append("RECEIPT_DUPLICATE:" + stage + ":" + key)
                observed[key] = row
                if row.get("result") != "success" or row.get("revision") != source:
                    issues.append("RECEIPT_FAILED_OR_STALE:" + stage + ":" + key)
            if set(stage_required) != set(observed):
                issues.append("REQUIRED_RECEIPT_SET_MISMATCH:" + stage)
            if set(stage_required) - active[stage]:
                issues.append("REQUIRED_TERMINAL_NOT_EXECUTED:" + stage)
    return {
        "status": "PASS" if not issues else "FAIL",
        "issues": sorted(set(issues)),
        "host_authenticated": False,
        "optimization_complete": False,
        "observed_runner_minutes_delta": "NOT_MEASURED",
        "observed_critical_path_delta": "NOT_MEASURED",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph", type=Path, help="trusted analyst-expanded graph JSON")
    parser.add_argument("--enforce", action="store_true",
                        help="exit 2 if evidenced dispositions are missing")
    parser.add_argument("--verify-cutover", action="store_true",
                        help="exit 3 on duplicate/stale/missing authoritative cutover verification")
    args = parser.parse_args(argv)
    try:
        source = args.graph.absolute()
        if any(p.is_symlink() for p in (source, *source.parents)):
            raise ValueError("linked graph path or ancestor")
        if source.stat().st_size > 1024 * 1024:
            raise ValueError("graph exceeds 1 MiB")
        graph = json.loads(source.read_text(encoding="utf-8"),
                           object_pairs_hook=no_duplicate_keys)
        result = audit(graph)
        if args.verify_cutover:
            result["cutover"] = qualify_cutover(graph, result)
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"INVALID_GRAPH: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    if args.enforce and result["unresolved"]:
        return 2
    if args.verify_cutover and result["cutover"]["status"] != "PASS":
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
