#!/usr/bin/env python3
"""Optional author-supplied evidence-to-blueprint gate for the Skillz builder.

No discovery, semantic inference, network access, source reuse, consumer
execution, consent recording or rights authentication occurs here.
The only output artifact is produced by the existing safe builder.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import build as builder

DOSSIER_FIELDS = {
    "schema_version", "case_id", "decision", "rationale",
    "evidence", "obligations", "probes", "blueprint",
}
EVIDENCE_FIELDS = {
    "id", "kind", "source_identity", "observation",
    "review_level", "reuse_scope",
}
OBLIGATION_FIELDS = {
    "id", "statement", "evidence_ids", "target",
}
PROBE_FIELDS = {"id", "kind", "input", "expected", "obligation_ids"}
CORE_TARGETS = {
    "outcome", "trigger", "non_trigger", "inputs",
    "verification", "failure_handling", "authority",
}
PROBE_EXPECTATIONS = {
    "positive": "COMPLETE_IF_VERIFIED",
    "near-non-trigger": "DECLINE",
    "missing-input": "HOLD",
    "authority-boundary": "HOLD",
    "false-green": "HOLD",
    "pack-handoff": "HOLD_IF_MISSING",
    "optional-fallback": "FALLBACK_NO_LOST_OBLIGATION",
}
REVIEW_LEVELS = {"stated", "author-reviewed", "host-observed-claimed"}
EVIDENCE_KINDS = {"user-task", "corpus-reference", "evaluation"}
DECISIONS = {"CREATE_ORIGINAL", "COMPOSE_ORIGINAL"}


def hold(condition, reason):
    builder.need(condition, reason)


def unique_id(value, label):
    builder.slug(value, label)


def nonempty_ids(items, known, label):
    hold(type(items) is list and bool(items) and
         all(type(i) is str and i in known for i in items) and
         len(items) == len(set(items)), "INVALID_REFERENCES:" + label)


def validate(dossier):
    """Validate link closure, not the truth of any authored evidence or task."""
    builder.fields(dossier, DOSSIER_FIELDS, "design-dossier")
    hold(type(dossier["schema_version"]) is int and
         dossier["schema_version"] == 1, "UNSUPPORTED_DESIGN_SCHEMA")
    unique_id(dossier["case_id"], "case_id")
    hold(type(dossier["decision"]) is str and
         dossier["decision"] in DECISIONS, "UNSUPPORTED_DESIGN_DECISION")
    builder.prose(dossier["rationale"], "design.rationale", 20)
    b = dossier["blueprint"]
    builder.validate_blueprint(b)
    is_pack = b["kind"] == "pack"
    hold((dossier["decision"] == "COMPOSE_ORIGINAL") == is_pack,
         "DECISION_BLUEPRINT_SHAPE_MISMATCH")

    evidence = dossier["evidence"]
    hold(type(evidence) is list and 1 <= len(evidence) <= 64,
         "DESIGN_EVIDENCE_COUNT")
    evidence_ids = set()
    for entry in evidence:
        builder.fields(entry, EVIDENCE_FIELDS, "evidence")
        unique_id(entry["id"], "evidence.id")
        hold(entry["id"] not in evidence_ids, "DUPLICATE_EVIDENCE_ID")
        evidence_ids.add(entry["id"])
        hold(type(entry["kind"]) is str and
             entry["kind"] in EVIDENCE_KINDS, "INVALID_EVIDENCE_KIND")
        builder.prose(entry["source_identity"], "evidence.source_identity", 6, 2000)
        builder.prose(entry["observation"], "evidence.observation", 12)
        hold(type(entry["review_level"]) is str and
             entry["review_level"] in REVIEW_LEVELS, "INVALID_REVIEW_LEVEL")
        hold(entry["reuse_scope"] == "design-reference-only",
             "SOURCE_REUSE_NOT_AUTHORIZED")
        # The claimed review level is never upgraded to an authenticated
        # observation, copyright entitlement or consumer execution.

    obligations = dossier["obligations"]
    required_targets = set(CORE_TARGETS)
    required_targets.update(
        ("modules." + m["id"] for m in b["modules"]) if is_pack else
        ("steps." + s["id"] for s in b["steps"])
    )
    hold(type(obligations) is list and
         1 <= len(obligations) <= 128,
         "DESIGN_OBLIGATION_COUNT")
    obligation_ids = set()
    targets = set()
    linked_evidence = set()
    target_by_id = {}
    for entry in obligations:
        builder.fields(entry, OBLIGATION_FIELDS, "obligation")
        unique_id(entry["id"], "obligation.id")
        hold(entry["id"] not in obligation_ids, "DUPLICATE_OBLIGATION_ID")
        obligation_ids.add(entry["id"])
        builder.prose(entry["statement"], "obligation.statement", 12)
        target = entry["target"]
        hold(type(target) is str and target in required_targets,
             "UNKNOWN_OBLIGATION_TARGET")
        targets.add(target)
        target_by_id[entry["id"]] = target
        nonempty_ids(entry["evidence_ids"], evidence_ids, "obligation.evidence_ids")
        linked_evidence.update(entry["evidence_ids"])
    hold(targets == required_targets,
         "UNCOVERED_BLUEPRINT_TARGETS:" +
         ",".join(sorted(required_targets - targets)))

    probes = dossier["probes"]
    hold(type(probes) is list and 1 <= len(probes) <= 64,
         "DESIGN_PROBE_COUNT")
    probe_kinds = set()
    probe_ids = set()
    probed_obligations = set()
    targets_by_kind = {}
    for probe in probes:
        builder.fields(probe, PROBE_FIELDS, "probe")
        unique_id(probe["id"], "probe.id")
        hold(probe["id"] not in probe_ids, "DUPLICATE_PROBE_ID")
        probe_ids.add(probe["id"])
        kind = probe["kind"]
        hold(type(kind) is str and kind in PROBE_EXPECTATIONS,
             "UNKNOWN_PROBE_KIND")
        hold(kind not in probe_kinds, "DUPLICATE_PROBE_KIND")
        probe_kinds.add(kind)
        hold(probe["expected"] == PROBE_EXPECTATIONS[kind],
             "UNSAFE_OR_FALSE_GREEN_PROBE_EXPECTATION")
        builder.prose(probe["input"], "probe.input", 16)
        nonempty_ids(probe["obligation_ids"], obligation_ids,
                     "probe.obligation_ids")
        probed_obligations.update(probe["obligation_ids"])
        targets_by_kind[kind] = {
            target_by_id[i] for i in probe["obligation_ids"]
        }

    minimum = {
        "positive", "near-non-trigger", "missing-input",
        "authority-boundary", "false-green",
    }
    if is_pack:
        minimum.add("pack-handoff")
    optional = {
        "modules." + m["id"] for m in b["modules"] if not m["required"]
    }
    if optional:
        minimum.add("optional-fallback")
    hold(minimum.issubset(probe_kinds),
         "MISSING_ADVERSARIAL_PROBES:" +
         ",".join(sorted(minimum - probe_kinds)))
    hold({"outcome", "trigger", "verification"}.issubset(
         targets_by_kind["positive"]), "POSITIVE_MISSING_OUTCOME_CHECK")
    hold("non_trigger" in targets_by_kind["near-non-trigger"],
         "NEGATIVE_MISSING_NON_TRIGGER")
    hold(bool({"inputs", "failure_handling"} &
              targets_by_kind["missing-input"]), "MISSING_INPUT_UNCOVERED")
    hold("authority" in targets_by_kind["authority-boundary"],
         "AUTHORITY_PROBE_UNCOVERED")
    hold("verification" in targets_by_kind["false-green"],
         "FALSE_GREEN_NOT_TIED_TO_COMPLETION")
    if is_pack:
        hold(bool(targets_by_kind["pack-handoff"] &
                  {t for t in required_targets if t.startswith("modules.")}),
             "HANDOFF_PROBE_UNCOVERED")
    if optional:
        hold(bool(targets_by_kind["optional-fallback"] & optional),
             "OPTIONAL_FALLBACK_UNCOVERED")
    hold(obligation_ids == probed_obligations,
         "UNTESTED_OBLIGATIONS:" +
         ",".join(sorted(obligation_ids - probed_obligations)))

    return {
        "status": "TRACE_LINKS_PRESENT_NOT_BEHAVIOR_VALIDATED",
        "case_id": dossier["case_id"],
        "decision": dossier["decision"],
        "evidence_items": len(evidence),
        "linked_evidence_items": len(linked_evidence),
        "unlinked_evidence_ids": sorted(evidence_ids - linked_evidence),
        "mapped_obligations": len(obligations),
        "planned_adversarial_probes": sorted(probe_kinds),
        "probes_executed": False,
        "source_identity_authenticated": False,
        "source_reuse_or_derivative_rights_authenticated": False,
        "semantic_coverage_verified": False,
        "independent_consumer_acceptance": False,
    }


def design_build(dossier, output=None, write=False, maintainer=False, hosts=None):
    report = validate(dossier)
    receipt = builder.build(dossier["blueprint"], output, write, maintainer, hosts=hosts)
    fingerprint = json.dumps(dossier, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False).encode("utf-8")
    receipt["design_gate"] = report
    receipt["design_gate"]["dossier_sha256"] = hashlib.sha256(
        fingerprint).hexdigest()
    return receipt


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True,
                        help="Authored design dossier (not source instructions)")
    parser.add_argument("--output")
    parser.add_argument("--host", action="append", choices=sorted(builder.host_compat.HOSTS),
                        help="Repeat for each target; default checks all configured profiles")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--repository-maintenance", action="store_true")
    args = parser.parse_args(argv)
    try:
        hold(not args.repository_maintenance or args.write,
             "MAINTENANCE_FLAG_WITHOUT_WRITE")
        result = design_build(builder.read_json(args.input), args.output,
                              args.write, args.repository_maintenance, hosts=args.host)
        print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
        return 0
    except (builder.BuildHold, builder.check_pack.PackHold, OSError,
            ValueError, TypeError, UnicodeError, KeyError) as exc:
        print("SKILL_DESIGN_HOLD: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
