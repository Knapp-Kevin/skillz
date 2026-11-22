"""Adversarial results-proof tests for CI Guard issue #867.

Entirely synthetic. Tests check proof boundaries, not consumer/provider savings.
"""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"scripts"))
spec=importlib.util.spec_from_file_location("ci_results_proof", ROOT/"scripts"/"ci_results_proof.py")
proof=importlib.util.module_from_spec(spec)
spec.loader.exec_module(proof)
import compare_ci_runs as strict


def receipt(run_id, billed, seconds, head="1"*40):
    return {
        "run_id":str(run_id),"attempt":1,"head":head,
        "scenario":"ready-ci","runner_profile":"ubuntu-24.04-x64",
        "cache_class":"cold","protected_status":"success",
        "jobs":[{"name":"required-gate","needs":[],"started_at":"2026-11-22T12:00:00Z",
                 "completed_at":f"2026-11-22T12:00:{seconds:02d}Z",
                 "billed_runner_minutes":billed,"result":"success"}]}


def case():
    return {
        "schema_version":1, "comparison_mode":"strict",
        "evidence":"OBSERVED_AS_SUPPLIED_NOT_AUTHENTICATED",
        "pairs":[{"baseline":receipt(1,10,50),"optimized":receipt(2,6,20)}],
        "assurance":{
            "expected_before":["lint/linux/default","native/windows/secure"],
            "executed_before":["lint/linux/default","native/windows/secure"],
            "expected_after":["lint/linux/default","native/windows/secure"],
            "executed_after":["lint/linux/default","native/windows/secure"],
            "contexts_before":["CI policy gate","release-signature"],
            "contexts_after":["CI policy gate","release-signature"],
            "seeded_fault_caught_before":True,"seeded_fault_caught_after":True,
            "release_guards_retained":True,"old_workflows_retired":True,"cutover_verified":True
        },
        "scope":{
            "event_before":"pull_request","event_after":"pull_request",
            "stage_before":"ready","stage_after":"ready",
            "os_before":"ubuntu","os_after":"ubuntu",
            "architecture_before":"x64","architecture_after":"x64",
            "matrix_before":2,"matrix_after":2,
            "toolchain_before":"python3.13","toolchain_after":"python3.13",
            "workload_equivalence":"same","confounders":[]
        },
        "source_refs":{
            "baseline_workflow":"baseline-workflow@sha","optimized_workflow":"candidate-workflow@sha",
            "baseline_tree":"1"*40,"optimized_tree":"2"*40,
            "receipt_refs":["synthetic-receipt-old","synthetic-receipt-new"]},
        "change":{
            "summary":"Deferred independent consumer until artifact was available",
            "waste_before":["billed dependency wait"],
            "retired_workflows":["unconditional-legacy"]
        }
    }


