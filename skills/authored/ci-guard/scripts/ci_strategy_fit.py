#!/usr/bin/env python3
"""CI Guard optional, read-only strategy-fit preflight.

Evaluates declared alternatives. Does not authenticate inputs or qualify CI.
"""
import argparse
import json
import math
import sys
from pathlib import Path

MAX_BYTES = 1024 * 1024
KINDS = {"full", "stage", "coarse", "dependency", "execution"}
EVIDENCE = {"observed", "estimated", "unknown"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def bounded_name(value, label):
    require(isinstance(value, str) and 0 < len(value) <= 120 and value.strip() == value,
            label + " must be a nonempty bounded string")
    return value


def nonnegative(value, label):
    require(type(value) in (int, float) and math.isfinite(value) and value >= 0,
            label + " must be a finite nonnegative number")
    return float(value)


def unique_object(pairs):
    value = {}
    for key, obj in pairs:
        require(key not in value, "duplicate JSON key: " + key)
        value[key] = obj
    return value


def load(path):
    p = Path(path).absolute()
    require(not any(q.is_symlink() for q in (p, *p.parents)), "symlink input refused")
    require(p.stat().st_size <= MAX_BYTES, "input too large")
    with p.open(encoding="utf-8") as fh:
        return json.load(fh, object_pairs_hook=unique_object,
                         parse_constant=lambda x: (_ for _ in ()).throw(ValueError("nonfinite JSON")))


def evaluate(data):
    """Return a bounded advisory comparison. No method is implicitly safe."""
    require(isinstance(data, dict) and type(data.get("schema_version")) is int and data["schema_version"] == 1,
            "strategy-fit schema_version must be 1")
    require(set(data) == {"schema_version", "revision", "objective", "baseline", "alternatives"},
            "unexpected or missing top-level key")
    revision = bounded_name(data["revision"], "revision")
    require(revision != "UNKNOWN", "revision must be source-pinned")
    objective = data["objective"]
    require(isinstance(objective, dict) and set(objective) == {
        "name", "comparison_horizon_runs", "graph_min_saved_runner_hours_per_maintenance_hour",
        "maximum_critical_path_regression_minutes"}, "explicit objective and graph value policy required")
    objective_name = bounded_name(objective["name"], "objective.name")
    horizon = nonnegative(objective["comparison_horizon_runs"], "comparison_horizon_runs")
    ratio_floor = nonnegative(objective["graph_min_saved_runner_hours_per_maintenance_hour"],
                              "graph_min_saved_runner_hours_per_maintenance_hour")
    max_delay = nonnegative(objective["maximum_critical_path_regression_minutes"],
                            "maximum_critical_path_regression_minutes")
    require(horizon > 0 and horizon == int(horizon), "comparison_horizon_runs must be positive integer")
    baseline = data["baseline"]
    require(isinstance(baseline, dict) and set(baseline) == {"job_minutes", "critical_path_minutes", "evidence"},
            "baseline metrics/evidence required")
    base_cost = nonnegative(baseline["job_minutes"], "baseline.job_minutes")
    base_time = nonnegative(baseline["critical_path_minutes"], "baseline.critical_path_minutes")
    require(base_cost > 0 and base_time > 0, "positive baseline measurements required")
    require(baseline["evidence"] in EVIDENCE, "invalid baseline evidence")
    alternatives = data["alternatives"]
    require(isinstance(alternatives, list) and 2 <= len(alternatives) <= 20,
            "compare 2 to 20 source-bound alternatives")
    ids = set()
    output = []
    for item in alternatives:
        require(isinstance(item, dict) and set(item) == {
            "id", "kind", "job_minutes", "critical_path_minutes", "evidence",
            "detector_parity", "required_status_and_spec_compatible",
            "source_impact_complete", "transitive_dependencies_complete",
            "stale_and_missing_receipts_refused", "rollback_defined", "maintenance_hours",
            "proof_reference"}, "invalid alternative fields")
        identifier = bounded_name(item["id"], "alternative.id")
        require(identifier not in ids, "duplicate alternative: " + identifier)
        ids.add(identifier)
        kind = item["kind"]
        require(kind in KINDS, "unrecognized strategy kind")
        cost = nonnegative(item["job_minutes"], identifier + ".job_minutes")
        critical = nonnegative(item["critical_path_minutes"], identifier + ".critical_path_minutes")
        maintenance = nonnegative(item["maintenance_hours"], identifier + ".maintenance_hours")
        require(item["evidence"] in EVIDENCE, "invalid alternative evidence")
        proof = bounded_name(item["proof_reference"], identifier + ".proof_reference")
        blockers = []
        for field, reason in [
            ("detector_parity", "DETECTOR_PARITY_UNPROVEN"),
            ("required_status_and_spec_compatible", "REQUIRED_STATUS_OR_SPEC_UNMAPPED"),
            ("stale_and_missing_receipts_refused", "FRESH_RECEIPT_GUARD_UNPROVEN"),
            ("rollback_defined", "ROLLBACK_MISSING"),
        ]:
            require(type(item[field]) is bool or item[field] is None, field + " must be true/false/null")
            if item[field] is not True:
                blockers.append(reason)
        if kind == "dependency":
            for field, reason in [
                ("source_impact_complete", "SOURCE_IMPACT_INCOMPLETE"),
                ("transitive_dependencies_complete", "TRANSITIVE_DEPENDENCIES_INCOMPLETE"),
            ]:
                require(type(item[field]) is bool or item[field] is None, field + " must be true/false/null")
                if item[field] is not True:
                    blockers.append(reason)
        else:
            for field in ("source_impact_complete", "transitive_dependencies_complete"):
                require(type(item[field]) is bool or item[field] is None, field + " must be true/false/null")
        if item["evidence"] == "unknown":
            blockers.append("COST_UNMEASURED")
        if item["evidence"] != "observed" or baseline["evidence"] != "observed":
            confidence = "MODELED_ONLY"
        else:
            confidence = "SOURCE_DECLARED_OBSERVED_UNAUTHENTICATED"
        saving = base_cost - cost
        speed = base_time - critical
        if saving <= 0 and speed <= 0:
            blockers.append("NO_OBSERVED_OR_PROJECTED_IMPROVEMENT")
        if critical - base_time > max_delay:
            blockers.append("CRITICAL_PATH_REGRESSION_EXCEEDS_POLICY")
        horizon_saved_runner_hours = (saving / 60) * horizon
        payback_ratio = None if maintenance == 0 else horizon_saved_runner_hours / maintenance
        if kind == "dependency" and (saving <= 0 or (maintenance > 0 and payback_ratio < ratio_floor)):
            blockers.append("DEPENDENCY_COMPLEXITY_NOT_JUSTIFIED")
        output.append({"id": identifier, "kind": kind, "proof_reference": proof,
                       "job_minutes": cost, "critical_path_minutes": critical,
                       "job_minutes_delta": round(saving, 6),
                       "critical_path_delta": round(speed, 6),
                       "maintenance_hours": maintenance,
                       "horizon_saved_runner_hours": round(horizon_saved_runner_hours, 6),
                       "saved_runner_hours_per_maintenance_hour": (
                           None if payback_ratio is None else round(payback_ratio, 6)),
                       "evidence": confidence,
                       "disposition": "CANDIDATE_FOR_VALIDATION" if not blockers else "HOLD",
                       "blockers": sorted(set(blockers))})
    viable = [x for x in output if x["disposition"] == "CANDIDATE_FOR_VALIDATION"]
    viable.sort(key=lambda x: (x["job_minutes"], x["critical_path_minutes"],
                               x["maintenance_hours"], x["id"]))
    return {"schema_version": 1, "revision": revision, "objective": objective_name,
            "decision": "OPTIONS_FOR_EXPERIMENT" if viable else "HOLD",
            "ranking_for_experiment": [x["id"] for x in viable],
            "alternatives": output,
            "qualification": "NOT_QUALIFIED",
            "savings_proof": "NOT_MEASURED_BY_THIS_TOOL"}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    args = parser.parse_args(argv)
    try:
        result = evaluate(load(args.input))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"decision": "HOLD", "error": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["decision"] == "OPTIONS_FOR_EXPERIMENT" else 1


if __name__ == "__main__":
    sys.exit(main())
