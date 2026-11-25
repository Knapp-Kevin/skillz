#!/usr/bin/env python3
"""Reconcile generated case claims with exact design, archive and host receipt.

Read-only, offline, no extraction, installation, model invocation, persistence,
or authentication of claimed observations. This is not a trial runner.
"""
import argparse
import hashlib
import json
import sys
import zipfile

import acceptance_plan as planner

a = planner.acceptance
FIELDS = {"schema_version", "plan_sha256", "receipt_sha256", "cases"}
CASE_FIELDS = {"case_id", "status", "fixture_id", "oracle_id", "evidence_id"}
CLAIMED = ("PASS_CLAIMED", "FAIL_CLAIMED")
STATUSES = CLAIMED + ("NOT_RUN", "UNKNOWN")
UNKNOWN_IDS = {"unknown", "not-run", "not_run", "none", "unset", "na", "n-a", "placeholder"}


def identity(value):
    return a.valid(a.ID, value) and value.casefold() not in UNKNOWN_IDS


def verify_members(archive, body, receipt):
    """Read bounded payloads, not just the ZIP directory or aggregate hash."""
    prefix, license_name = a.archive_contract(body["skill"], body["host"], receipt["asset"])
    expected = {prefix + m["output"]: m["output_sha256"]
                for m in body["host_member_manifest"]}
    a.require(len(expected) == len(body["host_member_manifest"]), "PLAN_MEMBER_COLLISION")
    p = a.local_file(archive, a.MAX_ARCHIVE)
    with p.open("rb") as stream:
        actual = hashlib.sha256()
        count = 0
        for data in iter(lambda: stream.read(1024 * 1024), b""):
            count += len(data)
            a.require(count <= a.MAX_ARCHIVE, "ARCHIVE_SIZE_LIMIT")
            actual.update(data)
        a.require(actual.hexdigest() == receipt["sha256"], "ARCHIVE_DIGEST_MISMATCH")
        stream.seek(0)
        a.check_archive_layout(stream, prefix, license_name)
        stream.seek(0)
        with zipfile.ZipFile(stream) as z:
            a.require(set(z.namelist()) == set(expected), "PLAN_ARCHIVE_INVENTORY_MISMATCH")
            total = 0
            for member in z.infolist():
                digest = hashlib.sha256()
                size = 0
                with z.open(member) as content:
                    for data in iter(lambda: content.read(1024 * 1024), b""):
                        size += len(data)
                        total += len(data)
                        a.require(total <= a.MAX_ARCHIVE and size <= member.file_size,
                                  "PLAN_ARCHIVE_PAYLOAD_LIMIT")
                        digest.update(data)
                a.require(size == member.file_size and digest.hexdigest() == expected[member.filename],
                          "PLAN_ARCHIVE_MEMBER_DIGEST_MISMATCH")


def aggregate(statuses):
    if "FAIL_CLAIMED" in statuses:
        return "FAIL_CLAIMED"
    if all(s == "PASS_CLAIMED" for s in statuses):
        return "PASS_CLAIMED"
    if all(s == "NOT_RUN" for s in statuses):
        return "NOT_RUN"
    return "UNKNOWN"


