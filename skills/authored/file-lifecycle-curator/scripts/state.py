#!/usr/bin/env python3
"""Opt-in durable, transactionally updated state for File Lifecycle Curator.

This helper stores *caller-supplied assertions* in a user-approved private
SQLite file. It does NOT scan a source, authenticate a viewer, run a schedule,
index content, perform a file move, or make a receipt independently true.
Default preview never creates a file. Python 3.9+ standard library.
"""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import stat
import sys

import reconcile
import render_structure

FORMAT = 1
MAX_CATALOG = 500
MAX_ACCEPTED_RUNS = 100000
CADENCES = {"manual", "hourly", "daily", "weekly"}
SQL_SCHEMA = (
    "CREATE TABLE IF NOT EXISTS curator_state ("
    "singleton INTEGER PRIMARY KEY CHECK(singleton = 1), "
    "format_version INTEGER NOT NULL, "
    "generation INTEGER NOT NULL, "
    "last_run_id TEXT NOT NULL, "
    "last_scan_json TEXT NOT NULL, "
    "catalog_json TEXT NOT NULL, "
    "plan_json TEXT, "
    "state_digest TEXT NOT NULL)",
    "CREATE TABLE IF NOT EXISTS accepted_runs ("
    "generation INTEGER PRIMARY KEY, "
    "run_id TEXT NOT NULL UNIQUE, "
    "cadence TEXT NOT NULL, "
    "snapshot_id TEXT NOT NULL, "
    "payload_digest TEXT NOT NULL, "
    "report_json TEXT NOT NULL)",
)


class Refused(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False)


def digest(obj):
    return hashlib.sha256(canonical(obj).encode("utf-8")).hexdigest()


def refuse(condition, status="INVALID_INPUT"):
    if not condition:
        raise Refused(status)


def read_plan(name):
    if name is None:
        return None
    plan = render_structure.read_input(name)
    render_structure.validate(plan)
    return plan


def private_file_path(name, create=False):
    """Host must select a trusted private directory, not a public repo."""
    p = Path(name).absolute()
    refuse(p.parent.is_dir(), "PRIVATE_STORE_REQUIRED")
    for ancestor in [p.parent] + list(p.parent.parents):
        try:
            refuse(not ancestor.is_symlink(), "UNSAFE_STORE_PATH")
        except OSError as exc:
            raise Refused("UNSAFE_STORE_PATH") from exc
    if os.name == "posix":
        refuse(p.parent.stat().st_mode & 0o077 == 0, "INSECURE_STORE_DIRECTORY")
    if p.exists() or p.is_symlink():
        info = p.lstat()
        refuse(stat.S_ISREG(info.st_mode) and not stat.S_ISLNK(info.st_mode),
               "UNSAFE_STORE_PATH")
        if os.name == "posix":
            refuse(info.st_mode & 0o077 == 0, "INSECURE_STORE_FILE")
        return p
    if not create:
        return p
    flags = os.O_CREAT | os.O_EXCL | os.O_RDWR
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    fd = os.open(str(p), flags, 0o600)
    os.close(fd)
    return p


def connect(p, read_only):
    if read_only:
        # SQLite URI escapes native filesystem path without introducing
        # write-mode initialization or creating -journal side effects.
        conn = sqlite3.connect(p.as_uri() + "?mode=ro", uri=True, timeout=1)
    else:
        conn = sqlite3.connect(str(p), timeout=1, isolation_level=None)
    conn.execute("PRAGMA busy_timeout=1000")
    if not read_only:
        conn.execute("PRAGMA journal_mode=DELETE")
        conn.execute("PRAGMA synchronous=FULL")
    return conn


