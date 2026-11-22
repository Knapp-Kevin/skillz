"""Synthetic, repository-neutral adversarial tests for CI self-repair preflight."""
import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "ci_self_repair.py"
SPEC = importlib.util.spec_from_file_location("ci_self_repair", SCRIPT)
repair = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(repair)


def sample():
    return {
        "revision": "source-H",
        "inventory_complete": True,
        "workflows": [
            {"id": "old-expensive", "events": ["ready", "push"],
             "paths": ["*"], "matrix_jobs": 48, "matrix_expanded": True,
             "invocations_expanded": True, "active": False, "expensive": True},
            {"id": "cheap-draft", "events": ["draft"], "paths": ["*"],
             "matrix_jobs": 0, "matrix_expanded": True,
             "invocations_expanded": True, "active": True, "expensive": False},
            {"id": "ready-targeted", "events": ["ready"], "paths": ["src/*", "tests/*"],
             "matrix_jobs": 2, "matrix_expanded": True,
             "invocations_expanded": True, "active": True, "expensive": True},
            {"id": "ready-style", "events": ["ready"], "paths": ["*"],
             "matrix_jobs": 1, "matrix_expanded": True,
             "invocations_expanded": True, "active": True, "expensive": False},
        ],
        "repair_events": [
            {"id": "draft-format-edit", "stage": "draft", "changed_paths": ["tests/check.py"]},
            {"id": "final-ready", "stage": "ready", "changed_paths": ["tests/check.py"]},
        ],
        "budget": {"max_preparation_jobs": 4, "max_expensive_cycles": 1,
                   "planned_expensive_cycles": 1},
        "controls": {
            "nested_execution_inventory_complete": True,
            "artifact_wait_inventory_complete": True,
            "required_status_and_spec_mapped": True,
            "release_unique_detection_preserved": True,
            "source_tests_and_policy_ready": True,
            "rollback_defined": True,
            "cheap_checks_passed": True,
            "exact_head_freshness_plan": True,
            "owner_authorized_full_gate": False,
        },
        "artifact_waits": [],
        "phases": [
            {"test_id": "case-A", "phase": "compile", "environment": "linux",
             "revision": "source-H", "p50_minutes": 2, "p90_minutes": 3,
             "evidence": "observed"},
            {"test_id": "case-A", "phase": "test", "environment": "linux",
             "revision": "source-H", "p50_minutes": 25, "p90_minutes": 35,
             "evidence": "observed", "unique_detection": True},
            {"test_id": "case-B", "phase": "test", "environment": "linux",
             "revision": "source-H", "p50_minutes": 26, "p90_minutes": 37,
             "evidence": "observed", "unique_detection": True},
        ],
    }


def blocked_artifact_consumer(producer_outcome="success", **kwargs):
    record = {
        "consumer_job": "platform-test-A",
        "producer_job": "shared-data-build",
        "artifact_id": "same-run-artifact/source-H",
        "requested_at_utc": "2026-11-22T08:00:00Z",
        "arrived_at_utc": "2026-11-22T08:30:00Z",
        "completed_at_utc": "2026-11-22T08:30:07Z",
        "consumer_runner_allocated_during_wait": True,
        "same_run_custody": True,
        "producer_outcome": producer_outcome,
        "scheduling_remedy": "none",
        "runner_deferral_verified": False,
        "producer_failure_propagates": True,
        "producer_skipped_alternate_preserved": True,
        "evidence": "observed",
    }
    record.update(kwargs)
    return record


