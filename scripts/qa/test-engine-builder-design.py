"""Adversarial source/obligation/probe tests for optional author design gate.

All input identities are fictional. These tests prove only the deterministic
handoff, NOT evidence authenticity, real agent behavior or consumer success.
"""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "engine" / "builder"))
import design

EXAMPLE = ROOT / "engine" / "builder" / "examples" / "fictional-design-case.json"
PACK = ROOT / "engine" / "builder" / "examples" / "pack-blueprint.json"


def case():
    return json.loads(EXAMPLE.read_text(encoding="utf-8"))


def pack_case():
    d = case()
    d["decision"] = "COMPOSE_ORIGINAL"
    d["blueprint"] = json.loads(PACK.read_text(encoding="utf-8"))
    d["obligations"] = [
        x for x in d["obligations"]
        if not x["target"].startswith("steps.")
    ]
    d["probes"][-1]["obligation_ids"].remove("requirement-8")
    d["probes"][0]["obligation_ids"].remove("requirement-8")
    for module in d["blueprint"]["modules"]:
        ident = "module-" + module["id"]
        d["obligations"].append({
            "id": ident,
            "target": "modules." + module["id"],
            "statement": "The module must deliver its declared handoff without inventing missing inputs.",
            "evidence_ids": ["fictional-task"],
        })
        if module["required"]:
            d["probes"][0]["obligation_ids"].append(ident)
        else:
            d["probes"].append({
                "id": "optional-fallback",
                "kind": "optional-fallback",
                "input": "A consumer declines the optional presentation variant after mandatory evidence checks.",
                "expected": "FALLBACK_NO_LOST_OBLIGATION",
                "obligation_ids": [ident],
            })
    d["probes"].append({
        "id": "pack-handoff",
        "kind": "pack-handoff",
        "input": "The evidence-check phase produces no handoff but the summarization phase claims success.",
        "expected": "HOLD_IF_MISSING",
        "obligation_ids": ["module-check", "module-summarize"],
    })
    return d