def reconcile(dossier, folder, manifest, manifest_sha, archive, receipt, receipt_sha, ledger, source_contract=False):
    # Regenerate the plan from actual canonical bytes; never trust a supplied
    # plan that could have removed inconvenient cases or changed their mappings.
    a.require(type(ledger) is dict and set(ledger) == FIELDS and
              type(ledger["schema_version"]) is int and ledger["schema_version"] == 1,
              "INVALID_LEDGER_FIELDS")
    native = a.validate(manifest, manifest_sha, archive, receipt)
    if source_contract:
        import source_acceptance
        regenerated = source_acceptance.plan(dossier, folder, receipt["host"])
    else:
        regenerated = planner.plan(dossier, folder, receipt["host"])
    body = regenerated["plan"]
    a.require(body["skill"] == receipt["skill"], "PLAN_SKILL_MISMATCH")
    a.require(ledger["plan_sha256"] == regenerated["plan_sha256"], "PLAN_DIGEST_MISMATCH")
    a.require(a.valid(a.HEX64, receipt_sha) and ledger["receipt_sha256"] == receipt_sha,
              "RECEIPT_DIGEST_MISMATCH")
    verify_members(archive, body, receipt)

    required = {c["id"] for c in body["cases"]}
    rows = ledger["cases"]
    a.require(type(rows) is list and len(rows) == len(required), "INCOMPLETE_CASE_LEDGER")
    by_case = {}
    evidence_ids, oracle_ids, fixture_ids = set(), set(), set()
    for row in rows:
        a.require(type(row) is dict and set(row) == CASE_FIELDS and
                  type(row["case_id"]) is str and row["case_id"] in required and
                  row["case_id"] not in by_case, "UNKNOWN_OR_DUPLICATE_CASE")
        status = row["status"]
        a.require(status in STATUSES, "INVALID_CASE_STATUS")
        fixture, oracle, evidence = (row["fixture_id"], row["oracle_id"], row["evidence_id"])
        if status in CLAIMED:
            a.require(identity(fixture) and identity(oracle) and identity(evidence),
                      "CASE_EVIDENCE_REQUIRED")
            a.require(evidence not in evidence_ids and oracle not in oracle_ids,
                      "REUSED_CASE_EVIDENCE_OR_ORACLE")
            evidence_ids.add(evidence)
            oracle_ids.add(oracle)
            fixture_ids.add(fixture)
        else:
            a.require(evidence is None, "UNOBSERVED_CASE_HAS_EVIDENCE")
            a.require((fixture is None and oracle is None) or
                      (identity(fixture) and identity(oracle)), "INCOMPLETE_CASE_PREPARATION")
            if fixture is not None:
                a.require(oracle not in oracle_ids, "REUSED_CASE_EVIDENCE_OR_ORACLE")
                fixture_ids.add(fixture)
                oracle_ids.add(oracle)
        by_case[row["case_id"]] = status
    a.require(set(by_case) == required, "INCOMPLETE_CASE_LEDGER")
    a.require(not (evidence_ids & oracle_ids or evidence_ids & fixture_ids or
                   oracle_ids & fixture_ids), "CASE_IDENTITY_ROLE_COLLISION")
    stage_ids = {c[k] for c in receipt["cases"] for k in ("evidence_id", "oracle_id")
                 if c[k] is not None}
    a.require(not stage_ids & (evidence_ids | oracle_ids | fixture_ids),
              "STAGE_EVIDENCE_REUSES_CASE_IDENTITY")
    groups = body["receipt_stage_requirements"]
    derived = {stage: aggregate([by_case[c] for c in group]) for stage, group in groups.items()}
    a.require(derived == native["stage_claims"], "STAGE_SUMMARY_CONTRADICTS_CASES")
    if receipt["execution_kind"] == "NOT_RUN":
        a.require(not any(s in CLAIMED for s in by_case.values()), "NOT_RUN_WITH_CASE_CLAIMS")
    counts = {s: sum(v == s for v in by_case.values()) for s in STATUSES}
    native.update({
        "status": ("COMPLETE_CASE_CLAIMS_REVIEW_REQUIRED"
                   if native["status"] == "COMPLETE_CLAIMS_REVIEW_REQUIRED" else native["status"]),
        "receipt_sha256": receipt_sha,
        "plan_sha256": regenerated["plan_sha256"],
        "case_ledger_reconciled": True,
        "archive_payload_crc_verified": True,
        "archive_members_match_regenerated_plan": True,
        "required_case_count": len(required),
        "case_claim_counts": counts,
        "fixture_and_oracle_contents_verified": False,
        "preregistration_time_verified": False,
        "next_action": "REVIEW_ACTUAL_PRIVATE_CASE_EVIDENCE_AND_HOST",
    })
    return native


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    route = parser.add_mutually_exclusive_group(required=True)
    route.add_argument("--design")
    route.add_argument("--source-contract")
    for name in ("package", "manifest", "archive", "receipt", "ledger"):
        parser.add_argument("--" + name, required=True)
    args = parser.parse_args(argv)
    try:
        dossier = (a.read_json(args.source_contract)[0] if args.source_contract else
                   planner.builder.read_json(args.design))
        manifest, manifest_sha = a.read_json(args.manifest)
        receipt, receipt_sha = a.read_json(args.receipt)
        ledger, ledger_sha = a.read_json(args.ledger)
        result = reconcile(dossier, args.package, manifest, manifest_sha, args.archive,
                           receipt, receipt_sha, ledger, source_contract=bool(args.source_contract))
        result["ledger_sha256"] = ledger_sha
    except (OSError, ValueError, TypeError, KeyError, RecursionError,
            zipfile.BadZipFile, RuntimeError, NotImplementedError):
        print(json.dumps({"status": "HOLD_INVALID_OR_CONTRADICTORY_CASE_LEDGER",
                          "host_execution_observed": False}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "COMPLETE_CASE_CLAIMS_REVIEW_REQUIRED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
