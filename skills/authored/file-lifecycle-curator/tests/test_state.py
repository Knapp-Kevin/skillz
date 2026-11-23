"""Adversarial tests of OPT-IN durable curation across process/run boundaries.

The store holds only synthetic test data here. These cases test real local
SQLite transactions, not source-host permissions, schedules or real files.
"""
import copy
import json
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import state as engine


def record(name, revision="rev-001"):
    return {
        "record_id": name, "source_revision": revision,
        "locator_token": "loc-" + name, "extraction": "metadata",
        "digest": None, "digest_basis": "not-computed",
        "viewer_check": "current-authorized"}


def snapshot(sid="shot-one", moment="2026-11-23T10:00:00-05:00",
             records=None, coverage="complete", absent="host-asserted-current"):
    return {"schema_version": 1, "snapshot_id": sid, "observed_at": moment,
            "scope": {"collection_id": "library-one", "root_id": "root-one",
                      "principal_id": "user-one", "audience_id": "viewer-one"},
            "coverage": coverage, "viewer_check": "current-authorized",
            "absent_identity_access": absent,
            "records": [record("alpha-id"), record("beta-id")]
                       if records is None else records}


def next_scan(old, sid="shot-two", moment="2026-11-23T11:00:00-05:00"):
    new = copy.deepcopy(old)
    new["snapshot_id"] = sid
    new["observed_at"] = moment
    return new


def plan(snap, revision="plan-rev-one", observed="2026-11-23T10:00:00-05:00",
         snapshot_id="plan-shot-one", state="PROPOSED"):
    rows = []
    for source in snap["records"]:
        key = source["record_id"]
        rows.append({
            "record_id": key, "original_path": "inbox/" + key,
            "observed_path": "inbox/" + key,
            "target_path": "organized/" + key,
            "source_revision": source["source_revision"],
            "state": state, "readback": None,
            "viewer_check": "current-authorized"})
    return {
        "schema_version": 1, "plan_id": "file-plan", "plan_revision": revision,
        "snapshot_id": snapshot_id, "observed_at": observed,
        "scope": copy.deepcopy(snap["scope"]), "coverage": snap["coverage"],
        "viewer_check": "current-authorized", "records": rows}


class PersistentCurationStateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = str(Path(self.tmp.name) / "private-state.sqlite")
        self.first = snapshot()

    def run_case(self, data=None, run_id="run-one", cadence="hourly",
                 commit=False, expected=None, init=False, obj=None,
                 replan=False, ack=False):
        return engine.process(self.path, data or self.first, obj,
                              run_id, cadence, commit=commit,
                              expected_generation=expected,
                              initialize=init, allow_replan=replan,
                              ack_private_store=ack)

    def init(self, **kwargs):
        return self.run_case(commit=True, expected=0, init=True,
                             ack=True, **kwargs)

    def state(self):
        with engine.connect(Path(self.path), read_only=True) as conn:
            return engine.read_state(conn)

    def test_default_first_run_is_preview_without_file_creation(self):
        out = self.run_case()
        self.assertEqual(out["status"], "COLD_START_PREVIEW")
        self.assertFalse(out["checkpoint_written"])
        self.assertFalse(Path(self.path).exists())

    def test_commit_requires_explicit_private_store_acknowledgment(self):
        with self.assertRaisesRegex(engine.Refused, "PRIVATE_STORAGE_APPROVAL_REQUIRED"):
            self.run_case(commit=True, expected=0, init=True)

    def test_initialize_is_not_implicit(self):
        with self.assertRaisesRegex(engine.Refused, "COLD_START_REQUIRES_INITIALIZE"):
            self.run_case(commit=True, expected=0, ack=True)
        self.assertFalse(Path(self.path).exists())

    def test_durable_state_survives_reopen_after_bootstrap(self):
        out = self.init()
        self.assertEqual(out["status"], "CHECKPOINT_COMMITTED")
        self.assertTrue(out["checkpoint_written"])
        self.assertEqual(self.state()["generation"], 1)
        self.assertEqual(len(self.state()["catalog"]), 2)

    def test_second_initialize_is_refused_and_does_not_replace_state(self):
        self.init()
        with self.assertRaisesRegex(engine.Refused, "ALREADY_INITIALIZED"):
            self.run_case(run_id="run-second", commit=True, expected=1,
                          init=True, ack=True)
        self.assertEqual(self.state()["generation"], 1)

    def test_exact_run_replay_does_not_duplicate_write(self):
        self.init()
        out = self.run_case(run_id="run-one", commit=True, expected=1, ack=True)
        self.assertEqual(out["status"], "ALREADY_APPLIED")
        self.assertFalse(out["checkpoint_written"])
        self.assertEqual(self.state()["generation"], 1)

    def test_run_id_reuse_with_different_content_rejected(self):
        self.init()
        changed = next_scan(self.first)
        with self.assertRaisesRegex(engine.Refused, "RUN_ID_REUSE_CONFLICT"):
            self.run_case(data=changed, commit=True, expected=1, ack=True)

    def test_distinct_run_id_same_snapshot_is_no_work(self):
        self.init()
        out = self.run_case(run_id="run-other", commit=True,
                            expected=1, ack=True)
        self.assertEqual(out["status"], "SAME_SNAPSHOT_NO_WORK")
        self.assertEqual(self.state()["generation"], 1)

    def test_same_snapshot_id_with_modified_bytes_refused(self):
        self.init()
        changed = copy.deepcopy(self.first)
        changed["records"][0]["source_revision"] = "rev-002"
        with self.assertRaisesRegex(engine.Refused, "SNAPSHOT_REUSE_CONFLICT"):
            self.run_case(data=changed, run_id="run-two",
                          commit=True, expected=1, ack=True)

    def test_old_agent_cannot_overwrite_new_generation(self):
        self.init()
        changed = next_scan(self.first)
        self.run_case(data=changed, run_id="run-two",
                      commit=True, expected=1, ack=True)
        third = next_scan(changed, sid="shot-three",
                          moment="2026-11-23T12:00:00-05:00")
        with self.assertRaisesRegex(engine.Refused, "GENERATION_CONFLICT"):
            self.run_case(data=third, run_id="run-three", commit=True,
                          expected=1, ack=True)
        self.assertEqual(self.state()["generation"], 2)

    def test_actual_delta_is_preserved_through_next_hourly_run(self):
        self.init()
        changed = next_scan(self.first)
        changed["records"][0]["source_revision"] = "rev-002"
        out = self.run_case(data=changed, run_id="run-two",
                            commit=True, expected=1, ack=True)
        self.assertEqual(out["counts"]["SOURCE_CHANGED_REVIEW"], 1)
        self.assertEqual(out["known_catalog_count"], 2)
        self.assertEqual(self.state()["catalog"]["alpha-id"]["row"]
                         ["source_revision"], "rev-002")

    def test_hourly_daily_weekly_cross_restart_sequence(self):
        first = self.init()
        self.assertEqual(first["generation"], 1)
        second = next_scan(self.first)
        d = self.run_case(data=second, run_id="run-daily", cadence="daily",
                          commit=True, expected=1, ack=True)
        third = next_scan(second, sid="shot-three",
                          moment="2026-11-25T10:00:00-05:00")
        w = self.run_case(data=third, run_id="run-weekly", cadence="weekly",
                          commit=True, expected=2, ack=True)
        self.assertEqual([d["generation"], w["generation"]], [2, 3])
        self.assertEqual(self.state()["scan"]["snapshot_id"], "shot-three")
        with sqlite3.connect(self.path) as conn:
            cadences = [x[0] for x in conn.execute(
                "SELECT cadence FROM accepted_runs ORDER BY generation")]
        self.assertEqual(cadences, ["hourly", "daily", "weekly"])

    def test_partial_scan_unverified_absence_is_privacy_hold(self):
        self.init()
        partial = next_scan(self.first)
        partial["coverage"] = "partial"
        partial["records"] = [record("alpha-id")]
        partial["absent_identity_access"] = "unverified"
        out = self.run_case(data=partial, run_id="run-two", commit=True,
                            expected=1, ack=True)
        self.assertEqual(out, {"status": "ABSENT_IDENTITY_ACCESS_HOLD",
                               "checkpoint_written": False})
        self.assertEqual(self.state()["generation"], 1)

    def test_partial_authorized_scan_preserves_last_known_record(self):
        self.init()
        partial = next_scan(self.first)
        partial["coverage"] = "partial"
        partial["records"] = [record("alpha-id")]
        out = self.run_case(data=partial, run_id="run-two", commit=True,
                            expected=1, ack=True)
        self.assertEqual(out["not_seen_this_run_count"], 1)
        self.assertEqual(out["known_catalog_count"], 2)
        self.assertIn("beta-id", self.state()["catalog"])
        self.assertEqual(self.state()["catalog"]["beta-id"]["last_seen_id"],
                         "shot-one")

    def test_multiple_partial_runs_do_not_erase_unvisited_catalog(self):
        self.init()
        p1 = next_scan(self.first)
        p1["records"] = [record("alpha-id")]
        p1["coverage"] = "partial"
        self.run_case(data=p1, run_id="run-two", commit=True,
                      expected=1, ack=True)
        p2 = next_scan(p1, sid="shot-three",
                       moment="2026-11-23T12:00:00-05:00")
        p2["records"] = [record("beta-id")]
        out = self.run_case(data=p2, run_id="run-three", commit=True,
                            expected=2, ack=True)
        self.assertEqual(out["known_catalog_count"], 2)
        self.assertEqual(out["not_seen_this_run_count"], 1)
        self.assertEqual(out["counts"]["NOT_OBSERVED_PARTIAL_SCOPE"], 1)

    def test_complete_scan_absence_is_retained_for_review_not_deleted(self):
        self.init()
        second = next_scan(self.first)
        second["records"] = [record("alpha-id")]
        out = self.run_case(data=second, run_id="run-two",
                            commit=True, expected=1, ack=True)
        self.assertEqual(out["counts"]["ABSENT_COMPLETE_SCOPE_REVIEW"], 1)
        self.assertIn("beta-id", self.state()["catalog"])

    def test_no_cross_collection_or_user_reuse(self):
        self.init()
        different = next_scan(self.first)
        different["scope"]["principal_id"] = "user-other"
        with self.assertRaisesRegex(engine.Refused, "CROSS_SCOPE_HOLD"):
            self.run_case(data=different, run_id="run-two",
                          commit=True, expected=1, ack=True)
        self.assertEqual(self.state()["generation"], 1)

    def test_current_denied_access_never_reports_prior_record_counts(self):
        self.init()
        denied = next_scan(self.first)
        denied["viewer_check"] = "denied"
        result = self.run_case(data=denied, run_id="run-two",
                               commit=True, expected=1, ack=True)
        self.assertEqual(result, {"status": "ACCESS_HOLD",
                                  "checkpoint_written": False})
        self.assertEqual(self.state()["generation"], 1)
        self.assertNotIn("alpha-id", json.dumps(result))

    def test_current_record_denied_access_never_reports_counts(self):
        self.init()
        denied = next_scan(self.first)
        denied["records"][0]["viewer_check"] = "denied"
        result = self.run_case(data=denied, run_id="run-two",
                               commit=True, expected=1, ack=True)
        self.assertEqual(result["status"], "ACCESS_HOLD")
        self.assertNotIn("counts", result)

    def test_store_digest_mismatch_holds_and_does_not_overwrite(self):
        self.init()
        with sqlite3.connect(self.path) as conn:
            conn.execute("UPDATE curator_state SET state_digest='000000'")
        changed = next_scan(self.first)
        with self.assertRaisesRegex(engine.Refused, "STATE_INTEGRITY_HOLD"):
            self.run_case(data=changed, run_id="run-two",
                          commit=True, expected=1, ack=True)

    def test_private_store_file_is_restricted_on_posix(self):
        self.init()
        if os.name == "posix":
            self.assertEqual(Path(self.path).stat().st_mode & 0o077, 0)

    def test_symlinked_checkpoint_path_is_refused(self):
        self.init()
        link = Path(self.tmp.name) / "link.sqlite"
        link.symlink_to(self.path)
        with self.assertRaisesRegex(engine.Refused, "UNSAFE_STORE_PATH"):
            engine.process(str(link), self.first, None, "run-two", "manual")

    def test_plan_persisted_without_promoting_to_real_operation(self):
        out = self.init(obj=plan(self.first))
        self.assertEqual(out["plan_freshness"], "CURRENT_CALLER_ASSERTED")
        self.assertEqual(self.state()["plan"]["plan_id"], "file-plan")
        self.assertEqual(self.state()["plan"]["records"][0]["state"], "PROPOSED")

    def test_later_run_does_not_claim_old_plan_current(self):
        self.init(obj=plan(self.first))
        next_value = next_scan(self.first)
        out = self.run_case(data=next_value, run_id="run-two",
                            commit=True, expected=1, ack=True)
        self.assertEqual(out["plan_freshness"], "HISTORICAL_NOT_REVALIDATED")
        self.assertIsNotNone(self.state()["plan"])

    def test_plan_source_revision_must_match_current_input(self):
        bad = plan(self.first)
        bad["records"][0]["source_revision"] = "rev-999"
        with self.assertRaisesRegex(engine.Refused, "PLAN_SOURCE_REVISION_HOLD"):
            self.init(obj=bad)

    def test_plan_may_not_visualize_unobserved_record(self):
        bad = plan(self.first)
        bad["records"].append({
            "record_id": "hidden-id", "original_path": "inbox/hidden-id",
            "observed_path": "inbox/hidden-id",
            "target_path": "organized/hidden-id", "source_revision": "rev-1",
            "state": "PROPOSED", "readback": None,
            "viewer_check": "current-authorized"})
        with self.assertRaisesRegex(engine.Refused, "PLAN_SOURCE_ACCESS_HOLD"):
            self.init(obj=bad)

    def test_plan_change_under_same_revision_is_not_silent(self):
        self.init(obj=plan(self.first))
        new = plan(self.first, observed="2026-11-23T11:00:00-05:00",
                   snapshot_id="plan-shot-two")
        new["records"][0]["target_path"] = "other/alpha-id"
        with self.assertRaisesRegex(engine.Refused, "PLAN_DRIFT_HOLD"):
            self.run_case(run_id="plan-update", obj=new, commit=True,
                          expected=1, ack=True)
        self.assertEqual(self.state()["generation"], 1)

    def test_replan_requires_separate_approval(self):
        self.init(obj=plan(self.first))
        new = plan(self.first, revision="plan-rev-two",
                   observed="2026-11-23T11:00:00-05:00",
                   snapshot_id="plan-shot-two")
        with self.assertRaisesRegex(engine.Refused, "REPLAN_REQUIRES_APPROVAL"):
            self.run_case(run_id="plan-update", obj=new, commit=True,
                          expected=1, ack=True)

    def test_owner_accepted_plan_revision_can_persist_without_new_scan(self):
        self.init(obj=plan(self.first))
        new = plan(self.first, revision="plan-rev-two",
                   observed="2026-11-23T11:00:00-05:00",
                   snapshot_id="plan-shot-two")
        result = self.run_case(run_id="plan-update", obj=new, replan=True,
                               commit=True, expected=1, ack=True)
        self.assertEqual(result["run_type"], "PLAN_ONLY")
        self.assertEqual(result["generation"], 2)
        self.assertEqual(self.state()["plan"]["plan_revision"], "plan-rev-two")

    def test_plan_only_replay_does_not_duplicate_changes(self):
        self.init(obj=plan(self.first))
        new = plan(self.first, revision="plan-rev-two",
                   observed="2026-11-23T11:00:00-05:00",
                   snapshot_id="plan-shot-two")
        self.run_case(run_id="plan-update", obj=new, replan=True, commit=True,
                      expected=1, ack=True)
        result = self.run_case(run_id="plan-update", obj=new, replan=True,
                               commit=True, expected=2, ack=True)
        self.assertEqual(result["status"], "ALREADY_APPLIED")
        self.assertEqual(self.state()["generation"], 2)

    def test_rollback_on_injected_sqlite_failure_keeps_prior_generation(self):
        self.init()
        with sqlite3.connect(self.path) as conn:
            conn.execute("CREATE TRIGGER break_insert BEFORE INSERT ON accepted_runs "
                         "BEGIN SELECT RAISE(ABORT, 'synthetic abort'); END")
        changed = next_scan(self.first)
        with self.assertRaisesRegex(engine.Refused, "STATE_IO_OR_INTEGRITY_HOLD"):
            self.run_case(data=changed, run_id="run-two", commit=True,
                          expected=1, ack=True)
        self.assertEqual(self.state()["generation"], 1)
        with sqlite3.connect(self.path) as conn:
            conn.execute("DROP TRIGGER break_insert")
        result = self.run_case(data=changed, run_id="run-two", commit=True,
                               expected=1, ack=True)
        self.assertEqual(result["generation"], 2)

    def test_successful_run_event_records_trend_not_private_raw_file(self):
        self.init()
        with sqlite3.connect(self.path) as conn:
            row = conn.execute("SELECT report_json, cadence FROM accepted_runs"
                               " WHERE generation=1").fetchone()
        report = json.loads(row[0])
        self.assertEqual(report["known_catalog_count"], 2)
        self.assertEqual(row[1], "hourly")
        self.assertNotIn("loc-alpha-id", row[0])

    def test_unrecognized_cadence_does_not_schedule_anything(self):
        with self.assertRaisesRegex(engine.Refused, "INVALID_INPUT"):
            self.run_case(cadence="every-minute")
        self.assertFalse(Path(self.path).exists())

    def test_no_unauthorized_content_processing_or_scheduler(self):
        text = (SCRIPTS / "state.py").read_text()
        for forbidden in ("import requests", "import socket",
                          "import subprocess", "urllib.request",
                          "schedule.create", "os.system("):
            self.assertNotIn(forbidden, text)


    def test_plan_only_after_partial_does_not_call_unseen_records_unchanged(self):
        self.init()
        partial = next_scan(self.first)
        partial["coverage"] = "partial"
        partial["records"] = [record("alpha-id")]
        self.run_case(data=partial, run_id="run-two",
                      commit=True, expected=1, ack=True)
        plan_update = plan(partial, observed="2026-11-23T11:00:00-05:00",
                           snapshot_id="plan-shot-two")
        result = self.run_case(data=partial, run_id="plan-three",
                               obj=plan_update, commit=True, expected=2,
                               ack=True)
        self.assertEqual(result["run_type"], "PLAN_ONLY")
        self.assertEqual(result["counts"]["UNCHANGED_NO_REWORK"], 1)
        self.assertEqual(result["counts"]["NOT_OBSERVED_PARTIAL_SCOPE"], 1)
        self.assertEqual(result["not_seen_this_run_count"], 1)
        self.assertEqual(self.state()["generation"], 3)


    def test_historical_snapshot_id_reuse_cannot_rewrite_last_seen_memory(self):
        self.init()
        partial = next_scan(self.first)
        partial["coverage"] = "partial"
        partial["records"] = [record("alpha-id")]
        self.run_case(data=partial, run_id="run-two",
                      commit=True, expected=1, ack=True)
        reused = next_scan(partial, sid="shot-one",
                           moment="2026-11-23T12:00:00-05:00")
        with self.assertRaisesRegex(engine.Refused, "SNAPSHOT_REUSE_CONFLICT"):
            self.run_case(data=reused, run_id="run-three",
                          commit=True, expected=2, ack=True)
        checkpoint = self.state()
        self.assertEqual(checkpoint["generation"], 2)
        self.assertEqual(checkpoint["catalog"]["beta-id"]["last_seen_id"],
                         "shot-one")
        self.assertEqual(checkpoint["scan"]["snapshot_id"], "shot-two")

    def test_old_snapshot_id_reused_even_with_different_timestamp_is_refused(self):
        self.init()
        second = next_scan(self.first)
        self.run_case(data=second, run_id="run-two",
                      commit=True, expected=1, ack=True)
        reused = next_scan(self.first, sid="shot-one",
                           moment="2026-11-23T12:00:00-05:00")
        with self.assertRaisesRegex(engine.Refused, "SNAPSHOT_REUSE_CONFLICT"):
            self.run_case(data=reused, run_id="run-three",
                          commit=True, expected=2, ack=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
