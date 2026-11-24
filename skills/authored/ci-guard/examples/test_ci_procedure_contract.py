"""Structural regression for relocated normative instructions; no host claim."""
from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[1]

class ProcedureContractTests(unittest.TestCase):
    def test_required_procedure_is_present_and_bounded(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf8")
        procedure = (ROOT / "procedure-contract.md").read_text(encoding="utf8")
        self.assertLess(len(skill), 20000)
        self.assertIn("[procedure-contract.md](procedure-contract.md)", skill)
        self.assertIn("normative", skill)
        self.assertIn("HOLD affected work", skill)
        self.assertEqual(procedure.count("\n## P0:"), 9)
        for heading in ("## Classification-first budget contract", "## Decision procedure", "## Report contract"):
            self.assertIn(heading, procedure)
        self.assertIn("untrusted pull request", procedure)
        self.assertIn("Never claim savings", procedure)

if __name__ == "__main__":
    unittest.main()
