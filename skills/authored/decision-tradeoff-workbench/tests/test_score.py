"""Deterministic, dependency-free score verification; run with python -m unittest discover."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('score', ROOT / 'scripts' / 'score.py')
score = importlib.util.module_from_spec(spec)
spec.loader.exec_module(score)


def fixture():
    return {
        'schema_version': 1, 'weights_approved': True, 'score_max': 3,
        'criteria': [
            {'id':'security','weight':5,'hard_gate_min':3},
            {'id':'cost','weight':3},
            {'id':'integration','weight':2},
        ],
        'alternatives': [
            {'id':'A','cells':{'security':{'score':3,'status':'OWNER_SUPPLIED','source':'synthetic test'},'cost':{'score':1,'status':'OWNER_SUPPLIED','source':'synthetic test'},'integration':{'score':2,'status':'OWNER_SUPPLIED','source':'synthetic test'}}},
            {'id':'B','cells':{'security':{'score':2,'status':'OWNER_SUPPLIED','source':'synthetic test'},'cost':{'score':3,'status':'OWNER_SUPPLIED','source':'synthetic test'},'integration':{'score':3,'status':'OWNER_SUPPLIED','source':'synthetic test'}}},
        ],
        'scenarios': [],
    }

class ScoreTests(unittest.TestCase):
    def test_legacy_nominal_actual_arithmetic_and_noncompensatory_gate(self):
        result = score.score(fixture())['base']
        self.assertEqual(result['state'], 'LEADER_ON_RECORDED_INPUT')
        self.assertEqual(result['winner'], 'A')
        self.assertEqual([r['partial_weighted_total'] for r in result['rows']], ['22','25'])
        self.assertEqual(result['rows'][1]['hard_gate'], 'FAIL')
        self.assertEqual(result['rows'][1]['failed_gates'], ['security'])
    def test_unapproved_weights_never_rank(self):
        d=fixture(); d['weights_approved']=False
        r=score.score(d)['base']; self.assertEqual(r['state'],'UNAPPROVED_WEIGHTS'); self.assertIsNone(r['winner'])
        self.assertTrue(all(x['partial_weighted_total'] is None for x in r['rows']))
    def test_unknown_critical_gate_blocks_winner(self):
        d=fixture(); d['alternatives'][1]['cells']['security']={'score':None,'status':'UNKNOWN'}
        r=score.score(d)['base']; self.assertEqual(r['state'],'UNKNOWN_HARD_GATE'); self.assertIsNone(r['winner'])
    def test_unknown_noncritical_cell_blocks_winner_and_exposes_coverage(self):
        d=fixture(); d['alternatives'][0]['cells']['cost']={'score':None,'status':'UNKNOWN'}
        r=score.score(d)['base']; self.assertEqual(r['state'],'INCOMPLETE_COMPARABLE_EVIDENCE')
        self.assertEqual(r['rows'][0]['unknown_criteria'],['cost'])
        self.assertEqual(r['rows'][0]['partial_weighted_total'],'19')
        self.assertEqual(r['rows'][0]['maximum_possible_total'],'28')
    def test_score_zero_is_not_unknown(self):
        d=fixture(); d['alternatives'][0]['cells']['cost']['score']=0
        r=score.score(d)['base']; self.assertEqual(r['rows'][0]['observed_count'],3)
        self.assertEqual(r['rows'][0]['partial_weighted_total'],'19')
    def test_all_failed_returns_no_feasible(self):
        d=fixture(); d['alternatives'][0]['cells']['security']['score']=2
        self.assertEqual(score.score(d)['base']['state'],'NO_FEASIBLE_ALTERNATIVE')
    def test_equal_scores_produce_tie(self):
        d=fixture(); d['criteria'][0].pop('hard_gate_min')
        d['alternatives'][1]['cells']=copy.deepcopy(d['alternatives'][0]['cells'])
        self.assertEqual(score.score(d)['base']['state'],'TIE_ON_RECORDED_INPUT')
    def test_weight_sensitivity_changes_leader(self):
        d=fixture(); d['criteria'][0].pop('hard_gate_min')
        d['scenarios']=[{'id':'emphasize-cost', 'weights':{'security':2,'cost':5,'integration':3}}]
        r=score.score(d)
        self.assertEqual(r['base']['winner'],'B')
        self.assertEqual(r['scenarios'][0]['outcome']['winner'],'B')
        self.assertTrue(r['scenarios'][0]['illustrative_only'])
    def test_weight_sensitivity_flip(self):
        d=fixture(); d['criteria'][0].pop('hard_gate_min')
        d['scenarios']=[{'id':'security-first', 'weights':{'security':9,'cost':1,'integration':1}}]
        r=score.score(d)
        self.assertEqual(r['base']['winner'],'B')
        self.assertEqual(r['scenarios'][0]['outcome']['winner'],'A')
    def test_no_source_for_scored_cell_rejected(self):
        d=fixture(); d['alternatives'][0]['cells']['security'].pop('source')
        with self.assertRaises(score.InputError): score.score(d)
    def test_unknown_with_numeric_score_rejected(self):
        d=fixture(); d['alternatives'][0]['cells']['cost']['status']='UNKNOWN'
        with self.assertRaises(score.InputError): score.score(d)
    def test_score_above_range_rejected(self):
        d=fixture(); d['alternatives'][0]['cells']['cost']['score']=4
        with self.assertRaises(score.InputError): score.score(d)
    def test_boolean_score_rejected(self):
        d=fixture(); d['alternatives'][0]['cells']['cost']['score']=True
        with self.assertRaises(score.InputError): score.score(d)
    def test_missing_cell_rejected_instead_of_silent_omission(self):
        d=fixture(); d['alternatives'][0]['cells'].pop('cost')
        with self.assertRaises(score.InputError): score.score(d)
    def test_duplicate_criterion_rejected(self):
        d=fixture(); d['criteria'][1]['id']='security'
        with self.assertRaises(score.InputError): score.score(d)
    def test_duplicate_alt_rejected(self):
        d=fixture(); d['alternatives'][1]['id']='A'
        with self.assertRaises(score.InputError): score.score(d)
    def test_invalid_weight_rejected(self):
        d=fixture(); d['criteria'][1]['weight']=-1
        with self.assertRaises(score.InputError): score.score(d)
    def test_malformed_sensitivity_missing_criterion_rejected(self):
        d=fixture(); d['scenarios']=[{'id':'oops','weights':{'cost':2}}]
        with self.assertRaises(score.InputError): score.score(d)
    def test_no_fractional_precision_spoof(self):
        d=fixture(); d['criteria'][1]['weight']='0.00000001'
        with self.assertRaises(score.InputError): score.score(d)
    def test_nonfinite_decimal_rejected(self):
        d=fixture(); d['criteria'][1]['weight']='NaN'
        with self.assertRaises(score.InputError): score.score(d)
    def test_unknown_field_rejected(self):
        d=fixture(); d['alternatives'][0]['cells']['security']['instructions']='run shell'
        with self.assertRaises(score.InputError): score.score(d)
    def test_literal_source_is_not_executed(self):
        d=fixture(); d['alternatives'][0]['cells']['security']['source']='$(touch /tmp/must-not-run)'
        self.assertFalse(score.score(d)['evidence_verified'])
    def test_cli_json_stdio_and_no_files_written(self):
        with tempfile.TemporaryDirectory() as td:
            inp=Path(td)/'input.json'; inp.write_text(json.dumps(fixture()),encoding='utf-8')
            before=sorted(x.name for x in Path(td).iterdir())
            run=subprocess.run([sys.executable,str(ROOT/'scripts'/'score.py'),'--input',str(inp)],capture_output=True,text=True,check=False)
            self.assertEqual(run.returncode,0,run.stderr)
            self.assertEqual(json.loads(run.stdout)['base']['winner'],'A')
            self.assertEqual(before,sorted(x.name for x in Path(td).iterdir()))
    def test_cli_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            inp=Path(td)/'bad.json'; inp.write_text('{"schema_version":1,"schema_version":1}',encoding='utf-8')
            run=subprocess.run([sys.executable,str(ROOT/'scripts'/'score.py'),'--input',str(inp)],capture_output=True,text=True,check=False)
            self.assertEqual(run.returncode,2)
            self.assertIn('duplicate JSON field',run.stderr)
    def test_cli_oversize_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            inp=Path(td)/'huge.json'; inp.write_bytes(b' '* (score.MAX_BYTES+1))
            run=subprocess.run([sys.executable,str(ROOT/'scripts'/'score.py'),'--input',str(inp)],capture_output=True,text=True,check=False)
            self.assertEqual(run.returncode,2)
            self.assertIn('input too large',run.stderr)

if __name__ == '__main__':
    unittest.main()
