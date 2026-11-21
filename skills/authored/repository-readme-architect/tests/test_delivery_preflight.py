import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SRC=Path(__file__).resolve().parents[1]/'scripts'/'delivery_preflight.py'
spec=importlib.util.spec_from_file_location('delivery_preflight',SRC)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
HEAD='a'*40

class DeliveryPreflightTests(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup)
        self.root=Path(self.t.name)
        self.put('README.md','# Example\n\nWorking setup instructions.\n')
    def put(self,path,text):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(text,encoding='utf-8');return p
    def obj(self,path,data):return self.put(path,json.dumps(data))
    def run_audit(self,mode='UPLIFT',**kwargs):
        return mod.audit(self.root,'README.md',mode,**kwargs)
    def cli(self,*extra):
        return subprocess.run([sys.executable,str(SRC),'--root',str(self.root),'--mode','UPLIFT',*extra],capture_output=True,text=True)
    def test_prettier_and_markdownlint_and_vale_discovery(self):
        for p in ('.prettierrc','.markdownlint.yaml','.vale.ini','.editorconfig'):self.put(p,'{}')
        z=self.run_audit('AUDIT')['formatter_preflight']
        self.assertEqual(set(z['discovered']),{'prettier','markdownlint','vale','editorconfig'})
        self.assertEqual(z['local_validation'],'NOT_RUN')
        self.assertFalse(z['configs_executed'])
    def test_package_script_name_only_not_code_execution(self):
        self.obj('package.json',{'scripts':{'lint:docs':'touch exploit_marker','test':'echo fine'}})
        z=self.run_audit('AUDIT')['formatter_preflight']['discovered']
        self.assertEqual(z['package_scripts'][0]['name'],'lint:docs')
        self.assertFalse((self.root/'exploit_marker').exists())
    def test_invalid_package_json_does_not_crash(self):
        self.put('package.json','{')
        self.assertIn('package_json',self.run_audit('AUDIT')['formatter_preflight']['discovered'])
    def test_symlinked_formatter_is_not_followed(self):
        outside=self.put('config.txt','do not execute')
        try:(self.root/'.prettierrc').symlink_to(outside)
        except (OSError,NotImplementedError):self.skipTest('no symlink')
        z=self.run_audit('AUDIT')['formatter_preflight']['discovered']['prettier'][0]
        self.assertEqual(z['state'],'SYMLINK_CONFIG_NOT_READ')
    def test_uplift_must_have_baseline(self):
        self.assertIn('BASELINE_REQUIRED_FOR_UPLIFT',self.run_audit()['blockers'])
    def test_create_no_baseline_required(self):
        self.assertNotIn('BASELINE_REQUIRED_FOR_UPLIFT',self.run_audit('CREATE')['blockers'])
    def test_unchanged_sections_retained(self):
        self.put('before.md','# Guide\n\nImportant constraints remain exactly here.\n')
        self.put('README.md','# New name\n\nImportant constraints remain exactly here.\n')
        p=self.run_audit(baseline='before.md')['preservation_audit']
        self.assertEqual(p['missing_dispositions'],0)
        self.assertEqual(p['section_findings'][0]['state'],'RETAINED_EXACT_BODY')
    def test_removed_section_without_disposition_blocks(self):
        self.put('before.md','# Intro\n\nCritical compatibility information.\n## Limits\n\nWindows build is not released.\n')
        z=self.run_audit(baseline='before.md')
        self.assertEqual(z['preservation_audit']['missing_dispositions'],2)
        self.assertEqual(z['README_delivery_preflight'],'BLOCKED')
    def test_unchanged_code_content_detected(self):
        self.put('before.md','# Setup\n\n```sh\npython -m app --safe\n```\n')
        self.put('README.md','# New setup\n\n```sh\npython -m app --safe\n```\n')
        z=self.run_audit(baseline='before.md')['preservation_audit']
        self.assertEqual(z['missing_dispositions'],0)
    def test_heading_inside_fenced_content_does_not_split(self):
        a=mod._sections('# Heading\n\n```md\n# Not a heading\n```\nUse responsibly.\n')
        self.assertEqual(len(a),1)
    def test_section_hash_stable_after_whitespace_only(self):
        self.assertEqual(mod._hash(mod._norm(' alpha\n beta')),
                         mod._hash(mod._norm('alpha beta')))
    def test_stale_manifest_hash_rejected(self):
        self.put('before.md','# Intro\n\nSafety considerations.\n')
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':'0'*64,'disposition':'OUTDATED','evidence_ref':'issue-123'}]})
        p=self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']
        self.assertEqual(p['section_findings'][0]['state'],'STALE_DISPOSITION_SOURCE_HASH')
    def test_unknown_id_manifest_rejected(self):
        self.put('before.md','# Intro\n\nSafety considerations.\n')
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s100','original_sha256':'0'*64,'disposition':'OUTDATED','evidence_ref':'issue-123'}]})
        with self.assertRaises(mod.Invalid):self.run_audit(baseline='before.md',dispositions='plan.json')
    def test_proper_outdated_disposition_still_manual_review(self):
        old='# Intro\n\nUnreleased Windows installer is available.\n'
        self.put('before.md',old)
        sha=mod._hash(mod._norm(mod._sections(old)[0]['body']))
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':sha,'disposition':'OUTDATED','evidence_ref':'release-assets-2026-11'}]})
        p=self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']
        self.assertEqual(p['missing_dispositions'],0)
        self.assertEqual(p['manual_evidence_reviews'],1)
        self.assertFalse(p['semantic_preservation_authenticated'])
    def test_unverified_disposition_blocks(self):
        old='# Title\n\nHistorical signing keys are documented here.\n'
        self.put('before.md',old)
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._norm(mod._sections(old)[0]['body'])),'disposition':'UNVERIFIED','evidence_ref':'missing-source'}]})
        self.assertIn('UNVERIFIED_SECTION_REMOVAL',self.run_audit(baseline='before.md',dispositions='plan.json')['blockers'])
    def test_retained_label_does_not_pass_deleted_text(self):
        old='# Title\n\nA unique compatibility limitation.\n'
        self.put('before.md',old)
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._norm(mod._sections(old)[0]['body'])),'disposition':'RETAINED','evidence_ref':'reviewer'}]})
        p=self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']
        self.assertEqual(p['section_findings'][0]['state'],'RETENTION_NOT_PROVEN')
        self.assertEqual(p['unresolved_removals'],1)
    def test_relocation_requires_destination(self):
        old='# Title\n\nUnique technical instruction from documentation.\n'
        self.put('before.md',old)
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._norm(mod._sections(old)[0]['body'])),'disposition':'RELOCATED','evidence_ref':'docs/guide.md'}]})
        with self.assertRaises(mod.Invalid):self.run_audit(baseline='before.md',dispositions='plan.json')
    def test_relocation_exact_text_recognized_not_fully_proven(self):
        old='# Title\n\nUnique technical instruction from documentation.\n'
        self.put('before.md',old);self.put('docs/guide.md','# Details\n\nUnique technical instruction from documentation.\n')
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._norm(mod._sections(old)[0]['body'])),'disposition':'RELOCATED','evidence_ref':'docs/guide.md','destination':'docs/guide.md'}]})
        p=self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']
        self.assertEqual(p['section_findings'][0]['state'],'RELOCATION_TEXT_PRESENT_REVIEW_REQUIRED')
        self.assertFalse(p['semantic_preservation_authenticated'])
    def test_relocation_missing_text_not_proven(self):
        old='# Title\n\nUnique technical instruction from documentation.\n'
        self.put('before.md',old);self.put('docs/guide.md','# Details\n\nNothing related.\n')
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._norm(mod._sections(old)[0]['body'])),'disposition':'RELOCATED','evidence_ref':'docs/guide.md','destination':'docs/guide.md'}]})
        self.assertEqual(self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']['unresolved_removals'],1)
    def test_malicious_relocation_outside_root_rejected(self):
        old='# Title\n\nUnique technical instruction from documentation.\n'
        self.put('before.md',old)
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._norm(mod._sections(old)[0]['body'])),'disposition':'RELOCATED','evidence_ref':'external','destination':'../outside.md'}]})
        with self.assertRaises(mod.Invalid):self.run_audit(baseline='before.md',dispositions='plan.json')
    def test_generated_root_owner_holds(self):
        self.put('README.md','<!-- AUTO-GENERATED by make readme -->\n# Product\nContent\n')
        z=self.run_audit('AUDIT')
        self.assertEqual(z['generated_ownership']['owner_status'],'GENERATED_OWNERSHIP_HOLD')
        self.assertIn('GENERATED_README_OWNERSHIP_UNRESOLVED',z['blockers'])
    def test_fenced_generator_snippet_not_actual_ownership(self):
        self.put('README.md','```md\n<!-- AUTO-GENERATED -->\n```\n# Real\ncontent\n')
        self.assertEqual(self.run_audit('AUDIT')['generated_ownership']['owner_status'],'NO_EXPLICIT_GENERATOR_MARKER_FOUND')
    def test_uor_framework_plain_language_generated_footer_holds(self):
        self.put('README.md', '# UOR Framework\n\nGenerated content.\n\n*This README is machine-generated by `uor-docs`. Do not edit by hand.*\n')
        z=self.run_audit('AUDIT')
        self.assertEqual(z['generated_ownership']['owner_status'],'GENERATED_OWNERSHIP_HOLD')
    def test_generated_footer_inside_code_fence_is_example_not_owner(self):
        self.put('README.md', '```md\n*This README is machine-generated by `uor-docs`. Do not edit by hand.*\n```\n')
        self.assertEqual(self.run_audit('AUDIT')['generated_ownership']['owner_status'],'NO_EXPLICIT_GENERATOR_MARKER_FOUND')
    def test_baseline_cannot_be_the_candidate_itself(self):
        with self.assertRaises(mod.Invalid):self.run_audit(baseline='README.md')
    def test_no_generated_marker_does_not_prove_manual_ownership(self):
        self.assertFalse(self.run_audit('AUDIT')['generated_ownership']['generator_source_verified'])
    def test_required_ci_failure_blocks(self):
        c={'schema_version':1,'head_sha':HEAD,'required_checks_known':True,'checks':[{'name':'docs lint','required':True,'status':'completed','conclusion':'failure','category':'documentation'}]}
        self.obj('ci.json',c)
        z=self.run_audit('AUDIT',ci_receipt='ci.json',head_sha=HEAD)
        self.assertEqual(z['ci_delivery']['state'],'HOLD')
        self.assertTrue(z['ci_delivery']['blockers'])
    def test_nonrequired_full_ci_failure_is_separate_advisory(self):
        c={'schema_version':1,'head_sha':HEAD,'required_checks_known':True,'checks':[{'name':'full suite','required':False,'status':'completed','conclusion':'failure','category':'repository'},{'name':'docs lint','required':True,'status':'completed','conclusion':'success','category':'documentation'}]}
        self.obj('ci.json',c)
        z=self.run_audit('AUDIT',ci_receipt='ci.json',head_sha=HEAD)
        self.assertEqual(z['ci_delivery']['blockers'],[])
        self.assertEqual(len(z['ci_delivery']['advisories']),1)
        self.assertFalse(z['repository_merge_ready'])
    def test_unknown_required_checks_never_green(self):
        c={'schema_version':1,'head_sha':HEAD,'required_checks_known':False,'checks':[]}
        self.obj('ci.json',c)
        self.assertIn('REQUIRED_GATE_INVENTORY_UNVERIFIED',self.run_audit('AUDIT',ci_receipt='ci.json',head_sha=HEAD)['ci_delivery']['blockers'])
    def test_pending_required_ci_blocked(self):
        c={'schema_version':1,'head_sha':HEAD,'required_checks_known':True,'checks':[{'name':'docs','required':True,'status':'queued','conclusion':None,'category':'documentation'}]}
        self.obj('ci.json',c)
        self.assertEqual(self.run_audit('AUDIT',ci_receipt='ci.json',head_sha=HEAD)['ci_delivery']['state'],'HOLD')
    def test_skipped_required_ci_not_green(self):
        c={'schema_version':1,'head_sha':HEAD,'required_checks_known':True,'checks':[{'name':'docs','required':True,'status':'completed','conclusion':'skipped','category':'documentation'}]}
        self.obj('ci.json',c)
        self.assertEqual(self.run_audit('AUDIT',ci_receipt='ci.json',head_sha=HEAD)['ci_delivery']['state'],'HOLD')
    def test_stale_ci_head_rejected(self):
        self.obj('ci.json',{'schema_version':1,'head_sha':'b'*40,'required_checks_known':True,'checks':[]})
        self.assertFalse(self.run_audit('AUDIT',ci_receipt='ci.json',head_sha=HEAD)['ci_delivery']['head_match'])
    def test_nonmatching_ci_without_head_never_green(self):
        self.obj('ci.json',{'schema_version':1,'head_sha':HEAD,'required_checks_known':True,'checks':[]})
        self.assertFalse(self.run_audit('AUDIT',ci_receipt='ci.json')['ci_delivery']['head_match'])
    def test_duplicate_ci_names_rejected(self):
        row={'name':'ci','required':True,'status':'completed','conclusion':'success','category':'repository'}
        self.obj('ci.json',{'schema_version':1,'head_sha':HEAD,'required_checks_known':True,'checks':[row,row]})
        with self.assertRaises(mod.Invalid):self.run_audit('AUDIT',ci_receipt='ci.json',head_sha=HEAD)
    def test_duplicate_json_keys_rejected(self):
        self.put('ci.json','{"schema_version":1,"schema_version":1}')
        with self.assertRaises(mod.Invalid):self.run_audit('AUDIT',ci_receipt='ci.json')
    def test_nonfinite_json_rejected(self):
        self.put('ci.json','{"schema_version":NaN}')
        with self.assertRaises(mod.Invalid):self.run_audit('AUDIT',ci_receipt='ci.json')
    def test_ci_no_receipt_unverified(self):
        self.assertEqual(self.run_audit('AUDIT')['ci_delivery']['state'],'NOT_VERIFIED')
    def test_cli_invalid_baseline_reports_code_2(self):
        self.assertEqual(self.cli('--baseline','../private.md').returncode,2)
    def test_cli_missing_baseline_blocks(self):
        z=self.cli()
        self.assertEqual(z.returncode,1)
        self.assertIn('BASELINE_REQUIRED_FOR_UPLIFT',z.stdout)
    def test_cli_audit_no_write_and_no_oversold_pass(self):
        p=subprocess.run([sys.executable,str(SRC),'--root',str(self.root),'--mode','AUDIT'],capture_output=True,text=True)
        self.assertEqual(p.returncode,0)
        z=json.loads(p.stdout)
        self.assertFalse(z['writes_performed'])
        self.assertFalse(z['repository_merge_ready'])
        self.assertFalse(z['reader_outcome_verified'])
    def test_symlink_input_rejected(self):
        target=self.put('candidate.md','# Real')
        link=self.root/'linked.md'
        try: link.symlink_to(target)
        except (OSError,NotImplementedError):self.skipTest('no symlink')
        p=subprocess.run([sys.executable,str(SRC),'--root',str(self.root),'--mode','AUDIT','--readme','linked.md'],capture_output=True,text=True)
        self.assertEqual(p.returncode,2)
    def test_large_readme_rejected(self):
        self.put('README.md','x'*(mod.MAX_BYTES+1))
        self.assertEqual(subprocess.run([sys.executable,str(SRC),'--root',str(self.root),'--mode','AUDIT'],capture_output=True).returncode,2)
    def test_no_scope_escape_on_rooted_input(self):
        with self.assertRaises(mod.Invalid):mod._path(self.root,'/tmp/x')
    def test_cmd_always_bounded(self):
        self.assertFalse(self.run_audit('CREATE')['source_authenticity_verified'])

if __name__=='__main__':unittest.main()
