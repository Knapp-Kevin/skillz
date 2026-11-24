"""Offline structural checks of two original sales-method skill packages.

These tests inspect text and package closure only. They do not simulate
a real buyer, train a salesperson, test independent agent interpretation,
verify third-party trademarks, or grant external account access.
"""
import re
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2] / "skills" / "authored"
SLUGS = ("sandler-conversation-strategist", "meddpicc-opportunity-assurance")


class MethodologyPackageTests(unittest.TestCase):
    def skill(self, slug):
        return (ROOT / slug / "SKILL.md").read_text(encoding="utf-8")

    def test_complete_offline_package_links(self):
        for slug in SLUGS:
            with self.subTest(slug=slug):
                base = (ROOT / slug).resolve()
                self.assertTrue((base / "LICENSE").is_file())
                self.assertTrue((base / "examples" / "acceptance.md").is_file())
                self.assertTrue((base / "references" / "advanced-practice.md").is_file())
                links = re.findall(r"(?<!!)\]\(([^)]+)\)", self.skill(slug))
                self.assertGreaterEqual(len(links), 2)
                for link in links:
                    if link.startswith(("https://", "http://")):
                        continue
                    ref = (base / link.split("#", 1)[0]).resolve()
                    self.assertTrue(ref.is_relative_to(base), link)
                    self.assertTrue(ref.is_file(), link)

    def test_both_are_original_unaffiliated_and_not_silent_operators(self):
        for slug in SLUGS:
            with self.subTest(slug=slug):
                doc = self.skill(slug).lower()
                self.assertRegex(doc, r"(not affiliated|no affiliation)")
                self.assertIn("original", doc)
                self.assertIn("without separately", doc)
                self.assertIn("do not", doc)
                self.assertIn("crm", doc)
                self.assertIn("schedule", doc)
                self.assertTrue("untrusted data" in doc or "as **data**" in doc)
                self.assertIn("buyer", doc)

    def test_sandler_is_buyer_conversation_not_vendor_certification(self):
        text = self.skill(SLUGS[0]).lower()
        for word in ("rapport", "up-front", "pain", "budget",
                     "decision", "fulfillment", "post-decision",
                     "no-fit", "buyer autonomy", "certification"):
            self.assertIn(word, text)

    def test_meddpicc_factor_coverage_and_no_fake_probability(self):
        text = self.skill(SLUGS[1]).lower()
        for factor in ("metrics", "economic buyer", "decision criteria",
                       "decision process", "paper process", "pain",
                       "champion", "competition"):
            self.assertIn(factor, text)
        self.assertIn("do not compute an automatic close probability", text)
        self.assertIn("seller_inferred", text)
        self.assertIn("disconfirmed", text)

    def test_crosswalk_does_not_promote_evidence(self):
        for slug in SLUGS:
            text = self.skill(slug).lower()
            self.assertIn("optional", text)
            self.assertIn("not", text)
            self.assertTrue("not automatically" in text or "not automatically infer" in text)

    def test_adversarial_cases_include_nontrigger_and_missing_authority(self):
        for slug in SLUGS:
            cases = (ROOT / slug / "examples" / "acceptance.md").read_text().lower()
            self.assertIn("nontrigger", cases)
            self.assertTrue("expect" in cases or "expected" in cases)
            self.assertIn("no", cases)
            self.assertTrue("privacy" in cases or "access" in cases)

    def test_buyer_evidence_is_not_promoted_from_seller_quotes(self):
        sandler = self.skill(SLUGS[0])
        med = self.skill(SLUGS[1])
        self.assertIn("SELLER_ASSERTED", sandler)
        self.assertIn("buyer quote", sandler.lower())
        self.assertIn("BUYER_CONFIRMED", sandler)
        self.assertIn("SELLER_INFERRED", med)
        self.assertIn("authentication_basis", med)
        self.assertIn("source_id/revision", med)
        self.assertIn("not automatic", med.lower())

    def test_eight_states_include_conflict_and_source_access_hold(self):
        med = self.skill(SLUGS[1])
        for state in ("BUYER_CONFIRMED", "DOCUMENT_OBSERVED",
                      "SELLER_INFERRED", "UNKNOWN", "DISCONFIRMED",
                      "CONFLICTED", "STALE", "ACCESS_HOLD"):
            with self.subTest(state=state):
                self.assertIn("| `" + state + "` |", med)
        self.assertIn("two current", med.lower())
        self.assertIn("detail-free", med.lower())

    def test_sandler_roi_uses_a_period_bound_monetary_baseline(self):
        base = ROOT / SLUGS[0]
        contract = (base / "references" / "advanced-practice.md").read_text()
        self.assertIn("R_t", contract)
        self.assertIn("benefit_t = R_t × u × m × a", contract)
        self.assertIn("net_t = benefit_t - F_t - C_t", contract)
        self.assertIn("first 12 months", contract)
        self.assertIn("a = 1", contract)
        self.assertIn("percentage points", contract)
        self.assertIn("UNKNOWN", contract)
        self.assertNotIn("B * r * m * a", contract)

    def test_joint_case_is_identical_and_contains_three_evidence_transitions(self):
        docs = [(ROOT / slug / "examples" / "acceptance.md").read_text()
                for slug in SLUGS]
        markers = [d.index("## CASE-JOINT-01:") for d in docs]
        self.assertEqual(docs[0][markers[0]:], docs[1][markers[1]:],
                         "The portable cross-method cases must not diverge")
        case = docs[0][markers[0]:]
        for stage in ("T0", "T1", "T2", "T3"):
            self.assertIn(stage, case)
        for requirement in ("seller-only", "buyer-controlled",
                            "DISCONFIRMED", "CONFLICTED", "ACCESS_HOLD",
                            "no close probability", "no numeric ROI",
                            "not a real"):
            self.assertIn(requirement.lower(), case.lower())

    def test_no_prerequisite_specific_model_or_external_api(self):
        for slug in SLUGS:
            doc = self.skill(slug)
            self.assertNotIn("pip install", doc)
            self.assertNotIn("import requests", doc)
            self.assertNotIn("API_KEY", doc)
            self.assertNotIn("must use GPT", doc)
            self.assertNotIn("must install", doc)


if __name__ == "__main__":
    unittest.main()
