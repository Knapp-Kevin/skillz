#!/usr/bin/env python3
"""Conservative offline CI scenario simulator for a bounded normalized graph.

NOT a GitHub Actions expression interpreter or a provider receipt authenticator.
A trusted host must derive this manifest from the complete exact-head workflow,
local conformance oracles, release specification, and reusable/nested jobs.
No workflow commands, scripts, actions, or remote operations are executed.
"""
from __future__ import annotations
import argparse
import fnmatch
import json
import math
from pathlib import Path
import sys

MAX_BYTES = 1024 * 1024
EVENTS = {"draft", "ready", "push", "release", "dispatch", "workflow_call", "cancelled"}
CONDITIONS = {"success", "always", "needs_failed", "needs_skipped"}
STATES = {"success", "failure", "skipped", "cancelled", "pending"}
ROLES = {"verify", "produce", "qualify", "other"}
LANES = {"independent", "dependent", "other"}
API = "shared-artifact-export"

class Invalid(Exception):
    pass

def need(ok, message):
    if not ok: raise Invalid(message)

def fields(record, allowed, required, where):
    need(isinstance(record, dict), where + " must be an object")
    need(not (set(record)-set(allowed)), where + " unknown fields")
    need(set(required) <= set(record), where + " missing required fields")

def ident(v, label):
    need(isinstance(v, str) and 1 <= len(v) <= 96 and
         all(c.isalnum() or c in "-._:/" for c in v), label + " invalid identity")
    return v

def number(v, label):
    need(type(v) in (int, float) and math.isfinite(v) and 0 <= v <= 86400,
         label + " must be finite nonnegative seconds")
    return float(v)

def unique(rows, where):
    need(isinstance(rows, list) and len(rows) <= 256, where + " expected bounded list")
    need(len(rows) == len(set(rows)), where + " contains duplicates")
    return rows

def parse(document):
    fields(document,{"schema_version","source_revision","inventory","designs","scenarios","known_semantics"},
           {"schema_version","source_revision","inventory","designs","scenarios","known_semantics"}, "manifest")
    need(document["schema_version"] == 1 and type(document["schema_version"]) is int, "unsupported schema")
    source=ident(document["source_revision"],"source revision")
    need(len(source) in (40, 64) and all(c in "0123456789abcdef" for c in source), "source revision must be lowercase SHA fingerprint")
    inventory=document["inventory"]
    fields(inventory,{"complete","workflow_files_checked","nested_invocations_expanded","conformance_tests_checked","normative_rules_checked","unresolved","source_revision"},
           {"complete","workflow_files_checked","nested_invocations_expanded","conformance_tests_checked","normative_rules_checked","unresolved","source_revision"}, "inventory")
    reasons=[]
    for flag in ("complete","workflow_files_checked","nested_invocations_expanded","conformance_tests_checked","normative_rules_checked"):
        if inventory[flag] is not True: reasons.append("INVENTORY_INCOMPLETE:"+flag)
    if inventory["source_revision"] != source: reasons.append("INVENTORY_STALE")
    if not isinstance(inventory["unresolved"],list) or inventory["unresolved"]: reasons.append("UNRESOLVED_PATH_OR_ORACLE")
    if document["known_semantics"] != "NORMALIZED_SUBSET_V1": reasons.append("UNSUPPORTED_SEMANTICS")
    designs=document["designs"]
    need(isinstance(designs,list) and 2 <= len(designs) <= 4, "compare two to four graph designs")
    design_ids=[]
    for d in designs:
        fields(d,{"id","source_revision","workflows","jobs","normative_obligations"},
               {"id","source_revision","workflows","jobs","normative_obligations"},"design")
        design_ids.append(ident(d["id"],"design id"))
        if d["source_revision"]!=source: reasons.append("DESIGN_STALE:"+d["id"])
        need(isinstance(d["workflows"],list) and 1 <= len(d["workflows"]) <= 24,"bounded workflows")
        need(isinstance(d["jobs"],list) and 1 <= len(d["jobs"]) <= 128,"bounded jobs")
    unique(design_ids,"design IDs")
    scenarios=document["scenarios"]
    need(isinstance(scenarios,list) and 1 <= len(scenarios) <= 64,"bounded scenarios required")
    unique([ident(s.get("id"),"scenario") for s in scenarios],"scenario IDs")
    return source,reasons

