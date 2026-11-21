import importlib.util
from pathlib import Path
import copy
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('metrics',ROOT/'scripts/compare_ci_runs.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def run(run_id, job_minutes, seconds):
    return {'run_id':str(run_id),'attempt':1,'head':'1'*40,
            'scenario':'passive-docs','runner_profile':'ubuntu-large','cache_class':'cold',
            'protected_status':'success','jobs':[{
            'name':'required-gate','needs':[],'started_at':'2026-11-20T00:00:00Z',
            'completed_at':'2026-11-20T00:00:%02dZ'%seconds,
            'billed_runner_minutes':job_minutes,'result':'success'}]}

class MeasuredBudgetTests(unittest.TestCase):
    def test_paired_actual_receipts_compute_billed_and_critical_separately(self):
        payload={'schema_version':1,'pairs':[{'baseline':run(1,9,50),'optimized':run(2,3,20)}]}
        result=m.compare(payload)
        self.assertEqual(result['sum_runner_minutes_saved'],6)
        self.assertEqual(result['median_critical_seconds_saved'],30)
        self.assertIn('NOT_EXTERNALLY_AUTHENTICATED',result['provenance'])

    def test_missing_or_unpaired_data_is_not_a_saving(self):
        with self.assertRaises(m.EvidenceError):m.compare({'schema_version':1,'pairs':[]})
        with self.assertRaises(m.EvidenceError):m.compare({'schema_version':1,'pairs':[{'baseline':run(1,9,50)}]})

    def test_different_cache_platform_revision_not_comparable(self):
        for key,value in [('head','2'*40),('cache_class','warm'),('runner_profile','windows')]:
            bad=run(2,3,20);bad[key]=value
            with self.subTest(key=key),self.assertRaises(m.EvidenceError):
                m.compare({'schema_version':1,'pairs':[{'baseline':run(1,9,50),'optimized':bad}]})

    def test_missing_billed_minutes_and_failed_gate_refused(self):
        for key,value in [('billed_runner_minutes',None),('result','skipped')]:
            bad=run(1,9,50);bad['jobs'][0][key]=value
            with self.subTest(key=key),self.assertRaises(m.EvidenceError):
                m.compare({'schema_version':1,'pairs':[{'baseline':bad,'optimized':run(2,3,20)}]})

    def test_same_run_duplicated_refused(self):
        with self.assertRaises(m.EvidenceError):
            m.compare({'schema_version':1,'pairs':[{'baseline':run(1,9,50),'optimized':run(1,3,20)}]})


class CriticalPathIntegrityTests(unittest.TestCase):
    def test_parallel_jobs_are_not_summed_as_critical_path(self):
        baseline = run(1, 9, 50)
        extra = dict(baseline['jobs'][0])
        extra['name'] = 'parallel-docs'
        extra['billed_runner_minutes'] = 4
        baseline['jobs'].append(extra)
        result=m.summarize_run(baseline)
        self.assertEqual(result['critical_path_seconds'],50)
        self.assertEqual(result['qualification_elapsed_seconds'],50)
        self.assertEqual(result['billed_runner_minutes'],13)

    def test_missing_cross_workflow_dependency_is_not_an_accepted_critical_path(self):
        baseline=run(1,9,50)
        baseline['jobs'][0]['needs']=['other-workflow-required-check']
        with self.assertRaises(m.EvidenceError):
            m.summarize_run(baseline)

    def test_job_graph_cycle_is_refused(self):
        baseline=run(1,9,50)
        baseline['jobs'][0]['needs']=['required-gate']
        with self.assertRaises(m.EvidenceError):
            m.summarize_run(baseline)
