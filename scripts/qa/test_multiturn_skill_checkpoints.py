#!/usr/bin/env python3
"""Static cross-skill continuation checkpoints, not consuming-agent evaluation."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
AUTH = ROOT / "skills" / "authored"

CASES = {
    "ci-guard": ("CI-specific continuation checkpoints",
                 "exact\nsource revision", "native and security", "older revision",
                 "open PR", "incomplete host attempt"),
    "repository-delivery-assessor": ("Delivery-assessment continuation checkpoints",
                                    "verified\nrevision/as-of", "blocked merges",
                                    "as current", "a merge"),
    "repository-readme-architect": ("README-work continuation checkpoints",
                                   "generator-owned regions", "preservation baselines",
                                   "merged PR", "user comprehension"),
    "evidence-driven-refinement-loop": ("Refinement-loop continuation checkpoints",
                                        "actual starting\nbaseline", "falsifier",
                                        "previously failed negative control",
                                        "owner\nconstraints", "new material failure"),
}


class CrossSkillSourceCases(unittest.TestCase):
    def test_each_complex_skill_has_domain_specific_continuity(self):
        for name, required in CASES.items():
            with self.subTest(skill=name):
                text = (AUTH / name / "SKILL.md").read_text(encoding="utf8")
                normalized = " ".join(text.lower().split())
                for phrase in required:
                    self.assertIn(" ".join(phrase.lower().split()), normalized)

    def test_common_and_specific_sections_not_competing(self):
        for name in (*CASES, "context-continuation-contract"):
            with self.subTest(skill=name):
                source = (AUTH / name / "SKILL.md").read_text(encoding="utf8")
                self.assertEqual(source.count("## Multi-turn continuity when the work is not one-shot"), 1)
                self.assertEqual(source.count("## Optional, anonymized-content skill feedback"), 1)
                self.assertLess(source.index("## Multi-turn continuity when the work is not one-shot"),
                                source.index("## Optional, anonymized-content skill feedback"))
                self.assertIn("Do not invent unavailable history or claim persistent storage.", source)

    def test_context_package_offers_offline_checker_as_optional(self):
        source = (AUTH / "context-continuation-contract" / "SKILL.md").read_text(encoding="utf8")
        self.assertIn("scripts/check_transition.py", source)
        self.assertIn("STATIC_TRANSITION_RECONCILED", source)
        self.assertIn("independent host authorization", source)
        self.assertIn("optional", source.lower())
        self.assertIn("does not", source.lower())

    def test_agent_host_outcomes_are_not_claimed(self):
        guide = (AUTH / "context-continuation-contract" /
                 "examples" / "multiturn-adversarial.md").read_text(encoding="utf8")
        self.assertIn("model_agent_behavior_observed:false", guide)
        self.assertIn("synthetic source-stage controls", guide.lower())
        self.assertIn("separately execute each transcript", guide)
        self.assertNotIn("independent agent trial passed", guide.lower())

    def test_all_four_domains_covered_in_fictional_matrix(self):
        guide = (AUTH / "context-continuation-contract" /
                 "examples" / "multiturn-adversarial.md").read_text(encoding="utf8")
        for label in ("CI Guard", "Repository Delivery Assessor",
                      "Repository README Architect",
                      "Evidence-Driven Refinement Loop"):
            self.assertIn(label, guide)

    def test_no_mandatory_sibling_skill_dependency(self):
        for name in CASES:
            text = (AUTH / name / "SKILL.md").read_text(encoding="utf8")
            # This source-only acceptance test is deliberately narrow:
            # skills still need independent host tests for true portability.
            self.assertNotIn("install context-continuation-contract first", text.lower())
            self.assertIn("No autonomous follow-up, session creation", text)


if __name__ == "__main__":
    unittest.main()
