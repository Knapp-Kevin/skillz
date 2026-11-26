"""Source-pinned manual acceptance pilot and negative tests; no host invocation."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "engine/builder"))
import source_acceptance as m
import acceptance_ledger as ledger

CONTRACT = ROOT / "engine/builder/examples/scheduled-work-source-contract.json"
PACKAGE = ROOT / "skills/authored/scheduled-work-proof-auditor"


class SourceTests(unittest.TestCase):
    def setUp(self):
        self.contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def read_corpus_contracts(self, files, authored, minimum):
        contracts = {}
        for path in files:
            contract, _ = m.a.read_json(path)
            self.assertIs(type(contract), dict, str(path))
            slug = contract.get("skill")
            self.assertIs(type(slug), str, str(path))
            self.assertIn(slug, authored, str(path))
            self.assertNotIn(slug, contracts, "Duplicate contract for " + slug)
            contracts[slug] = contract
        self.assertTrue(set(minimum) <= set(contracts), "Missing reviewed contracts: " +
                        ", ".join(sorted(set(minimum) - set(contracts))))
        return contracts

    def test_corpus_identity_uses_contents_and_rejects_duplicate_or_missing_contracts(self):
        slug = self.contract["skill"]
        alias = self.root / "short-alias-source-contract.json"
        alias.write_text(json.dumps(self.contract), encoding="utf-8")
        authored = {slug: {}}
        self.assertEqual(self.read_corpus_contracts([alias], authored, {slug}), {slug: self.contract})
        duplicate = self.root / "another-alias-source-contract.json"
        duplicate.write_text(json.dumps(self.contract), encoding="utf-8")
        with self.assertRaisesRegex(AssertionError, "Duplicate contract"):
            self.read_corpus_contracts([alias, duplicate], authored, {slug})
        with self.assertRaisesRegex(AssertionError, "Missing reviewed contracts"):
            self.read_corpus_contracts([], authored, {slug})
        foreign = self.root / "foreign-source-contract.json"
        foreign.write_text(json.dumps(dict(self.contract, skill="unregistered-skill")), encoding="utf-8")
        with self.assertRaises(AssertionError):
            self.read_corpus_contracts([foreign], authored, set())

    def test_all_reviewed_corpus_contracts_across_assessed_hosts(self):
        # Minimum reviewed coverage floor. A missing contract or removed case
        # cannot silently disappear from automatic discovery.
        minimum = {
            "scheduled-work-proof-auditor": (3, 9, 0),
            "mcp-tool-surface-auditor": (7, 12, 2),
            "decision-record-steward": (3, 10, 0),
            "agent-workspace-footprint-assessor": (3, 10, 0),
            "connector-capability-risk-review": (3, 10, 0),
            "effort-allocation-navigator": (18, 18, 7),
            "file-lifecycle-curator": (33, 24, 12),
            "repository-readme-architect": (18, 17, 7),
            "ci-guard": (55, 26, 24),
            "privilege-exposure-mapper": (3, 10, 0),
            "research-methods-appraiser": (3, 10, 0),
            "research-question-dossier": (3, 10, 0),
            "statement-variance-reviewer": (3, 10, 0),
            "work-period-evidence-reporter": (3, 10, 0),
            "personal-operations-control-board": (3, 10, 0),
            "evidence-narrative-composer": (3, 10, 0),
            "learning-evidence-progression": (3, 10, 0),
            "business-presence-observatory": (3, 10, 0),
            "professional-market-evidence-scout": (3, 10, 0),
            "develop-melodic-motif": (3, 10, 0),
            "metadata-taxonomy-steward": (4, 10, 0),
            "narrative-scene-gap-audit": (4, 10, 0),
            "character-motivation-interview": (4, 10, 0),
            "claim-evidence-adjudicator": (6, 13, 2),
            "agent-failure-boundary-analysis": (6, 13, 2),
            "source-debt-triage": (5, 13, 2),
            "decision-tradeoff-workbench": (6, 13, 2),
            "recursive-refinement-trace": (12, 18, 7),
            "evidence-driven-refinement-loop": (11, 16, 2),
            "skill-trial-evidence-auditor": (8, 15, 2),
        }
        registry = json.loads((ROOT / "registry/authored-skills-index.json").read_text(encoding="utf-8"))
        authored = {row["id"]: row for row in registry["skills"]}
        suffix = "-source-contract.json"
        files = sorted((ROOT / "engine/builder/examples").glob("*" + suffix))
        contracts = self.read_corpus_contracts(files, authored, minimum)
        for slug, contract in sorted(contracts.items()):
            with self.subTest(skill=slug):
                package = ROOT / "skills/authored" / slug
                self.assertEqual(m.inventory(package)["source_blobs"], contract["source_blobs"])
                self.assertEqual(len(contract["source_blobs"]), authored[slug]["package_file_count"])
                scripts = sorted(p for p in contract["source_blobs"]
                                 if Path(p).suffix.lower() in m.compat.SCRIPT_EXTENSIONS)
                if slug in minimum:
                    count, case_count, script_count = minimum[slug]
                    self.assertGreaterEqual(len(contract["source_blobs"]), count)
                    self.assertGreaterEqual(len(contract["cases"]), case_count)
                    self.assertGreaterEqual(len(scripts), script_count)
                for host in m.compat.HOSTS:
                    with self.subTest(host=host):
                        report = m.plan(contract, package, host)
                        plan = report["plan"]
                        self.assertEqual(len(plan["cases"]), len(contract["cases"]))
                        self.assertEqual(plan["script_resource_coverage"], scripts)
                        self.assertEqual(set(plan["receipt_stage_requirements"]), set(m.a.STAGES))
                        self.assertEqual({c["status"] for c in plan["cases"]}, {"NOT_RUN"})
                        self.assertEqual(report["plan_sha256"], m.generated.canonical_sha(plan))
                        self.assertFalse(plan["host_execution_observed"])
                        self.assertFalse(plan["consumer_accepted"])
                        if slug == "scheduled-work-proof-auditor":
                            self.assertEqual(report, m.plan(contract, package, host))

    def copy_package(self):
        import shutil
        return Path(shutil.copytree(PACKAGE, self.root / PACKAGE.name))

    def test_source_change_or_extra_member_rejected(self):
        folder = self.copy_package()
        extra = folder / "extra.txt"
        extra.write_text("extra")
        with self.assertRaisesRegex(ValueError, "SOURCE_INVENTORY_MISMATCH"):
            m.plan(self.contract, folder, "claude-code")
        extra.unlink()
        p = folder / "examples/synthetic-cases.md"
        p.write_bytes(p.read_bytes() + b"changed")
        with self.assertRaisesRegex(ValueError, "SOURCE_BLOB_MISMATCH"):
            m.plan(self.contract, folder, "claude-code")

    def test_missing_case_and_invalid_anchor_rejected(self):
        for mutation in ("remove", "anchor", "duplicate"):
            c = copy.deepcopy(self.contract)
            if mutation == "remove":
                c["cases"].pop()
            elif mutation == "anchor":
                c["cases"][0]["anchor"] = "Invented source text not found."
            else:
                c["cases"][-1]["id"] = c["cases"][0]["id"]
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                m.plan(c, PACKAGE, "claude-code")

    def test_example_cannot_replace_normative_anchor(self):
        self.contract["cases"][0].update(source="examples/synthetic-cases.md",
            anchor="These are hand-authored expected cases, not executed validation.")
        with self.assertRaisesRegex(ValueError, "CORE_CASE_REQUIRES_NORMATIVE_SOURCE"):
            m.plan(self.contract, PACKAGE, "claude-code")

    def test_unknown_host_and_unknown_contract_fields_rejected(self):
        with self.assertRaises(ValueError):
            m.plan(self.contract, PACKAGE, "chatgpt")
        self.contract["validated"] = True
        with self.assertRaises(ValueError):
            m.plan(self.contract, PACKAGE, "claude-code")

    def script_package(self):
        folder = self.copy_package()
        (folder / "scripts").mkdir()
        for name in ("helper.py", "check.ps1", "module.psm1"):
            (folder / "scripts" / name).write_text("# Fictional; never executed.\n", encoding="utf-8")
        c = copy.deepcopy(self.contract)
        c["source_blobs"] = m.inventory(folder)["source_blobs"]
        return folder, c

    def resource_case(self, paths):
        return {"id": "script-resource", "kind": "resource", "source": "SKILL.md",
                "anchor": self.contract["cases"][0]["anchor"],
                "setup": "Inspect the fictional helper resources without invoking them.",
                "expected": "Verify resource presence and respect the authorized runtime boundary.",
                "resource_paths": paths}

    def test_each_script_needs_exact_resource_and_unavailable_capability_coverage(self):
        folder, c = self.script_package()
        paths = ["scripts/helper.py", "scripts/check.ps1", "scripts/module.psm1"]
        with self.assertRaisesRegex(ValueError, "SCRIPT_RESOURCE_COVERAGE_INCOMPLETE"):
            m.plan(c, folder, "claude-code")
        c["cases"].append(self.resource_case(paths[:1]))
        with self.assertRaisesRegex(ValueError, "SCRIPT_RESOURCE_COVERAGE_INCOMPLETE"):
            m.plan(c, folder, "claude-code")
        c["cases"][-1]["resource_paths"] = paths
        with self.assertRaisesRegex(ValueError, "SCRIPT_DEPENDENCY_FAILURE_COVERAGE_INCOMPLETE"):
            m.plan(c, folder, "claude-code")
        dependency = next(x for x in c["cases"] if x["kind"] == "dependency-unavailable")
        dependency["resource_paths"] = paths[:2]
        with self.assertRaisesRegex(ValueError, "SCRIPT_DEPENDENCY_FAILURE_COVERAGE_INCOMPLETE"):
            m.plan(c, folder, "claude-code")
        dependency["resource_paths"] = paths
        result = m.plan(c, folder, "claude-code")["plan"]
        self.assertEqual(result["script_resource_coverage"], sorted(paths))
        resource = next(x for x in result["cases"] if x["kind"] == "resource")
        self.assertEqual({x["path"]: x["sha256"] for x in resource["resource_targets"]},
                         {p: result["canonical_files_sha256"][p] for p in paths})
        self.assertFalse(result["host_execution_observed"])

    def test_resource_case_rejects_unbound_duplicate_or_misplaced_paths(self):
        folder, c = self.script_package()
        for paths in ([], ["scripts/nonexistent.py"], ["scripts/helper.py"] * 2,
                      ["../outside.py"], ["SKILL.md"], "scripts/helper.py"):
            with self.subTest(paths=paths):
                c["cases"] = copy.deepcopy(self.contract["cases"]) + [self.resource_case(paths)]
                with self.assertRaises(ValueError):
                    m.plan(c, folder, "claude-code")
        c["cases"] = copy.deepcopy(self.contract["cases"])
        c["cases"][0]["resource_paths"] = ["scripts/helper.py"]
        with self.assertRaisesRegex(ValueError, "INVALID_RESOURCE_CASE_TARGETS"):
            m.plan(c, folder, "claude-code")

    def test_script_paths_cannot_be_bypassed_by_repinning_changed_inventory(self):
        folder, c = self.script_package()
        paths = ["scripts/helper.py", "scripts/check.ps1", "scripts/module.psm1"]
        c["cases"].append(self.resource_case(paths))
        next(x for x in c["cases"] if x["kind"] == "dependency-unavailable")["resource_paths"] = paths
        self.assertEqual(m.plan(c, folder, "claude-code")["plan"]["script_resource_coverage"], sorted(paths))
        (folder / "scripts" / "new.cmd").write_text("rem Fictional.\n")
        c["source_blobs"] = m.inventory(folder)["source_blobs"]
        with self.assertRaisesRegex(ValueError, "SCRIPT_RESOURCE_COVERAGE_INCOMPLETE"):
            m.plan(c, folder, "claude-code")

    def test_ci_guard_offline_nested_overlap_oracle(self):
        import subprocess
        package = ROOT / "skills/authored/ci-guard"
        run = subprocess.run([sys.executable, "-B", "-m", "unittest",
                              "test_ci_overlap.OverlapTest.test_nested_alias_is_found_as_partial_overlap",
                              "test_ci_overlap.OverlapTest.test_different_platform_is_unproven_not_safe_to_remove"],
                             cwd=package / "examples", capture_output=True, text=True,
                             timeout=15, check=True)
        self.assertIn("Ran 2 tests", run.stderr)
        self.assertIn("OK", run.stderr)

    def test_readme_architect_offline_gold_cannot_self_certify(self):
        import subprocess
        package = ROOT / "skills/authored/repository-readme-architect"
        run = subprocess.run([sys.executable, "-B", "-m", "unittest",
                              "test_profile_acceptance.QualityProfileTests.test_complete_structure_still_does_not_self_award_gold"],
                             cwd=package / "tests", capture_output=True, text=True,
                             timeout=15, check=True)
        self.assertIn("Ran 1 test", run.stderr)
        self.assertIn("OK", run.stderr)

    def test_curator_offline_visual_progress_oracle(self):
        import subprocess
        package = ROOT / "skills/authored/file-lifecycle-curator"
        result = subprocess.run([sys.executable, "-B", str(package / "scripts/render_structure.py"),
                                 "--current", str(package / "examples/structure-progress.json")],
                                capture_output=True, text=True, timeout=15, check=True)
        report = json.loads(result.stdout)
        self.assertEqual(report["status"], "PROVISIONAL_VISUAL_ONLY")
        self.assertEqual(report["progress"]["planned_relocations"], 3)
        self.assertEqual(report["progress"]["verified_relocations"], 1)
        self.assertEqual(report["progress"]["state_counts"]["EXECUTED"], 1)
        self.assertFalse(report["checkpoint_written"])
        self.assertTrue({"observed", "proposed", "verified"} <= set(report["visuals"]))

    def test_navigator_offline_focus_oracle(self):
        import subprocess
        package = ROOT / "skills/authored/effort-allocation-navigator"
        result = subprocess.run([sys.executable, "-B", str(package / "scripts/plan.py"),
                                 "--input", str(package / "examples/fictional-user-focus.json")],
                                capture_output=True, text=True, timeout=15, check=True)
        report = json.loads(result.stdout)
        self.assertEqual([c["task_id"] for c in report["choices"]],
                         ["review-notes", "draft-note"])
        self.assertEqual(report["focus_resolution"], "CONTINUED_ELIGIBLE_SELECTION")
        self.assertNotIn("Review fictional public project notes", result.stdout)

    def test_actual_mcp_fixture_matches_predeclared_offline_oracle(self):
        # This is an offline helper fixture test, not native-host activation.
        import subprocess
        package = ROOT / "skills/authored/mcp-tool-surface-auditor"
        run = subprocess.run([sys.executable, "-B", str(package / "scripts/audit.py"),
                              "--input", str(package / "examples/synthetic-18-versus-12.json")],
                             capture_output=True, text=True, timeout=15, check=True)
        result = json.loads(run.stdout)
        self.assertEqual(result["counts"], {"backend_registry": 18, "mcp_list": 18, "host_visible": 12})
        self.assertEqual(result["status"], "OBSERVED_DIFFERENCE")
        self.assertEqual(result["observed_differences"], [
            {"boundary": "mcp_list_to_host_visible", "finding": "NOT_VISIBLE_DOWNSTREAM",
             "name": f"tool_{i:02d}"} for i in range(13, 19)])
        self.assertFalse(result["host_or_server_fault_assigned"])
        self.assertFalse(result["mcp_transport_observed"])
        self.assertFalse(result["tool_invocations_tested"])

    def test_real_source_plan_to_ledger_handoff_preserves_not_run(self):
        host = "gemini-apps"
        p = m.plan(self.contract, PACKAGE, host)
        slug = PACKAGE.name
        archive = self.root / (slug + "-gemini.zip")
        m.compat.write_zip(PACKAGE, host, str(archive), m.compat.inspect(PACKAGE, host))
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        manifest = {"schema_version": 1, "source_commit": "a"*40,
                    "skills": [{"id": slug, "package_tree_sha": "b"*40,
                                "hosts": {host: {"status": "PACKAGE_READY", "blockers": [],
                                                 "asset": archive.name, "sha256": digest}}}]}
        manifest_sha = "c"*64
        receipt = {"schema_version": 1, "skill": slug, "host": host, "source_commit": "a"*40,
                   "package_tree_sha": "b"*40, "asset": archive.name, "sha256": digest,
                   "manifest_sha256": manifest_sha, "environment": {k: "UNKNOWN" for k in m.a.ENV_FIELDS},
                   "execution_kind": "NOT_RUN", "authorization": "NOT_ESTABLISHED",
                   "cases": [{"stage": s, "status": "NOT_RUN", "evidence_id": None, "oracle_id": None}
                             for s in m.a.STAGES]}
        receipt_sha = m.generated.canonical_sha(receipt)
        rows = {"schema_version": 1, "plan_sha256": p["plan_sha256"], "receipt_sha256": receipt_sha,
                "cases": [{"case_id": c["id"], "status": "NOT_RUN", "fixture_id": None,
                           "oracle_id": None, "evidence_id": None} for c in p["plan"]["cases"]]}
        result = ledger.reconcile(self.contract, PACKAGE, manifest, manifest_sha, archive, receipt,
                                  receipt_sha, rows, source_contract=True)
        self.assertEqual(result["status"], "HOLD_INCOMPLETE_NATIVE_CLAIM")
        self.assertTrue(result["archive_members_match_regenerated_plan"])
        self.assertFalse(result["host_execution_observed"])
        self.assertEqual(result["case_claim_counts"]["NOT_RUN"], len(rows["cases"]))
        rows["cases"].pop()
        with self.assertRaisesRegex(ValueError, "INCOMPLETE_CASE_LEDGER"):
            ledger.reconcile(self.contract, PACKAGE, manifest, manifest_sha, archive, receipt,
                             receipt_sha, rows, source_contract=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