class SelfRepairAcceptance(unittest.TestCase):
    def assess(self, data=None):
        return repair.preflight(sample() if data is None else data)

    def test_coordinated_draft_remains_cheap_until_final_ready(self):
        result = self.assess()
        self.assertEqual(result["status"], "PREFLIGHT_READY", result["issues"])
        self.assertEqual([x["predicted_jobs"] for x in result["fanout_forecast"]], [0, 3])
        self.assertFalse(result["optimization_complete"])

    def test_one_line_format_fix_triggers_old_fanout_before_cutover(self):
        case = sample()
        case["workflows"][0]["active"] = True
        result = self.assess(case)
        self.assertEqual(result["fanout_forecast"][1]["predicted_jobs"], 51)
        self.assertIn("UNINTENDED_READY_FANOUT:final-ready", result["issues"])

    def test_old_unconditional_draft_workflow_fails_preparation(self):
        case = sample()
        case["workflows"][0]["active"] = True
        case["workflows"][0]["events"].append("draft")
        result = self.assess(case)
        self.assertIn("EXPENSIVE_DRAFT_FANOUT:draft-format-edit", result["issues"])
        self.assertIn("PREPARATION_FANOUT_OVER_BUDGET:draft-format-edit", result["issues"])

    def test_real_test_execution_dominates_short_compile(self):
        result = self.assess()
        self.assertEqual(result["dominant_observed_or_reported_phase"], "test")
        self.assertEqual(result["sum_individual_p50_minutes"]["test"], 51.0)
        self.assertEqual(result["sum_individual_p50_minutes"]["compile"], 2.0)

    def test_repeated_immutable_setup_is_candidate_not_claimed_saved(self):
        case = sample()
        for ident in ("case-A", "case-B"):
            case["phases"].append({
                "test_id": ident, "phase": "fixture",
                "environment": "linux", "revision": "source-H",
                "shared_key": "same-readonly-checkout", "immutable": True,
                "p50_minutes": 8, "p90_minutes": 9, "evidence": "observed",
            })
        result = self.assess(case)
        self.assertEqual(result["repeated_operations"][0]["class"],
                         "REPEATED_IMMUTABLE_SETUP")
        self.assertIn("IMMUTABLE_REUSE_NOT_YET_PROVEN", result["issues"])
        self.assertIs(result["repeated_operations"][0]["reuse_authorized"], False)

    def test_mutated_or_fresh_directory_setup_keeps_isolation(self):
        case = sample()
        for ident, extra in (("A", {"mutates_fixture": True}),
                             ("B", {"fresh_directory_required": True})):
            case["phases"].append({
                "test_id": ident, "phase": "fixture",
                "environment": "linux", "revision": "source-H",
                "shared_key": "similar-setup", "immutable": True,
                "p50_minutes": 6, "p90_minutes": 8,
                "evidence": "observed", **extra,
            })
        result = self.assess(case)
        self.assertEqual(result["repeated_operations"][0]["class"],
                         "JUSTIFIED_ISOLATION")
        self.assertEqual(result["status"], "PREFLIGHT_READY")

    def test_unique_detection_blocks_false_claim_of_redundancy(self):
        case = sample()
        for ident in ("A", "B"):
            case["phases"].append({
                "test_id": ident, "phase": "oracle", "environment": "linux",
                "revision": "source-H", "shared_key": "same-loop-name",
                "unique_detection": True, "p50_minutes": 10,
                "p90_minutes": 11, "evidence": "observed",
            })
        self.assertEqual(self.assess(case)["repeated_operations"][0]["class"],
                         "UNIQUE_DETECTION")

    def test_multiple_expensive_ready_cycles_fail(self):
        case = sample()
        case["repair_events"].append({
            "id": "another-ready", "stage": "ready",
            "changed_paths": ["tests/check.py"]})
        result = self.assess(case)
        self.assertIn("FORECAST_QUALIFICATION_CYCLES_OVER_BUDGET",
                      result["issues"])

    def test_required_policy_or_release_detection_not_silently_dropped(self):
        case = sample()
        case["controls"]["required_status_and_spec_mapped"] = False
        case["controls"]["release_unique_detection_preserved"] = False
        result = self.assess(case)
        self.assertIn("REQUIRED_STATUS_OR_SPEC_UNMAPPED", result["issues"])
        self.assertIn("RELEASE_OR_NATIVE_PARITY_UNPROVEN", result["issues"])

    def test_draft_defer_is_not_exact_head_qualification(self):
        case = sample()
        case["controls"]["exact_head_freshness_plan"] = False
        case["controls"]["cheap_checks_passed"] = False
        result = self.assess(case)
        self.assertIn("EXACT_HEAD_ACCEPTANCE_NOT_PLANNED", result["issues"])
        self.assertIn("CHEAP_CHECKS_NOT_GREEN", result["issues"])

    def test_policy_edit_requires_complete_plan_and_matrix(self):
        case = sample()
        case["workflows"][2]["matrix_expanded"] = False
        case["controls"]["source_tests_and_policy_ready"] = False
        result = self.assess(case)
        self.assertIn("MATRIX_UNEXPANDED:ready-targeted", result["issues"])
        self.assertIn("COORDINATED_CHANGESET_NOT_READY", result["issues"])

    def test_fewer_jobs_does_not_claim_lower_critical_path(self):
        result = self.assess()
        self.assertEqual(result["observed_runner_minutes_delta"], "NOT_MEASURED")
        self.assertEqual(result["observed_critical_path_delta"], "NOT_MEASURED")
        self.assertFalse(result["provider_receipts_authenticated"])
        self.assertTrue(result["reported_p50_is_additive_not_critical_path"])
        self.assertTrue(result["p50_p90_sums_are_not_cohort_percentiles"])


    def test_bundled_artifact_wait_fixture_is_a_negative_control(self):
        path = ROOT / "examples" / "ci-artifact-wait-fixture.json"
        case = json.loads(path.read_text(encoding="utf-8"))
        result = self.assess(case)
        self.assertEqual(result["status"], "HOLD")
        self.assertEqual(result["dominant_explained_cause"],
                         "ARTIFACT_DEPENDENCY_WAIT")
        self.assertEqual(len(result["artifact_wait_analysis"]), 2)
        self.assertEqual(result["sum_reported_paid_dependency_wait_minutes"],
                         60.0)

    def test_shared_artifact_wait_is_not_algorithms_or_compilation(self):
        case = sample()
        case["artifact_waits"] = [
            blocked_artifact_consumer(),
            blocked_artifact_consumer(consumer_job="platform-test-B",
                                     completed_at_utc="2026-11-22T08:30:09Z")]
        result = self.assess(case)
        self.assertEqual(result["dominant_explained_cause"], "ARTIFACT_DEPENDENCY_WAIT")
        self.assertEqual(result["sum_reported_paid_dependency_wait_minutes"], 60)
        self.assertEqual([x["classification"] for x in result["artifact_wait_analysis"]],
                         ["DEPENDENCY_WAIT_ON_PAID_RUNNER"] * 2)
        self.assertIn("PAID_ARTIFACT_WAIT_REQUIRES_SAFE_JOB_DEPENDENCY:platform-test-A",
                      result["issues"])
        self.assertTrue(result["artifact_wait_can_overlap_test_duration"])
        self.assertEqual(result["observed_runner_minutes_delta"], "NOT_MEASURED")

    def test_declared_job_dependency_preserves_existing_proof_boundaries(self):
        case = sample()
        case["artifact_waits"] = [
            blocked_artifact_consumer(scheduling_remedy="producer-job-dependency",
                runner_deferral_verified=True,
                producer_failure_propagates=True,
                producer_skipped_alternate_preserved=True)]
        result = self.assess(case)
        self.assertEqual(result["status"], "PREFLIGHT_READY", result["issues"])
        self.assertFalse(result["artifact_wait_analysis"][0]
                         ["skip_path_and_failure_parity_proven_by_host"])
        self.assertFalse(result["provider_receipts_authenticated"])

    def test_producer_skipped_path_must_not_be_skipped_by_needs(self):
        case = sample()
        case["artifact_waits"] = [
            blocked_artifact_consumer(producer_outcome="skipped",
                scheduling_remedy="producer-job-dependency",
                runner_deferral_verified=True,
                producer_skipped_alternate_preserved=False)]
        result = self.assess(case)
        self.assertIn("PRODUCER_SKIPPED_PATH_BROKEN:platform-test-A",
                      result["issues"])
        self.assertEqual(result["status"], "HOLD")

    def test_producer_failure_propagates_cannot_be_bypassed(self):
        case = sample()
        case["artifact_waits"] = [
            blocked_artifact_consumer(producer_outcome="failure",
                scheduling_remedy="producer-job-dependency",
                runner_deferral_verified=True,
                producer_failure_propagates=False)]
        result = self.assess(case)
        self.assertIn("PRODUCER_FAILURE_NOT_PROPAGATED:platform-test-A",
                      result["issues"])

    def test_cross_run_artifact_not_treated_as_safe_dependency(self):
        case = sample()
        case["artifact_waits"] = [
            blocked_artifact_consumer(scheduling_remedy="producer-job-dependency",
                runner_deferral_verified=True, same_run_custody=False)]
        result = self.assess(case)
        self.assertIn("ARTIFACT_CUSTODY_NOT_PROVEN:platform-test-A",
                      result["issues"])

    def test_unverified_artifact_inventory_is_fail_closed(self):
        case = sample()
        case["controls"]["artifact_wait_inventory_complete"] = False
        self.assertIn("ARTIFACT_WAIT_INVENTORY_INCOMPLETE", self.assess(case)["issues"])

    def test_timing_out_of_order_is_rejected_not_negative_wait(self):
        case = sample()
        case["artifact_waits"] = [
            blocked_artifact_consumer(arrived_at_utc="2026-11-22T07:59:00Z")]
        with self.assertRaisesRegex(ValueError, "impossible artifact timestamp"):
            self.assess(case)

    def test_unobserved_wait_does_not_claim_verified_runtime(self):
        case = sample()
        case["artifact_waits"] = [blocked_artifact_consumer(evidence="estimated")]
        result = self.assess(case)
        self.assertIn("ARTIFACT_WAIT_TIMING_NOT_OBSERVED:platform-test-A",
                      result["issues"])
        self.assertEqual(result["observed_critical_path_delta"], "NOT_MEASURED")

    def test_cli_exit_code_and_read_only_filesystem(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            inp = root / "graph.json"
            inp.write_text(json.dumps(sample()), encoding="utf-8")
            before = list(root.iterdir())
            p = subprocess.run([sys.executable, "-B", str(SCRIPT),
                                "--input", str(inp), "--require-ready"],
                               text=True, capture_output=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertEqual(before, list(root.iterdir()))
            bad = sample()
            bad["inventory_complete"] = False
            inp.write_text(json.dumps(bad), encoding="utf-8")
            p = subprocess.run([sys.executable, "-B", str(SCRIPT),
                                "--input", str(inp), "--require-ready"],
                               text=True, capture_output=True)
            self.assertEqual(p.returncode, 3)
            self.assertEqual(json.loads(p.stdout)["status"], "HOLD")

    def test_invalid_duplicate_json_and_symlink_refused(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            inp = root / "bad.json"
            inp.write_text('{"revision":"A","revision":"B"}', encoding="utf-8")
            p = subprocess.run([sys.executable, "-B", str(SCRIPT),
                                "--input", str(inp)], text=True, capture_output=True)
            self.assertEqual(p.returncode, 2)
            self.assertIn("duplicate JSON", p.stderr)
            alias = root / "linked.json"
            alias.symlink_to(inp)
            p = subprocess.run([sys.executable, "-B", str(SCRIPT),
                                "--input", str(alias)], text=True, capture_output=True)
            self.assertEqual(p.returncode, 2)
            self.assertIn("linked input", p.stderr)


if __name__ == "__main__":
    unittest.main()
