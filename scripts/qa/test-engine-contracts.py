#!/usr/bin/env python3
"""Optional read-only static Skillz engine contract regression tests.

This checks actual repository instructions and synthetic negative mutations.
It does NOT execute an agent, prove retrieval precision, qualify a skill,
approve installation, require CI, or replace independent semantic review.
Python 3.9+ stdlib; no network, writes, or toolchain installation.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
SKILLS = {
    "audit": "engine/skills/skill-audit/SKILL.md",
    "bootstrap": "engine/skills/skill-bootstrap/SKILL.md",
    "eval": "engine/skills/skill-eval/SKILL.md",
    "forge": "engine/skills/skill-forge/SKILL.md",
    "sync": "engine/skills/skill-sync/SKILL.md",
    "pulse": "engine/skills/skills-pulse/SKILL.md",
    "vetting": "engine/skills/source-vetting/SKILL.md",
}


def read(path):
    file = ROOT / path
    if file.is_symlink() or not file.is_file():
        raise AssertionError("required engine source unavailable: " + str(path))
    return file.read_text(encoding="utf-8")


def forge_location_error(text):
    """Deterministically detect a known wrong first-party destination rule."""
    expected = "5. Create or revise the full standalone skill package under **" + (
        "\x60skills/authored/<slug>/\x60**")
    if expected not in text:
        return "canonical authored location not enforced by Forge"
    if re.search(r"^5\.\s+Create.+under\s+\x60skills/<name>/\x60", text, re.M):
        return "legacy root-level skills destination is enforced"
    return None


def markdown_local_links(path, content):
    """Check simple in-repo Markdown references; complex forms need review."""
    dirname = (ROOT / path).parent
    errors = []
    for match in re.finditer(r"\]\(([^)\n]+)\)", content):
        target = match.group(1).split("#", 1)[0]
        if not target or re.match(r"^(?:https?://|mailto:|data:)", target):
            continue
        parts = []
        for part in target.replace("\\", "/").split("/"):
            if part in ("", "."):
                continue
            if part == "..":
                parts.append("..")
            else:
                parts.append(part)
        relative = "/".join(parts)
        try:
            resolved = (dirname / relative).resolve(strict=False)
            if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                errors.append(target)
        except (OSError, ValueError):
            errors.append(target)
    return errors


class EngineStaticContracts(unittest.TestCase):
    def test_all_seven_repo_bound_skills_have_metadata(self):
        for name, path in SKILLS.items():
            with self.subTest(name=name):
                data = read(path)
                self.assertTrue(data.startswith("---\nname: "))
                self.assertIn("\n  repo-bound: true\n", data)
                self.assertRegex(data, r"(?m)^  version: [0-9]+\.[0-9]+\.[0-9]+$")
                self.assertIn("\n# ", data)

    def test_maintainer_destination_agrees_with_template(self):
        forge = read(SKILLS["forge"])
        self.assertIsNone(forge_location_error(forge))
        self.assertIn("skills/authored/<slug>/", read("docs/skill-template.md"))
        self.assertTrue((ROOT / "skills/authored").is_dir())
        self.assertIn("registry/skills/local-skills/<slug>.yaml", forge)
        self.assertIn("registry/verification/local-skills/<slug>.yaml", forge)

    def test_negative_mutation_of_forge_path_is_caught(self):
        original = read(SKILLS["forge"])
        bad = original.replace(
            "5. Create or revise the full standalone skill package under **"
            "\x60skills/authored/<slug>/\x60**",
            "5. Create or revise the full skill package under \x60skills/<name>/\x60",
        )
        self.assertNotEqual(original, bad)
        self.assertIsNotNone(forge_location_error(bad))

    def test_forge_respects_user_artifact_boundary_and_offline_closure(self):
        forge = read(SKILLS["forge"])
        self.assertIn("normal FIRST_VISIT or RETURNING_USER", forge)
        self.assertIn("mandatory instructions and their supporting files", forge.casefold())
        self.assertIn("must ship", forge)
        self.assertIn("stronger", forge)
        self.assertIn("old version\'s passing tests", forge)

    def test_eval_separates_static_deterministic_host_and_consumer(self):
        report = read(SKILLS["eval"])
        for value in ("four distinct evidence layers", "consumer/user",
                      "observed agent behavior", "counterexample",
                      "A score cannot average away"):
            with self.subTest(fragment=value):
                self.assertIn(value, report)

    def test_discovery_requires_false_positive_and_false_negative_probes(self):
        bootstrap = read(SKILLS["bootstrap"])
        for value in ("False positive probe", "False negative probe",
                      "Same-name/different-job probe", "Partial-corpus probe",
                      "Silent first-party bias probe", "serialized JSON keys"):
            with self.subTest(fragment=value):
                self.assertIn(value, bootstrap)
        self.assertNotIn("local 44", bootstrap)

    def test_pulse_does_not_impose_small_fixed_source_cap(self):
        pulse = read(SKILLS["pulse"])
        self.assertIn("pages/chunks/cursors", pulse)
        self.assertIn("precision probe", pulse)
        self.assertIn("recall probe", pulse)
        self.assertNotIn("Inspect a small, relevant set", pulse)

    def test_sync_requires_complete_package_and_destination_readback(self):
        sync = read(SKILLS["sync"])
        self.assertIn("all mandatory references", sync)
        self.assertIn("Verify the actual destination", sync)
        self.assertIn("COPIED_PARTIAL", sync)
        self.assertIn("readback", sync)

    def test_source_vetting_separates_mirrors_packages_and_rights(self):
        source = read(SKILLS["vetting"])
        for value in ("Mirror as origin", "Root license as blanket permission",
                      "One page as whole source", "Instruction-in-source"):
            self.assertIn(value, source)

    def test_audit_catches_cross_engine_drift(self):
        audit = read(SKILLS["audit"])
        self.assertIn("High-impact drift probes", audit)
        self.assertIn("Authoring destination", audit)
        self.assertIn("Evaluation depth", audit)
        self.assertIn("Evidence freshness", audit)

    def test_policy_allows_optional_package_testing_without_runtime_mandate(self):
        policy = read("docs/skill-verification.md")
        self.assertIn("no always-on testing runtime or mandatory CI", policy)
        self.assertIn("skill-owned scripts", policy)
        self.assertIn("offline deterministic fixtures", policy)
        self.assertNotIn("No tests, harnesses, CI, runtime, or other execution machinery belong", policy)

    def test_refinement_skill_is_a_complete_portable_package(self):
        root = "skills/authored/evidence-driven-refinement-loop/"
        for required in ("SKILL.md", "README.md", "LICENSE", "examples/acceptance.md"):
            self.assertTrue((ROOT / (root + required)).is_file())
        skill = read(root + "SKILL.md")
        for fragment in ("OBSERVE the delivered result", "EXPLAIN a testable mechanism",
                         "CHANGE the smallest adequate surface",
                         "CHALLENGE the candidate", "DECIDE against the frozen criteria",
                         "STOP_NO_CHANGE", "Do not trigger", "fresh, action-specific approval"):
            self.assertIn(fragment, skill)
        self.assertEqual(markdown_local_links(root + "SKILL.md", skill), [])

    def test_iteration_method_can_refuse_false_improvement(self):
        root = "skills/authored/evidence-driven-refinement-loop/"
        skill = read(root + "SKILL.md")
        cases = read(root + "examples/acceptance.md")
        self.assertIn("green", skill.lower())
        self.assertIn("REVERT", skill)
        self.assertIn("HOLD", skill)
        self.assertIn("STOP_NO_CHANGE", skill)
        self.assertIn("False success", cases)
        self.assertIn("Misleading tests and stale evidence", cases)
        self.assertIn("Improvement that sacrifices a hard invariant", cases)
        self.assertGreaterEqual(len(re.findall(r"(?m)^## Case [0-9]+:", cases)), 8)

    def test_engine_development_adopts_refinement_without_a_runtime_dependency(self):
        forge = read(SKILLS["forge"])
        evaluator = read(SKILLS["eval"])
        bootstrap = read(SKILLS["bootstrap"])
        template = read("docs/skill-template.md")
        self.assertIn("Iterative improvement as an execution discipline", forge)
        self.assertIn("Repeatable review of the newly corrected candidate", evaluator)
        self.assertIn("Iterate on a real artifact", bootstrap)
        self.assertIn("Built-in iterative refinement", template)
        for body in (forge, evaluator, bootstrap, template):
            self.assertIn("evidence", body.lower())
        self.assertIn("not a runtime dependency", forge)

    def test_modified_engine_markdown_links_are_local_and_present(self):
        for name, path in SKILLS.items():
            with self.subTest(name=name):
                self.assertEqual(markdown_local_links(path, read(path)), [])

    def test_negative_mutation_of_evidence_separation_detectable(self):
        original = read(SKILLS["eval"])
        changed = original.replace("four distinct evidence layers", "single score")
        self.assertNotEqual(original, changed)
        self.assertNotIn("four distinct evidence layers", changed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
