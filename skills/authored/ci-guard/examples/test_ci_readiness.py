"""Fictional cross-component outcome-first readiness regression tests.

No third-party consumer data, host API calls or CI dispatches.
"""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import ci_readiness

SHA = "a" * 40


def fixture():
    # Assemble inputs from the existing first-party fictional diagnostics.
    repair = json.loads((ROOT / "examples" / "ci-self-repair-fixture.json").read_text())
    repair["revision"] = SHA
    for phase in repair["phases"]:
        phase["revision"] = SHA
    overlap = json.loads((ROOT / "examples" / "ci-overlap-fixture.json").read_text())
    for row in overlap["entrypoints"]:
        row["revision"] = SHA
        if row["id"] == "standalone":
            row["active"] = False  # Fictional planned retirement, not host proof.
    fit = json.loads((ROOT / "examples" / "ci-strategy-fit-fixture.json").read_text())
    fit["revision"] = SHA
    scenario = json.loads((ROOT / "examples" / "ci-scenario-fixture.json").read_text())
    return {
        "schema_version": 1,
        "source_revision": SHA,
        "selected_strategy": "trusted-impact-graph",
        "selected_scenario_design": "split-independent",
        "objective": {
            "primary": "runner_and_critical_path",
            "min_runner_savings_percent": 25,
            "min_critical_path_savings_percent": 15,
            "max_first_failure_regression_minutes": 0,
        },
        "first_failure": {"baseline_minutes": 55, "candidate_minutes": 32,
                          "evidence": "estimated"},
        "controls": {k: True for k in ci_readiness.CONTROLS},
        "self_repair": repair, "overlap_graph": overlap,
        "strategy_fit": fit, "scenario_manifest": scenario,
        "source_receipt": {
            "schema_version": 1, "status": "STATIC_SOURCE_RECONCILED",
            "design": "split-independent", "claimed_source_revision": SHA,
            "workflow_files": 3, "jobs": 12, "oracle_checks": 12,
            "source_git_head_authenticated": False,
            "compiled_oracle_execution_verified": False,
            "automatic_cutover_authorized": False,
        },
    }


