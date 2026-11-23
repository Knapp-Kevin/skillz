#!/usr/bin/env python3
"""Read-only, offline reconciliation of two explicitly supplied curation snapshots.

This is a deterministic evidence-delta helper, not a filesystem scanner, an
access checker, a scheduler, a memory service, or an authority to change files.
Python 3.9+ standard library only.
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import stat
import sys

MAX_BYTES = 1024 * 1024
MAX_RECORDS = 500
TOKEN = re.compile(r"^[a-z][a-z0-9._:-]{1,95}$")
REVISION = re.compile(r"^[A-Za-z0-9._:@/-]{1,128}$")
DIGEST = re.compile(r"^[a-f0-9]{64}$")
TOP = {"schema_version", "snapshot_id", "observed_at", "scope",
       "coverage", "viewer_check", "records"}
SCOPE = {"collection_id", "root_id", "principal_id", "audience_id"}
RECORD = {"record_id", "source_revision", "locator_token",
          "extraction", "digest", "digest_basis", "viewer_check"}
COVERAGES = {"complete", "partial"}
ACCESS = {"current-authorized", "denied", "unknown"}
EXTRACTIONS = {"none", "metadata", "excerpt", "complete"}
DIGEST_BASIS = {"not-computed", "observed-full-bytes", "source-attested"}
ORDER = {"none": 0, "metadata": 1, "excerpt": 2, "complete": 3}


class Invalid(Exception):
    pass


def check(ok):
    if not ok:
        raise Invalid("INVALID_SNAPSHOT")


def token(value):
    check(type(value) is str and TOKEN.fullmatch(value) is not None)
    return value


def timestamp(value):
    check(type(value) is str and len(value) <= 40)
    try:
        parsed = dt.datetime.fromisoformat(value)
    except (ValueError, TypeError) as exc:
        raise Invalid("INVALID_SNAPSHOT") from exc
    check(parsed.tzinfo is not None and parsed.utcoffset() is not None)
    return parsed


def validate(snapshot):
    check(type(snapshot) is dict and set(snapshot) == TOP)
    check(type(snapshot["schema_version"]) is int and
          snapshot["schema_version"] == 1)
    token(snapshot["snapshot_id"])
    stamp = timestamp(snapshot["observed_at"])
    scope = snapshot["scope"]
    check(type(scope) is dict and set(scope) == SCOPE)
    for value in scope.values():
        token(value)
    check(type(snapshot["coverage"]) is str and
          snapshot["coverage"] in COVERAGES)
    check(type(snapshot["viewer_check"]) is str and
          snapshot["viewer_check"] in ACCESS)
    rows = snapshot["records"]
    check(type(rows) is list and len(rows) <= MAX_RECORDS)
    by_id = {}
    for row in rows:
        check(type(row) is dict and set(row) == RECORD)
        key = token(row["record_id"])
        check(key not in by_id)
        token(row["locator_token"])
        check(type(row["viewer_check"]) is str and
              row["viewer_check"] in ACCESS)
        check(type(row["extraction"]) is str and
              row["extraction"] in EXTRACTIONS)
        revision = row["source_revision"]
        if revision is not None:
            check(type(revision) is str and REVISION.fullmatch(revision) is not None)
        digest = row["digest"]
        basis = row["digest_basis"]
        check(type(basis) is str and basis in DIGEST_BASIS)
        if basis == "not-computed":
            check(digest is None)
        else:
            check(type(digest) is str and DIGEST.fullmatch(digest) is not None)
        # A source-attested digest is not an independently observed hash.
        by_id[key] = row
    return scope, stamp, by_id


def outcome(state, **details):
    return {"status": state, **details}


def reconcile(previous, current):
    current_scope, current_time, now = validate(current)
    if current["viewer_check"] != "current-authorized" or any(
        row["viewer_check"] != "current-authorized" for row in now.values()
    ):
        # No private identifiers, counts, metadata or source-revision values
        # leave the output when authorization is unavailable.
        return outcome("ACCESS_HOLD", actions=[])

    if previous is not None:
        old_scope, old_time, old = validate(previous)
        check(old_scope == current_scope)
        # A previous access grant must not be treated as a current grant.
        # A historical prior with an unknown/denied viewer state is not
        # a reliable baseline for recovering cached private information.
        if previous["viewer_check"] != "current-authorized" or any(
            row["viewer_check"] != "current-authorized" for row in old.values()
        ):
            return outcome("BASELINE_ACCESS_HOLD", actions=[])
        if current["snapshot_id"] == previous["snapshot_id"]:
            check(current == previous)
            return outcome("SAME_SNAPSHOT_NO_WORK", actions=[],
                           checkpoint_written=False)
        check(current_time > old_time)
    else:
        old = {}

    # Identity is source-scoped, not path-derived. Deletion never follows
    # from a record's absence, even in a confirmed complete source listing.
    actions = []
    stats = {}
    def note(code, record_id):
        actions.append({"class": code, "record_id": record_id})
        stats[code] = stats.get(code, 0) + 1

    for key in sorted(now):
        record = now[key]
        if key not in old:
            note("NEW_RECORD_REVIEW", key)
            continue
        before = old[key]
        if before["source_revision"] is None or record["source_revision"] is None:
            note("REVISION_UNKNOWN_REVALIDATE", key)
        elif before["source_revision"] != record["source_revision"]:
            note("SOURCE_CHANGED_REVIEW", key)
        elif (before["digest"] is not None and record["digest"] is not None
              and before["digest_basis"] == "observed-full-bytes"
              and record["digest_basis"] == "observed-full-bytes"
              and before["digest"] != record["digest"]):
            # Revision token equality cannot override contradicted observed
            # full-byte content. Do not mark unchanged.
            note("SAME_REVISION_DIGEST_CONFLICT", key)
        elif before["locator_token"] != record["locator_token"]:
            note("LOCATOR_CHANGED_RELINK", key)
        elif ORDER[record["extraction"]] < ORDER[before["extraction"]]:
            note("EXTRACTION_REGRESSION_HOLD", key)
        elif ORDER[record["extraction"]] > ORDER[before["extraction"]]:
            note("EXTRACTION_ENRICHMENT_REVIEW", key)
        elif before["digest"] != record["digest"] or before["digest_basis"] != record["digest_basis"]:
            note("FINGERPRINT_EVIDENCE_CHANGED_REVIEW", key)
        else:
            note("UNCHANGED_NO_REWORK", key)

    if previous is not None:
        for key in sorted(old.keys() - now.keys()):
            note("ABSENT_COMPLETE_SCOPE_REVIEW" if current["coverage"] == "complete"
                 else "NOT_OBSERVED_PARTIAL_SCOPE", key)

    # Bounded advice is not permission to write, delete, index, schedule,
    # upload, or invalidate actual host records.
    rank = {
        "SAME_REVISION_DIGEST_CONFLICT": 0,
        "EXTRACTION_REGRESSION_HOLD": 1,
        "REVISION_UNKNOWN_REVALIDATE": 2,
        "SOURCE_CHANGED_REVIEW": 3,
        "NEW_RECORD_REVIEW": 4,
        "ABSENT_COMPLETE_SCOPE_REVIEW": 5,
        "NOT_OBSERVED_PARTIAL_SCOPE": 6,
        "FINGERPRINT_EVIDENCE_CHANGED_REVIEW": 7,
        "LOCATOR_CHANGED_RELINK": 8,
        "EXTRACTION_ENRICHMENT_REVIEW": 9,
        "UNCHANGED_NO_REWORK": 10,
    }
    actions.sort(key=lambda x: (rank[x["class"]], x["record_id"]))
    return outcome(
        "PROVISIONAL_DELTA_ONLY",
        run_type="BOOTSTRAP" if previous is None else "INCREMENTAL",
        previous_snapshot_id=previous["snapshot_id"] if previous else None,
        current_snapshot_id=current["snapshot_id"],
        coverage=current["coverage"],
        counts={code: stats[code] for code in sorted(stats)},
        changed_count=sum(number for code, number in stats.items()
                          if code != "UNCHANGED_NO_REWORK"),
        actions=[row for row in actions if row["class"] != "UNCHANGED_NO_REWORK"][:10],
        omitted_action_count=max(
            0, sum(number for code, number in stats.items()
                   if code != "UNCHANGED_NO_REWORK") - 10),
        checkpoint_written=False,
        caveats=[
            "All scope, time, revision, digest and access claims came from caller input.",
            "No file, task, index, private memory, scheduled job or approval was changed.",
            "Missing from a listing is not permission or evidence to delete originals.",
        ],
    )


def unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        check(key not in result)
        result[key] = value
    return result


def read_snapshot(name):
    path = pathlib.Path(name).absolute()
    # Lexical checks help against accidental escapes; they are NOT
    # hostile concurrent filesystem/symlink protection.
    for item in [path] + list(path.parents):
        check(not stat.S_ISLNK(item.lstat().st_mode))
    check(path.is_file() and path.stat().st_size <= MAX_BYTES)
    data = path.read_bytes()
    check(len(data) <= MAX_BYTES)
    try:
        return json.loads(data.decode("utf-8"), object_pairs_hook=unique_pairs,
                          parse_constant=lambda x: (_ for _ in ()).throw(Invalid()))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Invalid("INVALID_SNAPSHOT") from exc


def main(argv=None):
    parser = argparse.ArgumentParser(description="Read-only bounded file curation delta")
    parser.add_argument("--current", required=True)
    parser.add_argument("--previous")
    args = parser.parse_args(argv)
    try:
        result = reconcile(read_snapshot(args.previous) if args.previous else None,
                           read_snapshot(args.current))
    except (Invalid, ValueError, KeyError, TypeError, OSError, RecursionError):
        result = outcome("INVALID_SNAPSHOT", actions=[])
        print(json.dumps(result))
        return 2
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
