#!/usr/bin/env python3
"""Optional offline structural audit for a portable Skillz refinement case.

This checks internal claims only. It does NOT confirm source facts, actual
model behavior, user approval, release, installation, or rights.
Python standard library; no code execution, network or mutations.
"""
import argparse
import json
from pathlib import Path
import sys

MAX_BYTES = 256 * 1024
ROUTES = {"USER_HOST", "REPOSITORY_MAINTENANCE"}
FINDINGS = {"OBSERVED_FAILURE", "STATIC_RISK", "HYPOTHESIS"}
LEVELS = {"STATIC_REVIEW", "LOCAL_TEST", "HOST_OBSERVED", "CONSUMER_ACCEPTED", "NOT_TESTED"}
DECISIONS = {"ACCEPT", "ITERATE", "HOLD", "REVERT", "STOP_NO_CHANGE"}
CHALLENGES = {"original", "near-negative", "regression", "authority", "false-green"}
KEYS = {"schema_version", "fictional", "scope", "target", "objective",
        "discovery", "finding", "candidate", "challenge", "decision", "delivery"}


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def fields(value, expected, name):
    require(type(value) is dict and set(value) == set(expected),
            "INVALID_FIELDS:" + name)


def text_field(value, name):
    require(type(value) is str and 1 <= len(value.strip()) <= 4096,
            "INVALID_TEXT:" + name)


def inspect(case):
    fields(case, KEYS, "root")
    require(type(case["schema_version"]) is int and case["schema_version"] == 1,
            "UNSUPPORTED_SCHEMA")
    require(type(case["fictional"]) is bool, "FICTIONAL_FLAG_REQUIRED")
    fields(case["scope"], ("route", "destination", "authority"), "scope")
    require(case["scope"]["route"] in ROUTES, "INVALID_ROUTE")
    for name in ("destination", "authority"):
        text_field(case["scope"][name], name)
    fields(case["target"], ("skill_id", "source_revision", "package_tree", "rights"), "target")
    for name in case["target"]:
        text_field(case["target"][name], name)
    fields(case["objective"], ("result", "pass_condition"), "objective")
    for name in case["objective"]:
        text_field(case["objective"][name], name)
    fields(case["discovery"], ("searched", "unavailable", "full_corpus_claim"), "discovery")
    for name in ("searched", "unavailable"):
        rows = case["discovery"][name]
        require(type(rows) is list and all(type(x) is str and 0 < len(x.strip()) <= 256 for x in rows),
                "INVALID_DISCOVERY:" + name)
    require(type(case["discovery"]["full_corpus_claim"]) is bool, "INVALID_DISCOVERY_CLAIM")
    # Corpus coverage can grow without a ceiling; a self-asserted "all" is not
    # evidence and must never be promoted by this checker.
    require(not case["discovery"]["full_corpus_claim"], "UNSUPPORTED_EXHAUSTIVE_CORPUS_CLAIM")
    fields(case["finding"], ("evidence", "input", "expected", "actual", "mechanism"), "finding")
    require(case["finding"]["evidence"] in FINDINGS, "INVALID_FINDING_EVIDENCE")
    for name in ("input", "expected", "actual", "mechanism"):
        text_field(case["finding"][name], name)
    fields(case["candidate"], ("change", "preserved", "source_changed"), "candidate")
    text_field(case["candidate"]["change"], "candidate.change")
    require(type(case["candidate"]["source_changed"]) is bool, "INVALID_SOURCE_CHANGE")
    require(type(case["candidate"]["preserved"]) is list and all(
        type(x) is str and x.strip() for x in case["candidate"]["preserved"]
    ), "INVALID_PROTECTED_BEHAVIOR")
    require(type(case["challenge"]) is list, "INVALID_CHALLENGES")
    names = set()
    for row in case["challenge"]:
        fields(row, ("name", "level", "result"), "challenge")
        require(row["name"] in CHALLENGES and row["name"] not in names,
                "DUPLICATE_OR_UNEXPECTED_CHALLENGE")
        names.add(row["name"])
        require(row["level"] in LEVELS, "INVALID_EVIDENCE_LEVEL")
        text_field(row["result"], "challenge.result")
        if row["level"] == "NOT_TESTED":
            require(row["result"] == "NOT_TESTED", "UNTESTED_CANNOT_CLAIM_RESULT")
    require(CHALLENGES <= names, "MISSING_ADVERSARIAL_CASE")
    fields(case["decision"], ("state", "reason", "next"), "decision")
    require(case["decision"]["state"] in DECISIONS, "INVALID_DECISION")
    for name in ("reason", "next"):
        text_field(case["decision"][name], "decision." + name)
    fields(case["delivery"],
           ("artifact", "installation", "repository_integration", "consumer_outcome"),
           "delivery")
    for name in case["delivery"]:
        text_field(case["delivery"][name], "delivery." + name)
    if case["decision"]["state"] == "ACCEPT":
        require(case["candidate"]["source_changed"] or
                case["delivery"]["artifact"] != "NOT_CREATED",
                "ACCEPT_WITHOUT_ARTIFACT")
        require(case["delivery"]["repository_integration"] != "UNMERGED"
                if case["scope"]["route"] == "REPOSITORY_MAINTENANCE" else True,
                "ACCEPT_UNMERGED_NOT_DELIVERED")
    return {
        "schema_version": 1,
        "status": "STRUCTURAL_RECEIPT_COMPLETE",
        "checks": sorted(names),
        "scope": case["scope"]["route"],
        "decision_as_supplied": case["decision"]["state"],
        "source_identity_authenticated": False,
        "behavioral_outcome_verified": False,
        "installation_or_merge_verified": False,
        "external_execution_performed": False,
        "license_authority_verified": False,
    }


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def load(path):
    p = Path(path).absolute()
    require(p.is_file() and not any(x.is_symlink() for x in (p, *p.parents))
            and p.stat().st_size <= MAX_BYTES, "MISSING_UNSAFE_OR_OVERSIZED_RECEIPT")
    with p.open(encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=no_duplicate_keys,
                         parse_constant=lambda _: (_ for _ in ()).throw(
                             Invalid("INVALID_NONFINITE_JSON")))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    args = parser.parse_args(argv)
    try:
        print(json.dumps(inspect(load(args.input)), indent=2, sort_keys=True))
        return 0
    except (Invalid, ValueError, TypeError, OSError, UnicodeError) as exc:
        print("REFINEMENT_CASE_HOLD:" + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
