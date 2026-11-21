import importlib.util
import hashlib
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
        self.put('README.md','# Guide\n\nImportant constraints remain exactly here.\n')
        p=self.run_audit(baseline='before.md')['preservation_audit']
        self.assertEqual(p['missing_dispositions'],0)
        self.assertEqual(p['section_findings'][0]['state'],'RETAINED_EXACT_SECTION')
    def test_removed_section_without_disposition_blocks(self):
        self.put('before.md','# Intro\n\nCritical compatibility information.\n## Limits\n\nWindows build is not released.\n')
        z=self.run_audit(baseline='before.md')
        self.assertEqual(z['preservation_audit']['missing_dispositions'],2)
        self.assertEqual(z['README_delivery_preflight'],'BLOCKED')
    def test_unchanged_code_content_detected(self):
        self.put('before.md','# Setup\n\n```sh\npython -m app --safe\n```\n')
        self.put('README.md','# Setup\n\n```sh\npython -m app --safe\n```\n')
        z=self.run_audit(baseline='before.md')['preservation_audit']
        self.assertEqual(z['missing_dispositions'],0)
    def test_changed_warning_heading_with_same_body_blocks(self):
        self.put('before.md','# Product\n\nOverview.\n## Experimental\n\nWorks only on development builds.\n')
        self.put('README.md','# Product\n\nOverview.\n## Production-ready\n\nWorks only on development builds.\n')
        result=self.run_audit(baseline='before.md')
        p=result['preservation_audit']
        self.assertEqual(p['baseline_sections'],2)
        self.assertEqual(p['missing_dispositions'],1)
        self.assertEqual(p['section_findings'][1]['state'],'MISSING_DISPOSITION')
        self.assertEqual(result['README_delivery_preflight'],'BLOCKED')

    def test_heading_only_warning_is_preserved_and_deletion_detected(self):
        old='# Product\n\n## Not production-ready\n'
        self.put('before.md',old);self.put('README.md',old)
        p=self.run_audit(baseline='before.md')['preservation_audit']
        self.assertEqual(p['baseline_sections'],2)
        self.assertEqual(p['missing_dispositions'],0)
        self.assertEqual(p['section_findings'][1]['state'],'RETAINED_EXACT_SECTION')
        self.put('README.md','# Product\n')
        p=self.run_audit(baseline='before.md')['preservation_audit']
        self.assertEqual(p['baseline_sections'],2)
        self.assertEqual(p['missing_dispositions'],1)

    def test_heading_level_change_requires_disposition(self):
        self.put('before.md','# Example\n\n## Experimental\n\nLimited preview.\n')
        self.put('README.md','# Example\n\n### Experimental\n\nLimited preview.\n')
        self.assertEqual(self.run_audit(baseline='before.md')['preservation_audit']['missing_dispositions'],1)

    def test_heading_replaced_by_prose_does_not_count_as_section(self):
        self.put('before.md','## Experimental\n\nDo not deploy.\n')
        self.put('README.md','# Summary\n\nExperimental Do not deploy.\n')
        self.assertEqual(self.run_audit(baseline='before.md')['preservation_audit']['missing_dispositions'],1)

    def test_heading_only_parent_with_unchanged_child_is_flagged(self):
        self.put('before.md','# Product\n\n## Experimental\n### Linux\n\nAvailable.\n')
        self.put('README.md','# Product\n\n## Stable\n### Linux\n\nAvailable.\n')
        p=self.run_audit(baseline='before.md')['preservation_audit']
        self.assertEqual(p['baseline_sections'],3)
        self.assertEqual(p['missing_dispositions'],1)
        self.assertEqual(p['section_findings'][2]['state'],'RETAINED_EXACT_SECTION')

    def test_body_only_legacy_manifest_hash_is_stale(self):
        old='# Experimental\n\nNot production-ready.\n'
        self.put('before.md',old)
        self.put('README.md','# Available\n\nNot production-ready.\n')
        legacy_hash=mod._hash(mod._norm(mod._sections(old)[0]['body']))
        self.obj('plan.json',{'schema_version':1,'sections':[{
            'section_id':'s1','original_sha256':legacy_hash,
            'disposition':'OUTDATED','evidence_ref':'release-evidence'}]})
        p=self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']
        self.assertEqual(p['section_findings'][0]['state'],'STALE_DISPOSITION_SOURCE_HASH')

    def test_relocated_body_with_changed_warning_heading_is_not_proven(self):
        old='# Experimental\n\nOnly development builds are supported.\n'
        self.put('before.md',old)
        self.put('README.md','# Public release\n\nAvailable for installation.\n')
        self.put('docs/release.md','# Stable\n\nOnly development builds are supported.\n')
        digest=mod._hash(mod._section_text(mod._sections(old)[0]))
        self.obj('plan.json',{'schema_version':1,'sections':[{
            'section_id':'s1','original_sha256':digest,'disposition':'RELOCATED',
            'evidence_ref':'manual-qualification','destination':'docs/release.md'}]})
        p=self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']
        self.assertEqual(p['section_findings'][0]['state'],'RELOCATION_NOT_PROVEN')
        self.assertEqual(p['unresolved_removals'],1)

    def test_section_digest_changes_when_only_heading_changes(self):
        old=mod._sections('# Experimental\n\nSame body.\n')[0]
        new=mod._sections('# Production-ready\n\nSame body.\n')[0]
        self.assertNotEqual(mod._hash(mod._section_text(old)),mod._hash(mod._section_text(new)))
        self.assertEqual(mod._norm(old['body']),mod._norm(new['body']))

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
        sha=mod._hash(mod._section_text(mod._sections(old)[0]))
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':sha,'disposition':'OUTDATED','evidence_ref':'release-assets-2026-11'}]})
        p=self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']
        self.assertEqual(p['missing_dispositions'],0)
        self.assertEqual(p['manual_evidence_reviews'],1)
        self.assertFalse(p['semantic_preservation_authenticated'])
    def test_unverified_disposition_blocks(self):
        old='# Title\n\nHistorical signing keys are documented here.\n'
        self.put('before.md',old)
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._section_text(mod._sections(old)[0])),'disposition':'UNVERIFIED','evidence_ref':'missing-source'}]})
        self.assertIn('UNVERIFIED_SECTION_REMOVAL',self.run_audit(baseline='before.md',dispositions='plan.json')['blockers'])
    def test_retained_label_does_not_pass_deleted_text(self):
        old='# Title\n\nA unique compatibility limitation.\n'
        self.put('before.md',old)
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._section_text(mod._sections(old)[0])),'disposition':'RETAINED','evidence_ref':'reviewer'}]})
        p=self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']
        self.assertEqual(p['section_findings'][0]['state'],'RETENTION_NOT_PROVEN')
        self.assertEqual(p['unresolved_removals'],1)
    def test_relocation_requires_destination(self):
        old='# Title\n\nUnique technical instruction from documentation.\n'
        self.put('before.md',old)
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._section_text(mod._sections(old)[0])),'disposition':'RELOCATED','evidence_ref':'docs/guide.md'}]})
        with self.assertRaises(mod.Invalid):self.run_audit(baseline='before.md',dispositions='plan.json')
    def test_relocation_exact_text_recognized_not_fully_proven(self):
        old='# Title\n\nUnique technical instruction from documentation.\n'
        self.put('before.md',old);self.put('docs/guide.md','# Title\n\nUnique technical instruction from documentation.\n')
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._section_text(mod._sections(old)[0])),'disposition':'RELOCATED','evidence_ref':'docs/guide.md','destination':'docs/guide.md'}]})
        p=self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']
        self.assertEqual(p['section_findings'][0]['state'],'RELOCATION_SECTION_PRESENT_REVIEW_REQUIRED')
        self.assertFalse(p['semantic_preservation_authenticated'])
    def test_relocation_missing_text_not_proven(self):
        old='# Title\n\nUnique technical instruction from documentation.\n'
        self.put('before.md',old);self.put('docs/guide.md','# Details\n\nNothing related.\n')
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._section_text(mod._sections(old)[0])),'disposition':'RELOCATED','evidence_ref':'docs/guide.md','destination':'docs/guide.md'}]})
        self.assertEqual(self.run_audit(baseline='before.md',dispositions='plan.json')['preservation_audit']['unresolved_removals'],1)
    def test_malicious_relocation_outside_root_rejected(self):
        old='# Title\n\nUnique technical instruction from documentation.\n'
        self.put('before.md',old)
        self.obj('plan.json',{'schema_version':1,'sections':[{'section_id':'s1','original_sha256':mod._hash(mod._section_text(mod._sections(old)[0])),'disposition':'RELOCATED','evidence_ref':'external','destination':'../outside.md'}]})
        with self.assertRaises(mod.Invalid):self.run_audit(baseline='before.md',dispositions='plan.json')

    def generated_fixture(self):
        readme='<!-- generated by docs-maker -->\n# Generated README\n\nOnly tested on Linux.\n'
        source='def build():\n    return "generated"\n'
        template='# Generated README\n\nOnly tested on Linux.\n'
        self.put('README.md',readme)
        self.put('tools/make_readme.py',source)
        self.put('templates/README.md.tmpl',template)
        sha=lambda text: hashlib.sha256(text.encode('utf-8')).hexdigest()
        evidence={
            'schema_version':1,
            'generator_source':{'path':'tools/make_readme.py','sha256':sha(source)},
            'templates':[{'path':'templates/README.md.tmpl','sha256':sha(template)}],
            'output_sha256':sha(readme),
            'candidate_head_sha':HEAD,
            'drift_check_name':'README output parity',
            'ci_evidence_ref':'run-123-exact-head',
        }
        ci={
            'schema_version':1,'head_sha':HEAD,'required_checks_known':True,
            'checks':[{'name':'README output parity','required':True,'status':'completed',
                       'conclusion':'success','category':'documentation'}]
        }
        self.obj('generated.json',evidence)
        self.obj('ci.json',ci)
        return evidence,ci

    def generated_audit(self):
        return self.run_audit('AUDIT',generated_evidence='generated.json',
                              ci_receipt='ci.json',head_sha=HEAD)

    def test_generated_no_evidence_stays_hold(self):
        self.generated_fixture()
        z=self.run_audit('AUDIT')
        self.assertIn('GENERATED_README_OWNERSHIP_UNRESOLVED',z['blockers'])
        self.assertEqual(z['generated_ownership']['evidence_review']['state'],'NOT_SUPPLIED')

    def test_matching_pins_and_recorded_drift_are_review_ready_not_approved(self):
        self.generated_fixture()
        z=self.generated_audit()
        o=z['generated_ownership']
        self.assertEqual(o['owner_status'],'GENERATED_EVIDENCE_PENDING_HUMAN_REVIEW')
        self.assertEqual(z['README_delivery_preflight'],'BLOCKED')
        self.assertIn('GENERATED_README_HUMAN_AUTHENTICATION_REQUIRED',z['blockers'])
        self.assertNotIn('GENERATED_README_OWNERSHIP_UNRESOLVED',z['blockers'])
        self.assertTrue(o['evidence_review']['source_template_pins_match'])
        self.assertTrue(o['evidence_review']['output_digest_match'])
        self.assertTrue(o['evidence_review']['ci_drift_recorded_success'])
        self.assertTrue(o['evidence_review']['human_review_required'])
        self.assertFalse(o['evidence_review']['ownership_clearance_granted'])
        self.assertFalse(o['evidence_review']['generator_execution_authenticated'])
        self.assertFalse(o['evidence_review']['ci_receipt_authenticated'])
        self.assertFalse(z['repository_merge_ready'])

    def test_changed_template_digest_blocks_evidence(self):
        self.generated_fixture()
        self.put('templates/README.md.tmpl','# Replaced template\n')
        z=self.generated_audit()
        self.assertEqual(z['generated_ownership']['owner_status'],'GENERATED_OWNERSHIP_HOLD')
        self.assertIn('SOURCE_OR_TEMPLATE_DIGEST_MISMATCH',
                      z['generated_ownership']['evidence_review']['issues'])
        self.assertEqual(z['README_delivery_preflight'],'BLOCKED')

    def test_generated_output_digest_mismatch_blocks(self):
        self.generated_fixture()
        self.put('README.md','<!-- generated by docs-maker -->\n# Altered generated output\n')
        z=self.generated_audit()
        self.assertIn('GENERATED_OUTPUT_DIGEST_MISMATCH',
                      z['generated_ownership']['evidence_review']['issues'])
        self.assertIn('GENERATED_README_OWNERSHIP_UNRESOLVED',z['blockers'])

    def test_stale_head_pin_blocks(self):
        evidence,_=self.generated_fixture()
        evidence['candidate_head_sha']='b'*40
        self.obj('generated.json',evidence)
        z=self.generated_audit()
        self.assertIn('EVIDENCE_HEAD_MISMATCH',z['generated_ownership']['evidence_review']['issues'])

    def test_missing_drift_check_blocks_even_with_other_green(self):
        evidence,ci=self.generated_fixture()
        ci['checks'][0]['name']='unrelated green'
        self.obj('ci.json',ci)
        z=self.generated_audit()
        self.assertIn('REQUIRED_DRIFT_CHECK_NOT_RECORDED_SUCCESSFUL',
                      z['generated_ownership']['evidence_review']['issues'])

    def test_skipped_drift_check_cannot_clear_safeguard(self):
        evidence,ci=self.generated_fixture()
        ci['checks'][0]['conclusion']='skipped'
        self.obj('ci.json',ci)
        z=self.generated_audit()
        self.assertEqual(z['generated_ownership']['owner_status'],'GENERATED_OWNERSHIP_HOLD')

    def test_receipt_wrong_head_does_not_qualify(self):
        evidence,ci=self.generated_fixture()
        ci['head_sha']='b'*40
        self.obj('ci.json',ci)
        z=self.generated_audit()
        self.assertIn('DRIFT_CI_RECEIPT_MISSING_OR_INCOMPLETE',
                      z['generated_ownership']['evidence_review']['issues'])

    def test_unverified_self_approval_field_is_rejected(self):
        evidence,_=self.generated_fixture()
        evidence['generator_execution_authenticated']=True
        self.obj('generated.json',evidence)
        with self.assertRaises(mod.Invalid):
            self.generated_audit()

    def test_symlinked_template_evidence_refused(self):
        self.generated_fixture()
        target=self.root/'templates/README.md.tmpl'
        target.unlink()
        try:
            target.symlink_to(self.root/'tools/make_readme.py')
        except (OSError,NotImplementedError):
            self.skipTest('symlinks not supported')
        with self.assertRaises(mod.Invalid):
            self.generated_audit()

    def test_unsafe_template_path_refused(self):
        evidence,_=self.generated_fixture()
        evidence['templates'][0]['path']='../external.md'
        self.obj('generated.json',evidence)
        with self.assertRaises(mod.Invalid):
            self.generated_audit()

    def test_generator_self_references_readme_rejected(self):
        evidence,_=self.generated_fixture()
        evidence['generator_source']={'path':'README.md','sha256':evidence['output_sha256']}
        self.obj('generated.json',evidence)
        with self.assertRaises(mod.Invalid):
            self.generated_audit()

    def test_generated_evidence_without_owner_marker_is_not_automatic_clearance(self):
        self.generated_fixture()
        self.put('README.md','# Ordinary source README\n')
        z=self.generated_audit()
        self.assertIn('GENERATED_EVIDENCE_WITHOUT_EXPLICIT_OWNERSHIP_MARKER',z['blockers'])

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
