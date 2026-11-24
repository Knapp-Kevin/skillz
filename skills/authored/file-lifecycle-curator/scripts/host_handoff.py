#!/usr/bin/env python3
"""Read-only agent-host continuity handoff for File Lifecycle Curator.

The host supplies fresh, authorized observations. This script DOES NOT
authenticate host claims, read original file bytes, execute operations,
create a scheduler, or persist any checkpoint. Python 3.9+ stdlib.
"""
import argparse
import json
import sys

import maintenance
import reconcile
import render_structure
import state


def hold(code):
    return {"status": code, "checkpoint_written": False,
            "source_operations_executed": False, "progress": None}


def preview(store, current, plan=None):
    """Compare fresh caller evidence with accepted state; never promote history."""
    reconcile.validate(current)
    if current["viewer_check"] != "current-authorized" or any(
        row["viewer_check"] != "current-authorized" for row in current["records"]
    ):
        return hold("ACCESS_HOLD")
    found = maintenance.inspect_checkpoint(store)
    if found is None:
        return hold("COLD_START_NO_CHECKPOINT")
    checkpoint, _ = found
    prior = checkpoint["scan"]
    if prior["scope"] != current["scope"]:
        return hold("CROSS_SCOPE_HOLD")
    if current["snapshot_id"] == prior["snapshot_id"]:
        if current != prior:
            return hold("SNAPSHOT_REUSE_HOLD")
        return hold("SAME_SNAPSHOT_NO_FRESH_HOST_EVIDENCE")
    delta = reconcile.reconcile(state.previous_catalog_scan(checkpoint), current)
    if delta["status"] != "PROVISIONAL_DELTA_ONLY":
        return hold(delta["status"])
    result = {
        "status": "FRESH_SOURCE_PROVISIONAL",
        "checkpoint_written": False, "source_operations_executed": False,
        "checkpoint_generation": checkpoint["generation"],
        "snapshot_id": current["snapshot_id"],
        "coverage": current["coverage"],
        "delta": {"counts": delta["counts"],
                  "changed_count": delta["changed_count"],
                  "actions": delta["actions"],
                  "omitted_action_count": delta["omitted_action_count"]},
        "plan_status": "NOT_SUPPLIED",
        "progress": None, "visuals": None,
        "source_evidence": "CALLER_ASSERTED_NOT_HOST_AUTHENTICATED",
        "operation_evidence": "NOT_INDEPENDENTLY_VERIFIED",
        "recommended_next_action": "Review source delta and separately authorize eligible work",
        "alternative": "Keep the existing organization; investigate holds",
    }
    if plan is None:
        return result
    render_structure.validate(plan)
    if plan["viewer_check"] != "current-authorized" or any(
        row["viewer_check"] != "current-authorized" for row in plan["records"]
    ):
        return hold("ACCESS_HOLD")
    if plan["scope"] != current["scope"]:
        return hold("CROSS_SCOPE_HOLD")
    prior_plan = checkpoint["plan"]
    if prior_plan is None:
        return hold("PLAN_NOT_ACCEPTED_HOLD")
    if (prior_plan["plan_id"], prior_plan["plan_revision"]) != (
        plan["plan_id"], plan["plan_revision"]
    ):
        return hold("REPLAN_REQUIRES_APPROVAL")
    # An immutable plan revision also has an immutable membership set.
    # Otherwise an injected newly VERIFIED record could bypass original/target
    # comparisons and inflate progress without owner-approved re-planning.
    previous_ids = {row["record_id"] for row in prior_plan["records"]}
    incoming_ids = {row["record_id"] for row in plan["records"]}
    if previous_ids != incoming_ids:
        return hold("PLAN_MEMBERSHIP_CHANGE_HOLD")
    if render_structure.date(plan["observed_at"]) <= render_structure.date(
        prior_plan["observed_at"]
    ):
        return hold("STALE_PLAN_EVIDENCE_HOLD")
    if render_structure.date(plan["observed_at"]) < reconcile.timestamp(
        current["observed_at"]
    ):
        return hold("PLAN_BEFORE_SOURCE_HOLD")
    now = {row["record_id"]: row for row in current["records"]}
    if any(row["record_id"] not in now for row in plan["records"]):
        return hold("PLAN_SOURCE_ACCESS_HOLD")
    if any(row["source_revision"] != now[row["record_id"]]["source_revision"]
           for row in plan["records"]):
        return hold("PLAN_SOURCE_REVISION_HOLD")
    view = render_structure.checked_view(plan, prior_plan)
    if view["status"] != "PROVISIONAL_VISUAL_ONLY":
        return hold(view["status"])
    result["plan_status"] = "FRESH_HOST_RECEIPTS_CALLER_ASSERTED"
    result["progress"] = view["progress"]
    result["visuals"] = view["visuals"]
    result["status"] = "HANDOFF_PREVIEW_NOT_PERSISTED"
    result["recommended_next_action"] = (
        "Independently verify host receipts and source permissions; "
        "then explicitly checkpoint with state.py if approved"
    )
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Read-only scoped agent handoff")
    parser.add_argument("--store", required=True)
    parser.add_argument("--current", required=True)
    parser.add_argument("--plan")
    args = parser.parse_args(argv)
    try:
        current = reconcile.read_snapshot(args.current)
        plan = render_structure.read_input(args.plan) if args.plan else None
        report = preview(args.store, current, plan)
    except (reconcile.Invalid, render_structure.Invalid, ValueError,
            TypeError, KeyError, OverflowError, RecursionError):
        report = hold("INVALID_HOST_EVIDENCE")
    except state.Refused as exc:
        report = hold(exc.code)
    except OSError:
        report = hold("INPUT_OR_CHECKPOINT_IO_HOLD")
    print(json.dumps(report, sort_keys=True))
    return 0 if report["status"] in {
        "FRESH_SOURCE_PROVISIONAL", "HANDOFF_PREVIEW_NOT_PERSISTED",
        "SAME_SNAPSHOT_NO_FRESH_HOST_EVIDENCE",
    } else 2


if __name__ == "__main__":
    sys.exit(main())
