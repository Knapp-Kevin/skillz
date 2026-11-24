#!/usr/bin/env python3
"""Read-only PR integration triage from normalized caller-provided snapshots.

No GitHub access, mutation, credentials, merge, issue closure, or remote execution.
Python 3.9+ standard library; all status claims are source-stage only.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 1_048_576
MAX_PRS = 256
SHA = re.compile(r"^[0-9a-f]{40}$")
LABEL = re.compile(r"^[A-Za-z0-9_.:/-]{1,128}$")
PATH = re.compile(r"^[A-Za-z0-9_.@+ -][A-Za-z0-9_.@+ /-]{0,255}$")
MERGEABILITY = {"clean", "conflicting", "blocked", "unknown"}
REVIEW = {"approved", "pending", "changes_requested", "unknown"}
CHECK = {"success", "failure", "pending", "cancelled", "skipped", "neutral", "unknown"}
QUEUE = {"required", "none", "unknown"}


class Hold(ValueError):
    pass


def need(predicate, reason):
    if not predicate:
        raise Hold(reason)


def fields(value, required, optional=(), label="record"):
    need(isinstance(value, dict), label + ": object required")
    need(set(required).issubset(value), label + ": missing required fields")
    need(not (set(value) - set(required) - set(optional)), label + ": unexpected fields")


def safe_label(value, what):
    need(isinstance(value, str) and LABEL.fullmatch(value) is not None,
         what + ": invalid label")
    return value


def sha(value, what):
    need(isinstance(value, str) and SHA.fullmatch(value) is not None,
         what + ": exact 40-char lowercase SHA required")
    return value


def timestamp(value):
    need(isinstance(value, str) and len(value) <= 40, "invalid observed_at")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise Hold("invalid observed_at") from exc
    need(parsed.tzinfo is not None and parsed.utcoffset() is not None,
         "observed_at requires timezone")


def unique(seq, limit, label):
    need(isinstance(seq, list) and len(seq) <= limit, label + ": invalid/oversize list")
    need(len(seq) == len(set(seq)), label + ": duplicate entries")


def normalized_path(path):
    need(isinstance(path, str) and PATH.fullmatch(path) is not None and
         not path.startswith("/") and not path.endswith("/") and
         not path.startswith("./") and "\\" not in path and
         all(part not in ("", ".", "..") for part in path.split("/")),
         "unsafe or ambiguous touched path")
    return path


def read_json(path):
    p = Path(path).absolute()
    need(p.is_file() and not any(x.is_symlink() for x in (p, *p.parents)),
         "input missing or symlinked")
    need(p.stat().st_size <= MAX_BYTES, "input exceeds one MiB")
    with p.open("rb") as f:
        raw = f.read(MAX_BYTES + 1)
        need(len(raw) <= MAX_BYTES, "input exceeds one MiB")
        return json.loads(raw.decode("utf-8"), object_pairs_hook=unique_keys,
                         parse_constant=lambda _: (_ for _ in ()).throw(Hold("nonfinite JSON")))


def unique_keys(pairs):
    out = {}
    for k, v in pairs:
        need(k not in out, "duplicate JSON key")
        out[k] = v
    return out


def parse(data):
    fields(data, ("schema_version", "repository", "observed_at", "base_branch",
                  "base_sha", "policy", "prs"), label="snapshot")
    need(type(data["schema_version"]) is int and data["schema_version"] == 1,
         "unsupported snapshot schema")
    safe_label(data["repository"], "repository")
    safe_label(data["base_branch"], "base branch")
    timestamp(data["observed_at"])
    sha(data["base_sha"], "base SHA")
    policy = data["policy"]
    fields(policy, ("observed_complete", "merge_queue", "review_required",
                    "required_checks"), label="policy")
    need(type(policy["observed_complete"]) is bool, "nonboolean policy completeness")
    need(policy["merge_queue"] in QUEUE, "invalid merge queue mode")
    need(type(policy["review_required"]) is bool, "nonboolean review requirement")
    checks = policy["required_checks"]
    need(isinstance(checks, list) and len(checks) <= 64, "invalid required checks")
    required = set()
    for item in checks:
        fields(item, ("name", "app"), label="required check")
        pair = (safe_label(item["name"], "check name"), safe_label(item["app"], "check app"))
        need(pair not in required, "duplicate required check identity")
        required.add(pair)
    prs = data["prs"]
    need(isinstance(prs, list) and len(prs) <= MAX_PRS, "too many PRs")
    by_num = {}
    for pr in prs:
        fields(pr, ("number", "head_sha", "base_sha", "draft", "mergeability",
                    "review", "checks", "depends_on", "touched_paths",
                    "paths_complete", "issue_refs"), label="PR")
        n = pr["number"]
        need(type(n) is int and n > 0 and n <= 1_000_000_000, "invalid PR number")
        need(n not in by_num, "duplicate PR number")
        sha(pr["head_sha"], "PR HEAD")
        sha(pr["base_sha"], "PR base SHA")
        need(type(pr["draft"]) is bool, "nonboolean draft")
        need(pr["mergeability"] in MERGEABILITY, "invalid mergeability")
        review = pr["review"]
        fields(review, ("state", "head_sha"), label="review")
        need(review["state"] in REVIEW, "invalid review state")
        need(review["head_sha"] is None or isinstance(review["head_sha"], str),
             "invalid review SHA")
        if review["head_sha"] is not None:
            sha(review["head_sha"], "review HEAD")
        need(isinstance(pr["checks"], list) and len(pr["checks"]) <= 128,
             "unbounded/invalid check list")
        seen = set()
        for check in pr["checks"]:
            fields(check, ("name", "app", "state", "head_sha"), label="check")
            pair = (safe_label(check["name"], "check name"),
                    safe_label(check["app"], "check app"))
            need(pair not in seen, "duplicate check identity in PR " + str(n))
            seen.add(pair)
            need(check["state"] in CHECK, "invalid check state")
            sha(check["head_sha"], "check HEAD")
        unique(pr["depends_on"], MAX_PRS, "dependencies")
        for dep in pr["depends_on"]:
            need(type(dep) is int and dep > 0 and dep != n,
                 "invalid/self PR dependency")
        unique(pr["touched_paths"], 256, "touched paths")
        for path in pr["touched_paths"]:
            normalized_path(path)
        need(type(pr["paths_complete"]) is bool, "nonboolean path completeness")
        unique(pr["issue_refs"], 128, "issue references")
        for i in pr["issue_refs"]:
            need(type(i) is int and i > 0, "invalid issue reference")
        by_num[n] = pr
    return policy, required, by_num


def topological(by_num):
    order = []
    visiting = set()
    visited = set()

    def visit(n):
        if n in visited:
            return
        need(n not in visiting, "DEPENDENCY_CYCLE:" + str(n))
        visiting.add(n)
        for parent in sorted(d for d in by_num[n]["depends_on"] if d in by_num):
            visit(parent)
        visiting.remove(n)
        visited.add(n)
        order.append(n)

    for n in sorted(by_num):
        visit(n)
    return order


def plan(data):
    policy, required, by_num = parse(data)
    order = topological(by_num)
    rows = []
    candidate_numbers = []
    for n in order:
        pr = by_num[n]
        reasons = []
        holds = []
        if not policy["observed_complete"]:
            holds.append("BRANCH_POLICY_NOT_COMPLETELY_OBSERVED")
        if policy["merge_queue"] == "unknown":
            holds.append("MERGE_QUEUE_POLICY_UNKNOWN")
        if pr["base_sha"] != data["base_sha"]:
            holds.append("BASE_REVISION_MISMATCH")
        if pr["draft"]:
            reasons.append("DRAFT_PR")
        if pr["mergeability"] == "conflicting":
            reasons.append("OBSERVED_CONFLICT_NEEDS_REPAIR")
        elif pr["mergeability"] == "blocked":
            reasons.append("PROVIDER_REPORTED_BLOCKED")
        elif pr["mergeability"] == "unknown":
            holds.append("MERGEABILITY_NOT_ESTABLISHED")
        if policy["review_required"]:
            review = pr["review"]
            if review["state"] == "changes_requested":
                reasons.append("REVIEW_CHANGES_REQUESTED")
            elif review["state"] != "approved":
                holds.append("REQUIRED_REVIEW_NOT_APPROVED")
            if review["head_sha"] != pr["head_sha"]:
                holds.append("REVIEW_NOT_BOUND_TO_CURRENT_HEAD")
        observed = {(c["name"], c["app"]): c for c in pr["checks"]}
        for name, app in sorted(required):
            check = observed.get((name, app))
            label = name + "@" + app
            if check is None:
                holds.append("REQUIRED_CHECK_NOT_OBSERVED:" + label)
            elif check["head_sha"] != pr["head_sha"]:
                holds.append("STALE_CHECK_HEAD:" + label)
            elif check["state"] == "failure":
                reasons.append("REQUIRED_CHECK_FAILED:" + label)
            elif check["state"] != "success":
                holds.append("REQUIRED_CHECK_NOT_CONFIRMED_SUCCESS:" + label)
        if pr["depends_on"]:
            for dep in sorted(pr["depends_on"]):
                if dep not in by_num:
                    holds.append("DEPENDENCY_NOT_IN_OPEN_SNAPSHOT_OR_PROVEN_MERGED:#" + str(dep))
                else:
                    holds.append("WAIT_FOR_PARENT_INTEGRATION_AND_REFRESH:#" + str(dep))
        if not pr["paths_complete"]:
            holds.append("CHANGED_PATH_INVENTORY_INCOMPLETE")
        overlapping = []
        for other_n, other in sorted(by_num.items()):
            if other_n == n or not (pr["paths_complete"] and other["paths_complete"]):
                continue
            common = sorted(set(pr["touched_paths"]) & set(other["touched_paths"]))
            if common:
                overlapping.append({"with_pr": other_n, "paths": common})
        if reasons:
            state = "BLOCKED"
        elif holds:
            state = "HOLD_RECHECK"
        else:
            state = "LIVE_RECHECK_CANDIDATE"
            candidate_numbers.append(n)
        rows.append({"number": n, "claimed_head_sha": pr["head_sha"],
                     "state": state, "blocking_reasons": sorted(set(reasons)),
                     "unverified_requirements": sorted(set(holds)),
                     "overlapping_paths_advisory": overlapping,
                     "declared_issue_refs_not_closed": sorted(pr["issue_refs"]),
                     "next_required_action": (
                         "FIX_BLOCKERS_AND_RECAPTURE" if reasons else
                         "GATHER_MISSING_OR_UPDATED_EVIDENCE" if holds else
                         "FETCH_LIVE_PR_HEAD_RULESETS_CHECKS_REVIEWS_AND_MERGE_QUEUE")})
    return {"schema_version": 1, "status": "STATIC_INTEGRATION_PLAN_ONLY",
            "claimed_repository": data["repository"],
            "claimed_base_sha": data["base_sha"],
            "claimed_observed_at": data["observed_at"],
            "declared_merge_queue_mode": policy["merge_queue"],
            "plan_order": order, "first_recheck_candidate": (
                candidate_numbers[0] if candidate_numbers else None),
            "prs": rows, "live_provider_verified": False,
            "actual_merge_eligibility_verified": False,
            "review_and_security_rules_independently_verified": False,
            "merge_queue_group_ci_verified": False,
            "merge_performed": False, "postmerge_delivery_verified": False,
            "issues_closed": False,
            "mandatory_follow_up": "After any merge or change of HEAD/base, re-fetch and re-evaluate all dependent PRs at their new exact HEAD. Independently verify merge, release/product outcome, and every issue before closure."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--require-candidate", action="store_true")
    args = parser.parse_args()
    try:
        output = plan(read_json(args.input))
        print(json.dumps(output, sort_keys=True, indent=2))
        return (3 if args.require_candidate and output["first_recheck_candidate"] is None else 0)
    except Hold as err:
        print("INTEGRATION_HOLD: " + str(err), file=sys.stderr)
        return 2
    except (ValueError, KeyError, TypeError, OSError, UnicodeError, RecursionError):
        print("INTEGRATION_HOLD: malformed or unreadable input", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
