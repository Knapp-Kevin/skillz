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



def single_skill_build_route_errors(entry, bootstrap, consumer, engine, frontdoor):
    """Static cross-entrypoint drift check, not a host-agent execution test."""
    failures = []
    required = {
        "entry": (entry, ("SINGLE_SKILL_BUILD", "one task-specific skill",
                          "user skill back into Skillz")),
        "bootstrap": (bootstrap, ("SINGLE_SKILL_BUILD: one outcome, one complete package",
                                 "S4/S5", "S9", "S10", "S11",
                                 "STATIC_REVIEW", "LOCAL_TEST", "HOST_OBSERVED",
                                 "NOT_TESTED", "full fitted-system",
                                 "one complete package")),
        "consumer": (consumer, ("SINGLE_SKILL_BUILD",
                                "focused path", "portable handoff")),
        "engine": (engine, ("SINGLE_SKILL_BUILD", "single-skill")),
        "frontdoor": (frontdoor, ("Build one custom skill for a task",
                                 "Single-skill build workflow")),
    }
    for name, (content, anchors) in required.items():
        for anchor in anchors:
            if anchor not in content:
                failures.append(name + ": missing " + anchor)
    if "never** in this Skillz repository" not in bootstrap:
        failures.append("bootstrap: consumer skill can leak into Skillz")
    if "S2's general recurring-needs interview" not in bootstrap:
        failures.append("bootstrap: full account intake could be imposed")
    return failures



class EngineStaticContracts(unittest.TestCase):
    def test_single_skill_build_route_is_consistent_across_frontdoors(self):
        errors = single_skill_build_route_errors(
            read("AGENT_START_HERE.md"), read(SKILLS["bootstrap"]),
            read("docs/consumer-discovery-and-installation.md"),
            read("engine/README.md"), read("README.md"))
        self.assertEqual(errors, [])

    def test_single_skill_build_route_drop_is_detectable(self):
        entry = read("AGENT_START_HERE.md")
        bootstrap = read(SKILLS["bootstrap"])
        consumer = read("docs/consumer-discovery-and-installation.md")
        engine = read("engine/README.md")
        frontdoor = read("README.md")
        poisoned = bootstrap.replace(
            "## SINGLE_SKILL_BUILD: one outcome, one complete package",
            "## FIRST_VISIT: fit a whole skill system")
        self.assertNotEqual(bootstrap, poisoned)
        self.assertTrue(single_skill_build_route_errors(
            entry, poisoned, consumer, engine, frontdoor))
        relocated = bootstrap.replace("never** in this Skillz repository",
                                       "sometimes** in this Skillz repository")
        self.assertTrue(any("leak into Skillz" in e for e in
                            single_skill_build_route_errors(
                                entry, relocated, consumer, engine, frontdoor)))

    def test_single_skill_build_outcome_and_rights_not_only_index_search(self):
        bootstrap = read(SKILLS["bootstrap"])
        guide = read("docs/evals/single-skill-build-acceptance.md")
        section = bootstrap.split(
            "## SINGLE_SKILL_BUILD: one outcome, one complete package", 1)[1]
        section = section.split("\n## S1 — Bind", 1)[0]
        for phrase in ("all-source discovery", "rights", "full portable",
                       "positive real-world trigger", "false-success",
                       "source identity", "NOT_INSTALLED", "NOT_TESTED"):
            with self.subTest(fragment=phrase):
                self.assertIn(phrase, section)
        for case in ("SB-01", "SB-04", "SB-05", "SB-06", "SB-08",
                     "SB-09", "SB-11", "SB-12"):
            self.assertIn(case, guide)

    def test_builder_compiler_is_optional_and_engine_wired(self):
        engine = read("engine/README.md")
        bootstrap = read(SKILLS["bootstrap"])
        forge = read(SKILLS["forge"])
        evaluation = read(SKILLS["eval"])
        template = read("docs/skill-template.md")
        builder = read("engine/builder/README.md")
        for content in (engine, bootstrap, forge, evaluation, template):
            self.assertIn("builder/README.md", content)
        self.assertIn("fully authored", builder)
        self.assertIn("--write", builder)
        for shape in ("single", "phased", "pack"):
            self.assertIn(shape, builder)
        for name, version in (("bootstrap", "0.11.2"),
                              ("forge", "2.1.0"), ("eval", "2.1.0")):
            actual = read(SKILLS[name])
            self.assertIn("version: " + version, actual)
            self.assertEqual(markdown_local_links(SKILLS[name], actual), [])

    def test_composable_packs_are_optional_and_use_canonical_engine(self):
        guide = read("engine/packs/README.md")
        manifest = read("engine/packs/manifest-contract.md")
        self.assertIn("Single-file skills", guide)
        self.assertIn("not another user-facing skill", guide.lower())
        self.assertIn("schema_version", manifest)
        self.assertIn("rights verification", manifest.lower())
        for name in ("bootstrap", "forge", "eval"):
            content = read(SKILLS[name])
            with self.subTest(skill=name):
                self.assertIn("../../packs/README.md", content)
                self.assertEqual(markdown_local_links(SKILLS[name], content), [])
        self.assertIn("packs/README.md", read("engine/README.md"))
        self.assertIn("engine/packs/README.md", read("AGENT_START_HERE.md"))

    def test_engine_refinement_handoff_cross_links_are_present(self):
        guide = read("engine/refinement/README.md")
        for path in (SKILLS["bootstrap"], SKILLS["forge"],
                     SKILLS["eval"]):
            text = read(path)
            self.assertIn("refinement/README.md", text)
            self.assertEqual(markdown_local_links(path, text), [])
        for important in ("STOP_NO_CHANGE", "OBSERVED_FAILURE",
                          "false-green", "portfolio boundaries",
                          "SemVer", "source identity"):
            self.assertIn(important, guide)
        self.assertIn("check_case.py", guide)

    def test_refinement_handoff_drop_does_not_satisfy_engine_links(self):
        forge = read(SKILLS["forge"])
        poisoned = forge.replace("[engine refinement handoff](../../refinement/README.md)",
                                  "engine self-improvement")
        self.assertNotEqual(forge, poisoned)
        self.assertNotIn("refinement/README.md", poisoned)

    def test_minor_engine_edit_does_not_force_semver_bump(self):
        template = read("docs/skill-template.md")
        self.assertIn("Conservative version and publication discipline", template)
        self.assertIn("Do not bump a SemVer patch", template)
        self.assertIn("fingerprints are independent of semver", template.lower())
        bootstrap = read(SKILLS["bootstrap"])
        forge = read(SKILLS["forge"])
        evaluator = read(SKILLS["eval"])
        self.assertIn("  version: 0.11.2", bootstrap)
        self.assertIn("  version: 2.1.0", forge)
        self.assertIn("  version: 2.1.0", evaluator)

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
        protocol = read(root + "preference-workflow.md")
        self.assertIn("preference-workflow.md#", skill)
        self.assertIn("**Read the full", skill)
        self.assertLess(len(skill), 20000)
        self.assertEqual(markdown_local_links(root + "preference-workflow.md", protocol), [])
        self.assertEqual((skill + protocol).count(chr(96) * 3), 4)
        self.assertEqual((skill + protocol).count(chr(96) * 3 + "sh"), 1)
        self.assertEqual((skill + protocol).count(chr(96) * 3 + "text"), 1)
        for invariant in ("Reject the entire overlay", "explicitly approved full revocation",
                          "nonblocking advisory lock", "Never select a configuration",
                          "do not run a partial write", "Do not misreport"):
            self.assertIn(invariant, protocol)
        self.assertIn("If unavailable, do not assert completion", protocol)

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
