"""Anonymized artifact-wait negative controls; never authenticates live CI."""
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
spec = importlib.util.spec_from_file_location('ci_repair_preflight_artifact', SCRIPT)
repair = importlib.util.module_from_spec(spec)
spec.loader.exec_module(repair)
FIXTURE = ROOT / 'examples' / 'ci-artifact-wait-fixture.json'


def scenario():
    return json.loads(FIXTURE.read_text())


class ArtifactWaitCases(unittest.TestCase):
    def check(self, data=None):
        state = repair.assess(scenario() if data is None else data)
        self.assertFalse(state['optimization_complete'])
        self.assertFalse(state['host_authenticated'])
        self.assertEqual(state['observed_runner_minutes_delta'], 'NOT_MEASURED')
        self.assertEqual(state['observed_critical_path_delta'], 'NOT_MEASURED')
        return state

    def test_shared_artifact_wait_not_test_computation(self):
        state = self.check()
        self.assertEqual(state['status'], 'STRUCTURAL_PASS')
        phase = state['phase_analysis']
        self.assertEqual(phase['dominant_phase'], 'dependency_wait')
        self.assertEqual(phase['phase_timings']['dependency_wait']['total_seconds'], 3490)
        self.assertEqual(phase['phase_timings']['test_execution']['total_seconds'], 13)
        self.assertEqual(phase['phase_timings']['compile']['total_seconds'], 110)
        self.assertEqual(phase['dominant_reported_critical_phase'], 'dependency_wait')
        self.assertFalse(state['artifact_dependency_analysis']['provider_authenticated'])
        self.assertEqual(state['artifact_dependency_analysis']['claimed_runner_occupied_wait_seconds'], 3490)

    def test_two_waiting_consumers_are_dependency_wait_not_shareable_setup(self):
        state = self.check()
        findings = [x for x in state['phase_analysis']['overlap_findings']
                    if x['operation'] == 'poll-shared-output']
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]['classification'], 'DEPENDENCY_WAIT')
        self.assertFalse(findings[0]['removal_authorized'])
        self.assertEqual(len(state['artifact_dependency_analysis']['diagnostics']), 2)

    def test_job_scheduler_must_delay_runner_allocation(self):
        data = scenario()
        data['artifact_schedules'][0]['routes'][0]['needs_producer_for'] = []
        data['artifact_schedules'][0]['routes'][0]['runner_allocated_while_waiting_for'] = ['case1']
        issues = self.check(data)['issues']
        self.assertIn('CONSUMER_MISSING_PRODUCER_NEEDS:full', issues)
        self.assertIn('PAID_RUNNER_WAITS_FOR_ARTIFACT:full', issues)

    def test_producer_failure_must_block_required_full_verification(self):
        data = scenario()
        data['artifact_schedules'][0]['routes'][0]['producer_failure_blocks'] = False
        self.assertIn('PRODUCER_FAILURE_NOT_PROPAGATED:full', self.check(data)['issues'])
        data = scenario()
        data['artifact_schedules'][0]['producer_status'] = 'failed'
        self.assertIn('ARTIFACT_PRODUCER_NOT_SUCCESSFUL:built-fixture-H', self.check(data)['issues'])

    def test_artifact_custody_must_match_run_and_revision(self):
        data = scenario()
        data['artifact_schedules'][0]['routes'][0]['artifact_custody'] = 'cross-run-cache'
        self.assertIn('CROSS_RUN_ARTIFACT_CUSTODY:full', self.check(data)['issues'])
        data = scenario()
        data['artifact_schedules'][0]['producer_run_id'] = 'run-old'
        self.assertIn('WAIT_ARTIFACT_UNMATCHED:case1-artifact-wait', self.check(data)['issues'])
        data = scenario()
        data['artifact_schedules'][0]['producer_revision'] = 'stale-head'
        self.assertIn('ARTIFACT_SOURCE_STALE:built-fixture-H', self.check(data)['issues'])

    def test_producer_skipped_legitimate_lightweight_consumers_must_run(self):
        data = scenario()
        alt = data['artifact_schedules'][0]['routes'][1]
        self.assertEqual(self.check(data)['status'], 'STRUCTURAL_PASS')
        alt['consumers_scheduled'] = []
        self.assertIn('LEGITIMATE_CONSUMER_SKIPPED:lightweight', self.check(data)['issues'])

    def test_unconditional_needs_on_skipped_producer_is_regression(self):
        data = scenario()
        data['artifact_schedules'][0]['routes'][1]['needs_producer_for'] = ['case1', 'case2']
        self.assertIn('SKIPPED_PRODUCER_UNCONDITIONAL_NEEDS:lightweight', self.check(data)['issues'])

    def test_alternate_path_requires_independent_fallback(self):
        data = scenario()
        data['artifact_schedules'][0]['routes'][1].pop('fallback_verification')
        self.assertIn('ALTERNATE_VERIFICATION_MISSING:lightweight', self.check(data)['issues'])
        data = scenario()
        data['artifact_schedules'][0]['routes'] = data['artifact_schedules'][0]['routes'][:1]
        self.assertIn('ARTIFACT_PATH_COVERAGE_INCOMPLETE:built-fixture-H', self.check(data)['issues'])

    def test_artifact_timestamps_required_before_declaring_dependency_wait(self):
        data = scenario()
        data['phase_observations'][-1]['seconds'] = 400
        self.assertIn('WAIT_DURATION_INCONSISTENT:case2-artifact-wait', self.check(data)['issues'])
        data = scenario()
        data['phase_observations'][-1]['available_at_s'] = 10
        self.assertIn('ARTIFACT_TIMELINE_INVALID:case2-artifact-wait', self.check(data)['issues'])
        data = scenario()
        data['artifact_schedules'][0]['producer_available_at_s'] = 1810
        self.assertIn('ARTIFACT_AVAILABILITY_MISMATCH:case1-artifact-wait', self.check(data)['issues'])

    def test_wait_records_require_corresponding_schedule(self):
        data = scenario()
        data.pop('artifact_schedules')
        issues = self.check(data)['issues']
        self.assertIn('ARTIFACT_SCHEDULE_MISSING', issues)
        self.assertIn('WAIT_ARTIFACT_UNMATCHED:case1-artifact-wait', issues)

    def test_synthetic_full_fixture_cli_reports_no_measured_benefit(self):
        proc = subprocess.run([sys.executable, str(SCRIPT), '--input', str(FIXTURE)],
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        report = json.loads(proc.stdout)
        self.assertEqual(report['phase_analysis']['dominant_phase'], 'dependency_wait')
        self.assertEqual(report['artifact_dependency_analysis']['measured_runner_minutes_saved'], 'NOT_MEASURED')
        self.assertFalse(report['optimization_complete'])


if __name__ == '__main__':
    unittest.main()
