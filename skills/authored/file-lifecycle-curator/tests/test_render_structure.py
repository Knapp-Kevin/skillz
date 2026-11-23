"""Adversarial source-only tests for a long-lived agent's visual structure view.

No host, actual file organization, source permission or read-back took place.
"""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "render_structure.py"
spec = importlib.util.spec_from_file_location("structure_visual", SCRIPT)
visual = importlib.util.module_from_spec(spec)
spec.loader.exec_module(visual)


def item(name="doc-one", **updates):
    data = {"record_id": name, "original_path": "inbox/" + name,
            "observed_path": "inbox/" + name, "target_path": "organized/" + name,
            "source_revision": "rev-1", "state": "PROPOSED", "readback": None,
            "viewer_check": "current-authorized"}
    data.update(updates)
    return data


def snapshot(*records, ident="shot-one", when="2026-11-23T14:00:00-05:00",
             coverage="complete", viewer="current-authorized"):
    return {"schema_version": 1, "plan_id": "plan-one",
            "plan_revision": "rev-one", "snapshot_id": ident,
            "observed_at": when, "scope": {
                "collection_id": "library-one", "root_id": "root-one",
                "principal_id": "user-one", "audience_id": "viewer-one"},
            "coverage": coverage, "viewer_check": viewer,
            "records": list(records)}


def after(old):
    result = copy.deepcopy(old)
    result["snapshot_id"] = "shot-two"
    result["observed_at"] = "2026-11-23T15:00:00-05:00"
    return result


def verified(record, plan_revision="rev-one"):
    copy_record = copy.deepcopy(record)
    copy_record["state"] = "VERIFIED"
    copy_record["observed_path"] = copy_record["target_path"]
    copy_record["readback"] = {
        "record_id": copy_record["record_id"],
        "plan_id": "plan-one", "plan_revision": plan_revision,
        "source_revision": copy_record["source_revision"],
        "destination_path": copy_record["target_path"],
        "integrity": "matched", "access": "preserved",
        "observed_at": "2026-11-23T13:30:00-05:00"}
    return copy_record


