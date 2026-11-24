#!/usr/bin/env python3
"""Offline adversarial structural tests for a fictional portfolio README.

These tests check only local anchors, completeness, duplicate presentation
and explicitly unverified remote links. They do NOT simulate a real reader
or prove a dependency graph, external URL, brand, or semantic quality.
"""
from pathlib import Path
import re
import sys
import tempfile
import unittest

PACKAGE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE / "scripts"))
import check_readme as links

EXAMPLE = PACKAGE / "examples" / "abstraction-portfolio-example.md"
ROLES = ("Experiences", "Coordination", "Shared capabilities",
         "Foundations", "Independent work")
EXPECTED = frozenset((
    "Lantern Board", "Trail Studio", "Junction Desk", "Gateway Contract",
    "Pattern Engine", "Record Toolkit", "Seed Core", "Symbol Format",
    "Field Notes",
))
ITEM = re.compile(r"^- \*\*\[([^\]]+)\]\((https://example\.invalid/[^)]+)\)\*\*", re.M)


class AbstractionNavigationTests(unittest.TestCase):
    def text(self):
        return EXAMPLE.read_text(encoding="utf-8")

    def inspect(self, body):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = root / "README.md"
            readme.write_text(body, encoding="utf-8")
            return links.audit(root, readme)

    def test_every_fictional_project_is_listed_once(self):
        matches = ITEM.findall(self.text())
        names = [name for name, _ in matches]
        self.assertEqual(len(matches), len(EXPECTED))
        self.assertEqual(set(names), EXPECTED)
        self.assertEqual(len(names), len(set(names)))

    def test_primary_abstraction_order_is_descending(self):
        body = self.text()
        loc = [body.index("#### " + role) for role in ROLES]
        self.assertEqual(loc, sorted(loc))

    def test_local_layer_navigation_has_valid_anchors(self):
        report = self.inspect(self.text())
        self.assertEqual(report["local_blockers"], 0)
        self.assertGreaterEqual(report["counts"].get("LOCAL_ANCHOR_FOUND", 0), 5)

    def test_wrong_layer_link_is_detected_not_ignored(self):
        body = self.text().replace("(#foundations)", "(#invented-foundations)")
        report = self.inspect(body)
        self.assertGreater(report["counts"].get("BROKEN_LOCAL_ANCHOR", 0), 0)

    def test_remote_example_domains_remain_unverified(self):
        report = self.inspect(self.text())
        self.assertGreaterEqual(report["counts"].get("EXTERNAL_NOT_CHECKED", 0), 9)
        self.assertFalse(report["external_links_tested"])
        self.assertFalse(report["readme_claims_verified"])
        self.assertFalse(report["reader_success_verified"])

    def test_unrelated_work_and_relation_caveats_survive(self):
        body = self.text()
        self.assertIn("#### Independent work", body)
        self.assertIn("not automatically a build dependency", body)
        self.assertIn("conceptual layers do not establish actual", body)
        self.assertIn("NOT_RUN", body)

    def test_package_guidance_covers_alternatives_and_false_dependencies(self):
        guide = (PACKAGE / "SKILL.md").read_text(encoding="utf-8")
        procedure = (PACKAGE / "procedure-contract.md").read_text(encoding="utf-8")
        self.assertIn("](procedure-contract.md)", guide)
        self.assertLess(len(guide), 20000)
        self.assertIn("## Binding quality profiles:", procedure)
        self.assertIn("## Four mandatory README delivery safeguards", procedure)
        self.assertIn("## Five-step production method", procedure)
        self.assertIn("## Portfolio and multi-project information architecture:", procedure)
        self.assertIn("abstraction-first", guide)
        self.assertIn("flat", guide)
        self.assertIn("conceptual layer", guide)
        self.assertIn("dependency", guide)
        self.assertIn("unclassified", guide.lower())
        self.assertIn("complete", guide.lower())


if __name__ == "__main__":
    unittest.main()
