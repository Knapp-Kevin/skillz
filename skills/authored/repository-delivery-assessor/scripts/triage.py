#!/usr/bin/env python3
"""Offline, read-only, source-bound GitHub PR pulse triage. No API calls."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys

MAX_SIZE = 1024 * 1024
REPO = re.compile(r"^[A-Za-z0-9_.-]{1,80}/[A-Za-z0-9_.-]{1,100}$")
SHA = re.compile(r"^[0-9a-fA-F]{40}$")
IDENT = re.compile(r"^[A-Za-z0-9_.\[\]-]{1,100}$")
CHECK_NAME = re.compile(r"^[^\x00-\x1f\x7f]{1,120}$")
STATUSES = {"success", "failure", "timed_out", "action_required", "cancelled", "skipped", "neutral", "pending", "queued", "in_progress", "unknown"}
FAILING = {"failure", "timed_out", "action_required"}
WAITING = {"pending", "queued", "in_progress"}


class InvalidInput(ValueError):
    pass


def require(cond, msg):
    if not cond:
        raise InvalidInput(msg)


def object_fields(v, allowed, at):
    require(isinstance(v, dict), f"{at}: object expected")
    require(not (set(v) - set(allowed)), f"{at}: unsupported keys")


def text_id(v, pattern, label):
    require(isinstance(v, str) and bool(pattern.fullmatch(v)), f"{label}: invalid")
    return v


def timestamp(value, at):
    if value is None:
        return None
    require(isinstance(value, str) and len(value) <= 40, f"{at}: UTC timestamp required")
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise InvalidInput(f"{at}: invalid timestamp") from exc
    require(dt.tzinfo is not None and dt.utcoffset().total_seconds() == 0, f"{at}: explicit UTC offset required")
    return dt.astimezone(timezone.utc)


def no_duplicates(values, at):
    require(len(values) == len(set(values)), f"{at}: duplicate entries")


def check_pr(pr, operator):
    object_fields(pr, {"number", "state", "head_sha", "draft", "author", "review_requests", "checks", "checks_complete", "required_checks", "required_checks_verified"}, "pr")
    n = pr.get("number")
    require(type(n) is int and n > 0, "pr.number: positive integer required")
    require(pr.get("state") == "OPEN", f"pr #{n}: only open PRs belong to a current pulse")
    sha = text_id(pr.get("head_sha"), SHA, "pr.head_sha").lower()
    require(type(pr.get("draft")) is bool, "pr.draft: boolean required")
    author = text_id(pr.get("author"), IDENT, "pr.author")
    requests = pr.get("review_requests")
    require(isinstance(requests, list) and len(requests) <= 50, "pr.review_requests: bounded list required")
    reviewers = [text_id(q, IDENT, "requested reviewer") for q in requests]
    no_duplicates(reviewers, "requested reviewers")
    require(type(pr.get("checks_complete")) is bool, "pr.checks_complete: explicit boolean required")
    require(type(pr.get("required_checks_verified")) is bool, "pr.required_checks_verified: explicit boolean required")
    names = pr.get("required_checks")
    require(isinstance(names, list) and len(names) <= 100, "required_checks: bounded list required")
    required = [text_id(x, CHECK_NAME, "required check name") for x in names]
    no_duplicates(required, "required checks")
    checks = pr.get("checks")
    require(isinstance(checks, list) and len(checks) <= 300, "pr.checks: bounded list required")
    by_name = {}
    for x in checks:
        object_fields(x, {"name", "head_sha", "conclusion"}, "check")
        name = text_id(x.get("name"), CHECK_NAME, "check.name")
        ref = text_id(x.get("head_sha"), SHA, "check.head_sha").lower()
        conclusion = x.get("conclusion")
        require(isinstance(conclusion, str) and conclusion in STATUSES, "check.conclusion: invalid")
        by_name.setdefault(name, []).append({"head_sha":ref, "conclusion": conclusion})
    results = {}
    for name in sorted(set(required) | set(by_name)):
        versions = by_name.get(name, [])
        at_head = [v["conclusion"] for v in versions if v["head_sha"] == sha]
        old = len(versions) - len(at_head)
        # Distinct attempts with same name are not silently treated as a successful protected gate.
        if len(at_head) > 1:
            status = "AMBIGUOUS_AT_HEAD"
        elif len(at_head) == 1:
            status = at_head[0].upper()
        else:
            status = "STALE_ONLY" if old else "MISSING"
        results[name] = {"at_head":status, "older_revision_count":old, "required_as_supplied":name in required}
    known_failing = sorted(n for n, s in results.items() if s["at_head"].lower() in FAILING)
    known_pending = sorted(n for n, s in results.items() if s["at_head"].lower() in WAITING)
    if not pr["required_checks_verified"]:
        gate = "REQUIRED_SET_NOT_VERIFIED"
    elif not pr["checks_complete"]:
        gate = "CHECK_INVENTORY_INCOMPLETE"
    elif not required:
        gate = "NO_REQUIRED_CHECKS_DEFINED"
    elif any(results[n]["at_head"] in {"FAILURE", "TIMED_OUT", "ACTION_REQUIRED"} for n in required):
        gate = "REQUIRED_CHECK_FAILED"
    elif any(results[n]["at_head"] in {"PENDING", "QUEUED", "IN_PROGRESS"} for n in required):
        gate = "REQUIRED_CHECK_PENDING"
    elif any(results[n]["at_head"] != "SUCCESS" for n in required):
        gate = "REQUIRED_CHECK_UNVERIFIED"
    else:
        gate = "REQUIRED_CHECKS_PASS_AT_HEAD_ONLY"
    return {
        "number":n, "head_sha":sha, "draft":pr["draft"], "author_is_operator":author.casefold() == operator.casefold(),
        "requested_operator_review":operator.casefold() in {q.casefold() for q in reviewers} and not pr["draft"],
        "check_evidence":results, "required_check_gate":gate,
        "known_failing_checks":known_failing, "known_pending_checks":known_pending,
        "not_checked": (["CHECK_INVENTORY_INCOMPLETE"] if not pr["checks_complete"] else []) +
                       (["REQUIRED_CHECK_SET_NOT_VERIFIED"] if not pr["required_checks_verified"] else []),
        "release_or_user_outcome_verified":False,
    }


def triage(doc):
    object_fields(doc, {"schema_version", "operator", "as_of_utc", "quiet_days", "authorized_repositories", "repositories"}, "root")
    require(type(doc.get("schema_version")) is int and doc["schema_version"] == 1, "schema_version: expected 1")
    operator = text_id(doc.get("operator"), IDENT, "operator")
    as_of = timestamp(doc.get("as_of_utc"), "as_of_utc")
    require(as_of is not None, "as_of_utc: required")
    days = doc.get("quiet_days")
    require(type(days) is int and 1 <= days <= 365, "quiet_days: 1..365 required")
    permitted = doc.get("authorized_repositories")
    require(isinstance(permitted, list) and 1 <= len(permitted) <= 100, "authorized_repositories: 1..100 required")
    allowed = [text_id(x, REPO, "authorized repository") for x in permitted]
    no_duplicates(allowed, "authorized_repositories")
    repositories = doc.get("repositories")
    require(isinstance(repositories, list) and len(repositories) <= len(allowed), "repositories: bounded list required")
    output, seen = [], set()
    for item in repositories:
        object_fields(item, {"name", "source_revision", "last_push_utc", "prs", "prs_complete"}, "repository")
        name = text_id(item.get("name"), REPO, "repository.name")
        require(name in allowed, "repository is not in authorized allowlist")
        require(name not in seen, "duplicate repository")
        seen.add(name)
        text_id(item.get("source_revision"), SHA, "repository.source_revision")
        require(type(item.get("prs_complete")) is bool, "prs_complete must be explicit boolean")
        last = timestamp(item.get("last_push_utc"), f"{name}.last_push_utc")
        if last is None:
            activity = "UNKNOWN"
        elif last > as_of:
            activity = "FUTURE_TIMESTAMP_UNTRUSTED"
        else:
            activity = "QUIET" if (as_of-last).total_seconds() > days*86400 else "ACTIVE"
        prs = item.get("prs")
        require(isinstance(prs, list) and len(prs) <= 200, "prs: bounded list required")
        checked = [check_pr(p, operator) for p in prs]
        no_duplicates([x["number"] for x in checked], f"{name}.prs")
        needs_you = [f"PR #{p['number']}: explicitly requested review" for p in checked if p["requested_operator_review"]]
        blocked_checks = [f"PR #{p['number']}: {p['required_check_gate']}" for p in checked if p["required_check_gate"] in {"REQUIRED_CHECK_FAILED", "REQUIRED_CHECK_PENDING", "REQUIRED_CHECK_UNVERIFIED", "CHECK_INVENTORY_INCOMPLETE"}]
        notes = ([] if item["prs_complete"] else ["OPEN_PR_ENUMERATION_INCOMPLETE"])
        notes += [f"PR #{p['number']}: {s}" for p in checked for s in p["not_checked"]]
        output.append({"repository":name,"source_revision":item["source_revision"].lower(), "activity":activity,
                       "last_push_utc":item.get("last_push_utc"), "needs_you":needs_you, "delivery_blockers":blocked_checks,
                       "open_prs":checked,"not_checked":notes+["LOCAL_WORKTREE_NOT_ASSESSED", "DEPLOYMENT_AND_USER_OUTCOME_NOT_ASSESSED"]})
    missing = sorted(set(allowed)-seen)
    return {"schema_version":1, "as_of_utc":doc["as_of_utc"], "authorized_repositories":allowed,
            "not_enumerated":missing, "results":output, "needs_you": [{"repository":r["repository"],"item":x} for r in output for x in r["needs_you"]],
            "quiet_repositories":[r["repository"] for r in output if r["activity"] == "QUIET"],
            "scope_limits":"No network reads, private data retrieval, local working tree verification, branch deletion, CI mutation, deployment or user outcome verification. Check-requiredness must be separately authenticated by the host."}


def pairs(pairs):
    out={}
    for k,v in pairs:
        if k in out:
            raise InvalidInput("duplicate JSON key")
        out[k]=v
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        # Reject linked input path/ancestor before stat/open. An isolated,
        # immutable host snapshot is required against concurrent races.
        source = args.input.absolute()
        if any(part.is_symlink() for part in (source, *source.parents)):
            raise InvalidInput("symlinked input or ancestor")
        if source.stat().st_size > MAX_SIZE:
            raise InvalidInput("input exceeds 1MiB")
        with source.open("r",encoding="utf-8") as f:
            doc = json.load(f,object_pairs_hook=pairs,parse_constant=lambda _: (_ for _ in ()).throw(InvalidInput("invalid numeric constant")))
        result = triage(doc)
    except (InvalidInput, OSError, ValueError, UnicodeError) as exc:
        print("INVALID_INPUT: " + str(exc),file=sys.stderr)
        return 2
    print(json.dumps(result,indent=2,ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
