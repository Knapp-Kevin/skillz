"""Synthetic host reconciliation negative controls; no GitHub network actions."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import ci_host_reconcile as audit
import ci_scenario as sim

FIXTURE=ROOT/"examples"/"ci-scenario-fixture.json"
RUN=73
SHA="a"*40


def story():
    doc=json.loads(FIXTURE.read_text(encoding="utf8"))
    return sim.run(doc)


def mapping():
    return {
        "schema_version":1,"repository":"fictional-org/fictional-repo",
        "source_revision":SHA,"scenario_id":"postmerge-push",
        "design_id":"split-independent","expected_event":"push",
        "workflow_runs":[{
            "workflow":"forward","workflow_file":".github/workflows/forward.yml",
            "run_id":RUN,"attempt":1,"jobs":{"forward":"forward-port simulation"}}]}


def observed(run_id=RUN, event="push", outcome="success"):
    return {
        "schema_version":1,"repository":"fictional-org/fictional-repo",
        "workflow_runs":[{
            "attempt":1,
            "run":{"id":run_id,"head_sha":SHA,"event":event,
                   "status":"completed","conclusion":outcome,
                   "path":".github/workflows/forward.yml@refs/heads/main",
                   "run_attempt":1},
            "jobs":[{"id":991,"run_id":RUN,"name":"forward-port simulation",
                     "status":"completed","conclusion":outcome,
                     "started_at":"2026-11-22T12:00:10Z",
                     "completed_at":"2026-11-22T12:00:16Z"}]
        }]}


class HostEvidenceTests(unittest.TestCase):
    def test_host_run_job_reconciles_without_falsely_certifying_assurance(self):
        result=audit.reconcile(story(),mapping(),observed())
        self.assertEqual(result["status"],"HOST_JOB_RECONCILED")
        self.assertEqual(result["issues"],[])
        self.assertEqual(result["observed_executed_job_seconds"],6)
        self.assertEqual(result["observed_job_wall_envelope_seconds"],6)
        self.assertEqual(result["observation_provenance"],
                         "OBSERVED_AS_SUPPLIED_NOT_AUTHENTICATED")
        self.assertEqual(result["provider_dispatch_causality"],"NOT_VERIFIED")
        self.assertEqual(result["old_workflow_absence"],"NOT_VERIFIED")
        self.assertFalse(result["end_to_end_ci_qualified"])
        self.assertFalse(result["automatic_cutover_authorized"])

    def test_direct_host_fetch_reports_limited_live_observation_not_cutover(self):
        calls=[]
        o=observed()
        def fake(url,token):
            calls.append((url,token))
            if "/jobs?" in url:return {"jobs":o["workflow_runs"][0]["jobs"]}
            return o["workflow_runs"][0]["run"]
        result=audit.observe_live(mapping(),token="never-print-secret",getter=fake)
        self.assertEqual(result["workflow_runs"][0]["jobs"][0]["id"],991)
        self.assertEqual(len(calls),2)
        self.assertIn("/attempts/1",calls[0][0])
        self.assertTrue(all(url.startswith("https://api.github.com/repos/fictional-org/fictional-repo/actions/runs/73")
                            for url,_ in calls))
        self.assertIn("/attempts/1/jobs?per_page=100&page=1",calls[-1][0])
        report=audit.reconcile(story(),mapping(),result,live=True)
        self.assertEqual(report["observation_provenance"],"OBSERVED_GITHUB_API_DIRECT")
        self.assertFalse(report["end_to_end_ci_qualified"])

    def test_host_source_mismatch_is_hard_refusal(self):
        o=observed();o["workflow_runs"][0]["run"]["head_sha"]="b"*40
        with self.assertRaisesRegex(audit.Hold,"HOST_SOURCE_REVISION_MISMATCH"):
            audit.reconcile(story(),mapping(),o)

    def test_scenario_mapping_source_mismatch_is_refusal(self):
        m=mapping();m["source_revision"]="b"*40
        with self.assertRaisesRegex(audit.Hold,"source revision mismatches"):
            audit.reconcile(story(),m,observed())

    def test_provider_event_mismatch_is_refusal(self):
        with self.assertRaisesRegex(audit.Hold,"HOST_EVENT_MISMATCH"):
            audit.reconcile(story(),mapping(),observed(event="release"))


    def test_old_attempt_cannot_inherit_later_successful_rerun_conclusion(self):
        o=observed()
        o["workflow_runs"][0]["run"]["run_attempt"]=2
        with self.assertRaisesRegex(audit.Hold,"HOST_RUN_NOT_COMPLETED_OR_ATTEMPT_STALE"):
            audit.reconcile(story(),mapping(),o)

    def test_stale_or_incomplete_run_attempt_refused(self):
        for key,value in [("run_attempt",0),("status","in_progress")]:
            with self.subTest(key=key):
                o=observed();o["workflow_runs"][0]["run"][key]=value
                with self.assertRaises(audit.Hold):
                    audit.reconcile(story(),mapping(),o)

    def test_missing_job_holds_not_fake_success(self):
        o=observed();o["workflow_runs"][0]["jobs"]=[]
        x=audit.reconcile(story(),mapping(),o)
        self.assertEqual(x["status"],"HOLD")
        self.assertIn("MISSING_HOST_JOB:forward",x["issues"])

    def test_extra_unmapped_host_job_holds_and_discloses(self):
        o=observed()
        extra=copy.deepcopy(o["workflow_runs"][0]["jobs"][0])
        extra["id"]=992;extra["name"]="unmapped-signed-native"
        o["workflow_runs"][0]["jobs"].append(extra)
        x=audit.reconcile(story(),mapping(),o)
        self.assertEqual(x["status"],"HOLD")
        self.assertIn("UNMAPPED_OR_MISSING_HOST_JOBS:forward",x["issues"])

    def test_duplicate_provider_name_or_identity_refused(self):
        for change in ("name","id"):
            with self.subTest(change=change):
                o=observed()
                extra=copy.deepcopy(o["workflow_runs"][0]["jobs"][0])
                extra[change]=("different-name" if change=="name" else extra["id"])
                if change=="name": extra["id"]=992
                o["workflow_runs"][0]["jobs"].append(extra)
                if change=="name":
                    x=audit.reconcile(story(),mapping(),o)
                    self.assertEqual(x["status"],"HOLD")
                else:
                    with self.assertRaisesRegex(audit.Hold,"duplicate global provider job"):
                        audit.reconcile(story(),mapping(),o)

    def test_host_job_failure_is_not_synthetic_success(self):
        o=observed(outcome="failure")
        x=audit.reconcile(story(),mapping(),o)
        self.assertEqual(x["status"],"HOLD")
        self.assertIn("HOST_JOB_OUTCOME_DRIFT:forward",x["issues"])

    def test_skipped_and_pending_provider_jobs_cannot_become_green(self):
        for status,conclusion in (("completed","skipped"),("in_progress",None),
                                  ("completed","neutral")):
            with self.subTest(conclusion=conclusion):
                o=observed()
                j=o["workflow_runs"][0]["jobs"][0]
                j["status"]=status;j["conclusion"]=conclusion
                x=audit.reconcile(story(),mapping(),o)
                self.assertEqual(x["status"],"HOLD")


    def test_all_jobs_green_but_workflow_failed_is_not_success(self):
        o=observed()
        o["workflow_runs"][0]["run"]["conclusion"]="failure"
        x=audit.reconcile(story(),mapping(),o)
        self.assertEqual(x["status"],"HOLD")
        self.assertIn("HOST_WORKFLOW_OUTCOME_DRIFT:forward",x["issues"])

    def test_incomplete_workflow_conclusion_holds(self):
        o=observed()
        o["workflow_runs"][0]["run"]["conclusion"]=None
        x=audit.reconcile(story(),mapping(),o)
        self.assertEqual(x["status"],"HOLD")
        self.assertIn("HOST_WORKFLOW_INCOMPLETE_OR_UNSUPPORTED:forward",x["issues"])

    def test_workflow_file_identity_is_source_bound(self):
        o=observed();o["workflow_runs"][0]["run"]["path"]=".github/workflows/not-the-same.yml"
        with self.assertRaisesRegex(audit.Hold,"HOST_WORKFLOW_PATH_MISMATCH"):
            audit.reconcile(story(),mapping(),o)

    def test_duplicate_simulated_job_or_host_name_mapping_rejected(self):
        m=mapping()
        m["workflow_runs"][0]["jobs"]["second"]="forward-port simulation"
        with self.assertRaisesRegex(audit.Hold,"duplicate provider job"):
            audit.parse_mapping(m)
        m=mapping()
        m["workflow_runs"].append(copy.deepcopy(m["workflow_runs"][0]))
        with self.assertRaisesRegex(audit.Hold,"duplicate workflow"):
            audit.parse_mapping(m)

    def test_partial_simulator_or_manual_false_green_not_accepted(self):
        for change in ("pending","unqualified","forged"):
            with self.subTest(change=change):
                s=story()
                if change=="pending":s["status"]="HOLD"
                elif change=="unqualified":next(x for x in s["results"] if x["design"]=="split-independent" and x["scenario"]=="postmerge-push")["matches_expected"]=False
                else:s["host_execution_proven"]=True
                with self.assertRaises(audit.Hold):
                    audit.reconcile(s,mapping(),observed())

    def test_workflow_run_coverage_cannot_be_declared_without_actual_jobs(self):
        m=mapping();m["workflow_runs"][0]["jobs"]={"fake":"madeup"}
        with self.assertRaisesRegex(audit.Hold,"every scheduled normalized job"):
            audit.reconcile(story(),m,observed())

    def test_wrong_run_id_and_attempt_receipts_refused(self):
        with self.assertRaisesRegex(audit.Hold,"expected run/attempt absent"):
            audit.reconcile(story(),mapping(),observed(run_id=74))
        o=observed();o["workflow_runs"][0]["attempt"]=2
        with self.assertRaisesRegex(audit.Hold,"expected run/attempt absent"):
            audit.reconcile(story(),mapping(),o)

    def test_job_from_different_provider_run_refused(self):
        o=observed();o["workflow_runs"][0]["jobs"][0]["run_id"]=999
        with self.assertRaisesRegex(audit.Hold,"job attached to other run"):
            audit.reconcile(story(),mapping(),o)

    def test_missing_timestamps_not_savings_evidence(self):
        o=observed();o["workflow_runs"][0]["jobs"][0]["started_at"]=None
        x=audit.reconcile(story(),mapping(),o)
        self.assertEqual(x["status"],"HOLD")
        self.assertIsNone(x["observed_job_wall_envelope_seconds"])
        self.assertIn("HOST_JOB_TIMESTAMPS_MISSING:forward",x["issues"])

    def test_negative_duration_is_refused(self):
        o=observed();o["workflow_runs"][0]["jobs"][0]["completed_at"]="2026-11-22T11:00:16Z"
        with self.assertRaisesRegex(audit.Hold,"negative observed host duration"):
            audit.reconcile(story(),mapping(),o)

    def test_live_pagination_is_bounded_and_never_combines_attempts(self):
        calls=[]
        def fake(url,token):
            calls.append(url)
            if "/jobs?" not in url:return observed()["workflow_runs"][0]["run"]
            return {"jobs":[{"id":i} for i in range(100)]}
        with self.assertRaisesRegex(audit.Hold,"too many jobs"):
            audit.observe_live(mapping(),getter=fake)
        self.assertTrue(all("/attempts/1/jobs?" in x for x in calls[1:]))

    def test_invalid_repo_or_workflow_path_cannot_request_arbitrary_hosts(self):
        for badrepo in ("../evil", "org/..", "org/.", "./repo", "example.com/a/b", "a:b/c", "evil/../../escape"):
            with self.subTest(repo=badrepo):
                m=mapping();m["repository"]=badrepo
                with self.assertRaises(audit.Hold):
                    audit.parse_mapping(m)
        m=mapping();m["workflow_runs"][0]["workflow_file"]="../../secrets.yaml"
        with self.assertRaises(audit.Hold):
            audit.parse_mapping(m)

    def test_cli_offline_reads_synthetic_receipts_without_host_claims(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for name,data in (("s.json",story()),("m.json",mapping()),("o.json",observed())):
                (root/name).write_text(json.dumps(data),encoding="utf8")
            cmd=[sys.executable,str(ROOT/"scripts"/"ci_host_reconcile.py"),
                 "--simulator-results",str(root/"s.json"),
                 "--mapping",str(root/"m.json"),
                 "--observations",str(root/"o.json"),"--require-pass"]
            run=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            report=json.loads(run.stdout)
            self.assertEqual(report["status"],"HOST_JOB_RECONCILED")
            self.assertFalse(report["host_api_transport_verified_at_read"])
            self.assertEqual(report["provider_billed_minutes"],"NOT_MEASURED")

    def test_cli_offline_holds_on_mismatched_receipt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            bad=observed();bad["workflow_runs"][0]["jobs"]=[]
            for name,data in (("s.json",story()),("m.json",mapping()),("o.json",bad)):
                (root/name).write_text(json.dumps(data),encoding="utf8")
            run=subprocess.run([sys.executable,str(ROOT/"scripts"/"ci_host_reconcile.py"),
                   "--simulator-results",str(root/"s.json"),
                   "--mapping",str(root/"m.json"),
                   "--observations",str(root/"o.json"),"--require-pass"],
                   capture_output=True,text=True)
            self.assertEqual(run.returncode,3,run.stderr)

    def test_source_fixture_is_not_real_provider_evidence(self):
        report=audit.reconcile(story(),mapping(),observed())
        self.assertNotIn("PROVED",json.dumps(report))
        self.assertFalse(report["source_simulator_authenticated"])
        self.assertEqual(report["provider_dispatch_causality"],"NOT_VERIFIED")



def retry_story_and_mapping():
    """Completely fictional 3-job retry; numbers are not provider traces."""
    m=mapping()
    m["workflow_runs"][0]["attempt"]=2
    m["workflow_runs"][0]["jobs"]={
        "forward":"synthetic compile", "audit":"synthetic audit",
        "format":"synthetic format"
    }
    x=story()
    selected=next(z for z in x["results"] if
                  z["design"]==m["design_id"] and
                  z["scenario"]==m["scenario_id"])
    selected["scheduled_jobs"]=["forward","audit","format"]
    selected["statuses"]={j:"success" for j in m["workflow_runs"][0]["jobs"]}
    return x,m


def retry_pair():
    old=observed(outcome="failure")
    row=old["workflow_runs"][0]
    row["jobs"][0]["name"]="synthetic compile"
    row["jobs"][0]["run_attempt"]=1
    row["jobs"].append({
        "id":992, "run_id":RUN, "run_attempt":1,
        "name":"synthetic audit", "status":"completed",
        "conclusion":"success",
        "started_at":"2026-11-20T09:00:00Z",
        "completed_at":"2026-11-20T09:00:08Z"
    })
    row["jobs"].append({
        "id":993, "run_id":RUN, "run_attempt":1,
        "name":"synthetic format", "status":"completed",
        "conclusion":"success",
        "started_at":"2026-11-20T09:01:00Z",
        "completed_at":"2026-11-20T09:01:04Z"
    })
    newer=copy.deepcopy(old)
    newrow=newer["workflow_runs"][0]
    newrow["attempt"]=2
    newrow["run"]["run_attempt"]=2
    newrow["run"]["conclusion"]="success"
    for job in newrow["jobs"]:
        job["id"]+=100
        job["run_attempt"]=2
    changed=newrow["jobs"][0]
    changed["conclusion"]="success"
    changed["started_at"]="2026-11-22T12:01:00Z"
    changed["completed_at"]="2026-11-22T12:01:10Z"
    return old,newer


class RetryReceiptTests(unittest.TestCase):
    def report(self,old=None,new=None,m=None,scenario=None):
        source,mm=retry_story_and_mapping()
        before,after=retry_pair()
        return audit.reconcile_targeted_retry(
            scenario or source,m or mm,
            old if old is not None else before,
            new if new is not None else after)

    def test_carries_old_success_without_counting_new_runner_time(self):
        outcome=self.report()
        self.assertEqual(outcome["status"],"RETRY_ACCOUNTING_RECONCILED")
        self.assertEqual(outcome["newly_reexecuted_jobs"],["synthetic compile"])
        self.assertEqual(outcome["carried_forward_jobs"],
                         ["synthetic audit","synthetic format"])
        self.assertEqual(outcome["inferred_new_execution_seconds"],10)
        self.assertEqual(outcome["provider_billed_minutes"],"NOT_MEASURED")
        self.assertFalse(outcome["runner_occupancy_proven"])
        self.assertFalse(outcome["end_to_end_ci_qualified"])
        self.assertEqual(outcome["downstream_release_or_tag_retriggered"],
                         "NOT_VERIFIED")

    def test_changed_api_ids_on_carry_forward_are_accepted(self):
        old,new=retry_pair()
        self.assertTrue(all(a["id"]!=b["id"] for a,b in
                         zip(old["workflow_runs"][0]["jobs"],
                             new["workflow_runs"][0]["jobs"])))
        self.assertEqual(self.report(old,new)["required_job_count"],3)

    def test_false_green_prior_failure_rejected(self):
        old,new=retry_pair()
        old["workflow_runs"][0]["run"]["conclusion"]="success"
        with self.assertRaisesRegex(audit.Hold,"expected completed state"):
            self.report(old,new)

    def test_in_progress_or_false_green_target_rejected(self):
        for key,value in (("status","in_progress"),("conclusion","failure"),
                          ("run_attempt",1)):
            with self.subTest(key=key):
                old,new=retry_pair()
                new["workflow_runs"][0]["run"][key]=value
                with self.assertRaises(audit.Hold):
                    self.report(old,new)

    def test_missing_or_extra_required_status_rejected(self):
        for action in ("drop","duplicate","rename"):
            with self.subTest(action=action):
                old,new=retry_pair()
                jobs=new["workflow_runs"][0]["jobs"]
                if action=="drop":jobs.pop()
                if action=="duplicate":jobs.append(copy.deepcopy(jobs[-1]))
                if action=="rename":jobs[-1]["name"]="unexpected job"
                with self.assertRaises(audit.Hold):self.report(old,new)

    def test_changed_carried_forward_interval_rejected(self):
        old,new=retry_pair()
        new["workflow_runs"][0]["jobs"][1]["started_at"]="2026-11-20T09:00:01Z"
        with self.assertRaisesRegex(audit.Hold,"changed execution window"):
            self.report(old,new)

    def test_retried_failure_must_have_new_execution_interval(self):
        for defect in ("same_id","same_window","early"):
            with self.subTest(defect=defect):
                old,new=retry_pair()
                previous=old["workflow_runs"][0]["jobs"][0]
                retried=new["workflow_runs"][0]["jobs"][0]
                if defect=="same_id":retried["id"]=previous["id"]
                if defect=="same_window":
                    retried["started_at"]=previous["started_at"]
                    retried["completed_at"]=previous["completed_at"]
                if defect=="early":
                    retried["started_at"]="2026-11-22T11:59:00Z"
                with self.assertRaisesRegex(audit.Hold,"distinct later retry"):
                    self.report(old,new)

    def test_cross_revision_run_identity_and_workflow_refused(self):
        for defect in ("head_sha","id","event","path"):
            with self.subTest(defect=defect):
                old,new=retry_pair()
                new["workflow_runs"][0]["run"][defect]={
                    "head_sha":"b"*40, "id":9999, "event":"release",
                    "path":".github/workflows/evil.yml"}[defect]
                with self.assertRaises(audit.Hold):self.report(old,new)

    def test_cross_attempt_or_cross_run_job_refused(self):
        for defect in ("run_attempt","run_id"):
            with self.subTest(defect=defect):
                old,new=retry_pair()
                new["workflow_runs"][0]["jobs"][1][defect]=555
                with self.assertRaises(audit.Hold):self.report(old,new)

    def test_incomplete_retry_page_or_extra_envelope_refused(self):
        old,new=retry_pair()
        new["workflow_runs"].append(copy.deepcopy(new["workflow_runs"][0]))
        with self.assertRaisesRegex(audit.Hold,"one complete workflow"):
            self.report(old,new)

    def test_skipped_or_still_failed_job_is_not_accepted(self):
        for status,conclusion in (("completed","skipped"),
                                  ("in_progress",None),
                                  ("completed","failure")):
            with self.subTest(status=status,conclusion=conclusion):
                old,new=retry_pair()
                new["workflow_runs"][0]["jobs"][0]["status"]=status
                new["workflow_runs"][0]["jobs"][0]["conclusion"]=conclusion
                with self.assertRaises(audit.Hold):self.report(old,new)

    def test_prior_attempt_gaps_and_multiple_mapped_runs_refused(self):
        scenario,m=retry_story_and_mapping()
        old,new=retry_pair()
        m["workflow_runs"][0]["attempt"]=3
        with self.assertRaises(audit.Hold):
            self.report(old,new,m=m,scenario=scenario)
        scenario,m=retry_story_and_mapping()
        m["workflow_runs"].append(copy.deepcopy(m["workflow_runs"][0]))
        with self.assertRaises(audit.Hold):
            self.report(old,new,m=m,scenario=scenario)

    def test_forged_local_simulator_proof_refused(self):
        scenario,m=retry_story_and_mapping()
        scenario["host_execution_proven"]=True
        with self.assertRaisesRegex(audit.Hold,"self-authentication"):
            self.report(m=m,scenario=scenario)

    def test_retry_and_live_conflict_refused_before_network_read(self):
        scenario,m=retry_story_and_mapping()
        old,_=retry_pair()
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for name,data in (("s",scenario),("m",m),("old",old)):
                (root/(name+".json")).write_text(json.dumps(data),encoding="utf8")
            cmd=[sys.executable,str(ROOT/"scripts"/"ci_host_reconcile.py"),
                 "--simulator-results",str(root/"s.json"),
                 "--mapping",str(root/"m.json"),
                 "--retry-previous-observations",str(root/"old.json"),
                 "--live","--require-pass"]
            run=subprocess.run(cmd,capture_output=True,text=True,timeout=8)
            self.assertEqual(run.returncode,2)
            self.assertIn("two supplied offline observation files",run.stderr)
            self.assertNotIn("GitHub API read failed",run.stderr)

    def test_cli_two_offline_files_never_upgrade_provenance(self):
        scenario,m=retry_story_and_mapping()
        old,new=retry_pair()
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for name,content in (("s",scenario),("m",m),("old",old),("new",new)):
                (root/(name+".json")).write_text(json.dumps(content),encoding="utf8")
            cmd=[sys.executable,str(ROOT/"scripts"/"ci_host_reconcile.py"),
                 "--simulator-results",str(root/"s.json"),
                 "--mapping",str(root/"m.json"),
                 "--retry-previous-observations",str(root/"old.json"),
                 "--observations",str(root/"new.json"),"--require-pass"]
            result=subprocess.run(cmd,capture_output=True,text=True)
            self.assertEqual(result.returncode,0,result.stderr)
            report=json.loads(result.stdout)
            self.assertEqual(report["status"],"RETRY_ACCOUNTING_RECONCILED")
            self.assertEqual(report["observation_provenance"],
                             "OBSERVED_AS_SUPPLIED_NOT_AUTHENTICATED")
            self.assertFalse(report["automatic_cutover_authorized"])


if __name__=="__main__":
    unittest.main()
