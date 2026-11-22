#!/usr/bin/env python3
"""Offline CI verification execution-graph audit. Caller supplies inspected graph.

Does not parse live workflows, authenticate receipts, execute commands or
change a repository. Refuses to approve source-only claims as measured savings.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import json
from pathlib import Path
import sys

MAX_BYTES = 1024 * 1024
MAX_NODES = 500
MAX_PATHS = 5000
STAGES = ("draft", "candidate", "release")
KINDS = {"workflow", "job", "recipe", "script", "terminal"}
DECISIONS = {"CONSOLIDATE", "KEEP", "RELOCATE", "VERIFY"}
STATUSES = {"success", "failed", "skipped", "missing", "stale", "not-run"}


class InvalidInput(ValueError):
    pass


def require(test: bool, detail: str) -> None:
    if not test:
        raise InvalidInput(detail)


def shape(obj: object, allowed: set[str], required: set[str], name: str) -> dict:
    require(type(obj) is dict, f"{name}: object required")
    require(required <= obj.keys() and obj.keys() <= allowed, f"{name}: missing/unknown fields")
    return obj


def word(value: object, where: str) -> str:
    require(type(value) is str and 0 < len(value) <= 200 and value.strip() == value,
            f"{where}: nonempty bounded string required")
    return value


def string_list(value: object, where: str, *, allow_empty=True) -> list[str]:
    require(type(value) is list and (allow_empty or bool(value)) and len(value) <= MAX_NODES,
            f"{where}: bounded list required")
    result = [word(v, where) for v in value]
    require(len(set(result)) == len(result), f"{where}: duplicate")
    return result


def parse(doc: object):
    shape(doc, {"schema_version", "revision", "phase", "inventory_complete",
                "unresolved_invocations", "nodes", "required", "qualification", "dispositions"},
          {"schema_version", "revision", "phase", "inventory_complete", "unresolved_invocations",
           "nodes", "required", "qualification", "dispositions"}, "root")
    require(type(doc["schema_version"]) is int and doc["schema_version"] == 1,
            "schema_version: expected 1")
    revision = word(doc["revision"], "revision")
    require(doc["phase"] in {"baseline", "candidate"}, "phase: invalid")
    require(type(doc["inventory_complete"]) is bool, "inventory_complete: boolean required")
    unresolved = string_list(doc["unresolved_invocations"], "unresolved_invocations")
    require(type(doc["nodes"]) is list and 1 <= len(doc["nodes"]) <= MAX_NODES,
            "nodes: 1..500 required")
    nodes = {}
    for raw in doc["nodes"]:
        common = {"id", "kind", "invokes", "stages", "needs", "matrix_expanded",
                  "obligation", "command", "sha", "inputs", "platform", "environment", "toolchain",
                  "trust", "failure_boundary", "equivalence_proven", "independent_assurance", "assurance_receipt",
                  "cost_class", "receipt", "assurance_receipt", "entrypoint", "events", "condition", "repetition_purpose"}
        node = shape(raw, common, {"id", "kind", "invokes"}, "node")
        nid = word(node["id"], "node.id")
        require(nid not in nodes, "duplicate node id")
        require(node["kind"] in KINDS, f"{nid}: unsupported node kind")
        string_list(node["invokes"], f"{nid}.invokes")
        if node["kind"] == "workflow":
            require(type(node.get("entrypoint")) is bool, f"{nid}: explicit entrypoint required")
            string_list(node.get("events"), f"{nid}.events", allow_empty=False)
            if node["entrypoint"]:
                require("workflow_call" not in node["events"] or len(node["events"]) > 1,
                        f"{nid}: reusable-only workflow cannot be direct entrypoint")
        if node["kind"] == "job":
            word(node.get("condition"), f"{nid}.condition")
        if node["kind"] in {"workflow", "job"}:
            string_list(node.get("stages"), f"{nid}.stages", allow_empty=False)
            require(set(node["stages"]) <= set(STAGES), f"{nid}: unknown stage")
            if node["kind"] == "job":
                string_list(node.get("needs"), f"{nid}.needs")
                require(type(node.get("matrix_expanded")) is bool and node["matrix_expanded"],
                        f"{nid}: job matrix must be explicitly expanded")
        if node["kind"] == "terminal":
            require(not node["invokes"], f"{nid}: terminal invokes other nodes")
            fields = {"obligation", "command", "sha", "inputs", "platform", "environment", "toolchain",
                      "trust", "failure_boundary", "equivalence_proven", "independent_assurance", "assurance_receipt",
                      "cost_class", "receipt"}
            require(fields <= node.keys(), f"{nid}: terminal evidence incomplete")
            for fld in ("obligation", "command", "sha", "platform", "toolchain",
                        "trust", "failure_boundary", "cost_class", "environment"):
                word(node[fld], f"{nid}.{fld}")
            require(node["sha"] == revision, f"{nid}: stale source revision")
            string_list(node["inputs"], f"{nid}.inputs", allow_empty=False)
            require(type(node["equivalence_proven"]) is bool,
                    f"{nid}: equivalence_proven must be bool")
            require(type(node["assurance_receipt"]) is str and len(node["assurance_receipt"]) <= 200,
                    f"{nid}: assurance_receipt invalid")
            require(type(node["independent_assurance"]) is str and len(node["independent_assurance"]) <= 240,
                    f"{nid}: independent_assurance invalid")
            require(node.get("repetition_purpose", "") in {"", "nondeterminism"},
                    f"{nid}: unsupported repetition purpose")
            require(node["cost_class"] in {"cheap", "expensive"}, f"{nid}: cost_class invalid")
            require(node["receipt"] in STATUSES, f"{nid}: receipt invalid")
        else:
            require(bool(node["invokes"]), f"{nid}: nonterminal must invoke nodes")
        nodes[nid] = node
    for n in nodes.values():
        for target in n["invokes"]:
            require(target in nodes, f"{n['id']}: unresolved child {target}")
            require(nodes[target]["kind"] != "workflow" or n["kind"] in {"workflow", "job"},
                    f"{n['id']}: reusable workflow must be invoked by workflow or job")
        if n["kind"] == "job":
            for target in n["needs"]:
                require(target in nodes and nodes[target]["kind"] == "job", "needs: unknown job")
    # The supplied invocation graph must be acyclic, even through reusable workflows.
    visiting, visited = set(), set()
    def visit(nid):
        require(nid not in visiting, "invocation cycle")
        if nid in visited:
            return
        visiting.add(nid)
        for target in nodes[nid]["invokes"]:
            visit(target)
        visiting.remove(nid)
        visited.add(nid)
    for nid in nodes:
        visit(nid)
    require(any(n["kind"] == "workflow" and n["entrypoint"] for n in nodes.values()), "no entrypoint workflow inventoried")
    shape(doc["required"], set(STAGES), set(STAGES), "required")
    shape(doc["qualification"], set(STAGES), set(STAGES), "qualification")
    for stage in STAGES:
        required = string_list(doc["required"][stage], f"required.{stage}")
        gate = shape(doc["qualification"][stage], {"required", "exact_revision", "reject_non_success",
                   "trusted", "draft_marker"}, {"required", "exact_revision", "reject_non_success", "trusted"},
                     f"qualification.{stage}")
        require(string_list(gate["required"], f"qualification.{stage}.required") == required,
                f"{stage}: gate does not cover required obligations")
        require(all(type(gate[field]) is bool for field in ("exact_revision", "reject_non_success", "trusted")),
                f"{stage}: gate controls must be explicit booleans")
        if stage == "draft":
            require(gate.get("draft_marker") == "DRAFT_DEFERRED_NOT_QUALIFIED",
                    "draft: explicit nonqualification marker required")
        require(all(gate[fld] for fld in ("exact_revision", "reject_non_success", "trusted")),
                f"{stage}: gate must be trusted, exact-revision and fail closed")
    require(not doc["required"]["draft"], "draft: cannot qualify expensive obligations")
    require(type(doc["dispositions"]) is list and len(doc["dispositions"]) <= MAX_NODES,
            "dispositions: bounded list required")
    decisions = {}
    for d in doc["dispositions"]:
        shape(d, {"stage", "obligation", "decision", "reason"},
              {"stage", "obligation", "decision", "reason"}, "disposition")
        require(d["stage"] in STAGES and d["decision"] in DECISIONS,
                "disposition: unknown stage or decision")
        key = (d["stage"], word(d["obligation"], "obligation"))
        require(key not in decisions and len(word(d["reason"], "reason")) >= 12,
                "disposition: duplicate or insufficient reasoning")
        decisions[key] = d
    return nodes, decisions, unresolved


def audit(doc: dict) -> dict:
    nodes, decisions, unresolved = parse(doc)
    runs = []
    for stage in STAGES:
        for root in sorted((n for n in nodes.values() if n["kind"] == "workflow" and n["entrypoint"]), key=lambda n: n["id"]):
            if stage not in root["stages"]:
                continue
            def walk(nid, path, job):
                node = nodes[nid]
                if node["kind"] in {"workflow", "job"} and stage not in node["stages"]:
                    return
                current_job = nid if node["kind"] == "job" else job
                if node["kind"] == "terminal":
                    require(current_job is not None, f"{nid}: terminal missing job")
                    runs.append({"stage": stage, "workflow": root["id"], "job": current_job,
                                 "path": path, "events": root["events"], "condition": nodes[current_job]["condition"], "obligation": node["obligation"],
                                 "command": node["command"],
                                 "signature": [node[k] for k in ("obligation", "sha", "platform",
                                   "toolchain", "trust", "failure_boundary", "environment")] + [node["inputs"]],
                                 "equivalence_proven": node["equivalence_proven"],
                                 "independent_assurance": node["independent_assurance"],
                                 "assurance_receipt": node["assurance_receipt"],
                                 "repetition_purpose": node.get("repetition_purpose", ""),
                                 "cost_class": node["cost_class"], "receipt": node["receipt"]})
                    require(len(runs) <= MAX_PATHS, "expanded invocation paths exceed 5000")
                else:
                    for child in node["invokes"]:
                        walk(child, path + [child], current_job)
            walk(root["id"], [root["id"]], None)
    # Discover the same logical obligation even when different wrappers call it.
    grouped = defaultdict(list)
    for row in runs:
        grouped[(row["stage"], row["obligation"])].append(row)
    overlaps, violations = [], []
    for (stage, check), records in sorted(grouped.items()):
        if len(records) < 2:
            continue
        signatures = {json.dumps(row["signature"], sort_keys=True) for row in records}
        all_equivalent = all(row["equivalence_proven"] for row in records)
        job_sets = {(row["workflow"], row["job"]) for row in records}
        event_sets = [set(row["events"]) for row in records]
        simultaneous = any(event_sets[i] & event_sets[j] for i in range(len(records)) for j in range(i + 1, len(records)))
        if not simultaneous:
            # Distinct events can coincide (push + PR), but only actual source
            # trigger/run evidence can establish they did on the same revision.
            classification = "UNPROVEN"
        elif (len(signatures) == 1 and all_equivalent
              and all(r["repetition_purpose"] == "nondeterminism"
                      and r["independent_assurance"].strip()
                      and r["assurance_receipt"].strip() for r in records)
              and len({r["assurance_receipt"] for r in records}) == len(records)):
            classification = "JUSTIFIED_REPETITION"
        elif len(signatures) == 1 and all_equivalent:
            # Partial overlap if any overlapping job executes other obligations too.
            job_checks = {
                (x["workflow"], x["job"]): {y["obligation"] for y in runs if
                    y["stage"] == stage and y["workflow"] == x["workflow"] and y["job"] == x["job"]}
                for x in records
            }
            classification = ("PARTIAL_OVERLAP" if len({frozenset(v) for v in job_checks.values()}) > 1
                              else "EXACT_DUPLICATE")
        elif len(signatures) > 1 and len({(r["signature"][2], r["signature"][4], r["signature"][5]) for r in records}) > 1 and all(r["independent_assurance"].strip() and r["assurance_receipt"].strip() for r in records):
            classification = "JUSTIFIED_REPETITION"
        else:
            classification = "UNPROVEN"
        decision = decisions.get((stage, check))
        if not decision:
            violations.append(f"{stage}/{check}: overlap lacks documented disposition")
        elif classification in {"EXACT_DUPLICATE", "PARTIAL_OVERLAP"}:
            if decision["decision"] not in {"CONSOLIDATE", "RELOCATE"}:
                violations.append(f"{stage}/{check}: avoidable overlap cannot be kept")
            violations.append(f"{stage}/{check}: duplicated effective execution still present")
        elif classification == "JUSTIFIED_REPETITION" and decision["decision"] != "KEEP":
            violations.append(f"{stage}/{check}: independently justified repetition must be kept")
        elif classification == "UNPROVEN":
            if decision["decision"] != "VERIFY":
                violations.append(f"{stage}/{check}: equivalence unproven; VERIFY required")
            violations.append(f"{stage}/{check}: overlap equivalence or unique assurance unproven")
        overlaps.append({"stage": stage, "obligation": check, "classification": classification,
                         "invocation_paths": [" > ".join(x["path"]) for x in records],
                         "decision": decision["decision"] if decision else "MISSING",
                         "reason": decision["reason"] if decision else "NOT_DOCUMENTED"})
    for stage in STAGES:
        present = {r["obligation"] for r in runs if r["stage"] == stage}
        if stage == "draft" and "draft-deferred" not in present:
            violations.append("draft: required cheap deferral status not emitted")
        missing = set(doc["required"][stage]) - present
        if missing:
            violations.append(f"{stage}: required verification absent: {','.join(sorted(missing))}")
        for r in runs:
            if r["stage"] != stage:
                continue
            if stage == "draft" and r["cost_class"] != "cheap":
                violations.append(f"draft: expensive work dispatched via {' > '.join(r['path'])}")
            if stage in ("candidate", "release") and r["obligation"] in doc["required"][stage]:
                if r["receipt"] != "success":
                    violations.append(f"{stage}/{r['obligation']}: {r['receipt']} does not qualify")
    if not doc["inventory_complete"] or unresolved:
        violations.append("incomplete source/command inventory or unresolved nested invocation")
    for key in decisions:
        if key not in {(x["stage"], x["obligation"]) for x in overlaps}:
            violations.append(f"{key[0]}/{key[1]}: stale disposition with no observed overlap")
    # A completely empty ready/release path is not a CI qualification.
    for stage in ("candidate", "release"):
        if not any(x["stage"] == stage for x in runs):
            violations.append(f"{stage}: no terminal commands inventoried")
    return {"schema_version": 1, "revision": doc["revision"], "phase": doc["phase"],
            "observed_source_graph_authenticated": False, "real_runner_receipts_authenticated": False,
            "unique_verification_execution_paths": len(runs),
            "execution_inventory": [{k: v for k, v in x.items() if k not in {"signature", "equivalence_proven", "independent_assurance", "assurance_receipt", "repetition_purpose"}} for x in runs],
            "overlaps": overlaps, "violations": sorted(set(violations)),
            "structural_assessment": "PASS" if not violations else "HOLD",
            "optimization_complete": False, "observed_runner_minutes_delta": "NOT_MEASURED",
            "observed_critical_path_delta": "NOT_MEASURED",
            "warning": "Graph, command equivalence, requirement mapping, run status and trust were asserted by the caller, not discovered or authenticated. A PASS is only a bounded offline structural check; source inventory, seeded faults, exact-head branch gates and actual CI cost/outcome receipts are still required."}


def unique_pairs(items):
    output = {}
    for key, value in items:
        require(key not in output, "duplicate JSON key")
        output[key] = value
    return output


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        path = args.input.absolute()
        require(not any(x.is_symlink() for x in (path, *path.parents)), "symlinked input path")
        require(path.stat().st_size <= MAX_BYTES, "input too large")
        with path.open(encoding="utf-8") as stream:
            document = json.load(stream, object_pairs_hook=unique_pairs,
                                 parse_constant=lambda x: (_ for _ in ()).throw(InvalidInput("nonfinite JSON")))
        report = audit(document)
    except (OSError, ValueError, UnicodeError, RecursionError) as exc:
        print(f"INVALID_INPUT: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=True))
    return 0 if report["structural_assessment"] == "PASS" else 3


if __name__ == "__main__":
    sys.exit(main())
