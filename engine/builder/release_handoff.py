#!/usr/bin/env python3
"""Prepare unexecuted source acceptance from actual local distribution bytes.

No extraction, install, model calls, network, writes or authenticity claims.
The receipt and ledger strings are exact UTF-8 JSON payloads, not observations.
"""
import argparse
import hashlib
import json
import sys

import acceptance_ledger as ledger
import source_acceptance as source

a = ledger.a


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False)


def prepare(contract, folder, manifest_path, archive, host):
    manifest, manifest_sha = a.read_json(manifest_path)
    plan = source.plan(contract, folder, host)
    slug = plan["plan"]["skill"]
    a.require(type(manifest) is dict and type(manifest.get("skills")) is list,
              "INVALID_MANIFEST")
    matches = [row for row in manifest["skills"]
               if type(row) is dict and row.get("id") == slug]
    a.require(len(matches) == 1, "SKILL_MISSING_OR_DUPLICATE")
    row = matches[0]
    profiles = row.get("hosts")
    a.require(type(profiles) is dict and type(profiles.get(host)) is dict,
              "HOST_UNASSESSED")
    profile = profiles[host]
    a.require(profile.get("status") == "PACKAGE_READY" and profile.get("blockers") == [],
              "HOST_PACKAGE_HOLD")
    receipt = {
        "schema_version": 1, "skill": slug, "host": host,
        "source_commit": manifest.get("source_commit"),
        "package_tree_sha": row.get("package_tree_sha"),
        "asset": profile.get("asset"), "sha256": profile.get("sha256"),
        "manifest_sha256": manifest_sha,
        "environment": {key: "UNKNOWN" for key in a.ENV_FIELDS},
        "execution_kind": "NOT_RUN", "authorization": "NOT_ESTABLISHED",
        "cases": [{"stage": stage, "status": "NOT_RUN", "evidence_id": None,
                   "oracle_id": None} for stage in a.STAGES],
    }
    receipt_json = canonical_json(receipt)
    receipt_sha = hashlib.sha256(receipt_json.encode("utf-8")).hexdigest()
    cases = {"schema_version": 1, "plan_sha256": plan["plan_sha256"],
             "receipt_sha256": receipt_sha,
             "cases": [{"case_id": case["id"], "status": "NOT_RUN", "fixture_id": None,
                        "oracle_id": None, "evidence_id": None}
                       for case in plan["plan"]["cases"]]}
    result = ledger.reconcile(contract, folder, manifest, manifest_sha, archive,
                              receipt, receipt_sha, cases, source_contract=True)
    a.require(result["status"] == "HOLD_INCOMPLETE_NATIVE_CLAIM",
              "UNEXPECTED_HANDOFF_STATUS")
    return {"status": "LOCAL_RELEASE_BYTES_BOUND_DESIGNED_NOT_RUN",
            "plan": plan, "receipt_json": receipt_json, "ledger_json": canonical_json(cases),
            "validation": result, "trial_execution_authorized": False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ("contract", "package", "manifest", "archive", "host"):
        parser.add_argument("--" + key, required=True)
    args = parser.parse_args(argv)
    try:
        contract, _ = a.read_json(args.contract)
        result = prepare(contract, args.package, args.manifest, args.archive, args.host)
    except (OSError, ValueError, TypeError, KeyError, RecursionError, RuntimeError):
        print(json.dumps({"status": "HOLD_INVALID_RELEASE_HANDOFF",
                          "host_execution_observed": False}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
