"""Offline structural checks of two original sales-method skill packages.

These tests inspect text and package closure only. They do not simulate
a real buyer, train a salesperson, test independent agent interpretation,
verify third-party trademarks, or grant external account access.
"""
import json
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

    def test_version_minor_release_is_consistent_across_five_file_packages(self):
        repo = ROOT.parents[1]
        index = json.loads((repo / "registry" / "authored-skills-index.json")
                           .read_text(encoding="utf-8"))
        for slug in SLUGS:
            with self.subTest(slug=slug):
                skill = self.skill(slug)
                self.assertIn("  version: 0.2.0", skill)
                changelog = ROOT / slug / "CHANGELOG.md"
                self.assertTrue(changelog.is_file())
                notes = changelog.read_text(encoding="utf-8")
                self.assertIn("## 0.2.0:", notes)
                self.assertIn("minor", notes.lower())
                record = next((x for x in index["skills"] if x["id"] == slug), None)
                self.assertIsNotNone(record)
                self.assertEqual("0.2.0", record["package_version"])
                self.assertEqual(5, record["package_file_count"])
                self.assertEqual("needs-re-review", record["review_status"])
                self.assertEqual("not-run", record["behavioral_validation"])
                for category in ("skills", "verification"):
                    yaml_path = repo / "registry" / category / "local-skills" / (slug + ".yaml")
                    companion = yaml_path.read_text(encoding="utf-8")
                    self.assertIn('skill_version: "0.2.0"', companion)
                    self.assertIn("needs-re-review", companion)

    def test_sandler_roleplay_requires_user_rep_turn_and_noninvented_feedback(self):
        skill = self.skill(SLUGS[0])
        examples = (ROOT / SLUGS[0] / "examples" / "acceptance.md").read_text()
        practice = (ROOT / SLUGS[0] / "references" / "advanced-practice.md").read_text()
        for token in ("## Live practice protocol", "**SETUP:**", "**PLAY:**",
                      "**OBSERVE:**", "**COACH:**", "**CONTINUE OR CLOSE:**",
                      "one buyer utterance", "ROLE_PLAY_OBSERVED", "SIMULATED"):
            self.assertIn(token, skill)
        for name in ("## S15. Multi-turn role-play", "## S16. Role-play stop",
                     "## S17. Host has no recording"):
            self.assertIn(name, examples)
        self.assertIn("NOT_OBSERVED_REP_BEHAVIOR", practice)
        self.assertIn("stops for the user's rep reply", practice)
        self.assertIn("INTERACTIVE_REHEARSAL", skill)
        self.assertIn("DEMONSTRATION", skill)
        self.assertIn("SIMULATED / DEMO_ONLY", skill)
        self.assertIn("## S18. Explicit fictional full-dialogue", examples)
        self.assertIn("full fictional demonstration", practice.lower())

    def test_meddpicc_hold_can_progress_only_after_complete_current_evidence(self):
        skill = self.skill(SLUGS[1])
        examples = (ROOT / SLUGS[1] / "examples" / "acceptance.md").read_text()
        practice = (ROOT / SLUGS[1] / "references" / "advanced-practice.md").read_text()
        for token in ("## Evidence-based release from a commercial HOLD",
                      "PROPOSAL_INPUTS_SUPPORTED", "FORECAST_POLICY_CHECK_READY",
                      "SIGNATURE_PREREQUISITES_OBSERVED", "CONTRACT_EXECUTION_OBSERVED",
                      "UNKNOWN_PREVIOUS_STATE", "ACCESS_HOLD", "CONFLICTED",
                      "prior_gate | new_gate", "never"):
            self.assertIn(token.lower(), skill.lower())
        for name in ("## M18. New security evidence clears", 
                     "## M19. Complete buyer authorization",
                     "## M20. Other-account source substitution",
                     "## M21. Old rejection"):
            self.assertIn(name, examples)
        self.assertIn("T1:", practice)
        self.assertIn("T2:", practice)
        self.assertIn("T3:", practice)
        self.assertIn("T4:", practice)
        self.assertIn("SIGNATURE_HOLD", practice)

    def test_optional_task_handoff_preserves_buyer_consent_boundaries(self):
        docs = [self.skill(slug) for slug in SLUGS]
        contract = ("source_method | source_evidence_state | internal_or_external |")
        for doc in docs:
            self.assertIn("## Optional task-planning handoff", doc)
            self.assertIn(contract, doc.replace("\n", " "))
            self.assertIn("BLOCKED", doc)
            self.assertIn("buyer", doc.lower())
            self.assertIn("host", doc.lower())
        self.assertIn("STOP_NO_CONTACT", docs[0])
        self.assertIn("SIGNATURE_PREREQUISITES_OBSERVED", docs[1])
        self.assertIn("ACCESS_HOLD", docs[1])

    def test_sales_handoff_adversaries_preserve_shared_crosswalk(self):
        a = (ROOT / SLUGS[0] / "examples" / "acceptance.md").read_text()
        b = (ROOT / SLUGS[1] / "examples" / "acceptance.md").read_text()
        self.assertIn("## S19. Task planner", a)
        self.assertIn("## M22. Readiness gate", b)
        self.assertIn("STOP_NO_CONTACT", a)
        self.assertIn("SELLER_INFERRED", b)
        self.assertIn("BLOCKED", b)
        shared = "## CASE-JOINT-01:"
        self.assertEqual(a[a.index(shared):], b[b.index(shared):])

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
