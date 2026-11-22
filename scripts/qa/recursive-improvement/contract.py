"""Phase-0 Skillz recursive-improvement contract. Python 3.9+, stdlib only.

Validation and observed-only replay; never executes actions, imports user profiles,
writes files, grants permission, or assumes a receipt digest proves authenticity.
A caller must independently establish trusted provenance and owner authority.
"""
from __future__ import annotations

import hashlib
import json
import re

ACTIONS = frozenset({
    "inspect", "adversarial-probe", "run-targeted-verification",
    "preservation-check", "hold", "stop-no-change",
})
BRANCH_ACTIONS = ACTIONS - {"hold", "stop-no-change"}
OUTCOMES = frozenset({"OBSERVED_PASS", "OBSERVED_FAIL", "BLOCKED"})
FAMILIES = frozenset({"schema-compatibility", "path-isolation", "ci-classification"})
ID = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
GIT_BLOB = re.compile(r"^[0-9a-f]{40}$")
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
ROOT_FIELDS = {"schema_version", "experiment_id", "evaluator_id",
               "evaluation_context_id", "nodes", "receipts"}
NODE_FIELDS = {"node_id", "parent_node_id", "record_type", "candidate_id",
               "task_family", "action", "source_artifact_git_blob",
               "workspace_state_digest", "evaluator_id",
               "evaluation_context_id"}
OBS_FIELDS = NODE_FIELDS | {"outcome", "receipt_digest", "post_workspace_state_digest",
                            "post_source_artifact_git_blob"}
RECEIPT_FIELDS = {"node_id", "outcome", "source_artifact_git_blob",
                  "workspace_state_digest", "evaluator_id", "evaluation_context_id",
                  "test_invocations", "wall_ms"}


class ContractError(ValueError):
    """Fail closed on malformed, ambiguous, or authority-expanding input."""


def _require(condition, message):
    if not condition:
        raise ContractError(message)


def _exact(obj, keys, label):
    _require(type(obj) is dict and set(obj) == keys, label + ": unexpected or missing fields")


def _id(value, label):
    _require(type(value) is str and ID.fullmatch(value) is not None,
             label + ": invalid identifier")


def _sha(value, pattern, label):
    _require(type(value) is str and pattern.fullmatch(value) is not None,
             label + ": invalid fingerprint")


def receipt_digest(payload):
    """Integrity checksum of canonical synthetic receipt data; NOT an attestation."""
    _exact(payload, RECEIPT_FIELDS, "receipt payload")
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=True, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _node(node, evaluator, context):
    _require(type(node) is dict, "node: expected object")
    kind = node.get("record_type")
    _require(kind in ("proposal", "observation"), "node: invalid record type")
    _exact(node, OBS_FIELDS if kind == "observation" else NODE_FIELDS, "node")
    for key in ("node_id", "candidate_id", "evaluator_id", "evaluation_context_id"):
        _id(node[key], key)
    _require(node["task_family"] in FAMILIES, "node: unsupported task family")
    _require(node["action"] in BRANCH_ACTIONS, "node: disallowed branch action")
    _require(node["evaluator_id"] == evaluator and
             node["evaluation_context_id"] == context, "node: evaluator/context drift")
    _sha(node["source_artifact_git_blob"], GIT_BLOB, "source blob")
    _sha(node["workspace_state_digest"], DIGEST, "workspace state")
    parent = node["parent_node_id"]
    _require(parent is None or (type(parent) is str and ID.fullmatch(parent)),
             "node: invalid parent identity")
    if kind == "observation":
        _require(node["outcome"] in OUTCOMES, "node: unobserved or fabricated outcome")
        _sha(node["receipt_digest"], DIGEST, "receipt digest")
        _sha(node["post_workspace_state_digest"], DIGEST, "post workspace state")
        _sha(node["post_source_artifact_git_blob"], GIT_BLOB, "post source blob")


