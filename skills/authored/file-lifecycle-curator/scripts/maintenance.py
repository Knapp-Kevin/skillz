#!/usr/bin/env python3
"""Bounded, host-invoked maintenance for File Lifecycle Curator.

No crawler, background service, source mutation, network call, or scheduler.
Python 3.9+ stdlib. All source/access facts are caller assertions.
"""
import argparse
import json
from pathlib import Path
import sqlite3
import sys

import reconcile
import state

ACTIONS = {
    "hourly": ("RECONCILE_CHANGED", "RETRY_HELD"),
    "daily": ("RECONCILE_CHANGED", "REVIEW_STALE_INDEX", "REVIEW_OPEN_HOLDS"),
    "weekly": ("RECONCILE_CHANGED", "AUDIT_UNCHANGED_SAMPLE",
               "CHECK_RECOVERY_READINESS", "REVIEW_RETENTION_AND_ACL"),
}
MAX_ACTIONS = 10


def journal_health(conn, checkpoint):
    """Fail closed on broken generation continuity or forged last-run pointer.

    This verifies internal consistency, NOT authenticity against a hostile
    writer who can replace both the database and its checksums.
    """
    generation = checkpoint["generation"]
    rows = conn.execute(
        "SELECT generation, run_id, cadence, snapshot_id, payload_digest, "
        "report_json FROM accepted_runs ORDER BY generation").fetchall()
    if len(rows) != generation or any(row[0] != i for i, row in
                                       enumerate(rows, start=1)):
        raise state.Refused("HISTORY_INTEGRITY_HOLD")
    if rows[-1][1] != checkpoint["last_run_id"]:
        raise state.Refused("HISTORY_INTEGRITY_HOLD")
    if rows[-1][3] != checkpoint["scan"]["snapshot_id"]:
        raise state.Refused("HISTORY_INTEGRITY_HOLD")
    for _, _, cadence, _, payload_digest, report in rows:
        if cadence not in state.CADENCES or not isinstance(payload_digest, str) or len(payload_digest) != 64:
            raise state.Refused("HISTORY_INTEGRITY_HOLD")
        try:
            value = json.loads(report, object_pairs_hook=reconcile.unique_pairs)
            if not isinstance(value, dict):
                raise ValueError("invalid report")
        except (ValueError, reconcile.Invalid):
            raise state.Refused("HISTORY_INTEGRITY_HOLD")
    return {"generation": generation, "accepted_runs": len(rows),
            "last_run_id": rows[-1][1]}


def inspect_checkpoint(store):
    """Read-only checkpoint inspection, never initializes or repairs a DB."""
    path = state.private_file_path(store)
    if not path.exists():
        return None
    try:
        with state.connect(path, read_only=True) as conn:
            checkpoint = state.read_state(conn)
            if checkpoint is None:
                raise state.Refused("STATE_SCHEMA_HOLD")
            receipt = journal_health(conn, checkpoint)
            return checkpoint, receipt
    except sqlite3.DatabaseError as exc:
        raise state.Refused("STATE_IO_OR_INTEGRITY_HOLD") from exc


def maintenance(store, current, run_id, cadence, commit=False,
                expected_generation=None, initialize=False,
                ack_private_store=False):
    if cadence not in ACTIONS:
        raise state.Refused("INVALID_CADENCE")
    reconcile.validate(current)
    # Authorization before even inspecting cached information.
    if current["viewer_check"] != "current-authorized" or any(
        row["viewer_check"] != "current-authorized" for row in current["records"]
    ):
        return {"status": "ACCESS_HOLD", "checkpoint_written": False}
    found = inspect_checkpoint(store)
    previous_generation = found[0]["generation"] if found else 0
    if found is not None and found[0]["scan"]["scope"] != current["scope"]:
        raise state.Refused("CROSS_SCOPE_HOLD")
    if commit and expected_generation != previous_generation:
        raise state.Refused("GENERATION_CONFLICT")
    # state.process provides the existing transactional, revision-aware CAS.
    outcome = state.process(
        store, current, None, run_id, cadence, commit=commit,
        expected_generation=expected_generation,
        initialize=initialize, ack_private_store=ack_private_store)
    status = outcome["status"]
    if status in {"ACCESS_HOLD", "ABSENT_IDENTITY_ACCESS_HOLD"}:
        return {"status": status, "checkpoint_written": False}
    if status in {"ALREADY_APPLIED", "SAME_SNAPSHOT_NO_WORK"}:
        return {"status": status, "checkpoint_written": False,
                "generation": outcome["generation"],
                "maintenance": ["NO_DUPLICATE_PROCESSING"]}
    categories = list(ACTIONS[cadence])
    delta = outcome.get("counts", {})
    if delta.get("UNCHANGED_NO_REWORK", 0) and cadence == "weekly":
        categories.append("SAMPLE_PRIOR_EVIDENCE_NOT_SOURCE_VERIFIED")
    if outcome.get("plan_freshness") == "HISTORICAL_NOT_REVALIDATED":
        categories.append("REVALIDATE_HISTORICAL_PLAN")
    return {**outcome,
            "maintenance": categories[:MAX_ACTIONS],
            "maintenance_executed": False,
            "source_operations_executed": False,
            "continuity_verified_before_run": bool(found),
            "prior_generation": previous_generation,
            "maintenance_note": "Recommendations only; no source or index work executed."}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Host-invoked file curation maintenance")
    parser.add_argument("--store", required=True)
    parser.add_argument("--current", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--cadence", choices=sorted(ACTIONS), required=True)
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--initialize", action="store_true")
    parser.add_argument("--ack-private-store", action="store_true")
    parser.add_argument("--expected-generation", type=int)
    args = parser.parse_args(argv)
    try:
        current = reconcile.read_snapshot(args.current)
        report = maintenance(
            args.store, current, args.run_id, args.cadence,
            commit=args.commit, expected_generation=args.expected_generation,
            initialize=args.initialize, ack_private_store=args.ack_private_store)
    except (state.Refused, reconcile.Invalid, OSError, ValueError, KeyError, TypeError) as exc:
        report = {"status": getattr(exc, "code", "INVALID_SNAPSHOT"),
                  "checkpoint_written": False}
    print(json.dumps(report, sort_keys=True))
    return 0 if report["status"] not in {
        "ACCESS_HOLD", "ABSENT_IDENTITY_ACCESS_HOLD",
        "GENERATION_CONFLICT", "CROSS_SCOPE_HOLD", "HISTORY_INTEGRITY_HOLD",
        "STATE_INTEGRITY_HOLD", "STATE_SCHEMA_HOLD",
        "STATE_IO_OR_INTEGRITY_HOLD"} and not report["status"].endswith("_HOLD") else 2


if __name__ == "__main__":
    sys.exit(main())
