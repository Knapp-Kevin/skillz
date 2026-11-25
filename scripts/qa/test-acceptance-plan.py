"""Offline design-derived plan mechanics, never consumer execution."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "engine/builder"))
import acceptance_plan as m
# Reuse existing fictional single/pack design fixtures, not a competing schema.
import importlib.util
spec = importlib.util.spec_from_file_location("design_cases", ROOT / "scripts/qa/test-engine-builder-design.py")
fixtures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixtures)


class PlanTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def package(self, d):
        folder = self.root / d["blueprint"]["name"]
        m.design.design_build(d, str(folder), write=True)
        return folder

    def test_single_preserves_contract_and_all_six_stages(self):
        d = fixtures.case()
        p = self.package(d)
        result = m.plan(d, p, "claude-apps")
        body = result["plan"]
        self.assertEqual(result, m.plan(d, p, "claude-apps"))
        self.assertEqual(result["plan_sha256"], m.canonical_sha(body))
        self.assertEqual(set(body["receipt_stage_requirements"]), set(m.acceptance.STAGES))
        self.assertEqual({c["status"] for c in body["cases"]}, {"NOT_RUN"})
        self.assertTrue(all(c["fixture_id"] is None and c["independent_oracle_id"] is None for c in body["cases"]))
        self.assertTrue({"missing-input", "false-green", "required-step-output-missing"} <= {c["kind"] for c in body["cases"]})
        self.assertEqual({o for c in body["cases"] for o in c["obligations"]},
                         {o["id"] for o in d["obligations"]})
        for key in ("probes_executed", "host_execution_observed", "consumer_accepted",
                    "semantic_coverage_verified", "release_identity_verified", "authorization_verified"):
            self.assertFalse(body[key])

    def test_pack_expands_each_required_and_optional_module(self):
        d = fixtures.pack_case()
        result = m.plan(d, self.package(d), "gemini-apps")["plan"]
        cases = {c["id"]: c for c in result["cases"]}
        for module in d["blueprint"]["modules"]:
            stem = "module-" + module["id"]
            self.assertIn(stem + "-output", cases)
            case = cases[stem + ("-missing" if module["required"] else "-fallback")]
            self.assertIn(case["id"], result["receipt_stage_requirements"]["outcome"])
            if not module["required"]:
                self.assertEqual(case["expected_contract"]["fallback"], module["fallback"])

    def test_extra_or_changed_package_member_rejected(self):
        d = fixtures.case()
        p = self.package(d)
        extra = p / "unreviewed.txt"
        extra.write_text("unreviewed")
        with self.assertRaisesRegex(ValueError, "PACKAGE_INVENTORY_MISMATCH"):
            m.plan(d, p, "claude-apps")
        extra.unlink()
        (p / "SKILL.md").write_bytes((p / "SKILL.md").read_bytes() + b"changed")
        with self.assertRaisesRegex(ValueError, "PACKAGE_BYTES_DIFFER_FROM_DESIGN"):
            m.plan(d, p, "claude-apps")

    def test_wrong_design_and_unknown_host_rejected(self):
        d = fixtures.case()
        p = self.package(d)
        with self.assertRaisesRegex(ValueError, "HOST_UNASSESSED"):
            m.plan(d, p, "chatgpt")
        changed = copy.deepcopy(d)
        changed["blueprint"]["verification"] += " Check the actual extra evidence."
        with self.assertRaisesRegex(ValueError, "PACKAGE_BYTES_DIFFER_FROM_DESIGN"):
            m.plan(changed, p, "claude-apps")

    def test_selected_host_adapter_is_bound_and_not_execution(self):
        d = fixtures.case()
        p = self.package(d)
        a = m.plan(d, p, "claude-apps")
        b = m.plan(d, p, "gemini-apps")
        self.assertEqual(a["plan"]["canonical_files_sha256"], b["plan"]["canonical_files_sha256"])
        self.assertNotEqual(a["plan_sha256"], b["plan_sha256"])
        self.assertIn("LICENSE.txt", {x["output"] for x in b["plan"]["host_member_manifest"]})
        self.assertFalse(b["plan"]["host_execution_observed"])

    def test_invalid_design_and_false_green_rejected(self):
        d = fixtures.case()
        p = self.package(d)
        d["probes"][-1]["expected"] = "COMPLETE_IF_VERIFIED"
        with self.assertRaisesRegex(ValueError, "UNSAFE_OR_FALSE_GREEN"):
            m.plan(d, p, "claude-apps")

    def test_plan_excludes_source_evidence_records(self):
        d = fixtures.case()
        p = self.package(d)
        result = json.dumps(m.plan(d, p, "claude-apps"))
        self.assertNotIn(d["evidence"][0]["source_identity"], result)
        self.assertNotIn(d["evidence"][0]["observation"], result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
