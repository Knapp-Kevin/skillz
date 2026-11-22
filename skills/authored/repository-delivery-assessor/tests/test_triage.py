"""Host-independent read-only behavior checks, not comparative skill-host A/B."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sp = importlib.util.spec_from_file_location('triage', ROOT / 'scripts' / 'triage.py')
engine = importlib.util.module_from_spec(sp)
sp.loader.exec_module(engine)


def base():
    return json.loads((ROOT / 'examples/pr816-public-source-snapshot.json').read_text(encoding='utf-8'))


def pr(doc):
    return doc['repositories'][0]['prs'][0]


def add_check(doc, name, state='success', sha=None):
    pr(doc)['checks'].append({'name':name, 'head_sha':sha or pr(doc)['head_sha'], 'conclusion':state})


class OfflinePulseTests(unittest.TestCase):
    def assert_invalid(self, mutator):
        doc=base();mutator(doc)
        with self.assertRaises(engine.InvalidInput):engine.triage(doc)
    def test_real_pr816_no_inferred_review_request(self):
        r=engine.triage(base())
        self.assertEqual(r['needs_you'],[])
        self.assertEqual(r['results'][0]['open_prs'][0]['required_check_gate'], 'REQUIRED_SET_NOT_VERIFIED')
        self.assertEqual(r['results'][0]['activity'],'UNKNOWN')
    def test_exact_head_socket_checks_preserved(self):
        d=engine.triage(base())['results'][0]['open_prs'][0]['check_evidence']
        self.assertEqual(d['Socket Security: Project Report']['at_head'],'SUCCESS')
        self.assertEqual(d['Socket Security: Pull Request Alerts']['at_head'],'SUCCESS')
    def test_does_not_claim_release_on_green_checks(self):
        self.assertFalse(engine.triage(base())['results'][0]['open_prs'][0]['release_or_user_outcome_verified'])
    def test_explicit_review_request_is_needs_you(self):
        d=base();pr(d)['review_requests']=['Knapp-Kevin']
        self.assertEqual(len(engine.triage(d)['needs_you']),1)
    def test_unrequested_open_pr_not_needs_you(self):
        d=base();pr(d)['review_requests']=['another-maintainer']
        self.assertEqual(engine.triage(d)['needs_you'],[])
    def test_draft_review_request_not_needs_you(self):
        d=base();pr(d)['review_requests']=['Knapp-Kevin'];pr(d)['draft']=True
        self.assertEqual(engine.triage(d)['needs_you'],[])
    def test_case_insensitive_operator_login(self):
        d=base();pr(d)['review_requests']=['knapp-kevin']
        self.assertEqual(len(engine.triage(d)['needs_you']),1)
    def test_stale_green_check_rejected(self):
        d=base();pr(d)['required_checks_verified']=True;pr(d)['checks_complete']=True
        pr(d)['required_checks']=['Socket Security: Project Report'];pr(d)['checks'][1]['head_sha']='a'*40
        p=engine.triage(d)['results'][0]['open_prs'][0]
        self.assertEqual(p['required_check_gate'],'REQUIRED_CHECK_UNVERIFIED')
        self.assertEqual(p['check_evidence']['Socket Security: Project Report']['at_head'],'STALE_ONLY')
    def test_current_required_failure_blocks(self):
        d=base();pr(d)['required_checks_verified']=True;pr(d)['checks_complete']=True
        pr(d)['required_checks']=['Socket Security: Project Report'];pr(d)['checks'][1]['conclusion']='failure'
        self.assertEqual(engine.triage(d)['results'][0]['open_prs'][0]['required_check_gate'],'REQUIRED_CHECK_FAILED')
    def test_current_required_timeout_blocks(self):
        d=base();pr(d)['required_checks_verified']=True;pr(d)['checks_complete']=True
        pr(d)['required_checks']=['Socket Security: Project Report'];pr(d)['checks'][1]['conclusion']='timed_out'
        self.assertEqual(engine.triage(d)['results'][0]['open_prs'][0]['required_check_gate'],'REQUIRED_CHECK_FAILED')
    def test_pending_stays_pending(self):
        d=base();pr(d)['required_checks_verified']=True;pr(d)['checks_complete']=True
        pr(d)['required_checks']=['Socket Security: Project Report'];pr(d)['checks'][1]['conclusion']='in_progress'
        self.assertEqual(engine.triage(d)['results'][0]['open_prs'][0]['required_check_gate'],'REQUIRED_CHECK_PENDING')
    def test_skipped_required_check_not_green(self):
        d=base();pr(d)['required_checks_verified']=True;pr(d)['checks_complete']=True
        pr(d)['required_checks']=['Socket Security: Project Report'];pr(d)['checks'][1]['conclusion']='skipped'
        self.assertEqual(engine.triage(d)['results'][0]['open_prs'][0]['required_check_gate'],'REQUIRED_CHECK_UNVERIFIED')
    def test_neutral_required_check_not_green(self):
        d=base();pr(d)['required_checks_verified']=True;pr(d)['checks_complete']=True
        pr(d)['required_checks']=['Socket Security: Project Report'];pr(d)['checks'][1]['conclusion']='neutral'
        self.assertEqual(engine.triage(d)['results'][0]['open_prs'][0]['required_check_gate'],'REQUIRED_CHECK_UNVERIFIED')
    def test_current_green_required_checks_only(self):
        d=base();pr(d)['required_checks_verified']=True;pr(d)['checks_complete']=True
        pr(d)['required_checks']=['Socket Security: Project Report','Socket Security: Pull Request Alerts']
        self.assertEqual(engine.triage(d)['results'][0]['open_prs'][0]['required_check_gate'],'REQUIRED_CHECKS_PASS_AT_HEAD_ONLY')
    def test_verified_empty_required_set_is_not_green(self):
        d=base();pr(d)["required_checks_verified"]=True;pr(d)["checks_complete"]=True
        self.assertEqual(engine.triage(d)["results"][0]["open_prs"][0]["required_check_gate"],"NO_REQUIRED_CHECKS_DEFINED")
    def test_required_set_unknown_never_proves_green(self):
        d=base();pr(d)['checks_complete']=True
        self.assertEqual(engine.triage(d)['results'][0]['open_prs'][0]['required_check_gate'],'REQUIRED_SET_NOT_VERIFIED')
    def test_incomplete_check_snapshot_not_green(self):
        d=base();pr(d)['required_checks_verified']=True;pr(d)['required_checks']=['Socket Security: Project Report']
        self.assertEqual(engine.triage(d)['results'][0]['open_prs'][0]['required_check_gate'],'CHECK_INVENTORY_INCOMPLETE')
    def test_duplicate_at_head_name_is_ambiguous(self):
        d=base();pr(d)['required_checks_verified']=True;pr(d)['checks_complete']=True
        pr(d)['required_checks']=['Socket Security: Project Report'];add_check(d,'Socket Security: Project Report')
        self.assertEqual(engine.triage(d)['results'][0]['open_prs'][0]['required_check_gate'],'REQUIRED_CHECK_UNVERIFIED')
    def test_missing_required_check_not_green(self):
        d=base();pr(d)['required_checks_verified']=True;pr(d)['checks_complete']=True
        pr(d)['required_checks']=['security-gate']
        self.assertEqual(engine.triage(d)['results'][0]['open_prs'][0]['required_check_gate'],'REQUIRED_CHECK_UNVERIFIED')
    def test_outside_allowlist_rejected(self):
        self.assert_invalid(lambda d:d['repositories'][0].update(name='private-org/unknown'))
    def test_missing_allowlist_repo_disclosed_without_data(self):
        d=base();d['authorized_repositories'].append('public-org/missing')
        self.assertEqual(engine.triage(d)['not_enumerated'],['public-org/missing'])
    def test_quiet_repo_threshold(self):
        d=base();d['repositories'][0]['last_push_utc']='2026-09-01T00:00:00Z'
        self.assertEqual(engine.triage(d)['quiet_repositories'],['Knapp-Kevin/skillz'])
    def test_recent_activity(self):
        d=base();d['repositories'][0]['last_push_utc']='2026-11-19T00:00:00Z'
        self.assertEqual(engine.triage(d)['results'][0]['activity'],'ACTIVE')
    def test_future_timestamp_not_assumed_activity(self):
        d=base();d['repositories'][0]['last_push_utc']='2027-01-01T00:00:00Z'
        self.assertEqual(engine.triage(d)['results'][0]['activity'],'FUTURE_TIMESTAMP_UNTRUSTED')
    def test_unqualified_local_state_always_not_checked(self):
        self.assertIn('LOCAL_WORKTREE_NOT_ASSESSED',engine.triage(base())['results'][0]['not_checked'])
    def test_incomplete_pr_enumeration_disclosed(self):
        self.assertIn('OPEN_PR_ENUMERATION_INCOMPLETE',engine.triage(base())['results'][0]['not_checked'])
    def test_no_implicit_empty_repo_full_coverage(self):
        d=base();d['repositories'][0]['prs']=[]
        self.assertIn('OPEN_PR_ENUMERATION_INCOMPLETE',engine.triage(d)['results'][0]['not_checked'])
    def test_duplicate_pr_rejected(self):
        self.assert_invalid(lambda d:d['repositories'][0]['prs'].append(copy.deepcopy(pr(d))))
    def test_duplicate_required_check_rejected(self):
        self.assert_invalid(lambda d:pr(d).update(required_checks=['security-gate','security-gate']))
    def test_duplicate_review_request_rejected(self):
        self.assert_invalid(lambda d:pr(d).update(review_requests=['user','user']))
    def test_malformed_sha_rejected(self):
        self.assert_invalid(lambda d:pr(d).update(head_sha='not-a-sha'))
    def test_unknown_check_status_rejected(self):
        self.assert_invalid(lambda d:pr(d)['checks'][0].update(conclusion='green'))
    def test_conflicting_input_field_rejected(self):
        self.assert_invalid(lambda d:pr(d).update(merge_now=True))
    def test_missing_as_of_utc_rejected(self):
        self.assert_invalid(lambda d:d.pop('as_of_utc'))
    def test_non_utc_time_rejected(self):
        self.assert_invalid(lambda d:d.update(as_of_utc='2026-11-20T13:20:00-05:00'))
    def test_private_source_text_cannot_direct_tools(self):
        self.assert_invalid(lambda d:pr(d)['checks'][0].update(do='send secret'))
    def test_cli_read_only_json_output(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'input.json';p.write_text(json.dumps(base()),encoding='utf8')
            before={f.name for f in Path(td).iterdir()}
            out=subprocess.run([sys.executable,str(ROOT/'scripts'/'triage.py'),'--input',str(p)],capture_output=True,text=True)
            self.assertEqual(out.returncode,0,out.stderr)
            self.assertEqual(json.loads(out.stdout)['needs_you'],[])
            self.assertEqual(before,{f.name for f in Path(td).iterdir()})
    def test_cli_rejects_duplicate_json_keys(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'input.json';p.write_text('{"schema_version":1,"schema_version":1}',encoding='utf8')
            out=subprocess.run([sys.executable,str(ROOT/'scripts'/'triage.py'),'--input',str(p)],capture_output=True,text=True)
            self.assertEqual(out.returncode,2)
    def test_cli_rejects_oversized_input(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'input.json';p.write_bytes(b' '* (engine.MAX_SIZE+1))
            out=subprocess.run([sys.executable,str(ROOT/'scripts'/'triage.py'),'--input',str(p)],capture_output=True,text=True)
            self.assertEqual(out.returncode,2)


    def test_cli_refuses_linked_input_file(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            private = root / "outside.json"
            private.write_text("out-of-scope sentinel", encoding="utf-8")
            alias = root / "approved.json"
            alias.symlink_to(private)
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "triage.py"), "--input", str(alias)],
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
                [sys.executable, str(ROOT / "scripts" / "triage.py"), "--input",
                 str(alias / "outside.json")], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 2)
            self.assertIn("symlinked input", proc.stderr)
            self.assertNotIn("out-of-scope sentinel", proc.stdout + proc.stderr)

if __name__ == '__main__':unittest.main()
