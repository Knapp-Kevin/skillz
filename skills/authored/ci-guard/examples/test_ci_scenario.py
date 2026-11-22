"""Executable adversarial, offline normal-form CI architecture scenario tests."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location('ci_scenario',ROOT/'scripts'/'ci_scenario.py')
sim=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sim)
FIXTURE=ROOT/'examples'/'ci-scenario-fixture.json'

def case():
    return json.loads(FIXTURE.read_text(encoding='utf-8'))

def result_for(result,design,scenario):
    return next(x for x in result['results'] if x['design']==design and x['scenario']==scenario)

class ScenarioTests(unittest.TestCase):
    def run_doc(self,edit=None):
        d=case()
        if edit:edit(d)
        return sim.run(d)

    def test_two_designs_ten_scenarios_twenty_expected_outcomes(self):
        r=self.run_doc()
        self.assertEqual(r['status'],'STRUCTURAL_PASS',r['issues'])
        self.assertEqual(len(r['results']),20)
        self.assertTrue(all(x['matches_expected'] for x in r['results']))
        self.assertEqual(len(case()['designs'][0]['workflows']),8)
        self.assertFalse(r['real_provider_semantics_authenticated'])
        self.assertFalse(r['host_execution_proven'])

    def test_selective_producer_dependency_shortens_estimated_critical_path(self):
        r=self.run_doc()
        blanket=result_for(r,'blanket-barrier','ready-full')
        split=result_for(r,'split-independent','ready-full')
        self.assertEqual(blanket['estimated_runner_seconds'],split['estimated_runner_seconds'])
        self.assertGreater(blanket['estimated_critical_path_seconds'],
                           split['estimated_critical_path_seconds'])
        self.assertEqual(blanket['scheduled_start_seconds']['independent-full'],1800)
        self.assertEqual(split['scheduled_start_seconds']['independent'],0)
        self.assertEqual(split['scheduled_start_seconds']['dependent'],1800)
        self.assertEqual(r['observed_runner_savings'],'NOT_MEASURED')
        self.assertFalse(r['automatic_best_design_selected'])

    def test_draft_event_does_not_allocate_verifier_runners(self):
        r=self.run_doc()
        for d in ('blanket-barrier','split-independent'):
            x=result_for(r,d,'draft-full')
            self.assertEqual(x['scheduled_jobs'],[])
            self.assertFalse(x['actual_qualifies'])

    def test_ready_on_same_source_revision_recomputes_proof(self):
        r=self.run_doc()
        for d in ('blanket-barrier','split-independent'):
            self.assertTrue(result_for(r,d,'ready-full')['actual_qualifies'])
            self.assertFalse(result_for(r,d,'draft-full')['actual_qualifies'])
            self.assertFalse(result_for(r,d,'stale-ready-receipt')['actual_qualifies'])

    def test_intentionally_skipped_producer_keeps_lightweight_checks(self):
        r=self.run_doc()
        for d in ('blanket-barrier','split-independent'):
            x=result_for(r,d,'ready-light')
            self.assertTrue(x['actual_qualifies'])
            self.assertEqual(x['statuses']['producer'],'skipped')
            self.assertEqual(x['statuses']['lint'],'success')
            self.assertEqual(x['statuses']['independent' if d=='split-independent' else 'independent-light'],'success')

    def test_producer_failure_holds_full_qualification(self):
        r=self.run_doc()
        for d in ('blanket-barrier','split-independent'):
            x=result_for(r,d,'producer-failed')
            self.assertFalse(x['actual_qualifies'])
            self.assertEqual(x['statuses']['dependent'],'skipped')
            self.assertTrue(any('MISSING_OR_FAILED_OBLIGATION:proof-' in k for k in x['issues']))

    def test_one_failed_matrix_shard_cannot_be_smoothed_into_success(self):
        r=self.run_doc()
        for d in ('blanket-barrier','split-independent'):
            x=result_for(r,d,'proof-shard-failed')
            self.assertEqual(x['shard_states']['dependent']['a'],'success')
            self.assertEqual(x['shard_states']['dependent']['b'],'failure')
            self.assertIn('proof-b/generic/default',x['missing'])
            self.assertFalse(x['actual_qualifies'])

    def test_indirect_export_attempt_in_independent_lane_is_failure(self):
        r=self.run_doc()
        for d in ('blanket-barrier','split-independent'):
            x=result_for(r,d,'independent-api-violation')
            self.assertFalse(x['actual_qualifies'])
            self.assertTrue(any('INDEPENDENT_ARTIFACT_EXPORT_ATTEMPT' in k for k in x['issues']))

    def test_remove_independent_lane_runtime_guard_fails_source_review(self):
        def edit(doc):
            for d in doc['designs']:
                for job in d['jobs']:
                    if job['lane']=='independent':job['runtime_guard']=False
        r=self.run_doc(edit)
        self.assertEqual(r['status'],'HOLD')
        self.assertTrue(any('INDEPENDENT_LANE_GUARD_ABSENT' in k for k in r['issues']))

    def test_producer_dependency_missing_is_detected_even_when_job_runs(self):
        def edit(doc):
            for d in doc['designs']:
                for j in d['jobs']:
                    if j['id']=='dependent':j['needs']=[];j['conformance_needs']=[]
        r=self.run_doc(edit)
        self.assertEqual(r['status'],'HOLD')
        self.assertTrue(any('EXPECTED_SCENARIO_MISMATCH' in k for k in r['issues']))
        self.assertTrue(any('ARTIFACT_PRODUCER_NOT_IN_NEEDS' in i
                            for x in r['results'] for i in x['issues']))

    def test_deliberately_wrong_guard_disagrees_with_source_oracle(self):
        def edit(doc):doc['designs'][1]['jobs'][0]['condition']='always'
        r=self.run_doc(edit)
        self.assertEqual(r['status'],'HOLD')
        self.assertTrue(any('VALIDATOR_DRIFT' in x for x in r['issues']))

    def test_oracle_deleted_without_reference_is_not_proof(self):
        def edit(doc):doc['inventory']['conformance_tests_checked']=False
        self.assertIn('INVENTORY_INCOMPLETE:conformance_tests_checked',
                      self.run_doc(edit)['issues'])

    def test_policy_or_source_inventory_incomplete_holds(self):
        def edit(doc):doc['inventory']['complete']=False;doc['inventory']['unresolved']=['subworkflow not read']
        self.assertIn('UNRESOLVED_PATH_OR_ORACLE',self.run_doc(edit)['issues'])

    def test_wrong_revision_policy_receipt_holds(self):
        def edit(doc):doc['scenarios'][0]['status_checks']['lint/generic/default']['revision']='b'*40
        r=self.run_doc(edit)
        self.assertTrue(any('EXPECTED_SCENARIO_MISMATCH' in i for i in r['issues']))

    def test_draft_green_only_context_never_qualifies(self):
        def edit(doc):doc['scenarios'][0]['status_checks']['lint/generic/default']['kind']='DRAFT_DEFERRED_NOT_QUALIFIED'
        r=self.run_doc(edit)
        self.assertEqual(r['status'],'HOLD')
        self.assertIn('DRAFT_OR_NONVERIFIER_STATUS_REUSED:lint/generic/default',
                      result_for(r,'split-independent','ready-full')['issues'])

    def test_missing_required_status_cannot_qualify(self):
        def edit(doc):doc['scenarios'][0]['status_checks'].pop('native/native/security')
        r=self.run_doc(edit)
        self.assertIn('REQUIRED_STATUS_ABSENT:native/native/security',
                      result_for(r,'split-independent','ready-full')['issues'])

    def test_skipped_failed_cancelled_protected_statuses_fail(self):
        for state in ('skipped','failure','cancelled'):
            with self.subTest(state=state):
                def edit(doc):doc['scenarios'][0]['status_checks']['security/generic/high']['conclusion']=state
                self.assertIn('REQUIRED_STATUS_UNQUALIFIED:security/generic/high',
                   result_for(self.run_doc(edit),'split-independent','ready-full')['issues'])

    def test_success_claim_for_failed_verifier_is_spoofed(self):
        r=self.run_doc()
        x=result_for(r,'split-independent','proof-shard-failed')
        self.assertIn('REQUIRED_STATUS_SPOOFED:proof-b/generic/default',x['issues'])

    def test_duplicate_same_obligation_is_not_false_assurance(self):
        def edit(doc):
            for d in doc['designs']:
                j=copy.deepcopy(next(x for x in d['jobs'] if x['id']=='lint'))
                j['id']='duplicate-lint';d['jobs'].append(j)
        r=self.run_doc(edit)
        self.assertEqual(r['status'],'HOLD')
        self.assertTrue(any('DUPLICATE_UNIQUE_OBLIGATION' in k
                            for x in r['results'] for k in x['issues']))

    def test_distinct_platform_and_trust_is_not_false_duplicate(self):
        def edit(doc):
            for d in doc['designs']:
                j=copy.deepcopy(next(x for x in d['jobs'] if x['id']=='lint'))
                j.update(id='other-platform-lint',platform='windows',trust='other')
                d['jobs'].append(j)
                d['normative_obligations']['full'].append('lint/windows/other')
                d['normative_obligations']['light'].append('lint/windows/other')
            for s in doc['scenarios']:
                s['required_obligations'].append('lint/windows/other')
                s['status_checks']['lint/windows/other']={
                    'revision':doc['source_revision'],
                    'conclusion':'success','kind':'EXECUTED_VERIFIER'}
        r=self.run_doc(edit)
        self.assertEqual(r['status'],'STRUCTURAL_PASS',r['issues'])
        self.assertFalse(any(x['duplicate'] for x in r['results']))

    def test_matrix_expansion_unmapped_source_holds(self):
        def edit(doc):doc['designs'][0]['jobs'][2]['matrix_source']='unknown-plan'
        with self.assertRaisesRegex(sim.Invalid,'dynamic matrix source unmapped'):
            self.run_doc(edit)

    def test_matrix_source_revision_mismatch_refused(self):
        def edit(doc):doc['designs'][0]['jobs'][2]['matrix_source']='producer';doc['designs'][0]['jobs'][2]['matrix_revision']='b'*40
        with self.assertRaisesRegex(sim.Invalid,'revision stale'):
            self.run_doc(edit)

    def test_cross_workflow_needs_invalid_not_normalized_as_github_job_dependency(self):
        def edit(doc):
            for d in doc['designs']:
                x=next(j for j in d['jobs'] if j['id']=='lint')
                x['needs']=['producer'];x['conformance_needs']=['producer']
        with self.assertRaisesRegex(sim.Invalid,'cross-workflow needs'):
            self.run_doc(edit)

    def test_cycle_is_rejected_before_scheduling(self):
        def edit(doc):
            for d in doc['designs']:
                x=next(j for j in d['jobs'] if j['id']=='producer')
                x['needs']=['dependent'];x['conformance_needs']=['dependent']
        with self.assertRaisesRegex(sim.Invalid,'dependency cycle'):
            self.run_doc(edit)

    def test_unsupported_github_expression_holds(self):
        def edit(doc):doc['designs'][0]['jobs'][0]['condition']='github.event.pull_request.draft == false'
        with self.assertRaisesRegex(sim.Invalid,'unsupported job condition'):
            self.run_doc(edit)

    def test_unknown_github_trigger_token_rule_holds(self):
        def edit(doc):doc['designs'][0]['workflows'][6]['trigger_from']='forward';doc['designs'][0]['workflows'][6]['token_semantics']='UNKNOWN'
        r=self.run_doc(edit)
        self.assertEqual(r['status'],'HOLD')
        self.assertTrue(any('UNSUPPORTED_TRIGGER_CHAIN' in i for i in r['issues']))

    def test_release_tag_and_forward_side_effect_cannot_qualify_proof(self):
        r=self.run_doc()
        for d in ('blanket-barrier','split-independent'):
            for scenario in ('release-without-gate','postmerge-push'):
                x=result_for(r,d,scenario)
                self.assertFalse(x['actual_qualifies'])
                self.assertTrue(x['missing'])

    def test_live_metrics_and_provider_authentication_explicitly_unknown(self):
        r=self.run_doc()
        self.assertEqual(r['observed_critical_path_delta'],'NOT_MEASURED')
        self.assertEqual(r['observed_runner_savings'],'NOT_MEASURED')
        self.assertFalse(r['real_provider_semantics_authenticated'])
        self.assertFalse(r['automatic_best_design_selected'])

    def test_changed_source_revision_holds(self):
        def edit(doc):doc['scenarios'][0]['source_revision']='b'*40
        self.assertIn('SCENARIO_REVISION_STALE:ready-full',self.run_doc(edit)['issues'])

    def test_manifest_must_pin_complete_inventory_and_at_least_two_designs(self):
        def edit(doc):doc['designs'].pop()
        with self.assertRaisesRegex(sim.Invalid,'two to four'):
            self.run_doc(edit)

    def test_unknown_forced_result_job_refused(self):
        def edit(doc):doc['scenarios'][0]['forced_outcomes']['fake-shard']='success'
        with self.assertRaisesRegex(sim.Invalid,'not in candidate union'):
            self.run_doc(edit)

    def test_duplicate_json_keys_refused(self):
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'input.json';path.write_text('{"schema_version":1,"schema_version":1}')
            p=subprocess.run([sys.executable,str(ROOT/'scripts'/'ci_scenario.py'),
                             '--input',str(path)],capture_output=True,text=True)
            self.assertEqual(p.returncode,2)
            self.assertIn('duplicate JSON key',p.stderr)

    def test_cli_complete_offline_fixture_exit_and_no_writes(self):
        with tempfile.TemporaryDirectory() as td:
            src=Path(td)/'input.json';src.write_text(json.dumps(case()),encoding='utf8')
            before=set(Path(td).iterdir())
            p=subprocess.run([sys.executable,str(ROOT/'scripts'/'ci_scenario.py'),
                             '--input',str(src),'--require-pass'],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr)
            self.assertEqual(json.loads(p.stdout)['status'],'STRUCTURAL_PASS')
            self.assertEqual(before,set(Path(td).iterdir()))

    def test_cli_symlink_file_and_parent_refused(self):
        with tempfile.TemporaryDirectory() as td:
            folder=Path(td);real=folder/'actual';real.mkdir()
            original=real/'input.json';original.write_text(json.dumps(case()))
            alias=folder/'alias';alias.symlink_to(original)
            parent=folder/'linked';parent.symlink_to(real,target_is_directory=True)
            for path in (alias,parent/'input.json'):
                with self.subTest(path=path):
                    p=subprocess.run([sys.executable,str(ROOT/'scripts'/'ci_scenario.py'),
                                      '--input',str(path)],capture_output=True,text=True)
                    self.assertEqual(p.returncode,2)
                    self.assertIn('symlinked',p.stderr)

    def test_cli_oversized_manifest_refused(self):
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'large.json';path.write_bytes(b' '*(sim.MAX_BYTES+1))
            p=subprocess.run([sys.executable,str(ROOT/'scripts'/'ci_scenario.py'),
                             '--input',str(path)],capture_output=True,text=True)
            self.assertEqual(p.returncode,2)
            self.assertIn('too large',p.stderr)

    def test_ambiguous_github_style_path_glob_requires_normalization(self):
        def edit(doc):
            for d in doc['designs']:
                d['workflows'][0]['paths']=['src/*']
        with self.assertRaisesRegex(sim.Invalid,'UNSUPPORTED_SEMANTICS'):
            self.run_doc(edit)

    def test_qualifying_job_cannot_run_before_prerequisite_verifiers(self):
        def edit(doc):
            for d in doc['designs']:
                gate=next(j for j in d['jobs'] if j['id']=='gate-full')
                gate['needs']=[]
                gate['conformance_needs']=[]
        r=self.run_doc(edit)
        self.assertEqual(r['status'],'HOLD')
        self.assertTrue(any('QUALIFICATION_GATE_MISSING_PREREQUISITES' in i
                            for x in r['results'] for i in x['issues']))

if __name__=='__main__':unittest.main()
