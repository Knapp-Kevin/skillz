#!/usr/bin/env python3
"""Bind CI Guard normalized jobs to exact local workflow and oracle source.

This is a strict, read-only TEXTUAL subset, not a general YAML interpreter
and not execution of local conformance tests. Fail closed on syntax outside
the supported subset; require separate Git HEAD, host oracle and provider
verification. Python 3.9+ standard library; never execute repository code.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 1024 * 1024
PATH = re.compile(r"^[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*$")
JOB = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*$")
HEX = re.compile(r"^[0-9a-f]{64}$")
SCALAR = re.compile(r"^[A-Za-z0-9_.-]+$")
EXPR = re.compile(r"^[^\r\n]{1,300}$")
SUPPORTED_EVENTS = {"push", "pull_request", "workflow_dispatch", "repository_dispatch",
                    "release", "workflow_call"}


class Hold(ValueError):
    pass


def need(condition, reason):
    if not condition:
        raise Hold(reason)


def record(obj, required, optional=(), label="record"):
    need(isinstance(obj, dict), label + ": object required")
    need(set(required) <= set(obj), label + ": missing required keys")
    need(not set(obj) - set(required) - set(optional),
         label + ": unknown keys")


def path_id(value, label):
    need(isinstance(value, str) and len(value) <= 180 and PATH.fullmatch(value),
         label + ": invalid relative path")
    need(all(part not in {".", ".."} for part in value.split("/")),
         label + ": dot-segment path refused")
    return value


def unique(items, label):
    need(isinstance(items, list) and len(items) <= 128 and
         all(isinstance(x, str) and 0 < len(x) <= 160 for x in items),
         label + ": bounded string list required")
    need(len(set(items)) == len(items), label + ": duplicate entries")
    return items


def root_dir(path):
    root = Path(path).absolute()
    need(root.is_dir() and not any(p.is_symlink() for p in (root, *root.parents)),
         "root must be existing, non-symlinked directory")
    return root


def local_file(root, path):
    path_id(path, "source path")
    target = root.joinpath(*path.split("/"))
    need(not any(p.is_symlink() for p in (target, *target.parents)),
         "symlinked file or directory refused")
    need(target.is_file() and target.stat().st_size <= MAX_BYTES,
         "missing or oversized source file: " + path)
    data = target.read_bytes()
    need(len(data) <= MAX_BYTES, "source too large")
    try:
        return data.decode("utf-8"), hashlib.sha256(data).hexdigest()
    except UnicodeError as exc:
        raise Hold("non-UTF8 source file") from exc


def expected_sha(value):
    need(isinstance(value, str) and HEX.fullmatch(value), "SHA-256 digest required")
    return value


def scalar(value, label):
    need(isinstance(value,str) and SCALAR.fullmatch(value) and
         value not in {"null", "true", "false"}, label + ": unsupported scalar")
    return value


def literal_guard(value):
    need(isinstance(value, str) and EXPR.fullmatch(value) and value.strip()
         and value not in {"|", "|-", ">", ">-"}
         and not value.lstrip().startswith(("*", "&")),
         "UNSUPPORTED_SEMANTICS: multiline, aliased or absent job if")
    return value.strip()


def bracket_list(value, label, nonempty=False):
    need(isinstance(value,str) and value,"UNSUPPORTED_SEMANTICS: missing "+label)
    if value.startswith("[") and value.endswith("]"):
        pieces = [x.strip() for x in value[1:-1].split(",") if x.strip()]
    else:
        pieces=[value.strip()]
    need((pieces or not nonempty) and all(SCALAR.fullmatch(x) for x in pieces),
         "UNSUPPORTED_SEMANTICS: complex "+label)
    unique(pieces,label)
    return pieces


def read_workflow(source):
    """Understand only literal on/events and jobs/job-level if, needs, runs-on.

    Unparsed YAML structures must NEVER be treated as provider behavior.
    Fail closed on dynamic matrix, reusable workflows, event filters, aliases
    or multiline job-level conditions rather than making up their semantics.
    """
    top=None
    current=None
    events=[]
    jobs={}
    pending_events=False
    for lineno,line in enumerate(source.splitlines(),1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        stripped=line.lstrip(" ")
        indent=len(line)-len(stripped)
        need("\t" not in line[:indent] and indent%2==0,
             "UNSUPPORTED_SEMANTICS: invalid indentation at line "+str(lineno))
        if indent==0:
            m=re.fullmatch(r"([A-Za-z][A-Za-z0-9_-]*):(?:[ ]*(.*))?",line)
            need(m is not None,"UNSUPPORTED_SEMANTICS: top-level YAML syntax")
            top=m.group(1)
            if top=="on":
                need(not events and not pending_events,
                     "duplicate on trigger")
                val=(m.group(2) or "").strip()
                if val:
                    events=bracket_list(val,"trigger events",nonempty=True)
                else:
                    pending_events=True
            if top=="jobs":
                need(not jobs, "duplicate jobs section")
                need(not (m.group(2) or "").strip(),"UNSUPPORTED_SEMANTICS: inline jobs")
            current=None
            continue
        if top=="on":
            need(pending_events and indent==2,
                 "UNSUPPORTED_SEMANTICS: event filters and triggers require host parsing")
            m=re.fullmatch(r"  ([A-Za-z_][A-Za-z0-9_-]*):(?:[ ]*)",line)
            need(m is not None,"UNSUPPORTED_SEMANTICS: complex event")
            events.append(m.group(1))
            continue
        if top!="jobs":
            continue
        if indent==2:
            m=re.fullmatch(r"  ([A-Za-z_][A-Za-z0-9_-]*):[ ]*",line)
            need(m is not None,"UNSUPPORTED_SEMANTICS: complex job key")
            current=m.group(1)
            need(current not in jobs,"duplicate workflow job")
            jobs[current]={"if":None,"needs":[],"needs_literal":None,
                           "runs_on":None,"uses":False,"matrix":False}
            continue
        need(current is not None,"job member without job")
        if indent==4:
            m=re.fullmatch(r"    ([A-Za-z][A-Za-z0-9_-]*):(?:[ ]*(.*))?",line)
            need(m is not None,"UNSUPPORTED_SEMANTICS: complex job field")
            key=m.group(1); val=(m.group(2) or "").strip()
            job=jobs[current]
            if key=="if":
                need(job["if"] is None,"duplicate job if")
                job["if"]=literal_guard(val)
            elif key=="needs":
                need(job["needs_literal"] is None,"duplicate job needs")
                job["needs"]=bracket_list(val,"job needs")
                job["needs_literal"]="    needs: "+val
            elif key=="runs-on":
                need(job["runs_on"] is None,"duplicate runs-on")
                job["runs_on"]=scalar(val,"runs-on")
            elif key=="uses":
                job["uses"]=True
            elif key=="strategy":
                job["matrix"]=True
    need(bool(events) and bool(jobs),"UNSUPPORTED_SEMANTICS: workflow events or jobs missing")
    unique(events,"workflow events")
    need(set(events) <= SUPPORTED_EVENTS,"UNSUPPORTED_SEMANTICS: unknown event")
    for job in jobs.values():
        need(not job["uses"] and not job["matrix"],
             "UNSUPPORTED_SEMANTICS: reusable job or matrix expansion")
        need(job["runs_on"] is not None,
             "UNSUPPORTED_SEMANTICS: job runner not statically normalized")
    return {"events":sorted(events),"jobs":jobs}


def oracle_assertions(path_text, function_name):
    try:
        tree=ast.parse(path_text)
    except SyntaxError as exc:
        raise Hold("UNSUPPORTED_ORACLE: Python syntax") from exc
    functions=[node for node in ast.walk(tree)
               if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef))
               and node.name==function_name]
    need(len(functions)==1 and function_name.startswith("test_"),
         "UNSUPPORTED_ORACLE: test function missing or ambiguous")
    func=functions[0]
    # An ast.Assert is only a STATIC indicator; binding the actual file read
    # and executing the test are separate consumer-host obligations.
    assertions=set()
    for node in ast.walk(func):
        if isinstance(node,ast.Assert):
            expr=node.test
            if (isinstance(expr,ast.Compare) and len(expr.ops)==1
                and isinstance(expr.ops[0],ast.In)
                and len(expr.comparators)==1
                and isinstance(expr.left,ast.Constant) and
                isinstance(expr.left.value,str)
                and isinstance(expr.comparators[0],ast.Name)
                and expr.comparators[0].id=="workflow_text"):
                assertions.add(expr.left.value)
    strings={node.value for node in ast.walk(func)
             if isinstance(node,ast.Constant) and isinstance(node.value,str)}
    reading=any(isinstance(node,ast.Call) and isinstance(node.func,ast.Attribute)
                and node.func.attr=="read_text" for node in ast.walk(func))
    need(reading,"UNSUPPORTED_ORACLE: test source read not found")
    return assertions,strings


def validate_manifest(doc, design):
    record(doc,("schema_version","source_revision","design_id",
                "workflow_files","oracle_files"))
    need(type(doc["schema_version"]) is int and doc["schema_version"]==1,
         "unsupported source map version")
    need(doc["source_revision"]==design["source_revision"],
         "SOURCE_REVISION_MISMATCH")
    need(doc["design_id"]==design["id"],"DESIGN_ID_MISMATCH")
    workflows=doc["workflow_files"]
    need(isinstance(workflows,list) and 1 <= len(workflows) <= 24,
         "bounded workflow files required")
    unique([x.get("workflow") for x in workflows if isinstance(x,dict)],
           "workflow mappings")
    for entry in workflows:
        record(entry,("workflow","path","sha256","events","jobs"),
               label="workflow mapping")
        path=path_id(entry["path"],"workflow path")
        need(path.startswith(".github/workflows/") and
             path.endswith((".yml",".yaml")) and
             len(path.split("/"))==3,
             "workflow path must be direct .github/workflows file")
        expected_sha(entry["sha256"])
        unique(entry["events"],"workflow events")
        need(isinstance(entry["jobs"],list) and entry["jobs"],
             "workflow job mappings missing")
        for row in entry["jobs"]:
            record(row,("job","source_job","if","needs","runs_on"),
                   label="job mapping")
            scalar(row["source_job"],"source job")
            need(row["if"] is None or isinstance(row["if"],str),
                 "if must be literal or null")
            unique(row["needs"],"normalized needs")
            scalar(row["runs_on"],"runner")
    oracle_files=doc["oracle_files"]
    need(isinstance(oracle_files,list) and 1 <= len(oracle_files) <= 24,
         "explicit conformance oracle files required")
    for oracle in oracle_files:
        record(oracle,("path","sha256","checks"),label="oracle mapping")
        need(path_id(oracle["path"],"oracle path").endswith(".py"),
             "only Python AST subset supported")
        expected_sha(oracle["sha256"])
        need(isinstance(oracle["checks"],list),"oracle checks required")
        for item in oracle["checks"]:
            record(item,("job","function"),label="oracle job check")
            scalar(item["function"],"oracle test function")


def reconcile(root, scenario, source_map):
    root=root_dir(root)
    need(isinstance(scenario,dict) and type(scenario.get("schema_version")) is int
         and scenario["schema_version"]==3,"expected normalized v3 scenario input")
    # Use the existing source-schema authority rather than inventing a
    # competing manifest validator. This does NOT execute scenarios.
    import ci_scenario as simulator
    try:
        _, parse_issues = simulator.parse(scenario)
    except simulator.Invalid as exc:
        raise Hold("INVALID_NORMALIZED_SCENARIO: "+str(exc)) from exc
    need(not parse_issues,"INCOMPLETE_NORMALIZED_INVENTORY:"+",".join(parse_issues))
    need(isinstance(scenario.get("designs"),list),"designs absent")
    matched=[d for d in scenario["designs"]
             if isinstance(d,dict) and d.get("id")==source_map.get("design_id")]
    need(len(matched)==1,"design unavailable or ambiguous")
    design=matched[0]
    need(scenario.get("source_revision")==design.get("source_revision"),
         "scenario/design source revision drift")
    validate_manifest(source_map,design)
    expected_w={x["id"]:x for x in design["workflows"]}
    declared_w={x["workflow"]:x for x in source_map["workflow_files"]}
    need(set(declared_w)==set(expected_w),"UNINVENTORIED_OR_MISSING_WORKFLOW")
    workflow_dir=root/".github"/"workflows"
    need(workflow_dir.is_dir() and not workflow_dir.is_symlink(),
         "missing workflow directory")
    actual_workflows={}
    for child in workflow_dir.iterdir():
        if child.suffix in {".yml",".yaml"}:
            need(not child.is_symlink() and child.is_file(),"symlinked workflow")
            actual_workflows[child.relative_to(root).as_posix()]=True
    declared_files=[entry["path"] for entry in source_map["workflow_files"]]
    need(len(set(declared_files))==len(declared_files),
         "DUPLICATE_WORKFLOW_SOURCE_FILE")
    need(set(actual_workflows)==set(declared_files),
         "UNINVENTORIED_WORKFLOW_FILES")
    jobmap={j["id"]:j for j in design["jobs"]}
    need(len(jobmap)==len(design["jobs"]),"duplicated normalized job identity")
    referenced=set()
    evidence=[]
    job_source={}
    for workflow in source_map["workflow_files"]:
        raw,digest=local_file(root,workflow["path"])
        need(digest==workflow["sha256"],
             "WORKFLOW_DIGEST_MISMATCH:"+workflow["workflow"])
        parsed=read_workflow(raw)
        need(parsed["events"]==sorted(workflow["events"]),
             "SOURCE_TRIGGER_DRIFT:"+workflow["workflow"])
        mapped={row["source_job"]:row for row in workflow["jobs"]}
        need(len(mapped)==len(workflow["jobs"]),
             "duplicate workflow source job mapping")
        need(set(mapped)==set(parsed["jobs"]),
             "SOURCE_JOB_COVERAGE_DRIFT:"+workflow["workflow"])
        for source_id,row in mapped.items():
            sim_id=row["job"]
            need(sim_id in jobmap and sim_id not in referenced,
                 "UNMAPPED_OR_DUPLICATE_SIM_JOB:"+str(sim_id))
            referenced.add(sim_id)
            norm=jobmap[sim_id]
            need(norm["workflow"]==workflow["workflow"],
                 "SIM_JOB_WORKFLOW_DRIFT:"+sim_id)
            job=parsed["jobs"][source_id]
            need(job["if"]==row["if"],
                 "SOURCE_IF_DRIFT:"+sim_id)
            need(job["runs_on"]==row["runs_on"],
                 "SOURCE_RUNNER_DRIFT:"+sim_id)
            need(job["needs"]==list(row["needs"]),
                 "SOURCE_NEEDS_DRIFT:"+sim_id)
            actual_needs=[mapped[dep]["job"] for dep in job["needs"]]
            need(set(actual_needs)==set(norm["needs"]),
                 "SIM_NEEDS_DRIFT:"+sim_id)
            job_source[sim_id]={"workflow":workflow["workflow"],
                                "path":workflow["path"],"source_job":source_id,
                                "if":job["if"],"needs_literal":job["needs_literal"]}
            evidence.append({"job":sim_id,"workflow":workflow["workflow"],
                             "workflow_sha256":digest,"source_job":source_id,
                             "if_literal":job["if"],"needs":actual_needs})
    need(referenced==set(jobmap),"MISSING_SIMULATED_SOURCE_JOB")
    anchored=set()
    oracles=[]
    for oracle in source_map["oracle_files"]:
        src,digest=local_file(root,oracle["path"])
        need(digest==oracle["sha256"],"ORACLE_DIGEST_MISMATCH:"+oracle["path"])
        for check in oracle["checks"]:
            sim_id=check["job"]
            need(sim_id in job_source and sim_id not in anchored,
                 "MISSING_OR_DUPLICATE_ORACLE_MAPPING:"+sim_id)
            ref=job_source[sim_id]
            anchors,strings=oracle_assertions(src,check["function"])
            mandatory={ref["path"],"  "+ref["source_job"]+":"}
            if ref["if"] is not None:mandatory.add("    if: "+ref["if"])
            if ref["needs_literal"] is not None:mandatory.add(ref["needs_literal"])
            need(ref["path"] in strings,
                 "ORACLE_WORKFLOW_PATH_UNBOUND:"+sim_id)
            need(mandatory-{ref["path"]} <= anchors,
                 "ORACLE_ASSERTION_DRIFT:"+sim_id)
            anchored.add(sim_id)
            oracles.append({"job":sim_id,"oracle_path":oracle["path"],
                            "oracle_sha256":digest,"function":check["function"],
                            "static_anchor_count":len(mandatory)-1,
                            "executed":False})
    need(anchored==set(jobmap),"UNBOUND_CONFORMANCE_JOB")
    return {"schema_version":1, "status":"STATIC_SOURCE_RECONCILED",
            "design":design["id"],"claimed_source_revision":source_map["source_revision"],
            "workflow_files":len(source_map["workflow_files"]),
            "jobs":len(evidence),"oracle_checks":len(oracles),
            "source_evidence":sorted(evidence,key=lambda x:x["job"]),
            "oracle_evidence":sorted(oracles,key=lambda x:x["job"]),
            "provenance":"LOCAL_FILES_SHA256_AS_SUPPLIED_NOT_GIT_AUTHENTICATED",
            "source_git_head_authenticated":False,
            "yaml_effective_semantics_verified":False,
            "compiled_oracle_execution_verified":False,
            "run_conformance_tests_separately":True,
            "nested_commands_reconciled":False,
            "provider_job_dispatch_verified":False,
            "branch_rules_verified":False,
            "proves_live_ci_assurance":False,
            "proves_runner_savings":False,
            "automatic_cutover_authorized":False,
            "limitations":["Only a narrow literal YAML job/trigger subset is parsed.",
                           "Python AST presence is not test execution or source-runtime binding.",
                           "Source digest comparison verifies supplied bytes, not Git provider provenance.",
                           "Reuse/matrix/trigger filters require full host interpretation and HOLD."]}


def load_json(path):
    target=Path(path).absolute()
    need(target.is_file() and not any(p.is_symlink()
         for p in (target,*target.parents)), "invalid or symlinked input")
    need(target.stat().st_size <= MAX_BYTES,"input too large")
    raw=target.read_text(encoding="utf-8")
    return json.loads(raw,object_pairs_hook=unique_pairs,
                      parse_constant=lambda _: (_ for _ in ()).throw(Hold("nonfinite JSON")))


def unique_pairs(pairs):
    result={}
    for k,v in pairs:
        need(k not in result,"duplicate JSON key")
        result[k]=v
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root",required=True)
    p.add_argument("--scenario-input",required=True)
    p.add_argument("--source-map",required=True)
    p.add_argument("--require-pass",action="store_true")
    args=p.parse_args()
    try:
        result=reconcile(args.root,load_json(args.scenario_input),
                         load_json(args.source_map))
        print(json.dumps(result,sort_keys=True))
        return 0
    except (Hold,ValueError,OSError,UnicodeError,KeyError,TypeError) as exc:
        print("CI_SOURCE_RECONCILE_HOLD: "+str(exc),file=sys.stderr)
        return 2


if __name__=="__main__":
    raise SystemExit(main())
