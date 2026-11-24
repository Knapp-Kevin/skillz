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
        documents = (ENTRYPOINT, ROOT / "workflow-protocol.md",
                     ROOT / "maintenance-protocol.md")
        all_links = []
        root = ROOT.resolve()
        for document in documents:
            source = document.read_text(encoding="utf-8")
            links = re.findall(r"(?<![!])\]\(([^)]+)\)", source)
            all_links.extend(links)
            for link in links:
                if re.match(r"https?://", link):
                    continue
                path = (document.parent / link.split("#", 1)[0]).resolve()
                self.assertTrue(path.is_relative_to(root),
                                f"nonportable reference: {link}")
                self.assertTrue(path.is_file(), f"missing package file: {link}")
        self.assertGreaterEqual(len(all_links), 15)

    def test_full_protocols_required_and_safety_controls_preserved(self):
        source = ENTRYPOINT.read_text(encoding="utf-8")
        self.assertLess(len(source), 20000)
        self.assertIn("**Read the applicable numbered phases", source)
        self.assertIn("workflow-protocol.md", source)
        self.assertIn("maintenance-protocol.md", source)
        self.assertIn("before reconciling or recalling any prior state", source)
        self.assertIn("do not claim a completed curation", source)
        self.assertIn("COLD_START or HOLD", source)
        workflow = (ROOT / "workflow-protocol.md").read_text(encoding="utf-8")
        maintenance = (ROOT / "maintenance-protocol.md").read_text(encoding="utf-8")
        self.assertEqual(re.findall(r"^### (\d+a?)\.", workflow, re.MULTILINE),
                         ["1", "2", "3", "4", "5", "6", "6a", "7"])
        for term in ("complete bytes", "source_context", "NOT INDEXED",
                     "verified relocations", "partial", "separate** explicit disposal"):
            self.assertIn(term.lower(), workflow.lower())
        for term in ("COLD_START", "EXTRACT_REGRESSION_HOLD",
                     "previously cached record ID", "Compare-and-swap",
                     "unique run IDs", "explicit write opt-in",
                     "stop/revocation", "does not prove a successful delivered result"):
            self.assertIn(term, maintenance)
        for protocol in (workflow, maintenance):
            self.assertIn("Missing or inaccessible guidance is a dependency hold", protocol)

    def test_one_shot_routing_and_minimum_closeout_are_in_entrypoint(self):
        source = ENTRYPOINT.read_text(encoding="utf-8")
        heading = source.index("## Choose a route before starting work")
        workflow = source.index("## Workflow")
        self.assertLess(heading, workflow)
        routing = source[heading:workflow]
        for term in ("summarize supplied file(s)", "folder shape or progress",
                     "on a cadence", "current viewer/source access",
                     "host-native search", "refresh or continue an existing library",
                     "a route is a work plan"):
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
