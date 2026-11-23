#!/usr/bin/env python3
"""CI Guard outcome-first pre-qualification receipt.

Thin, read-only composition of CI Guard's existing canonical diagnostics.
Never executes workflow commands, contacts GitHub or authorizes qualification.
All evidence is caller-supplied and not independently authenticated.
Python 3.9+ standard library only.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import sys

import ci_self_repair
import ci_overlap
import ci_strategy_fit
import ci_scenario

MAX_BYTES = 1024 * 1024
CONTROLS = (
    "source_oracle_tests_executed",
    "seeded_negative_controls_executed",
    "protected_statuses_and_release_paths_mapped",
    "native_and_unique_detectors_preserved",
    "old_workflow_retirement_verified",
    "bounded_rollback_defined",
    "owner_approved_experiment_budget",
)
OBJECTIVES = {"runner_and_critical_path", "runner_minutes", "critical_path"}


class Hold(ValueError):
    pass


def need(ok, message):
    if not ok:
        raise Hold(message)


def bounded(value, label):
    need(isinstance(value, str) and bool(value.strip()) and
         len(value) <= 128, label + ": nonempty short string required")
    return value


def percent(value, label):
    need(type(value) in (int, float) and math.isfinite(value) and
         0 <= value <= 100, label + ": expected 0..100 finite number")
    return float(value)


def minutes(value, label):
    need(type(value) in (int, float) and math.isfinite(value) and
         0 <= value <= 1000000, label + ": invalid nonnegative minutes")
    return float(value)


def evaluate(data):
    """Recompute the declared diagnostics; never accept a caller-forged PASS."""
    need(isinstance(data, dict), "root object required")
    keys = {"schema_version", "source_revision", "selected_strategy",
            "selected_scenario_design", "objective", "first_failure",
            "controls", "self_repair", "overlap_graph", "strategy_fit",
            "scenario_manifest", "source_receipt"}
    need(set(data) == keys and type(data["schema_version"]) is int
         and data["schema_version"] == 1, "readiness schema mismatch")
    sha = bounded(data["source_revision"], "source revision")
    need(len(sha) == 40 and all(c in "0123456789abcdef" for c in sha),
         "full lowercase Git SHA-1 required")
    strategy_id = bounded(data["selected_strategy"], "selected strategy")
    design_id = bounded(data["selected_scenario_design"], "scenario design")
    obj = data["objective"]
    need(isinstance(obj, dict) and set(obj) == {
        "primary", "min_runner_savings_percent",
        "min_critical_path_savings_percent", "max_first_failure_regression_minutes"
    }, "explicit primary objective and economic thresholds required")
    need(obj["primary"] in OBJECTIVES, "unsupported primary objective")
    min_runner = percent(obj["min_runner_savings_percent"], "runner threshold")
    min_critical = percent(obj["min_critical_path_savings_percent"], "critical threshold")
    max_failure = minutes(obj["max_first_failure_regression_minutes"],
                          "maximum first failure regression")
    fail = data["first_failure"]
    need(isinstance(fail, dict) and set(fail) == {
        "baseline_minutes", "candidate_minutes", "evidence"
    }, "first failure observations or estimates required")
    first_before = minutes(fail["baseline_minutes"], "first failure baseline")
    first_after = minutes(fail["candidate_minutes"], "first failure candidate")
    need(first_before > 0 and fail["evidence"] in {"observed", "estimated"},
         "first failure comparison provenance missing")
    controls = data["controls"]
    need(isinstance(controls, dict) and set(controls) == set(CONTROLS),
         "all required qualification preflight controls must be declared")
    need(all(type(value) is bool for value in controls.values()),
         "qualification controls must be actual booleans")
    issues = []
    for name in CONTROLS:
        if not controls[name]:
            issues.append("CONTROL_NOT_EVIDENCED:" + name)

    # Reuse the canonical implementations; supplied summaries are not a PASS.
    pre = ci_self_repair.preflight(data["self_repair"])
    overlap = ci_overlap.audit(data["overlap_graph"])
    fit = ci_strategy_fit.evaluate(data["strategy_fit"])
    scenario = ci_scenario.run(data["scenario_manifest"])

    for label, actual in (("self-repair", pre["revision"]),
                          ("strategy", fit["revision"]),
                          ("scenario", scenario["exact_source_revision"])):
        if actual != sha:
            issues.append("SOURCE_REVISION_MISMATCH:" + label)
    if pre["status"] != "PREFLIGHT_READY":
        issues.append("SELF_REPAIR_NOT_READY")
    for problem in pre["issues"]:
        issues.append("SELF_REPAIR:" + problem)
    if overlap["unresolved"]:
        issues.append("OVERLAP_UNRESOLVED")
    for finding in overlap["findings"]:
        if finding["classification"] in (
            "EXACT_DUPLICATE_CANDIDATE", "PARTIAL_OVERLAP", "UNPROVEN"
        ):
            issues.append("REPEATED_TERMINAL_STILL_ACTIVE:" + finding["pair"])
    entries = data["overlap_graph"]["entrypoints"]
    stages = set()
    for e in entries:
        if e.get("revision") != sha:
            issues.append("OVERLAP_REVISION_NOT_BOUND:" + str(e.get("id")))
        if e.get("active") is not False:
            stages.add(e.get("stage"))
    if not {"candidate", "release"} <= stages:
        issues.append("CANDIDATE_OR_RELEASE_PATH_UNMAPPED")

    if fit["decision"] != "OPTIONS_FOR_EXPERIMENT":
        issues.append("NO_VIABLE_ARCHITECTURE_COMPARISON")
    alt = next((a for a in fit["alternatives"] if a["id"] == strategy_id), None)
    need(alt is not None, "selected strategy is not in canonical comparison")
    if len(fit["alternatives"]) < 3 or len(fit["ranking_for_experiment"]) < 2:
        issues.append("INSUFFICIENT_ALTERNATIVE_COMPARISON")
    if alt["disposition"] != "CANDIDATE_FOR_VALIDATION":
        issues.append("SELECTED_STRATEGY_UNQUALIFIED")
    for block in alt["blockers"]:
        issues.append("STRATEGY:" + block)
    if data["strategy_fit"]["baseline"]["evidence"] != "observed":
        issues.append("BASELINE_NOT_OBSERVED")
    baseline = data["strategy_fit"]["baseline"]
    raw_alt = next(a for a in data["strategy_fit"]["alternatives"]
                   if a["id"] == strategy_id)
    runner_saving = 100 * (baseline["job_minutes"] - raw_alt["job_minutes"]) / baseline["job_minutes"]
    critical_saving = 100 * (baseline["critical_path_minutes"] - raw_alt["critical_path_minutes"]) / baseline["critical_path_minutes"]
    if obj["primary"] in {"runner_and_critical_path", "runner_minutes"} and runner_saving < min_runner:
        issues.append("PRIMARY_RUNNER_SAVINGS_BELOW_THRESHOLD")
    if obj["primary"] in {"runner_and_critical_path", "critical_path"} and critical_saving < min_critical:
        issues.append("PRIMARY_CRITICAL_PATH_SAVINGS_BELOW_THRESHOLD")
    if first_after - first_before > max_failure:
        issues.append("FIRST_FAILURE_FEEDBACK_REGRESSION")
    if scenario["status"] != "STRUCTURAL_PASS" or scenario["issues"]:
        issues.append("SCENARIOS_NOT_STRUCTURALLY_QUALIFIED")
    selected = [x for x in scenario["results"] if x["design"] == design_id]
    if not selected or any(not row["matches_expected"] for row in selected):
        issues.append("SCENARIO_DESIGN_NOT_COVERED")
    if not any(not row.get("qualifies", False) for row in selected):
        issues.append("ADVERSE_SCENARIO_MISSING")

    # Supplied source receipt from existing static source reconciler. Cannot
    # authenticate Git tree, actual oracle execution, or GitHub semantics.
    source = data["source_receipt"]
    need(isinstance(source, dict), "canonical source receipt required")
    required = ("schema_version", "status", "design", "claimed_source_revision",
                "workflow_files", "jobs", "oracle_checks", "source_git_head_authenticated",
                "compiled_oracle_execution_verified", "automatic_cutover_authorized")
    need(all(k in source for k in required), "incomplete source receipt")
    if not (source["schema_version"] == 1 and
            source["status"] == "STATIC_SOURCE_RECONCILED" and
            source["design"] == design_id and
            source["claimed_source_revision"] == sha and
            all(type(source[k]) is int and source[k] > 0 for k in
                ("workflow_files", "jobs", "oracle_checks"))):
        issues.append("SOURCE_OR_ORACLE_RECEIPT_MISMATCH")
    if (source["source_git_head_authenticated"] is not False or
            source["compiled_oracle_execution_verified"] is not False or
            source["automatic_cutover_authorized"] is not False):
        issues.append("FORGED_SOURCE_VERIFICATION_AUTHORITY")

    verdict = "HOLD" if issues else "READY_FOR_ONE_QUALIFICATION"
    return {
        "schema_version": 1, "status": verdict, "issues": sorted(set(issues)),
        "source_revision": sha, "selected_strategy": strategy_id,
        "selected_scenario_design": design_id,
        "primary_objective": obj["primary"],
        "projected_runner_minutes_savings_percent": round(runner_saving, 4),
        "projected_critical_path_savings_percent": round(critical_saving, 4),
        "projected_first_failure_feedback_delta_minutes": round(first_before - first_after, 4),
        "cost_basis": "ANALYST_DECLARED_ESTIMATE_NOT_MEASURED_SAVINGS",
        "source_receipt_basis": "SUPPLIED_STATIC_REPORT_NOT_AUTHENTICATED",
        "diagnostic_results_recomputed_from_declared_inputs": True,
        "ready_only_for_one_bounded_qualification": verdict == "READY_FOR_ONE_QUALIFICATION",
        "owner_authorization_granted": False,
        "protected_branch_rules_verified": False,
        "end_to_end_ci_qualified": False,
        "production_cutover_authorized": False,
        "observed_provider_billing": "NOT_MEASURED",
        "next_action": ("REQUEST_SEPARATE_OWNER_AND_HOST_QUALIFICATION"
                        if verdict == "READY_FOR_ONE_QUALIFICATION"
                        else "RESOLVE_READINESS_HOLDS_BEFORE_EXPENSIVE_CI"),
    }


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def load(path):
    target = Path(path).absolute()
    need(target.is_file() and target.stat().st_size <= MAX_BYTES and
         not any(x.is_symlink() for x in (target, *target.parents)),
         "missing, oversized or symlinked input")
    with target.open(encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=unique_pairs,
                         parse_constant=lambda _: (_ for _ in ()).throw(Hold("nonfinite JSON")))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--require-ready", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = evaluate(load(args.input))
        print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
        return 3 if args.require_ready and report["status"] != "READY_FOR_ONE_QUALIFICATION" else 0
    except (Hold, ValueError, TypeError, OSError, KeyError, OverflowError) as err:
        print("CI_READINESS_HOLD: " + str(err), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
