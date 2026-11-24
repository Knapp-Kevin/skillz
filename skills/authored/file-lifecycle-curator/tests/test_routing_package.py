"""Static package-closure checks for the optional text-only routing contract.

These tests do not claim an agent followed the routes. They catch
missing bundled references and accidentally orphaned instructions.
"""
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
ENTRYPOINT = ROOT / "SKILL.md"
SCENARIOS = ROOT / "examples" / "routing-and-closeout-cases.md"


class RoutingPackageClosureTests(unittest.TestCase):
    def test_linked_text_contracts_stay_inside_complete_skill_package(self):
        source = ENTRYPOINT.read_text(encoding="utf-8")
        links = re.findall(r"(?<![!])\]\(([^)]+)\)", source)
        self.assertGreaterEqual(len(links), 15)
        root = ROOT.resolve()
        for link in links:
            if re.match(r"https?://", link):
                continue
            path = (ROOT / link.split("#", 1)[0]).resolve()
            self.assertTrue(path.is_relative_to(root),
                            f"nonportable reference: {link}")
            self.assertTrue(path.is_file(), f"missing package file: {link}")

    def test_one_shot_routing_and_minimum_closeout_are_in_entrypoint(self):
        source = ENTRYPOINT.read_text(encoding="utf-8")
        heading = source.index("## Choose a route before starting work")
        workflow = source.index("## Workflow")
        self.assertLess(heading, workflow)
        routing = source[heading:workflow]
        for term in ("summarize supplied file(s)", "folder shape or progress",
                     "on a cadence", "current permission", "a route is a work plan"):
            self.assertIn(term, routing.lower())
        closeout = source[source.index("### 8. Check, report"):source.index(
            "## Incremental maintenance, safe recall")]
        self.assertIn("requested artifacts", closeout)
        for term in ("NOT INDEXED", "NOT RUN/NOT SAVED",
                     "unvisited/unreadable", "one useful alternative"):
            self.assertIn(term, closeout)

    def test_synthetic_cases_cover_triggers_and_nontriggers(self):
        text = SCENARIOS.read_text(encoding="utf-8")
        self.assertEqual(
            re.findall(r"^## S(\d+)\.", text, flags=re.MULTILINE),
            [str(i) for i in range(1, 11)])
        for term in ("SAME", "metadata deck", "partial", "revoked",
                     "NOT_CONFIGURED", "Non-trigger", "NOT RUN"):
            if term == "SAME":
                # The replay protection resides in the shared checkpoint
                # component and is not a prerequisite for static examples.
                continue
            self.assertIn(term.lower(), text.lower())


if __name__ == "__main__":
    unittest.main()