def read_state(conn):
    try:
        row = conn.execute("SELECT format_version, generation, last_run_id, "
                           "last_scan_json, catalog_json, plan_json, state_digest "
                           "FROM curator_state WHERE singleton=1").fetchone()
    except sqlite3.OperationalError as exc:
        raise Refused("STATE_SCHEMA_HOLD") from exc
    if row is None:
        return None
    version, generation, run_id, raw_scan, raw_catalog, raw_plan, check_digest = row
    try:
        refuse(type(version) is int and version == FORMAT and
               type(generation) is int and generation > 0 and
               type(run_id) is str)
        scan = json.loads(raw_scan, object_pairs_hook=reconcile.unique_pairs)
        catalog = json.loads(raw_catalog, object_pairs_hook=reconcile.unique_pairs)
        plan = (json.loads(raw_plan, object_pairs_hook=reconcile.unique_pairs)
                if raw_plan is not None else None)
        reconcile.validate(scan)
        refuse(type(catalog) is dict and len(catalog) <= MAX_CATALOG)
        for key, entry in catalog.items():
            reconcile.token(key)
            refuse(type(entry) is dict and
                   set(entry) == {"row", "last_seen_id", "last_seen_at"})
            refuse(type(entry["row"]) is dict and
                   entry["row"].get("record_id") == key)
            reconcile.token(entry["last_seen_id"])
            reconcile.timestamp(entry["last_seen_at"])
        # Validate remembered rows too: a partial scan cannot silently
        # turn a malformed cached record into a durable truth claim.
        catalog_scan = copy.deepcopy(scan)
        catalog_scan["records"] = [entry["row"] for entry in catalog.values()]
        reconcile.validate(catalog_scan)
        if plan is not None:
            render_structure.validate(plan)
            refuse(plan["scope"] == scan["scope"])
        expected = digest([version, generation, run_id, scan, catalog, plan])
        refuse(check_digest == expected, "STATE_INTEGRITY_HOLD")
    except (reconcile.Invalid, render_structure.Invalid, ValueError, TypeError,
            KeyError, OverflowError, RecursionError, Refused) as exc:
        raise Refused("STATE_INTEGRITY_HOLD") from exc
    return {"generation": generation, "last_run_id": run_id,
            "scan": scan, "catalog": catalog, "plan": plan}


def previous_catalog_scan(state):
    if state is None:
        return None
    old = copy.deepcopy(state["scan"])
    old["records"] = [copy.deepcopy(item["row"])
                      for _, item in sorted(state["catalog"].items())]
    # Old entries are known history only, not current source presence.
    return old


def guard_plan_observation(incoming, stored, current):
    """Apply the same safety contract to checkpoint writers and host previews.

    Caller timestamps, source IDs, and receipts remain assertions; this
    only prevents contradictory claims from being durably promoted.
    """
    refuse(incoming["coverage"] == current["coverage"],
           "PLAN_COVERAGE_CONFLICT_HOLD")
    source_time = reconcile.timestamp(current["observed_at"])
    refuse(render_structure.date(incoming["observed_at"]) >= source_time,
           "PLAN_BEFORE_SOURCE_HOLD")
    baseline_time = (render_structure.date(stored["observed_at"])
                     if stored is not None else None)
    if stored is not None and (incoming["plan_id"],
                               incoming["plan_revision"]) == (
                                   stored["plan_id"], stored["plan_revision"]):
        previous_ids = {r["record_id"] for r in stored["records"]}
        incoming_ids = {r["record_id"] for r in incoming["records"]}
        refuse(previous_ids == incoming_ids, "PLAN_MEMBERSHIP_CHANGE_HOLD")
    # The plan's timestamp is not a substitute for fresh per-record readback.
    for row in incoming["records"]:
        if row["state"] in {"VERIFIED", "ROLLED_BACK"}:
            when = render_structure.date(row["readback"]["observed_at"])
            refuse(when >= source_time and
                   (baseline_time is None or when > baseline_time),
                   "STALE_OPERATION_READBACK_HOLD")


