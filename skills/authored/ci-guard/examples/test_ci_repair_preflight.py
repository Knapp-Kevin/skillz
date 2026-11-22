"""Anonymous self-repair / phase-cost adversarial tests. No CI provider execution."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'ci_repair_preflight.py'
spec = importlib.util.spec_from_file_location('ci_repair_preflight', SCRIPT)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


def phase(id, kind, op, fingerprint, seconds, *, immutable=False, mutates=False,
          isolation='none', unique=False, assertion='not-applicable', equivalent=False,
          on_critical_path=False):
    return {'id': id, 'kind': kind, 'operation': op, 'fingerprint': fingerprint,
            'seconds': seconds, 'revision': 'revision-H', 'platform': 'linux-pinned',
            'environment': 'ubuntu-24.04', 'run_id': 'synthetic-run-1',
            'on_critical_path': on_critical_path,
            'trust_boundary': 'candidate-readonly', 'assertion': assertion,
            'immutable': immutable, 'mutates': mutates, 'isolation': isolation,
            'equivalence_proven': equivalent, 'unique_detection': unique}


def fixture():
    return {
        'schema_version': 1, 'source_revision': 'revision-H',
        'inventory': {'complete': True, 'nested_graph_traced': True,
                      'normative_specs_inspected': True, 'branch_rules_inspected': True,
                      'workflows': ['acceptance', 'standalone', 'release'],
                      'unresolved_paths': []},
        'repair': {'mode': 'CI_SELF_REPAIR',
                   'stages': ['DISCOVER', 'PREPARE', 'PROVE', 'CUTOVER', 'OBSERVE', 'ROLLBACK'],
                   'one_coordinated_change': True, 'draft_preparation': True,
                   'readiness': dict.fromkeys(('source', 'workflow', 'tests', 'policy',
                                               'negative_controls', 'rollback'), True),
                   'readiness_head': 'revision-H',
                   'planned_expensive_cycles': 1, 'max_expensive_cycles': 1,
                   'forecast': [
                       {'event': 'draft', 'selected_jobs': 0, 'expensive': False,
                        'inputs_revision': 'revision-H'},
                       {'event': 'ready', 'selected_jobs': 4, 'expensive': True,
                        'approval': 'owner-authorized', 'inputs_revision': 'revision-H'},
                       {'event': 'release', 'selected_jobs': 3, 'expensive': True,
                        'approval': 'owner-authorized', 'inputs_revision': 'revision-H'},
                   ],
                   'old_unconditional_paths': 0,
                   'cheap_preflight_result': 'success', 'cheap_preflight_head': 'revision-H',
                   'normative_required': ['format', 'model', 'native-security', 'release-signing'],
                   'candidate_selected': ['format', 'model', 'native-security', 'release-signing'],
                   'release_selected': ['format', 'model', 'native-security', 'release-signing'],
                   'protected_statuses': ['format', 'model', 'native-security'],
                   'change_classes': ['docs'], 'authorized_policy_migration': False,
                   'full_qualification': True, 'merge_qualified_from_draft': False},
        'phase_observations': [
            phase('case1-compile', 'compile', 'compile-tests', 'bin-H', 50,
                  immutable=True),
            phase('case2-compile', 'compile', 'compile-tests', 'bin-H', 60,
                  immutable=True),
            phase('case1-fixture', 'setup', 'construct-project', 'immutable-fixture-H', 300,
                  immutable=True),
            phase('case2-fixture', 'setup', 'construct-project', 'immutable-fixture-H', 320,
                  immutable=True),
            phase('case1-test', 'test_execution', 'native-conformance', 'baseline-H', 2200,
                  unique=True, assertion='assert-proof-one', on_critical_path=True),
            phase('case2-test', 'test_execution', 'native-conformance', 'baseline-H', 2300,
                  unique=True, assertion='assert-proof-two', on_critical_path=True),
            phase('case1-mutate', 'setup', 'copy-mutable-project', 'mutating-fixture-H', 100,
                  mutates=True, isolation='fresh-directory'),
            phase('case2-mutate', 'setup', 'copy-mutable-project', 'mutating-fixture-H', 110,
                  mutates=True, isolation='fresh-directory'),
        ]}


class SelfRepairTests(unittest.TestCase):
    def evaluate(self, data=None):
        result = p.assess(fixture() if data is None else data)
        self.assertFalse(result['optimization_complete'])
        self.assertFalse(result['host_authenticated'])
        self.assertEqual(result['observed_runner_minutes_delta'], 'NOT_MEASURED')
        self.assertEqual(result['observed_critical_path_delta'], 'NOT_MEASURED')
        return result

    def test_baseline_detects_real_case_execution_dominates_compile(self):
        result = self.evaluate()
        self.assertEqual(result['status'], 'STRUCTURAL_PASS')
        by_kind = result['phase_analysis']['phase_timings']
        self.assertEqual(by_kind['compile']['total_seconds'], 110)
        self.assertEqual(by_kind['test_execution']['total_seconds'], 4500)
        self.assertEqual(by_kind['test_execution']['p50_seconds'], 2300)
        self.assertEqual(by_kind['test_execution']['p90_seconds'], 2300)
        self.assertEqual(result['phase_analysis']['dominant_phase'], 'test_execution')
        self.assertEqual(result['phase_analysis']['dominant_reported_critical_phase'],
                         'test_execution')
        self.assertEqual(by_kind['test_execution']['reported_critical_path_seconds'], 4500)

    def test_draft_fanout_prevents_inherited_full_matrix(self):
        data = fixture()
        data['repair']['forecast'][0]['selected_jobs'] = 48
        data['repair']['forecast'][0]['expensive'] = True
        self.assertIn('DRAFT_EXPENSIVE_FANOUT', self.evaluate(data)['issues'])

    def test_missing_readiness_and_repair_staging_block_proof(self):
        data = fixture()
        data['repair']['readiness']['negative_controls'] = False
        self.assertIn('READINESS_MISSING:negative_controls', self.evaluate(data)['issues'])
        data = fixture()
        data['repair']['one_coordinated_change'] = False
        self.assertIn('PREPARE_NOT_BOUNDED_AND_CHEAP', self.evaluate(data)['issues'])

    def test_repeated_immutable_setup_vs_mutated_fresh_setup(self):
        findings = self.evaluate()['phase_analysis']['overlap_findings']
        cls = {f['operation']: f['classification'] for f in findings}
        self.assertEqual(cls['construct-project'], 'REPEATED_IMMUTABLE_SETUP')
        self.assertEqual(cls['copy-mutable-project'], 'JUSTIFIED_ISOLATION')
        self.assertFalse(any(f['removal_authorized'] for f in findings))

    def test_unique_test_assertions_do_not_become_duplicate_checks(self):
        findings = self.evaluate()['phase_analysis']['overlap_findings']
        detection = [f for f in findings if f['operation'] == 'native-conformance'][0]
        self.assertEqual(detection['classification'], 'UNIQUE_DETECTION')

    def test_unknown_setup_equivalence_is_unproven(self):
        data = fixture()
        for op in data['phase_observations']:
            if op['operation'] == 'construct-project':
                op['immutable'] = False
        findings = self.evaluate(data)['phase_analysis']['overlap_findings']
        self.assertEqual(next(f for f in findings if f['operation']=='construct-project')['classification'],
                         'UNPROVEN')

    def test_recorded_duplicate_same_revision_still_not_auto_removed(self):
        data = fixture()
        for op in data['phase_observations']:
            if op['operation'] == 'construct-project':
                op['immutable'] = False
                op['equivalence_proven'] = True
        finding = next(f for f in self.evaluate(data)['phase_analysis']['overlap_findings']
                       if f['operation'] == 'construct-project')
        self.assertEqual(finding['classification'], 'REDUNDANT_SAME_REVISION')
        self.assertFalse(finding['removal_authorized'])

    def test_job_reduction_without_critical_path_proof_cannot_claim_savings(self):
        result = self.evaluate()
        self.assertEqual(result['observed_critical_path_delta'], 'NOT_MEASURED')
        self.assertFalse(result['optimization_complete'])

    def test_old_unconditional_workflow_stops_cutover(self):
        data = fixture()
        data['repair']['old_unconditional_paths'] = 1
        self.assertIn('OLD_UNCONDITIONAL_PATH_REMAINS', self.evaluate(data)['issues'])

    def test_normative_release_checks_survive_even_if_branch_protection_removed(self):
        data = fixture()
        data['repair']['protected_statuses'] = []
        data['repair']['release_selected'].remove('release-signing')
        self.assertIn('NORMATIVE_RELEASE_CHECK_REMOVED', self.evaluate(data)['issues'])

    def test_draft_ready_same_sha_has_fresh_cheap_preflight(self):
        data = fixture()
        data['repair']['merge_qualified_from_draft'] = True
        self.assertIn('DRAFT_NOT_QUALIFIED', self.evaluate(data)['issues'])
        data = fixture()
        data['repair']['cheap_preflight_head'] = 'old-H'
        self.assertIn('CHEAP_CHECK_MISSING_OR_STALE', self.evaluate(data)['issues'])

    def test_policy_or_workflow_edit_defaults_to_full_protected_plan(self):
        data = fixture()
        data['repair']['change_classes'] = ['policy']
        data['repair']['full_qualification'] = False
        self.assertIn('RISKY_POLICY_CHANGE_REQUIRES_FULL_OR_AUTHORIZED_MIGRATION',
                      self.evaluate(data)['issues'])

    def test_fanout_unknown_or_missing_events_fails(self):
        data = fixture()
        data['repair']['forecast'] = data['repair']['forecast'][:2]
        self.assertIn('FANOUT_EVENTS_INCOMPLETE', self.evaluate(data)['issues'])
        data = fixture()
        data['repair']['forecast'][1]['approval'] = 'UNKNOWN'
        self.assertIn('FANOUT_NOT_ACKNOWLEDGED:ready', self.evaluate(data)['issues'])

    def test_multiple_expensive_repair_cycles_require_readiness_and_limit(self):
        data = fixture()
        data['repair']['planned_expensive_cycles'] = 5
        self.assertIn('UNBOUNDED_EXPENSIVE_REVALIDATION', self.evaluate(data)['issues'])

    def test_missing_source_inventories_fail_closed(self):
        data = fixture()
        data['inventory']['nested_graph_traced'] = False
        self.assertIn('INCOMPLETE_EXECUTION_INVENTORY', self.evaluate(data)['issues'])
        data = fixture()
        data['inventory']['normative_specs_inspected'] = False
        self.assertIn('GOVERNANCE_SOURCES_NOT_INSPECTED', self.evaluate(data)['issues'])

    def test_json_duplicate_and_symlinked_manifest_refused(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            path = root/'manifest.json'
            path.write_text('{"schema_version":1,"schema_version":1}')
            proc = subprocess.run([sys.executable, str(SCRIPT), '--input', str(path)],
                                  capture_output=True, text=True)
            self.assertEqual(proc.returncode, 2)
            self.assertIn('duplicate JSON key', proc.stderr)
            path.write_text(json.dumps(fixture()))
            link = root/'alias.json'
            link.symlink_to(path)
            proc = subprocess.run([sys.executable, str(SCRIPT), '--input', str(link)],
                                  capture_output=True, text=True)
            self.assertEqual(proc.returncode, 2)
            self.assertIn('linked input', proc.stderr)

    def test_cli_fixture_returns_structural_pass_but_no_host_authentication(self):
        path = ROOT/'examples'/'ci-self-repair-fixture.json'
        doc = json.loads(path.read_text())
        self.assertEqual(self.evaluate(doc)['status'], 'STRUCTURAL_PASS')
        proc = subprocess.run([sys.executable, str(SCRIPT), '--input', str(path)],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertFalse(json.loads(proc.stdout)['optimization_complete'])


if __name__ == '__main__':
    unittest.main()