def eval_design(d, scenario, source):
    wmap={}
    for w in d["workflows"]:
        fields(w,{"id","events","paths","trigger_from","token_semantics"},
               {"id","events","paths"},"workflow")
        wid=ident(w["id"],"workflow id")
        need(wid not in wmap,"duplicate workflow")
        need(isinstance(w["events"],list) and w["events"] and set(w["events"]) <= EVENTS,"unsupported event")
        need(isinstance(w["paths"],list) and w["paths"] and all(isinstance(x,str) and x for x in w["paths"]),"workflow paths")
        wmap[wid]=w
    jmap={}
    for j in d["jobs"]:
        fields(j,{"id","workflow","needs","condition","routes","role","lane","obligation","platform","trust","seconds","matrix","artifact_from","artifact_id","runtime_guard","conformance_condition","conformance_needs","independent_detection","eligible_events","matrix_source","matrix_revision"},
               {"id","workflow","needs","condition","routes","role","lane","seconds","matrix","conformance_condition","conformance_needs","eligible_events"},"job")
        jid=ident(j["id"],"job id")
        need(jid not in jmap,"duplicate job")
        need(j["workflow"] in wmap,"unknown workflow job")
        need(j["condition"] in CONDITIONS and j["role"] in ROLES and j["lane"] in LANES,"unsupported job condition/role/lane")
        need(isinstance(j["routes"],list) and j["routes"] and set(j["routes"]) <= {"full","light"},"invalid routes")
        need(isinstance(j["eligible_events"],list) and j["eligible_events"] and set(j["eligible_events"]) <= EVENTS,"invalid job events")
        unique(j["needs"],"needs");need(isinstance(j["conformance_needs"],list),"conformance needs absent")
        number(j["seconds"],"job duration")
        need(isinstance(j["matrix"],list) and 1 <= len(j["matrix"]) <= 16,"matrix needs explicit bounded shards")
        unique(j["matrix"],"matrix shards")
        if j["role"]=="verify":
            obligation=j.get("obligation")
            if isinstance(obligation,str) and "{shard}" in obligation:
                ident(obligation.replace("{shard}","shard"),"verification obligation")
            else: ident(obligation,"verification obligation")
        if j.get("matrix_source") is not None:
            if j.get("matrix_source") not in jmap and j.get("matrix_source") not in [x["id"] for x in d["jobs"]]:
                raise Invalid("dynamic matrix source unmapped")
            if j.get("matrix_revision") != source:
                raise Invalid("dynamic matrix expansion revision stale")
        if j["role"]=="produce": ident(j.get("artifact_id"),"produced artifact")
        jmap[jid]=j
    for j in jmap.values():
        need(all(dep in jmap and dep!=j["id"] for dep in j["needs"]),"missing/self job dependency")
        need(all(jmap[dep]["workflow"] == j["workflow"] for dep in j["needs"]),
             "cross-workflow needs is not a GitHub job dependency")
    waiting=list(jmap)
    order=[]
    while waiting:
        available=[k for k in waiting if all(n in order for n in jmap[k]["needs"])]
        need(available,"dependency cycle or missing source")
        for k in available: order.append(k);waiting.remove(k)
    problems=[]
    for j in jmap.values():
        if j["condition"] != j["conformance_condition"] or j["needs"] != j["conformance_needs"]:
            problems.append("VALIDATOR_DRIFT:"+j["id"])
        if j["lane"]=="independent" and j.get("runtime_guard") is not True:
            problems.append("INDEPENDENT_LANE_GUARD_ABSENT:"+j["id"])
        if j["lane"]=="dependent" and j.get("artifact_from") not in jmap:
            problems.append("ARTIFACT_PRODUCER_UNMAPPED:"+j["id"])
        if j["lane"]=="dependent" and j.get("artifact_from") not in j["needs"]:
            problems.append("ARTIFACT_PRODUCER_NOT_IN_NEEDS:"+j["id"])
        if j.get("matrix_source") is not None and j["matrix_source"] not in j["needs"]:
            problems.append("MATRIX_PLAN_NOT_IN_NEEDS:"+j["id"])
        if j["role"]=="qualify" and j.get("obligation"):
            problems.append("GATE_CANNOT_IMPERSONATE_VERIFIER:"+j["id"])
    selected=set()
    event=scenario["event"]
    for wid,w in wmap.items():
        if event in w["events"] and any(fnmatch.fnmatchcase(path,pat) for path in scenario["changed_paths"] for pat in w["paths"]):
            selected.add(wid)
        if w.get("trigger_from") is not None:
            # Never invent GitHub token-trigger behavior; this subset supports
            # only independently evidenced externally-dispatched chains.
            if w.get("token_semantics") != "EXTERNAL_DISPATCH_VERIFIED":
                problems.append("UNSUPPORTED_TRIGGER_CHAIN:"+wid)
    statuses={};ends={};starts={};run_scheduled=set();shard_states={}
    calls=scenario.get("runtime_api_calls",{})
    forced=scenario.get("forced_outcomes",{})
    need(isinstance(forced,dict) and isinstance(calls,dict),"invalid scenario result maps")
    recognized={jid for jid in jmap}
    recognized.update(jid+"#"+shard for jid,j in jmap.items() for shard in j["matrix"])
    # Scenario can name equivalent jobs from both candidate designs. Their
    # union is checked once by run(); a candidate ignores the other design.
    # Never silently allow names outside all designs.
    for job_calls in calls.values():
        need(isinstance(job_calls,list) and all(v==API for v in job_calls),"unsupported runtime API call")
    for jid in order:
        j=jmap[jid];deps=[statuses[x] for x in j["needs"]]
        allowed=(j["workflow"] in selected and scenario["route"] in j["routes"]
                 and event in j["eligible_events"])
        if j["condition"]=="success": allowed=allowed and all(x=="success" for x in deps)
        elif j["condition"]=="needs_skipped": allowed=allowed and "skipped" in deps and "failure" not in deps and "cancelled" not in deps
        elif j["condition"]=="needs_failed": allowed=allowed and "failure" in deps
        # Always is explicitly requested and never implies qualification.
        states={shard: (forced.get(jid+"#"+shard,forced.get(jid,"success"))
                        if allowed else "skipped") for shard in j["matrix"]}
        need(set(states.values()) <= STATES,"unrecognized forced result")
        if any(v!="skipped" for v in states.values()):
            run_scheduled.add(jid)
            starts[jid]=max([ends.get(n,0) for n in j["needs"]] or [0.0])
            ends[jid]=starts[jid]+number(j["seconds"],"time")
            if j["lane"]=="independent" and API in calls.get(jid,[]):
                states={k:"failure" if v!="skipped" else v for k,v in states.items()}
                problems.append("INDEPENDENT_ARTIFACT_EXPORT_ATTEMPT:"+jid)
            if j["lane"]=="dependent":
                upstream=jmap[j["artifact_from"]]
                if (statuses.get(upstream["id"])!="success" or
                    upstream.get("artifact_id") != j.get("artifact_id") or
                    j["artifact_from"] not in j["needs"]):
                    states={k:"failure" if v!="skipped" else v for k,v in states.items()}
                    problems.append("ARTIFACT_CUSTODY_OR_PRODUCER_FAILURE:"+jid)
            if j["condition"]=="always" and any(x in {"failure","cancelled","skipped"} for x in deps) and j["role"]=="qualify":
                problems.append("ALWAYS_GATE_MUST_AUDIT_NEEDS:"+jid)
        shard_states[jid]=states
        status=("failure" if "failure" in states.values() else
                "cancelled" if "cancelled" in states.values() else
                "pending" if "pending" in states.values() else
                "skipped" if all(x=="skipped" for x in states.values()) else
                "success" if all(x=="success" for x in states.values()) else "failure")
        statuses[jid]=status
    req=scenario["required_obligations"]
    unique(req,"scenario obligations")
    need(bool(req), "required obligation set cannot be empty")
    for key in req: ident(key,"obligation identity")
    found={key:[] for key in req}
    for jid in run_scheduled:
        j=jmap[jid]
        if j["role"]!="verify":continue
        for shard in j["matrix"]:
            shard_obligation=j["obligation"].replace("{shard}",shard)
            sig="/".join([shard_obligation,j.get("platform","generic"),j.get("trust","default")])
            if sig in found:
                found[sig].append(shard_states[jid][shard])
    missing=[k for k,v in found.items() if not v or not all(x=="success" for x in v)]
    duplicates=[k for k,v in found.items() if len(v)>1]
    # Exact-head provider-status assertions are declared simulator inputs,
    # not independently authenticated GitHub check receipts.
    receipts=scenario["status_checks"]
    need(isinstance(receipts,dict),"required status evidence must be an object")
    for key in req:
        receipt=receipts.get(key)
        if not isinstance(receipt,dict):
            problems.append("REQUIRED_STATUS_ABSENT:"+key);continue
        fields(receipt,{"revision","conclusion","kind"},
              {"revision","conclusion","kind"},"required status")
        if receipt["revision"]!=source:
            problems.append("REQUIRED_STATUS_STALE:"+key)
        if receipt["kind"]!="EXECUTED_VERIFIER":
            problems.append("DRAFT_OR_NONVERIFIER_STATUS_REUSED:"+key)
        if receipt["conclusion"]!="success":
            problems.append("REQUIRED_STATUS_UNQUALIFIED:"+key)
        if receipt["conclusion"]=="success" and (key in missing):
            problems.append("REQUIRED_STATUS_SPOOFED:"+key)
    norm=d["normative_obligations"].get(scenario["route"])
    if norm is None: problems.append("NORMATIVE_ROUTE_NOT_MAPPED")
    elif set(norm)!=set(req):problems.append("NORMATIVE_OBLIGATIONS_DRIFT")
    for k in duplicates:problems.append("DUPLICATE_UNIQUE_OBLIGATION:"+k)
    for k in missing:problems.append("MISSING_OR_FAILED_OBLIGATION:"+k)
    if scenario.get("provider_semantics")!="NORMALIZED_DECLARED":problems.append("UNSUPPORTED_SEMANTICS")
    if scenario.get("receipt_revision") != source:
        problems.append("STALE_RECEIPT_OR_DRAFT_GREEN")
    gate_success=any(jmap[k]["role"]=="qualify" and statuses[k]=="success" for k in run_scheduled)
    qualifies=gate_success and not problems and not missing
    costs=sum(number(jmap[k]["seconds"],"time")*sum(v!="skipped" for v in shard_states[k].values()) for k in run_scheduled)
    critical=max([ends.get(k,0) for k in run_scheduled] or [0.0])
    earliest_failure=min([ends.get(k,0) for k in run_scheduled if statuses.get(k)=="failure"] or [float("inf")])
    return {"design":d["id"],"scenario":scenario["id"],"actual_qualifies":qualifies,
        "expected_qualifies":scenario["expected_qualifies"],
        "matches_expected":qualifies==scenario["expected_qualifies"],
        "statuses":statuses,"shard_states":shard_states,"scheduled_jobs":sorted(run_scheduled),
        "scheduled_start_seconds":starts,"scheduled_end_seconds":ends,"missing":missing,
        "duplicate":duplicates,"issues":sorted(set(problems)),
        "estimated_runner_seconds":round(costs,3),"estimated_critical_path_seconds":round(critical,3),
        "earliest_failure_seconds":None if earliest_failure==float("inf") else round(earliest_failure,3),
        "provider_authenticated":False}