class ResultsProofTests(unittest.TestCase):
    def test_rp01_strict_matched_receipts_and_qualified_control_outputs(self):
        res=proof.report(case())
        self.assertEqual(res["comparison_eligibility"]["status"],"STRICT_AS_SUPPLIED")
        self.assertTrue(res["comparison_eligibility"]["strict_comparator_executed"])
        self.assertEqual(res["assurance_parity"]["verdict"],"QUALIFIED")
        self.assertTrue(res["assurance_parity"]["seeded_faults_both_detected"])
        self.assertEqual(res["metrics"]["summaries"]["billed_runner_minutes"]["saved"],4)
        self.assertEqual(res["metrics"]["summaries"]["billed_runner_minutes"]["saved_percent"],40)
        self.assertEqual(res["metrics"]["summaries"]["critical_path_seconds"]["saved"],30)
        self.assertEqual(res["metrics"]["summaries"]["executed_job_minutes"]["saved"],.5)
        self.assertEqual(res["decision"]["verdict"],"NOT_MEASURED")
        self.assertFalse(res["decision"]["provider_verified"])
        md=proof.render_markdown(res)
        self.assertIn("## Before",md)
        self.assertIn("## After",md)
        self.assertIn("**Provider-certified:** NO",md)
        self.assertIn("saved 4.0 billed-min (40.0%",md)

    def test_rp02_full_release_versus_narrow_pr_not_comparable(self):
        d=case()
        d["scope"].update(event_before="release",stage_before="release",
                          matrix_before=78)
        d["assurance"]["expected_before"].append("native/macos/release")
        res=proof.report(d)
        self.assertEqual(res["comparison_eligibility"]["status"],"NOT_COMPARABLE")
        self.assertEqual(res["decision"]["verdict"],"NOT_COMPARABLE")
        self.assertEqual(res["assurance_parity"]["verdict"],"NOT_QUALIFIED")

    def test_rp03_runner_savings_do_not_imply_latency(self):
        d=case()
        d["pairs"][0]["optimized"]=receipt(2,6,50)
        res=proof.report(d)
        self.assertEqual(res["metrics"]["summaries"]["billed_runner_minutes"]["saved_percent"],40)
        self.assertEqual(res["metrics"]["summaries"]["critical_path_seconds"]["saved"],0)
        self.assertEqual(res["metrics"]["summaries"]["qualification_elapsed_seconds"]["saved"],0)
        self.assertEqual(res["decision"]["indicated_effect"],"IMPROVEMENT_AS_SUPPLIED")

    def test_rp04_forecast_without_observed_pair_not_proved(self):
        d=case()
        d["pairs"]=[];d["comparison_mode"]="estimate";d["evidence"]="ESTIMATED"
        d["change"]["forecast_runner_savings_percent"]=20
        res=proof.report(d)
        self.assertEqual(res["decision"]["verdict"],"NOT_MEASURED")
        self.assertIsNone(res["metrics"]["summaries"]["billed_runner_minutes"]["saved"])
        self.assertEqual(res["metrics"]["estimated_runner_savings_percent"],20)
        self.assertNotIn("PROVED_IMPROVEMENT",json.dumps(res))

    def test_rp05_dropped_detector_or_legacy_trigger_is_not_qualified(self):
        for mutate in ("remove_detector","legacy_still_running","missing_fault"):
            with self.subTest(mutate=mutate):
                d=case()
                if mutate=="remove_detector":
                    d["assurance"]["executed_after"].remove("native/windows/secure")
                elif mutate=="legacy_still_running":
                    d["assurance"]["old_workflows_retired"]=False
                else:
                    d["assurance"]["seeded_fault_caught_after"]=False
                res=proof.report(d)
                self.assertEqual(res["assurance_parity"]["verdict"],"NOT_QUALIFIED")
                self.assertNotEqual(res["decision"]["verdict"],"PROVED_IMPROVEMENT")
                self.assertIn(res["decision"]["verdict"],("REGRESSION","NOT_CUT_OVER"))

    def test_rp06_source_drift_strict_refused_but_longitudinal_is_directional(self):
        d=case()
        d["pairs"][0]["optimized"]["head"]="2"*40
        strict_result=proof.report(d)
        self.assertEqual(strict_result["decision"]["verdict"],"NOT_COMPARABLE")
        self.assertFalse(strict_result["comparison_eligibility"]["strict_comparator_executed"])
        d["comparison_mode"]="longitudinal"
        result=proof.report(d)
        self.assertEqual(result["comparison_eligibility"]["status"],"DIRECTIONAL_ONLY")
        self.assertTrue(result["comparison_eligibility"]["source_mismatch"])
        self.assertEqual(result["decision"]["verdict"],"NOT_COMPARABLE")
        self.assertIn("causal claim"," ".join(result["limitations"]))

    def test_rp07_missing_provider_billing_does_not_fabricate_dollars(self):
        d=case()
        for pair in d["pairs"]:
            for phase in ("baseline","optimized"):
                pair[phase]["jobs"][0]["billed_runner_minutes"]=None
        res=proof.report(d)
        self.assertEqual(res["metrics"]["summaries"]["billed_runner_minutes"]["saved"],None)
        self.assertEqual(res["metrics"]["summaries"]["executed_job_minutes"]["saved"],.5)
        self.assertEqual(res["metrics"]["provider_cost"]["status"],"NOT_MEASURED_NO_AUTHENTICATED_PRICING")
        self.assertFalse(res["comparison_eligibility"]["strict_comparator_executed"])
        with self.assertRaises(strict.EvidenceError):
            strict.compare({"schema_version":1,"pairs":d["pairs"]})

    def test_rp08_lower_cost_with_longer_critical_path_is_regression(self):
        d=case()
        d["pairs"][0]["baseline"]=receipt(1,10,20)
        d["pairs"][0]["optimized"]=receipt(2,6,50)
        res=proof.report(d)
        self.assertEqual(res["metrics"]["summaries"]["billed_runner_minutes"]["saved_percent"],40)
        self.assertEqual(res["metrics"]["summaries"]["critical_path_seconds"]["saved"],-30)
        self.assertEqual(res["decision"]["verdict"],"REGRESSION")
        self.assertEqual(res["decision"]["indicated_effect"],"REGRESSION_OR_TRADEOFF")

    def test_no_cutover_even_if_scope_matched_and_cheap(self):
        d=case();d["assurance"]["cutover_verified"]=False
        self.assertEqual(proof.report(d)["decision"]["verdict"],"NOT_CUT_OVER")

    def test_repeated_samples_include_p50_p90_not_fake_single_sample_p90(self):
        d=case()
        for x in range(3,6):
            d["pairs"].append({"baseline":receipt(x*2,10,50),
                               "optimized":receipt(x*2+1,6,20)})
        v=proof.report(d)["metrics"]["summaries"]["critical_path_seconds"]
        self.assertEqual(v["sample_count"],4)
        self.assertEqual(v["baseline_p90"],50)

    def test_failed_required_job_never_becomes_savings_receipt(self):
        d=case();d["pairs"][0]["optimized"]["jobs"][0]["result"]="skipped"
        with self.assertRaises(strict.EvidenceError):
            proof.report(d)

    def test_bounded_schema_and_unverified_provider_claim(self):
        d=case();d["evidence"]="OBSERVED_PROVIDER"
        with self.assertRaises(strict.EvidenceError):
            proof.report(d)
        d=case();d["assurance"]["unexpected"]="silent"
        with self.assertRaises(strict.EvidenceError):
            proof.report(d)

    def test_output_cli_emits_linked_reports_without_overwrite(self):
        with tempfile.TemporaryDirectory() as td:
            base=Path(td);src=base/"input.json"
            src.write_text(json.dumps(case()),encoding="utf8")
            cmd=[sys.executable,str(ROOT/"scripts"/"ci_results_proof.py"),
                 "--input",str(src),"--output-dir",td]
            first=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(first.returncode,0,first.stderr)
            data=json.loads((base/"ci-results-proof.json").read_text(encoding="utf8"))
            md=(base/"CI-BEFORE-AFTER.md").read_text(encoding="utf8")
            self.assertEqual(data["decision"]["verdict"],"NOT_MEASURED")
            self.assertIn("## Integrity and limitations",md)
            second=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(second.returncode,2)
            self.assertIn("overwrite",second.stderr)

    def test_missing_billing_raw_job_minutes_preserve_strict_comparator_invariant(self):
        a=receipt(1,None,40)
        sums=strict.summarize_run(a,allow_missing_billing=True)
        self.assertIsNone(sums["billed_runner_minutes"])
        self.assertAlmostEqual(sums["executed_job_minutes"],.6667,places=4)
        with self.assertRaises(strict.EvidenceError):
            strict.summarize_run(a)

    def test_negative_nonfinite_runner_cost_rejected(self):
        for bad in (-1,float("inf"),float("nan")):
            with self.subTest(value=bad):
                d=case();d["pairs"][0]["baseline"]["jobs"][0]["billed_runner_minutes"]=bad
                with self.assertRaises(strict.EvidenceError):
                    proof.report(d)


if __name__=="__main__":
    unittest.main()
