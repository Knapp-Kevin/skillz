"""Offline maintenance and persistence regression tests, no host or scheduler."""
import copy
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from test_state import snapshot, next_scan
import maintenance


class MaintenanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.store = str(Path(self.tmp.name) / "state.sqlite")
        self.first = snapshot()

    def invoke(self, current=None, run="run-one", cadence="hourly", **kwargs):
        return maintenance.maintenance(self.store, current or self.first,
                                       run, cadence, **kwargs)

    def initialize(self):
        return self.invoke(commit=True, initialize=True,
                           ack_private_store=True, expected_generation=0)

    def test_preview_does_not_create_checkpoint_or_schedule(self):
        outcome = self.invoke()
        self.assertEqual(outcome["status"], "COLD_START_PREVIEW")
        self.assertFalse(Path(self.store).exists())
        self.assertFalse(outcome["source_operations_executed"])
        self.assertFalse(outcome["maintenance_executed"])

    def test_recovers_across_runs_and_does_not_rewrite_replayed_snapshot(self):
        self.initialize()
        same = self.invoke(run="new-nochange-run")
        self.assertEqual(same["status"], "SAME_SNAPSHOT_NO_WORK")
        self.assertEqual(same["maintenance"], ["NO_DUPLICATE_PROCESSING"])
        updated = next_scan(self.first)
        result = self.invoke(updated, run="run-two", cadence="daily",
                             commit=True, expected_generation=1,
                             ack_private_store=True)
        self.assertEqual(result["generation"], 2)
        self.assertTrue(result["continuity_verified_before_run"])
        self.assertIn("REVIEW_STALE_INDEX", result["maintenance"])
        replay = self.invoke(updated, run="run-two", cadence="daily",
                             commit=True, expected_generation=2,
                             ack_private_store=True)
        self.assertEqual(replay["status"], "ALREADY_APPLIED")
        with sqlite3.connect(self.store) as conn:
            self.assertEqual(conn.execute(
                "SELECT COUNT(*) FROM accepted_runs").fetchone()[0], 2)

    def test_no_change_weekly_still_proposes_audit_without_commit(self):
        self.initialize()
        result = self.invoke(run="weekly-new-run", cadence="weekly")
        self.assertEqual(result["status"], "SAME_SNAPSHOT_NO_WORK")
        self.assertIn("CHECK_RECOVERY_READINESS", result["maintenance"])
        self.assertFalse(result["checkpoint_written"])
        self.assertFalse(result["maintenance_executed"])

    def test_overlap_generation_conflict_leaves_state_intact(self):
        self.initialize()
        changed = next_scan(self.first)
        with self.assertRaisesRegex(Exception, "GENERATION_CONFLICT"):
            self.invoke(changed, run="run-two", commit=True,
                        expected_generation=0, ack_private_store=True)
        with sqlite3.connect(self.store) as conn:
            self.assertEqual(conn.execute(
                "SELECT generation FROM curator_state").fetchone()[0], 1)

    def test_tampered_or_missing_journal_requires_hold(self):
        self.initialize()
        with sqlite3.connect(self.store) as conn:
            conn.execute("DELETE FROM accepted_runs")
        with self.assertRaisesRegex(Exception, "HISTORY_INTEGRITY_HOLD"):
            self.invoke(next_scan(self.first), run="run-two")
        with sqlite3.connect(self.store) as conn:
            self.assertEqual(conn.execute(
                "SELECT generation FROM curator_state").fetchone()[0], 1)

    def test_tampered_last_receipt_requires_hold(self):
        self.initialize()
        with sqlite3.connect(self.store) as conn:
            conn.execute("UPDATE accepted_runs SET run_id='altered-run'")
        with self.assertRaisesRegex(Exception, "HISTORY_INTEGRITY_HOLD"):
            self.invoke(next_scan(self.first), run="run-two")

    def test_weekly_detects_malformed_intermediate_journal_entry(self):
        self.initialize()
        second = next_scan(self.first)
        self.invoke(second, run="run-two", commit=True,
                    expected_generation=1, ack_private_store=True)
        third = next_scan(second, sid="shot-three",
                          moment="2026-11-23T12:00:00-05:00")
        self.invoke(third, run="run-three", commit=True,
                    expected_generation=2, ack_private_store=True)
        with sqlite3.connect(self.store) as conn:
            conn.execute(
                "UPDATE accepted_runs SET report_json='broken-json' "
                "WHERE generation=1")
        # This is a deliberately DEEP weekly check. Regular hourly checks
        # validate latest receipt + continuous generation count only.
        with self.assertRaisesRegex(Exception, "HISTORY_INTEGRITY_HOLD"):
            self.invoke(third, run="weekly-check", cadence="weekly")
        with sqlite3.connect(self.store) as conn:
            self.assertEqual(conn.execute(
                "SELECT generation FROM curator_state").fetchone()[0], 3)

    def test_revoked_access_never_leaks_cached_identity_or_counts(self):
        self.initialize()
        denied = next_scan(self.first)
        denied["viewer_check"] = "denied"
        result = self.invoke(denied, run="run-two")
        self.assertEqual(result, {"status": "ACCESS_HOLD",
                                  "checkpoint_written": False})
        self.assertNotIn("alpha-id", json.dumps(result))

    def test_wrong_scope_does_not_inherit_catalog(self):
        self.initialize()
        other = next_scan(self.first)
        other["scope"]["principal_id"] = "another-user"
        with self.assertRaisesRegex(Exception, "CROSS_SCOPE_HOLD"):
            self.invoke(other, run="run-two")

    def test_partial_scan_does_not_erase_previous_catalog(self):
        self.initialize()
        partial = next_scan(self.first)
        partial["coverage"] = "partial"
        partial["records"] = partial["records"][:1]
        out = self.invoke(partial, run="run-two", cadence="weekly",
                          commit=True, expected_generation=1,
                          ack_private_store=True)
        self.assertEqual(out["known_catalog_count"], 2)
        self.assertEqual(out["not_seen_this_run_count"], 1)
        self.assertIn("AUDIT_UNCHANGED_SAMPLE", out["maintenance"])
        self.assertFalse(out["maintenance_executed"])

    def test_uncertain_absence_does_not_commit_or_reveal_counts(self):
        self.initialize()
        partial = next_scan(self.first)
        partial["coverage"] = "partial"
        partial["records"] = partial["records"][:1]
        partial["absent_identity_access"] = "unverified"
        result = self.invoke(partial, run="run-two", commit=True,
                             expected_generation=1,
                             ack_private_store=True)
        self.assertEqual(result, {"status": "ABSENT_IDENTITY_ACCESS_HOLD",
                                  "checkpoint_written": False})

    def test_no_ambient_network_scheduler_or_source_mutations(self):
        source = (ROOT / "scripts" / "maintenance.py").read_text()
        for forbidden in ("import requests", "import socket",
                          "import subprocess", "os.remove(",
                          "shutil.move(", "schedule.create"):
            self.assertNotIn(forbidden, source)


if __name__ == "__main__":
    unittest.main()
