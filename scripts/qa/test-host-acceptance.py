"""Fictional offline receipt challenges; never invoke a consumer host."""
import copy
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("host_acceptance", ROOT / "engine/builder/host_acceptance.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.archive = Path(tmp.name) / "demo-claude.zip"
        self.archive.write_bytes(b"fictional archive identity only")
        self.digest = hashlib.sha256(self.archive.read_bytes()).hexdigest()
        self.manifest_sha = "b" * 64
        self.manifest = {"schema_version": 1, "source_commit": "a" * 40,
                         "skills": [{"id": "demo", "package_tree_sha": "c" * 40,
                                     "hosts": {"claude-apps": {"status": "PACKAGE_READY",
                                                              "blockers": [], "asset": self.archive.name,
                                                              "sha256": self.digest}}}]}
        self.receipt = {"schema_version": 1, "skill": "demo", "host": "claude-apps",
                        "source_commit": "a" * 40, "package_tree_sha": "c" * 40,
                        "manifest_sha256": self.manifest_sha, "asset": self.archive.name,
                        "sha256": self.digest, "environment": {k: "fictional-" + k for k in m.ENV_FIELDS},
                        "execution_kind": "NATIVE_HOST_CLAIMED", "authorization": "APPROVAL_CLAIMED",
                        "cases": [{"stage": s, "status": "PASS_CLAIMED",
                                   "evidence_id": "e-" + s, "oracle_id": "o-" + s} for s in m.STAGES]}

    def check(self):
        return m.validate(self.manifest, self.manifest_sha, self.archive, self.receipt)

    def test_complete_claims_never_become_observed_or_accepted(self):
        r = self.check()
        self.assertEqual(r["status"], "COMPLETE_CLAIMS_REVIEW_REQUIRED")
        for key in ("host_execution_observed", "authorization_verified", "independent_oracles_verified",
                    "consumer_accepted", "installed_or_published", "manifest_authenticity_verified"):
            self.assertIs(r[key], False)

    def test_wrong_revision_or_manifest_or_asset_rejected(self):
        original = copy.deepcopy(self.receipt)
        for key, value in (("source_commit", "d" * 40), ("manifest_sha256", "d" * 64),
                           ("package_tree_sha", "d" * 40), ("asset", "demo.zip"),
                           ("sha256", "d" * 64)):
            with self.subTest(key=key):
                self.receipt = dict(original, **{key: value})
                with self.assertRaises(ValueError):
                    self.check()

    def test_changed_archive_rejected(self):
        self.archive.write_bytes(b"other")
        with self.assertRaisesRegex(ValueError, "ARCHIVE_DIGEST_MISMATCH"):
            self.check()

    def test_held_or_unassessed_profile_not_native_eligible(self):
        self.manifest["skills"][0]["hosts"]["claude-apps"]["status"] = "HOLD"
        with self.assertRaisesRegex(ValueError, "HOST_PACKAGE_HOLD"):
            self.check()
        self.receipt["host"] = "chatgpt"
        with self.assertRaisesRegex(ValueError, "HOST_UNASSESSED"):
            self.check()

    def test_missing_duplicate_and_reused_evidence_rejected(self):
        original = copy.deepcopy(self.receipt["cases"])
        for cases in (original[:-1], original[:-1] + [original[0]],
                      original[:-1] + [dict(original[-1], evidence_id=original[0]["evidence_id"])]):
            self.receipt["cases"] = cases
            with self.assertRaises(ValueError):
                self.check()

    def test_no_load_or_activation_cannot_support_behavior(self):
        for stage in ("load", "positive_trigger"):
            with self.subTest(stage=stage):
                original = copy.deepcopy(self.receipt["cases"])
                for case in self.receipt["cases"]:
                    if case["stage"] == stage:
                        case.update(status="NOT_RUN", evidence_id=None, oracle_id=None)
                with self.assertRaises(ValueError):
                    self.check()
                self.receipt["cases"] = original

    def test_emulation_or_missing_authority_is_hold(self):
        self.receipt["execution_kind"] = "EMULATED"
        self.assertEqual(self.check()["status"], "HOLD_INCOMPLETE_NATIVE_CLAIM")
        self.receipt["execution_kind"] = "NATIVE_HOST_CLAIMED"
        self.receipt["authorization"] = "NOT_ESTABLISHED"
        self.assertEqual(self.check()["status"], "HOLD_INCOMPLETE_NATIVE_CLAIM")

    def test_reported_failure_and_missing_cleanup_are_not_pass(self):
        self.receipt["cases"][-1]["status"] = "FAIL_CLAIMED"
        self.assertEqual(self.check()["status"], "HOLD_REPORTED_FAILURE")
        self.receipt["cases"][-1].update(status="NOT_RUN", evidence_id=None, oracle_id=None)
        self.assertEqual(self.check()["status"], "HOLD_INCOMPLETE_NATIVE_CLAIM")

    def test_not_run_cannot_contain_pass_claims(self):
        self.receipt["execution_kind"] = "NOT_RUN"
        with self.assertRaisesRegex(ValueError, "NOT_RUN_WITH_OBSERVATION_CLAIM"):
            self.check()

    def test_duplicate_manifest_skill_and_unknown_receipt_field_rejected(self):
        self.manifest["skills"].append(self.manifest["skills"][0])
        with self.assertRaisesRegex(ValueError, "SKILL_MISSING_OR_DUPLICATE"):
            self.check()
        self.manifest["skills"].pop()
        self.receipt["verified"] = True
        with self.assertRaisesRegex(ValueError, "INVALID_RECEIPT_FIELDS"):
            self.check()


if __name__ == "__main__":
    unittest.main(verbosity=2)