def validate_trace(trace):
    """Validate a closed, single-root observation tree with verified receipt bytes.

    Receipt hashes establish internal integrity only. They do NOT establish that
    external tests ran, a human approved the action, or the agent was independent.
    """
    _exact(trace, ROOT_FIELDS, "trace")
    _require(type(trace["schema_version"]) is int and trace["schema_version"] == 1,
             "trace: unsupported schema version")
    _id(trace["experiment_id"], "experiment")
    _id(trace["evaluator_id"], "evaluator")
    _id(trace["evaluation_context_id"], "evaluation context")
    nodes, receipts = trace["nodes"], trace["receipts"]
    _require(type(nodes) is list and 1 <= len(nodes) <= 1000, "trace: invalid node count")
    _require(type(receipts) is list and len(receipts) <= 1000, "trace: invalid receipts")

    indexed = {}
    for node in nodes:
        _node(node, trace["evaluator_id"], trace["evaluation_context_id"])
        _require(node["node_id"] not in indexed, "trace: duplicate node")
        indexed[node["node_id"]] = node

    roots = [node for node in nodes if node["parent_node_id"] is None]
    _require(len(roots) == 1 and roots[0]["record_type"] == "proposal",
             "trace: exactly one proposal root required")
    _require(roots[0]["action"] == "inspect", "trace: root must inspect")
    for node in nodes:
        parent_id = node["parent_node_id"]
        if parent_id is None:
            continue
        _require(parent_id in indexed, "trace: missing parent")
        parent = indexed[parent_id]
        # Reject state/source mismatch instead of pretending two branches share
        # identical causal preconditions. A cycle also necessarily fails DFS.
        base_state = (parent["post_workspace_state_digest"] if
                      parent["record_type"] == "observation" else
                      parent["workspace_state_digest"])
        base_source = (parent["post_source_artifact_git_blob"] if
                       parent["record_type"] == "observation" else
                       parent["source_artifact_git_blob"])
        _require(node["workspace_state_digest"] == base_state and
                 node["source_artifact_git_blob"] == base_source,
                 "trace: UNKNOWN_STATE parent/child mismatch")

    visiting, visited = set(), set()

    def visit(node_id):
        _require(node_id not in visiting, "trace: cycle")
        if node_id in visited:
            return
        visiting.add(node_id)
        for child in nodes:
            if child["parent_node_id"] == node_id:
                visit(child["node_id"])
        visiting.remove(node_id)
        visited.add(node_id)

    visit(roots[0]["node_id"])
    _require(len(visited) == len(nodes), "trace: unreachable nodes")

    validated_receipts = {}
    for item in receipts:
        _exact(item, {"digest", "payload"}, "receipt")
        payload = item["payload"]
        _exact(payload, RECEIPT_FIELDS, "receipt payload")
        _id(payload["node_id"], "receipt node")
        _id(payload["evaluator_id"], "receipt evaluator")
        _id(payload["evaluation_context_id"], "receipt context")
        _sha(payload["source_artifact_git_blob"], GIT_BLOB, "receipt source")
        _sha(payload["workspace_state_digest"], DIGEST, "receipt state")
        _require(payload["outcome"] in OUTCOMES, "receipt: unsupported outcome")
        _require(type(payload["test_invocations"]) is int and
                 1 <= payload["test_invocations"] <= 1000, "receipt: invalid test count")
        _require(type(payload["wall_ms"]) is int and
                 0 <= payload["wall_ms"] <= 86_400_000, "receipt: invalid duration")
        _sha(item["digest"], DIGEST, "receipt digest")
        _require(item["digest"] == receipt_digest(payload), "receipt: corrupted digest")
        _require(item["digest"] not in validated_receipts, "receipt: duplicate digest")
        validated_receipts[item["digest"]] = payload

    used = set()
    for node in nodes:
        if node["record_type"] != "observation":
            continue
        digest = node["receipt_digest"]
        _require(digest in validated_receipts, "observation: missing receipt")
        rec = validated_receipts[digest]
        for key in ("node_id", "outcome", "source_artifact_git_blob",
                    "workspace_state_digest", "evaluator_id",
                    "evaluation_context_id"):
            _require(node[key] == rec[key], "observation: receipt binding mismatch")
        used.add(digest)
    _require(used == set(validated_receipts), "trace: unreferenced receipt")
    return indexed


def decide(trace, parent_id, policy, *, workspace_state_digest,
           source_artifact_git_blob, evaluator_id, evaluation_context_id,
           budget_remaining):
    """Inspect a policy proposal. This function NEVER executes a branch."""
    indexed = validate_trace(trace)
    _exact(policy, {"action", "selected_node_id", "max_attempts"}, "policy")
    _require(type(budget_remaining) is int and 0 <= budget_remaining <= 1000,
             "trusted budget: invalid")
    _require(type(policy["max_attempts"]) is int and
             0 <= policy["max_attempts"] <= 3, "policy: invalid attempt bound")
    action = policy["action"]
    _require(action in ACTIONS, "policy: unapproved action")
    _require(parent_id in indexed, "policy: missing parent")
    _sha(workspace_state_digest, DIGEST, "current workspace")
    _sha(source_artifact_git_blob, GIT_BLOB, "current source")
    _id(evaluator_id, "current evaluator")
    _id(evaluation_context_id, "current context")
    _require(evaluator_id == trace["evaluator_id"] and
             evaluation_context_id == trace["evaluation_context_id"],
             "policy: evaluator/context mutation forbidden")
    if action in ("hold", "stop-no-change"):
        _require(policy["selected_node_id"] is None and
                 policy["max_attempts"] == 0, "policy: stop may not run work")
        return {"status": "HOLD" if action == "hold" else "STOP_NO_CHANGE"}
    _require(policy["max_attempts"] >= 1 and
             policy["max_attempts"] <= budget_remaining, "policy: budget exceeded")
    selected = policy["selected_node_id"]
    _require(type(selected) is str and ID.fullmatch(selected),
             "policy: invalid node choice")
    node = indexed.get(selected)
    if node is None or node["parent_node_id"] != parent_id or node["action"] != action:
        return {"status": "UNKNOWN_BRANCH"}
    if node["record_type"] != "observation":
        return {"status": "UNKNOWN_BRANCH"}
    if (node["workspace_state_digest"] != workspace_state_digest or
            node["source_artifact_git_blob"] != source_artifact_git_blob):
        return {"status": "UNKNOWN_STATE"}
    return {"status": node["outcome"], "node_id": node["node_id"],
            "receipt_digest": node["receipt_digest"]}