class StructureVisualizationTests(unittest.TestCase):
    def test_proposal_not_reported_as_applied(self):
        out = visual.checked_view(snapshot(item()))
        self.assertEqual(out["progress"]["planned_relocations"], 1)
        self.assertEqual(out["progress"]["verified_relocations"], 0)
        self.assertIn("Proposed target (NOT APPLIED)", out["visuals"]["proposed"])
        self.assertNotIn("organized/doc-one", out["visuals"]["observed"])

    def test_readback_is_required_for_verified(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(item(state="VERIFIED",
                observed_path="organized/doc-one")))

    def test_receipt_with_observed_target_counts_verified(self):
        out = visual.checked_view(snapshot(verified(item())))
        self.assertEqual(out["progress"]["verified_relocations"], 1)
        self.assertEqual(out["progress"]["percent_of_scoped_plan"], 100)
        self.assertIn("RECEIPT_ASSERTED", out["visuals"]["verified"])

    def test_execution_not_equivalent_to_verified_completion(self):
        out = visual.checked_view(snapshot(item(state="EXECUTED")))
        self.assertEqual(out["progress"]["verified_relocations"], 0)
        self.assertEqual(out["progress"]["state_counts"]["EXECUTED"], 1)

    def test_approval_not_equivalent_to_verified(self):
        out = visual.checked_view(snapshot(item(state="APPROVED")))
        self.assertEqual(out["progress"]["verified_relocations"], 0)

    def test_unplanned_record_not_hypothetically_moved(self):
        out = visual.checked_view(snapshot(item(state="UNPLANNED",
                                      target_path=None)))
        self.assertEqual(out["progress"]["planned_relocations"], 0)
        self.assertEqual(out["progress"]["percent_of_scoped_plan"], None)
        self.assertIn("UNPLACED_KEEP_CURRENT", out["visuals"]["proposed"])
        self.assertIn("inbox/", out["visuals"]["proposed"])

    def test_unchanged_is_not_a_relocation(self):
        unchanged = item(state="UNCHANGED", target_path="inbox/doc-one")
        out = visual.checked_view(snapshot(unchanged))
        self.assertEqual(out["progress"]["verified_relocations"], 0)
        self.assertEqual(out["progress"]["planned_relocations"], 0)

    def test_verified_requires_current_observed_at_target(self):
        bad = verified(item())
        bad["observed_path"] = bad["original_path"]
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(bad))

    def test_stale_plan_revision_readback_cannot_be_reused(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(verified(item(), "obsolete-rev")))

    def test_readback_source_revision_must_match_current(self):
        bad = verified(item())
        bad["readback"]["source_revision"] = "different"
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(bad))

    def test_readback_permission_must_be_preserved(self):
        bad = verified(item())
        bad["readback"]["access"] = "broadened"
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(bad))

    def test_readback_integrity_must_be_asserted_matched(self):
        bad = verified(item())
        bad["readback"]["integrity"] = "not-checked"
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(bad))

    def test_readback_after_snapshot_time_invalid(self):
        bad = verified(item())
        bad["readback"]["observed_at"] = "2026-11-24T14:00:00-05:00"
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(bad))

    def test_duplicate_proposed_destination_rejected(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(item(), item("doc-two",
                                      target_path="organized/doc-one")))

    def test_file_folder_collision_rejected(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(item(target_path="organized"),
                                      item("doc-two", target_path="organized/doc-two")))

    def test_relative_path_traversal_rejected(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(item(target_path="../private/data")))

    def test_mermaid_injection_label_rejected(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(item(target_path='other/x"] --> Z["bad')))

    def test_external_absolute_path_rejected(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(item(target_path="/root/private")))

    def test_current_collection_access_denied_suppresses_output(self):
        out = visual.checked_view(snapshot(item(), viewer="denied"))
        self.assertEqual(out, {"status": "ACCESS_HOLD", "visuals": None})
        self.assertNotIn("doc-one", json.dumps(out))

    def test_current_record_access_denied_suppresses_output(self):
        out = visual.checked_view(snapshot(item(viewer_check="denied")))
        self.assertEqual(out, {"status": "ACCESS_HOLD", "visuals": None})
        self.assertNotIn("doc-one", json.dumps(out))

    def test_cross_principal_resume_rejected(self):
        old = snapshot(item())
        now = after(old)
        now["scope"]["principal_id"] = "someone-else"
        with self.assertRaises(visual.Invalid):
            visual.checked_view(now, old)

    def test_missing_cached_id_holds_without_leak(self):
        old = snapshot(item())
        now = after(old)
        now["records"] = []
        out = visual.checked_view(now, old)
        self.assertEqual(out, {"status": "ABSENT_IDENTITY_ACCESS_HOLD", "visuals": None})

    def test_replan_revision_is_not_silent_progress(self):
        old = snapshot(item())
        now = after(old)
        now["plan_revision"] = "rev-two"
        self.assertEqual(visual.checked_view(now, old)["status"], "REPLAN_REVIEW")

    def test_plan_target_changed_without_new_revision_holds(self):
        old = snapshot(item())
        now = after(old)
        now["records"][0]["target_path"] = "another/doc-one"
        self.assertEqual(visual.checked_view(now, old)["status"], "PLAN_DRIFT_HOLD")

    def test_verified_status_regression_is_reported(self):
        old = snapshot(verified(item()))
        now = after(old)
        now["records"][0] = item(state="FAILED")
        out = visual.checked_view(now, old)
        self.assertEqual(out["progress"]["regressed_record_ids"], ["doc-one"])
        self.assertEqual(out["progress"]["verified_relocations"], 0)

    def test_same_snapshot_idempotent(self):
        old = snapshot(item())
        out = visual.checked_view(old, copy.deepcopy(old))
        self.assertEqual(out["status"], "SAME_SNAPSHOT_NO_WORK")

    def test_same_snapshot_conflicting_data_refused(self):
        old = snapshot(item())
        now = copy.deepcopy(old)
        now["records"][0]["state"] = "APPROVED"
        with self.assertRaises(visual.Invalid):
            visual.checked_view(now, old)

    def test_truncated_view_has_explicit_omission_count(self):
        rows = [item("file-" + str(i).zfill(3)) for i in range(40)]
        out = visual.checked_view(snapshot(*rows))
        self.assertTrue(out["visuals"]["truncated"])
        self.assertEqual(out["visuals"]["shown_record_count"], 24)
        self.assertEqual(out["visuals"]["omitted_record_count"], 16)
        self.assertEqual(out["progress"]["planned_relocations"], 40)

    def test_partial_scope_never_claims_total_percent(self):
        out = visual.checked_view(snapshot(verified(item()), coverage="partial"))
        self.assertIsNone(out["progress"]["percent_of_scoped_plan"])
        self.assertEqual(out["progress"]["denominator_basis"], "PARTIAL_SCOPE_NO_PERCENT")

    def test_multiple_views_are_not_same_tree(self):
        out = visual.checked_view(snapshot(item()))
        self.assertIn("inbox/", out["visuals"]["observed"])
        self.assertIn("organized/", out["visuals"]["proposed"])
        self.assertNotIn("organized/", out["visuals"]["verified"])
        self.assertIn("flowchart LR", out["visuals"]["mermaid"])

    def test_known_noop_not_hundred_percent(self):
        out = visual.checked_view(snapshot())
        self.assertEqual(out["progress"]["planned_relocations"], 0)
        self.assertIsNone(out["progress"]["percent_of_scoped_plan"])

    def test_duplicate_current_path_rejected(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(item(), item("doc-two",
                                      observed_path="inbox/doc-one")))

    def test_unsupported_status_rejected(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(item(state="MOVED_AND_DONE")))

    def test_receipt_wrong_plan_id_rejected(self):
        bad = verified(item())
        bad["readback"]["plan_id"] = "different-plan"
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(bad))

    def test_rollback_not_counted_as_verified(self):
        rolled = item(state="ROLLED_BACK")
        rolled["readback"] = {
            "record_id": "doc-one", "plan_id": "plan-one",
            "plan_revision": "rev-one", "source_revision": "rev-1",
            "destination_path": "inbox/doc-one", "integrity": "matched",
            "access": "preserved",
            "observed_at": "2026-11-23T13:30:00-05:00"}
        out = visual.checked_view(snapshot(rolled))
        self.assertEqual(out["progress"]["verified_relocations"], 0)
        self.assertEqual(out["progress"]["state_counts"]["ROLLED_BACK"], 1)

    def test_unverified_recognition_cannot_use_readback_field(self):
        bad = verified(item())
        bad["state"] = "EXECUTED"
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(bad))

    def test_repeated_current_run_requires_monotonic_observation(self):
        old = snapshot(item())
        now = after(old)
        now["observed_at"] = "2026-11-22T14:00:00-05:00"
        with self.assertRaises(visual.Invalid):
            visual.checked_view(now, old)

    def test_source_does_not_write_or_start_jobs(self):
        data = SCRIPT.read_text(encoding="utf-8")
        for forbidden in ("import subprocess", "urllib.request", "import requests",
                          "import socket", "write_text(", "write_bytes(", "os.system("):
            self.assertNotIn(forbidden, data)


    def test_target_occupied_by_unplanned_file_is_rejected(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(
                item("doc-one", target_path="inbox/doc-two"),
                item("doc-two", state="UNPLANNED", target_path=None)))

    def test_target_occupied_by_a_moving_file_needs_staging_review(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(
                item("doc-one", target_path="inbox/doc-two"),
                item("doc-two", target_path="organized/doc-two")))

    def test_target_cannot_replace_existing_directory_with_file(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(
                item("doc-one", target_path="other"),
                item("doc-two", state="UNPLANNED", target_path=None,
                     observed_path="other/doc-two")))

    def test_target_cannot_use_existing_file_as_folder(self):
        with self.assertRaises(visual.Invalid):
            visual.checked_view(snapshot(
                item("doc-one", target_path="inbox/doc-two/nested"),
                item("doc-two", state="UNPLANNED", target_path=None)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
