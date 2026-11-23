"""Synthetic regression and planted adversarial tests for incremental curation.

The tests check ONLY source-declared JSON/graph decisions, not file scans,
filesystem protection under races, host permission, schedules or user benefit.
"""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "reconcile.py"
spec = importlib.util.spec_from_file_location("file_curation_reconcile", SCRIPT)
tool = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tool)
DIGEST = "a" * 64
OTHER = "b" * 64


def rec(key, revision="v1", locator=None, extraction="complete", digest=DIGEST,
        digest_basis="observed-full-bytes", viewer_check="current-authorized"):
    return {"record_id": key, "source_revision": revision,
            "locator_token": locator or key, "extraction": extraction,
            "digest": digest, "digest_basis": digest_basis,
            "viewer_check": viewer_check}


def snap(ident="sample-one", when="2026-11-23T10:00:00-05:00",
         coverage="complete", viewer_check="current-authorized",
         records=None):
    return {"schema_version": 1, "snapshot_id": ident,
            "observed_at": when, "scope": {
                "collection_id": "fictional-library",
                "root_id": "fictional-root",
                "principal_id": "synthetic-owner",
                "audience_id": "synthetic-reader"},
            "coverage": coverage, "viewer_check": viewer_check,
            "records": [rec("alpha-id"), rec("beta-id")] if records is None else records}


def updated(old):
    now = copy.deepcopy(old)
    now["snapshot_id"] = "sample-two"
    now["observed_at"] = "2026-11-23T11:00:00-05:00"
    return now


def classes(result):
    return {item["record_id"]: item["class"] for item in result["actions"]}