def guarded_plan(incoming, stored, current, allow_replan):
    if incoming is None:
        return stored, "HISTORICAL_NOT_REVALIDATED" if stored else "NO_PLAN"
    refuse(incoming["scope"] == current["scope"], "CROSS_SCOPE_HOLD")
    if incoming["viewer_check"] != "current-authorized" or any(
        r["viewer_check"] != "current-authorized" for r in incoming["records"]
    ):
        raise Refused("ACCESS_HOLD")
    now = {r["record_id"]: r for r in current["records"]}
    # A private plan cannot show identifiers that the current run did
    # not actually observe and currently permit.
    refuse(all(r["record_id"] in now for r in incoming["records"]),
           "PLAN_SOURCE_ACCESS_HOLD")
    refuse(all(r["source_revision"] == now[r["record_id"]]["source_revision"]
               for r in incoming["records"]), "PLAN_SOURCE_REVISION_HOLD")
    guard_plan_observation(incoming, stored, current)
    if stored is not None:
        same = (stored["plan_id"], stored["plan_revision"]) == (
            incoming["plan_id"], incoming["plan_revision"])
        if not same:
            refuse(allow_replan, "REPLAN_REQUIRES_APPROVAL")
            refuse(render_structure.date(incoming["observed_at"]) >
                   render_structure.date(stored["observed_at"]),
                   "PLAN_TIME_CONFLICT")
        else:
            result = render_structure.checked_view(incoming, stored)
            refuse(result["status"] not in {
                "ABSENT_IDENTITY_ACCESS_HOLD", "BASELINE_ACCESS_HOLD",
                "ACCESS_HOLD", "PLAN_DRIFT_HOLD", "REPLAN_REVIEW",
                "INVALID_PLAN"}, result["status"])
    else:
        result = render_structure.checked_view(incoming)
        refuse(result["status"] not in {"ACCESS_HOLD", "INVALID_PLAN"},
               result["status"])
    return incoming, "CURRENT_CALLER_ASSERTED"


