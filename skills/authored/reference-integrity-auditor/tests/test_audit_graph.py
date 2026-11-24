import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('audit_graph', ROOT/'scripts'/'audit_graph.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def original():
    return json.loads((ROOT/'examples'/'skillz-public-links-pinned.json').read_text(encoding='utf-8'))


def row(state='FOUND',**updates):
    d = copy.deepcopy(original())
    item = d['edges'][0]['lookup']
    item['state'] = state
    item.update(updates)
    return d


class ReferenceGraphTests(unittest.TestCase):
    def finding(self, d):
        return mod.audit(d)['findings'][0]

    def reject(self, mutate):
        d = original()
        mutate(d)
        with self.assertRaises(mod.InvalidInput):
            mod.audit(d)

    def test_public_pinned_links_verifiably_present(self):
        o = mod.audit(original())
        self.assertEqual([f['status'] for f in o['findings']], ['VERIFIED_CURRENT']*3)
        self.assertEqual(o['impacts'][0]['direct_dependents'], ['entrypoint'])
        self.assertEqual(o['impacts'][0]['transitive_dependents'], [])
        self.assertFalse(o['target_evidence_authenticated'])
        self.assertFalse(o['writes_performed'])
        self.assertEqual(o['orphan_coverage'], 'UNDETERMINED_INCOMPLETE_ENUMERATION')
    def test_missing_known_target_only_broken_with_proof(self):
        self.assertEqual(self.finding(row('ABSENT',absence_proven=True,target_current=None))['status'],'BROKEN_CONFIRMED')
    def test_missing_target_without_proof_unresolved(self):
        self.assertEqual(self.finding(row('ABSENT',absence_proven=False,target_current=None))['status'],'UNRESOLVED')
    def test_404_does_not_mean_broken(self):
        self.assertEqual(self.finding(row('HTTP_404',absence_proven=False))['status'],'UNRESOLVED')
    def test_403_denied_is_not_broken(self):
        self.assertEqual(self.finding(row('DENIED'))['status'],'INACCESSIBLE')
    def test_denied_never_shows_target_id(self):
        self.assertNotIn('target_id',self.finding(row('DENIED')))
    def test_unapproved_lookup_is_blocked(self):
        self.assertEqual(self.finding(row(authorized=False))['status'],'BLOCKED')
    def test_incomplete_lookup_is_unresolved(self):
        self.assertEqual(self.finding(row(complete=False))['status'],'UNRESOLVED')
    def test_unchecked_is_unresolved(self):
        self.assertEqual(self.finding(row('NOT_RUN'))['status'],'UNRESOLVED')
    def test_unknown_lookup_unresolved(self):
        self.assertEqual(self.finding(row('UNKNOWN'))['status'],'UNRESOLVED')
    def test_stale_source_wins_over_404(self):
        self.assertEqual(self.finding(row('HTTP_404',source_current=False))['status'],'STALE_VERSION')
    def test_stale_target_wins_over_404(self):
        self.assertEqual(self.finding(row('HTTP_404',target_current=False))['status'],'STALE_VERSION')
    def test_missing_source_revision_binding_unresolved(self):
        self.assertEqual(self.finding(row(source_current=None))['status'],'UNRESOLVED')
    def test_missing_target_revision_binding_unresolved(self):
        self.assertEqual(self.finding(row(target_current=None))['status'],'UNRESOLVED')
    def test_redirect_with_provider_proof(self):
        self.assertEqual(self.finding(row('REDIRECT',redirect_verified=True))['status'],'MOVED_OR_REDIRECT')
    def test_unverified_redirect_is_blocked(self):
        self.assertEqual(self.finding(row('REDIRECT',redirect_verified=False))['status'],'BLOCKED')
    def test_verified_missing_heading_can_be_broken(self):
        d = row(anchor='MISSING',anchor_renderer_verified=True);d['edges'][0]['kind']='HEADING_ANCHOR'
        self.assertEqual(self.finding(d)['status'],'BROKEN_CONFIRMED')
    def test_heading_with_unknown_renderer_not_broken(self):
        d=row(anchor='NOT_CHECKED');d['edges'][0]['kind']='HEADING_ANCHOR'
        self.assertEqual(self.finding(d)['status'],'UNRESOLVED')
    def test_anchor_not_applicable_to_heading_unresolved(self):
        d=row(anchor='NOT_APPLICABLE');d['edges'][0]['kind']='HEADING_ANCHOR'
        self.assertEqual(self.finding(d)['status'],'UNRESOLVED')
    def test_renderer_not_verified_keeps_missing_anchor_unresolved(self):
        d=row(anchor='MISSING',anchor_renderer_verified=False);d['edges'][0]['kind']='HEADING_ANCHOR'
        self.assertEqual(self.finding(d)['status'],'UNRESOLVED')
    def test_renderer_not_verified_keeps_valid_anchor_unresolved(self):
        d=row(anchor='VALID',anchor_renderer_verified=False);d['edges'][0]['kind']='HEADING_ANCHOR'
        self.assertEqual(self.finding(d)['status'],'UNRESOLVED')
    def test_absent_target_cannot_have_current_target_version(self):
        self.reject(lambda d:d['edges'][0]['lookup'].update(state='ABSENT',absence_proven=True,target_current=True))
    def test_redirect_proof_invalid_for_found_state(self):
        self.reject(lambda d:d['edges'][0]['lookup'].update(redirect_verified=True))
    def test_absence_proof_invalid_for_found_state(self):
        self.reject(lambda d:d['edges'][0]['lookup'].update(absence_proven=True))
    def test_secret_target_node_completely_withheld(self):
        d=original();d['nodes'][1]['visible']=False
        result=mod.audit(d)
        self.assertTrue(result['privacy_limited'])
        self.assertNotIn('contract',json.dumps(result))
        self.assertNotIn('link-contract',json.dumps(result))
    def test_secret_source_node_and_edge_withheld(self):
        d=original();d['nodes'][0]['visible']=False
        result=mod.audit(d)
        self.assertEqual(result['findings'],[])
        self.assertNotIn('entrypoint',json.dumps(result))
    def test_unknown_target_does_not_assert_verified_or_broken(self):
        d=original();d['edges'][0]['target']='not-indexed'
        f=self.finding(d)
        self.assertNotIn('target_id',f)
        self.assertEqual(f['status'],'UNRESOLVED')
    def test_bounded_orphans_only_when_enumeration_complete(self):
        d=original();d['enumeration']['sources_complete']=True
        out=mod.audit(d)
        self.assertEqual(out['orphan_coverage'],'BOUNDED_COMPLETE_WITHIN_SCOPE')
        self.assertEqual(out['orphan_candidates_within_approved_scope'],['entrypoint'])
    def test_partial_enumeration_never_claims_orphan(self):
        d=original();d['enumeration']['sources_complete']=False
        self.assertEqual(mod.audit(d)['orphan_candidates_within_approved_scope'],[])
    def test_visibility_incomplete_never_claims_orphan(self):
        d=original();d['enumeration']['sources_complete']=True;d['enumeration']['visibility_complete']=False
        self.assertEqual(mod.audit(d)['orphan_candidates_within_approved_scope'],[])
    def test_hidden_node_blocks_orphan_claim_even_without_visible_edges(self):
        d=original();d['nodes'].append({'id':'withheld','visible':False,'revision':'s0'})
        d['enumeration']['sources_complete']=True
        self.assertEqual(mod.audit(d)['orphan_coverage'],'UNDETERMINED_INCOMPLETE_ENUMERATION')
    def test_unresolved_edge_is_possible_not_confirmed_impact(self):
        d=row('NOT_RUN')
        impacted=mod.audit(d)['impacts'][0]
        self.assertEqual(impacted['direct_dependents'],[])
        self.assertEqual(impacted['unverified_direct_dependents'],['entrypoint'])
    def test_transitive_impact_reverse_graph(self):
        d=original();d['nodes'].extend([{'id':'consumer','visible':True,'revision':'rev1'}, {'id':'top','visible':True,'revision':'rev1'}])
        proto=copy.deepcopy(d['edges'][0]);proto['id']='ref-downstream';proto['source']='consumer';proto['target']='entrypoint';d['edges'].append(proto)
        proto2=copy.deepcopy(proto);proto2['id']='ref-top';proto2['source']='top';proto2['target']='consumer';d['edges'].append(proto2)
        a=mod.audit(d)['impacts'][0]
        self.assertEqual(a['direct_dependents'],['entrypoint'])
        self.assertEqual(a['transitive_dependents'],['consumer','top'])
    def test_cycle_terminates_and_does_not_self_impact(self):
        d=original();proto=copy.deepcopy(d['edges'][0]);proto['id']='reverse';proto['source']='contract';proto['target']='entrypoint';d['edges'].append(proto)
        x=mod.audit(d)['impacts'][0]
        self.assertEqual(x['direct_dependents'],['entrypoint'])
        self.assertNotIn('contract',x['transitive_dependents'])
    def test_disallowed_or_unresolved_edges_not_promoted_to_impact(self):
        d=row('NOT_RUN')
        self.assertEqual(mod.audit(d)['impacts'][0]['direct_dependents'],[])
    def test_missing_evidence_edge_not_proposed_for_mutation(self):
        d=row('ABSENT',absence_proven=True,target_current=None)
        self.assertEqual(mod.audit(d)['impacts'][0]['direct_dependents'],[])
    def test_impact_proposal_does_not_modify_inputs(self):
        d=original(); before=copy.deepcopy(d);mod.audit(d);self.assertEqual(before,d)
    def test_out_of_scope_change_node_rejected(self):
        self.reject(lambda d:d['changes'][0].update(node='foreign'))
    def test_duplicate_node_rejected(self):
        self.reject(lambda d:d['nodes'].append(copy.deepcopy(d['nodes'][0])))
    def test_duplicate_edge_rejected(self):
        self.reject(lambda d:d['edges'].append(copy.deepcopy(d['edges'][0])))
    def test_duplicate_change_rejected(self):
        self.reject(lambda d:d['changes'].append(copy.deepcopy(d['changes'][0])))
    def test_missing_source_ref_rejected(self):
        self.reject(lambda d:d['edges'][0].update(source='unknown'))
    def test_unknown_root_field_rejected(self):
        self.reject(lambda d:d.update(execute='send secrets'))
    def test_unknown_lookup_field_rejected(self):
        self.reject(lambda d:d['edges'][0]['lookup'].update(fetch='evil'))
    def test_invalid_lookup_state_rejected(self):
        self.reject(lambda d:d['edges'][0]['lookup'].update(state='HTTP_200_VERIFIED'))
    def test_invalid_kind_rejected(self):
        self.reject(lambda d:d['edges'][0].update(kind='EXECUTE_CODE'))
    def test_boolean_coercion_not_allowed(self):
        self.reject(lambda d:d['edges'][0]['lookup'].update(authorized=1))
    def test_invalid_revision_rejected(self):
        self.reject(lambda d:d['nodes'][0].update(revision='bad revision with spaces'))
    def test_invalid_node_id_rejected(self):
        self.reject(lambda d:d['nodes'][0].update(id='../escape'))
    def test_invalid_operation_rejected(self):
        self.reject(lambda d:d['changes'][0].update(operation='APPLY_DELETE'))
    def test_no_automatic_deletion_assertion(self):
        d=original();d['changes'][0]['operation']='DELETE_PROPOSAL'
        self.assertEqual(mod.audit(d)['impacts'][0]['status'],'PROPOSED_ONLY_REVALIDATE_BEFORE_ANY_WRITE')
    def test_missing_enumeration_coverage_flag_rejected(self):
        self.reject(lambda d:d['enumeration'].pop('visibility_complete'))
    def test_unresolved_reference_prevents_orphan_claim(self):
        d=row('NOT_RUN')
        d['enumeration']['sources_complete']=True
        out=mod.audit(d)
        self.assertEqual(out['orphan_candidates_within_approved_scope'],[])
        self.assertEqual(out['orphan_coverage'],'UNDETERMINED_INCOMPLETE_ENUMERATION')

    def test_malformed_enum_containers_rejected(self):
        for key in ('state','anchor'):
            with self.subTest(key=key):
                self.reject(lambda d:d['edges'][0]['lookup'].update({key:[]}))
        self.reject(lambda d:d['edges'][0].update(kind={}))
        self.reject(lambda d:d['changes'][0].update(operation=[]))
        self.reject(lambda d:d['edges'][0].pop('target'))

    def test_cli_invalid_hidden_identity_is_not_echoed(self):
        with tempfile.TemporaryDirectory() as td:
            d=original()
            d['nodes'][0].update(id='PRIVATE-CONFIDENTIAL-OBJECT',visible='malformed')
            p=Path(td)/'in.json';p.write_text(json.dumps(d),encoding='utf-8')
            v=subprocess.run([sys.executable,str(ROOT/'scripts'/'audit_graph.py'),'--input',str(p)],capture_output=True,text=True,timeout=10)
            self.assertEqual(v.returncode,2)
            self.assertNotIn('PRIVATE-CONFIDENTIAL-OBJECT',v.stderr+v.stdout)

    def test_cli_missing_private_path_is_not_echoed(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'PRIVATE-CONFIDENTIAL-PATH.json'
            v=subprocess.run([sys.executable,str(ROOT/'scripts'/'audit_graph.py'),'--input',str(p)],capture_output=True,text=True,timeout=10)
            self.assertEqual(v.returncode,2)
            self.assertNotIn('PRIVATE-CONFIDENTIAL-PATH',v.stderr+v.stdout)

    def test_cli_deep_json_is_bounded_without_traceback(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'in.json';p.write_text('['*2000+'0'+']'*2000,encoding='utf-8')
            v=subprocess.run([sys.executable,str(ROOT/'scripts'/'audit_graph.py'),'--input',str(p)],capture_output=True,text=True,timeout=10)
            self.assertEqual(v.returncode,2)
            self.assertNotIn('Traceback',v.stderr)

    def test_cli_valid_json_stdout_no_files(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'in.json';p.write_text(json.dumps(original()),encoding='utf-8')
            before={x.name for x in Path(td).iterdir()}
            v=subprocess.run([sys.executable,str(ROOT/'scripts'/'audit_graph.py'),'--input',str(p)],capture_output=True,text=True)
            self.assertEqual(v.returncode,0,v.stderr)
            self.assertFalse(json.loads(v.stdout)['writes_performed'])
            self.assertEqual(before,{x.name for x in Path(td).iterdir()})
    def test_cli_rejects_symlink_input(self):
        with tempfile.TemporaryDirectory() as td:
            original_path=Path(td)/'original.json'
            original_path.write_text(json.dumps(original()),encoding='utf-8')
            link=Path(td)/'link.json'
            try: link.symlink_to(original_path)
            except (OSError, NotImplementedError): self.skipTest('symlink unavailable')
            v=subprocess.run([sys.executable,str(ROOT/'scripts'/'audit_graph.py'),'--input',str(link)],capture_output=True,text=True)
            self.assertEqual(v.returncode,2)
            self.assertIn('symlinked input',v.stderr)
    def test_cli_duplicate_json_fields_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'in.json';p.write_text('{"schema_version":1,"schema_version":1}')
            v=subprocess.run([sys.executable,str(ROOT/'scripts'/'audit_graph.py'),'--input',str(p)],capture_output=True,text=True)
            self.assertEqual(v.returncode,2)
            self.assertIn('duplicate JSON field',v.stderr)
    def test_cli_nonfinite_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'in.json';p.write_text('{"x":NaN}')
            v=subprocess.run([sys.executable,str(ROOT/'scripts'/'audit_graph.py'),'--input',str(p)],capture_output=True,text=True)
            self.assertEqual(v.returncode,2)
            self.assertIn('nonfinite JSON constant',v.stderr)
    def test_cli_oversize_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'in.json';p.write_bytes(b' '* (mod.MAX_BYTES+1))
            v=subprocess.run([sys.executable,str(ROOT/'scripts'/'audit_graph.py'),'--input',str(p)],capture_output=True,text=True)
            self.assertEqual(v.returncode,2)
    def test_no_network_or_subprocess_imports(self):
        source=(ROOT/'scripts'/'audit_graph.py').read_text(encoding='utf-8')
        for word in ('urllib', 'requests', 'socket', 'subprocess', 'os.system', 'exec('):
            self.assertNotIn(word,source)
    def test_sparse_records_reject_instead_of_guess(self):
        self.reject(lambda d:d['edges'][0]['lookup'].pop('absence_proven'))
    def test_hidden_change_does_not_leak_impact(self):
        d=original();d['nodes'][1]['visible']=False
        res=mod.audit(d)
        self.assertEqual(res['impacts'],[])


if __name__=='__main__':unittest.main()
