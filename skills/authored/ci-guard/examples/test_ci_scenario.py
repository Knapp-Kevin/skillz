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

def add_dispatch_chain(doc):
    """Expand each fictional graph with an explicit, source-bound dispatch hop."""
    for design in doc['designs']:
        source=next(j for j in design['jobs'] if j['id']=='forward')
        source['dispatch_target']='forward-relay'
        source['emitted_event']='dispatch'
        design['workflows'].append({
            'id':'forward-relay','events':['dispatch'],'paths':['**'],
            'trigger_from':'forward','token_semantics':'EXTERNAL_DISPATCH_DECLARED'})
        design['jobs'].insert(0,{
            'id':'forward-relay-job','workflow':'forward-relay','needs':[],
            'condition':'success','conformance_condition':'success',
            'conformance_needs':[],'routes':['full'],'eligible_events':['dispatch'],
            'role':'other','lane':'other','seconds':2,'matrix':['default'],
            'side_effect':'forward-relay-reconciled','effect_kind':'forward'})
        design['normative_side_effects']['push'].append('forward-relay-reconciled')
    next(s for s in doc['scenarios'] if s['id']=='postmerge-push'
         )['required_side_effects'].append('forward-relay-reconciled')

class ScenarioTests(unittest.TestCase):
    def run_doc(self,edit=None):
        d=case()
        if edit:edit(d)
        return sim.run(d)

    def test_two_designs_eleven_scenarios_twenty_two_expected_outcomes(self):
        r=self.run_doc()
        self.assertEqual(r['status'],'STRUCTURAL_PASS',r['issues'])
        self.assertEqual(len(r['results']),22)
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
        def edit(doc):
            add_dispatch_chain(doc)
            doc['designs'][0]['workflows'][-1]['token_semantics']='GITHUB_TOKEN_PUSH'
        r=self.run_doc(edit)
        self.assertEqual(r['status'],'HOLD')
        self.assertTrue(any('UNSUPPORTED_TRIGGER_CHAIN' in i for i in r['issues']))
        self.assertNotIn('forward-relay-job',result_for(r,'blanket-barrier','postmerge-push')['scheduled_jobs'])

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


    def test_push_release_dispatch_effects_independent_of_pr_gate(self):
        result=self.run_doc()
        for design in ('blanket-barrier','split-independent'):
            for scenario,effect in (('postmerge-push','forward-port'),
                                    ('release-without-gate','tag-validation'),
                                    ('dispatch-regeneration','regenerate-assets')):
                with self.subTest(design=design,scenario=scenario):
                    row=result_for(result,design,scenario)
                    self.assertFalse(row['actual_qualifies'])
                    self.assertEqual(row['required_side_effects'],[effect])
                    self.assertEqual(row['executed_side_effects'][effect],['success'])
                    self.assertFalse(any('SIDE_EFFECT' in issue for issue in row['issues']))

    def test_missing_forward_effect_holds_even_when_gate_intentionally_false(self):
        def edit(doc):
            for design in doc['designs']:
                next(j for j in design['jobs'] if j['id']=='forward')['routes']=['light']
        result=self.run_doc(edit)
        self.assertEqual(result['status'],'HOLD')
        for design in ('blanket-barrier','split-independent'):
            self.assertIn('MISSING_OR_FAILED_SIDE_EFFECT:forward-port',
                          result_for(result,design,'postmerge-push')['issues'])

    def test_duplicate_tag_effect_is_not_extra_assurance(self):
        def edit(doc):
            for design in doc['designs']:
                duplicate=copy.deepcopy(next(j for j in design['jobs'] if j['id']=='tag'))
                duplicate['id']='tag-copy'
                design['jobs'].append(duplicate)
        result=self.run_doc(edit)
        self.assertEqual(result['status'],'HOLD')
        self.assertIn('DUPLICATE_SIDE_EFFECT:tag-validation',
                      result_for(result,'split-independent','release-without-gate')['issues'])

    def test_unexpected_effect_requires_policy_approval(self):
        def edit(doc):
            for design in doc['designs']:
                next(j for j in design['jobs'] if j['id']=='forward')['side_effect']='unexpected-forward'
        result=self.run_doc(edit)
        self.assertEqual(result['status'],'HOLD')
        row=result_for(result,'split-independent','postmerge-push')
        self.assertIn('UNEXPECTED_SIDE_EFFECT:unexpected-forward',row['issues'])
        self.assertIn('MISSING_OR_FAILED_SIDE_EFFECT:forward-port',row['issues'])

    def test_failed_effect_does_not_count_as_done(self):
        def edit(doc):
            next(s for s in doc['scenarios'] if s['id']=='release-without-gate')['forced_outcomes']['tag']='failure'
        result=self.run_doc(edit)
        self.assertEqual(result['status'],'HOLD')
        self.assertIn('MISSING_OR_FAILED_SIDE_EFFECT:tag-validation',
                      result_for(result,'split-independent','release-without-gate')['issues'])

    def test_normative_effects_cannot_be_edited_away_with_candidate(self):
        def edit(doc):
            for design in doc['designs']:design['normative_side_effects']['push']=[]
        result=self.run_doc(edit)
        self.assertEqual(result['status'],'HOLD')
        self.assertIn('NORMATIVE_SIDE_EFFECTS_DRIFT',
                      result_for(result,'split-independent','postmerge-push')['issues'])

    def test_missing_scenario_side_effect_inventory_is_invalid(self):
        def edit(doc):doc['scenarios'][0].pop('required_side_effects')
        with self.assertRaisesRegex(sim.Invalid,'missing required fields'):
            self.run_doc(edit)

    def test_other_job_requires_explicit_effect_kind(self):
        def edit(doc):
            for design in doc['designs']:
                next(j for j in design['jobs'] if j['id']=='forward').pop('effect_kind')
        with self.assertRaisesRegex(sim.Invalid,'explicit effect_kind'):
            self.run_doc(edit)


    def test_declared_event_chain_runs_only_after_successful_emitter(self):
        result=self.run_doc(add_dispatch_chain)
        self.assertEqual(result['status'],'STRUCTURAL_PASS',result['issues'])
        for design in ('blanket-barrier','split-independent'):
            x=result_for(result,design,'postmerge-push')
            self.assertEqual(x['statuses']['forward'],'success')
            self.assertEqual(x['statuses']['forward-relay-job'],'success')
            self.assertIn('forward-relay',x['activated_workflows'])
            self.assertEqual(x['scheduled_start_seconds']['forward-relay-job'],4)
            self.assertEqual(x['modeled_dispatch_edges'],[
                {'from_job':'forward','to_workflow':'forward-relay',
                 'event':'dispatch','provider_authenticated':False}])
            self.assertEqual(x['executed_side_effects']['forward-relay-reconciled'],['success'])
        self.assertFalse(result['event_chains_provider_authenticated'])

    def test_failed_emitter_does_not_allocate_downstream_runner(self):
        def edit(doc):
            add_dispatch_chain(doc)
            next(s for s in doc['scenarios'] if s['id']=='postmerge-push')['forced_outcomes']['forward']='failure'
        result=self.run_doc(edit)
        self.assertEqual(result['status'],'HOLD')
        x=result_for(result,'split-independent','postmerge-push')
        self.assertEqual(x['statuses']['forward-relay-job'],'skipped')
        self.assertNotIn('forward-relay-job',x['scheduled_jobs'])
        self.assertNotIn('forward-relay',x['activated_workflows'])
        self.assertIn('MISSING_OR_FAILED_SIDE_EFFECT:forward-relay-reconciled',x['issues'])

    def test_direct_dispatch_does_not_forge_an_emitted_workflow(self):
        result=self.run_doc(add_dispatch_chain)
        for design in ('blanket-barrier','split-independent'):
            x=result_for(result,design,'dispatch-regeneration')
            self.assertEqual(x['statuses']['forward'],'skipped')
            self.assertEqual(x['statuses']['forward-relay-job'],'skipped')
            self.assertNotIn('forward-relay',x['activated_workflows'])
            self.assertEqual(x['statuses']['regenerate'],'success')

    def test_missing_dispatch_target_refused(self):
        def edit(doc):
            add_dispatch_chain(doc)
            next(j for j in doc['designs'][0]['jobs'] if j['id']=='forward').pop('dispatch_target')
        with self.assertRaisesRegex(sim.Invalid,'explicit dispatch'):
            self.run_doc(edit)

    def test_orphaned_dispatch_target_refused(self):
        def edit(doc):
            add_dispatch_chain(doc)
            # Preserve the receiver and its job; orphan only the event edge.
            receiver=doc['designs'][0]['workflows'][-1]
            receiver.pop('trigger_from')
            receiver.pop('token_semantics')
        with self.assertRaisesRegex(sim.Invalid,'unmapped or contradictory dispatch target'):
            self.run_doc(edit)

    def test_bad_emitter_identity_refused(self):
        def edit(doc):
            add_dispatch_chain(doc)
            doc['designs'][0]['workflows'][-1]['trigger_from']='not-a-job'
        with self.assertRaisesRegex(sim.Invalid,'unmapped event emitter'):
            self.run_doc(edit)

    def test_cross_workflow_needs_remains_forbidden_with_dispatch_edge(self):
        def edit(doc):
            add_dispatch_chain(doc)
            j=next(j for j in doc['designs'][0]['jobs'] if j['id']=='forward-relay-job')
            j['needs']=['forward'];j['conformance_needs']=['forward']
        with self.assertRaisesRegex(sim.Invalid,'cross-workflow needs'):
            self.run_doc(edit)

    def test_emitter_must_be_non_verifier_job(self):
        def edit(doc):
            add_dispatch_chain(doc)
            next(j for j in doc['designs'][0]['jobs'] if j['id']=='forward')['role']='verify'
        with self.assertRaises(sim.Invalid):
            self.run_doc(edit)

    def test_predecessor_cancellation_does_not_trigger_dispatch(self):
        def edit(doc):
            add_dispatch_chain(doc)
            next(s for s in doc['scenarios'] if s['id']=='postmerge-push')['forced_outcomes']['forward']='cancelled'
        result=self.run_doc(edit)
        self.assertEqual(result['status'],'HOLD')
        x=result_for(result,'split-independent','postmerge-push')
        self.assertEqual(x['statuses']['forward-relay-job'],'skipped')
        self.assertNotIn('forward-relay-job',x['scheduled_jobs'])

    def test_normalized_dispatch_requires_explicit_supported_event(self):
        def edit(doc):
            add_dispatch_chain(doc)
            doc['designs'][0]['workflows'][-1]['events']=['push','dispatch']
        with self.assertRaisesRegex(sim.Invalid,'only supports dispatch'):
            self.run_doc(edit)

if __name__=='__main__':unittest.main()
