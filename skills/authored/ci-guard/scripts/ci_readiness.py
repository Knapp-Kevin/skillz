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
import hashlib
import os
import subprocess
from pathlib import Path
import sys

import ci_self_repair
import ci_overlap
import ci_strategy_fit
import ci_scenario
import ci_source_reconcile

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



def verify_local_source(root, manifest, source_map):
    """Recompute static source/oracle evidence and compare bytes to local Git HEAD.

    Uses only fixed, read-only git builtins, never status/filter/checkout/hooks.
    This does NOT authenticate a remote ref, GitHub semantics or oracle execution.
    """
    directory=ci_source_reconcile.root_dir(root)
    evidence=ci_source_reconcile.reconcile(str(directory),manifest,source_map)
    revision=bounded(manifest["source_revision"],"source revision")
    need(len(revision)==40 and all(c in "0123456789abcdef" for c in revision),
         "local Git bridge currently supports SHA-1 repositories only")
    def git(*args):
        command=["git","-C",str(directory),"-c","core.fsmonitor=false",*args]
        env=os.environ.copy()
        env.update({"GIT_CONFIG_NOSYSTEM":"1", "GIT_CONFIG_GLOBAL":os.devnull,
                    "GIT_OPTIONAL_LOCKS":"0","GIT_TERMINAL_PROMPT":"0",
                    "GIT_ATTR_NOSYSTEM":"1"})
        try:
            run=subprocess.run(command,env=env,capture_output=True,
                               timeout=8,check=False)
        except (FileNotFoundError,subprocess.TimeoutExpired,OSError) as exc:
            raise Hold("local Git evidence unavailable") from exc
        need(run.returncode==0 and len(run.stdout)<=4096,
             "local Git evidence unavailable or invalid")
        try:return run.stdout.decode("utf-8").strip()
        except UnicodeError as exc:
            raise Hold("invalid local Git output") from exc
    top=Path(git("rev-parse","--show-toplevel"))
    need(top==directory,"source root must be exact Git worktree root")
    need(git("rev-parse","--show-object-format")=="sha1",
         "unsupported Git repository object format")
    head=git("rev-parse","HEAD")
    need(head==revision,"LOCAL_GIT_HEAD_MISMATCH")
    paths=[x["path"] for x in source_map["workflow_files"]]+[
        x["path"] for x in source_map["oracle_files"]]
    need(len(set(paths))==len(paths) and bool(paths),
         "duplicated or missing declared source paths")
    for path in sorted(paths):
        ci_source_reconcile.path_id(path,"tracked source path")
        listing=git("ls-tree","HEAD","--",path)
        line=listing.split("\n")
        need(len(line)==1 and "\t" in listing,
             "LOCAL_SOURCE_NOT_TRACKED_AT_HEAD:"+path)
        header,gitpath=listing.split("\t",1)
        words=header.split()
        need(gitpath==path and len(words)==3 and
             words[0] in {"100644","100755"} and words[1]=="blob" and
             len(words[2])==40 and
             all(c in "0123456789abcdef" for c in words[2]),
             "LOCAL_SOURCE_GIT_TREE_INVALID:"+path)
        file=directory.joinpath(*path.split("/"))
        need(not file.is_symlink() and file.is_file(),
             "LOCAL_SOURCE_PATH_MISSING_OR_LINKED:"+path)
        raw=file.read_bytes()
        need(len(raw)<=ci_source_reconcile.MAX_BYTES,
             "LOCAL_SOURCE_OVERSIZED:"+path)
        blob=hashlib.sha1(b"blob "+str(len(raw)).encode("ascii")+b"\0"+raw).hexdigest()
        need(blob==words[2],"LOCAL_SOURCE_BYTES_NOT_AT_HEAD:"+path)
    return {"source_receipt":evidence,
            "binding":"LOCAL_GIT_HEAD_AND_TRACKED_SOURCE_BYTES_MATCHED",
            "local_head":head, "verified_tracked_files":len(paths),
            "git_remote_ref_authenticated":False,
            "compiled_oracle_execution_verified":False,
            "effective_github_semantics_verified":False}


def evaluate(data, local_source=None):
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
    if not any(row.get("actual_qualifies") is False for row in selected):
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

    if local_source is not None:
        need(isinstance(local_source,dict) and
             local_source.get("binding")=="LOCAL_GIT_HEAD_AND_TRACKED_SOURCE_BYTES_MATCHED",
             "invalid local source-bound evidence")
        recomputed=local_source.get("source_receipt")
        need(isinstance(recomputed,dict),"local source receipt unavailable")
        for field in required:
            if source.get(field)!=recomputed.get(field):
                issues.append("LOCAL_SOURCE_RECEIPT_DRIFT:"+field)
        if local_source.get("local_head")!=sha:
            issues.append("LOCAL_SOURCE_HEAD_DRIFT")

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
        "source_receipt_basis": ("LOCAL_TRACKED_BYTES_RECOMPUTED_NOT_REMOTE_AUTHENTICATED"
                                  if local_source is not None else
                                  "SUPPLIED_STATIC_REPORT_NOT_AUTHENTICATED"),
        "local_git_source_binding_verified": local_source is not None,
        "remote_git_identity_authenticated": False,
        "source_oracle_runtime_executed_by_bridge": False,
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
    parser.add_argument("--source-root",
                        help="Opt-in exact local Git worktree root; read-only source binding")
    parser.add_argument("--source-map",
                        help="Existing CI Guard static source map for the selected design")
    parser.add_argument("--require-source-bound", action="store_true",
                        help="Exit nonzero unless local Git HEAD and all mapped source bytes match")
    args = parser.parse_args(argv)
    try:
        need(bool(args.source_root)==bool(args.source_map),
             "source root and map must be provided together")
        data=load(args.input)
        bound=(verify_local_source(args.source_root,data["scenario_manifest"],
               ci_source_reconcile.load_json(args.source_map))
               if args.source_root else None)
        report = evaluate(data, local_source=bound)
        print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))
        if args.require_source_bound and bound is None:
            return 3
        return 3 if args.require_ready and report["status"] != "READY_FOR_ONE_QUALIFICATION" else 0
    except (Hold, ValueError, TypeError, OSError, KeyError, OverflowError) as err:
        print("CI_READINESS_HOLD: " + str(err), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
