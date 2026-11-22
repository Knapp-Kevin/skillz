"""Executable negative controls for strict CI Guard post-cutover source-graph qualification.

All sources and receipts are invented. A structural PASS does not
authenticate any real workflow or prove actual runner-minute savings.
"""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
SCRIPT = HERE / "scripts" / "ci_overlap.py"
spec = importlib.util.spec_from_file_location("ci_overlap", SCRIPT)
overlap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(overlap)


def fixture():
    def entry(name, cohort, stage, recipe, event, *, expensive=True):
        return {"id": name, "cohort": cohort, "stage": stage, "event": event,
                "revision": "head-H", "environment": "linux-pinned",
                "trust_boundary": "read-only", "condition": "true",
                "matrix_expanded": True, "expensive": expensive,
                "invokes": [recipe]}
    nodes = {
        "acceptance": {"calls": ["model", "nested-task"]},
        "nested-task": {"calls": ["repro"]},
        "independent-task": {"calls": ["repro"]},
        "release-task": {"calls": ["repro", "sign"]},
        "model": {"command": "python -m qa.models",
                  "obligation": "model-validation", "inputs": "head-H"},
        "repro": {"command": "python -m qa.reproducibility",
                  "obligation": "reproducibility", "inputs": "head-H"},
        "sign": {"command": "python -m qa.signature_check",
                 "obligation": "release-signing", "inputs": "head-H"},
        "draft-gate": {"command": "python -m qa.defer",
                       "obligation": "draft-deferred", "inputs": "head-H"},
    }
    jobs = [
        entry("acceptance-job", "ready-H", "candidate", "acceptance", "pull_request"),
        entry("standalone-job", "ready-H", "candidate", "independent-task", "pull_request"),
        entry("release-job", "release-H", "release", "release-task", "release"),
        entry("draft-only-gate", "draft-H", "draft", "draft-gate",
              "pull_request", expensive=False),
    ]
    receipts = {
        "candidate": [{"obligation": o, "revision": "head-H", "result": "success"}
                      for o in ("model-validation", "reproducibility")],
        "release": [{"obligation": o, "revision": "head-H", "result": "success"}
                    for o in ("reproducibility", "release-signing")],
    }
    return {"nodes": nodes, "entrypoints": jobs, "decisions": {
        "acceptance-job|standalone-job": {
            "disposition": "VERIFY", "evidence": "source parity comparison pending"}},
        "post_cutover": {
            "inventory_complete": True, "source_revision": "head-H",
            "draft_status": "DRAFT_DEFERRED_NOT_QUALIFIED",
            "draft_qualified": False,
            "required": {
                "candidate": ["model-validation", "reproducibility"],
                "release": ["reproducibility", "release-signing"]},
            "receipts": receipts,
        }}


def consolidated():
    data = fixture()
    old = data["entrypoints"][1]
    old["active"] = False
    old["retirement_proof"] = {
        "revision": "head-H", "evidence": "disabled at observed revision head-H"}
    return data


