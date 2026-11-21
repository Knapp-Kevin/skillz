#!/usr/bin/env python3
"""Trust-base CI plan, dependency closure, and exact-revision qualification.

Standard-library Python 3.9+ and Git only. The policy/this program must be run
from a trusted base checkout, not from an untrusted PR's modified files.
Does not execute test programs, authorize merges, or establish cost savings.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import time

SHA = re.compile(r"[a-f0-9]{40}(?:[a-f0-9]{24})?\Z")
IDENT = re.compile(r"[a-z][a-z0-9-]{0,63}\Z")
MAX_PATHS = 2000
MAX_NODES = 64
MAX_RULES = 256
MAX_SIZE = 131072


class PlanError(ValueError):
    pass


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()


def distinct(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise PlanError("duplicate key: " + key)
        out[key] = value
    return out


def json_file(path):
    path = Path(path)
    try:
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_SIZE:
            raise PlanError("missing, linked, or oversized JSON input")
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=distinct)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise PlanError("unavailable or malformed JSON") from exc


def safe_path(p):
    return isinstance(p, str) and bool(p) and not p.startswith("/") and (
        "\\" not in p and all(part not in ("", ".", "..") for part in p.split("/"))
        and all(ord(ch) >= 32 and ord(ch) != 127 for ch in p))


def validate_policy(p):
    if not isinstance(p, dict) or set(p) != {
        "schema_version", "groups", "obligations", "always", "full", "rules"}:
        raise PlanError("unexpected policy schema")
    if type(p["schema_version"]) is not int or p["schema_version"] != 1:
        raise PlanError("unsupported policy version")
    groups = p["groups"]
    nodes = p["obligations"]
    rules = p["rules"]
    if (not isinstance(groups, list) or not groups or len(groups) > MAX_NODES
            or not all(isinstance(x, str) and IDENT.fullmatch(x) for x in groups)
            or len(set(groups)) != len(groups)):
        raise PlanError("invalid group inventory")
    if (not isinstance(nodes, dict) or not nodes or len(nodes) > MAX_NODES
            or not isinstance(rules, list) or len(rules) > MAX_RULES):
        raise PlanError("invalid obligation/rule inventory")
    for name, cfg in nodes.items():
        if (not isinstance(name, str) or not IDENT.fullmatch(name)
                or not isinstance(cfg, dict) or set(cfg) != {"group", "needs"}
                or cfg["group"] not in groups or not isinstance(cfg["needs"], list)
                or len(set(cfg["needs"])) != len(cfg["needs"])
                or any(not isinstance(v, str) or v not in nodes for v in cfg["needs"])):
            raise PlanError("invalid obligation or dependency: " + str(name))
    for key in ("always", "full"):
        values = p[key]
        if (not isinstance(values, list) or not values
                or any(not isinstance(x, str) or x not in nodes for x in values)
                or len(values) != len(set(values))):
            raise PlanError("invalid " + key + " obligation set")
    if not set(p["always"]).issubset(p["full"]):
        raise PlanError("full plan cannot drop mandatory baseline")
    for rule in rules:
        if (not isinstance(rule, dict) or set(rule) != {"match", "pattern", "obligations"}
                or rule["match"] not in ("exact", "prefix")
                or not isinstance(rule["pattern"], str)
                or not safe_path(rule["pattern"][:-1] if rule["match"] == "prefix"
                                 and rule["pattern"].endswith("/") else rule["pattern"])
                or rule["match"] == "prefix" and not rule["pattern"].endswith("/")
                or not isinstance(rule["obligations"], list) or not rule["obligations"]
                or any(not isinstance(x, str) or x not in nodes for x in rule["obligations"])):
            raise PlanError("invalid source to obligation binding")
    closure(nodes, nodes.keys())  # All obligations must be acyclic.
    return p


def closure(nodes, required):
    active, finished, visiting = set(), set(), set()

    def visit(name):
        if name in visiting:
            raise PlanError("dependency cycle")
        if name in finished:
            return
        if name not in nodes:
            raise PlanError("unknown obligation: " + str(name))
        visiting.add(name)
        for dep in nodes[name]["needs"]:
            visit(dep)
        visiting.remove(name)
        finished.add(name)
        active.add(name)

    for name in required:
        visit(name)
    return sorted(active)


def critical(p):
    lower = p.lower()
    return (p.startswith((".github/", "ci/", "scripts/ci/", "infra/", "deploy/", "release/"))
            or lower.rsplit("/", 1)[-1] in (
                "agents.md", "claude.md", "codeowners", "security.md",
                "cargo.lock", "cargo.toml", "pyproject.toml",
                "package-lock.json", "package.json", "impact-policy.json", "impact-graph.json")
            or p.endswith((".lock", ".lockb")))


def matches(path, rule):
    return (path == rule["pattern"] if rule["match"] == "exact"
            else path.startswith(rule["pattern"]))


def validate_executor(executor, policy):
    if (not isinstance(executor, dict) or set(executor) != {"schema_version", "commands"}
            or executor["schema_version"] != 1 or not isinstance(executor["commands"], dict)
            or set(executor["commands"]) != set(policy["obligations"])):
        raise PlanError("executor must cover every obligation exactly")
    for name, item in executor["commands"].items():
        if (not isinstance(item, dict) or set(item) != {"argv", "timeout_sec"}
                or not isinstance(item["argv"], list) or not item["argv"]
                or not all(isinstance(a, str) and a and len(a) < 1024
                           and "\0" not in a for a in item["argv"])
                or type(item["timeout_sec"]) is not int
                or not (1 <= item["timeout_sec"] <= 3600)):
            raise PlanError("invalid command for obligation " + name)
    return executor


def ordered(nodes, wanted):
    required = set(wanted)
    done, visiting, output = set(), set(), []
    def walk(name):
        if name in done:
            return
        if name in visiting:
            raise PlanError("obligation dependency cycle")
        visiting.add(name)
        for dep in nodes[name]["needs"]:
            if dep in required:
                walk(dep)
        visiting.remove(name)
        done.add(name)
        output.append(name)
    for key in sorted(required):
        walk(key)
    return output


def make_plan(policy, paths, base, head, merge_base, stage="candidate", executor=None):
    validate_policy(policy)
    if (not all(isinstance(x, str) and SHA.fullmatch(x) for x in (base, head, merge_base))
            or stage not in ("draft", "candidate", "release")):
        raise PlanError("unbound revision or stage")
    if (not isinstance(paths, list) or not paths or len(paths) > MAX_PATHS
            or any(not safe_path(x) for x in paths)):
        raise PlanError("empty, unsupported or unsafe Git diff")
    paths = sorted(set(paths))
    forced = stage == "release"
    roots = set(policy["always"])
    unmatched = []
    for path in paths:
        if critical(path):
            forced = True
        matched = [x for rule in policy["rules"] if matches(path, rule)
                   for x in rule["obligations"]]
        if not matched:
            unmatched.append(path)
            forced = True
        roots.update(matched)
    if forced:
        roots.update(policy["full"])
    obligations = closure(policy["obligations"], roots)
    group_map = {g: sorted(x for x in obligations
                            if policy["obligations"][x]["group"] == g)
                 for g in policy["groups"]}
    doc = {
        "schema_version": 1, "policy_sha256": digest(policy),
        "executor_sha256": digest(validate_executor(executor, policy)) if executor is not None else None, "base": base,
        "head": head, "merge_base": merge_base, "stage": stage,
        "changed_paths": paths, "full": bool(forced), "unmapped": unmatched,
        "obligations": obligations, "group_obligations": group_map,
        "groups": {g: bool(x) for g, x in group_map.items()},
    }
    doc["plan_sha256"] = digest(doc)
    return doc


def git(repo, *args):
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo), "-c", "core.hooksPath=/dev/null",
             "-c", "core.fsmonitor=false", *args],
            stderr=subprocess.DEVNULL, timeout=15).strip()
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise PlanError("exact Git revision or diff unavailable") from exc


def git_plan(policy, repo, base, head, stage, executor=None):
    for ref in (base, head):
        if not SHA.fullmatch(ref):
            raise PlanError("SHA pins must be full commit ids")
        if git(repo, "rev-parse", "--verify", ref + "^{commit}").decode() != ref:
            raise PlanError("SHA pin does not identify exact commit")
    mb = git(repo, "merge-base", base, head).decode()
    # Both additions and deletions must participate. Renames -> delete + add.
    raw = git(repo, "diff", "--no-ext-diff", "--no-renames",
              "--raw", "-z", mb, head)
    chunks = raw.split(b"\0")
    if chunks and chunks[-1] == b"":
        chunks.pop()
    if len(chunks) % 2:
        raise PlanError("malformed NUL-delimited raw diff")
    paths = []
    nonregular = False
    for i in range(0, len(chunks), 2):
        header, path = chunks[i], chunks[i+1]
        cols = header.decode("ascii", errors="strict").split()
        if len(cols) != 5 or cols[4] not in ("A", "M", "D", "T"):
            raise PlanError("unsupported Git raw diff status")
        if cols[0][1:] not in ("100644", "000000") or cols[1] not in ("100644", "000000"):
            nonregular = True
        paths.append(path.decode("utf-8", errors="strict"))
    if nonregular:
        paths.append("__NONREGULAR_GIT_CHANGE__")  # Full, not silence.
    return make_plan(policy, paths, base, head, mb, stage, executor)


def receipt(plan, group, run_id, attempt, execution=None):
    if group not in plan["groups"] or not plan["groups"][group]:
        raise PlanError("receipt attempted for unselected group")
    if not run_id or not str(attempt).isdigit():
        raise PlanError("invalid run context")
    return {
        "schema_version": 1, "group": group, "plan_sha256": plan["plan_sha256"],
        "policy_sha256": plan["policy_sha256"], "head": plan["head"],
        "base": plan["base"], "merge_base": plan["merge_base"],
        "stage": plan["stage"], "run_id": str(run_id), "attempt": str(attempt),
        "obligations": plan["group_obligations"][group],
        "executor_sha256": plan["executor_sha256"],
        "execution": execution if execution is not None else [],
    }


def qualify(policy, plan, observed, expected, run_id, attempt, executor=None):
    """Gate observed trusted CI job conclusions and source-bound receipts.

    Actual command success comes from GitHub needs.*.result. Receipts are
    generated only *after* consumer checks complete. This function cannot
    independently authenticate GitHub or a compromised runner; the caller
    must supply actual job conclusions from a trusted workflow context.
    """
    if (plan != expected or plan.get("policy_sha256") != digest(policy)
            or executor is not None and plan.get("executor_sha256") != digest(executor)):
        raise PlanError("stale, altered, or incomplete plan/current revision")
    if not isinstance(observed, dict) or set(observed) != {"schema_version", "jobs"}:
        raise PlanError("missing job evidence")
    if observed["schema_version"] != 1 or not isinstance(observed["jobs"], dict):
        raise PlanError("invalid job evidence")
    if set(observed["jobs"]) != set(plan["groups"]):
        raise PlanError("missing or extra group evidence")
    for group, wanted in plan["groups"].items():
        item = observed["jobs"][group]
        if not isinstance(item, dict) or set(item) != {"result", "receipt"}:
            raise PlanError("invalid job result shape: " + group)
        if wanted:
            if item["result"] != "success":
                raise PlanError("missing/skipped/failed selected group: " + group)
            actual = item["receipt"]
            if not isinstance(actual, dict) or set(actual) != set(receipt(plan, group, run_id, attempt)):
                raise PlanError("wrong receipt shape: " + group)
            if {k: v for k, v in actual.items() if k != "execution"} != {
                    k: v for k, v in receipt(plan, group, run_id, attempt).items()
                    if k != "execution"}:
                raise PlanError("wrong revision/run/obligations receipt: " + group)
            if executor is not None:
                execution = actual["execution"]
                names = ordered(policy["obligations"], plan["group_obligations"][group])
                if (not isinstance(execution, list) or len(execution) != len(names)
                        or [item.get("obligation") if isinstance(item, dict) else None
                            for item in execution] != names):
                    raise PlanError("missing or reordered individual obligation: " + group)
                for item in execution:
                    name = item["obligation"]
                    expected_command = executor["commands"][name]
                    if (set(item) != {"obligation", "exit_code", "argv_sha256", "elapsed_ms"}
                            or type(item["exit_code"]) is not int or item["exit_code"] != 0
                            or item["argv_sha256"] != digest(expected_command["argv"])
                            or type(item["elapsed_ms"]) is not int or item["elapsed_ms"] < 0):
                        raise PlanError("obligation execution unverified: " + name)
            elif actual["execution"]:
                raise PlanError("unverifiable execution without executor manifest")
        elif item["result"] != "skipped" or item["receipt"] not in (None, ""):
            raise PlanError("unselected group unexpectedly executed: " + group)
    return {"qualified": True, "head": plan["head"],
            "plan_sha256": plan["plan_sha256"], "groups": sorted(
                name for name, enabled in plan["groups"].items() if enabled)}


def execute(policy, executor, plan, group, workdir, run_id, attempt):
    if plan.get("executor_sha256") != digest(validate_executor(executor, policy)):
        raise PlanError("executor manifest does not match selected plan")
    if group not in plan["groups"] or not plan["groups"][group]:
        raise PlanError("cannot execute unselected obligation group")
    if plan.get("plan_sha256") != digest({k:v for k,v in plan.items()
                                             if k != "plan_sha256"}):
        raise PlanError("plan digest mismatch")
    root = Path(workdir).resolve(strict=True)
    if not root.is_dir():
        raise PlanError("workspace unavailable")
    observations = []
    for name in ordered(policy["obligations"], plan["group_obligations"][group]):
        cfg = executor["commands"][name]
        start = time.monotonic()
        try:
            completed = subprocess.run(cfg["argv"], cwd=root, shell=False,
                                      timeout=cfg["timeout_sec"], check=False,
                                      stdout=sys.stderr, stderr=sys.stderr)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise PlanError("obligation execution unavailable: " + name) from exc
        elapsed = int((time.monotonic()-start)*1000)
        if completed.returncode != 0:
            raise PlanError("obligation failed (no success receipt): " + name)
        observations.append({"obligation":name, "exit_code":0,
                             "argv_sha256":digest(cfg["argv"]), "elapsed_ms":elapsed})
    return receipt(plan, group, run_id, attempt, observations)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    subs = ap.add_subparsers(dest="command", required=True)
    create = subs.add_parser("plan")
    check = subs.add_parser("qualify")
    rec = subs.add_parser("receipt")
    run = subs.add_parser("execute")
    for command in (create, check):
        command.add_argument("--executor", required=True)
        command.add_argument("--policy", required=True)
        command.add_argument("--repo", required=True)
        command.add_argument("--base", required=True)
        command.add_argument("--head", required=True)
        command.add_argument("--stage", choices=("draft", "candidate", "release"), default="candidate")
    create.add_argument("--github-output")
    create.add_argument("--file")
    check.add_argument("--plan", required=True)
    check.add_argument("--evidence", required=True)
    check.add_argument("--run-id", required=True)
    check.add_argument("--attempt", required=True)
    run.add_argument("--plan", required=True)
    run.add_argument("--policy", required=True)
    run.add_argument("--executor", required=True)
    run.add_argument("--group", required=True)
    run.add_argument("--workdir", required=True)
    run.add_argument("--run-id", required=True)
    run.add_argument("--attempt", required=True)
    run.add_argument("--github-output")
    rec.add_argument("--plan", required=True)
    rec.add_argument("--group", required=True)
    rec.add_argument("--run-id", required=True)
    rec.add_argument("--attempt", required=True)
    rec.add_argument("--github-output")
    args = ap.parse_args(argv)
    if args.command == "receipt":
        obj = receipt(json_file(args.plan), args.group, args.run_id, args.attempt)
    elif args.command == "execute":
        policy = validate_policy(json_file(args.policy))
        executor = validate_executor(json_file(args.executor), policy)
        obj = execute(policy, executor, json_file(args.plan), args.group,
                      args.workdir, args.run_id, args.attempt)
    else:
        policy = validate_policy(json_file(args.policy))
        executor = validate_executor(json_file(args.executor), policy)
        exact = git_plan(policy, Path(args.repo), args.base, args.head, args.stage, executor)
        if args.command == "plan":
            obj = exact
        else:
            obj = qualify(policy, json_file(args.plan), json_file(args.evidence),
                          exact, args.run_id, args.attempt, executor)
    result = canonical(obj)
    print(result)
    if getattr(args, "file", None):
        Path(args.file).write_text(result + "\n", encoding="utf-8")
    if getattr(args, "github_output", None):
        # All dynamic values are encoded as a single JSON line, never shell.
        key = "plan_json" if args.command == "plan" else "receipt_json"
        with Path(args.github_output).open("a", encoding="utf-8") as f:
            f.write(key + "=" + result + "\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (PlanError, UnicodeError, OSError) as exc:
        print("CI_PLAN_UNQUALIFIED: " + str(exc), file=sys.stderr)
        sys.exit(2)
