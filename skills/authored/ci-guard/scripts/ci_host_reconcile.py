#!/usr/bin/env python3
"""Reconcile one normalized CI Guard scenario against GitHub run/job receipts.

Default: offline, supplied JSON, NEVER an authenticated provider claim.
Opt-in --live: read-only GitHub REST run and per-attempt jobs via fixed
api.github.com HTTPS endpoints; never execute repository code or mutate CI.
Even direct API observations cannot authenticate branch protection, downstream
dispatch causality, side effects, provider billing, or release assurance.
Python 3.9+ standard library.
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
from pathlib import Path
import re
import ssl
import sys
import urllib.error
import urllib.request

MAX_BYTES = 1024 * 1024
REPO = re.compile(r"^[A-Za-z0-9_.-]{1,100}/[A-Za-z0-9_.-]{1,100}$")
SHA = re.compile(r"^[0-9a-f]{40}$|^[0-9a-f]{64}$")
FILE = re.compile(r"^\.github/workflows/[A-Za-z0-9_.-]+\.ya?ml$")
CONCLUSIONS = {"success", "failure", "skipped", "cancelled"}
MAX_JOBS_PER_RUN = 200


class Hold(ValueError):
    pass


def require(ok, explanation):
    if not ok:
        raise Hold(explanation)


def shape(obj, required, optional=(), label="object"):
    require(isinstance(obj, dict), label + ": expected object")
    require(set(required) <= set(obj), label + ": missing fields")
    require(not set(obj) - set(required) - set(optional),
            label + ": unexpected fields")


def identity(x, label):
    require(isinstance(x, str) and len(x) <= 120 and bool(x),
            label + ": invalid identifier")
    return x


def integer(x, label):
    require(type(x) is int and 1 <= x <= 2**53,
            label + ": invalid positive integer")
    return x


def parse_mapping(d):
    shape(d, ("schema_version", "repository", "source_revision", "scenario_id",
              "design_id", "expected_event", "workflow_runs"), label="mapping")
    require(d["schema_version"] == 1 and type(d["schema_version"]) is int,
            "unsupported mapping schema")
    require(isinstance(d["repository"], str) and REPO.fullmatch(d["repository"]),
            "repository must be owner/name")
    require(isinstance(d["source_revision"], str) and SHA.fullmatch(d["source_revision"]),
            "source must be exact full lowercase commit SHA")
    identity(d["scenario_id"], "scenario");identity(d["design_id"], "design")
    require(d["expected_event"] in {"pull_request", "push", "release",
                                   "workflow_dispatch", "repository_dispatch",
                                   "workflow_call"}, "unsupported provider event")
    runs=d["workflow_runs"]
    require(isinstance(runs, list) and 1 <= len(runs) <= 24,
            "bounded nonempty workflow run mapping required")
    seen_jobs=set(); seen_runs=set(); seen_workflows=set()
    for w in runs:
        shape(w, ("workflow", "workflow_file", "run_id", "attempt", "jobs"),
              label="workflow mapping")
        key=identity(w["workflow"], "workflow")
        require(key not in seen_workflows,"duplicate workflow mapping")
        seen_workflows.add(key)
        require(isinstance(w["workflow_file"],str) and FILE.fullmatch(w["workflow_file"]),
                "workflow file must be .github/workflows/*.yml or *.yaml")
        pair=(integer(w["run_id"], "run id"),integer(w["attempt"], "attempt"))
        require(pair not in seen_runs,"duplicate run/attempt mapping")
        seen_runs.add(pair)
        jobs=w["jobs"]
        require(isinstance(jobs,dict) and jobs and len(jobs) <= 128,
                "workflow jobs mapping required")
        host_names=set()
        for sim_id,display_name in jobs.items():
            identity(sim_id,"simulated job")
            identity(display_name,"provider displayed job")
            require(sim_id not in seen_jobs,"duplicate simulated job mapping")
            seen_jobs.add(sim_id)
            require(display_name not in host_names,"duplicate provider job mapping")
            host_names.add(display_name)
    return d


def selected_result(sim, mapping):
    shape(sim, ("schema_version", "status", "exact_source_revision", "results"),
          ("issues", "real_provider_semantics_authenticated", "host_execution_proven",
           "event_chains_provider_authenticated", "observed_runner_savings",
           "observed_critical_path_delta","automatic_best_design_selected"),
          "simulator summary")
    require(sim["schema_version"] == 3 and sim["status"] == "STRUCTURAL_PASS",
            "simulator must be an exact-source STRUCTURAL_PASS v3")
    require(sim["exact_source_revision"] == mapping["source_revision"],
            "simulation source revision mismatches mapping")
    require(sim.get("host_execution_proven") is False and
            sim.get("real_provider_semantics_authenticated") is False,
            "reject untrusted simulator self-authentication")
    require(isinstance(sim["results"],list) and sim["results"],
            "simulator results unavailable")
    matched=[x for x in sim["results"] if isinstance(x,dict) and
             x.get("design")==mapping["design_id"] and
             x.get("scenario")==mapping["scenario_id"]]
    require(len(matched)==1,"scenario/design identity absent or ambiguous")
    x=matched[0]
    require(x.get("matches_expected") is True,
            "scenario does not match source-qualified expectation")
    require(isinstance(x.get("statuses"),dict) and
            isinstance(x.get("scheduled_jobs"),list) and
            isinstance(x.get("activated_workflows"),list),
            "source simulation job graph missing")
    require(set(x["scheduled_jobs"]) <= set(x["statuses"]),
            "scheduled job status absent")
    return x


def observe_live(mapping, token=None, getter=None):
    """Only fixed GitHub API GET URLs. Inject getter for offline unit tests."""
    parse_mapping(mapping)
    if getter is None:
        getter=_github_get
    collected=[]
    for w in mapping["workflow_runs"]:
        rid=w["run_id"]; attempt=w["attempt"]
        prefix="https://api.github.com/repos/"+mapping["repository"]+"/actions/runs/"+str(rid)
        run=getter(prefix,token)
        # Per-attempt job endpoint. Do NOT silently blend jobs from reruns.
        jobs=[]
        for page in (1,2,3):
            path=prefix+"/attempts/"+str(attempt)+"/jobs?per_page=100&page="+str(page)
            payload=getter(path,token)
            require(isinstance(payload,dict) and isinstance(payload.get("jobs"),list),
                    "GitHub jobs response malformed")
            jobs.extend(payload["jobs"])
            require(len(jobs) <= MAX_JOBS_PER_RUN,"too many jobs, refuse truncated receipt")
            if len(payload["jobs"]) < 100:
                break
        else:
            raise Hold("job pagination exceeds supported bounded read")
        collected.append({"run":run,"jobs":jobs,"attempt":attempt})
    return {"schema_version":1, "repository":mapping["repository"],
            "workflow_runs":collected}


def _github_get(url,token):
    require(url.startswith("https://api.github.com/repos/") and
            "@" not in url and "#" not in url,
            "only supported GitHub API URLs allowed")
    headers={"Accept":"application/vnd.github+json",
             "User-Agent":"ci-guard-host-reconcile/1.0",
             "X-GitHub-Api-Version":"2022-11-28"}
    if token: headers["Authorization"]="Bearer "+token
    req=urllib.request.Request(url,headers=headers,method="GET")
    # No credential leakage on redirect to another host.
    opener=urllib.request.build_opener(_NoRedirect,
        urllib.request.HTTPSHandler(context=ssl.create_default_context()))
    try:
        with opener.open(req,timeout=12) as response:
            require(response.geturl()==url, "API redirect refused")
            size=response.headers.get("Content-Length")
            if size is not None: require(int(size) <= MAX_BYTES,"oversized API response")
            raw=response.read(MAX_BYTES+1)
    except (urllib.error.HTTPError,urllib.error.URLError) as exc:
        raise Hold("GitHub API read failed; verify actions:read permission and run ID") from exc
    require(len(raw) <= MAX_BYTES,"oversized API response")
    try:
        return json.loads(raw.decode("utf-8"),object_pairs_hook=no_duplicate_keys,
                          parse_constant=lambda _: (_ for _ in ()).throw(Hold("non-finite JSON")))
    except (ValueError,UnicodeError) as exc:
        raise Hold("invalid API JSON") from exc


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):
        raise Hold("GitHub API redirect refused")


def no_duplicate_keys(pairs):
    out={}
    for key,value in pairs:
        require(key not in out,"duplicate JSON key")
        out[key]=value
    return out


def time_value(text):
    require(isinstance(text,str) and text, "missing observed timestamp")
    try:
        dt=datetime.datetime.fromisoformat(text.replace("Z","+00:00"))
    except ValueError as exc:
        raise Hold("invalid job timestamp") from exc
    require(dt.utcoffset() is not None,"timestamp must specify timezone")
    return dt


def reconcile(sim,mapping,observed,live=False):
    parse_mapping(mapping)
    source=selected_result(sim,mapping)
    shape(observed, ("schema_version", "repository", "workflow_runs"),
          label="observations")
    require(type(observed["schema_version"]) is int and observed["schema_version"]==1,
            "unsupported observations schema")
    require(observed["repository"]==mapping["repository"],
            "receipt repository mismatch")
    rows=observed["workflow_runs"]
    require(isinstance(rows,list) and len(rows)==len(mapping["workflow_runs"]),
            "missing or extra provider workflow runs")
    scheduled=set(source["scheduled_jobs"])
    expected=set(source["statuses"])
    mapped={jid for w in mapping["workflow_runs"] for jid in w["jobs"]}
    require(mapped==scheduled,"every scheduled normalized job must map exactly once")
    issues=[];bound=[]
    seen_host_jobs=set();all_observed=set()
    if set(source["activated_workflows"]) != {w["workflow"] for w in mapping["workflow_runs"]}:
        issues.append("ACTIVATED_WORKFLOW_COVERAGE_UNKNOWN")
    observed_by_key={}
    for row in rows:
        require(isinstance(row,dict) and set(row)=={"run","jobs","attempt"},
                "invalid observed run envelope")
        run=row["run"]
        require(isinstance(run,dict),"invalid provider run")
        require(isinstance(row["jobs"],list),"missing provider jobs")
        pair=(run.get("id"),row["attempt"])
        require(pair not in observed_by_key,"duplicate provider receipt")
        observed_by_key[pair]=row
    intervals=[]
    for w in mapping["workflow_runs"]:
        key=(w["run_id"],w["attempt"])
        rec=observed_by_key.get(key)
        require(rec is not None,"expected run/attempt absent")
        run=rec["run"]
        require(run.get("head_sha")==mapping["source_revision"],
                "HOST_SOURCE_REVISION_MISMATCH")
        require(run.get("event")==mapping["expected_event"],
                "HOST_EVENT_MISMATCH")
        require(run.get("status")=="completed" and
                run.get("run_attempt",0)>=w["attempt"],
                "HOST_RUN_NOT_COMPLETED_OR_ATTEMPT_STALE")
        runpath=run.get("path")
        require(isinstance(runpath,str) and runpath.split("@",1)[0]==w["workflow_file"],
                "HOST_WORKFLOW_PATH_MISMATCH")
        require(run.get("id")==w["run_id"],"HOST_RUN_ID_MISMATCH")
        hostjobs=rec["jobs"]
        expected_states=[source["statuses"][name] for name in w["jobs"]]
        run_conclusion=run.get("conclusion")
        if run_conclusion not in CONCLUSIONS:
            issues.append("HOST_WORKFLOW_INCOMPLETE_OR_UNSUPPORTED:"+w["workflow"])
        elif all(x=="success" for x in expected_states) and run_conclusion!="success":
            issues.append("HOST_WORKFLOW_OUTCOME_DRIFT:"+w["workflow"])
        elif any(x in {"failure","cancelled"} for x in expected_states) and run_conclusion=="success":
            issues.append("HOST_WORKFLOW_FALSE_GREEN:"+w["workflow"])
        require(len(hostjobs) <= MAX_JOBS_PER_RUN,"unbounded host jobs")
        names={}
        for job in hostjobs:
            require(isinstance(job,dict) and type(job.get("id")) is int and job["id"]>0,
                    "invalid provider job identity")
            job_id=job["id"]
            require(job_id not in seen_host_jobs,"duplicate global provider job receipt")
            seen_host_jobs.add(job_id)
            name=identity(job.get("name"),"provider job name")
            require(name not in names,"duplicated provider display name")
            names[name]=job
            if job.get("run_id") is not None:
                require(job["run_id"]==w["run_id"],"job attached to other run")
        permitted=set(w["jobs"].values())
        if set(names)!=permitted:
            issues.append("UNMAPPED_OR_MISSING_HOST_JOBS:"+w["workflow"])
        for sim_id,display in w["jobs"].items():
            got=names.get(display)
            if got is None:
                issues.append("MISSING_HOST_JOB:"+sim_id);continue
            state=got.get("conclusion")
            if got.get("status")!="completed" or state not in CONCLUSIONS:
                issues.append("HOST_JOB_INCOMPLETE_OR_UNSUPPORTED:"+sim_id);continue
            expected_state=source["statuses"][sim_id]
            if state!=expected_state:
                issues.append("HOST_JOB_OUTCOME_DRIFT:"+sim_id)
            start,finish=got.get("started_at"),got.get("completed_at")
            if state!="skipped":
                if not start or not finish:
                    issues.append("HOST_JOB_TIMESTAMPS_MISSING:"+sim_id)
                else:
                    began,ended=time_value(start),time_value(finish)
                    require(ended>=began,"negative observed host duration")
                    intervals.append((began,ended,sim_id))
            all_observed.add(sim_id)
            bound.append({"sim_job":sim_id,"provider_job_id":got["id"],
                          "provider_name":display,"simulated_state":expected_state,
                          "observed_state":state,"run_id":w["run_id"],
                          "attempt":w["attempt"]})
    if all_observed!=scheduled:
        issues.append("INCOMPLETE_JOB_COVERAGE")
    # Exactly one bounded run per declared workflow cannot establish absence
    # of concurrent legacy/duplicate workflows or causal dispatch lineage.
    issues=sorted(set(issues))
    observed_time=round(sum((b-a).total_seconds() for a,b,_ in intervals),3)
    observed_envelope=(round((max(b for _,b,_ in intervals)-
                              min(a for a,_,_ in intervals)).total_seconds(),3)
                       if intervals else None)
    return {"schema_version":1,"status":"HOST_JOB_RECONCILED" if not issues else "HOLD",
            "issues":issues,"scenario":mapping["scenario_id"],"design":mapping["design_id"],
            "source_revision":mapping["source_revision"],
            "observation_provenance":("OBSERVED_GITHUB_API_DIRECT" if live else
                                      "OBSERVED_AS_SUPPLIED_NOT_AUTHENTICATED"),
            "provider_job_receipts":sorted(bound,key=lambda j:(j["run_id"],j["sim_job"])),
            "observed_executed_job_seconds":observed_time,
            "observed_job_wall_envelope_seconds":observed_envelope,
            "provider_billed_minutes":"NOT_MEASURED",
            "provider_dispatch_causality":"NOT_VERIFIED",
            "protected_branch_rules":"NOT_VERIFIED",
            "old_workflow_absence":"NOT_VERIFIED",
            "artifact_custody":"NOT_VERIFIED",
            "release_side_effects":"NOT_VERIFIED",
            "end_to_end_ci_qualified":False,
            "host_api_transport_verified_at_read":bool(live),
            "source_simulator_authenticated":False,
            "automatic_cutover_authorized":False,
            "not_measured":["queue","checkout","setup","artifact_wait",
                            "dependent-critical-path","first-failure-feedback",
                            "provider_billing","monetary_cost"]}


def load_json(path):
    p=Path(path).absolute()
    require(not any(x.is_symlink() for x in (p,*p.parents)),
            "symlinked input or parent")
    require(p.is_file() and p.stat().st_size <= MAX_BYTES,
            "input absent or oversized")
    with p.open(encoding="utf-8") as src:
        return json.load(src,object_pairs_hook=no_duplicate_keys,
                         parse_constant=lambda _: (_ for _ in ()).throw(Hold("non-finite JSON")))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--simulator-results",required=True)
    p.add_argument("--mapping",required=True)
    evidence=p.add_mutually_exclusive_group(required=True)
    evidence.add_argument("--observations")
    evidence.add_argument("--live",action="store_true")
    p.add_argument("--require-pass",action="store_true")
    args=p.parse_args()
    try:
        sim=load_json(args.simulator_results)
        mapping=parse_mapping(load_json(args.mapping))
        if args.live:
            obs=observe_live(mapping,token=os.environ.get("GH_TOKEN"))
        else:
            obs=load_json(args.observations)
        result=reconcile(sim,mapping,obs,live=bool(args.live))
        print(json.dumps(result,sort_keys=True,allow_nan=False))
        return 3 if args.require_pass and result["status"]!="HOST_JOB_RECONCILED" else 0
    except (Hold,ValueError,OSError,UnicodeError,TypeError,KeyError) as err:
        print("CI_HOST_RECONCILE_HOLD: "+str(err),file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