class ReadinessContract(unittest.TestCase):
    def test_ready_is_only_bounded_advisory_not_cutover_authority(self):
        report = ci_readiness.evaluate(fixture())
        self.assertEqual(report["status"], "READY_FOR_ONE_QUALIFICATION", report["issues"])
        self.assertEqual(report["issues"], [])
        self.assertAlmostEqual(report["projected_runner_minutes_savings_percent"], 60)
        self.assertFalse(report["owner_authorization_granted"])
        self.assertFalse(report["protected_branch_rules_verified"])
        self.assertFalse(report["end_to_end_ci_qualified"])
        self.assertFalse(report["production_cutover_authorized"])
        self.assertEqual(report["observed_provider_billing"], "NOT_MEASURED")
        self.assertEqual(report["source_receipt_basis"], "SUPPLIED_STATIC_REPORT_NOT_AUTHENTICATED")

    def test_partial_scheduler_fix_fails_primary_economic_threshold(self):
        case = fixture()
        case["selected_strategy"] = "stage-separation"
        case["objective"]["min_runner_savings_percent"] = 30
        report = ci_readiness.evaluate(case)
        self.assertEqual(report["status"], "HOLD")
        self.assertIn("PRIMARY_RUNNER_SAVINGS_BELOW_THRESHOLD", report["issues"])

    def test_existing_duplicate_command_even_with_disposition_holds(self):
        case = fixture()
        case["overlap_graph"]["entrypoints"][1]["active"] = True
        case["overlap_graph"]["decisions"]["acceptance|standalone"] = {
            "disposition": "KEEP", "evidence": "owner still wants it"
        }
        result = ci_readiness.evaluate(case)
        self.assertEqual(result["status"], "HOLD")
        self.assertTrue(any(x.startswith("REPEATED_TERMINAL_STILL_ACTIVE")
                            for x in result["issues"]))

    def test_unresolved_duplicate_is_not_an_optional_phase_b(self):
        case = fixture()
        case["overlap_graph"]["entrypoints"][1]["active"] = True
        result = ci_readiness.evaluate(case)
        self.assertIn("OVERLAP_UNRESOLVED", result["issues"])

    def test_repeated_immutable_setup_not_mistaken_for_win(self):
        case = fixture()
        for name in ("first", "second"):
            case["self_repair"]["phases"].append({
                "test_id": name, "phase": "fixture", "environment": "linux",
                "revision": SHA, "p50_minutes": 20, "p90_minutes": 25,
                "evidence": "observed", "shared_key": "fictional-repeat",
                "immutable": True,
            })
        result = ci_readiness.evaluate(case)
        self.assertIn("SELF_REPAIR_NOT_READY", result["issues"])
        self.assertIn("SELF_REPAIR:IMMUTABLE_REUSE_NOT_YET_PROVEN", result["issues"])

    def test_unproven_test_internal_phase_inventory_holds(self):
        case = fixture()
        case["self_repair"]["phases"] = [x for x in
            case["self_repair"]["phases"] if x["phase"] != "test"]
        self.assertIn("SELF_REPAIR:TEST_INTERNAL_TIMING_MISSING",
                      ci_readiness.evaluate(case)["issues"])

    def test_missing_source_test_or_release_receipt_holds(self):
        for key in ("source_oracle_tests_executed", "seeded_negative_controls_executed",
                    "protected_statuses_and_release_paths_mapped",
                    "native_and_unique_detectors_preserved"):
            with self.subTest(key=key):
                case = fixture()
                case["controls"][key] = False
                self.assertIn("CONTROL_NOT_EVIDENCED:" + key,
                              ci_readiness.evaluate(case)["issues"])

    def test_owner_budget_or_rollback_missing_holds(self):
        for key in ("owner_approved_experiment_budget", "bounded_rollback_defined"):
            with self.subTest(key=key):
                case = fixture()
                case["controls"][key] = False
                self.assertEqual(ci_readiness.evaluate(case)["status"], "HOLD")

    def test_missing_old_workflow_retirement_holds(self):
        case = fixture()
        case["controls"]["old_workflow_retirement_verified"] = False
        self.assertIn("CONTROL_NOT_EVIDENCED:old_workflow_retirement_verified",
                      ci_readiness.evaluate(case)["issues"])

    def test_critical_path_not_hidden_by_runner_savings(self):
        case = fixture()
        case["objective"]["min_critical_path_savings_percent"] = 50
        self.assertIn("PRIMARY_CRITICAL_PATH_SAVINGS_BELOW_THRESHOLD",
                      ci_readiness.evaluate(case)["issues"])

    def test_first_failure_regression_is_a_blocker(self):
        case = fixture()
        case["first_failure"]["candidate_minutes"] = 60
        self.assertIn("FIRST_FAILURE_FEEDBACK_REGRESSION",
                      ci_readiness.evaluate(case)["issues"])

    def test_missing_two_viable_alternatives_holds(self):
        case = fixture()
        for x in case["strategy_fit"]["alternatives"]:
            if x["id"] in ("stage-separation", "test-internal-reuse"):
                x["detector_parity"] = False
        self.assertIn("INSUFFICIENT_ALTERNATIVE_COMPARISON",
                      ci_readiness.evaluate(case)["issues"])

    def test_mismatched_revision_between_canonical_modules_holds(self):
        for field in ("self_repair", "strategy_fit"):
            with self.subTest(field=field):
                case = fixture()
                case[field]["revision"] = "b" * 40
                if field == "self_repair":
                    for phase in case[field]["phases"]:
                        phase["revision"] = "b" * 40
                self.assertIn("SOURCE_REVISION_MISMATCH:" +
                              ("self-repair" if field == "self_repair" else "strategy"),
                              ci_readiness.evaluate(case)["issues"])

    def test_source_receipt_unknown_or_forged_authority_is_refused(self):
        case = fixture()
        case["source_receipt"]["status"] = "HOLD"
        self.assertIn("SOURCE_OR_ORACLE_RECEIPT_MISMATCH",
                      ci_readiness.evaluate(case)["issues"])
        case = fixture()
        case["source_receipt"]["automatic_cutover_authorized"] = True
        self.assertIn("FORGED_SOURCE_VERIFICATION_AUTHORITY",
                      ci_readiness.evaluate(case)["issues"])

    def test_no_negative_scenario_cannot_claim_readiness(self):
        case = fixture()
        # Simulated negative cases are required even when the main status passes.
        case["scenario_manifest"]["scenarios"] = [
            x for x in case["scenario_manifest"]["scenarios"]
            if x.get("expected_qualifies") is True
        ]
        report = ci_readiness.evaluate(case)
        self.assertEqual(report["status"], "HOLD")
        self.assertIn("ADVERSE_SCENARIO_MISSING", report["issues"])

    def test_repaired_baseline_not_observed_holds(self):
        case = fixture()
        case["strategy_fit"]["baseline"]["evidence"] = "estimated"
        self.assertIn("BASELINE_NOT_OBSERVED",
                      ci_readiness.evaluate(case)["issues"])

    def test_cli_acceptance_and_fail_closed_exit(self):
        case = fixture()
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "in.json"
            p.write_text(json.dumps(case))
            cmd = [sys.executable, str(ROOT / "scripts" / "ci_readiness.py"),
                   "--input", str(p), "--require-ready"]
            run = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            self.assertEqual(json.loads(run.stdout)["status"], "READY_FOR_ONE_QUALIFICATION")
            case["controls"]["source_oracle_tests_executed"] = False
            p.write_text(json.dumps(case))
            run = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(run.returncode, 3, run.stderr)
            self.assertEqual(json.loads(run.stdout)["status"], "HOLD")

    def test_duplicate_json_key_and_nonfinite_refused(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "bad.json"
            cmd = [sys.executable, str(ROOT / "scripts" / "ci_readiness.py"),
                   "--input", str(p), "--require-ready"]
            for raw in ('{"schema_version":1,"schema_version":1}', '{"bad":NaN}'):
                with self.subTest(raw=raw):
                    p.write_text(raw)
                    run = subprocess.run(cmd, capture_output=True, text=True)
                    self.assertEqual(run.returncode, 2)

    def test_no_untrusted_execution_or_network_required(self):
        # The fixture has no live URLs, tokens or source commands to execute.
        report = ci_readiness.evaluate(fixture())
        self.assertTrue(report["diagnostic_results_recomputed_from_declared_inputs"])
        self.assertFalse(report["owner_authorization_granted"])


if __name__ == "__main__":
    unittest.main()
