"""Adversarial regressions for CI Guard's cross-workflow overlap inventory."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "ci_overlap.py"
spec = importlib.util.spec_from_file_location("ci_overlap", SCRIPT)
overlap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(overlap)


def graph():
    return {
        "nodes": {
            "accept": {"calls": ["check-model", "nested"]},
            "nested": {"calls": ["run-repro"]},
            "standalone": {"calls": ["run-repro"]},
            "run-repro": {
                "command": "python -m project.verify_reproducibility",
                "obligation": "artifact-determinism",
                "inputs": "tree-SHA-H",
            },
            "check-model": {
                "command": "python -m project.validate_model",
                "obligation": "model-consistency",
                "inputs": "tree-SHA-H",
            },
            "different": {
                "command": "python -m project.check_signatures",
                "obligation": "artifact-signatures",
                "inputs": "tree-SHA-H",
            },
        },
        "entrypoints": [
            {"id": "full-gate", "cohort": "ready-H", "environment": "linux-locked",
             "trust_boundary": "untrusted-pr", "invokes": ["accept"]},
            {"id": "standalone-repro", "cohort": "ready-H",
             "environment": "linux-locked",
             "trust_boundary": "untrusted-pr", "invokes": ["standalone"]},
        ],
        "decisions": {},
    }


class OverlapTest(unittest.TestCase):
    def finding(self, data=None):
        result = overlap.audit(graph() if data is None else data)
        self.assertEqual(result["status"], "ANALYST_GRAPH_ONLY_NOT_HOST_VERIFIED")
        self.assertEqual(len(result["findings"]), 1)
        return result["findings"][0]

    def test_nested_alias_is_found_as_partial_overlap(self):
        finding = self.finding()
        self.assertEqual(finding["classification"], "PARTIAL_OVERLAP")
        self.assertEqual(finding["disposition"], "UNDISPOSED")
        self.assertEqual(finding["terminal_commands"],
                         ["python -m project.verify_reproducibility"])

    def test_same_underlying_command_both_exclusive_is_exact_candidate_only(self):
        data = graph()
        data["entrypoints"][0]["invokes"] = ["nested"]
        finding = self.finding(data)
        self.assertEqual(finding["classification"], "EXACT_DUPLICATE_CANDIDATE")
        self.assertFalse(finding["resolved"])

    def test_different_platform_is_unproven_not_safe_to_remove(self):
        data = graph()
        data["entrypoints"][1]["environment"] = "windows-locked"
        finding = self.finding(data)
        self.assertEqual(finding["classification"], "UNPROVEN")
        data["decisions"]["full-gate|standalone-repro"] = {
            "disposition": "CONSOLIDATE", "evidence": "same command"}
        self.assertEqual(self.finding(data)["disposition"], "UNDISPOSED")

    def test_different_input_is_unproven(self):
        data = graph()
        data["nodes"]["other-repro"] = {
            "command": data["nodes"]["run-repro"]["command"],
            "obligation": "artifact-determinism",
            "inputs": "different-merge-base",
        }
        data["nodes"]["standalone"]["calls"] = ["other-repro"]
        self.assertEqual(self.finding(data)["classification"], "UNPROVEN")

    def test_independent_release_attestation_claim_requires_disposition(self):
        data = graph()
        data["entrypoints"][1]["independence"] = {
            "reason": "release-signing boundary",
            "evidence": "independent signing transcript",
        }
        finding = self.finding(data)
        self.assertEqual(finding["classification"], "JUSTIFIED_REPETITION_CLAIM")
        self.assertFalse(finding["resolved"])
        data["decisions"]["full-gate|standalone-repro"] = {
            "disposition": "KEEP",
            "evidence": "signatures verified separately by a trusted release actor",
        }
        self.assertTrue(self.finding(data)["resolved"])

    def test_disposition_requires_actual_evidence(self):
        data = graph()
        data["decisions"]["full-gate|standalone-repro"] = {
            "disposition": "VERIFY", "evidence": " ",
        }
        self.assertEqual(self.finding(data)["disposition"], "UNDISPOSED")
        data["decisions"]["full-gate|standalone-repro"]["evidence"] = "pending fault injection"
        self.assertTrue(self.finding(data)["resolved"])

    def test_distinct_verifiers_not_duplicates(self):
        data = graph()
        data["entrypoints"][1]["invokes"] = ["different"]
        self.assertEqual(overlap.audit(data)["findings"], [])

    def test_separate_candidate_revisions_are_not_duplicates(self):
        data = graph()
        data["entrypoints"][1]["cohort"] = "release-H2"
        self.assertEqual(overlap.audit(data)["findings"], [])

    def test_unknown_assurance_context_is_not_safely_equivalent(self):
        data = graph()
        data["entrypoints"][1]["trust_boundary"] = "UNKNOWN"
        self.assertEqual(self.finding(data)["classification"], "UNPROVEN")
        data = graph()
        data["nodes"]["run-repro"]["inputs"] = "UNKNOWN"
        self.assertEqual(self.finding(data)["classification"], "UNPROVEN")

    def test_cycle_and_missing_invocation_fail_closed(self):
        data = graph()
        data["nodes"]["nested"] = {"calls": ["accept"]}
        with self.assertRaisesRegex(ValueError, "cycle"):
            overlap.audit(data)
        data = graph()
        data["nodes"]["standalone"] = {"calls": ["nonexistent"]}
        with self.assertRaisesRegex(ValueError, "unresolved"):
            overlap.audit(data)

    def test_duplicate_entrypoint_ids_fail_closed(self):
        data = graph()
        data["entrypoints"][1]["id"] = "full-gate"
        with self.assertRaisesRegex(ValueError, "duplicate"):
            overlap.audit(data)

    def test_cli_enforcement_refuses_undisposed_overlap(self):
        data = graph()
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "graph.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            process = subprocess.run(
                [sys.executable, str(SCRIPT), "--enforce", str(path)],
                check=False, capture_output=True, text=True,
            )
            self.assertEqual(process.returncode, 2)
            self.assertIn('"unresolved": 1', process.stdout)
            data["decisions"]["full-gate|standalone-repro"] = {
                "disposition": "VERIFY", "evidence": "bounded parity trial planned"}
            path.write_text(json.dumps(data), encoding="utf-8")
            process = subprocess.run(
                [sys.executable, str(SCRIPT), "--enforce", str(path)],
                check=False, capture_output=True, text=True,
            )
            self.assertEqual(process.returncode, 0)


if __name__ == "__main__":
    unittest.main()
