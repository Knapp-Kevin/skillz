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

    def test_real_authored_pilot_exact_pins_and_all_assessed_hosts(self):
        self.assertEqual(m.inventory(PACKAGE)["source_blobs"], self.contract["source_blobs"])
        for host in m.compat.HOSTS:
            with self.subTest(host=host):
                p = m.plan(self.contract, PACKAGE, host)
                self.assertEqual(p, m.plan(self.contract, PACKAGE, host))
                self.assertEqual(set(p["plan"]["receipt_stage_requirements"]), set(m.a.STAGES))
                self.assertEqual({c["status"] for c in p["plan"]["cases"]}, {"NOT_RUN"})
                self.assertFalse(p["plan"]["host_execution_observed"])

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

    def test_script_bearing_real_pilot_all_assessed_hosts(self):
        contract = json.loads((ROOT / "engine/builder/examples/mcp-tool-surface-source-contract.json").read_text(encoding="utf-8"))
        package = ROOT / "skills/authored/mcp-tool-surface-auditor"
        self.assertEqual(m.inventory(package)["source_blobs"], contract["source_blobs"])
        for host in m.compat.HOSTS:
            with self.subTest(host=host):
                plan = m.plan(contract, package, host)["plan"]
                self.assertEqual(len(plan["cases"]), 12)
                self.assertEqual(plan["script_resource_coverage"], ["scripts/audit.py", "tests/test_audit.py"])
                self.assertFalse(plan["host_execution_observed"])
                self.assertEqual({c["status"] for c in plan["cases"]}, {"NOT_RUN"})

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
