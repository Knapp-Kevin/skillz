#!/usr/bin/env python3
"""Offline, synthetic strategy-fit falsifiers. No consumer repository actions."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "ci_strategy_fit", ROOT.parent / "scripts" / "ci_strategy_fit.py"
)
ci = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ci)
FIXTURE = json.loads((ROOT / "ci-strategy-fit-fixture.json").read_text())


class StrategyFit(unittest.TestCase):
    def setUp(self):
        self.data = copy.deepcopy(FIXTURE)

    def find(self, report, identifier):
        return next(row for row in report["alternatives"] if row["id"] == identifier)

    def test_four_competing_options_are_compared_without_qualification(self):
        report = ci.evaluate(self.data)
        self.assertEqual(report["decision"], "OPTIONS_FOR_EXPERIMENT")
        self.assertEqual(report["qualification"], "NOT_QUALIFIED")
        self.assertEqual(report["savings_proof"], "NOT_MEASURED_BY_THIS_TOOL")
        self.assertEqual(report["ranking_for_experiment"], [
            "trusted-impact-graph", "test-internal-reuse", "stage-separation"])
        self.assertEqual(self.find(report, "existing-full")["disposition"], "HOLD")
        self.assertAlmostEqual(self.find(report, "trusted-impact-graph")["job_minutes_delta"], 360)

    def test_small_repository_keeps_simple_strategy_instead_of_graph(self):
        self.data["baseline"]["job_minutes"] = 30
        self.data["baseline"]["critical_path_minutes"] = 8
        full, stage, graph, internal = self.data["alternatives"]
        full["job_minutes"], full["critical_path_minutes"] = 30, 8
        stage["job_minutes"], stage["critical_path_minutes"] = 24, 6
        graph["job_minutes"], graph["critical_path_minutes"] = 23, 7
        graph["maintenance_hours"] = 80
        internal["job_minutes"], internal["critical_path_minutes"] = 25, 6
        self.data["objective"]["comparison_horizon_runs"] = 20
        report = ci.evaluate(self.data)
        self.assertEqual(report["ranking_for_experiment"], [
            "stage-separation", "test-internal-reuse"])
        self.assertIn("DEPENDENCY_COMPLEXITY_NOT_JUSTIFIED",
                      self.find(report, "trusted-impact-graph")["blockers"])

    def test_unmapped_transitive_dependencies_hold_cheap_graph(self):
        graph = self.data["alternatives"][2]
        graph["job_minutes"] = 1
        graph["transitive_dependencies_complete"] = False
        report = ci.evaluate(self.data)
        self.assertIn("TRANSITIVE_DEPENDENCIES_INCOMPLETE",
                      self.find(report, graph["id"])["blockers"])
        self.assertNotIn(graph["id"], report["ranking_for_experiment"])

    def test_stale_or_missing_receipts_cannot_qualify(self):
        self.data["alternatives"][2]["stale_and_missing_receipts_refused"] = False
        report = ci.evaluate(self.data)
        self.assertIn("FRESH_RECEIPT_GUARD_UNPROVEN",
                      self.find(report, "trusted-impact-graph")["blockers"])

    def test_spec_or_branch_protection_unknown_holds(self):
        self.data["alternatives"][2]["required_status_and_spec_compatible"] = None
        report = ci.evaluate(self.data)
        self.assertIn("REQUIRED_STATUS_OR_SPEC_UNMAPPED",
                      self.find(report, "trusted-impact-graph")["blockers"])

    def test_no_proven_disposition_does_not_auto_adopt_graph(self):
        for candidate in self.data["alternatives"]:
            candidate["detector_parity"] = None
        report = ci.evaluate(self.data)
        self.assertEqual(report["decision"], "HOLD")
        self.assertEqual(report["ranking_for_experiment"], [])

    def test_critical_path_regression_rejected_even_with_cost_savings(self):
        self.data["alternatives"][2]["critical_path_minutes"] = 90
        report = ci.evaluate(self.data)
        self.assertIn("CRITICAL_PATH_REGRESSION_EXCEEDS_POLICY",
                      self.find(report, "trusted-impact-graph")["blockers"])

    def test_unknown_benefit_does_not_become_measured(self):
        self.data["alternatives"][2]["evidence"] = "unknown"
        report = ci.evaluate(self.data)
        self.assertIn("COST_UNMEASURED",
                      self.find(report, "trusted-impact-graph")["blockers"])

    def test_positive_but_uneconomic_graph_not_recommended(self):
        graph = self.data["alternatives"][2]
        graph["job_minutes"] = 590
        graph["maintenance_hours"] = 900
        report = ci.evaluate(self.data)
        self.assertIn("DEPENDENCY_COMPLEXITY_NOT_JUSTIFIED",
                      self.find(report, "trusted-impact-graph")["blockers"])

    def test_duplicate_id_and_unsupported_kind_rejected(self):
        self.data["alternatives"][2]["id"] = self.data["alternatives"][1]["id"]
        with self.assertRaisesRegex(ValueError, "duplicate alternative"):
            ci.evaluate(self.data)
        self.data["alternatives"][2]["id"] = "graph"
        self.data["alternatives"][2]["kind"] = "magical-compressed-ci"
        with self.assertRaisesRegex(ValueError, "unrecognized strategy"):
            ci.evaluate(self.data)

    def test_invalid_boolean_value_rejected(self):
        self.data["alternatives"][2]["source_impact_complete"] = 1
        with self.assertRaisesRegex(ValueError, "true/false/null"):
            ci.evaluate(self.data)

    def test_cli_hold_exit_and_duplicate_json_keys(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp) / "fixture.json"
            for candidate in self.data["alternatives"]:
                candidate["detector_parity"] = False
            p.write_text(json.dumps(self.data))
            script = ROOT.parent / "scripts" / "ci_strategy_fit.py"
            result = subprocess.run([sys.executable, str(script), "--input", str(p)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(json.loads(result.stdout)["decision"], "HOLD")
            p.write_text('{"schema_version":1,"schema_version":1}')
            result = subprocess.run([sys.executable, str(script), "--input", str(p)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stdout)["decision"], "HOLD")


if __name__ == "__main__":
    unittest.main()
