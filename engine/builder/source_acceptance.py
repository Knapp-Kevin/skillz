#!/usr/bin/env python3
"""Generate NOT_RUN acceptance cases for exact manually authored skill source.

The reviewer supplies explicit source anchors and cases. This is a bounded
structural check, not automatic semantic extraction, execution or validation.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import acceptance_plan as generated

a = generated.acceptance
compat = generated.compat
FIELDS = {"schema_version", "skill", "source_blobs", "cases"}
CASE_FIELDS = {"id", "kind", "source", "anchor", "setup", "expected"}
RESOURCE_FIELD = "resource_paths"
STAGES = {"load": "load", "positive": "positive_trigger",
          "near-non-trigger": "near_non_trigger", "outcome": "outcome",
          "missing-input": "outcome", "false-green": "outcome",
          "dependency-unavailable": "outcome", "authority-boundary": "authority_boundary",
          "cleanup": "cleanup", "resource": "outcome", "nested-skill": "outcome"}
MINIMUM = set(STAGES) - {"resource", "nested-skill"}


def git_blob(data):
    # Historical Git source identity, not a cryptographic trust attestation.
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data,
                        usedforsecurity=False).hexdigest()


def snapshot(folder):
    folder = Path(folder).absolute()
    files = compat.source_files(folder)
    a.require(0 < len(files) <= 10000, "SOURCE_INVENTORY_LIMIT")
    data, total = {}, 0
    for p in files:
        a.require(p.stat().st_size <= a.MAX_ARCHIVE - total, "SOURCE_SIZE_LIMIT")
        with p.open("rb") as stream:
            content = stream.read(a.MAX_ARCHIVE - total + 1)
        total += len(content)
        a.require(total <= a.MAX_ARCHIVE, "SOURCE_SIZE_LIMIT")
        data[p.relative_to(folder).as_posix()] = content
    return data


def inventory(folder):
    data = snapshot(folder)
    return {"source_blobs": {n: git_blob(v) for n, v in sorted(data.items())},
            "source_sha256": {n: hashlib.sha256(v).hexdigest() for n, v in sorted(data.items())},
            "source_identity_authenticated": False}


def plan(contract, folder, host):
    a.require(type(contract) is dict and set(contract) == FIELDS and
              type(contract["schema_version"]) is int and contract["schema_version"] == 1,
              "INVALID_SOURCE_CONTRACT")
    slug = contract["skill"]
    a.require(a.valid(a.SLUG, slug) and host in compat.HOSTS, "INVALID_SKILL_OR_HOST")
    folder = Path(folder).absolute()
    a.require(folder.name == slug, "CANONICAL_FOLDER_NAME_REQUIRED")
    data = snapshot(folder)
    pins = contract["source_blobs"]
    a.require(type(pins) is dict and set(pins) == set(data), "SOURCE_INVENTORY_MISMATCH")
    a.require(all(a.valid(a.HEX40, pin) and git_blob(data[name]) == pin
                  for name, pin in pins.items()), "SOURCE_BLOB_MISMATCH")
    source_digests = {n: hashlib.sha256(v).hexdigest() for n, v in sorted(data.items())}
    report = compat.inspect(folder, host)
    a.require(report["package_ready"], "HOST_PACKAGE_HOLD")
    a.require({m["source"]: m["sha256"] for m in report["manifest"]} == source_digests,
              "PACKAGE_CHANGED_SINCE_CONTRACT_CHECK")

    rows = contract["cases"]
    a.require(type(rows) is list and len(MINIMUM) <= len(rows) <= 128,
              "INVALID_SOURCE_CASE_COUNT")
    cases, seen, kinds, anchored_nested = [], set(), set(), set()
    nested = {name for name in data if name.endswith("/SKILL.md")}
    scripts = {name for name in data if Path(name).suffix.lower() in compat.SCRIPT_EXTENSIONS}
    covered_resources, unavailable_resources = set(), set()
    for row in rows:
        a.require(type(row) is dict and set(row) in (CASE_FIELDS, CASE_FIELDS | {RESOURCE_FIELD}),
                  "INVALID_SOURCE_CASE")
        ident, kind, source = row["id"], row["kind"], row["source"]
        a.require(a.valid(a.SLUG, ident) and len(ident) <= 80 and ident not in seen and
                  type(kind) is str and kind in STAGES, "INVALID_OR_DUPLICATE_SOURCE_CASE")
        a.require(type(source) is str and source in data and source.lower().endswith(".md"),
                  "SOURCE_ANCHOR_FILE_MISSING")
        for field in ("anchor", "setup", "expected"):
            value = row[field]
            a.require(type(value) is str and 12 <= len(value.strip()) <= 4000 and
                      not any(ord(c) < 32 and c not in "\n\r\t" for c in value),
                      "INVALID_SOURCE_CASE_TEXT")
        source_text = data[source].decode("utf-8")
        a.require(source_text.count(row["anchor"]) == 1, "SOURCE_ANCHOR_MISSING_OR_AMBIGUOUS")
        targets = row.get(RESOURCE_FIELD, [])
        if RESOURCE_FIELD in row:
            a.require(kind in ("resource", "dependency-unavailable") and
                      type(targets) is list and bool(targets) and
                      all(type(p) is str and p in data and p != "SKILL.md" for p in targets) and
                      len(targets) == len(set(targets)), "INVALID_RESOURCE_CASE_TARGETS")
        if kind == "resource":
            a.require(bool(targets), "RESOURCE_CASE_REQUIRES_EXACT_PATHS")
            covered_resources.update(targets)
        elif kind == "dependency-unavailable":
            unavailable_resources.update(targets)
        if kind == "nested-skill":
            a.require(source in nested, "NESTED_CASE_REQUIRES_ENTRYPOINT")
            anchored_nested.add(source)
        if kind in MINIMUM:
            # The core reviewed contract must be anchored in actual skill
            # instructions, not merely a favorable example or test title.
            a.require(source == "SKILL.md" or source in nested or
                      source.startswith("references/"), "CORE_CASE_REQUIRES_NORMATIVE_SOURCE")
        seen.add(ident)
        kinds.add(kind)
        cases.append({"id": ident, "kind": kind, "receipt_stage": STAGES[kind],
                      "source_anchor": {"path": source, "sha256": source_digests[source],
                                        "excerpt": row["anchor"]},
                      "setup": row["setup"], "expected_contract": row["expected"],
                      "resource_targets": [{"path": n, "sha256": source_digests[n]}
                                           for n in sorted(targets)],
                      "fixture_id": None, "independent_oracle_id": None, "status": "NOT_RUN",
                      "preparation": "CONCRETE_FIXTURE_AND_INDEPENDENT_ORACLE_REQUIRED"})
    a.require(MINIMUM <= kinds, "MISSING_REQUIRED_SOURCE_CASE_KIND")
    a.require(anchored_nested == nested, "MISSING_NESTED_ENTRYPOINT_CASE")
    a.require(scripts <= covered_resources, "SCRIPT_RESOURCE_COVERAGE_INCOMPLETE")
    a.require(scripts <= unavailable_resources, "SCRIPT_DEPENDENCY_FAILURE_COVERAGE_INCOMPLETE")
    groups = {stage: [c["id"] for c in cases if c["receipt_stage"] == stage]
              for stage in a.STAGES}
    a.require(all(groups.values()), "INVALID_PLAN_STAGE_COVERAGE")
    body = {"schema_version": 1, "status": "DESIGNED_NOT_RUN",
            "kind": "reviewed-source", "skill": slug, "host": host,
            "source_contract_sha256": generated.canonical_sha(contract),
            "canonical_files_sha256": source_digests,
            "host_member_manifest": report["manifest"],
            "host_member_manifest_sha256": generated.canonical_sha(report["manifest"]),
            "cases": cases, "receipt_stage_requirements": groups,
            "script_resource_coverage": sorted(scripts),
            "semantic_coverage_verified": False, "probes_executed": False,
            "release_identity_verified": False, "host_execution_observed": False,
            "consumer_accepted": False, "authorization_verified": False,
            "next_action": "REVIEW_FIXTURES_ORACLES_AND_BIND_RELEASE_BEFORE_AUTHORIZED_TRIAL"}
    return {"plan": body, "plan_sha256": generated.canonical_sha(body)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True)
    parser.add_argument("--inventory", action="store_true")
    parser.add_argument("--contract")
    parser.add_argument("--host", choices=sorted(compat.HOSTS))
    args = parser.parse_args(argv)
    if args.inventory:
        if args.contract or args.host:
            parser.error("--inventory is separate from --contract and --host")
    elif not args.contract or not args.host:
        parser.error("plan requires --contract and --host")
    try:
        if args.inventory:
            result = inventory(args.package)
        else:
            contract, _ = a.read_json(args.contract)
            result = plan(contract, args.package, args.host)
    except (OSError, ValueError, TypeError, KeyError, RecursionError):
        print(json.dumps({"status": "HOLD_INVALID_SOURCE_CONTRACT_OR_PACKAGE",
                          "probes_executed": False}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
