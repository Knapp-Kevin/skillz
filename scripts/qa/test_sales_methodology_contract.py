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
        self.assertIn("two credible, current", med.lower())
        self.assertIn("suppress private rows", med.lower())
        self.assertIn("derived counts", med.lower())

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
                            "not an actual"):
            self.assertIn(requirement.lower(), case.lower())

    def test_sandler_buyer_choice_and_no_contact_precedence(self):
        skill = self.skill(SLUGS[0])
        examples = (ROOT / SLUGS[0] / "examples" / "acceptance.md").read_text()
        for item in ("## Buyer-controlled decision branches",
                     "STOP_NO_CONTACT", "PAUSE_OR_NO_FIT", "PROPOSAL_HOLD",
                     "open questions", "buyer"):
            self.assertIn(item, skill)
        self.assertIn("## S11. Explicit buyer opt-out", examples)
        self.assertIn("## S12. Sparse first-meeting", examples)
        self.assertIn("## S13. Buyer requested proposal", examples)
        self.assertIn("STOP_NO_CONTACT", examples)
        self.assertIn("precautionary", skill.lower())
        self.assertIn("Do not seek to verify a no-contact", skill)
        self.assertIn("NO_CONTACT", examples)
        self.assertIn("PROPOSAL_HOLD", examples)

    def test_meddpicc_decision_gates_are_not_scores_or_win_claims(self):
        skill = self.skill(SLUGS[1])
        examples = (ROOT / SLUGS[1] / "examples" / "acceptance.md").read_text()
        for item in ("## Opportunity decision gates",
                     "DISCOVERY_ONLY", "PROPOSAL_HOLD",
                     "FORECAST_NOT_ESTABLISHED", "SIGNATURE_HOLD",
                     "NOT_WON_OR_NOT_DELIVERED",
                     "evidence_review_state", "requested_action_gate",
                     "ACCESS_HOLD"):
            self.assertIn(item, skill)
        for item in ("## M13. Eight green fields", "## M14. Document observed",
                     "## M15. Conflict precedence",
                     "## M16. Readable dossier"):
            self.assertIn(item, examples)
        self.assertIn("SIGNATURE_HOLD", examples)
        self.assertIn("CONFLICTED", examples)

    def test_explicit_portable_state_translation_agrees_in_both_skills(self):
        sandler, med = [self.skill(slug) for slug in SLUGS]
        for text in (sandler, med):
            for mapping in ("SELLER_ASSERTED → SELLER_INFERRED",
                            "SOURCE_OBSERVED → DOCUMENT_OBSERVED",
                            "BUYER_CONFIRMED → BUYER_CONFIRMED"):
                self.assertIn(mapping, text)
            self.assertIn("SIMULATED", text)
            self.assertIn("ACCESS_HOLD", text)
        self.assertIn("## S14. Cross-skill source-state", 
                      (ROOT / SLUGS[0] / "examples" / "acceptance.md").read_text())
        self.assertIn("## M17. Exact Sandler-to-MEDDPICC",
                      (ROOT / SLUGS[1] / "examples" / "acceptance.md").read_text())

    def test_false_success_is_explicit_in_both_original_walkthroughs(self):
        sandler = (ROOT / SLUGS[0] / "references" / "advanced-practice.md").read_text()
        med = (ROOT / SLUGS[1] / "references" / "advanced-practice.md").read_text()
        self.assertIn("## Branch-first conversation practice", sandler)
        self.assertIn("STOP", sandler.upper())
        self.assertIn("SELLER_ASSERTED", sandler)
        self.assertIn("## Decision-gate example", med)
        self.assertIn("SIGNATURE_HOLD", med)
        self.assertIn("evidence_review_state", med)
        self.assertIn("requested_action_gate", med)

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
