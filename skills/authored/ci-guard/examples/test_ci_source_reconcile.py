"""Negative controls for exact-source CI workflow/validator textual reconciliation.

All fixtures are synthetic. The source binder parses YAML literals and
Python AST only; it NEVER executes a consuming source file or checker.
"""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import ci_source_reconcile as source

HEAD="a"*40
GUARD="\${{ always() && needs.producer.result == 'success' }}"
VERIFY="""name: Synthetic verify
on: [pull_request]
permissions: read-all
jobs:
  producer:
    runs-on: ubuntu-24.04
    steps:
      - run: echo readonly
  gate:
    needs: [producer]
    if: """+GUARD+"""
    runs-on: ubuntu-24.04
    steps:
      - run: echo gate
"""
RELEASE="""name: Synthetic release
on: [release]
jobs:
  release-check:
    runs-on: ubuntu-24.04
    steps:
      - run: echo release
"""

def fn(name,path,job,guard=None,needs=None,trap=False):
    lines=[
        f"def test_{name}():",
        f"    workflow_text=(Path(__file__).parents[1] / {path!r}).read_text()",
        f"    assert {'  '+job+':'!r} in workflow_text",
    ]
    if needs is not None:lines.append(f"    assert {'    needs: '+needs!r} in workflow_text")
    if guard is not None:lines.append(f"    assert {'    if: '+guard!r} in workflow_text")
    if trap:lines.append("    raise RuntimeError('MUST_NOT_EXECUTE_USER_TEST')")
    return "\n".join(lines)+"\n\n"


def scenario():
    design={"id":"candidate","source_revision":HEAD,
            "workflows":[{"id":"verify"},{"id":"release"}],
            "jobs":[{"id":"producer","workflow":"verify","needs":[]},
                    {"id":"gate","workflow":"verify","needs":["producer"]},
                    {"id":"release-check","workflow":"release","needs":[]}],
            "normative_obligations":{}, "normative_side_effects":{}}
    other=copy.deepcopy(design);other["id"]="other"
    return {"schema_version":3,"source_revision":HEAD,
            "inventory":{"complete":True,"workflow_files_checked":True,
                         "nested_invocations_expanded":True,
                         "conformance_tests_checked":True,
                         "normative_rules_checked":True,
                         "unresolved":[],"source_revision":HEAD},
            "designs":[design,other],"known_semantics":"NORMALIZED_SUBSET_V3",
            "scenarios":[{"id":"synthetic"}]}


