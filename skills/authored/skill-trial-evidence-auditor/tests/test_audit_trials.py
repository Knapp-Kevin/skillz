"""Executed local method tests. All runs synthetic, not independent agent evaluations."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(HERE/'scripts'))
from audit_trials import audit,parse,Invalid,exact_sign_pvalue


def mk_arm(suffix, result, skill):
    return dict(run_id='run_'+suffix,host_id='host',model_id='model',agent_version='v1',
       config_sha='c'*40,snapshot_sha='e'*40,grader_sha='d'*40,
       result=result,verification_kind='DETERMINISTIC',verifier_independent=True,
       blind_to_arm=True,observed_execution=True,skill_triggered=skill,
       authority_violation=False,tokens=100,duration_ms=1000,receipt_sha=hashlib.sha256(suffix.encode()).hexdigest())


def mk_pair(i=0,b='FAIL',t='PASS',positive=True):
    return dict(pair_id='pair_'+str(i),case_id='case_'+str(i),should_trigger=positive,
        leakage_review='CLEAR',baseline=mk_arm('b'+str(i),b,False),
        treatment=mk_arm('t'+str(i),t,positive))


def mk(n=12):
    return dict(schema_version=1,skill=dict(id='fixture_skill',entrypoint_blob_sha='a'*40,package_tree_sha='b'*40),
        protocol=dict(id='protocol',run_kind='HOST_EXECUTED',preregistered=True,
        minimum_pairs=10,minimum_delta_pp=20,holdout_isolated=True),
        pairs=[mk_pair(i) for i in range(n)]+[mk_pair(n,'PASS','PASS',False)])

class MethodTests(unittest.TestCase):
    def test_positive_recorded_not_authenticated(self):
        x=audit(mk())
        self.assertEqual(x['determination'],'RECORDED_POSITIVE_SIGNAL_NOT_AUTHENTICATED')
        self.assertFalse(x['source_authenticity_verified'])
        self.assertFalse(x['actual_independent_host_validation_verified'])
        self.assertEqual(x['paired_improvements'],12)
        self.assertEqual(x['paired_regressions'],0)
        self.assertEqual(x['qualified_nontrigger_pairs'],1)
    def test_emulated_wont_claim_host(self):
        d=mk();d['protocol']['run_kind']='CONTROLLED_EMULATION';self.assertIn('WITHHELD',audit(d)['determination'])
    def test_pre_registration_required(self):
        d=mk();d['protocol']['preregistered']=False;self.assertIn('WITHHELD',audit(d)['determination'])
    def test_holdout_required(self):
        d=mk();d['protocol']['holdout_isolated']=False;self.assertIn('WITHHELD',audit(d)['determination'])
    def test_minimum_pairs(self):
        d=mk(4);self.assertIn('WITHHELD',audit(d)['determination'])
    def test_nontrigger_required(self):
        d=mk();d['pairs'].pop();self.assertIn('WITHHELD',audit(d)['determination'])
    def test_ratio_zero_baseline_not_infinity(self):
        self.assertIsNone(audit(mk())['relative_pass_ratio'])
    def test_no_uplift_not_positive(self):
        d=mk();
        for p in d['pairs'][:-1]:p['baseline']['result']='PASS'
        self.assertEqual(audit(d)['determination'],'NO_SIGNIFICANT_POSITIVE_SIGNAL')
    def test_cost_ledger_medians(self):
        x=audit(mk());self.assertEqual(x['median_baseline_tokens_if_reported'],100)
    def test_cost_incomplete_not_imputed(self):
        d=mk();d['pairs'][0]['treatment']['tokens']=None
        self.assertIsNone(audit(d)['median_treatment_tokens_if_reported'])
    def test_discordance_exact_pvalue(self):
        self.assertAlmostEqual(exact_sign_pvalue(12,0),0.00048828125)
        self.assertEqual(exact_sign_pvalue(0,0),1)
        self.assertEqual(exact_sign_pvalue(1,1),1)
    def test_incomparable_fields(self):
        for k in ['host_id','model_id','agent_version','config_sha','snapshot_sha','grader_sha']:
            with self.subTest(k=k):
                d=mk();d['pairs'][0]['treatment'][k]=('f'*40 if k in ('config_sha','snapshot_sha','grader_sha') else 'different')
                o=audit(d);self.assertIn('INCOMPARABLE_'+k.upper(),o['excluded_pairs'][0]['reasons'])
                self.assertIn('WITHHELD',o['determination'])
    def test_malformed_sources(self):
        for key,value in [('result','WIN'),('verification_kind','SECRET'),('tokens',True),('duration_ms',-1),('skill_triggered','yes'),('observed_execution','yes'),('blind_to_arm',None)]:
            with self.subTest(key=key):
                d=mk();d['pairs'][0]['baseline'][key]=value
                with self.assertRaises(Invalid):audit(d)
    def test_untrusted_extra_fields(self):
        d=mk();d['pairs'][0]['treatment']['hidden_tool_call']='run secrets'
        with self.assertRaises(Invalid):audit(d)
    def test_unknown_schema(self):
        d=mk();d['schema_version']=2
        with self.assertRaises(Invalid):audit(d)
    def test_boolean_schema_version(self):
        d=mk();d['schema_version']=True
        with self.assertRaises(Invalid):audit(d)
    def test_duplicate_pair_id(self):
        d=mk();d['pairs'][1]['pair_id']=d['pairs'][0]['pair_id']
        with self.assertRaises(Invalid):audit(d)
    def test_duplicate_run_id(self):
        d=mk();d['pairs'][1]['baseline']['run_id']=d['pairs'][0]['baseline']['run_id']
        with self.assertRaises(Invalid):audit(d)
    def test_duplicate_receipt(self):
        d=mk();d['pairs'][1]['baseline']['receipt_sha']=d['pairs'][0]['baseline']['receipt_sha']
        with self.assertRaises(Invalid):audit(d)
    def test_data_inconsistent_baseline(self):
        d=mk();d['pairs'][0]['baseline']['skill_triggered']=True
        self.assertIn('BASELINE_SKILL_TRIGGERED',audit(d)['excluded_pairs'][0]['reasons'])
    def test_positive_trigger_missing(self):
        d=mk();d['pairs'][0]['treatment']['skill_triggered']=None
        self.assertIn('SKILL_NOT_OBSERVED_TRIGGERED',audit(d)['excluded_pairs'][0]['reasons'])
    def test_nontrigger_fired(self):
        d=mk();d['pairs'][-1]['treatment']['skill_triggered']=True
        self.assertIn('NONTRIGGER_FIRED',audit(d)['excluded_pairs'][0]['reasons'])
    def test_leakage_review(self):
        for state in ['POSSIBLE','UNREVIEWED']:
            d=mk();d['pairs'][0]['leakage_review']=state
            self.assertIn('LEAKAGE_'+state,audit(d)['excluded_pairs'][0]['reasons'])
    def test_authority_violation(self):
        d=mk();d['pairs'][0]['treatment']['authority_violation']=True
        self.assertIn('AUTHORITY_VIOLATION',audit(d)['excluded_pairs'][0]['reasons'])
    def test_incomplete_arm(self):
        d=mk();d['pairs'][0]['baseline']['result']='INCOMPLETE'
        self.assertIn('INCOMPLETE_ARM',audit(d)['excluded_pairs'][0]['reasons'])
    def test_unobserved_execution(self):
        d=mk();d['pairs'][0]['treatment']['observed_execution']=False
        self.assertIn('EXECUTION_NOT_OBSERVED',audit(d)['excluded_pairs'][0]['reasons'])
    def test_judge_blind(self):
        d=mk();d['pairs'][0]['treatment']['verification_kind']='BLIND_JUDGE';d['pairs'][0]['treatment']['blind_to_arm']=False
        self.assertIn('JUDGE_NOT_BLINDED',audit(d)['excluded_pairs'][0]['reasons'])
    def test_independent_verifier(self):
        d=mk();d['pairs'][0]['treatment']['verifier_independent']=False
        self.assertIn('NO_INDEPENDENT_VERIFIER',audit(d)['excluded_pairs'][0]['reasons'])
    def test_repeated_cases_hold_statistical_claim(self):
        d=mk();d['pairs'][1]['case_id']=d['pairs'][0]['case_id']
        x=audit(d)
        self.assertIsNone(x['exact_two_sided_discordant_p'])
        self.assertIn('REPEATED_CASES_CORRELATED_UNCERTAINTY_WITHHELD',x['warnings'])
        self.assertIn('WITHHELD',x['determination'])
    def test_empty_pairs(self):
        d=mk();d['pairs']=[]
        with self.assertRaises(Invalid):audit(d)
    def test_too_many_pairs(self):
        d=mk();d['pairs']=[mk_pair(i) for i in range(2001)]
        with self.assertRaises(Invalid):audit(d)
    def test_duplicates_in_json_and_nans(self):
        with self.assertRaises(Invalid):parse('{"x":1,"x":2}')
        with self.assertRaises(Invalid):parse('{"x":NaN}')
    def test_reject_secrets_in_ids(self):
        for val in ['https://example.com','foo@bar','a?token=123','path/to/a','line\nheader']:
            d=mk();d['skill']['id']=val
            with self.assertRaises(Invalid):audit(d)
    def test_malformed_root(self):
        with self.assertRaises(Invalid):audit([])
    def test_nontrigger_task_regression_holds(self):
        d=mk();d['pairs'][-1]['treatment']['result']='FAIL'
        x=audit(d)
        self.assertTrue(x['nontrigger_task_regression'])
        self.assertIn('WITHHELD',x['determination'])
    def test_verifier_kind_differences_disqualify(self):
        d=mk();d['pairs'][0]['treatment']['verification_kind']='HUMAN'
        self.assertIn('INCOMPARABLE_VERIFICATION_KIND',audit(d)['excluded_pairs'][0]['reasons'])
    def test_unblinded_human_disqualified(self):
        d=mk();d['pairs'][0]['treatment']['verification_kind']='HUMAN'
        d['pairs'][0]['baseline']['verification_kind']='HUMAN'
        d['pairs'][0]['treatment']['blind_to_arm']=False
        self.assertIn('JUDGE_NOT_BLINDED',audit(d)['excluded_pairs'][0]['reasons'])
    def test_digest_validation(self):
        d=mk();d['skill']['entrypoint_blob_sha']='invalid'
        with self.assertRaises(Invalid):audit(d)
    def test_invalid_protocol_gate(self):
        d=mk();d['protocol']['minimum_pairs']=True
        with self.assertRaises(Invalid):audit(d)
    def test_unknown_baseline_activation_withholds_signal(self):
        d=mk();d['pairs'][0]['baseline']['skill_triggered']=None
        x=audit(d)
        self.assertIn('BASELINE_TRIGGER_UNKNOWN',x['excluded_pairs'][0]['reasons'])
        self.assertIn('WITHHELD',x['determination'])
    def test_unknown_negative_control_activation_withholds_signal(self):
        d=mk();d['pairs'][-1]['treatment']['skill_triggered']=None
        x=audit(d)
        self.assertIn('NONTRIGGER_ACTIVATION_UNKNOWN',x['excluded_pairs'][0]['reasons'])
        self.assertIn('WITHHELD',x['determination'])
    def test_malformed_enum_is_invalid_not_type_error(self):
        d=mk();d['pairs'][0]['baseline']['result']=[]
        with self.assertRaises(Invalid):audit(d)
    def test_cli_deep_json_and_private_path_errors_are_bounded(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'PRIVATE-CONFIDENTIAL-SOURCE.json'
            cmd=[sys.executable,str(HERE/'scripts'/'audit_trials.py'),'--input',str(p)]
            x=subprocess.run(cmd,capture_output=True,text=True,timeout=5)
            self.assertEqual(x.returncode,2)
            self.assertNotIn('PRIVATE-CONFIDENTIAL-SOURCE',x.stderr)
            p.write_text('['*2000+'0'+']'*2000,encoding='utf8')
            x=subprocess.run(cmd,capture_output=True,text=True,timeout=5)
            self.assertEqual(x.returncode,2)
            self.assertNotIn('Traceback',x.stderr)
    def test_cli_roundtrip(self):
        d=mk();d['protocol']['run_kind']='CONTROLLED_EMULATION'
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'input.json';p.write_text(json.dumps(d),encoding='utf8')
            x=subprocess.run([sys.executable,str(HERE/'scripts'/'audit_trials.py'),'--input',str(p)],capture_output=True,text=True)
            self.assertEqual(x.returncode,0,x.stderr)
            self.assertIn('WITHHELD',json.loads(x.stdout)['determination'])
    def test_cli_reject_duplicate_field_without_leak(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'input.json';p.write_text('{"pass@token":1,"pass@token":2}',encoding='utf8')
            x=subprocess.run([sys.executable,str(HERE/'scripts'/'audit_trials.py'),'--input',str(p)],capture_output=True,text=True)
            self.assertEqual(x.returncode,2)
            self.assertNotIn('token',x.stderr)
    def test_cli_reject_symlink(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'input.json';p.write_text(json.dumps(mk()),encoding='utf8');link=Path(td)/'linked.json'
            try:link.symlink_to(p)
            except (OSError,NotImplementedError):self.skipTest('symlink unsupported')
            x=subprocess.run([sys.executable,str(HERE/'scripts'/'audit_trials.py'),'--input',str(link)],capture_output=True,text=True)
            self.assertEqual(x.returncode,2)
    def test_cli_reject_directory(self):
        with tempfile.TemporaryDirectory() as td:
            x=subprocess.run([sys.executable,str(HERE/'scripts'/'audit_trials.py'),'--input',td],capture_output=True,text=True)
            self.assertEqual(x.returncode,2)
            self.assertIn('regular input',x.stderr)
    def test_cli_reject_oversize(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'input.json';p.write_bytes(b'a'*(1024*1024+1))
            x=subprocess.run([sys.executable,str(HERE/'scripts'/'audit_trials.py'),'--input',str(p)],capture_output=True,text=True)
            self.assertEqual(x.returncode,2)

if __name__=='__main__':unittest.main()
