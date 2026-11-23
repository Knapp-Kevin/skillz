"""Synthetic release provenance failures. No installer, network, or signature verifier."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "reconcile.py"
spec = importlib.util.spec_from_file_location("reconcile", SCRIPT)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
SRC = "a" * 40
OTHER = "b" * 40
PAYLOAD = b"FICTIONAL_RELEASE_PAYLOAD_V1\n"
DIGEST = hashlib.sha256(PAYLOAD).hexdigest()
DIFFERENT = hashlib.sha256(b"tampered").hexdigest()


def fixture():
    return {
        "schema_version": 1,
        "source": {"repository": "fictional/release", "commit": SRC,
                   "tag": "v0.1.0", "tag_target": SRC},
        "build": {"source_commit": SRC, "run_id": "synthetic_run_101",
                  "conclusion": "success", "checks_complete": True,
                  "required_checks": [{"name": "unit", "app": "actions"},
                                      {"name": "security", "app": "security"}],
                  "checks": [{"name": "unit", "app": "actions",
                              "state": "success", "head_sha": SRC},
                             {"name": "security", "app": "security",
                              "state": "success", "head_sha": SRC}]},
        "channels": [{"id": "linux_x64", "platform": "linux",
                      "architecture": "x86_64",
                      "filename": "fictional-installer.bin",
                      "build_sha256": DIGEST,
                      "published_sha256_claim": DIGEST,
                      "provenance": {"status": "reported_verified",
                                     "subject_sha256": DIGEST,
                                     "source_commit": SRC,
                                     "repository": "fictional/release",
                                     "verifier_receipt": "fictional-verifier-result"},
                      "install": {"status": "reported_pass",
                                  "artifact_sha256": DIGEST,
                                  "receipt": "fictional-installed-smoke"}}]
    }


class ReleaseEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "fictional-installer.bin").write_bytes(PAYLOAD)

    def inspect(self, data=None):
        return m.inspect(fixture() if data is None else data, self.root)

    def hold(self, phrase, data):
        with self.assertRaisesRegex(m.Invalid, phrase):
            self.inspect(data)

    def test_all_declared_stages_match_bytes_but_not_external_authority(self):
        result = self.inspect()
        self.assertEqual(result["status"],
                         "LOCAL_BYTE_CHAIN_MATCHED_UNTRUSTED_RECEIPTS")
        self.assertEqual(result["local_artifacts"][0]["actual_local_sha256"], DIGEST)
        for field in ("build_provider_authenticated",
                      "external_attestation_signature_verified_by_this_tool",
                      "publisher_or_download_origin_authenticated",
                      "installer_execution_observed_by_this_tool",
                      "installed_product_accepted", "release_authorized"):
            self.assertFalse(result[field], field)

    def test_real_local_byte_change_blocks_claimed_digest(self):
        (self.root / "fictional-installer.bin").write_bytes(b"tampered")
        result = self.inspect()
        self.assertEqual(result["status"], "BLOCKED_CONTRADICTORY_EVIDENCE")
        self.assertIn("LOCAL_PUBLISHED_BYTES_DIGEST_DIFFERS:linux_x64",
                      result["blockers"])

    def test_missing_published_bytes_holds(self):
        (self.root / "fictional-installer.bin").unlink()
        result = self.inspect()
        self.assertEqual(result["status"], "HOLD_INCOMPLETE_EVIDENCE")
        self.assertIn("LOCAL_ARTIFACT_UNAVAILABLE_OR_UNSAFE:linux_x64",
                      result["holds"])

    def test_build_digest_claim_conflicts_with_publisher(self):
        data = fixture()
        data["channels"][0]["published_sha256_claim"] = DIFFERENT
        self.assertIn("DECLARED_BUILD_PUBLISH_DIGEST_DIFFER:linux_x64",
                      self.inspect(data)["blockers"])

    def test_tag_does_not_resolve_to_shipped_source(self):
        data = fixture()
        data["source"]["tag_target"] = OTHER
        self.assertIn("TAG_TARGET_DIFFERS_FROM_SOURCE",
                      self.inspect(data)["blockers"])

    def test_build_source_differs_from_tag_commit(self):
        data = fixture()
        data["build"]["source_commit"] = OTHER
        self.assertIn("BUILD_SOURCE_DIFFERS_FROM_RELEASE",
                      self.inspect(data)["blockers"])

    def test_build_failed_is_not_release_ready(self):
        data = fixture()
        data["build"]["conclusion"] = "failure"
        self.assertIn("BUILD_REPORTED_FAILED", self.inspect(data)["blockers"])

    def test_build_pending_unknown_are_evidence_holds(self):
        for state in ("pending", "unknown"):
            with self.subTest(state=state):
                data = fixture()
                data["build"]["conclusion"] = state
                self.assertIn("BUILD_SUCCESS_NOT_OBSERVED",
                              self.inspect(data)["holds"])

    def test_required_check_failure_is_blocking(self):
        data = fixture()
        data["build"]["checks"][0]["state"] = "failure"
        self.assertIn("REQUIRED_CHECK_REPORTED_FAILED:unit@actions",
                      self.inspect(data)["blockers"])

    def test_required_check_non_success_is_not_passing(self):
        for state in ("pending", "cancelled", "skipped", "unknown"):
            with self.subTest(state=state):
                data = fixture()
                data["build"]["checks"][0]["state"] = state
                self.assertIn("REQUIRED_CHECK_NOT_SUCCESS:unit@actions",
                              self.inspect(data)["holds"])

    def test_check_on_earlier_sha_requires_rerun(self):
        data = fixture()
        data["build"]["checks"][0]["head_sha"] = OTHER
        self.assertIn("REQUIRED_CHECK_STALE_HEAD:unit@actions",
                      self.inspect(data)["holds"])

    def test_same_name_wrong_provider_app_is_missing_check(self):
        data = fixture()
        data["build"]["checks"][1]["app"] = "untrusted"
        self.assertIn("REQUIRED_CHECK_MISSING:security@security",
                      self.inspect(data)["holds"])

    def test_required_security_check_not_present_is_hold(self):
        data = fixture()
        data["build"]["checks"].pop()
        self.assertIn("REQUIRED_CHECK_MISSING:security@security",
                      self.inspect(data)["holds"])

    def test_incomplete_check_inventory_holds_even_if_known_checks_green(self):
        data = fixture()
        data["build"]["checks_complete"] = False
        self.assertIn("REQUIRED_CHECK_INVENTORY_INCOMPLETE",
                      self.inspect(data)["holds"])

    def test_provenance_claimed_digest_differs(self):
        data = fixture()
        data["channels"][0]["provenance"]["subject_sha256"] = DIFFERENT
        self.assertIn("ATTESTATION_SUBJECT_DIGEST_DIFFERS:linux_x64",
                      self.inspect(data)["blockers"])

    def test_provenance_repo_mismatch_blocks(self):
        data = fixture()
        data["channels"][0]["provenance"]["repository"] = "other/repo"
        self.assertIn("ATTESTATION_SOURCE_OR_REPO_DIFFERS:linux_x64",
                      self.inspect(data)["blockers"])

    def test_provenance_source_commit_mismatch_blocks(self):
        data = fixture()
        data["channels"][0]["provenance"]["source_commit"] = OTHER
        self.assertIn("ATTESTATION_SOURCE_OR_REPO_DIFFERS:linux_x64",
                      self.inspect(data)["blockers"])

    def test_failed_provenance_claim_blocks(self):
        data = fixture()
        data["channels"][0]["provenance"]["status"] = "reported_failed"
        self.assertIn("ATTESTATION_REPORTED_FAILED:linux_x64",
                      self.inspect(data)["blockers"])

    def test_missing_provenance_verification_holds(self):
        data = fixture()
        data["channels"][0]["provenance"]["status"] = "not_run"
        self.assertIn("ATTESTATION_NOT_VERIFIED_EXTERNALLY:linux_x64",
                      self.inspect(data)["holds"])

    def test_missing_verifier_receipt_holds(self):
        data = fixture()
        data["channels"][0]["provenance"]["verifier_receipt"] = None
        self.assertIn("ATTESTATION_VERIFIER_RECEIPT_MISSING:linux_x64",
                      self.inspect(data)["holds"])

    def test_installer_reports_failure_blocks(self):
        data = fixture()
        data["channels"][0]["install"]["status"] = "reported_fail"
        self.assertIn("INSTALL_REPORTED_FAILED:linux_x64",
                      self.inspect(data)["blockers"])

    def test_unrun_install_holds(self):
        data = fixture()
        data["channels"][0]["install"]["status"] = "not_run"
        self.assertIn("INSTALL_NOT_TESTED:linux_x64",
                      self.inspect(data)["holds"])

    def test_install_receipt_missing_holds(self):
        data = fixture()
        data["channels"][0]["install"]["receipt"] = None
        self.assertIn("INSTALL_RECEIPT_MISSING:linux_x64",
                      self.inspect(data)["holds"])

    def test_install_target_digest_mismatch_blocks(self):
        data = fixture()
        data["channels"][0]["install"]["artifact_sha256"] = DIFFERENT
        self.assertIn("INSTALL_ARTIFACT_DIGEST_DIFFERS:linux_x64",
                      self.inspect(data)["blockers"])

    def test_reported_verified_not_claimed_as_signature_verification(self):
        result = self.inspect()
        self.assertFalse(result["external_attestation_signature_verified_by_this_tool"])

    def test_simulated_two_channel_release(self):
        data = fixture()
        data["channels"].append(copy.deepcopy(data["channels"][0]))
        second = data["channels"][-1]
        second["id"] = "windows_x64"
        second["platform"] = "windows"
        second["filename"] = "fictional-windows.zip"
        (self.root / "fictional-windows.zip").write_bytes(PAYLOAD)
        result = self.inspect(data)
        self.assertEqual(result["declared_channel_count"], 2)
        self.assertEqual(result["status"],
                         "LOCAL_BYTE_CHAIN_MATCHED_UNTRUSTED_RECEIPTS")
        self.assertFalse(result["installed_product_accepted"])

    def test_missing_second_channel_files_prevent_full_match(self):
        data = fixture()
        data["channels"].append(copy.deepcopy(data["channels"][0]))
        data["channels"][-1]["id"] = "windows_x64"
        data["channels"][-1]["filename"] = "missing-windows.zip"
        self.assertEqual(self.inspect(data)["status"], "HOLD_INCOMPLETE_EVIDENCE")

    def test_duplicate_channel_id_refused(self):
        data = fixture()
        data["channels"].append(copy.deepcopy(data["channels"][0]))
        self.hold("DUPLICATE_CHANNEL_ID", data)

    def test_reject_empty_channel_inventory(self):
        data = fixture()
        data["channels"] = []
        self.hold("INVALID_CHANNEL_COUNT", data)

    def test_reject_more_than_32_channels(self):
        data = fixture()
        data["channels"] *= 33
        self.hold("INVALID_CHANNEL_COUNT", data)

    def test_duplicate_check_name_app_refused(self):
        data = fixture()
        data["build"]["checks"].append(copy.deepcopy(data["build"]["checks"][0]))
        self.hold("DUPLICATE_OBSERVED_CHECK", data)

    def test_duplicate_required_check_refused(self):
        data = fixture()
        data["build"]["required_checks"].append(
            copy.deepcopy(data["build"]["required_checks"][0]))
        self.hold("DUPLICATE_REQUIRED_CHECK", data)

    def test_nonboolean_checks_complete_refused(self):
        data = fixture()
        data["build"]["checks_complete"] = "true"
        self.hold("INVALID_CHECK_COMPLETENESS", data)

    def test_invalid_sha_refused(self):
        data = fixture()
        data["source"]["commit"] = "short"
        self.hold("full lowercase digest", data)

    def test_invalid_artifact_digest_refused(self):
        data = fixture()
        data["channels"][0]["build_sha256"] = "a" * 40
        self.hold("full lowercase digest", data)

    def test_path_escape_refused(self):
        for path in ("../secret", "dir/../secret", "/tmp/raw", "dir//file",
                     "./local.bin", "C:\\secret", "."):
            with self.subTest(path=path):
                data = fixture()
                data["channels"][0]["filename"] = path
                self.hold("INVALID_LOCAL_ARTIFACT_PATH", data)

    def test_root_symlink_refused_as_missing_evidence(self):
        alias = self.root / "alias"
        try:
            alias.symlink_to(self.root, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlink unavailable")
        result = m.inspect(fixture(), alias)
        self.assertEqual(result["status"], "HOLD_INCOMPLETE_EVIDENCE")

    def test_leaf_symlink_refused(self):
        target = self.root / "secret.txt"
        target.write_bytes(PAYLOAD)
        p = self.root / "fictional-installer.bin"
        p.unlink()
        try:
            p.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("symlink unavailable")
        result = self.inspect()
        self.assertEqual(result["status"], "HOLD_INCOMPLETE_EVIDENCE")

    def test_nested_parent_symlink_refused(self):
        real = self.root / "real"
        real.mkdir()
        (real / "file.bin").write_bytes(PAYLOAD)
        alias = self.root / "link"
        try:
            alias.symlink_to(real, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlink unavailable")
        data = fixture()
        data["channels"][0]["filename"] = "link/file.bin"
        self.assertEqual(self.inspect(data)["status"], "HOLD_INCOMPLETE_EVIDENCE")

    def test_directory_not_accepted_as_artifact(self):
        d = self.root / "folder"
        d.mkdir()
        data = fixture()
        data["channels"][0]["filename"] = "folder"
        self.assertEqual(self.inspect(data)["status"], "HOLD_INCOMPLETE_EVIDENCE")

    def test_oversize_artifact_holds(self):
        p = self.root / "fictional-installer.bin"
        with p.open("wb") as f:
            f.truncate(m.MAX_ARTIFACT_BYTES + 1)
        result = self.inspect()
        self.assertEqual(result["status"], "HOLD_INCOMPLETE_EVIDENCE")

    def test_missing_root_holds(self):
        result = m.inspect(fixture(), self.root / "missing")
        self.assertEqual(result["status"], "HOLD_INCOMPLETE_EVIDENCE")

    def test_invalid_extra_root_schema_field_refused(self):
        data = fixture()
        data["automatic_publish"] = True
        self.hold("unexpected field", data)

    def test_nonfinite_and_duplicate_json_keys_refused(self):
        p = self.root / "invalid.json"
        for text, needle in (
                ('{"v":1,"v":2}', "DUPLICATE_JSON_KEY"),
                ('{"v":Infinity}', "NONFINITE_JSON")):
            with self.subTest(needle=needle):
                p.write_text(text)
                with self.assertRaisesRegex(m.Invalid, needle):
                    m.read_json(p)

    def test_manifest_symlink_refused(self):
        target = self.root / "manifest.json"
        target.write_text(json.dumps(fixture()))
        alias = self.root / "alias-manifest.json"
        try:
            alias.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("symlink unavailable")
        with self.assertRaisesRegex(m.Invalid, "JSON_PATH_MISSING_OR_SYMLINKED"):
            m.read_json(alias)

    def test_cli_local_chain_success_but_not_release_authorization(self):
        p = self.root / "release.json"
        p.write_text(json.dumps(fixture()), encoding="utf8")
        process = subprocess.run(
            [sys.executable, str(SCRIPT), "--manifest", str(p),
             "--artifact-root", str(self.root), "--require-local-match"],
            capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        result = json.loads(process.stdout)
        self.assertFalse(result["release_authorized"])

    def test_cli_mismatch_exits_three_when_required(self):
        p = self.root / "release.json"
        p.write_text(json.dumps(fixture()), encoding="utf8")
        (self.root / "fictional-installer.bin").write_bytes(b"tampered")
        process = subprocess.run(
            [sys.executable, str(SCRIPT), "--manifest", str(p),
             "--artifact-root", str(self.root), "--require-local-match"],
            capture_output=True, text=True)
        self.assertEqual(process.returncode, 3)

    def test_cli_source_input_error_exits_two(self):
        p = self.root / "invalid.json"
        p.write_text("{}")
        process = subprocess.run(
            [sys.executable, str(SCRIPT), "--manifest", str(p),
             "--artifact-root", str(self.root), "--require-local-match"],
            capture_output=True, text=True)
        self.assertEqual(process.returncode, 2)

    def test_example_manifest_and_bytes_match(self):
        manifest = m.read_json(ROOT / "examples" / "synthetic-release.json")
        result = m.inspect(manifest, ROOT / "examples" / "artifacts")
        self.assertEqual(result["status"],
                         "LOCAL_BYTE_CHAIN_MATCHED_UNTRUSTED_RECEIPTS")
        self.assertEqual(result["local_artifacts"][0]["actual_local_sha256"], DIGEST)
        self.assertFalse(result["release_authorized"])


if __name__ == "__main__":
    unittest.main()
