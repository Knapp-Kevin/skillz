#!/usr/bin/env python3
"""Conservative offline incident-evidence integrity checks, not causal attribution."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 1024 * 1024
MAX_EVENTS = 500
MAX_CLAIMS = 50
ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,95}$")
EVENT_KINDS = {"APPROVAL", "PR_MERGE_RECEIPT", "CI_RECEIPT", "DEPLOY_RECEIPT", "USER_OUTCOME_RECEIPT", "WRITE_ACTION", "TOOL_ATTEMPT", "TOOL_REFUSAL", "OTHER"}
EVIDENCE_STATES = {"OBSERVED", "ALLEGED", "MISSING"}
CLAIM_KINDS = {"MERGED", "CI_PASSED", "DEPLOYED", "USER_OUTCOME_VERIFIED"}
CLAIM_REQUIREMENTS = {"MERGED": "PR_MERGE_RECEIPT", "CI_PASSED": "CI_RECEIPT", "DEPLOYED": "DEPLOY_RECEIPT", "USER_OUTCOME_VERIFIED": "USER_OUTCOME_RECEIPT"}


class TraceError(ValueError):
    pass


def strict_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise TraceError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def nonfinite(value):
    raise TraceError(f"nonfinite constant: {value}")


def fields(obj, keys, label):
    if not isinstance(obj, dict):
        raise TraceError(f"{label}: object required")
    if obj.keys() - keys:
        raise TraceError(f"{label}: unrecognized fields: {sorted(obj.keys()-keys)}")


def ident(value, label):
    if not isinstance(value, str) or not ID.fullmatch(value):
        raise TraceError(f"{label}: invalid identifier")
    return value


def ref_list(value, label):
    if not isinstance(value, list) or len(value) > MAX_EVENTS:
        raise TraceError(f"{label}: expected bounded list")
    ids = [ident(x, label) for x in value]
    if len(set(ids)) != len(ids):
        raise TraceError(f"{label}: duplicate references")
    return ids


def bounded_str(value, label, maxlen=300):
    if not isinstance(value, str) or not value.strip() or len(value) > maxlen:
        raise TraceError(f"{label}: nonempty bounded string required")
    return value


def validate(doc):
    fields(doc, {"schema_version", "incident_id", "events", "claims", "attempt_budget", "inventory_complete"}, "root")
    if type(doc.get("schema_version")) is not int or doc["schema_version"] != 1:
        raise TraceError("schema_version must be 1")
    ident(doc.get("incident_id"), "incident_id")
    events = doc.get("events")
    if not isinstance(events, list) or not 1 <= len(events) <= MAX_EVENTS:
        raise TraceError("events: 1..500 entries required")
    claims = doc.get("claims", [])
    if not isinstance(claims, list) or len(claims) > MAX_CLAIMS:
        raise TraceError("claims: maximum 50")
    if type(doc.get("inventory_complete")) is not bool:
        raise TraceError("inventory_complete must be explicitly true or false")
    budget = doc.get("attempt_budget")
    if budget is not None and (type(budget) is not int or not 1 <= budget <= 100000):
        raise TraceError("attempt_budget: positive bounded integer required")
    observed = {}
    for i, row in enumerate(events):
        fields(row, {"id", "kind", "state", "source_ref", "after", "action_scope", "authorizes_scope", "approval_ref"}, f"events[{i}]")
        key = ident(row.get("id"), f"events[{i}].id")
        if key in observed:
            raise TraceError("duplicate event id")
        if row.get("kind") not in EVENT_KINDS or row.get("state") not in EVIDENCE_STATES:
            raise TraceError(f"event {key}: invalid kind or evidence state")
        if row.get("state") != "MISSING":
            bounded_str(row.get("source_ref"), f"event {key} source_ref", maxlen=512)
        elif row.get("source_ref") is not None:
            bounded_str(row["source_ref"], f"event {key} source_ref", maxlen=512)
        after = ref_list(row.get("after", []), f"event {key} after")
        if key in after:
            raise TraceError(f"event {key}: self-ordering edge")
        if row.get("kind") == "WRITE_ACTION":
            ident(row.get("action_scope"), "action_scope")
            if row.get("approval_ref") is not None:
                ident(row["approval_ref"], "approval_ref")
        elif row.get("approval_ref") is not None or row.get("action_scope") is not None:
            raise TraceError(f"event {key}: unexpected action-only fields")
        if row.get("kind") == "APPROVAL":
            ident(row.get("authorizes_scope"), "authorizes_scope")
        elif row.get("authorizes_scope") is not None:
            raise TraceError(f"event {key}: unexpected approval scope")
        observed[key] = dict(row, after=after)
    for event in observed.values():
        for parent in event["after"]:
            if parent not in observed:
                raise TraceError(f"unknown causal-order reference: {parent}")
    # A DAG is required. No chronological claim can be derived from timestamps alone.
    processed, ready = set(), sorted(k for k, e in observed.items() if not e["after"])
    layers = []
    while ready:
        layer = ready
        layers.append(layer)
        processed.update(layer)
        ready = sorted(k for k, e in observed.items() if k not in processed and all(p in processed for p in e["after"]))
    if len(processed) != len(observed):
        raise TraceError("causal-order cycle: no defensible ordering")
    return observed, claims, budget, layers


def audit(doc):
    events, claims, budget, layers = validate(doc)
    def ancestors(eid):
        result, queue = set(), list(events[eid]["after"])
        while queue:
            name = queue.pop()
            if name not in result:
                result.add(name)
                queue.extend(events[name]["after"])
        return result

    write_checks = []
    for e in events.values():
        if e["kind"] != "WRITE_ACTION":
            continue
        aid = e.get("approval_ref")
        authority = events.get(aid) if aid is not None else None
        valid = bool(authority and authority["kind"] == "APPROVAL" and authority["state"] == "OBSERVED"
                     and authority.get("authorizes_scope") == e["action_scope"] and aid in ancestors(e["id"]))
        write_checks.append({"event": e["id"], "status": "APPROVAL_REFERENCE_PRESENT" if valid else "AUTHORITY_NOT_ESTABLISHED"})
    claim_results, seen_claim_ids = [], set()
    for i, claim in enumerate(claims):
        fields(claim, {"id", "kind", "evidence_refs"}, f"claims[{i}]")
        cid = ident(claim.get("id"), f"claims[{i}].id")
        if cid in seen_claim_ids:
            raise TraceError("duplicate claim id")
        seen_claim_ids.add(cid)
        kind = claim.get("kind")
        if kind not in CLAIM_KINDS:
            raise TraceError(f"claim {cid}: unsupported kind")
        refs = ref_list(claim.get("evidence_refs"), f"claim {cid} evidence_refs")
        if any(r not in events for r in refs):
            raise TraceError(f"claim {cid}: nonexistent evidence reference")
        matches = [r for r in refs if events[r]["kind"] == CLAIM_REQUIREMENTS[kind] and events[r]["state"] == "OBSERVED"]
        claim_results.append({"claim": cid, "kind": kind, "status": "SUPPORTED_BY_RECORDED_INPUT" if matches else "INSUFFICIENT_RECORDED_EVIDENCE", "supporting_event_ids": matches})
    attempts = sum(e["kind"] == "TOOL_ATTEMPT" and e["state"] == "OBSERVED" for e in events.values())
    if budget is None:
        budget_status = "NO_BUDGET_PROVIDED"
    elif attempts > budget:
        budget_status = "OBSERVED_ATTEMPTS_EXCEED_RECORDED_LIMIT"
    elif doc["inventory_complete"]:
        budget_status = "WITHIN_LIMIT_IN_DECLARED_COMPLETE_INPUT"
    else:
        budget_status = "UNKNOWN_INPUT_INCOMPLETE"
    return {
        "schema_version": 1, "incident_id": doc["incident_id"],
        "evidence_authenticity_verified": False, "root_cause": "NOT_DETERMINED",
        "ordering": {"explicit_precedence_layers": layers, "note": "Only supplied after-edges establish order; timestamps not interpreted."},
        "claims": claim_results, "writes": write_checks,
        "attempt_limit": {"recorded_limit": budget, "observed_attempt_records": attempts, "status": budget_status},
        "warnings": ["This tool checks consistency of caller-supplied records, not authenticity, causality, permission ownership, or user impact."],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        # Refuse caller-selected linked roots/parents before stat/open.
        # Lexical checks are not a TOCTOU-proof sandbox for hostile roots.
        source = args.input.absolute()
        if any(part.is_symlink() for part in (source, *source.parents)):
            raise TraceError("symlinked input or ancestor")
        if source.stat().st_size > MAX_BYTES:
            raise TraceError("input exceeds 1 MiB")
        with source.open("r", encoding="utf-8") as stream:
            payload = json.load(stream, object_pairs_hook=strict_pairs, parse_constant=nonfinite)
        output = audit(payload)
    except (OSError, ValueError, UnicodeError) as error:
        print(f"INVALID_INPUT: {error}", file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