class DesignCases(unittest.TestCase):
    def reject(self, dossier, code):
        with self.assertRaisesRegex(design.builder.BuildHold, code):
            design.design_build(dossier)

    def test_original_design_generates_only_a_dry_run(self):
        report = design.design_build(case())
        self.assertEqual(report["status"], "RENDERED_DRAFT_PLAN_NOT_INSTALLED")
        self.assertEqual(report["design_gate"]["status"],
                         "TRACE_LINKS_PRESENT_NOT_BEHAVIOR_VALIDATED")
        self.assertEqual(report["design_gate"]["mapped_obligations"], 8)
        self.assertEqual(report["design_gate"]["evidence_items"], 2)
        self.assertEqual(report["design_gate"]["unlinked_evidence_ids"], [])
        self.assertEqual(len(report["design_gate"]["dossier_sha256"]), 64)
        self.assertFalse(report["design_gate"]["probes_executed"])
        self.assertFalse(report["design_gate"]["source_identity_authenticated"])
        self.assertFalse(report["consumer_outcome_accepted"])
        self.assertIsNone(report["destination"])

    def test_design_gate_propagates_host_targets_and_hard_limit(self):
        d = case()
        d["blueprint"]["steps"][0]["instructions"] = "Inspect authorized evidence. " * 400
        d["blueprint"]["verification"] = "Check actual evidence and output. " * 400
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "not-created"
            with self.assertRaisesRegex(design.builder.BuildHold, "SKILL_MD_OVER_HOST_HARD_LIMIT"):
                design.design_build(d, str(target), write=True, hosts=["m365-agent-builder"])
            self.assertFalse(target.exists())
        receipt = design.design_build(d, hosts=["claude-code"])
        self.assertEqual([x["host"] for x in receipt["host_compatibility"]["profiles"]],
                         ["claude-code"])
        self.assertFalse(receipt["host_execution_observed"])

    def test_written_draft_does_not_package_research_notes_or_case(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "new-skill"
            receipt = design.design_build(case(), str(target), write=True)
            self.assertEqual(receipt["status"], "WRITTEN_DRAFT_REVIEW_REQUIRED")
            self.assertTrue((target / "SKILL.md").is_file())
            self.assertFalse((target / "design-case.json").exists())
            self.assertNotIn("fictional-adversarial-case-v1",
                             (target / "SKILL.md").read_text())
            self.assertEqual(receipt["files"], ["LICENSE", "SKILL.md"])
            self.assertFalse(receipt["semantic_task_quality_verified"])

    def test_composed_pack_has_required_handoff_and_optional_fallback(self):
        receipt = design.design_build(pack_case())
        self.assertEqual(receipt["kind"], "pack")
        self.assertIn("pack-handoff", receipt["design_gate"]["planned_adversarial_probes"])
        self.assertIn("optional-fallback", receipt["design_gate"]["planned_adversarial_probes"])
        self.assertEqual(receipt["design_gate"]["mapped_obligations"], 11)

    def test_complete_required_obligation_mapping(self):
        d = case()
        d["obligations"] = [x for x in d["obligations"]
                            if x["target"] != "verification"]
        self.reject(d, "UNCOVERED_BLUEPRINT_TARGETS")

    def test_unexpected_target_fails(self):
        d = case()
        d["obligations"][0]["target"] = "steps.unknown"
        self.reject(d, "UNKNOWN_OBLIGATION_TARGET")

    def test_reference_to_unknown_evidence_fails(self):
        d = case()
        d["obligations"][1]["evidence_ids"] = ["fake-corpus-id"]
        self.reject(d, "INVALID_REFERENCES")

    def test_reuse_not_implied_by_evidence_review(self):
        d = case()
        d["evidence"][0]["reuse_scope"] = "authorized-copy"
        self.reject(d, "SOURCE_REUSE_NOT_AUTHORIZED")

    def test_alleged_observation_does_not_authenticate_host_behavior(self):
        d = case()
        d["evidence"][0]["review_level"] = "host-observed-claimed"
        receipt = design.design_build(d)
        self.assertFalse(receipt["design_gate"]["source_identity_authenticated"])
        self.assertFalse(receipt["host_execution_observed"])

    def test_unlinked_obligation_probe_is_not_a_complete_design(self):
        d = case()
        d["probes"][2]["obligation_ids"].remove("requirement-6")
        self.reject(d, "UNTESTED_OBLIGATIONS")

    def test_missing_false_green_probe_refused(self):
        d = case()
        d["probes"] = [p for p in d["probes"] if p["kind"] != "false-green"]
        self.reject(d, "MISSING_ADVERSARIAL_PROBES")

    def test_false_green_cannot_expect_success(self):
        d = case()
        d["probes"][-1]["expected"] = "COMPLETE_IF_VERIFIED"
        self.reject(d, "UNSAFE_OR_FALSE_GREEN_PROBE_EXPECTATION")

    def test_probes_must_bind_to_relevant_obligations(self):
        d = case()
        d["probes"][1]["obligation_ids"] = ["requirement-1"]
        self.reject(d, "NEGATIVE_MISSING_NON_TRIGGER")

    def test_optional_pack_requires_fallback_probe(self):
        d = pack_case()
        d["probes"] = [p for p in d["probes"]
                        if p["kind"] != "optional-fallback"]
        self.reject(d, "MISSING_ADVERSARIAL_PROBES")

    def test_pack_probes_cannot_be_faked_as_single(self):
        d = case()
        d["decision"] = "COMPOSE_ORIGINAL"
        self.reject(d, "DECISION_BLUEPRINT_SHAPE_MISMATCH")

    def test_invalid_review_level_fails(self):
        d = case()
        d["evidence"][0]["review_level"] = "independent-certified"
        self.reject(d, "INVALID_REVIEW_LEVEL")

    def test_duplicate_evidence_id_fails(self):
        d = case()
        d["evidence"][1]["id"] = d["evidence"][0]["id"]
        self.reject(d, "DUPLICATE_EVIDENCE_ID")

    def test_blueprint_is_still_subject_to_original_content_boundary(self):
        d = case()
        d["blueprint"]["rights_declaration"] = "copied-from-online"
        self.reject(d, "ORIGINAL_RIGHTS_DECLARATION_REQUIRED")

    def test_maintainer_scope_without_write_is_refused(self):
        p = subprocess.run([sys.executable, str(ROOT / "engine" / "builder" /
               "design.py"), "--input", str(EXAMPLE),
               "--repository-maintenance"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 2)
        self.assertIn("MAINTENANCE_FLAG_WITHOUT_WRITE", p.stderr)

    def test_cli_dry_run_cannot_write_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "new"
            p = subprocess.run([sys.executable, str(ROOT / "engine" / "builder" /
                 "design.py"), "--input", str(EXAMPLE),
                 "--output", str(target)], capture_output=True, text=True)
            self.assertEqual(p.returncode, 0, p.stderr)
            self.assertFalse(target.exists())
            self.assertFalse(json.loads(p.stdout)["design_gate"]["probes_executed"])

    def test_existing_destination_cannot_be_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "existing"
            target.mkdir()
            self.reject_write(case(), target, "OUTPUT_EXISTS_OR_INVALID")

    def reject_write(self, d, target, code):
        with self.assertRaisesRegex(design.builder.BuildHold, code):
            design.design_build(d, output=str(target), write=True)

    def test_invalid_and_duplicate_json_fields_refused_by_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "case.json"
            for payload in ('{"schema_version":1,"schema_version":1}',
                            '{"schema_version":NaN}'):
                with self.subTest(payload=payload):
                    path.write_text(payload, encoding="utf-8")
                    p = subprocess.run([sys.executable,
                         str(ROOT / "engine" / "builder" / "design.py"),
                         "--input", str(path)], capture_output=True, text=True)
                    self.assertEqual(p.returncode, 2)
                    self.assertIn("SKILL_DESIGN_HOLD", p.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
