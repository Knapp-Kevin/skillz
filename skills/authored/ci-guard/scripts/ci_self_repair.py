#!/usr/bin/env python3
"""CI Guard: bounded, read-only self-repair preflight from declared evidence.

Does NOT scrape workflows, execute repository commands, authorize rule changes,
authenticate receipts or measure provider billing. Caller must inventory real
workflow/script and test-internal traces and independently validate assertions.
"""
import argparse
import fnmatch
import json
import math
import sys
from pathlib import Path

MAX_BYTES = 1024 * 1024
KINDS = {"compile", "setup", "fixture", "project-check", "generation",
         "test", "oracle", "mutation", "cleanup", "other"}
MUTATING = {"mutation", "cleanup"}
EVIDENCE = {"observed", "estimated"}
STAGES = {"draft", "ready", "push", "release", "dispatch"}


def require(cond, message):
    if not cond:
        raise ValueError(message)


def nonempty(v, label):
    require(isinstance(v, str) and bool(v.strip()) and len(v) <= 256,
            label + ": nonempty bounded string required")
    return v


def number(v, label):
    require(type(v) in (int, float) and math.isfinite(v) and v >= 0,
            label + ": finite nonnegative number required")
    return float(v)


def pairs_no_duplicates(pairs):
    result = {}
    for k, v in pairs:
        require(k not in result, "duplicate JSON key")
        result[k] = v
    return result


def reject_constant(value):
    raise ValueError("nonfinite JSON value")


def source(path):
    p = path.absolute()
    require(not any(x.is_symlink() for x in (p, *p.parents)),
            "linked input or ancestor refused")
    require(p.stat().st_size <= MAX_BYTES, "input exceeds 1MiB")
    with p.open(encoding="utf-8") as f:
        return json.load(f, object_pairs_hook=pairs_no_duplicates,
                         parse_constant=reject_constant)


