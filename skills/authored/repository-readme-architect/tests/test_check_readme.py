"""Offline standard-library regression tests for README local checks."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]/'scripts'/'check_readme.py'
spec=importlib.util.spec_from_file_location('check_readme',SOURCE)
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class ReadmeAuditTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        self.main=self.root/'README.md'
    def put(self,path,content):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content,encoding='utf-8');return p
    def run_audit(self,text,baseline=None):
        self.put('README.md',text)
        return mod.audit(self.root,self.main,self.put('original.md',baseline) if baseline is not None else None)
    def stat(self,text):return self.run_audit(text)['counts']
    def cli(self,*args):
        return subprocess.run([sys.executable,str(SOURCE),'--root',str(self.root),*args],capture_output=True,text=True)


    def test_dense_pr_history_is_editorial_advisory_not_link_failure(self):
        text=('''# Project
A short project summary.

## Recent PRs
- Merged PR #101: updated the formatter
- Merged PR #102: added a helper
- Merged PR #103: refined the docs

## Getting started
Run the included example.
''')
        result=self.run_audit(text)
        self.assertEqual(result['counts']['CHRONOLOGICAL_LOG_ADVISORY'],1)
        self.assertEqual(result['local_blockers'],0)
        self.assertIs(result['editorial_advisories_are_blockers'],False)
        self.assertEqual(result['findings'][0]['line'],4)
        self.assertEqual(result['findings'][0]['kind'],'editorial')

    def test_sparse_single_pr_reference_is_not_history_log(self):
        counts=self.stat('# Project\n\n## Progress\n- See PR #101 for rationale\n')
        self.assertNotIn('CHRONOLOGICAL_LOG_ADVISORY',counts)

    def test_regular_quick_start_list_is_not_history_log(self):
        counts=self.stat('# Start here\n\n- Install\n- Run tests\n- Read the API reference\n')
        self.assertNotIn('CHRONOLOGICAL_LOG_ADVISORY',counts)

    def test_fenced_changelog_example_is_ignored(self):
        text='''# Project
## Recent PRs
```md
- Merged PR #101
- Merged PR #102
- Merged PR #103
```
'''
        self.assertNotIn('CHRONOLOGICAL_LOG_ADVISORY',self.stat(text))

    def test_changelog_heading_with_three_dated_entries_is_advisory(self):
        text='''# Tool
## Changelog
- 2026-11-01: Added CLI
- 2026-11-07: Refined CLI
- 2026-11-14: Changed CLI
'''
        self.assertEqual(self.stat(text)['CHRONOLOGICAL_LOG_ADVISORY'],1)

    def test_other_sections_do_not_inflate_log_threshold(self):
        text='''# Tool
## Recent PRs
- Merged PR #101
- Merged PR #102

## Architecture
- Merged PR #103
'''
        self.assertNotIn('CHRONOLOGICAL_LOG_ADVISORY',self.stat(text))

    def test_warning_does_not_fail_cli(self):
        self.put('README.md','''# Tool
## Recent PRs
- PR #101
- PR #102
- PR #103
''')
        outcome=self.cli()
        self.assertEqual(outcome.returncode,0,outcome.stderr)
        self.assertIn('CHRONOLOGICAL_LOG_ADVISORY',outcome.stdout)

    def test_multiple_log_sections_report_separately(self):
        text='''# Tool
## Progress log
- PR #101
- PR #102
- PR #103
## Latest updates
- PR #104
- PR #105
- PR #106
'''
        result=self.run_audit(text)
        self.assertEqual(result['counts']['CHRONOLOGICAL_LOG_ADVISORY'],2)
        self.assertEqual([x['line'] for x in result['findings']],[2,6])

    def test_existing_file(self):
        self.put('docs/guide.md','# Guide\n');self.assertEqual(self.stat('[Guide](docs/guide.md)')['LOCAL_FILE_EXISTS'],1)
    def test_existing_heading(self):
        self.put('docs/guide.md','# Quick Start\n');self.assertEqual(self.stat('[Guide](docs/guide.md#quick-start)')['LOCAL_ANCHOR_FOUND'],1)
    def test_missing_file(self):self.assertEqual(self.stat('[No](missing.md)')['BROKEN_LOCAL_FILE'],1)
    def test_missing_heading(self):
        self.put('docs/guide.md','# Guide\n');self.assertEqual(self.stat('[No](docs/guide.md#missing)')['BROKEN_LOCAL_ANCHOR'],1)
    def test_self_anchor(self):self.assertEqual(self.stat('# Install\n\n[Go](#install)')['LOCAL_ANCHOR_FOUND'],1)
    def test_duplicate_headings(self):
        self.assertEqual(self.stat('# Intro\n# Intro\n\n[Second](#intro-1)')['LOCAL_ANCHOR_FOUND'],1)
    def test_linked_reference(self):
        self.put('LICENSE','MIT');self.assertEqual(self.stat('[License][license]\n\n[license]: LICENSE')['LOCAL_FILE_EXISTS'],1)
    def test_missing_reference_definition(self):self.assertEqual(self.stat('[No][unknown]')['UNRESOLVED_REFERENCE_DEFINITION'],1)
    def test_fenced_false_link(self):
        self.assertNotIn('BROKEN_LOCAL_FILE',self.stat('```md\n[Bad](bad.md)\n```'))
    def test_inline_code_false_link(self):self.assertNotIn('BROKEN_LOCAL_FILE',self.stat('`[Bad](bad.md)`'))
    def test_image_missing(self):self.assertEqual(self.stat('![Logo](assets/no.png)')['BROKEN_LOCAL_FILE'],1)
    def test_image_existing(self):
        self.put('assets/a.png','asset');self.assertEqual(self.stat('![Logo](assets/a.png)')['LOCAL_FILE_EXISTS'],1)
    def test_percent_escaped_path(self):
        self.put('docs/A B.md','hi');self.assertEqual(self.stat('[A](docs/A%20B.md)')['LOCAL_FILE_EXISTS'],1)
    def test_query_is_not_file_path(self):
        self.put('docs/a.md','# A');self.assertEqual(self.stat('[A](docs/a.md?plain=1)')['LOCAL_FILE_EXISTS'],1)
    def test_remote_http_not_fetched(self):self.assertEqual(self.stat('[X](https://example.com/hello)')['EXTERNAL_NOT_CHECKED'],1)
    def test_mailto_not_fetched(self):self.assertEqual(self.stat('[X](mailto:a@b.com)')['EXTERNAL_NOT_CHECKED'],1)
    def test_js_unsafe_scheme(self):self.assertEqual(self.stat('[X](javascript:alert)')['UNSUPPORTED_SCHEME'],1)
    def test_url_secret_not_echoed(self):
        out=self.run_audit('[X](https://example.com?token=SHOULD_NOT_APPEAR)')
        self.assertEqual(out['counts']['SENSITIVE_QUERY_NOT_INSPECTED'],1)
        self.assertNotIn('SHOULD_NOT_APPEAR',json.dumps(out))
    def test_root_absolute_unknown(self):self.assertEqual(self.stat('[A](/docs/a.md)')['REPOSITORY_ROOT_ABSOLUTE_UNVERIFIED'],1)
    def test_escape_parent_blocked(self):self.assertEqual(self.stat('[A](../../secrets.txt)')['OUT_OF_SCOPE_PATH'],1)
    def test_case_sensitive_path(self):
        self.put('LICENSE','MIT');self.assertEqual(self.stat('[x](license)')['BROKEN_LOCAL_FILE'],1)
    def test_sibling_folder_from_nested_readme(self):
        self.put('docs/README.md','[go](../LICENSE)');self.put('LICENSE','MIT')
        out=mod.audit(self.root,self.root/'docs'/'README.md')
        self.assertEqual(out['counts'].get('LOCAL_FILE_EXISTS'),1)
    def test_symlink_target_blocked(self):
        target=self.put('real.txt','hello');link=self.root/'alias.txt'
        try:link.symlink_to(target)
        except (OSError,NotImplementedError):self.skipTest('symlink unavailable')
        self.assertEqual(self.stat('[x](alias.txt)')['SYMLINK_NOT_FOLLOWED'],1)
    def test_directory_unverified(self):
        self.put('docs/file.md','hi');self.assertEqual(self.stat('[Docs](docs/)')['DIRECTORY_ROUTING_NOT_CHECKED'],1)
    def test_setext_anchor_unverified(self):
        self.put('docs/a.md','Some Title\n==========\n');self.assertEqual(self.stat('[link](docs/a.md#some-title)')['ANCHOR_UNVERIFIED_COMPLEX_MARKDOWN'],1)
    def test_inline_markdown_heading_unverified(self):
        self.put('docs/a.md','# Guide [API](api.md)\n');self.assertEqual(self.stat('[link](docs/a.md#guide-api)')['ANCHOR_UNVERIFIED_COMPLEX_MARKDOWN'],1)
    def test_explicit_named_anchor(self):
        self.put('docs/a.md','<a id="test"></a>\n');self.assertEqual(self.stat('[link](docs/a.md#test)')['LOCAL_ANCHOR_FOUND'],1)
    def test_duplicate_generated_block_preserved(self):
        t='hello\n<!-- generated:begin -->\nunchanged\n<!-- generated:end -->\n'
        self.assertEqual(self.run_audit(t,t)['counts']['GENERATED_REGIONS_UNCHANGED'],1)
    def test_generated_block_modified(self):
        before='<!-- generated:begin -->\nX\n<!-- generated:end -->'
        after='<!-- generated:begin -->\nY\n<!-- generated:end -->'
        self.assertEqual(self.run_audit(after,before)['counts']['GENERATED_REGIONS_CHANGED'],1)
    def test_generated_block_removed(self):
        before='<!-- generated:begin -->\nX\n<!-- generated:end -->'
        self.assertEqual(self.run_audit('hello',before)['counts']['GENERATED_REGIONS_CHANGED'],1)
    def test_unbalanced_generated_block(self):self.assertEqual(self.stat('<!-- generated:begin -->')['MALFORMED_GENERATED_MARKERS'],1)
    def test_no_baseline_not_preservation_pass(self):
        self.assertEqual(self.stat('<!-- generated:begin -->\na\n<!-- generated:end -->')['GENERATED_BASELINE_NOT_SUPPLIED'],1)
    def test_no_generated_regions(self):self.assertEqual(self.stat('hello'),{})
    def test_readonly_flags(self):
        z=self.run_audit('hello');self.assertIs(z['source_authenticity_verified'],False)
        self.assertIs(z['external_links_tested'],False);self.assertIs(z['reader_success_verified'],False)
        self.assertIs(z['commands_executed'],False)
    def test_cli_exit_broken(self):
        self.put('README.md','[Bad](missing.md)');p=self.cli()
        self.assertEqual(p.returncode,1);self.assertIn('BROKEN_LOCAL_FILE',p.stdout)
    def test_cli_exit_valid(self):
        self.put('LICENSE','MIT');self.put('README.md','[MIT](LICENSE)')
        self.assertEqual(self.cli().returncode,0)
    def test_cli_refuses_missing_root(self):
        p=subprocess.run([sys.executable,str(SOURCE),'--root',str(self.root/'missing')],capture_output=True,text=True)
        self.assertEqual(p.returncode,2)
    def test_cli_refuses_outside_readme(self):
        self.put('README.md','Hi');self.assertEqual(self.cli('--readme','../out.md').returncode,2)
    def test_cli_refuses_symlink_readme(self):
        original=self.put('real.md','hi');link=self.root/'README.md'
        try:link.symlink_to(original)
        except (OSError,NotImplementedError):self.skipTest('symlink unavailable')
        self.assertEqual(self.cli().returncode,2)
    def test_cli_refuses_symlink_directory(self):
        outside=self.root/'real';outside.mkdir();(outside/'README.md').write_text('hi')
        link=self.root/'sub'
        try:link.symlink_to(outside,target_is_directory=True)
        except (OSError,NotImplementedError):self.skipTest('symlink unavailable')
        self.assertEqual(self.cli('--readme','sub/README.md').returncode,2)
    def test_cli_refuses_big_readme(self):
        self.put('README.md','x'*(mod.MAX_BYTES+1));self.assertEqual(self.cli().returncode,2)
    def test_cli_stable_json(self):
        self.put('README.md','[x](missing)');a=self.cli().stdout;b=self.cli().stdout
        self.assertEqual(a,b)
    def test_multiple_links(self):
        self.put('LICENSE','text');out=self.run_audit('[a](LICENSE) and [b](oops)')
        self.assertEqual(out['counts']['BROKEN_LOCAL_FILE'],1)
        self.assertEqual(out['counts']['LOCAL_FILE_EXISTS'],1)
    def test_nested_parentheses_not_false_broken(self):
        self.assertEqual(self.stat('[x](file(1).md)')['COMPLEX_LINK_SYNTAX_NOT_CHECKED'],1)
    def test_non_markdown_anchor_not_called_broken(self):
        self.put('index.html','<h1>Title</h1>')
        self.assertEqual(self.stat('[x](index.html#title)')['ANCHOR_UNVERIFIED_NON_MARKDOWN'],1)
    def test_generated_markers_in_code_fence_ignored(self):
        self.assertEqual(self.stat('```md\n<!-- generated:begin -->\n```'),{})
    def test_local_escape_is_cli_blocker(self):
        self.put('README.md','[x](../../secret)');self.assertEqual(self.cli().returncode,1)
    def test_unsafe_scheme_is_cli_blocker(self):
        self.put('README.md','[x](javascript:alert)');self.assertEqual(self.cli().returncode,1)
    def test_generated_markers_in_fence_do_not_change_baseline(self):
        base='<!-- generated:begin -->\nA\n<!-- generated:end -->'
        text=base+'\n```md\n<!-- generated:begin -->\n```'
        self.assertEqual(self.run_audit(text,base)['counts']['GENERATED_REGIONS_UNCHANGED'],1)
    def test_binary_image_fragment_not_unicode_error(self):
        (self.root/'photo.png').write_bytes(bytes([0x89,0x50,0x4e,0x47,0xff]))
        self.assertEqual(self.stat('[image](photo.png#section)')['ANCHOR_UNVERIFIED_NON_MARKDOWN'],1)
    def test_invalid_utf8_readme_fails_closed(self):
        (self.root/'README.md').write_bytes(b'\xff\xfe')
        self.assertEqual(self.cli().returncode,2)
    def test_generated_marker_line_internal_content_preserved(self):
        base='A\n<!-- generated:begin -->\nB\n<!-- generated:end -->\nC'
        edit='Rewritten intro\n<!-- generated:begin -->\nB\n<!-- generated:end -->\nUpdated outro'
        self.assertEqual(self.run_audit(edit,base)['counts']['GENERATED_REGIONS_UNCHANGED'],1)
    def test_line_reporting(self):
        z=self.run_audit('heading\n\n[x](missing)')
        self.assertEqual(z['findings'][0]['line'],3)

if __name__=='__main__':unittest.main()

class CompleteWorkflowExercises(unittest.TestCase):
    """Actual bounded CREATE and UPLIFT artifact exercises, not external user tests."""
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)
        self.example=SOURCE.parent.parent/'examples'/'create-python-library-output.md'
    def put(self,path,data):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(data,encoding='utf-8');return p
    def test_create_without_existing_readme_source_compatible(self):
        # A source tree exists, but README does not. Create and execute one
        # demonstrably source-compatible path without pip/network access.
        self.put('pyproject.toml','[project]\nname = "safestrip"\nrequires-python = ">=3.11"\n')
        self.put('src/safestrip/__init__.py','')
        self.put('src/safestrip/format.py','def clean(value: str) -> str:\n    return value.strip()\n')
        self.put('tests/test_format.py','import unittest\nfrom safestrip.format import clean\nclass Example(unittest.TestCase):\n def test_clean(self):\n  self.assertEqual(clean(" a "),"a")\n')
        self.assertFalse((self.root/'README.md').exists())
        text=self.example.read_text('utf-8')
        readme=self.put('README.md',text)
        result=mod.audit(self.root,readme)
        self.assertEqual(result['local_blockers'],0)
        self.assertIn('Run from a source checkout',text)
        self.assertNotIn('pip install -e',text)
        # This exact sample command was executed in the isolated controlled tree.
        import os
        env=os.environ.copy();env['PYTHONPATH']='src'
        outcome=subprocess.run([sys.executable,'-c',"from safestrip.format import clean; print(clean(' a '))"],cwd=self.root,env=env,text=True,capture_output=True)
        self.assertEqual(outcome.returncode,0,outcome.stderr)
        self.assertEqual(outcome.stdout,'a\n')
        tests=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=self.root,env=env,text=True,capture_output=True)
        self.assertEqual(tests.returncode,0,tests.stderr)
        self.assertIn('OK',tests.stderr)
    def test_uplift_preserves_generated_bytes_and_validates_local_navigation(self):
        old='''# Example\n\n<!-- generated:begin -->\n| Version | Asset |\n| --- | --- |\n| 0.1 | release.bin |\n<!-- generated:end -->\n\nSee docs.\n'''
        new='''# Example\n\nUse Example to inspect deterministic local files.\n\n[Getting started](docs/quickstart.md)\n\n<!-- generated:begin -->\n| Version | Asset |\n| --- | --- |\n| 0.1 | release.bin |\n<!-- generated:end -->\n\nRelease identities in the generated block are historical and must be authenticated independently.\n'''
        self.put('docs/quickstart.md','# Getting started\n')
        oldfile=self.put('old.md',old)
        newfile=self.put('README.md',new)
        result=mod.audit(self.root,newfile,oldfile)
        self.assertEqual(result['local_blockers'],0)
        self.assertEqual(result['counts']['GENERATED_REGIONS_UNCHANGED'],1)
        self.assertEqual(result['counts']['LOCAL_FILE_EXISTS'],1)
        self.assertFalse(result['readme_claims_verified'])
    def test_verifier_does_not_claim_external_release_verified(self):
        readme=self.put('README.md','# Example\n\nWindows installer available.\n\n[Installer](https://example.org/installer.exe)')
        result=mod.audit(self.root,readme)
        self.assertEqual(result['counts']['EXTERNAL_NOT_CHECKED'],1)
        self.assertFalse(result['readme_claims_verified'])
        self.assertFalse(result['external_links_tested'])

class EmptyRepositoryExercise(unittest.TestCase):
    def test_no_source_readme_has_no_fabricated_quickstart(self):
        text=(SOURCE.parent.parent/'examples'/'empty-repository-output.md').read_text('utf-8')
        self.assertIn('no verified command',text.lower())
        self.assertNotIn('pip install ',text)
        self.assertNotIn('npm install',text)
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); (root/'README.md').write_text(text,encoding='utf-8')
            result=mod.audit(root,root/'README.md')
            self.assertEqual(result['local_blockers'],0)
            self.assertFalse(result['readme_claims_verified'])