class Sources(unittest.TestCase):
    def setUp(self):
        self.t=tempfile.TemporaryDirectory()
        self.addCleanup(self.t.cleanup)
        self.root=Path(self.t.name)
        (self.root/".github"/"workflows").mkdir(parents=True)
        (self.root/"tests").mkdir()
        self.workflow_files={
            ".github/workflows/verify.yml":VERIFY,
            ".github/workflows/release.yml":RELEASE,
        }
        self.oracle_source=(
            "from pathlib import Path\n\n"
            +fn("producer",".github/workflows/verify.yml","producer",trap=True)
            +fn("gate",".github/workflows/verify.yml","gate",guard=GUARD,needs="[producer]")
            +fn("release",".github/workflows/release.yml","release-check")
        )
        self.s=scenario()
        self.mapping={
            "schema_version":1,"source_revision":HEAD,"design_id":"candidate",
            "workflow_files":[
                {"workflow":"verify","path":".github/workflows/verify.yml",
                 "sha256":"","events":["pull_request"],
                 "jobs":[{"job":"producer","source_job":"producer","if":None,
                          "needs":[],"runs_on":"ubuntu-24.04"},
                         {"job":"gate","source_job":"gate","if":GUARD,
                          "needs":["producer"],"runs_on":"ubuntu-24.04"}]},
                {"workflow":"release","path":".github/workflows/release.yml",
                 "sha256":"","events":["release"],
                 "jobs":[{"job":"release-check","source_job":"release-check",
                          "if":None,"needs":[],"runs_on":"ubuntu-24.04"}]}
            ],
            "oracle_files":[{"path":"tests/test_workflow_contract.py","sha256":"",
                             "checks":[{"job":"producer","function":"test_producer"},
                                       {"job":"gate","function":"test_gate"},
                                       {"job":"release-check","function":"test_release"}]}]
        }
        self.write_all()

    def write(self,path,content):
        p=self.root.joinpath(path)
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(content,encoding="utf-8")

    def hash(self,path):
        return hashlib.sha256(self.root.joinpath(path).read_bytes()).hexdigest()

    def write_all(self):
        for name,body in self.workflow_files.items():self.write(name,body)
        self.write("tests/test_workflow_contract.py",self.oracle_source)
        self.repin()

    def repin(self):
        for w in self.mapping["workflow_files"]:
            w["sha256"]=self.hash(w["path"])
        for o in self.mapping["oracle_files"]:
            o["sha256"]=self.hash(o["path"])

    def check(self):
        return source.reconcile(str(self.root),self.s,self.mapping)

    def test_exact_source_reconciles_but_remains_unverified_host_claim(self):
        r=self.check()
        self.assertEqual(r["status"],"STATIC_SOURCE_RECONCILED")
        self.assertEqual((r["workflow_files"],r["jobs"],r["oracle_checks"]),(2,3,3))
        self.assertFalse(r["yaml_effective_semantics_verified"])
        self.assertFalse(r["compiled_oracle_execution_verified"])
        self.assertFalse(r["source_git_head_authenticated"])
        self.assertFalse(r["automatic_cutover_authorized"])
        self.assertFalse(r["proves_live_ci_assurance"])

    def test_edited_guard_with_stale_source_digest_holds(self):
        p=".github/workflows/verify.yml"
        self.write(p,VERIFY.replace(GUARD,"false"))
        with self.assertRaisesRegex(source.Hold,"WORKFLOW_DIGEST_MISMATCH"):
            self.check()

    def test_edited_guard_with_updated_digest_still_holds(self):
        self.write(".github/workflows/verify.yml",VERIFY.replace(GUARD,"false"))
        self.repin()
        with self.assertRaisesRegex(source.Hold,"SOURCE_IF_DRIFT"):
            self.check()

    def test_stale_local_oracle_guard_is_not_accepted(self):
        self.oracle_source=self.oracle_source.replace("    if: "+GUARD,
                                                       "    if: false")
        self.write("tests/test_workflow_contract.py",self.oracle_source)
        self.repin()
        with self.assertRaisesRegex(source.Hold,"ORACLE_ASSERTION_DRIFT"):
            self.check()

    def test_missing_oracle_source_assertion_refused(self):
        self.oracle_source=self.oracle_source.replace("    assert '  gate:' in workflow_text",
                                                       "    assert '  missing:' in workflow_text")
        self.write("tests/test_workflow_contract.py",self.oracle_source)
        self.repin()
        with self.assertRaisesRegex(source.Hold,"ORACLE_ASSERTION_DRIFT"):
            self.check()

    def test_missing_source_oracle_source_read_refused(self):
        self.oracle_source=self.oracle_source.replace(
            'workflow_text=(Path(__file__).parents[1] / \'.github/workflows/verify.yml\').read_text()',
            "workflow_text='manually constructed not source-bound'")
        self.write("tests/test_workflow_contract.py",self.oracle_source)
        self.repin()
        with self.assertRaisesRegex(source.Hold,"UNSUPPORTED_ORACLE: test source read not found"):
            self.check()

    def test_needs_mapping_must_match_normalized_graph(self):
        self.s["designs"][0]["jobs"][1]["needs"]=[]
        with self.assertRaisesRegex(source.Hold,"SIM_NEEDS_DRIFT"):
            self.check()

    def test_missing_source_dependency_is_detected(self):
        self.write(".github/workflows/verify.yml",VERIFY.replace("    needs: [producer]\n",""))
        self.repin()
        with self.assertRaisesRegex(source.Hold,"SOURCE_NEEDS_DRIFT"):
            self.check()

    def test_source_runner_change_is_detected(self):
        self.write(".github/workflows/release.yml",RELEASE.replace("ubuntu-24.04","windows-2025"))
        self.repin()
        with self.assertRaisesRegex(source.Hold,"SOURCE_RUNNER_DRIFT"):
            self.check()

    def test_extra_uninventoried_workflow_is_hold(self):
        self.write(".github/workflows/secret-release.yml",RELEASE)
        with self.assertRaisesRegex(source.Hold,"UNINVENTORIED_WORKFLOW_FILES"):
            self.check()

    def test_oracle_digest_change_is_hold(self):
        self.write("tests/test_workflow_contract.py",self.oracle_source+"\n# changed\n")
        with self.assertRaisesRegex(source.Hold,"ORACLE_DIGEST_MISMATCH"):
            self.check()

    def test_changed_or_missing_source_job_refused(self):
        self.write(".github/workflows/release.yml",RELEASE.replace("release-check:","different-check:"))
        self.repin()
        with self.assertRaisesRegex(source.Hold,"SOURCE_JOB_COVERAGE_DRIFT"):
            self.check()

    def test_repeated_normalized_job_map_refused(self):
        self.mapping["workflow_files"][1]["jobs"][0]["job"]="gate"
        with self.assertRaisesRegex(source.Hold,"UNMAPPED_OR_DUPLICATE_SIM_JOB"):
            self.check()

    def test_missing_static_conformance_oracle_holds(self):
        self.mapping["oracle_files"][0]["checks"].pop()
        with self.assertRaisesRegex(source.Hold,"UNBOUND_CONFORMANCE_JOB"):
            self.check()

    def test_python_ast_is_never_executed_by_binder(self):
        # Fixture deliberately raises on invocation, but static source
        # analysis only sees its AST and does not run the function.
        r=self.check()
        self.assertEqual(r["status"],"STATIC_SOURCE_RECONCILED")
        self.assertFalse(r["compiled_oracle_execution_verified"])

    def test_yaml_complex_event_filters_are_unsupported(self):
        self.write(".github/workflows/verify.yml",VERIFY.replace(
            "on: [pull_request]","on:\n  pull_request:\n    paths: [src/**]"))
        self.repin()
        with self.assertRaisesRegex(source.Hold,"UNSUPPORTED_SEMANTICS"):
            self.check()

    def test_multiline_guard_requires_host_parser(self):
        self.write(".github/workflows/verify.yml",VERIFY.replace(
            "    if: "+GUARD,"    if: >-\n      always()"))
        self.repin()
        with self.assertRaisesRegex(source.Hold,"UNSUPPORTED_SEMANTICS"):
            self.check()

    def test_reusable_job_and_matrix_are_unsupported(self):
        for fragment in ("    uses: ./reusable.yml\n",
                         "    strategy:\n      matrix:\n        os: [ubuntu, windows]\n"):
            with self.subTest(fragment=fragment):
                self.write(".github/workflows/release.yml",RELEASE.replace(
                    "    steps:\n",fragment+"    steps:\n"))
                self.repin()
                with self.assertRaisesRegex(source.Hold,"UNSUPPORTED_SEMANTICS"):
                    self.check()
        self.write(".github/workflows/release.yml",RELEASE)
        self.repin()

    def test_job_renamed_in_source_cannot_reuse_old_oracle(self):
        self.write(".github/workflows/verify.yml",VERIFY.replace("  gate:","  gate-new:"))
        self.repin()
        with self.assertRaisesRegex(source.Hold,"SOURCE_JOB_COVERAGE_DRIFT"):
            self.check()

    def test_source_sha_and_inventory_flag_cannot_be_stale(self):
        self.mapping["source_revision"]="b"*40
        with self.assertRaisesRegex(source.Hold,"SOURCE_REVISION_MISMATCH"):
            self.check()
        self.mapping["source_revision"]=HEAD
        self.s["inventory"]["complete"]=False
        with self.assertRaisesRegex(source.Hold,"INCOMPLETE_NORMALIZED_INVENTORY"):
            self.check()

    def test_source_symlink_never_followed(self):
        if not hasattr(Path,"symlink_to"):self.skipTest("symlinks unavailable")
        target=self.root/".github/workflows/verify.yml"
        target.unlink()
        try:target.symlink_to(self.root/".github/workflows/release.yml")
        except OSError:self.skipTest("system denied symlink")
        with self.assertRaisesRegex(source.Hold,"symlinked workflow"):
            self.check()

    def test_path_traversal_source_and_checker_refused(self):
        for path in ("../secret.yml",".github/workflows/../other.yml",
                     "/tmp/absolute.yaml"):
            with self.subTest(path=path):
                self.mapping["workflow_files"][0]["path"]=path
                with self.assertRaises(source.Hold):
                    self.check()
                self.mapping["workflow_files"][0]["path"]=".github/workflows/verify.yml"

    def test_duplicate_source_workflow_path_refused(self):
        self.mapping["workflow_files"][1]["path"]=".github/workflows/verify.yml"
        with self.assertRaisesRegex(source.Hold,"DUPLICATE_WORKFLOW_SOURCE_FILE"):
            self.check()

    def test_cli_output_and_fail_closed_exit_code(self):
        scenario_input=self.root/"scenario.json"
        source_map=self.root/"source-map.json"
        scenario_input.write_text(json.dumps(self.s),encoding="utf8")
        source_map.write_text(json.dumps(self.mapping),encoding="utf8")
        command=[sys.executable,str(ROOT/"scripts/ci_source_reconcile.py"),
                 "--root",str(self.root),
                 "--scenario-input",str(scenario_input),
                 "--source-map",str(source_map),"--require-pass"]
        pass_run=subprocess.run(command,capture_output=True,text=True)
        self.assertEqual(pass_run.returncode,0,pass_run.stderr)
        self.assertEqual(json.loads(pass_run.stdout)["status"],"STATIC_SOURCE_RECONCILED")
        self.write(".github/workflows/release.yml",RELEASE+"# source changed\n")
        failed=subprocess.run(command,capture_output=True,text=True)
        self.assertEqual(failed.returncode,2)
        self.assertIn("CI_SOURCE_RECONCILE_HOLD",failed.stderr)

    def test_compiled_oracle_test_is_not_claimed_passed(self):
        result=self.check()
        self.assertTrue(result["run_conformance_tests_separately"])
        self.assertFalse(result["compiled_oracle_execution_verified"])
        self.assertFalse(result["provider_job_dispatch_verified"])


if __name__=="__main__":
    unittest.main()
