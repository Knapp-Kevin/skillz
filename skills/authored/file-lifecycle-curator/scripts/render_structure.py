#!/usr/bin/env python3
"""Bounded read-only folder-shape visualization from an explicit plan snapshot.

No filesystem enumeration, file writes, permissions, execution or scheduler.
Every observed/verified state is an untrusted caller assertion and displayed
as such. Python 3.9+ standard library only.
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import stat
import sys

MAX_BYTES = 1024 * 1024
MAX_RECORDS = 200
MAX_VISIBLE = 24
SEGMENT = re.compile(r"^[a-z0-9][a-z0-9._-]{0,47}$")
IDENT = re.compile(r"^[a-z][a-z0-9._:-]{1,95}$")
REVISION = re.compile(r"^[A-Za-z0-9._:@/-]{1,128}$")
STATES = {"UNPLANNED", "UNCHANGED", "PROPOSED", "APPROVED",
          "EXECUTED", "VERIFIED", "FAILED", "BLOCKED", "UNKNOWN",
          "ROLLED_BACK"}
TOP = {"schema_version", "plan_id", "plan_revision", "snapshot_id",
       "observed_at", "scope", "viewer_check", "coverage", "records"}
SCOPE = {"collection_id", "root_id", "principal_id", "audience_id"}
ENTRY = {"record_id", "original_path", "observed_path", "target_path",
         "source_revision", "state", "readback", "viewer_check"}
RECEIPT = {"record_id", "plan_id", "plan_revision", "source_revision",
           "destination_path", "integrity", "access", "observed_at"}


class Invalid(Exception):
    pass


def ensure(value):
    if not value:
        raise Invalid("INVALID_PLAN")


def token(value):
    ensure(type(value) is str and IDENT.fullmatch(value) is not None)
    return value


def date(value):
    ensure(type(value) is str and len(value) <= 40)
    try:
        d = dt.datetime.fromisoformat(value)
    except (TypeError, ValueError) as e:
        raise Invalid("INVALID_PLAN") from e
    ensure(d.tzinfo is not None and d.utcoffset() is not None)
    return d


def path(value):
    # Intentionally *render-safe aliases*, not arbitrary host filenames.
    # The authorized host maps a private native path to these labels.
    ensure(type(value) is str and len(value) <= 220)
    parts = value.split("/")
    ensure(1 <= len(parts) <= 6 and
           all(SEGMENT.fullmatch(p) and p not in {".", ".."} for p in parts))
    return value


def validate(data):
    ensure(type(data) is dict and set(data) == TOP)
    ensure(type(data["schema_version"]) is int and data["schema_version"] == 1)
    for field in ("plan_id", "plan_revision", "snapshot_id"):
        token(data[field])
    observed = date(data["observed_at"])
    scope = data["scope"]
    ensure(type(scope) is dict and set(scope) == SCOPE)
    for val in scope.values():
        token(val)
    ensure(type(data["viewer_check"]) is str)
    ensure(data["viewer_check"] in {"current-authorized", "denied", "unknown"})
    ensure(type(data["coverage"]) is str and data["coverage"] in {"complete", "partial"})
    rows = data["records"]
    ensure(type(rows) is list and len(rows) <= MAX_RECORDS)
    ids, records = set(), []
    original, current, destination = set(), set(), set()
    for record in rows:
        ensure(type(record) is dict and set(record) == ENTRY)
        ident = token(record["record_id"])
        ensure(ident not in ids)
        ids.add(ident)
        first = path(record["original_path"])
        actual = path(record["observed_path"])
        planned = record["target_path"]
        if planned is not None:
            planned = path(planned)
        ensure(type(record["viewer_check"]) is str and
               record["viewer_check"] in {"current-authorized", "denied", "unknown"})
        revision = record["source_revision"]
        if revision is not None:
            ensure(type(revision) is str and REVISION.fullmatch(revision) is not None)
        state = record["state"]
        ensure(type(state) is str and state in STATES)
        if state == "UNPLANNED":
            ensure(planned is None and record["readback"] is None)
        elif state == "UNCHANGED":
            ensure(first == actual == planned and record["readback"] is None)
        else:
            ensure(planned is not None and planned != first)
        receipt = record["readback"]
        if state in {"VERIFIED", "ROLLED_BACK"}:
            ensure(type(receipt) is dict and set(receipt) == RECEIPT)
            target = planned if state == "VERIFIED" else first
            ensure(receipt["record_id"] == ident and
                   receipt["plan_id"] == data["plan_id"] and
                   receipt["plan_revision"] == data["plan_revision"] and
                   revision is not None and
                   receipt["source_revision"] == revision and
                   receipt["destination_path"] == target and
                   receipt["integrity"] == "matched" and
                   receipt["access"] == "preserved" and
                   actual == target and date(receipt["observed_at"]) <= observed)
        else:
            ensure(receipt is None)
        for label, container in ((first, original), (actual, current)):
            norm = label.casefold()
            ensure(norm not in container)
            container.add(norm)
        if planned is not None:
            norm = planned.casefold()
            ensure(norm not in destination)
            destination.add(norm)
        records.append(record)
    # A declared file cannot also be a folder. Reject case-insensitive
    # collisions *within supplied records*. External destination presence
    # remains UNKNOWN and must be independently checked by the host.
    for names in (original, current, destination):
        for name in names:
            parts = name.split("/")
            for i in range(1, len(parts)):
                ensure("/".join(parts[:i]) not in names)
    # A target cannot overwrite, become the parent of, or become
    # a child of a currently occupied FILE from another record.
    # Even when the occupant plans to move later, this simple visual
    # contract does not qualify a safe operation ordering. Hold it.
    # This is still only a within-snapshot check, never a global
    # destination collision clearance.
    for proposal in records:
        target = proposal["target_path"]
        if target is None or target == proposal["original_path"]:
            continue
        dest = target.casefold()
        for other in records:
            if other["record_id"] == proposal["record_id"]:
                continue
            existing = other["observed_path"].casefold()
            ensure(dest != existing and
                   not dest.startswith(existing + "/") and
                   not existing.startswith(dest + "/"))
    return observed, records


def checked_view(snapshot, previous=None):
    observed, records = validate(snapshot)
    # No individual ID or count is displayed when a current viewer gate
    # is missing, and no cached private ID can bypass it.
    if snapshot["viewer_check"] != "current-authorized" or any(
        r["viewer_check"] != "current-authorized" for r in records
    ):
        return {"status": "ACCESS_HOLD", "visuals": None}
    if previous is not None:
        prev_time, prior = validate(previous)
        if (previous["viewer_check"] != "current-authorized" or
            any(r["viewer_check"] != "current-authorized" for r in prior)):
            return {"status": "BASELINE_ACCESS_HOLD", "visuals": None}
        ensure(previous["scope"] == snapshot["scope"])
        if (previous["plan_id"], previous["plan_revision"]) != (
            snapshot["plan_id"], snapshot["plan_revision"]
        ):
            return {"status": "REPLAN_REVIEW", "visuals": None}
        if previous["snapshot_id"] == snapshot["snapshot_id"]:
            ensure(previous == snapshot)
            replay = True
        else:
            ensure(observed > prev_time)
            replay = False
        # A previously authorized item that is now missing from a
        # filtered listing might be revoked. Never display old ID/count.
        if {r["record_id"] for r in prior} - {r["record_id"] for r in records}:
            return {"status": "ABSENT_IDENTITY_ACCESS_HOLD", "visuals": None}
        old_by_id = {r["record_id"]: r for r in prior}
        for r in records:
            old = old_by_id.get(r["record_id"])
            if old and (old["original_path"] != r["original_path"] or
                        old["target_path"] != r["target_path"]):
                return {"status": "PLAN_DRIFT_HOLD", "visuals": None}
    else:
        replay = False
        old_by_id = {}
    total_planned = sum(r["target_path"] is not None and
                        r["target_path"] != r["original_path"] for r in records)
    verified = [r for r in records if r["state"] == "VERIFIED"]
    regressions = sorted(r["record_id"] for r in records
                         if r["record_id"] in old_by_id
                         and old_by_id[r["record_id"]]["state"] == "VERIFIED"
                         and r["state"] != "VERIFIED")
    counters = {state: sum(r["state"] == state for r in records)
                for state in sorted(STATES)}
    progress = {
        "verified_relocations": len(verified),
        "planned_relocations": total_planned,
        "percent_of_scoped_plan": (
            round(100 * len(verified) / total_planned, 1)
            if total_planned and snapshot["coverage"] == "complete" else None
        ),
        "denominator_basis": "CALLER_ASSERTED_COMPLETE_SCOPE" if
        snapshot["coverage"] == "complete" else "PARTIAL_SCOPE_NO_PERCENT",
        "state_counts": counters,
        "regressed_record_ids": regressions,
    }
    candidates = sorted(records, key=lambda r: r["record_id"])
    visible = candidates[:MAX_VISIBLE]
    omitted = len(candidates) - len(visible)
    observed_view = [(r["observed_path"], r["state"]) for r in visible]
    # Unplanned files are not erased from the hypothetical final
    # shape. Keep their observed location, visibly tagged as still
    # requiring a placement decision; no imaginary target is created.
    planned_view = [
        (r["target_path"] if r["target_path"] is not None
         else r["observed_path"],
         r["state"] if r["target_path"] is not None
         else "UNPLACED_KEEP_CURRENT")
        for r in visible
    ]
    verified_view = [(r["target_path"], "RECEIPT_ASSERTED") for r in visible
                     if r["state"] == "VERIFIED"]
    def ascii_tree(items, label):
        # Portable indentation fallback; parent directories are explicit.
        root = {}
        for full, status in items:
            node = root
            for part in full.split("/")[:-1]:
                node = node.setdefault(part + "/", {})
            node[full.split("/")[-1] + " (" + status + ")"] = None
        lines = [label]
        def visit(node, depth):
            for name, child in sorted(node.items()):
                lines.append("  " * depth + "- " + name)
                if child is not None:
                    visit(child, depth + 1)
        visit(root, 1)
        if not items:
            lines.append("  (no records in this view)")
        return "\n".join(lines)
    def mermaid(views):
        # Every label is constructed from controlled enums/strict slugs.
        lines = ["flowchart LR"]
        seq = 0
        for prefix, label, items in views:
            root_id = prefix + "_ROOT"
            lines.append("  " + root_id + '["' + label + '"]')
            nodes = {(): root_id}
            for full, state in sorted(items):
                segments = full.split("/")
                for idx in range(1, len(segments) + 1):
                    parts = tuple(segments[:idx])
                    if parts not in nodes:
                        seq += 1
                        n = prefix + "_N" + str(seq)
                        nodes[parts] = n
                        title = segments[idx - 1]
                        if idx == len(segments):
                            title += " (" + state + ")"
                        lines.append("  " + n + '["' + title + '"]')
                        lines.append("  " + nodes[parts[:-1]] + " --> " + n)
        return "\n".join(lines)
    return {
        "status": "SAME_SNAPSHOT_NO_WORK" if replay else "PROVISIONAL_VISUAL_ONLY",
        "snapshot_id": snapshot["snapshot_id"],
        "plan_id": snapshot["plan_id"],
        "plan_revision": snapshot["plan_revision"],
        "coverage": snapshot["coverage"],
        "progress": progress,
        "visuals": {
            "observed": ascii_tree(observed_view, "Observed (caller asserted)"),
            "proposed": ascii_tree(planned_view, "Proposed target (NOT APPLIED)"),
            "verified": ascii_tree(verified_view, "Read-back-attested relocations"),
            "mermaid": mermaid([
                ("O", "Observed (asserted)", observed_view),
                ("P", "Proposed (not applied)", planned_view),
                ("V", "Readback (asserted)", verified_view),
            ]),
            "shown_record_count": len(visible),
            "omitted_record_count": omitted,
            "truncated": omitted > 0,
        },
        "destination_collision_basis": "ONLY_WITHIN_SUPPLIED_RECORDS",
        "checkpoint_written": False,
        "caveats": [
            "Current access, snapshot coverage and read-back receipts are caller assertions.",
            "This diagram is not authority to move, rename, delete or index files.",
            "All source paths are safe display aliases, not validated native destinations.",
        ],
    }


def unique_pairs(pairs):
    obj = {}
    for key, value in pairs:
        ensure(key not in obj)
        obj[key] = value
    return obj


def read_input(name):
    p = pathlib.Path(name).absolute()
    for parent in [p] + list(p.parents):
        ensure(not stat.S_ISLNK(parent.lstat().st_mode))
    ensure(p.is_file() and p.stat().st_size <= MAX_BYTES)
    raw = p.read_bytes()
    ensure(len(raw) <= MAX_BYTES)
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs,
                          parse_constant=lambda _: (_ for _ in ()).throw(Invalid()))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise Invalid("INVALID_PLAN") from exc


def main(argv=None):
    a = argparse.ArgumentParser(description="Read-only file plan visual")
    a.add_argument("--current", required=True)
    a.add_argument("--previous")
    args = a.parse_args(argv)
    try:
        obj = checked_view(read_input(args.current),
                           read_input(args.previous) if args.previous else None)
    except (Invalid, OSError, ValueError, TypeError, KeyError, RecursionError):
        obj = {"status": "INVALID_PLAN", "visuals": None}
        print(json.dumps(obj, sort_keys=True))
        return 2
    print(json.dumps(obj, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
