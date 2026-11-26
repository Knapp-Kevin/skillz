"""Optional normalized-session to existing design gate; never imports raw logs.

All evidence and approvals are caller claims. No extraction, inference,
semantic redaction, network, session discovery or automatic destination writes.
"""
import argparse
import hashlib
import json
import re
import sys

import design
import host_acceptance as acceptance

FORMATS = {"manual-minimized-v1", "fictional-claude-normalized-v1",
           "fictional-codex-normalized-v1"}
MAX_ROWS = 128
# Opaque locally assigned IDs, not raw host identifiers, names or paths.
TOKEN = re.compile(r"[a-z][a-z0-9-]{0,63}")
STATUSES = {"PASS_CLAIMED", "FAIL_CLAIMED", "NOT_RUN", "UNKNOWN"}


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def keys(row, fields):
    return type(row) is dict and set(row) == set(fields.split())


def ident(value):
    return type(value) is str and TOKEN.fullmatch(value) is not None and value not in {
        "unknown", "none", "unset", "placeholder", "not-run", "na", "n-a"}


def sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=False, allow_nan=False).encode("utf-8")).hexdigest()


def intake(session, dossier, authorization):
    # The declaration binds exactly these already minimized inputs. It is
    # not proof that consent, privacy review, rights or discovery occurred.
    need(keys(authorization, "schema_version scope session_sha256 dossier_sha256 custody review") and
         type(authorization["schema_version"]) is int and authorization["schema_version"] == 1 and
         authorization["scope"] == "REVIEWED_MINIMIZED_DESIGN_PREFLIGHT_ONLY" and
         authorization["custody"] in ("PRIVATE_LOCAL", "CLEARED_SYNTHETIC") and
         authorization["review"] == "CALLER_ASSERTS_MINIMIZATION_AND_ORIGINAL_CONTENT_REVIEW",
         "MINIMIZED_SCOPE_DECLARATION_REQUIRED")
    need(authorization["session_sha256"] == sha(session) and
         authorization["dossier_sha256"] == sha(dossier), "REVIEW_INPUT_DIGEST_MISMATCH")
    need(keys(session, "schema_version format complete session_id environment_id discovery requirements observations excluded") and
         type(session["schema_version"]) is int and session["schema_version"] == 1 and
         type(session["format"]) is str and session["format"] in FORMATS and
         session["complete"] is True and ident(session["session_id"]) and ident(session["environment_id"]),
         "UNSUPPORTED_OR_INCOMPLETE_NORMALIZED_SESSION")
    need(not session["format"].startswith("fictional-") or authorization["custody"] == "CLEARED_SYNTHETIC",
         "FICTIONAL_FORMAT_REQUIRES_SYNTHETIC_CUSTODY")
    discovery = session["discovery"]
    need(keys(discovery, "decision coverage review_id") and ident(discovery["review_id"]) and
         discovery["coverage"] == "CALLER_REVIEWED" and
         discovery["decision"] in ("CREATE_ORIGINAL", "COMPOSE_ORIGINAL"),
         "BOOTSTRAP_ORIGINAL_ROUTE_NOT_ESTABLISHED")
    # Validate the existing authoring contract, not another blueprint format.
    gate = design.validate(dossier)
    need(dossier["decision"] == discovery["decision"], "BOOTSTRAP_DECISION_MISMATCH")
    targets = {row["target"] for row in dossier["obligations"]}
    excluded = session["excluded"]
    need(type(excluded) is list and len(excluded) <= MAX_ROWS and
         all(type(x) is str and x in {"raw-transcript", "private-preference", "task-answer",
                                     "host-setup", "secret", "third-party-content"} for x in excluded) and
         len(excluded) == len(set(excluded)) and "raw-transcript" in excluded,
         "EXCLUSION_REVIEW_REQUIRED")
    # Chronological requirement IDs, with a single current revision per
    # target. A correction must replace the current revision, not a stale one.
    reqs = session["requirements"]
    need(type(reqs) is list and 0 < len(reqs) <= MAX_ROWS, "INVALID_REQUIREMENT_INVENTORY")
    active, known = {}, {}
    for row in reqs:
        need(keys(row, "id target supersedes") and ident(row["id"]) and
             row["id"] not in known and type(row["target"]) is str and row["target"] in targets,
             "INVALID_OR_FOREIGN_REQUIREMENT")
        target = row["target"]
        need(row["supersedes"] == active.get(target), "CORRECTION_CHAIN_MISMATCH")
        known[row["id"]] = target
        active[target] = row["id"]
    need(set(active) == targets, "MISSING_CURRENT_REQUIREMENT")
    # Evidence claims are bound to the exact requirement revision. A failed
    # current claim remains a hold even if another observation says PASS.
    observations = session["observations"]
    need(type(observations) is list and 0 < len(observations) <= MAX_ROWS,
         "INVALID_OBSERVATION_INVENTORY")
    observed, oracles = {}, set()
    for row in observations:
        need(keys(row, "id requirement_id oracle_id status") and ident(row["id"]) and
             row["id"] not in known and row["id"] not in observed and
             type(row["requirement_id"]) is str and row["requirement_id"] in known and
             type(row["status"]) is str and row["status"] in STATUSES,
             "INVALID_OR_FOREIGN_OBSERVATION")
        if row["status"] in ("PASS_CLAIMED", "FAIL_CLAIMED"):
            need(ident(row["oracle_id"]) and row["oracle_id"] not in oracles,
                 "MISSING_OR_REUSED_ORACLE")
            oracles.add(row["oracle_id"])
        else:
            need(row["oracle_id"] is None, "UNOBSERVED_ORACLE_CLAIM")
        observed[row["id"]] = row
    need(not oracles & (set(known) | set(observed)), "EVIDENCE_IDENTITY_COLLISION")
    need(not ({session["session_id"], session["environment_id"], discovery["review_id"]} &
              (set(known) | set(observed) | oracles)), "CONTEXT_IDENTITY_COLLISION")
    current = set(active.values())
    for req in current:
        statuses = {row["status"] for row in observed.values() if row["requirement_id"] == req}
        need(statuses == {"PASS_CLAIMED"}, "CURRENT_REQUIREMENT_NOT_SUPPORTED")
    evidence_ids = {e["id"] for e in dossier["evidence"]}
    # Every accepted evidence reference must come from this minimized ledger.
    # Source prose is independently authored, never copied from session rows.
    need(evidence_ids <= set(known) | set(observed), "UNBOUND_DESIGN_EVIDENCE")
    for obligation in dossier["obligations"]:
        refs = set(obligation["evidence_ids"])
        req = active[obligation["target"]]
        need(req in refs, "CURRENT_CORRECTION_NOT_MAPPED")
        need(any(ident in refs and row["requirement_id"] == req and row["status"] == "PASS_CLAIMED"
                 for ident, row in observed.items()), "CURRENT_OBSERVATION_NOT_MAPPED")
        need(not any((known.get(ref) if ref in known else known[observed[ref]["requirement_id"]])
                     != obligation["target"] for ref in refs), "CROSS_TARGET_EVIDENCE_MAPPING")
    need(set(known) <= evidence_ids and set(observed) <= evidence_ids and
         not gate["unlinked_evidence_ids"], "OMITTED_SESSION_HISTORY")
    return {"status": "NORMALIZED_EVIDENCE_LINKED_REVIEW_REQUIRED",
            "requirements": len(reqs), "current_requirements": len(current),
            "corrections": len(reqs) - len(current), "observations": len(observed),
            "historical_failures": sum(row["status"] == "FAIL_CLAIMED" for row in observed.values()),
            "authorization_verified": False, "semantic_sanitization_verified": False,
            "source_rights_verified": False, "oracle_independence_verified": False,
            "session_success_verified": False, "discovery_verified": False}


def prepare(session, dossier, authorization):
    review = intake(session, dossier, authorization)
    result = design.design_build(dossier)
    result["session_intake"] = review
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("session", "dossier", "authorization"):
        parser.add_argument("--" + name, required=True)
    args = parser.parse_args(argv)
    try:
        inputs = [acceptance.read_json(getattr(args, key))[0]
                  for key in ("session", "dossier", "authorization")]
        result = prepare(*inputs)
    except (OSError, ValueError, TypeError, KeyError, UnicodeError, RecursionError,
            design.builder.BuildHold, design.builder.check_pack.PackHold):
        # Do not echo private inputs, paths, source IDs or exception messages.
        print(json.dumps({"status": "HOLD_SESSION_DESIGN_INTAKE",
                          "session_success_verified": False}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