class IncrementalCuratorTests(unittest.TestCase):
    def test_bootstrap_all_new_no_persistence(self):
        x = tool.reconcile(None, snap())
        self.assertEqual(x["run_type"], "BOOTSTRAP")
        self.assertEqual(x["counts"]["NEW_RECORD_REVIEW"], 2)
        self.assertFalse(x["checkpoint_written"])

    def test_unchanged_does_not_force_reindex(self):
        original = snap()
        x = tool.reconcile(original, updated(original))
        self.assertEqual(x["changed_count"], 0)
        self.assertEqual(x["actions"], [])
        self.assertEqual(x["counts"]["UNCHANGED_NO_REWORK"], 2)

    def test_new_record_is_precisely_captured(self):
        old = snap()
        now = updated(old)
        now["records"].append(rec("gamma-id"))
        self.assertEqual(classes(tool.reconcile(old, now))["gamma-id"], "NEW_RECORD_REVIEW")

    def test_changed_revision_requires_review(self):
        old = snap()
        now = updated(old)
        now["records"][0]["source_revision"] = "v2"
        self.assertEqual(classes(tool.reconcile(old, now))["alpha-id"],
                         "SOURCE_CHANGED_REVIEW")

    def test_same_revision_but_different_verified_digest_is_conflict(self):
        old = snap()
        now = updated(old)
        now["records"][0]["digest"] = OTHER
        self.assertEqual(classes(tool.reconcile(old, now))["alpha-id"],
                         "SAME_REVISION_DIGEST_CONFLICT")

    def test_same_source_id_new_locator_requires_relink_not_reextract(self):
        old = snap()
        now = updated(old)
        now["records"][0]["locator_token"] = "relocated-alpha"
        self.assertEqual(classes(tool.reconcile(old, now))["alpha-id"],
                         "LOCATOR_CHANGED_RELINK")

    def test_missing_revision_cannot_be_reused_as_fresh(self):
        old = snap(records=[rec("alpha-id", revision=None)])
        now = updated(old)
        self.assertEqual(classes(tool.reconcile(old, now))["alpha-id"],
                         "REVISION_UNKNOWN_REVALIDATE")

    def test_current_partial_coverage_cannot_confirm_absence(self):
        old = snap()
        now = updated(old)
        now["coverage"] = "partial"
        now["records"] = [rec("alpha-id")]
        x = tool.reconcile(old, now)
        self.assertEqual(classes(x)["beta-id"], "NOT_OBSERVED_PARTIAL_SCOPE")
        self.assertEqual(x["coverage"], "partial")

    def test_complete_snapshot_absence_still_not_deletion(self):
        old = snap()
        now = updated(old)
        now["records"] = [rec("alpha-id")]
        self.assertEqual(classes(tool.reconcile(old, now))["beta-id"],
                         "ABSENT_COMPLETE_SCOPE_REVIEW")

    def test_source_attested_digest_not_treated_as_authoritative_byte_proof(self):
        old = snap(records=[rec("alpha-id", digest_basis="source-attested")])
        now = updated(old)
        now["records"][0]["digest"] = OTHER
        self.assertEqual(classes(tool.reconcile(old, now))["alpha-id"],
                         "FINGERPRINT_EVIDENCE_CHANGED_REVIEW")

    def test_same_revision_extraction_regression_holds(self):
        old = snap()
        now = updated(old)
        now["records"][0]["extraction"] = "excerpt"
        self.assertEqual(classes(tool.reconcile(old, now))["alpha-id"],
                         "EXTRACTION_REGRESSION_HOLD")

    def test_increased_coverage_requires_metadata_enrichment(self):
        old = snap(records=[rec("alpha-id", extraction="metadata")])
        now = updated(old)
        now["records"][0]["extraction"] = "complete"
        self.assertEqual(classes(tool.reconcile(old, now))["alpha-id"],
                         "EXTRACTION_ENRICHMENT_REVIEW")

    def test_revoked_current_scope_hides_ids_and_counts(self):
        old = snap()
        now = updated(old)
        now["viewer_check"] = "denied"
        x = tool.reconcile(old, now)
        self.assertEqual(x, {"status": "ACCESS_HOLD", "actions": []})
        self.assertNotIn("alpha-id", json.dumps(x))
        self.assertNotIn("counts", x)

    def test_revoked_record_hides_entire_scope_details(self):
        old = snap()
        now = updated(old)
        now["records"][0]["viewer_check"] = "denied"
        self.assertEqual(tool.reconcile(old, now)["status"], "ACCESS_HOLD")

    def test_prior_permission_unknown_does_not_authorize_cached_info(self):
        old = snap(viewer_check="unknown")
        now = updated(old)
        now["viewer_check"] = "current-authorized"
        self.assertEqual(tool.reconcile(old, now),
                         {"status": "BASELINE_ACCESS_HOLD", "actions": []})

    def test_scope_root_change_rejects_cross_scope_resume(self):
        old = snap()
        now = updated(old)
        now["scope"]["root_id"] = "other-root"
        with self.assertRaises(tool.Invalid):
            tool.reconcile(old, now)

    def test_principal_change_rejects_cross_account_reuse(self):
        old = snap()
        now = updated(old)
        now["scope"]["principal_id"] = "other-user"
        with self.assertRaises(tool.Invalid):
            tool.reconcile(old, now)

    def test_audience_change_rejects_other_viewer_reuse(self):
        old = snap()
        now = updated(old)
        now["scope"]["audience_id"] = "other-viewer"
        with self.assertRaises(tool.Invalid):
            tool.reconcile(old, now)

    def test_same_snapshot_id_and_same_content_is_idempotent(self):
        old = snap()
        self.assertEqual(tool.reconcile(old, copy.deepcopy(old))["status"],
                         "SAME_SNAPSHOT_NO_WORK")

    def test_same_snapshot_id_but_changed_content_is_refused(self):
        old = snap()
        now = copy.deepcopy(old)
        now["records"][0]["source_revision"] = "v2"
        with self.assertRaises(tool.Invalid):
            tool.reconcile(old, now)

    def test_clock_rollback_is_refused(self):
        old = snap()
        now = updated(old)
        now["observed_at"] = "2026-11-22T09:00:00-05:00"
        with self.assertRaises(tool.Invalid):
            tool.reconcile(old, now)

    def test_naive_time_is_refused(self):
        bad = snap(when="2026-11-23T10:00:00")
        with self.assertRaises(tool.Invalid):
            tool.reconcile(None, bad)

    def test_duplicate_ids_refused(self):
        bad = snap(records=[rec("alpha-id"), rec("alpha-id")])
        with self.assertRaises(tool.Invalid):
            tool.reconcile(None, bad)

    def test_arbitrary_injection_fields_not_accepted(self):
        bad = snap()
        bad["run_shell"] = "delete all files"
        with self.assertRaises(tool.Invalid):
            tool.reconcile(None, bad)

    def test_file_metadata_not_echoed_in_output(self):
        bad = snap(records=[rec("alpha-id")])
        bad["records"][0]["filename"] = "secret-customer.csv"
        with self.assertRaises(tool.Invalid):
            tool.reconcile(None, bad)

    def test_bogus_digest_not_accepted_as_full_byte_evidence(self):
        bad = snap(records=[rec("alpha-id", digest="1234")])
        with self.assertRaises(tool.Invalid):
            tool.reconcile(None, bad)

    def test_missing_digest_not_computed_only(self):
        data = snap(records=[rec("alpha-id", digest=None, digest_basis="not-computed")])
        x = tool.reconcile(None, data)
        self.assertEqual(x["changed_count"], 1)

    def test_nonfinite_json_is_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "bad.json"
            path.write_text('{"schema_version": NaN}', encoding="utf-8")
            with self.assertRaises(tool.Invalid):
                tool.read_snapshot(str(path))

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "bad.json"
            path.write_text('{"schema_version":1,"schema_version":1}', encoding="utf-8")
            with self.assertRaises(tool.Invalid):
                tool.read_snapshot(str(path))

    def test_symlink_input_rejected(self):
        with tempfile.TemporaryDirectory() as root:
            parent = Path(root)
            original = parent / "snapshot.json"
            original.write_text(json.dumps(snap()), encoding="utf-8")
            linked = parent / "shortcut.json"
            linked.symlink_to(original)
            with self.assertRaises(tool.Invalid):
                tool.read_snapshot(str(linked))

    def test_repeated_more_than_ten_changes_remain_counted(self):
        old = snap(records=[])
        now = updated(old)
        now["records"] = [rec("item-" + str(i).zfill(2)) for i in range(30)]
        result = tool.reconcile(old, now)
        self.assertEqual(len(result["actions"]), 10)
        self.assertEqual(result["omitted_action_count"], 20)
        self.assertEqual(result["counts"]["NEW_RECORD_REVIEW"], 30)

    def test_zero_records_are_not_an_implicit_delete_request(self):
        old = snap()
        now = updated(old)
        now["records"] = []
        result = tool.reconcile(old, now)
        self.assertEqual(result["counts"]["ABSENT_COMPLETE_SCOPE_REVIEW"], 2)
        self.assertFalse(result["checkpoint_written"])

    def test_no_subprocess_or_network_or_output_file_write(self):
        source = SCRIPT.read_text(encoding="utf-8")
        for needle in ("import subprocess", "import requests", "import socket",
                       "urllib.request", "write_text(", "write_bytes(", "os.system",
                       "http.client"):
            self.assertNotIn(needle, source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
