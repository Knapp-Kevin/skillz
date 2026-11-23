#!/usr/bin/env python3
"""Audit declared multi-turn task state without executing work or trusting receipts.

A bounded, offline structural guard for a *provided* before/after checkpoint.
No memory, GitHub, agent-host authority, authentication or test execution.
Python >=3.9, standard library only.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 1_048_576
ID = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]{0,79}$")
SHA = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64}|UNKNOWN)$")
STATES = {"remaining", "current", "blocked", "completed"}
PROOFS = {"host_receipt", "local_test", "user_acceptance", "analysis_evidence"}
CHANGE = {"continue", "user_scope_change_declared"}


class Hold(ValueError):
    pass


def need(ok, reason):
    if not ok:
        raise Hold(reason)


def keys(obj, required, optional=(), label="record"):
    need(isinstance(obj, dict), label + ": object required")
    need(set(required).issubset(obj), label + ": required fields absent")
    need(not (set(obj) - set(required) - set(optional)),
         label + ": unexpected fields")


def atom(value, label, size=1000):
    need(isinstance(value, str) and 0 < len(value.strip()) <= size,
         label + ": nonempty bounded text required")
    return value


def identifier(value, label):
    need(isinstance(value, str) and ID.fullmatch(value) is not None,
         label + ": invalid ID")
    return value


def unique(items, label, maximum=128):
    need(isinstance(items, list) and len(items) <= maximum,
         label + ": bounded list required")
    need(len(set(items)) == len(items), label + ": duplicate identity")
    return items


def checkpoint(value):
    keys(value, ("schema_version", "workstream_id", "revision", "objective",
                 "source_revision", "permission_scope", "guardrails",
                 "decisions", "obligations", "next_action", "claimed_complete",
                 "context_gap"), label="checkpoint")
    need(type(value["schema_version"]) is int and value["schema_version"] == 1,
         "unsupported checkpoint schema")
    identifier(value["workstream_id"], "workstream")
    need(type(value["revision"]) is int and 1 <= value["revision"] < 1_000_000,
         "invalid revision counter")
    atom(value["objective"], "objective")
    need(isinstance(value["source_revision"], str) and
         SHA.fullmatch(value["source_revision"]) is not None,
         "source revision must be full hash or UNKNOWN")
    perms = unique(value["permission_scope"], "permission_scope", 32)
    for permission in perms:
        identifier(permission, "permission")
    guardrails = value["guardrails"]
    need(isinstance(guardrails, list) and 1 <= len(guardrails) <= 64,
         "at least one bounded guardrail required")
    guardmap = {}
    for g in guardrails:
        keys(g, ("id", "text"), label="guardrail")
        key = identifier(g["id"], "guardrail ID")
        need(key not in guardmap, "duplicated guardrail")
        guardmap[key] = atom(g["text"], "guardrail text")
    decisions = value["decisions"]
    need(isinstance(decisions, list) and len(decisions) <= 128,
         "bounded decision list required")
    decisionmap = {}
    for d in decisions:
        keys(d, ("id", "text", "authority_ref"), label="decision")
        key = identifier(d["id"], "decision ID")
        need(key not in decisionmap, "duplicated decision")
        decisionmap[key] = (atom(d["text"], "decision text"),
                            atom(d["authority_ref"], "decision authority"))
    obligations = value["obligations"]
    need(isinstance(obligations, list) and 1 <= len(obligations) <= 128,
         "nonempty bounded obligations required")
    workmap = {}
    for o in obligations:
        keys(o, ("id", "criterion", "acceptance_kind", "state", "proof"),
             ("reopened_reason", "unblocked_ref"), label="obligation")
        key = identifier(o["id"], "obligation ID")
        need(key not in workmap, "duplicated obligation ID")
        atom(o["criterion"], "criterion")
        need(o["acceptance_kind"] in PROOFS, "unsupported acceptance category")
        need(o["state"] in STATES, "unsupported obligation state")
        proof = o["proof"]
        if o["state"] == "completed":
            keys(proof, ("kind", "ref", "source_revision"), label="completion proof")
            need(proof["kind"] == o["acceptance_kind"],
                 "PROOF_CATEGORY_MISMATCH:" + key)
            atom(proof["ref"], "proof reference", 250)
            need(proof["source_revision"] == value["source_revision"] and
                 value["source_revision"] != "UNKNOWN",
                 "STALE_OR_UNKNOWN_PROOF_REVISION:" + key)
        else:
            need(proof is None, "UNQUALIFIED_PROOF_ON_OPEN_OBLIGATION:" + key)
        if "reopened_reason" in o:
            atom(o["reopened_reason"], "reopen reason")
        if "unblocked_ref" in o:
            atom(o["unblocked_ref"], "unblocked reference")
        workmap[key] = o
    need(type(value["claimed_complete"]) is bool and
         type(value["context_gap"]) is bool,
         "boolean completion and context fields required")
    if value["claimed_complete"]:
        need(not value["context_gap"], "CONTEXT_GAP_CANNOT_CLAIM_COMPLETE")
        need(all(o["state"] == "completed" for o in obligations),
             "OPEN_OBLIGATIONS_CANNOT_CLAIM_COMPLETE")
        need(value["next_action"] is None,
             "COMPLETED_TASK_HAS_PENDING_NEXT_ACTION")
    else:
        action = value["next_action"]
        need(action is None or
             (action in workmap and workmap[action]["state"] in {"remaining", "current"}),
             "NEXT_ACTION_NOT_EXECUTABLE")
        if any(o["state"] in {"remaining", "current"} for o in obligations):
            need(action is not None, "EXECUTABLE_OBLIGATION_WITHOUT_NEXT_ACTION")
    return {"guardrails": guardmap, "decisions": decisionmap, "work": workmap,
            "permissions": set(perms)}


def reconcile(previous, updated, transition):
    """Reconcile supplied snapshots; NEVER authenticate their evidence or actor."""
    before = checkpoint(previous)
    after = checkpoint(updated)
    keys(transition, ("change_type", "change_ref"), label="transition")
    need(transition["change_type"] in CHANGE, "unknown change kind")
    if transition["change_type"] == "user_scope_change_declared":
        atom(transition["change_ref"], "declared change source")
        return {"schema_version": 1, "status": "HOLD",
                "issues": ["USER_SCOPE_CHANGE_REQUIRES_INDEPENDENT_HOST_AUTHORIZATION"],
                "claimed_workstream": updated["workstream_id"],
                "source_and_proofs_authenticated": False,
                "model_agent_behavior_observed": False,
                "automatic_side_effect_authorized": False}
    need(transition["change_ref"] is None, "UNEXPECTED_SCOPE_CHANGE_RECEIPT")
    need(previous["workstream_id"] == updated["workstream_id"],
         "WORKSTREAM_ID_CHANGED")
    need(updated["revision"] == previous["revision"] + 1,
         "NON_SEQUENTIAL_CONTINUATION")
    need(previous["objective"] == updated["objective"],
         "SILENT_OBJECTIVE_CHANGE")
    need(before["permissions"] == after["permissions"],
         "PERMISSION_SCOPE_DRIFT")
    need(before["guardrails"] == after["guardrails"],
         "PROTECTED_GUARDRAIL_DRIFT")
    for key, decision in before["decisions"].items():
        need(after["decisions"].get(key) == decision,
             "DECISION_DROPPED_OR_REWRITTEN:" + key)
    changes = []
    for key, old in before["work"].items():
        new = after["work"].get(key)
        need(new is not None, "DROPPED_UNFINISHED_OR_PROTECTED_OBLIGATION:" + key)
        need(new["criterion"] == old["criterion"] and
             new["acceptance_kind"] == old["acceptance_kind"],
             "ACCEPTANCE_GATE_REWRITTEN:" + key)
        if old["state"] == "completed" and new["state"] != "completed":
            need("reopened_reason" in new, "REOPENED_WITHOUT_REASON:" + key)
        if old["state"] == "blocked" and new["state"] != "blocked":
            need("unblocked_ref" in new, "UNBLOCKED_WITHOUT_EVIDENCE:" + key)
        if old["state"] != new["state"]:
            changes.append(key)
    # Proofs are structural claims from the caller, not independently
    # authenticated; a moved revision cannot silently keep stale proof.
    if previous["source_revision"] != updated["source_revision"]:
        for key, old in before["work"].items():
            new = after["work"][key]
            if old["state"] == "completed" and new["state"] == "completed":
                need(old["proof"] != new["proof"],
                     "SOURCE_CHANGED_BUT_OLD_PROOF_REUSED:" + key)
    return {"schema_version": 1, "status": "STATIC_TRANSITION_RECONCILED",
            "claimed_workstream": updated["workstream_id"],
            "previous_revision": previous["revision"],
            "current_revision": updated["revision"],
            "carried_obligations": len(before["work"]),
            "new_obligations": len(after["work"]) - len(before["work"]),
            "changed_obligation_ids": sorted(changes),
            "claimed_complete": updated["claimed_complete"],
            "source_and_proofs_authenticated": False,
            "model_agent_behavior_observed": False,
            "user_authorization_authenticated": False,
            "host_test_execution_verified": False,
            "provider_or_merge_outcome_verified": False,
            "automatic_side_effect_authorized": False,
            "scope": "CALLER_SUPPLIED_SNAPSHOT_STRUCTURAL_RECONCILIATION_ONLY"}


def read_json(path):
    src = Path(path).absolute()
    need(src.is_file() and not any(p.is_symlink() for p in (src, *src.parents)),
         "input missing or symlinked")
    need(src.stat().st_size <= MAX_BYTES, "input too large")
    with src.open(encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=no_dupes,
                         parse_constant=lambda _: (_ for _ in ()).throw(Hold("nonfinite JSON")))


def no_dupes(pairs):
    out = {}
    for k, v in pairs:
        need(k not in out, "duplicate JSON key")
        out[k] = v
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous", required=True)
    parser.add_argument("--updated", required=True)
    parser.add_argument("--transition", required=True)
    parser.add_argument("--require-pass", action="store_true")
    args = parser.parse_args()
    try:
        outcome = reconcile(read_json(args.previous),
                            read_json(args.updated),
                            read_json(args.transition))
        print(json.dumps(outcome, sort_keys=True))
        return (3 if args.require_pass and outcome["status"] !=
                "STATIC_TRANSITION_RECONCILED" else 0)
    except (Hold, TypeError, KeyError, ValueError, OSError, UnicodeError) as exc:
        print("CONTINUATION_HOLD: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