def evaluate(conn, current, plan, run_id, cadence, commit, expected_generation,
             initialize=False, allow_replan=False):
    reconcile.token(run_id)
    refuse(type(cadence) is str and cadence in CADENCES)
    reconcile.validate(current)
    if current["viewer_check"] != "current-authorized" or any(
        row["viewer_check"] != "current-authorized" for row in current["records"]
    ):
        return {"status": "ACCESS_HOLD", "checkpoint_written": False}
    if plan is not None:
        render_structure.validate(plan)
    refuse(not allow_replan or plan is not None, "REPLAN_REQUIRES_PLAN")
    if commit:
        refuse(type(expected_generation) is int and expected_generation >= 0,
               "EXPECTED_GENERATION_REQUIRED")
        conn.execute("BEGIN IMMEDIATE")
    try:
        state = read_state(conn)
        generation = state["generation"] if state is not None else 0
        if state is None:
            refuse(initialize, "COLD_START_REQUIRES_INITIALIZE" if commit
                   else "COLD_START")
        if state is not None and initialize:
            raise Refused("ALREADY_INITIALIZED")
        input_digest = digest([current, plan])
        source_same = False
        if state is not None:
            existing = conn.execute(
                "SELECT payload_digest FROM accepted_runs WHERE run_id=?",
                (run_id,)).fetchone()
            if existing is not None:
                refuse(existing[0] == input_digest, "RUN_ID_REUSE_CONFLICT")
                return {"status": "ALREADY_APPLIED", "generation": generation,
                        "checkpoint_written": False}
            latest = state["scan"]
            # Snapshot IDs identify unique observations within this
            # private collection, not a rotating timestamp label.
            # Reusing an older ID after another accepted snapshot
            # corrupts per-record last_seen bookkeeping.
            historical = conn.execute(
                "SELECT generation FROM accepted_runs "
                "WHERE snapshot_id=? LIMIT 1",
                (current["snapshot_id"],)).fetchone()
            if (historical is not None and
                    current["snapshot_id"] != latest["snapshot_id"]):
                raise Refused("SNAPSHOT_REUSE_CONFLICT")
            if current["snapshot_id"] == latest["snapshot_id"]:
                refuse(current == latest, "SNAPSHOT_REUSE_CONFLICT")
                source_same = True
                if plan is None or plan == state["plan"]:
                    return {"status": "SAME_SNAPSHOT_NO_WORK",
                            "generation": generation, "checkpoint_written": False}
        if commit:
            refuse(expected_generation == generation,
                   "GENERATION_CONFLICT")
        prior = previous_catalog_scan(state)
        if prior is not None:
            refuse(prior["scope"] == current["scope"], "CROSS_SCOPE_HOLD")
        if source_same:
            # A repeated PARTIAL scan cannot classify old unseen
            # catalog members as re-observed unchanged files.
            unseen = len(state["catalog"]) - len(current["records"])
            counts = {"UNCHANGED_NO_REWORK": len(current["records"])}
            if unseen:
                counts["NOT_OBSERVED_PARTIAL_SCOPE"] = unseen
            delta = {"status": "PROVISIONAL_DELTA_ONLY",
                     "changed_count": 0, "counts": counts,
                     "actions": [], "omitted_action_count": 0}
        else:
            delta = reconcile.reconcile(prior, current)
            if delta["status"] != "PROVISIONAL_DELTA_ONLY":
                return {"status": delta["status"], "checkpoint_written": False}
        next_plan, plan_freshness = guarded_plan(
            plan, state["plan"] if state else None, current, allow_replan)
        catalog = copy.deepcopy(state["catalog"]) if state else {}
        for r in current["records"]:
            catalog[r["record_id"]] = {
                "row": r, "last_seen_id": current["snapshot_id"],
                "last_seen_at": current["observed_at"]}
        refuse(len(catalog) <= MAX_CATALOG, "CATALOG_LIMIT_HOLD")
        # The full last-known inventory is retained across PARTIAL
        # snapshots. Missing records are never discarded or certified
        # absent; each retains its last_seen timestamp.
        stale_count = sum(entry["last_seen_id"] != current["snapshot_id"]
                          for entry in catalog.values())
        result = {
            "status": "DRY_RUN" if not commit else "CHECKPOINT_COMMITTED",
            "checkpoint_written": False,
            "generation": generation if not commit else generation + 1,
            "run_type": ("BOOTSTRAP" if state is None else
                         "PLAN_ONLY" if source_same else "INCREMENTAL"),
            "cadence": cadence, "snapshot_id": current["snapshot_id"],
            "delta_status": delta["status"], "changed_count": delta["changed_count"],
            "counts": delta["counts"], "actions": delta["actions"],
            "omitted_action_count": delta["omitted_action_count"],
            "known_catalog_count": len(catalog),
            "not_seen_this_run_count": stale_count,
            "coverage": current["coverage"],
            "plan_freshness": plan_freshness,
            "source_claims": "CALLER_ASSERTED_NOT_INDEPENDENTLY_VERIFIED",
            "source_files_changed": False,
            "scheduled_task_created": False,
        }
        if not commit:
            return result
        refuse(generation < MAX_ACCEPTED_RUNS, "RUN_HISTORY_LIMIT_HOLD")
        new_generation = generation + 1
        value = digest([FORMAT, new_generation, run_id, current,
                        catalog, next_plan])
        if state is None:
            conn.execute(
                "INSERT INTO curator_state VALUES (1,?,?,?,?,?,?,?)",
                (FORMAT, new_generation, run_id, canonical(current),
                 canonical(catalog), canonical(next_plan) if next_plan else None,
                 value))
        else:
            cursor = conn.execute(
                "UPDATE curator_state SET generation=?, last_run_id=?, "
                "last_scan_json=?, catalog_json=?, plan_json=?, state_digest=? "
                "WHERE singleton=1 AND generation=?",
                (new_generation, run_id, canonical(current), canonical(catalog),
                 canonical(next_plan) if next_plan else None, value, generation))
            refuse(cursor.rowcount == 1, "GENERATION_CONFLICT")
        conn.execute(
            "INSERT INTO accepted_runs VALUES (?,?,?,?,?,?)",
            (new_generation, run_id, cadence, current["snapshot_id"], input_digest,
             canonical({
                 "changed_count": result["changed_count"],
                 "counts": result["counts"],
                 "coverage": current["coverage"],
                 "known_catalog_count": len(catalog),
                 "not_seen_this_run_count": stale_count,
                 "plan_freshness": plan_freshness,
                 "planned_relocations": (sum(
                     p["target_path"] is not None and
                     p["target_path"] != p["original_path"]
                     for p in next_plan["records"]) if plan is not None else None),
                 "receipt_asserted_verified": (sum(
                     p["state"] == "VERIFIED" for p in next_plan["records"])
                     if plan is not None else None),
             })))
        conn.commit()
        written = read_state(conn)
        refuse(written is not None and
               written["generation"] == new_generation and
               written["last_run_id"] == run_id, "READBACK_HOLD")
        result["checkpoint_written"] = True
        return result
    finally:
        if conn.in_transaction:
            conn.rollback()


