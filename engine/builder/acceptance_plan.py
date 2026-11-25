#!/usr/bin/env python3
"""Derive an offline acceptance plan from an authored design and exact draft.

No generated prompts are executed, no model calls, no installs, no publication,
and no claim of semantic coverage or accepted outcomes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import design
import host_acceptance as acceptance

builder = design.builder
compat = builder.host_compat


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False, allow_nan=False).encode("utf-8")).hexdigest()


def plan(dossier, folder, host):
    design.validate(dossier)
    b = dossier["blueprint"]
    builder.need(host in compat.HOSTS, "HOST_UNASSESSED")
    folder = Path(folder).absolute()
    builder.need(folder.name == b["name"], "CANONICAL_FOLDER_NAME_REQUIRED")
    expected = builder.generate_files(b)
    actual = {p.relative_to(folder).as_posix(): p for p in compat.source_files(folder)}
    builder.need(set(actual) == set(expected), "PACKAGE_INVENTORY_MISMATCH")
    for name, content in expected.items():
        builder.need(actual[name].read_bytes() == content.encode("utf-8"),
                     "PACKAGE_BYTES_DIFFER_FROM_DESIGN")
    builder.verify_layout(folder, b, expected)
    report = compat.inspect(folder, host)
    builder.need(report["package_ready"], "HOST_PACKAGE_HOLD")
    source_digests = {n: hashlib.sha256(v.encode("utf-8")).hexdigest()
                      for n, v in sorted(expected.items())}
    builder.need({m["source"]: m["sha256"] for m in report["manifest"]} == source_digests,
                 "PACKAGE_CHANGED_SINCE_DESIGN_CHECK")

    obligations = {o["id"]: o for o in dossier["obligations"]}
    probes = {p["kind"]: p for p in dossier["probes"]}
    cases = []

    def add(ident, kind, stage, setup, oracle, refs=(), probe=None):
        cases.append({
            "id": ident, "kind": kind, "receipt_stage": stage,
            "setup": setup, "expected_contract": oracle,
            "obligations": sorted(refs), "design_probe_id": probe,
            "fixture_id": None, "independent_oracle_id": None,
            "status": "NOT_RUN",
            "preparation": "CONCRETE_FIXTURE_AND_INDEPENDENT_ORACLE_REQUIRED",
        })

    def target_refs(*targets):
        return [oid for oid, o in obligations.items() if o["target"] in targets]

    add("host-load", "host-load", "load",
        "Use a separately authorized clean native environment and exact selected distribution.",
        "Observe host-native discovery and correct resource access for the exact skill; self-report is insufficient.")
    positive = probes["positive"]
    add("positive-activation", "positive", "positive_trigger",
        positive["input"], b["trigger"], target_refs("trigger"), positive["id"])
    add("positive-outcome", "positive", "outcome", positive["input"],
        {"outcome": b["outcome"], "verification": b["verification"]},
        positive["obligation_ids"], positive["id"])

    mapping = {"near-non-trigger": ("near_non_trigger", ("non_trigger",)),
               "missing-input": ("outcome", ("inputs", "failure_handling")),
               "authority-boundary": ("authority_boundary", ("authority",)),
               "false-green": ("outcome", ("verification",)),
               "pack-handoff": ("outcome", ()),
               "optional-fallback": ("outcome", ())}
    for kind, (stage, fields) in mapping.items():
        if kind not in probes:
            continue
        p = probes[kind]
        add("probe-" + kind, kind, stage, p["input"],
            {"expected": p["expected"], "contract": {k: b[k] for k in fields}},
            p["obligation_ids"], p["id"])

    if b["kind"] == "pack":
        for m in b["modules"]:
            ref = target_refs("modules." + m["id"])
            add("module-" + m["id"] + "-output", "module-output", "outcome",
                {"module": m["id"], "requires": m["requires"], "output": m["output"]},
                {"output": m["output"], "authority": m["authority"]}, ref)
            if m["required"]:
                add("module-" + m["id"] + "-missing", "required-handoff-missing", "outcome",
                    {"withhold": m["id"], "requires": m["requires"]},
                    {"expected": "HOLD_IF_MISSING", "verification": b["verification"]}, ref)
            else:
                add("module-" + m["id"] + "-fallback", "optional-module-unavailable", "outcome",
                    {"withhold": m["id"], "requires": m["requires"]},
                    {"expected": "FALLBACK_NO_LOST_OBLIGATION", "fallback": m["fallback"],
                     "verification": b["verification"]}, ref)
    else:
        for step in b["steps"]:
            ref = target_refs("steps." + step["id"])
            add("step-" + step["id"] + "-output", "step-output", "outcome",
                {"step": step["id"], "instructions": step["instructions"]},
                {"output": step["output"], "verification": b["verification"]}, ref)
            add("step-" + step["id"] + "-missing", "required-step-output-missing", "outcome",
                {"withhold": step["id"], "output": step["output"]},
                {"expected": "HOLD_IF_MISSING", "failure_handling": b["failure_handling"]}, ref)
    add("host-cleanup", "cleanup", "cleanup",
        "Restore the approved isolated test scope using its predeclared reset method.",
        "Independently confirm the baseline is restored or explicitly hold cleanup.")
    groups = {stage: [c["id"] for c in cases if c["receipt_stage"] == stage]
              for stage in acceptance.STAGES}
    builder.need(all(groups.values()) and len({c["id"] for c in cases}) == len(cases),
                 "INVALID_PLAN_STAGE_COVERAGE")
    builder.need(set(obligations) == {oid for c in cases for oid in c["obligations"]},
                 "UNCOVERED_PLAN_OBLIGATIONS")
    body = {"schema_version": 1, "status": "DESIGNED_NOT_RUN",
            "skill": b["name"], "host": host, "kind": b["kind"],
            "dossier_sha256": canonical_sha(dossier),
            "canonical_files_sha256": source_digests,
            "host_member_manifest": report["manifest"],
            "host_member_manifest_sha256": canonical_sha(report["manifest"]),
            "obligations": [{"id": o["id"], "target": o["target"], "statement": o["statement"]}
                            for o in dossier["obligations"]],
            "cases": cases, "receipt_stage_requirements": groups,
            "semantic_coverage_verified": False, "probes_executed": False,
            "release_identity_verified": False, "host_execution_observed": False,
            "consumer_accepted": False, "authorization_verified": False,
            "next_action": "REVIEW_FIXTURES_ORACLES_AND_BIND_RELEASE_BEFORE_AUTHORIZED_TRIAL"}
    return {"plan": body, "plan_sha256": canonical_sha(body)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--design", required=True)
    ap.add_argument("--package", required=True)
    ap.add_argument("--host", required=True, choices=sorted(compat.HOSTS))
    args = ap.parse_args(argv)
    try:
        result = plan(builder.read_json(args.design), args.package, args.host)
    except (OSError, ValueError, TypeError, KeyError, RecursionError):
        # Do not echo private input text or filesystem paths.
        print(json.dumps({"status": "HOLD_INVALID_DESIGN_OR_PACKAGE",
                          "probes_executed": False}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
