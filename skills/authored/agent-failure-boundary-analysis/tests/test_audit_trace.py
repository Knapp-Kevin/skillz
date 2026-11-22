import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('audit_trace', ROOT / 'scripts' / 'audit_trace.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def fixture():
    return {
        'schema_version': 1, 'incident_id': 'PUBLIC-REPO-PR815', 'inventory_complete': False, 'attempt_budget': None,
        'events': [
            {'id':'socket', 'kind':'CI_RECEIPT','state':'OBSERVED','source_ref':'github:pr815/socket-success','after':[]},
            {'id':'merge','kind':'PR_MERGE_RECEIPT','state':'OBSERVED','source_ref':'github:pr815/merge99b3fe','after':['socket']},
        ],
        'claims':[
            {'id':'merged','kind':'MERGED','evidence_refs':['merge']},
            {'id':'deployed','kind':'DEPLOYED','evidence_refs':['merge']},
            {'id':'user-success','kind':'USER_OUTCOME_VERIFIED','evidence_refs':['merge']},
        ]
    }


class TraceAuditTests(unittest.TestCase):
    def check_invalid(self, mutate):
        d=fixture(); mutate(d)
        with self.assertRaises(audit.TraceError):audit.audit(d)

    def test_actual_public_state_receipt_vs_deploy_claim(self):
        result=audit.audit(fixture())
        self.assertEqual([x['status'] for x in result['claims']], [
            'SUPPORTED_BY_RECORDED_INPUT', 'INSUFFICIENT_RECORDED_EVIDENCE','INSUFFICIENT_RECORDED_EVIDENCE'])
        self.assertFalse(result['evidence_authenticity_verified'])
        self.assertEqual(result['root_cause'],'NOT_DETERMINED')
    def test_merge_does_not_imply_deploy_or_user_outcome(self):
        r=audit.audit(fixture())
        self.assertEqual(r['claims'][1]['supporting_event_ids'],[])
        self.assertEqual(r['claims'][2]['supporting_event_ids'],[])
    def test_declared_deploy_receipt_supports_only_deploy(self):
        d=fixture();d['events'].append({'id':'deployment','kind':'DEPLOY_RECEIPT','state':'OBSERVED','source_ref':'redacted deploy receipt','after':['merge']});d['claims'][1]['evidence_refs']=['deployment']
        r=audit.audit(d);self.assertEqual(r['claims'][1]['status'],'SUPPORTED_BY_RECORDED_INPUT');self.assertEqual(r['claims'][2]['status'],'INSUFFICIENT_RECORDED_EVIDENCE')
    def test_alleged_deploy_receipt_not_enough(self):
        d=fixture();d['events'].append({'id':'deployment','kind':'DEPLOY_RECEIPT','state':'ALLEGED','source_ref':'agent assertion','after':[]});d['claims'][1]['evidence_refs']=['deployment']
        self.assertEqual(audit.audit(d)['claims'][1]['status'],'INSUFFICIENT_RECORDED_EVIDENCE')
    def test_user_receipt_requires_distinct_outcome_event(self):
        d=fixture();d['events'].append({'id':'customer','kind':'USER_OUTCOME_RECEIPT','state':'OBSERVED','source_ref':'customer verification','after':['merge']});d['claims'][2]['evidence_refs']=['customer']
        self.assertEqual(audit.audit(d)['claims'][2]['status'],'SUPPORTED_BY_RECORDED_INPUT')
    def test_ordering_is_from_dependencies_not_input_order(self):
        d=fixture();d['events'].reverse()
        self.assertEqual(audit.audit(d)['ordering']['explicit_precedence_layers'], [['socket'],['merge']])
    def test_independent_events_do_not_acquire_artificial_sequence(self):
        d=fixture();d['events'][1]['after']=[]
        self.assertEqual(audit.audit(d)['ordering']['explicit_precedence_layers'], [['merge','socket']])
    def test_unknown_order_parent(self):
        self.check_invalid(lambda d:d['events'][1]['after'].append('phantom'))
    def test_cyclic_order(self):
        self.check_invalid(lambda d:d['events'][0]['after'].append('merge'))
    def test_self_edge(self):
        self.check_invalid(lambda d:d['events'][0]['after'].append('socket'))
    def test_duplicate_after_edge(self):
        self.check_invalid(lambda d:d['events'][1]['after'].append('socket'))
    def test_duplicate_event(self):
        self.check_invalid(lambda d:d['events'].append(copy.deepcopy(d['events'][0])))
    def test_missing_source_for_observed(self):
        self.check_invalid(lambda d:d['events'][0].pop('source_ref'))
    def test_undeclared_claim_ref(self):
        self.check_invalid(lambda d:d['claims'][0]['evidence_refs'].append('phantom'))
    def test_duplicate_claim(self):
        self.check_invalid(lambda d:d['claims'].append(copy.deepcopy(d['claims'][0])))
    def test_unknown_event_kind(self):
        self.check_invalid(lambda d:d['events'][0].update(kind='DEPLOYED_SUCCESSFUL_NOT_REAL'))
    def test_unsupported_extra_instruction_fields(self):
        self.check_invalid(lambda d:d['events'][0].update(execute='curl secret.example'))
    def test_missing_completeness_flag(self):
        self.check_invalid(lambda d:d.pop('inventory_complete'))
    def test_successful_authorization_scope_and_order_is_recorded(self):
        d=fixture();d['events'].extend([
            {'id':'approval','kind':'APPROVAL','state':'OBSERVED','source_ref':'owner scope','authorizes_scope':'repo.write','after':[]},
            {'id':'write','kind':'WRITE_ACTION','state':'OBSERVED','source_ref':'write receipt','action_scope':'repo.write','approval_ref':'approval','after':['approval']},
        ])
        self.assertEqual(audit.audit(d)['writes'][0]['status'],'APPROVAL_REFERENCE_PRESENT')
    def test_bare_claimed_approval_not_sufficient(self):
        d=fixture();d['events'].extend([
            {'id':'approval','kind':'APPROVAL','state':'ALLEGED','source_ref':'agent quote','authorizes_scope':'repo.write','after':[]},
            {'id':'write','kind':'WRITE_ACTION','state':'OBSERVED','source_ref':'write receipt','action_scope':'repo.write','approval_ref':'approval','after':['approval']},
        ])
        self.assertEqual(audit.audit(d)['writes'][0]['status'],'AUTHORITY_NOT_ESTABLISHED')
    def test_approval_wrong_scope_does_not_authorize(self):
        d=fixture();d['events'].extend([
            {'id':'approval','kind':'APPROVAL','state':'OBSERVED','source_ref':'owner scope','authorizes_scope':'docs.read','after':[]},
            {'id':'write','kind':'WRITE_ACTION','state':'OBSERVED','source_ref':'write receipt','action_scope':'repo.write','approval_ref':'approval','after':['approval']},
        ])
        self.assertEqual(audit.audit(d)['writes'][0]['status'],'AUTHORITY_NOT_ESTABLISHED')
    def test_approval_must_precede_action_in_explicit_order(self):
        d=fixture();d['events'].extend([
            {'id':'approval','kind':'APPROVAL','state':'OBSERVED','source_ref':'owner scope','authorizes_scope':'repo.write','after':[]},
            {'id':'write','kind':'WRITE_ACTION','state':'OBSERVED','source_ref':'write receipt','action_scope':'repo.write','approval_ref':'approval','after':[]},
        ])
        self.assertEqual(audit.audit(d)['writes'][0]['status'],'AUTHORITY_NOT_ESTABLISHED')
    def test_runaway_breach_only_from_observed_attempts(self):
        d=fixture();d['attempt_budget']=2
        for i in range(3):d['events'].append({'id':f'attempt{i}','kind':'TOOL_ATTEMPT','state':'OBSERVED','source_ref':f'tool{i}','after':[]})
        self.assertEqual(audit.audit(d)['attempt_limit']['status'],'OBSERVED_ATTEMPTS_EXCEED_RECORDED_LIMIT')
    def test_partial_attempts_below_limit_are_unknown(self):
        d=fixture();d['attempt_budget']=4;d['events'].append({'id':'attempt','kind':'TOOL_ATTEMPT','state':'OBSERVED','source_ref':'tool','after':[]})
        self.assertEqual(audit.audit(d)['attempt_limit']['status'],'UNKNOWN_INPUT_INCOMPLETE')
    def test_missing_attempts_cannot_count_as_observed(self):
        d=fixture();d['attempt_budget']=1;d['events'].append({'id':'attempt','kind':'TOOL_ATTEMPT','state':'MISSING','after':[]})
        self.assertEqual(audit.audit(d)['attempt_limit']['observed_attempt_records'],0)
    def test_input_claimed_complete_allows_conditional_no_breach(self):
        d=fixture();d['attempt_budget']=1;d['inventory_complete']=True
        self.assertEqual(audit.audit(d)['attempt_limit']['status'],'WITHIN_LIMIT_IN_DECLARED_COMPLETE_INPUT')
    def test_invalid_budget_type(self):
        self.check_invalid(lambda d:d.update(attempt_budget=True))
    def test_source_content_is_inert(self):
        d=fixture();d['events'][0]['source_ref']='$(echo hacked >&2)'
        self.assertFalse(audit.audit(d)['evidence_authenticity_verified'])
    def test_cli_outputs_json_without_side_effects(self):
        with tempfile.TemporaryDirectory() as td:
            inp=Path(td)/'input.json';inp.write_text(json.dumps(fixture()),encoding='utf-8')
            before={p.name for p in Path(td).iterdir()}
            r=subprocess.run([sys.executable,str(ROOT/'scripts/audit_trace.py'),'--input',str(inp)],capture_output=True,text=True)
            self.assertEqual(r.returncode,0,r.stderr)
            self.assertEqual(json.loads(r.stdout)['root_cause'],'NOT_DETERMINED')
            self.assertEqual(before,{p.name for p in Path(td).iterdir()})
    def test_cli_rejects_duplicate_json_field(self):
        with tempfile.TemporaryDirectory() as td:
            inp=Path(td)/'bad.json';inp.write_text('{"schema_version":1,"schema_version":1}',encoding='utf-8')
            r=subprocess.run([sys.executable,str(ROOT/'scripts/audit_trace.py'),'--input',str(inp)],capture_output=True,text=True)
            self.assertEqual(r.returncode,2)
            self.assertIn('duplicate JSON key',r.stderr)
    def test_cli_rejects_oversized_file(self):
        with tempfile.TemporaryDirectory() as td:
            inp=Path(td)/'huge.json';inp.write_bytes(b' '* (audit.MAX_BYTES+1))
            r=subprocess.run([sys.executable,str(ROOT/'scripts/audit_trace.py'),'--input',str(inp)],capture_output=True,text=True)
            self.assertEqual(r.returncode,2)
            self.assertIn('exceeds 1 MiB',r.stderr)


    def test_cli_refuses_linked_input_file(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            private = root / "outside.json"
            private.write_text("out-of-scope sentinel", encoding="utf-8")
            alias = root / "approved.json"
            alias.symlink_to(private)
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "audit_trace.py"), "--input", str(alias)],
                capture_output=True, text=True)
            self.assertEqual(proc.returncode, 2)
            self.assertIn("symlinked input", proc.stderr)
            self.assertNotIn("out-of-scope sentinel", proc.stdout + proc.stderr)

    def test_cli_refuses_linked_parent_directory(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "private").mkdir()
            target = root / "private" / "outside.json"
            target.write_text("out-of-scope sentinel", encoding="utf-8")
            alias = root / "approved"
            alias.symlink_to(root / "private", target_is_directory=True)
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "audit_trace.py"), "--input",
                 str(alias / "outside.json")], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 2)
            self.assertIn("symlinked input", proc.stderr)
            self.assertNotIn("out-of-scope sentinel", proc.stdout + proc.stderr)

if __name__=='__main__':unittest.main()
