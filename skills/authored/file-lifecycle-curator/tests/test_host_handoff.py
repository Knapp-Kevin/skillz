"""Agent-host handoff contract with controlled physical fixture operations.

All physical changes are confined to unittest TemporaryDirectory; neither
the skill nor its runtime helpers ever touch the simulated source.
"""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from test_state import snapshot, next_scan, plan
import host_handoff
import maintenance
import state


class HostHandoffTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root = Path(self.tmp.name)
        self.root = root
        self.store = str(root / "checkpoint.sqlite")
        (root / "inbox").mkdir()
        (root / "organized").mkdir()
        (root / "inbox" / "alpha-id").write_bytes(b"source-one-controlled")
        (root / "inbox" / "beta-id").write_bytes(b"source-two-controlled")
        self.first = snapshot()
        self.initial_plan = plan(self.first)
        committed = state.process(
            self.store, self.first, self.initial_plan, "agent-initial",
            "hourly", commit=True, initialize=True, expected_generation=0,
            ack_private_store=True)
        self.assertTrue(committed["checkpoint_written"])

    def fresh(self):
        later = next_scan(self.first)
        later["records"][0]["locator_token"] = "loc-alpha-organized"
        newer_plan = plan(later, observed="2026-11-23T11:00:00-05:00",
                          snapshot_id="plan-shot-two")
        return later, newer_plan

    def test_real_temp_host_move_readback_and_separate_checkpoint(self):
        original = self.root / "inbox" / "alpha-id"
        destination = self.root / "organized" / "alpha-id"
        digest = hashlib.sha256(original.read_bytes()).hexdigest()
        # This is THE CONTROLLED TEST HOST performing an actual move.
        # The portable skill only consumes subsequent claimed evidence.
        original.rename(destination)
        observed = hashlib.sha256(destination.read_bytes()).hexdigest()
        self.assertFalse(original.exists())
        self.assertEqual(observed, digest)
        later, newer_plan = self.fresh()
        later["records"][0]["digest_basis"] = "observed-full-bytes"
        later["records"][0]["digest"] = observed
        newer_plan["records"][0]["observed_path"] = "organized/alpha-id"
        newer_plan["records"][0]["state"] = "VERIFIED"
        newer_plan["records"][0]["readback"] = {
            "record_id": "alpha-id", "plan_id": "file-plan",
            "plan_revision": "plan-rev-one",
            "source_revision": "rev-001",
            "destination_path": "organized/alpha-id",
            "integrity": "matched", "access": "preserved",
            "observed_at": "2026-11-23T11:00:00-05:00"}
        preview = host_handoff.preview(self.store, later, newer_plan)
        self.assertEqual(preview["status"], "HANDOFF_PREVIEW_NOT_PERSISTED")
        self.assertEqual(preview["progress"]["verified_relocations"], 1)
        self.assertEqual(preview["progress"]["planned_relocations"], 2)
        self.assertEqual(preview["progress"]["percent_of_scoped_plan"], 50.0)
        self.assertEqual(preview["operation_evidence"],
                         "NOT_INDEPENDENTLY_VERIFIED")
        self.assertEqual(preview["source_evidence"],
                         "CALLER_ASSERTED_NOT_HOST_AUTHENTICATED")
        self.assertFalse(preview["checkpoint_written"])
        self.assertEqual(maintenance.inspect_checkpoint(self.store)[0][
            "generation"], 1)
        # A separate explicit approved checkpoint operation is necessary.
        saved = state.process(self.store, later, newer_plan,
                              "agent-second", "hourly", commit=True,
                              expected_generation=1, ack_private_store=True)
        self.assertTrue(saved["checkpoint_written"])
        self.assertEqual(maintenance.inspect_checkpoint(self.store)[0][
            "generation"], 2)
        new_observation = next_scan(later, sid="shot-three",
                                    moment="2026-11-23T12:00:00-05:00")
        unconfirmed = host_handoff.preview(self.store, new_observation)
        self.assertEqual(unconfirmed["status"], "FRESH_SOURCE_PROVISIONAL")
        self.assertIsNone(unconfirmed["progress"])

    def test_replayed_receipt_cannot_be_treated_as_fresh(self):
        later, _ = self.fresh()
        old = copy.deepcopy(self.initial_plan)
        result = host_handoff.preview(self.store, later, old)
        self.assertEqual(result["status"], "STALE_PLAN_EVIDENCE_HOLD")
        self.assertIsNone(result["progress"])

    def test_checkpoint_snapshot_replay_is_not_host_qualification(self):
        old = host_handoff.preview(self.store, self.first, self.initial_plan)
        self.assertEqual(old["status"], "SAME_SNAPSHOT_NO_FRESH_HOST_EVIDENCE")
        self.assertIsNone(old["progress"])
        forged = copy.deepcopy(self.first)
        forged["records"][0]["locator_token"] = "different-locator"
        self.assertEqual(host_handoff.preview(self.store, forged)["status"],
                         "SNAPSHOT_REUSE_HOLD")

    def test_revoked_permission_suppresses_source_details(self):
        later, newer_plan = self.fresh()
        later["viewer_check"] = "denied"
        result = host_handoff.preview(self.store, later, newer_plan)
        self.assertEqual(result["status"], "ACCESS_HOLD")
        self.assertNotIn("alpha-id", json.dumps(result))
        self.assertNotIn("counts", json.dumps(result))

    def test_missing_cached_record_without_current_permission_holds(self):
        later, _ = self.fresh()
        later["records"] = later["records"][:1]
        later["coverage"] = "partial"
        later["absent_identity_access"] = "unverified"
        result = host_handoff.preview(self.store, later)
        self.assertEqual(result["status"], "ABSENT_IDENTITY_ACCESS_HOLD")
        self.assertNotIn("beta-id", json.dumps(result))

    def test_wrong_scope_and_revision_do_not_disclose_progress(self):
        later, newer_plan = self.fresh()
        later["scope"]["principal_id"] = "different-principal"
        self.assertEqual(host_handoff.preview(self.store, later)["status"],
                         "CROSS_SCOPE_HOLD")
        later, newer_plan = self.fresh()
        newer_plan["records"][0]["source_revision"] = "rev-999"
        self.assertEqual(host_handoff.preview(self.store, later, newer_plan)[
            "status"], "PLAN_SOURCE_REVISION_HOLD")

    def test_retarget_under_same_revision_blocks(self):
        later, newer_plan = self.fresh()
        newer_plan["records"][0]["target_path"] = "wrong/alpha-id"
        self.assertEqual(host_handoff.preview(self.store, later, newer_plan)[
            "status"], "PLAN_DRIFT_HOLD")

    def test_fresh_plan_preceding_source_observation_blocks(self):
        later, newer_plan = self.fresh()
        later["observed_at"] = "2026-11-23T11:30:00-05:00"
        self.assertEqual(host_handoff.preview(self.store, later, newer_plan)[
            "status"], "PLAN_BEFORE_SOURCE_HOLD")

    def test_helper_is_nonmutating_and_has_no_scheduler_or_connector(self):
        content = (ROOT / "scripts" / "host_handoff.py").read_text()
        for forbidden in ("import requests", "import socket", "subprocess",
                          "shutil.move(", "os.rename(", "os.remove(",
                          "schedule.create", "state.process("):
            self.assertNotIn(forbidden, content)


if __name__ == "__main__":
    unittest.main()
