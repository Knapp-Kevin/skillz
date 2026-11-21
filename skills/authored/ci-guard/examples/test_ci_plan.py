"""Anonymous offline true-Git source fixture and independent plan/qualifier tests.

No GitHub Actions run, no external runner-minute evidence, no observed
model behavior. All fixtures created in disposable local repositories.
"""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('ci_plan', ROOT/'scripts/ci_plan.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)
POLICY = p.validate_policy(p.json_file(ROOT/'examples/impact-graph.json'))
BASE = '1'*40
HEAD = '2'*40
MB = '0'*40


def plan(paths, stage='candidate'):
    return p.make_plan(POLICY, paths, BASE, HEAD, MB, stage)


def evidence(document, run='77', attempt='1'):
    return {'schema_version': 1, 'jobs': {name: {
        'result': 'success' if enabled else 'skipped',
        'receipt': p.receipt(document, name, run, attempt) if enabled else None}
        for name, enabled in document['groups'].items()}}


class PlanTests(unittest.TestCase):
    def test_docs_passive_has_real_docs_obligation_and_no_rust(self):
        doc = plan(['docs/passive/guide.md'])
        self.assertEqual(doc['obligations'], ['docs-links', 'trust-policy'])
        self.assertTrue(doc['groups']['docs'])
        self.assertFalse(doc['groups']['rust'])
        self.assertTrue(p.qualify(POLICY, doc, evidence(doc), doc, '77', '1')['qualified'])

    def test_readme_is_model_input_and_rust_dependency(self):
        doc = plan(['README.md'])
        self.assertEqual(doc['obligations'], ['model-consumer', 'rust-build', 'trust-policy'])
        self.assertFalse(doc['groups']['docs'])
        self.assertTrue(doc['groups']['model'])
        self.assertTrue(doc['groups']['rust'])
        self.assertNotIn('rust-tests', doc['obligations'])

    def test_rust_change_closes_rust_tests_and_build(self):
        doc = plan(['src/lib.rs'])
        self.assertEqual(doc['obligations'], ['rust-build', 'rust-tests', 'trust-policy'])
        self.assertTrue(doc['groups']['rust'])
        self.assertFalse(doc['groups']['docs'])

    def test_declared_group_without_any_obligation_is_refused(self):
        from copy import deepcopy
        policy = deepcopy(POLICY)
        policy['groups'].append('security-phantom')
        with self.assertRaisesRegex(p.PlanError, 'group has no executable'):
            p.validate_policy(policy)

    def test_declared_group_with_real_obligation_is_not_ghost(self):
        from copy import deepcopy
        policy = deepcopy(POLICY)
        policy['groups'].append('security-extra')
        policy['obligations']['security-proof'] = {
            'group': 'security-extra', 'needs': []}
        policy['full'].append('security-proof')
        validated = p.validate_policy(policy)
        result = p.make_plan(validated,
                             ['.github/workflows/test.yml'], BASE, HEAD, MB)
        self.assertTrue(result['groups']['security-extra'])

    def test_full_policy_rejects_independent_omitted_obligation(self):
        from copy import deepcopy
        policy = deepcopy(POLICY)
        policy['obligations']['native-proof'] = {'group': 'rust', 'needs': []}
        with self.assertRaisesRegex(p.PlanError, 'full plan omits'):
            p.validate_policy(policy)

    def test_full_policy_allows_transitive_obligation_not_repeated_in_roots(self):
        # The graph fixture omits rust-build from full roots but includes
        # it transitively through rust-tests and model-consumer.
        validated = p.validate_policy(POLICY)
        self.assertNotIn('rust-build', validated['full'])
        self.assertEqual(set(p.closure(validated['obligations'], validated['full'])),
                         set(validated['obligations']))

    def test_trust_policy_change_selects_all(self):
        doc = plan(['.github/workflows/check.yml'])
        self.assertTrue(doc['full'])
        self.assertTrue(all(doc['groups'].values()))
        self.assertEqual(doc['unmapped'], ['.github/workflows/check.yml'])

    def test_unknown_change_forces_full(self):
        doc = plan(['data/unknown.binary'])
        self.assertTrue(doc['full'])
        self.assertTrue(all(doc['groups'].values()))

    def test_release_forces_full_and_never_implies_release_publication(self):
        doc = plan(['docs/passive/intro.md'], 'release')
        self.assertTrue(all(doc['groups'].values()))
        self.assertTrue(doc['full'])
        self.assertNotIn('release-qualified', doc)

    def test_overlapping_sources_union_and_deduplicate(self):
        doc = plan(['README.md','src/main.rs','README.md'])
        self.assertEqual(doc['changed_paths'], ['README.md','src/main.rs'])
        self.assertIn('rust-tests', doc['obligations'])
        self.assertIn('model-consumer', doc['obligations'])

    def test_documentation_prefix_collision_forces_full(self):
        self.assertTrue(plan(['docs-private/secret.md'])['full'])
        self.assertTrue(plan(['docsecrets/secret.md'])['full'])

    def test_missing_skipped_failed_canceled_or_timed_out_docs_cannot_pass(self):
        doc = plan(['docs/passive/guide.md'])
        for status in ('skipped','failure','cancelled','timed_out','neutral',''):
            e = evidence(doc)
            e['jobs']['docs']['result'] = status
            with self.subTest(status=status), self.assertRaises(p.PlanError):
                p.qualify(POLICY, doc, e, doc, '77', '1')
        e = evidence(doc)
        e['jobs'].pop('docs')
        with self.assertRaises(p.PlanError):
            p.qualify(POLICY, doc, e, doc, '77', '1')

    def test_doc_result_missing_receipt_fails(self):
        doc = plan(['docs/passive/guide.md'])
        e = evidence(doc)
        e['jobs']['docs']['receipt'] = None
        with self.assertRaises(p.PlanError):
            p.qualify(POLICY, doc, e, doc, '77', '1')

    def test_misrouted_docs_fails(self):
        doc = plan(['docs/passive/guide.md'])
        e = evidence(doc)
        e['jobs']['docs']['receipt'] = e['jobs']['trust']['receipt']
        with self.assertRaises(p.PlanError):
            p.qualify(POLICY, doc, e, doc, '77', '1')

    def test_stale_head_base_merge_base_plan_or_policy_fails(self):
        doc = plan(['README.md'])
        for field, value in [('head','3'*40),('base','3'*40),
                             ('merge_base','3'*40),('policy_sha256','f'*64),
                             ('plan_sha256','f'*64)]:
            stale = dict(doc, **{field:value})
            with self.subTest(field=field), self.assertRaises(p.PlanError):
                p.qualify(POLICY, stale, evidence(stale), doc, '77', '1')

    def test_changed_plan_obligations_rejected_even_if_digest_forged(self):
        doc = plan(['README.md'])
        stale = dict(doc, obligations=['trust-policy'])
        stale['plan_sha256'] = p.digest({k:v for k,v in stale.items() if k != 'plan_sha256'})
        with self.assertRaises(p.PlanError):
            p.qualify(POLICY, stale, evidence(doc), doc, '77', '1')

    def test_duplicated_or_missing_plan_receipts_fails(self):
        doc = plan(['README.md'])
        e = evidence(doc)
        e['jobs']['rust']['receipt']['obligations'] = ['rust-build','rust-build']
        with self.assertRaises(p.PlanError):
            p.qualify(POLICY, doc, e, doc, '77', '1')
        e = evidence(doc)
        e['jobs']['rust'] = {'result':'success'}
        with self.assertRaises(p.PlanError):
            p.qualify(POLICY, doc, e, doc, '77', '1')

    def test_wrong_run_or_attempt_fails(self):
        doc = plan(['README.md'])
        for new_run, new_attempt in [('88','1'),('77','2')]:
            with self.subTest(new_run=new_run,new_attempt=new_attempt), self.assertRaises(p.PlanError):
                p.qualify(POLICY, doc, evidence(doc), doc, new_run, new_attempt)

    def test_unexpected_executed_unselected_job_fails(self):
        doc = plan(['docs/passive/guide.md'])
        e = evidence(doc)
        e['jobs']['model']['result'] = 'success'
        with self.assertRaises(p.PlanError):
            p.qualify(POLICY, doc, e, doc, '77', '1')

    def test_graph_cycles_are_rejected(self):
        bad = json.loads(json.dumps(POLICY))
        bad['obligations']['rust-build']['needs'] = ['rust-tests']
        with self.assertRaises(p.PlanError):
            p.validate_policy(bad)

    def test_graph_dangling_dependency_rejected(self):
        bad = json.loads(json.dumps(POLICY))
        bad['obligations']['rust-tests']['needs'] = ['missing']
        with self.assertRaises(p.PlanError):
            p.validate_policy(bad)

    def test_policy_prefix_requires_separator(self):
        bad = json.loads(json.dumps(POLICY))
        bad['rules'][0]['pattern'] = 'docs'
        with self.assertRaises(p.PlanError):
            p.validate_policy(bad)

    def test_duplicate_keys_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path=Path(d)/'bad.json'
            path.write_text('{"schema_version":1,"schema_version":1}',encoding='utf-8')
            with self.assertRaises(p.PlanError):
                p.json_file(path)

    def test_direct_git_changed_paths_and_merge_base_are_real(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            def git(*args):
                return subprocess.check_output(['git','-C',str(root),*args],stderr=subprocess.DEVNULL).decode().strip()
            git('init','-q')
            git('config','user.name','Fixture')
            git('config','user.email','fixture@example.invalid')
            (root/'README.md').write_text('initial', encoding='utf-8')
            git('add','.')
            git('commit','-qm','first')
            base=git('rev-parse','HEAD')
            (root/'README.md').write_text('model-input-changed', encoding='utf-8')
            (root/'src').mkdir()
            (root/'src/lib.rs').write_text('fn main() {}', encoding='utf-8')
            git('add','.')
            git('commit','-qm','head')
            head=git('rev-parse','HEAD')
            doc=p.git_plan(POLICY, root, base, head, 'candidate')
            self.assertEqual(doc['merge_base'],base)
            self.assertEqual(doc['changed_paths'],['README.md','src/lib.rs'])
            self.assertEqual(doc['head'],head)
            self.assertTrue(p.qualify(POLICY,doc,evidence(doc),doc,'77','1')['qualified'])
            # Change the current candidate ref: stale plan cannot be reused.
            (root/'src/lib.rs').write_text('fn main() { println!("x"); }', encoding='utf-8')
            git('add','.')
            git('commit','-qm','new head')
            newhead=git('rev-parse','HEAD')
            current=p.git_plan(POLICY,root,base,newhead,'candidate')
            with self.assertRaises(p.PlanError):
                p.qualify(POLICY,doc,evidence(doc),current,'77','1')

    def test_git_rename_delete_is_conservative(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            def git(*args):
                return subprocess.check_output(['git','-C',str(root),*args],stderr=subprocess.DEVNULL).decode().strip()
            git('init','-q');git('config','user.name','Fixture');git('config','user.email','fixture@example.invalid')
            (root/'docs').mkdir();(root/'docs/passive').mkdir()
            (root/'docs/passive/start.md').write_text('hello')
            git('add','.');git('commit','-qm','base')
            base=git('rev-parse','HEAD')
            (root/'docs/passive/start.md').rename(root/'README.md')
            git('add','-A');git('commit','-qm','head')
            head=git('rev-parse','HEAD')
            doc=p.git_plan(POLICY,root,base,head,'candidate')
            self.assertEqual(doc['changed_paths'],['README.md','docs/passive/start.md'])
            self.assertTrue(doc['groups']['model'])
            self.assertTrue(doc['groups']['docs'])


if __name__=='__main__':
    unittest.main(verbosity=2)

class ExecutionTests(unittest.TestCase):
    def test_actual_commands_execute_in_dependency_order_and_are_qualified(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            work=root/'work';work.mkdir()
            trace=root/'trace.txt'
            helper=root/'check.py'
            helper.write_text('import sys\nfrom pathlib import Path\np=Path(sys.argv[1]);p.write_text((p.read_text() if p.exists() else "")+sys.argv[2]+"\\n")\n')
            executor={'schema_version':1,'commands':{}}
            for name in POLICY['obligations']:
                executor['commands'][name]={'argv':['python3',str(helper),str(trace),name],'timeout_sec':5}
            p.validate_executor(executor,POLICY)
            doc=p.make_plan(POLICY,['src/lib.rs'],BASE,HEAD,MB,'candidate',executor)
            proof=p.execute(POLICY,executor,doc,'rust',work,'100','1')
            self.assertEqual([x['obligation'] for x in proof['execution']],['rust-build','rust-tests'])
            self.assertEqual(trace.read_text().splitlines(),['rust-build','rust-tests'])
            result={'schema_version':1,'jobs':{group:{
                'result':'success' if active else 'skipped',
                'receipt': p.execute(POLICY,executor,doc,group,work,'100','1') if active else None}
                for group, active in doc['groups'].items()}}
            self.assertTrue(p.qualify(POLICY,doc,result,doc,'100','1',executor)['qualified'])

    def test_execution_refuses_wrong_checkout_or_modified_tracked_source(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            project = root / 'work'
            project.mkdir()
            def git(*args):
                return subprocess.check_output(
                    ['git', '-C', str(project), *args],
                    stderr=subprocess.DEVNULL, text=True).strip()
            git('init', '-q')
            git('config', 'user.name', 'Fixture')
            git('config', 'user.email', 'fixture@example.invalid')
            (project/'docs/passive').mkdir(parents=True)
            doc = project/'docs/passive/guide.md'
            doc.write_text('baseline\n', encoding='utf-8')
            git('add', '.')
            git('commit', '-qm', 'baseline')
            base = git('rev-parse', 'HEAD')
            doc.write_text('revision 2\n', encoding='utf-8')
            git('add', '.')
            git('commit', '-qm', 'head')
            head = git('rev-parse', 'HEAD')
            executor = {'schema_version': 1, 'commands': {
                name: {'argv': ['python3', '-c', 'print(123)'], 'timeout_sec': 5}
                for name in POLICY['obligations']
            }}
            planned = p.git_plan(POLICY, project, base, head, 'candidate', executor)
            proof = p.execute(POLICY, executor, planned, 'docs', root, '14', '1',
                              source_repo=project)
            self.assertEqual([x['exit_code'] for x in proof['execution']], [0])
            git('checkout', '--detach', '-q', base)
            with self.assertRaisesRegex(p.PlanError, 'HEAD does not match'):
                p.execute(POLICY, executor, planned, 'docs', root, '14', '1',
                          source_repo=project)
            git('checkout', '--detach', '-q', head)
            doc.write_text('tampered after checkout\n', encoding='utf-8')
            with self.assertRaisesRegex(p.PlanError, 'modified tracked'):
                p.execute(POLICY, executor, planned, 'docs', root, '14', '1',
                          source_repo=project)

    def test_execution_fails_if_verifier_mutates_tracked_input(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            gitroot = root / 'candidate'
            gitroot.mkdir()
            def git(*args):
                return subprocess.check_output(['git', '-C', str(gitroot), *args],
                                               stderr=subprocess.DEVNULL, text=True).strip()
            git('init', '-q')
            git('config', 'user.name', 'Fixture')
            git('config', 'user.email', 'fixture@example.invalid')
            (gitroot/'docs/passive').mkdir(parents=True)
            source = gitroot/'docs/passive/check.md'
            source.write_text('clean', encoding='utf-8')
            git('add', '.')
            git('commit', '-qm', 'base')
            baseline = git('rev-parse', 'HEAD')
            source.write_text('head', encoding='utf-8')
            git('add', '.')
            git('commit', '-qm', 'head')
            head = git('rev-parse', 'HEAD')
            commands = {name: {'argv':['python3','-c','print(0)'], 'timeout_sec':5}
                        for name in POLICY['obligations']}
            commands['docs-links']['argv'] = [
                'python3', '-c',
                'from pathlib import Path;Path(' + repr(str(source)) + ').write_text("dirty")']
            executor = {'schema_version':1, 'commands':commands}
            plan = p.git_plan(POLICY,gitroot,baseline,head,'candidate',executor)
            with self.assertRaisesRegex(p.PlanError, 'modified tracked'):
                p.execute(POLICY,executor,plan,'docs',root,'44','1',source_repo=gitroot)

    def test_untrusted_command_does_not_inherit_github_output_channels(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            trace = root/'seen.json'
            commands = {name: {'argv':['python3','-c', 'print("ok")'],
                               'timeout_sec':5} for name in POLICY['obligations']}
            commands['docs-links']['argv'] = ['python3', '-c',
                'import os,json;from pathlib import Path;Path(' + repr(str(trace)) +
                ').write_text(json.dumps({k:os.getenv(k) for k in '
                '["GITHUB_OUTPUT","GITHUB_ENV","ACTIONS_RUNTIME_TOKEN"]}))']
            executor={'schema_version':1,'commands':commands}
            plan=p.make_plan(POLICY,['docs/passive/guide.md'],BASE,HEAD,MB,
                             'candidate',executor)
            with mock.patch.dict(os.environ, {'GITHUB_OUTPUT':'/tmp/test-output',
                                             'GITHUB_ENV':'/tmp/test-env',
                                             'ACTIONS_RUNTIME_TOKEN':'not-a-real-token'}):
                p.execute(POLICY,executor,plan,'docs',root,'14','1')
            self.assertEqual(json.loads(trace.read_text()),{
                'GITHUB_OUTPUT':None,'GITHUB_ENV':None,
                'ACTIONS_RUNTIME_TOKEN':None})

    def test_workflow_requires_checkout_preflight_in_every_group(self):
        workflow = (ROOT / 'examples/classified-github-pr.yml').read_text(encoding='utf-8')
        self.assertEqual(workflow.count('--workdir . --repo work --group'), 4)
        self.assertNotIn('--workdir . --group ', workflow)

    def test_missing_command_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);executor={'schema_version':1,'commands':{}}
            for name in POLICY['obligations']:
                executor['commands'][name]={'argv':['bash',str(root/'missing.sh')], 'timeout_sec':5}
            doc=p.make_plan(POLICY,['docs/passive/manual.md'],BASE,HEAD,MB,'candidate',executor)
            with self.assertRaises(p.PlanError):
                p.execute(POLICY,executor,doc,'docs',root,'1','1')

    def test_failed_command_must_not_emit_success_receipt(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            exe={'schema_version':1,'commands':{}}
            for n in POLICY['obligations']:
                exe['commands'][n]={'argv':['python3','-c','raise SystemExit(5)'], 'timeout_sec':5}
            doc=p.make_plan(POLICY,['docs/passive/manual.md'],BASE,HEAD,MB,'candidate',exe)
            with self.assertRaises(p.PlanError):
                p.execute(POLICY,exe,doc,'docs',root,'1','1')

    def test_success_label_with_missing_obligation_proof_does_not_qualify(self):
        ex={'schema_version':1,'commands':{n:{'argv':['true'], 'timeout_sec':5}
                                           for n in POLICY['obligations']}}
        doc=p.make_plan(POLICY,['src/main.rs'],BASE,HEAD,MB,'candidate',ex)
        e={'schema_version':1,'jobs':{}}
        for group,want in doc['groups'].items():
            e['jobs'][group]={'result':'skipped','receipt':None}
            if want:
                e['jobs'][group]['result']='success'
                e['jobs'][group]['receipt']=p.receipt(doc,group,'1','1',[])
        with self.assertRaises(p.PlanError):
            p.qualify(POLICY,doc,e,doc,'1','1',ex)

    def test_tampered_executor_manifest_is_rejected(self):
        ex={'schema_version':1,'commands':{n:{'argv':['true'], 'timeout_sec':5}
                                           for n in POLICY['obligations']}}
        doc=p.make_plan(POLICY,['docs/passive/a.md'],BASE,HEAD,MB,'candidate',ex)
        changed=json.loads(json.dumps(ex))
        changed['commands']['docs-links']['argv']=['false']
        with self.assertRaises(p.PlanError):
            p.execute(POLICY,changed,doc,'docs',Path('.'),'1','1')
        with self.assertRaises(p.PlanError):
            p.qualify(POLICY,doc,{'schema_version':1,'jobs':{}},doc,'1','1',changed)

    def test_no_missing_execution_manifest_obligation_allowed(self):
        ex={'schema_version':1,'commands':{n:{'argv':['true'], 'timeout_sec':5}
                                           for n in POLICY['obligations']}}
        del ex['commands']['model-consumer']
        with self.assertRaises(p.PlanError):
            p.validate_executor(ex,POLICY)

    def test_workflow_actual_docs_job_and_final_gate_cover_all_groups(self):
        try:
            import yaml
        except ImportError:
            self.skipTest('Optional PyYAML needed for YAML syntax fixture')
        wf=yaml.safe_load((ROOT/'examples/classified-github-pr.yml').read_text())['jobs']
        self.assertTrue(set(('classify','docs','rust','model','trust','ci-policy-gate')).issubset(wf))
        self.assertEqual(set(wf['ci-policy-gate']['needs']),set(('classify','docs','rust','model','trust')))
        self.assertIn('always()',wf['ci-policy-gate']['if'])
        self.assertIn('rust',wf['model']['needs'])
        for name in ('docs','rust','model','trust'):
            script='\n'.join(x.get('run','') for x in wf[name]['steps'])
            self.assertIn('ci_plan.py execute',script)
            self.assertIn('--group '+name,script)
            self.assertIn('exec-policy.json',script)
        gate='\n'.join(x.get('run','') for x in wf['ci-policy-gate']['steps'])
        self.assertIn('ci_plan.py qualify',gate)
        self.assertIn('ci-evidence.json',gate)
        self.assertIn('--executor trusted/ci/exec-policy.json',gate)
        self.assertNotIn('pull_request_target',str(wf))

    def test_approval_rule_not_auto_created_for_protected_status(self):
        text=(ROOT/'examples/classified-github-pr.yml').read_text()
        self.assertIn('Stable branch-protection status',text)
        self.assertIn('release/production',text)
        self.assertNotIn('workflow_dispatch',text)

    def test_real_git_cli_end_to_end_documentation_job(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)
            def git(*args):
                return subprocess.check_output(['git','-C',str(root),*args],stderr=subprocess.DEVNULL).decode().strip()
            git('init','-q');git('config','user.name','Fixture');git('config','user.email','fixture@example.invalid')
            (root/'docs/passive').mkdir(parents=True)
            (root/'docs/passive/a.md').write_text('initial')
            git('add','.');git('commit','-qm','base');base=git('rev-parse','HEAD')
            (root/'docs/passive/a.md').write_text('updated')
            git('add','.');git('commit','-qm','head');head=git('rev-parse','HEAD')
            policy_path=root/'policy.json';policy_path.write_text(json.dumps(POLICY))
            ex={'schema_version':1,'commands':{n:{'argv':['python3','-c','print("ok")'], 'timeout_sec':5}
                                               for n in POLICY['obligations']}}
            executor_path=root/'executor.json';executor_path.write_text(json.dumps(ex))
            script=ROOT/'scripts/ci_plan.py'
            plan_file=root/'plan.json';ev_file=root/'evidence.json'
            subprocess.run(['python3',str(script),'plan','--repo',str(root),
                            '--policy',str(policy_path),'--executor',str(executor_path),
                            '--base',base,'--head',head,'--file',str(plan_file)],check=True,capture_output=True)
            doc=json.loads(plan_file.read_text())
            self.assertEqual(doc['obligations'],['docs-links','trust-policy'])
            receipts={}
            for group, enabled in doc['groups'].items():
                receipts[group]={'result':'skipped','receipt':None}
                if enabled:
                    proc=subprocess.run(['python3',str(script),'execute','--plan',str(plan_file),
                                         '--policy',str(policy_path),'--executor',str(executor_path),
                                         '--workdir',str(root),'--repo',str(root),'--group',group,
                                         '--run-id','123','--attempt','1'],
                                        check=True,capture_output=True,text=True)
                    receipts[group]={'result':'success','receipt':json.loads(proc.stdout)}
            ev_file.write_text(json.dumps({'schema_version':1,'jobs':receipts}))
            final=subprocess.run(['python3',str(script),'qualify','--repo',str(root),
                                  '--policy',str(policy_path),'--executor',str(executor_path),
                                  '--base',base,'--head',head,'--plan',str(plan_file),
                                  '--evidence',str(ev_file),'--run-id','123','--attempt','1'],
                                 check=True,capture_output=True,text=True)
            self.assertTrue(json.loads(final.stdout)['qualified'])
