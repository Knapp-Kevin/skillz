#!/usr/bin/env python3
"""Optional offline comparison bookkeeping; never executes a model or oracle."""
import hashlib
import json
import re

ARMS = ("control", "baseline", "candidate")
STATUSES = ("PASS_CLAIMED", "FAIL_CLAIMED", "NOT_RUN", "INVALID", "TIMEOUT")
OBSERVED = {"PASS_CLAIMED", "FAIL_CLAIMED", "INVALID", "TIMEOUT"}


def need(ok, code):
    if not ok:
        raise ValueError(code)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False, allow_nan=False).encode("utf-8")).hexdigest()


def hex64(value):
    return type(value) is str and bool(re.fullmatch(r"[0-9a-f]{64}", value))


def ident(value):
    return type(value) is str and bool(re.fullmatch(r"[a-z0-9][a-z0-9-]{0,95}", value))


def keys(value, expected):
    return type(value) is dict and set(value) == set(expected.split())


def plan_body(envelope):
    need(keys(envelope, "plan plan_sha256"), "INVALID_ACCEPTANCE_ENVELOPE")
    p = envelope["plan"]
    need(type(p) is dict and p.get("status") == "DESIGNED_NOT_RUN" and
         type(p.get("schema_version")) is int and p["schema_version"] == 1 and
         envelope["plan_sha256"] == digest(p), "ACCEPTANCE_PLAN_DIGEST_MISMATCH")
    need(ident(p.get("skill")) and ident(p.get("host")), "INVALID_PLAN_IDENTITY")
    files = p.get("canonical_files_sha256")
    manifest = p.get("host_member_manifest")
    need(type(files) is dict and bool(files) and all(hex64(v) for v in files.values()) and
         type(manifest) is list and bool(manifest) and
         p.get("host_member_manifest_sha256") == digest(manifest), "INVALID_PACKAGE_IDENTITY")
    cases = p.get("cases")
    need(type(cases) is list and 0 < len(cases) <= 256 and
         all(type(c) is dict and ident(c.get("id")) and c.get("status") == "NOT_RUN"
             for c in cases), "INVALID_ACCEPTANCE_CASES")
    need(len({c["id"] for c in cases}) == len(cases), "DUPLICATE_ACCEPTANCE_CASE")
    return p


def freeze(baseline, candidate, config):
    """Consume existing plan envelopes; callers must regenerate and verify them."""
    b, c = plan_body(baseline), plan_body(candidate)
    need((b["skill"], b["host"]) == (c["skill"], c["host"]), "INCOMPARABLE_PLANS")
    need(keys(config, "schema_version runtime_sha256 budget_per_trial repetitions fixtures") and
         type(config["schema_version"]) is int and config["schema_version"] == 1 and
         hex64(config["runtime_sha256"]) and type(config["budget_per_trial"]) is int and
         1 <= config["budget_per_trial"] <= 1000000 and type(config["repetitions"]) is int and
         1 <= config["repetitions"] <= 10, "INVALID_EXPERIMENT_CONFIG")
    fixtures = config["fixtures"]
    need(type(fixtures) is list and 0 < len(fixtures) <= 256, "INVALID_FIXTURE_INVENTORY")
    common = {x["id"]: x for x in b["cases"]}
    other = {x["id"]: x for x in c["cases"]}
    seen, families, fixture_partitions = set(), {}, {}
    for f in fixtures:
        need(keys(f, "case_id family partition fixture_sha256 oracle_sha256") and
             ident(f["case_id"]) and ident(f["family"]) and
             f["partition"] in ("development", "held-out") and
             hex64(f["fixture_sha256"]) and hex64(f["oracle_sha256"]), "INVALID_FIXTURE")
        k = f["case_id"]
        need(k in common and k in other and k not in seen, "UNKNOWN_OR_DUPLICATE_CASE")
        need(common[k].get("kind") == other[k].get("kind") and
             common[k].get("receipt_stage") == other[k].get("receipt_stage"), "CASE_MAPPING_CHANGED")
        need(common[k].get("kind") not in ("host-load", "load", "cleanup"), "NONCOMPARABLE_HOST_CASE")
        need(families.setdefault(f["family"], f["partition"]) == f["partition"] and
             fixture_partitions.setdefault(f["fixture_sha256"], f["partition"]) == f["partition"],
             "PARTITION_LEAKAGE")
        seen.add(k)
    need(set(families.values()) == {"development", "held-out"}, "MISSING_PARTITION")
    subjects = {"control": None, "baseline": baseline["plan_sha256"],
                "candidate": candidate["plan_sha256"]}
    need(subjects["baseline"] != subjects["candidate"], "IDENTICAL_PLAN_ARMS")
    runs = []
    for f in sorted(fixtures, key=lambda row: row["case_id"]):
        for rep in range(1, config["repetitions"] + 1):
            for arm in ARMS:
                row = {**f, "repetition": rep, "arm": arm, "subject_sha256": subjects[arm]}
                runs.append({"run_id": digest(row), **row})
    body = {"schema_version": 1, "skill": b["skill"], "host": b["host"],
            "runtime_sha256": config["runtime_sha256"], "budget_per_trial": config["budget_per_trial"],
            "subjects": subjects, "runs": runs, "status": "DESIGNED_NOT_RUN"}
    return {"experiment": body, "experiment_sha256": digest(body)}


def reconcile(baseline, candidate, config, ledger):
    """Regenerate inventory; report claims, never acceptance or causal improvement."""
    frozen = freeze(baseline, candidate, config)
    need(keys(ledger, "experiment_sha256 rows") and
         ledger["experiment_sha256"] == frozen["experiment_sha256"], "EXPERIMENT_DIGEST_MISMATCH")
    expected = {r["run_id"]: r for r in frozen["experiment"]["runs"]}
    rows = ledger["rows"]
    need(type(rows) is list and len(rows) <= len(expected), "INVALID_TRIAL_INVENTORY")
    found, evidence = {}, set()
    for row in rows:
        need(keys(row, "run_id status evidence_sha256") and hex64(row["run_id"]) and
             row["run_id"] in expected and row["run_id"] not in found and
             row["status"] in STATUSES, "UNKNOWN_DUPLICATE_OR_INVALID_TRIAL")
        e = row["evidence_sha256"]
        if row["status"] in OBSERVED:
            need(hex64(e) and e not in evidence, "MISSING_OR_REUSED_EVIDENCE")
            evidence.add(e)
        else:
            need(e is None, "NOT_RUN_WITH_EVIDENCE")
        found[row["run_id"]] = row["status"]
    groups = {p: {a: {s: 0 for s in (*STATUSES, "MISSING")} for a in ARMS}
              for p in ("development", "held-out")}
    for run_id, spec in expected.items():
        groups[spec["partition"]][spec["arm"]][found.get(run_id, "MISSING")] += 1
    complete = len(found) == len(expected) and all(s in ("PASS_CLAIMED", "FAIL_CLAIMED")
                                                    for s in found.values())
    return {"status": "COMPLETE_COMPARATIVE_CLAIMS_REVIEW_REQUIRED" if complete else "HOLD_INCOMPLETE_TRIALS",
            "experiment_sha256": frozen["experiment_sha256"], "expected_runs": len(expected),
            "submitted_runs": len(found), "counts": groups, "host_execution_verified": False,
            "evidence_authenticated": False, "consumer_accepted": False, "promotion_authorized": False}
