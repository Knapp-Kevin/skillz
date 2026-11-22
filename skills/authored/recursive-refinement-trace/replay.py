#!/usr/bin/env python3
"""Deterministic, observed-only replay of externally approved Skillz traces.

This component is optional and host-invoked. It never runs discovery tasks,
executes arbitrary code from traces, writes a log, or promotes a policy.
Only recorded, causally compatible branches may supply outcomes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

# Resolved from the installed, standalone skill package beside this file.
import trace as capture

POLICIES = ("recorded-order", "adversarial-first")
FIELDS = frozenset({"schema_version", "experiment_id", "evaluator_id",
                    "evaluation_context_id", "nodes", "receipts"})
BASE = frozenset({"node_id", "parent_node_id", "record_type", "candidate_id",
                  "task_family", "action", "source_artifact_git_blob",
                  "workspace_state_digest", "evaluator_id", "evaluation_context_id"})
OBSERVED = BASE | frozenset({"outcome", "receipt_digest",
                            "post_source_artifact_git_blob", "post_workspace_state_digest"})
RECEIPT = frozenset({"node_id", "outcome", "action", "source_artifact_git_blob",
                     "workspace_state_digest", "evaluator_id", "evaluation_context_id",
                     "test_invocations", "wall_ms"})
PRIORITY = {"adversarial-probe": 0, "preservation-check": 1,
            "run-targeted-verification": 2, "inspect": 3}
ID = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
SHA1 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
MAX = 1000


class ReplayError(ValueError):
    """Unsafe, unverifiable or unsupported replay request."""


def require(condition, reason):
    if not condition:
        raise ReplayError(reason)


def exact(value, fields, reason):
    require(type(value) is dict and set(value) == fields, reason + ": invalid fields")


def ident(value, reason):
    require(type(value) is str and ID.fullmatch(value) is not None,
            reason + ": invalid identifier")


def fingerprint(value, pattern, reason):
    require(type(value) is str and pattern.fullmatch(value) is not None,
            reason + ": invalid digest")


def receipt_digest(payload):
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=True, allow_nan=False).encode("ascii")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def validate_export(data):
    """Validate v1 closed-world export; does not authenticate external execution.

    Returned children preserve recorded order, not post-hoc outcome rankings.
    The actual CLI additionally requires the Phase-1 verified local hash chain.
    """
    exact(data, FIELDS, "trace")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1,
            "Unsupported trace version")
    for key in ("experiment_id", "evaluator_id", "evaluation_context_id"):
        ident(data[key], key)
    nodes, receipts = data["nodes"], data["receipts"]
    require(type(nodes) is list and 1 <= len(nodes) <= MAX, "Invalid node count")
    require(type(receipts) is list and len(receipts) <= MAX, "Invalid receipt count")
    indexed, children = {}, {}
    roots = []
    for index, node in enumerate(nodes):
        require(type(node) is dict, "Node must be an object")
        kind = node.get("record_type")
        require(type(kind) is str and kind in ("proposal", "observation"),
                "Unsupported record type")
        exact(node, OBSERVED if kind == "observation" else BASE, "node")
        for key in ("node_id", "candidate_id", "evaluator_id", "evaluation_context_id"):
            ident(node[key], key)
        require(node["node_id"] not in indexed, "Duplicate node identity")
        require(node["evaluator_id"] == data["evaluator_id"] and
                node["evaluation_context_id"] == data["evaluation_context_id"],
                "Evaluator/context drift")
        require(type(node["task_family"]) is str and
                node["task_family"] in capture.TASKS, "Unsupported task family")
        require(type(node["action"]) is str and
                node["action"] in capture.ACTIONS, "Unsupported action")
        fingerprint(node["source_artifact_git_blob"], SHA1, "source")
        fingerprint(node["workspace_state_digest"], SHA256, "state")
        parent = node["parent_node_id"]
        require(parent is None or (type(parent) is str and ID.fullmatch(parent)),
                "Invalid parent identity")
        if parent is None:
            roots.append(node["node_id"])
        if kind == "observation":
            require(type(node["outcome"]) is str and
                    node["outcome"] in capture.OUTCOMES, "Unsupported outcome")
            fingerprint(node["receipt_digest"], SHA256, "receipt")
            fingerprint(node["post_source_artifact_git_blob"], SHA1, "post source")
            fingerprint(node["post_workspace_state_digest"], SHA256, "post state")
        indexed[node["node_id"]] = node
        children[node["node_id"]] = []
    require(len(roots) == 1, "Exactly one root required")
    root_id = roots[0]
    require(indexed[root_id]["record_type"] == "proposal" and
            indexed[root_id]["action"] == "inspect", "Invalid root")
    task_family = indexed[root_id]["task_family"]
    require(all(node["task_family"] == task_family for node in nodes),
            "Task family drift within a frozen experiment")

    # No recursive traversal: a 1,000-node chain must remain supported.
    for node_index, node in enumerate(nodes):
        parent = node["parent_node_id"]
        if parent is None:
            continue
        require(parent in indexed and parent != node["node_id"], "Missing/cyclic parent")
        require(next(i for i, item in enumerate(nodes) if item["node_id"] == parent) < node_index,
                "Child precedes parent in recorded history")
        ancestor = indexed[parent]
        expect_source = (ancestor["post_source_artifact_git_blob"] if
                         ancestor["record_type"] == "observation" else
                         ancestor["source_artifact_git_blob"])
        expect_state = (ancestor["post_workspace_state_digest"] if
                        ancestor["record_type"] == "observation" else
                        ancestor["workspace_state_digest"])
        require(node["source_artifact_git_blob"] == expect_source and
                node["workspace_state_digest"] == expect_state,
                "UNKNOWN_STATE: child preconditions differ from parent")
        children[parent].append(node["node_id"])
    visited, stack = set(), [root_id]
    while stack:
        node_id = stack.pop()
        require(node_id not in visited, "Cycle or reused node")
        visited.add(node_id)
        stack.extend(children[node_id])
    require(len(visited) == len(nodes), "Unreachable or cyclic branch")

    by_digest = {}
    for item in receipts:
        exact(item, {"digest", "payload"}, "receipt")
        payload = item["payload"]
        exact(payload, RECEIPT, "receipt payload")
        for key in ("node_id", "evaluator_id", "evaluation_context_id"):
            ident(payload[key], key)
        require(type(payload["outcome"]) is str and payload["outcome"] in capture.OUTCOMES,
                "Unsupported receipt outcome")
        require(type(payload["action"]) is str and payload["action"] in capture.ACTIONS,
                "Unsupported receipt action")
        fingerprint(payload["source_artifact_git_blob"], SHA1, "receipt source")
        fingerprint(payload["workspace_state_digest"], SHA256, "receipt state")
        require(type(payload["test_invocations"]) is int and
                1 <= payload["test_invocations"] <= MAX,
                "Invalid test invocation count")
        require(type(payload["wall_ms"]) is int and
                0 <= payload["wall_ms"] <= 86_400_000,
                "Invalid elapsed time")
        fingerprint(item["digest"], SHA256, "receipt digest")
        require(receipt_digest(payload) == item["digest"], "Corrupted receipt")
        require(item["digest"] not in by_digest, "Duplicate receipt")
        by_digest[item["digest"]] = payload
    used = set()
    for node in nodes:
        if node["record_type"] != "observation":
            continue
        key = node["receipt_digest"]
        require(key in by_digest, "Missing receipt")
        proof = by_digest[key]
        for field in ("node_id", "outcome", "action", "source_artifact_git_blob",
                      "workspace_state_digest", "evaluator_id", "evaluation_context_id"):
            require(proof[field] == node[field], "Receipt not bound to observation")
        used.add(key)
    require(used == set(by_digest), "Unreferenced receipt")
    return root_id, indexed, children, by_digest


def replay(data, *, policy, budget, source, state, evaluator, context,
           requested_node=None, max_steps=MAX):
    """Replay one isolated observed lineage; unknowns NEVER become reward."""
    require(type(policy) is str and policy in POLICIES, "Unsupported policy")
    require(type(budget) is int and 0 <= budget <= MAX, "Invalid call budget")
    require(type(max_steps) is int and 1 <= max_steps <= MAX, "Invalid step bound")
    if requested_node is not None:
        ident(requested_node, "requested node")
    fingerprint(source, SHA1, "trusted source")
    fingerprint(state, SHA256, "trusted state")
    ident(evaluator, "trusted evaluator")
    ident(context, "trusted context")
    root_id, indexed, children, receipts = validate_export(data)
    require(data["evaluator_id"] == evaluator and
            data["evaluation_context_id"] == context,
            "Trusted evaluator/context mismatch")
    root = indexed[root_id]
    spent_calls = 0
    spent_ms = 0
    visited = []
    decisions_attempted = 0
    outcomes = {key: 0 for key in sorted(capture.OUTCOMES)}
    known = sum(n["record_type"] == "observation" for n in indexed.values())
    terminal = "PATH_COMPLETE"
    current, source_now, state_now = root_id, source, state
    if root["source_artifact_git_blob"] != source or root["workspace_state_digest"] != state:
        terminal = "UNKNOWN_STATE"
    else:
        for _ in range(max_steps):
            options = children[current]
            if not options:
                if requested_node is not None:
                    decisions_attempted += 1
                    terminal = "UNKNOWN_BRANCH"
                else:
                    terminal = "PATH_COMPLETE" if visited else "NO_OBSERVED_BRANCH"
                break
            decisions_attempted += 1
            if requested_node is not None:
                choice = requested_node
                requested_node = None
                if choice not in options:
                    terminal = "UNKNOWN_BRANCH"
                    break
            elif policy == "recorded-order":
                choice = options[0]
            else:
                choice = min(enumerate(options),
                             key=lambda pair: (PRIORITY[indexed[pair[1]]["action"]], pair[0]))[1]
            node = indexed[choice]
            if node["record_type"] != "observation":
                terminal = "UNKNOWN_BRANCH"
                break
            if node["source_artifact_git_blob"] != source_now or node["workspace_state_digest"] != state_now:
                terminal = "UNKNOWN_STATE"
                break
            proof = receipts[node["receipt_digest"]]
            if proof["test_invocations"] > budget - spent_calls:
                terminal = "BUDGET_EXHAUSTED"
                break
            spent_calls += proof["test_invocations"]
            spent_ms += proof["wall_ms"]
            visited.append(choice)
            outcomes[node["outcome"]] += 1
            source_now = node["post_source_artifact_git_blob"]
            state_now = node["post_workspace_state_digest"]
            current = choice
            if node["outcome"] == "BLOCKED":
                terminal = "RECORDED_BLOCKED"
                break
        else:
            terminal = "STEP_LIMIT" if children[current] else "PATH_COMPLETE"
    return {
        "status": "REPLAYED_RECORDED_PATH_ONLY", "policy": policy,
        "experiment_id": data["experiment_id"], "terminal_status": terminal,
        "root_node_id": root_id, "visited_node_ids": visited,
        "observed_nodes_in_tree": known, "observed_nodes_visited": len(visited),
        "unvisited_observed_nodes": known - len(visited),
        "recorded_branch_coverage": {"numerator": len(visited), "denominator": known},
        "unknown_branch_count": int(terminal == "UNKNOWN_BRANCH"),
        "unknown_state_count": int(terminal == "UNKNOWN_STATE"),
        "unknown_branch_rate": {"numerator": int(terminal == "UNKNOWN_BRANCH"),
                                "denominator": decisions_attempted},
        "test_invocations": spent_calls, "wall_ms": spent_ms,
        "max_test_invocations": budget, "observed_outcomes": outcomes,
        "evaluator_id": evaluator, "evaluation_context_id": context,
        "state_scope": "supplied-snapshot-file-not-complete-environment",
        "external_execution_authenticated": False,
        "counterfactual_outcomes_inferred": False,
        "promotion_eligible": False,
    }


def compare(data, *, budget, source, state, evaluator, context, max_steps=MAX):
    """Compare only recorded navigation, never select a winning policy."""
    result = [replay(data, policy=policy, budget=budget, source=source,
                     state=state, evaluator=evaluator, context=context,
                     max_steps=max_steps)
              for policy in POLICIES]
    return {"status": "COMPARISON_NOT_A_PROMOTION_DECISION",
            "policies": result,
            "distinct_recorded_paths": result[0]["visited_node_ids"] != result[1]["visited_node_ids"],
            "winner": None, "external_execution_authenticated": False,
            "limited_to_observed_branches": True}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, help="Existing authorized private host root")
    parser.add_argument("--experiment-id", required=True)
    parser.add_argument("--source", required=True, help="Authorized public/synthetic source file")
    parser.add_argument("--state", required=True, help="Authorized supplied snapshot file")
    parser.add_argument("--expected-evaluator", required=True)
    parser.add_argument("--expected-context", required=True)
    parser.add_argument("--budget", required=True, type=int)
    parser.add_argument("--policy", choices=POLICIES, default="recorded-order")
    parser.add_argument("--requested-node")
    parser.add_argument("--max-steps", type=int, default=MAX)
    parser.add_argument("--compare", action="store_true")
    parser.add_argument("--approved-public", action="store_true")
    args = parser.parse_args(argv)
    try:
        require(args.approved_public, "Host must establish public/synthetic clearance")
        require(not args.compare or args.requested_node is None,
                "Cannot force an unobserved node in a policy comparison")
        data = capture.inspect(args.root, args.experiment_id, export=True)
        source = capture.public_source(args.source)
        state = capture.public_snapshot(args.state)
        settings = {"budget": args.budget, "source": source, "state": state,
                    "max_steps": args.max_steps,
                    "evaluator": args.expected_evaluator,
                    "context": args.expected_context}
        result = compare(data, **settings) if args.compare else replay(
            data, policy=args.policy, requested_node=args.requested_node,
            **settings)
    except (ReplayError, capture.TraceError, OSError, UnicodeError, ValueError, TypeError) as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