class CutoverTests(unittest.TestCase):
    def assess(self, data):
        report = overlap.audit(data)
        state = overlap.qualify_cutover(data, report)
        self.assertIs(state["optimization_complete"], False)
        self.assertEqual(state["observed_runner_minutes_delta"], "NOT_MEASURED")
        self.assertEqual(state["observed_critical_path_delta"], "NOT_MEASURED")
        self.assertIs(state["host_authenticated"], False)
        return state

    def test_nested_composite_and_standalone_same_verifier_fails(self):
        data = fixture()
        report = overlap.audit(data)
        self.assertEqual(report["findings"][0]["normalized_class"], "PARTIAL_OVERLAP")
        paths = report["findings"][0]["invocation_paths"]
        self.assertTrue(any("acceptance -> nested-task -> repro" in p["path"]
                            for p in paths))
        self.assertTrue(any("standalone-job -> independent-task -> repro" in p["path"]
                            for p in paths))
        self.assertIn("REDUNDANT_ACTIVE_INVOCATION:acceptance-job|standalone-job",
                      self.assess(data)["issues"])

    def test_renamed_task_runner_alias_still_overlaps(self):
        data = fixture()
        data["nodes"]["independent-task"] = {"calls": ["alias-two"]}
        data["nodes"]["alias-two"] = {"calls": ["repro"]}
        self.assertEqual(overlap.audit(data)["findings"][0]["normalized_class"],
                         "PARTIAL_OVERLAP")
        self.assertEqual(self.assess(data)["status"], "FAIL")

    def test_declared_consolidation_not_equal_executed_consolidation(self):
        data = fixture()
        data["decisions"]["acceptance-job|standalone-job"] = {
            "disposition": "CONSOLIDATE", "evidence": "PR proposal"}
        self.assertEqual(self.assess(data)["status"], "FAIL")

    def test_old_workflow_removed_with_revision_bound_proof_passes_structure(self):
        data = consolidated()
        result = self.assess(data)
        self.assertEqual(result["status"], "PASS", result["issues"])
        self.assertFalse(overlap.audit(data)["findings"])

    def test_disabled_old_workflow_without_proof_fails(self):
        data = consolidated()
        data["entrypoints"][1].pop("retirement_proof")
        self.assertIn("DISABLED_PATH_UNVERIFIED:standalone-job",
                      self.assess(data)["issues"])

    def test_unique_release_signing_cannot_disappear(self):
        data = consolidated()
        data["entrypoints"][2]["invokes"] = ["independent-task"]
        self.assertIn("REQUIRED_TERMINAL_NOT_EXECUTED:release",
                      self.assess(data)["issues"])

    def test_policy_required_receipts_cannot_silently_shrink(self):
        data = consolidated()
        data["post_cutover"]["receipts"]["release"].pop()
        self.assertIn("REQUIRED_RECEIPT_SET_MISMATCH:release",
                      self.assess(data)["issues"])

    def test_skipped_or_stale_authoritative_receipt_fails(self):
        for state in ("skipped", "failed", "missing", "canceled"):
            data = consolidated()
            data["post_cutover"]["receipts"]["candidate"][0]["result"] = state
            self.assertEqual(self.assess(data)["status"], "FAIL", state)
        data = consolidated()
        data["post_cutover"]["receipts"]["release"][0]["revision"] = "older-H"
        self.assertIn("RECEIPT_FAILED_OR_STALE:release:reproducibility",
                      self.assess(data)["issues"])

    def test_draft_must_skip_expensive_and_not_qualify(self):
        data = consolidated()
        data["entrypoints"][-1]["expensive"] = True
        self.assertIn("DRAFT_EXPENSIVE_PATH:draft-only-gate",
                      self.assess(data)["issues"])
        data = consolidated()
        data["post_cutover"]["draft_qualified"] = True
        self.assertIn("DRAFT_FALSE_QUALIFICATION", self.assess(data)["issues"])

    def test_unexpanded_matrix_or_unknown_condition_blocks(self):
        data = consolidated()
        data["entrypoints"][0]["matrix_expanded"] = False
        self.assertIn("TRIGGER_OR_MATRIX_UNPROVEN:acceptance-job",
                      self.assess(data)["issues"])
        data = consolidated()
        data["entrypoints"][0]["condition"] = "UNKNOWN"
        self.assertEqual(self.assess(data)["status"], "FAIL")

    def test_incomplete_inventory_never_passes(self):
        data = consolidated()
        data["post_cutover"]["inventory_complete"] = False
        self.assertIn("INVENTORY_NOT_COMPLETE", self.assess(data)["issues"])

    def test_distinct_platform_proven_keep_and_no_unknown_equivalence(self):
        data = consolidated()
        data["entrypoints"][1]["active"] = True
        data["entrypoints"][1].pop("retirement_proof")
        data["entrypoints"][1]["environment"] = "windows-native"
        data["entrypoints"][1]["independence"] = {
            "reason": "native ABI", "evidence": "planted Windows-only failure"}
        data["decisions"]["acceptance-job|standalone-job"] = {
            "disposition": "KEEP", "evidence": "verified native ABI fault receipt"}
        self.assertEqual(self.assess(data)["status"], "PASS")
        data["entrypoints"][1].pop("independence")
        self.assertIn("EQUIVALENCE_NOT_PROVEN:acceptance-job|standalone-job",
                      self.assess(data)["issues"])

    def test_cutover_cli_rejects_missing_graph_and_accepts_structural_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "graph.json"
            p.write_text(json.dumps(fixture()))
            failed = subprocess.run(
                [sys.executable, str(SCRIPT), "--verify-cutover", str(p)],
                capture_output=True, text=True)
            self.assertEqual(failed.returncode, 3)
            self.assertEqual(json.loads(failed.stdout)["cutover"]["status"], "FAIL")
            p.write_text(json.dumps(consolidated()))
            okay = subprocess.run(
                [sys.executable, str(SCRIPT), "--verify-cutover", str(p)],
                capture_output=True, text=True)
            self.assertEqual(okay.returncode, 0, okay.stderr)
            self.assertEqual(json.loads(okay.stdout)["cutover"]["status"], "PASS")

    def test_shipped_anonymous_cli_fixtures(self):
        examples = HERE / "examples"
        before = json.loads((examples / "ci-overlap-fixture.json").read_text())
        after = json.loads((examples / "ci-cutover-fixture.json").read_text())
        self.assertEqual(overlap.audit(before)["findings"][0]["normalized_class"],
                         "PARTIAL_OVERLAP")
        self.assertEqual(self.assess(before)["status"], "FAIL")
        self.assertEqual(self.assess(after)["status"], "PASS")

    def test_duplicate_json_fields_and_symlink_input_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_file = root / "graph.json"
            input_file.write_text('{"nodes":{},"nodes":{}}')
            p = subprocess.run(
                [sys.executable, str(SCRIPT), "--verify-cutover", str(input_file)],
                capture_output=True, text=True)
            self.assertEqual(p.returncode, 2)
            self.assertIn("duplicate JSON key", p.stderr)
            input_file.write_text(json.dumps(consolidated()))
            link = root / "linked.json"
            link.symlink_to(input_file)
            p = subprocess.run(
                [sys.executable, str(SCRIPT), "--verify-cutover", str(link)],
                capture_output=True, text=True)
            self.assertEqual(p.returncode, 2)
            self.assertIn("linked graph path", p.stderr)


if __name__ == "__main__":
    unittest.main()
