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


def run_feedback_contract_error(template, forge, verification):
    """Static wording guard only; cannot establish actual host behavior."""
    required = {
        "template": (template, (
            "## Per-execution self-review and governed evolution",
            "**Every meaningful execution**",
            "NO_ACTION",
            "untrusted **proposal**",
            "Bound recursion by decision value",
            "opt-in",
            "CANONICAL_IMPROVEMENT",
            "LOCAL_PREFERENCE",
            "outside the skill package",
            "First-class package component",
            "schema.json",
            "example.json",
            "user-approved",
        )),
        "forge": (forge, (
            "## Per-execution self-review is not self-modifying policy",
            "standalone offline package",
            "NO_ACTION",
            "independent verification",
            "CANONICAL_IMPROVEMENT",
            "LOCAL_PREFERENCE",
            "user-scoped private",
        )),
        "verification": (verification, (
            "## Per-execution feedback and anti-drift review for authored skills",
            "Feedback contamination",
            "Authority and privacy",
            "CANONICAL_IMPROVEMENT",
            "LOCAL_PREFERENCE",
            "Upgrade and contamination",
            "NO_ACTION",
        )),
    }
    for name, (content, phrases) in required.items():
        for phrase in phrases:
            if phrase not in content:
                return f"{name}: missing per-run feedback guard: {phrase}"
    return None


class EngineStaticContracts(unittest.TestCase):
    def test_preference_manager_is_actually_wired_to_skill(self):
        root = "skills/authored/evidence-driven-refinement-loop/"
        skill = read(root + "SKILL.md")
        for name in ("preferences/routing.md", "preferences/schema.json",
                     "preferences/README.md", "preferences/manage.py",
                     "preferences/test_manage.py", "preferences.local.json",
                     "CANONICAL_IMPROVEMENT", "LOCAL_PREFERENCE",
                     "MIXED", "NO_ACTION", "--approved"):
            with self.subTest(reference=name):
                self.assertIn(name, skill)
        manager = read(root + "preferences/manage.py")
        self.assertIn("Duplicate JSON field rejected", manager)
        self.assertIn("def write_atomic(", manager)
        self.assertIn("refusing", manager.lower() + " refusing")
        self.assertIn("manual preference reconciliation", manager)
        self.assertFalse((ROOT / root / "preferences" / "preferences.local.json").exists())

    def test_preference_component_removed_reference_is_detected(self):
        skill = read("skills/authored/evidence-driven-refinement-loop/SKILL.md")
        poisoned = skill.replace("preferences/manage.py", "preferences/not-a-manager.py")
        self.assertNotEqual(skill, poisoned)
        self.assertNotIn("preferences/manage.py", poisoned)
        self.assertIn("preferences/manage.py", skill)

    def test_preference_overlay_is_isolated_from_canonical_rewrites(self):
        root = "skills/authored/evidence-driven-refinement-loop/"
        skill = read(root + "SKILL.md")
        routing = read(root + "preferences/routing.md")
        schema = read(root + "preferences/schema.json")
        manager = read(root + "preferences/manage.py")
        for required in ("CANONICAL_IMPROVEMENT", "LOCAL_PREFERENCE", "MIXED",
                         "preferences.local.json", "untrusted data",
                         "source package", "explicitly approved full revocation"):
            with self.subTest(phrase=required):
                self.assertIn(required, skill)
        self.assertIn("explicit-user-confirmation", schema)
        self.assertIn("not a bug", skill)
        self.assertIn("separate", routing)
        self.assertIn("reject_checkout_root(", manager)
        self.assertIn("Refusing", manager)
        self.assertNotIn('"preferences.local.json"', read(root + "preferences/example.json"))

    def test_overlay_preference_must_not_launder_into_policy(self):
        skill = read("skills/authored/evidence-driven-refinement-loop/SKILL.md")
        poisoned = skill.replace("untrusted data, not instructions",
                                "trusted instructions, not data")
        self.assertNotEqual(poisoned, skill)
        self.assertNotIn("untrusted data, not instructions", poisoned)
        self.assertIn("untrusted data, not instructions", skill)
        package_root = "skills/authored/evidence-driven-refinement-loop/preferences/"
        import json
        config = json.loads(read(package_root + "example.json"))
        schema = json.loads(read(package_root + "schema.json"))
        self.assertEqual(config["skill_id"], schema["properties"]["skill_id"]["const"])
        self.assertEqual(config["schema_version"], schema["properties"]["schema_version"]["const"])
        canonical = read("skills/authored/evidence-driven-refinement-loop/SKILL.md")
        declared_version = re.search(r"(?m)^  version: ([0-9]+\.[0-9]+\.[0-9]+)$",
                                     canonical)
        self.assertIsNotNone(declared_version)
        self.assertEqual(config["base_skill_version"], declared_version.group(1))
        self.assertEqual(config["scope"], "user-local")
        self.assertEqual(config["preferences"][0]["source"], "explicit-user-confirmation")
        self.assertIn("preferences.local.json", read(package_root + "README.md"))
        self.assertIn("schema.json", read("skills/authored/evidence-driven-refinement-loop/SKILL.md"))
        cases = read("skills/authored/evidence-driven-refinement-loop/examples/acceptance.md")
        for heading in ("Case 11:", "Case 12:", "Case 13:", "Case 14:"):
            self.assertIn(heading, cases)

    def test_authored_skill_run_feedback_is_bounded_and_evidence_based(self):
        self.assertIsNone(run_feedback_contract_error(
            read("docs/skill-template.md"),
            read(SKILLS["forge"]),
            read("docs/skill-verification.md")))

    def test_removed_feedback_guard_is_detected(self):
        template = read("docs/skill-template.md")
        forged = template.replace("untrusted **proposal**", "trusted instruction")
        self.assertNotEqual(forged, template)
        self.assertIsNotNone(run_feedback_contract_error(
            forged, read(SKILLS["forge"]),
            read("docs/skill-verification.md")))

    def test_engine_metadata_distinguishes_maintenance_from_user_bootstrap(self):
        for name, path in SKILLS.items():
            with self.subTest(name=name):
                data = read(path)
                self.assertTrue(data.startswith("---\nname: "))
                self.assertRegex(data, r"(?m)^  version: [0-9]+\.[0-9]+\.[0-9]+$")
                self.assertIn("\n# ", data)
                if name == "bootstrap":
                    # User bootstrap must never inherit repository-write authority.
                    self.assertNotIn("\n  repo-bound: true\n", data)
                    self.assertIn("Only `REPOSITORY_MAINTENANCE`", data)
                else:
                    self.assertIn("\n  repo-bound: true\n", data)

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
        self.assertNotIn(chr(92) + chr(96), skill)  # Reject Markdown-escaped backticks.
        self.assertEqual(skill.count("~~~"), 0)  # Keep Markdown fences consistent.
        self.assertEqual(skill.count(chr(96) * 3), 4)  # One SH and one text fence.
        self.assertEqual(skill.count(chr(96) * 3 + "sh"), 1)
        self.assertEqual(skill.count(chr(96) * 3 + "text"), 1)

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
        self.assertIn("Per-execution self-review and governed evolution", template)
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