def run(doc):
    rev,problems=parse(doc);results=[]
    allowable={j["id"] for d in doc["designs"] for j in d["jobs"]}
    allowable_shards=allowable | {j["id"]+"#"+shard for d in doc["designs"] for j in d["jobs"] for shard in j["matrix"]}
    for scenario in doc["scenarios"]:
        fields(scenario,{"id","source_revision","event","route","changed_paths","expected_qualifies","required_obligations","forced_outcomes","runtime_api_calls","provider_semantics","receipt_revision","status_checks"},
            {"id","source_revision","event","route","changed_paths","expected_qualifies","required_obligations","forced_outcomes","runtime_api_calls","provider_semantics","receipt_revision","status_checks"},"scenario")
        need(scenario["event"] in EVENTS and scenario["route"] in {"full","light"},"invalid scenario event/route")
        need(type(scenario["expected_qualifies"]) is bool,"expected_qualifies boolean")
        need(isinstance(scenario["changed_paths"],list) and scenario["changed_paths"],"changed paths absent")
        if scenario["source_revision"]!=rev:problems.append("SCENARIO_REVISION_STALE:"+scenario["id"])
        need(set(scenario["runtime_api_calls"]) <= allowable, "runtime API call job not in candidate union")
        need(set(scenario["forced_outcomes"]) <= allowable_shards, "forced outcome not in candidate union")
        for design in doc["designs"]:
            results.append(eval_design(design,scenario,rev))
    for x in results:
        if not x["matches_expected"]:problems.append("EXPECTED_SCENARIO_MISMATCH:"+x["design"]+":"+x["scenario"])
        for y in x["issues"]:
            if y.startswith(("UNSUPPORTED", "VALIDATOR_DRIFT", "INDEPENDENT_LANE_GUARD_ABSENT",
                             "ARTIFACT_PRODUCER_NOT_IN_NEEDS", "MATRIX_PLAN_NOT_IN_NEEDS")):
                problems.append("STRUCTURAL_GRAPH_HOLD:"+x["design"]+":"+x["scenario"]+":"+y)
    return {"status":"STRUCTURAL_PASS" if not problems else "HOLD","issues":sorted(set(problems)),
      "results":results,"schema_version":1,"exact_source_revision":rev,
      "observed_runner_savings":"NOT_MEASURED","observed_critical_path_delta":"NOT_MEASURED",
      "real_provider_semantics_authenticated":False,"host_execution_proven":False,
      "automatic_best_design_selected":False}

def object_pairs(pairs):
    out={}
    for key,val in pairs:
        if key in out:raise Invalid("duplicate JSON key")
        out[key]=val
    return out

def main(args=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--require-pass",action="store_true")
    a=p.parse_args(args)
    try:
        path=a.input.absolute()
        need(not any(p.is_symlink() for p in (path,*path.parents)),"symlinked source/parent")
        need(path.stat().st_size<=MAX_BYTES,"manifest too large")
        with path.open(encoding="utf8") as src:
            d=json.load(src,object_pairs_hook=object_pairs,parse_constant=lambda _: (_ for _ in ()).throw(Invalid("nonfinite")))
        result=run(d)
    except (Invalid,ValueError,OSError,UnicodeError,KeyError,TypeError) as exc:
        print("INVALID_INPUT: " + str(exc),file=sys.stderr)
        return 2
    print(json.dumps(result,indent=2,sort_keys=True))
    return (3 if a.require_pass and result["status"]!="STRUCTURAL_PASS" else 0)

if __name__=="__main__":raise SystemExit(main())