def process(store, current, plan, run_id, cadence, commit=False,
            expected_generation=None, initialize=False, allow_replan=False,
            ack_private_store=False):
    reconcile.token(run_id)
    refuse(type(cadence) is str and cadence in CADENCES,
           "INVALID_INPUT")
    refuse(not commit or ack_private_store, "PRIVATE_STORAGE_APPROVAL_REQUIRED")
    if current["viewer_check"] != "current-authorized" or any(
        row["viewer_check"] != "current-authorized" for row in current["records"]
    ):
        return {"status": "ACCESS_HOLD", "checkpoint_written": False}
    reconcile.validate(current)
    if plan is not None:
        render_structure.validate(plan)
    storepath = private_file_path(store, create=False)
    exists = storepath.exists()
    if not exists and not commit:
        reconcile.validate(current)
        delta = reconcile.reconcile(None, current)
        if delta["status"] != "PROVISIONAL_DELTA_ONLY":
            return {"status": delta["status"], "checkpoint_written": False}
        if plan is not None:
            guarded_plan(plan, None, current, False)
        return {
            "status": "COLD_START_PREVIEW", "generation": 0,
            "checkpoint_written": False, "changed_count": delta["changed_count"],
            "counts": delta["counts"], "coverage": current["coverage"],
            "known_catalog_count": len(current["records"]),
            "plan_freshness": "CURRENT_CALLER_ASSERTED" if plan else "NO_PLAN",
            "source_claims": "CALLER_ASSERTED_NOT_INDEPENDENTLY_VERIFIED"}
    if not exists:
        refuse(initialize and commit and expected_generation == 0,
               "COLD_START_REQUIRES_INITIALIZE")
        storepath = private_file_path(store, create=True)
    try:
        conn = connect(storepath, read_only=not commit)
        try:
            if commit and initialize and not exists:
                conn.execute("BEGIN IMMEDIATE")
                for command in SQL_SCHEMA:
                    conn.execute(command)
                conn.commit()
            return evaluate(conn, current, plan, run_id, cadence, commit,
                            expected_generation, initialize=initialize,
                            allow_replan=allow_replan)
        finally:
            conn.close()
    except sqlite3.DatabaseError as exc:
        raise Refused("STATE_IO_OR_INTEGRITY_HOLD") from exc


def main(argv=None):
    parser = argparse.ArgumentParser(description="Authorized private curation checkpoint")
    parser.add_argument("--store", required=True, help="Explicit private SQLite file")
    parser.add_argument("--current", required=True, help="Current source snapshot JSON")
    parser.add_argument("--plan", help="Optional current plan/receipt snapshot JSON")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--cadence", choices=sorted(CADENCES), default="manual")
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--initialize", action="store_true")
    parser.add_argument("--expected-generation", type=int)
    parser.add_argument("--accept-replan", action="store_true")
    parser.add_argument("--ack-private-store", action="store_true")
    opts = parser.parse_args(argv)
    try:
        refuse(not opts.initialize or opts.commit, "COMMIT_REQUIRED")
        refuse(not opts.accept_replan or opts.commit, "COMMIT_REQUIRED")
        current = reconcile.read_snapshot(opts.current)
        plan = read_plan(opts.plan)
        result = process(opts.store, current, plan, opts.run_id, opts.cadence,
                         commit=opts.commit,
                         expected_generation=opts.expected_generation,
                         initialize=opts.initialize,
                         allow_replan=opts.accept_replan,
                         ack_private_store=opts.ack_private_store)
    except (Refused, reconcile.Invalid, render_structure.Invalid, OSError,
            ValueError, TypeError, KeyError, RecursionError) as exc:
        status = exc.code if isinstance(exc, Refused) else "INVALID_INPUT"
        result = {"status": status, "checkpoint_written": False}
    print(canonical(result))
    return 0 if result.get("status") in {"DRY_RUN", "CHECKPOINT_COMMITTED",
                       "SAME_SNAPSHOT_NO_WORK", "ALREADY_APPLIED",
                       "COLD_START", "COLD_START_PREVIEW"} else 2


if __name__ == "__main__":
    sys.exit(main())
