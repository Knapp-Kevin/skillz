"""Offline synthetic cases for the optional refinement receipt checker."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "engine" / "refinement" / "check_case.py"
SPEC = importlib.util.spec_from_file_location("refinement_case", MODULE)
contract = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(contract)
EXAMPLE = ROOT / "engine" / "refinement" / "fictional-refinement-case.json"


def case():
    return json.loads(EXAMPLE.read_text(encoding="utf8"))


class RefinementCases(unittest.TestCase):
    def test_fictional_case_is_structurally_complete_not_accepted(self):
        result = contract.inspect(case())
        self.assertEqual(result["status"], "STRUCTURAL_RECEIPT_COMPLETE")
        self.assertEqual(result["decision_as_supplied"], "HOLD")
        for name in ("source_identity_authenticated", "behavioral_outcome_verified",
                     "installation_or_merge_verified", "external_execution_performed",
                     "license_authority_verified"):
            self.assertFalse(result[name])

    def test_untrusted_evidence_claim_never_becomes_validation(self):
        data = case()
        data["challenge"][0]["level"] = "HOST_OBSERVED"
        result = contract.inspect(data)
        self.assertFalse(result["behavioral_outcome_verified"])

    def test_omitted_adversarial_boundary_is_refused(self):
        data = case()
        data["challenge"] = [x for x in data["challenge"] if x["name"] != "false-green"]
        with self.assertRaisesRegex(contract.Invalid, "MISSING_ADVERSARIAL"):
            contract.inspect(data)

    def test_duplicate_case_never_conceals_missing_negative(self):
        data = case()
        data["challenge"][-1]["name"] = "original"
        with self.assertRaisesRegex(contract.Invalid, "DUPLICATE"):
            contract.inspect(data)

    def test_cannot_claim_exhaustive_index_search(self):
        data = case()
        data["discovery"]["full_corpus_claim"] = True
        with self.assertRaisesRegex(contract.Invalid, "UNSUPPORTED_EXHAUSTIVE"):
            contract.inspect(data)

    def test_unverified_cannot_be_treated_as_verified(self):
        data = case()
        data["challenge"][2]["result"] = "PASSED"
        with self.assertRaisesRegex(contract.Invalid, "UNTESTED_CANNOT"):
            contract.inspect(data)

    def test_accept_without_source_or_artifact_refused(self):
        data = case()
        data["decision"]["state"] = "ACCEPT"
        with self.assertRaisesRegex(contract.Invalid, "ACCEPT_WITHOUT_ARTIFACT"):
            contract.inspect(data)

    def test_unmerged_maintainer_change_is_not_delivery(self):
        data = case()
        data["candidate"]["source_changed"] = True
        data["decision"]["state"] = "ACCEPT"
        with self.assertRaisesRegex(contract.Invalid, "ACCEPT_UNMERGED"):
            contract.inspect(data)

    def test_user_host_artifact_does_not_require_skillz_merge(self):
        data = case()
        data["scope"]["route"] = "USER_HOST"
        data["delivery"]["artifact"] = "PORTABLE_HANDOFF"
        data["decision"]["state"] = "ACCEPT"
        self.assertEqual(contract.inspect(data)["scope"], "USER_HOST")
        self.assertFalse(contract.inspect(data)["installation_or_merge_verified"])

    def test_changed_input_cannot_fake_schema(self):
        data = case()
        data["schema_version"] = True
        with self.assertRaisesRegex(contract.Invalid, "UNSUPPORTED_SCHEMA"):
            contract.inspect(data)

    def test_unknown_decision_cannot_sneak_through(self):
        data = case()
        data["decision"]["state"] = "AUTO_PUBLISH"
        with self.assertRaisesRegex(contract.Invalid, "INVALID_DECISION"):
            contract.inspect(data)

    def test_unknown_side_effect_flags_are_refused(self):
        data = case()
        data["run_untrusted_script"] = True
        with self.assertRaisesRegex(contract.Invalid, "INVALID_FIELDS"):
            contract.inspect(data)

    def test_cli_fictional_case_no_external_calls(self):
        run = subprocess.run([sys.executable, str(MODULE), "--input", str(EXAMPLE)],
                             capture_output=True, text=True, timeout=10)
        self.assertEqual(run.returncode, 0, run.stderr)
        result = json.loads(run.stdout)
        self.assertEqual(result["status"], "STRUCTURAL_RECEIPT_COMPLETE")
        self.assertFalse(result["external_execution_performed"])

    def test_duplicate_json_and_nonfinite_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "malformed.json"
            for source in ('{"a":1,"a":2}', '{"weight":NaN}'):
                with self.subTest(source=source):
                    p.write_text(source, encoding="utf8")
                    run = subprocess.run(
                        [sys.executable, str(MODULE), "--input", str(p)],
                        capture_output=True, text=True, timeout=10)
                    self.assertEqual(run.returncode, 2)
                    self.assertIn("REFINEMENT_CASE_HOLD", run.stderr)


if __name__ == "__main__":
    unittest.main()