def preflight(data):
    require(isinstance(data, dict), "root object required")
    revision = nonempty(data.get("revision"), "revision")
    require(revision != "UNKNOWN", "unknown revision")
    workflows = data.get("workflows")
    events = data.get("repair_events")
    phases = data.get("phases")
    controls = data.get("controls")
    budget = data.get("budget")
    require(isinstance(workflows, list) and workflows, "workflow inventory missing")
    require(isinstance(events, list) and events, "repair event forecast missing")
    require(isinstance(phases, list) and phases, "phase observations missing")
    require(isinstance(controls, dict) and isinstance(budget, dict),
            "controls or budget missing")
    issues = []
    if data.get("inventory_complete") is not True:
        issues.append("INVENTORY_INCOMPLETE")
    if controls.get("nested_execution_inventory_complete") is not True:
        issues.append("NESTED_EXECUTION_NOT_INVENTORIED")
    if controls.get("required_status_and_spec_mapped") is not True:
        issues.append("REQUIRED_STATUS_OR_SPEC_UNMAPPED")
    if controls.get("release_unique_detection_preserved") is not True:
        issues.append("RELEASE_OR_NATIVE_PARITY_UNPROVEN")
    if controls.get("source_tests_and_policy_ready") is not True:
        issues.append("COORDINATED_CHANGESET_NOT_READY")
    if controls.get("rollback_defined") is not True:
        issues.append("ROLLBACK_NOT_DEFINED")
    if controls.get("cheap_checks_passed") is not True:
        issues.append("CHEAP_CHECKS_NOT_GREEN")
    if controls.get("exact_head_freshness_plan") is not True:
        issues.append("EXACT_HEAD_ACCEPTANCE_NOT_PLANNED")
    max_jobs = number(budget.get("max_preparation_jobs"), "max_preparation_jobs")
    max_cycles = number(budget.get("max_expensive_cycles"), "max_expensive_cycles")
    planned_cycles = number(budget.get("planned_expensive_cycles"), "planned_expensive_cycles")
    if planned_cycles > max_cycles:
        issues.append("EXPENSIVE_QUALIFICATION_CYCLES_OVER_BUDGET")

    wf = {}
    for row in workflows:
        require(isinstance(row, dict), "workflow object required")
        name = nonempty(row.get("id"), "workflow.id")
        require(name not in wf, "duplicate workflow: " + name)
        triggers = row.get("events")
        paths = row.get("paths")
        require(isinstance(triggers, list) and triggers and
                all(v in STAGES for v in triggers), "invalid workflow events")
        require(isinstance(paths, list) and paths and
                all(isinstance(v, str) and v for v in paths), "invalid paths")
        jobs = number(row.get("matrix_jobs"), name + ".matrix_jobs")
        require(jobs == int(jobs), "matrix_jobs must be integer")
        if row.get("matrix_expanded") is not True:
            issues.append("MATRIX_UNEXPANDED:" + name)
        if row.get("invocations_expanded") is not True:
            issues.append("NESTED_COMMANDS_UNEXPANDED:" + name)
        if row.get("active") not in (True, False):
            issues.append("ACTIVITY_UNKNOWN:" + name)
        wf[name] = row

    forecasts = []
    expensive_cycles = 0
    for event in events:
        require(isinstance(event, dict), "repair event object required")
        eid = nonempty(event.get("id"), "event.id")
        stage = event.get("stage")
        require(stage in STAGES, "unknown event stage")
        changed = event.get("changed_paths")
        require(isinstance(changed, list) and changed and
                all(isinstance(x, str) and x for x in changed),
                "changed paths incomplete")
        matching = []
        for name, row in wf.items():
            if row["active"] is False or stage not in row["events"]:
                continue
            if any(fnmatch.fnmatchcase(path, pattern)
                   for path in changed for pattern in row["paths"]):
                matching.append(name)
        total = sum(int(wf[n]["matrix_jobs"]) for n in matching)
        forecast = {"event": eid, "stage": stage, "changed_paths": changed,
                    "matched_workflows": matching, "predicted_jobs": total,
                    "cost_source": "DECLARED_CONFIGURATION_NOT_BILLED"}
        forecasts.append(forecast)
        if stage == "draft" and any(wf[n].get("expensive") is not False
                                    for n in matching):
            issues.append("EXPENSIVE_DRAFT_FANOUT:" + eid)
        if stage == "draft" and total > max_jobs:
            issues.append("PREPARATION_FANOUT_OVER_BUDGET:" + eid)
        if stage in {"ready", "push", "release"} and total:
            expensive_cycles += 1
        if (stage == "ready" and total > max_jobs and
                not controls.get("owner_authorized_full_gate", False)):
            issues.append("UNINTENDED_READY_FANOUT:" + eid)
    if expensive_cycles > max_cycles:
        issues.append("FORECAST_QUALIFICATION_CYCLES_OVER_BUDGET")

    timing = {}
    details = []
    by_shared = {}
    for row in phases:
        require(isinstance(row, dict), "phase row required")
        ident = nonempty(row.get("test_id"), "test_id")
        phase = row.get("phase")
        require(phase in KINDS, "unsupported test phase")
        environment = nonempty(row.get("environment"), "environment")
        revision_row = nonempty(row.get("revision"), "phase revision")
        if revision_row != revision:
            issues.append("STALE_PHASE_TRACE:" + ident)
        p50 = number(row.get("p50_minutes"), "phase.p50")
        p90 = number(row.get("p90_minutes"), "phase.p90")
        require(p90 >= p50, "p90 below p50")
        if row.get("evidence") not in EVIDENCE:
            issues.append("TIMING_UNVERIFIED:" + ident)
        timing[phase] = timing.get(phase, 0) + p50
        shared = row.get("shared_key")
        if shared is not None:
            nonempty(shared, "shared_key")
            by_shared.setdefault((shared, environment, revision_row), []).append(row)
        details.append({"test_id": ident, "phase": phase, "p50_minutes": p50,
                        "p90_minutes": p90, "environment": environment,
                        "unique_detection": row.get("unique_detection") is True})

    repeated = []
    for (key, environment, rev), group in sorted(by_shared.items()):
        if len(group) < 2:
            continue
        if any(x["phase"] in MUTATING or x.get("mutates_fixture") is True
               or x.get("fresh_directory_required") is True or
               x.get("process_isolation_required") is True for x in group):
            cls = "JUSTIFIED_ISOLATION"
        elif any(x.get("unique_detection") is True for x in group):
            cls = "UNIQUE_DETECTION"
        elif all(x.get("immutable") is True for x in group):
            cls = "REPEATED_IMMUTABLE_SETUP"
        else:
            cls = "UNPROVEN"
        repeated.append({"shared_key": key, "environment": environment,
                         "revision": rev, "class": cls,
                         "test_ids": [x["test_id"] for x in group],
                         "reuse_authorized": False})
    dominant = max(timing, key=timing.get) if timing else "UNKNOWN"
    if not any(x["phase"] == "test" for x in phases):
        issues.append("TEST_INTERNAL_TIMING_MISSING")
    if any(r["class"] == "UNPROVEN" for r in repeated):
        issues.append("REPEATED_WORK_NOT_CHARACTERIZED")
    if any(r["class"] == "REPEATED_IMMUTABLE_SETUP" for r in repeated):
        # Detection alone does not prove reuse is safe or executed.
        issues.append("IMMUTABLE_REUSE_NOT_YET_PROVEN")

    return {
        "status": "PREFLIGHT_READY" if not issues else "HOLD",
        "issues": sorted(set(issues)),
        "revision": revision,
        "fanout_forecast": forecasts,
        "phase_p50_minutes": dict(sorted(timing.items())),
        "dominant_observed_or_reported_phase": dominant,
        "phase_details": details,
        "repeated_operations": repeated,
        "reported_p50_is_additive_not_critical_path": True,
        "claimed_test_equivalence": False,
        "optimization_complete": False,
        "provider_receipts_authenticated": False,
        "observed_runner_minutes_delta": "NOT_MEASURED",
        "observed_critical_path_delta": "NOT_MEASURED",
        "note": "Caller-declared workflow/phase data; no mutation, execution, billing or full CI adoption.",
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True, type=Path)
    p.add_argument("--require-ready", action="store_true")
    args = p.parse_args(argv)
    try:
        data = preflight(source(args.input))
    except (ValueError, OSError, UnicodeError, RecursionError) as exc:
        print("INVALID_INPUT: " + str(exc), file=sys.stderr)
        return 2
    print(json.dumps(data, indent=2, sort_keys=True))
    return 0 if data["status"] == "PREFLIGHT_READY" else (3 if args.require_ready else 0)


if __name__ == "__main__":
    sys.exit(main())
