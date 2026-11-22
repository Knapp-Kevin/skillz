#!/usr/bin/env python3
"""Produce CI Guard results proof from caller-supplied run receipts.

Offline, Python stdlib only. Does not authenticate GitHub, fetch provider
data, execute CI, publish releases or modify a consuming repository.
Strict comparisons reuse compare_ci_runs.py without relaxing its safeguards.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
import re
import statistics
import sys

import compare_ci_runs as strict

MAX_BYTES = 1024 * 1024
EVIDENCE = {"OBSERVED_AS_SUPPLIED_NOT_AUTHENTICATED", "SIMULATED", "ESTIMATED", "NOT_MEASURED"}
MODES = {"strict", "longitudinal", "estimate"}


def check(ok, description):
    if not ok:
        raise strict.EvidenceError(description)


def fields(obj, required, optional=(), where="object"):
    check(isinstance(obj, dict), where + " must be an object")
    check(set(required) <= set(obj), where + " missing required field")
    check(not set(obj) - set(required) - set(optional), where + " contains unknown field")


def ids(items, label):
    check(isinstance(items, list) and len(items) <= 256, label + " must be bounded list")
    check(all(isinstance(x, str) and 0 < len(x) <= 160 for x in items), label + " invalid identity")
    check(len(items) == len(set(items)), label + " duplicated identity")
    return items


def safe_text(value):
    text = str(value)
    return (text.replace("\\", "\\\\").replace("|", "\\|")
            .replace("\n", " ").replace("\r", " ").replace("<", "&lt;")
            .replace(">", "&gt;"))


def percent(before, after):
    if before is None or after is None or before == 0:
        return None
    return round(100.0 * (before - after) / before, 3)


def median(values):
    return round(statistics.median(values), 4) if values else None


def p90(values):
    if len(values) < 3:
        return None
    return round(sorted(values)[math.ceil(0.9 * len(values)) - 1], 4)


def summary(run):
    # Optional billing applies ONLY to this report's raw timing lens.
    # compare_ci_runs.compare() keeps its strict billed-minute requirement.
    return strict.summarize_run(run, allow_missing_billing=True)


def validate_assurance(a):
    required = ("expected_before", "executed_before", "expected_after", "executed_after",
                "contexts_before", "contexts_after", "seeded_fault_caught_before",
                "seeded_fault_caught_after", "release_guards_retained",
                "old_workflows_retired", "cutover_verified")
    fields(a, required, where="assurance")
    for key in required[:6]:
        ids(a[key], key)
    for key in required[6:]:
        check(type(a[key]) is bool, key + " must be boolean")
    expected = set(a["expected_before"])
    after = set(a["expected_after"])
    executed_before = set(a["executed_before"])
    executed_after = set(a["executed_after"])
    parity = (bool(expected) and expected == after == executed_before == executed_after
              and bool(a["contexts_before"]) and
              set(a["contexts_before"]) == set(a["contexts_after"]) and
              all(a[k] for k in required[6:8]) and a["release_guards_retained"]
              and a["old_workflows_retired"] and a["cutover_verified"])
    missing_before = sorted(expected - executed_before)
    missing_after = sorted(expected - executed_after)
    return {"verdict": "QUALIFIED" if parity else "NOT_QUALIFIED",
            "authenticated": False, "declared_only": True,
            "missing_before": missing_before, "missing_after": missing_after,
            "retained_unique_obligations": sorted(expected & after & executed_after),
            "seeded_faults_both_detected": a["seeded_fault_caught_before"] and a["seeded_fault_caught_after"],
            "release_guards_retained": a["release_guards_retained"],
            "old_workflows_retired": a["old_workflows_retired"],
            "cutover_verified_as_supplied": a["cutover_verified"],
            "context_sets_equal": set(a["contexts_before"]) == set(a["contexts_after"])}


def validate_scope(scope):
    keys = ("event_before", "event_after", "stage_before", "stage_after",
            "os_before", "os_after", "architecture_before", "architecture_after",
            "matrix_before", "matrix_after", "toolchain_before", "toolchain_after",
            "workload_equivalence", "confounders")
    fields(scope, keys, where="scope")
    for name in keys[:-2]:
        if name.startswith("matrix_"):
            check(type(scope[name]) is int and 0 < scope[name] <= 10000, "invalid matrix size")
        else:
            check(isinstance(scope[name], str) and scope[name], "scope identity absent")
    check(scope["workload_equivalence"] in {"same", "different", "unknown"}, "invalid workload equivalence")
    ids(scope["confounders"], "confounders")
    mismatches = [k for k in ("event", "stage", "os", "architecture", "toolchain")
                  if scope[k + "_before"] != scope[k + "_after"]]
    if scope["matrix_before"] != scope["matrix_after"]:
        mismatches.append("matrix")
    if scope["workload_equivalence"] != "same":
        mismatches.append("workload")
    return mismatches


def raw_delta(before, after):
    result = {}
    for name in ("executed_job_minutes", "billed_runner_minutes", "critical_path_seconds",
                 "qualification_elapsed_seconds"):
        old, new = before.get(name), after.get(name)
        result[name] = {"baseline": old, "optimized": new,
                        "saved": round(old - new, 4) if old is not None and new is not None else None,
                        "saved_percent": percent(old, new),
                        "denominator": old,
                        "unit": "seconds" if name.endswith("seconds") else "minutes"}
    return result


def report(data):
    fields(data, ("schema_version", "comparison_mode", "evidence", "pairs", "assurance",
                  "scope", "source_refs", "change"), where="results proof input")
    check(type(data["schema_version"]) is int and data["schema_version"] == 1, "unsupported schema")
    mode = data["comparison_mode"]
    check(mode in MODES, "unknown comparison mode")
    evidence = data["evidence"]
    check(evidence in EVIDENCE, "unknown evidence provenance")
    # Caller claims about authentication cannot elevate the offline tool.
    check(isinstance(data["pairs"], list) and len(data["pairs"]) <= 40, "invalid pair count")
    refs = data["source_refs"]
    fields(refs, ("baseline_workflow", "optimized_workflow", "baseline_tree",
                  "optimized_tree", "receipt_refs"), where="source refs")
    for key in ("baseline_workflow", "optimized_workflow", "baseline_tree", "optimized_tree"):
        check(isinstance(refs[key], str) and bool(refs[key]), "source ref missing")
    ids(refs["receipt_refs"], "receipt refs")
    change = data["change"]
    fields(change, ("summary", "waste_before", "retired_workflows"),
           ("forecast_runner_savings_percent",), "change")
    check(isinstance(change["summary"], str) and bool(change["summary"]), "change summary required")
    ids(change["waste_before"], "waste causes")
    ids(change["retired_workflows"], "retired workflows")
    if "forecast_runner_savings_percent" in change:
        v = change["forecast_runner_savings_percent"]
        check(type(v) in (int, float) and math.isfinite(v) and -1000 <= v <= 100,
              "invalid forecast percent")
    assurances = validate_assurance(data["assurance"])
    scope_differences = validate_scope(data["scope"])

    aggregate = []
    strict_checked = False
    source_mismatch = False
    invalid_pair = False
    for pair in data["pairs"]:
        fields(pair, ("baseline", "optimized"), where="pair")
        before, after = pair["baseline"], pair["optimized"]
        if not isinstance(before, dict) or not isinstance(after, dict):
            raise strict.EvidenceError("incomplete run pair")
        source_mismatch |= before.get("head") != after.get("head")
        # Validate each run and DAG even for a longitudinal or incomparable scope.
        old, new = summary(before), summary(after)
        same_inputs = all(before.get(k) == after.get(k)
                          for k in ("head", "scenario", "runner_profile", "cache_class"))
        distinct = (before.get("run_id"), before.get("attempt")) != (
            after.get("run_id"), after.get("attempt"))
        check(distinct, "baseline and optimized are the same run attempt")
        if not same_inputs:
            invalid_pair = True
        billed = old["billed_runner_minutes"] is not None and new["billed_runner_minutes"] is not None
        if mode == "strict" and same_inputs and billed:
            # Authoritative existing comparator for complete same-source pairs.
            strict.compare({"schema_version": 1, "pairs": [pair]})
            strict_checked = True
        aggregate.append({"baseline_run": before["run_id"], "optimized_run": after["run_id"],
                          "source_equal": before["head"] == after["head"],
                          "strict_inputs_match": same_inputs, "billing_available": billed,
                          "baseline": old, "optimized": new, "metrics": raw_delta(old, new)})

    has_receipts = bool(aggregate) and evidence == "OBSERVED_AS_SUPPLIED_NOT_AUTHENTICATED"
    comparable = (mode == "strict" and has_receipts and not invalid_pair
                  and not scope_differences and not source_mismatch)
    if mode == "longitudinal":
        comparable = False
    scopes = sorted(set(scope_differences +
                        (["source revision"] if source_mismatch else []) +
                        (["runner/cache/scenario"] if invalid_pair else [])))
    limitations = [
        "Offline tool did not authenticate provider receipts, workflow rulesets, publication, or cost invoices.",
        "Assurance parity and source references are caller declarations, not live host evidence."
    ]
    if mode == "longitudinal":
        limitations.append("Different source revisions allow directional observations only; no exact-source causal claim.")
    if scopes:
        limitations.append("Different scopes/inputs: " + ", ".join(scopes))
    if any(not x["billing_available"] for x in aggregate):
        limitations.append("Missing provider billing; raw executed-job minutes are not billed or monetary cost.")
    if not has_receipts:
        limitations.append("No authenticated observed baseline/optimized pair; forecast is not measured savings.")
    if len(aggregate) < 3:
        limitations.append("Fewer than three samples; p90 is unavailable.")
    metric_names = ("executed_job_minutes", "billed_runner_minutes",
                    "critical_path_seconds", "qualification_elapsed_seconds")
    metrics = {}
    for key in metric_names:
        old_vals = [p["baseline"][key] for p in aggregate if p["baseline"][key] is not None]
        new_vals = [p["optimized"][key] for p in aggregate if p["optimized"][key] is not None]
        if len(old_vals) == len(new_vals) == len(aggregate) and aggregate:
            b, a = median(old_vals), median(new_vals)
            metrics[key] = {"baseline_median": b, "optimized_median": a,
                            "saved": round(b-a, 4), "saved_percent": percent(b, a),
                            "denominator": b, "sample_count": len(aggregate),
                            "baseline_p90": p90(old_vals), "optimized_p90": p90(new_vals)}
        else:
            metrics[key] = {"baseline_median": None, "optimized_median": None,
                            "saved": None, "saved_percent": None, "denominator": None,
                            "sample_count": len(aggregate), "baseline_p90": None,
                            "optimized_p90": None}
    cost = {"currency": None, "baseline": None, "optimized": None, "saved": None,
            "status": "NOT_MEASURED_NO_AUTHENTICATED_PRICING"}
    billed_delta = metrics["billed_runner_minutes"]["saved"]
    critical_delta = metrics["critical_path_seconds"]["saved"]
    elapsed_delta = metrics["qualification_elapsed_seconds"]["saved"]
    runner_delta = metrics["executed_job_minutes"]["saved"]
    if any(v is not None and v < 0 for v in (billed_delta, critical_delta, elapsed_delta, runner_delta)):
        indicated = "REGRESSION_OR_TRADEOFF"
    elif any(v is not None and v > 0 for v in (billed_delta, critical_delta, elapsed_delta, runner_delta)):
        indicated = "IMPROVEMENT_AS_SUPPLIED"
    elif has_receipts:
        indicated = "NO_GAIN_AS_SUPPLIED"
    else:
        indicated = "NO_MEASURED_COMPARISON"
    if not data["assurance"]["cutover_verified"] or not data["assurance"]["old_workflows_retired"]:
        verdict = "NOT_CUT_OVER"
    elif assurances["verdict"] != "QUALIFIED":
        verdict = "REGRESSION"
    elif not comparable and mode != "strict":
        verdict = "NOT_COMPARABLE" if has_receipts else "NOT_MEASURED"
    elif not comparable:
        verdict = "NOT_COMPARABLE" if has_receipts else "NOT_MEASURED"
    elif indicated == "REGRESSION_OR_TRADEOFF":
        verdict = "REGRESSION"
    else:
        # Never certify PROVED_* from unauthenticated caller-supplied receipts.
        verdict = "NOT_MEASURED"
    decision = {"verdict": verdict, "indicated_effect": indicated,
                "provider_verified": False, "certified_improvement": False,
                "reason": "No authenticated provider and assurance receipts available to this offline tool"}
    return {"schema_version": 1,
            "baseline": [p["baseline"] for p in aggregate],
            "optimized": [p["optimized"] for p in aggregate],
            "comparison_eligibility": {"mode": mode,
                                       "status": ("STRICT_AS_SUPPLIED" if comparable else
                                                  "DIRECTIONAL_ONLY" if mode == "longitudinal" and has_receipts and not scopes else
                                                  "NOT_COMPARABLE" if has_receipts else "NOT_MEASURED"),
                                       "strict_comparator_executed": strict_checked,
                                       "scope_differences": scopes,
                                       "source_mismatch": source_mismatch},
            "metrics": {"summaries": metrics, "pairs": aggregate,
                        "provider_cost": cost,
                        "estimated_runner_savings_percent": change.get("forecast_runner_savings_percent"),
                        "first_failure_feedback": "NOT_MEASURED"},
            "assurance_parity": assurances,
            "source_refs": refs, "change": change, "scope": data["scope"],
            "evidence_provenance": evidence, "limitations": limitations,
            "decision": decision}


def render_markdown(result):
    verdict = result["decision"]["verdict"]
    qualification = result["assurance_parity"]["verdict"]
    m = result["metrics"]["summaries"]
    def fmt(key, unit):
        item = m[key]
        if item["saved"] is None:
            return "NOT_MEASURED"
        return (f'{item["baseline_median"]} → {item["optimized_median"]} {unit}; '
                f'saved {item["saved"]} {unit} ({item["saved_percent"]}%, '
                f'baseline denominator {item["denominator"]})')
    c = result["change"]
    src = result["source_refs"]
    return "\n".join([
        "# CI Guard: before and after results proof", "",
        f'**Outcome:** {verdict}  ',
        f'**Assurance parity (declared):** {qualification}  ',
        f'**Evidence:** {result["evidence_provenance"]}  ',
        f'**Comparison:** {result["comparison_eligibility"]["status"]}  ',
        "**Provider-certified:** NO", "",
        "## Before", "",
        f'Workflow: {safe_text(src["baseline_workflow"])}',
        f'Tree: {safe_text(src["baseline_tree"])}',
        "Known waste: " + (", ".join(safe_text(x) for x in c["waste_before"]) or "not supplied"), "",
        "## What changed", "",
        safe_text(c["summary"]),
        "Retired paths: " + (", ".join(safe_text(x) for x in c["retired_workflows"]) or "none declared"), "",
        "## After", "",
        f'Workflow: {safe_text(src["optimized_workflow"])}',
        f'Tree: {safe_text(src["optimized_tree"])}', "",
        "## Outcomes and ROI", "",
        f'- Total executed job time: {fmt("executed_job_minutes", "job-min")}',
        f'- Provider billed runner time: {fmt("billed_runner_minutes", "billed-min")}',
        f'- Dependency critical path: {fmt("critical_path_seconds", "s")}',
        f'- Qualification wall-clock envelope: {fmt("qualification_elapsed_seconds", "s")}',
        "- First failing feedback: NOT_MEASURED unless independently measured",
        "- Monetary cost and payback: NOT_MEASURED without authenticated pricing and engineering cost",
        f'- Forecast (never an observed saving): {c.get("forecast_runner_savings_percent", "NOT_PROVIDED")}', "",
        "## Integrity and limitations", "",
        f'- Detection parity: {qualification}; declared only, not independently authenticated',
        f'- Seeded faults detected in both: {result["assurance_parity"]["seeded_faults_both_detected"]}',
        f'- Old workflows retired: {result["assurance_parity"]["old_workflows_retired"]}',
        f'- Release guards retained: {result["assurance_parity"]["release_guards_retained"]}',
        f'- Direction on supplied data: {result["decision"]["indicated_effect"]}', "",
        *("- " + safe_text(x) for x in result["limitations"]), "",
        "Source receipts: " + (", ".join(safe_text(x) for x in src["receipt_refs"]) or "none"), "",
        "This artifact records supplied evidence, not provider-verified production savings or permission to publish.", ""
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    source = args.input.absolute()
    check(not any(p.is_symlink() for p in (source, *source.parents)), "symlinked input/parent")
    check(source.is_file() and source.stat().st_size <= MAX_BYTES, "missing or oversized input")
    with source.open(encoding="utf-8") as f:
        data = json.load(f, object_pairs_hook=unique_json_pairs,
                         parse_constant=lambda _: (_ for _ in ()).throw(strict.EvidenceError("non-finite JSON")))
    result = report(data)
    target = args.output_dir.absolute()
    check(target.exists() and target.is_dir(), "output directory must already exist")
    check(not any(p.is_symlink() for p in (target, *target.parents)), "symlinked output/parent")
    json_path, md_path = target/"ci-results-proof.json", target/"CI-BEFORE-AFTER.md"
    check(not json_path.exists() and not md_path.exists(), "refuse overwrite of existing proof files")
    json_path.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False)+"\n", encoding="utf-8")
    md_path.write_text(render_markdown(result), encoding="utf-8")
    print(json.dumps({"json": str(json_path), "markdown": str(md_path),
                      "verdict": result["decision"]["verdict"]}, sort_keys=True))


def unique_json_pairs(pairs):
    result = {}
    for k, v in pairs:
        check(k not in result, "duplicate JSON key")
        result[k] = v
    return result


if __name__ == "__main__":
    try:
        main()
    except (strict.EvidenceError, OSError, UnicodeError, ValueError, TypeError, KeyError) as err:
        print("CI_RESULTS_PROOF_HOLD: "+str(err), file=sys.stderr)
        sys.exit(2)
