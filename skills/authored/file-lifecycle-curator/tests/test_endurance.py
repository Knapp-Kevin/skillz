"""Deterministic 90-day lifecycle qualification of the optional skill helper.

Virtual timestamps, real temporary SQLite transactions and process-level
reopens. Does NOT observe a host account or execute a live scheduled task.
"""
import copy
from datetime import datetime, timedelta, timezone
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from test_state import snapshot
import maintenance
import state


class NinetyDayContinuityTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.store = str(Path(self.workspace.name) / "state.sqlite")
        self.base = snapshot()
        self.start = datetime(2026, 1, 1, tzinfo=timezone.utc)

    def observed(self, hour):
        current = copy.deepcopy(self.base)
        current["snapshot_id"] = "hour-%04d" % hour
        current["observed_at"] = (self.start + timedelta(hours=hour)).isoformat()
        # Preserve stable source IDs while changing a genuine source revision.
        current["records"][0]["source_revision"] = "rev-%04d" % (hour // 11)
        if hour and hour % 37 == 0:
            current["coverage"] = "partial"
            current["records"] = current["records"][:1]
        return current

    def test_ninety_virtual_days_cross_restart_and_failure_injection(self):
        total = 90 * 24
        commits = 0
        daily_checks = 0
        weekly_checks = 0
        denied_checks = 0
        for hour in range(total):
            current = self.observed(hour)
            run_id = "run-%04d" % hour
            if hour and hour % 97 == 0:
                denied = copy.deepcopy(current)
                denied["viewer_check"] = "denied"
                result = maintenance.maintenance(
                    self.store, denied, "denied-%04d" % hour, "hourly",
                    commit=True, expected_generation=commits,
                    ack_private_store=True)
                self.assertEqual(result, {
                    "status": "ACCESS_HOLD", "checkpoint_written": False})
                denied_checks += 1

            if hour == 550:
                with sqlite3.connect(self.store) as conn:
                    conn.execute(
                        "CREATE TRIGGER crash_on_receipt BEFORE INSERT ON accepted_runs "
                        "BEGIN SELECT RAISE(ABORT, 'injected crash'); END")
                with self.assertRaisesRegex(state.Refused,
                                             "STATE_IO_OR_INTEGRITY_HOLD"):
                    maintenance.maintenance(
                        self.store, current, run_id, "hourly",
                        commit=True, expected_generation=commits,
                        ack_private_store=True)
                self.assertEqual(
                    maintenance.inspect_checkpoint(self.store)[0]["generation"],
                    commits)
                with sqlite3.connect(self.store) as conn:
                    conn.execute("DROP TRIGGER crash_on_receipt")

            if hour == 1500:
                with self.assertRaisesRegex(state.Refused,
                                             "GENERATION_CONFLICT"):
                    maintenance.maintenance(
                        self.store, current, run_id, "hourly",
                        commit=True, expected_generation=commits - 1,
                        ack_private_store=True)

            receipt = maintenance.maintenance(
                self.store, current, run_id, "hourly",
                commit=True, expected_generation=commits,
                initialize=(hour == 0), ack_private_store=True)
            self.assertEqual(receipt["status"], "CHECKPOINT_COMMITTED")
            self.assertTrue(receipt["checkpoint_written"])
            self.assertFalse(receipt["source_operations_executed"])
            self.assertEqual(receipt["generation"], commits + 1)
            self.assertEqual(receipt["known_catalog_count"], 2)
            if current["coverage"] == "partial":
                self.assertEqual(receipt["not_seen_this_run_count"], 1)
            commits += 1

            # These checks must remain useful on unchanged source snapshots,
            # but cannot create another generation or claim actual work.
            if hour % 24 == 23:
                daily = maintenance.maintenance(
                    self.store, current, "daily-%04d" % hour, "daily")
                self.assertEqual(daily["status"], "SAME_SNAPSHOT_NO_WORK")
                self.assertFalse(daily["checkpoint_written"])
                self.assertIn("REVIEW_STALE_INDEX", daily["maintenance"])
                daily_checks += 1
            if hour % 168 == 167:
                weekly = maintenance.maintenance(
                    self.store, current, "weekly-%04d" % hour, "weekly")
                self.assertEqual(weekly["status"], "SAME_SNAPSHOT_NO_WORK")
                self.assertEqual(weekly["journal_audit_depth"],
                                 "full-structural")
                self.assertFalse(weekly["maintenance_executed"])
                weekly_checks += 1

        persisted, continuity = maintenance.inspect_checkpoint(self.store,
                                                                deep=True)
        self.assertEqual((commits, daily_checks, weekly_checks),
                         (2160, 90, 12))
        self.assertEqual(denied_checks, 22)
        self.assertEqual(continuity["accepted_runs"], commits)
        self.assertEqual(persisted["generation"], commits)
        self.assertEqual(persisted["scan"]["snapshot_id"], "hour-2159")
        self.assertEqual(persisted["catalog"]["alpha-id"]["row"][
            "source_revision"], "rev-0196")
        self.assertEqual(len(persisted["catalog"]), 2)

    def test_corrupted_primary_must_not_automatically_restore_backup(self):
        first = self.observed(0)
        accepted = maintenance.maintenance(
            self.store, first, "run-initial", "hourly",
            commit=True, initialize=True, expected_generation=0,
            ack_private_store=True)
        self.assertTrue(accepted["checkpoint_written"])
        backup = Path(self.workspace.name) / "backup-candidate.sqlite"
        # Only synthetic test fixtures: a real backup needs distinct owner
        # authority, protected storage and independently tested recovery.
        with sqlite3.connect(self.store) as source:
            with sqlite3.connect(backup) as destination:
                source.backup(destination)
        backup.chmod(0o600)
        self.assertEqual(maintenance.inspect_checkpoint(str(backup))[0][
            "generation"], 1)
        with sqlite3.connect(self.store) as conn:
            conn.execute("UPDATE curator_state SET state_digest='corrupt'")
        with self.assertRaisesRegex(state.Refused, "STATE_INTEGRITY_HOLD"):
            maintenance.inspect_checkpoint(self.store)
        with self.assertRaisesRegex(state.Refused, "STATE_INTEGRITY_HOLD"):
            maintenance.maintenance(
                self.store, self.observed(1), "run-next", "hourly",
                commit=True, expected_generation=1,
                ack_private_store=True)
        # Neither the state helper nor the maintenance helper restores files.
        self.assertEqual(maintenance.inspect_checkpoint(str(backup))[0][
            "generation"], 1)
        self.assertEqual(self.store, str(Path(self.workspace.name) / "state.sqlite"))


if __name__ == "__main__":
    unittest.main()
