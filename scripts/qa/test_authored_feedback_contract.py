#!/usr/bin/env python3
"""Portable first-party authored feedback contract: offline QA, no issue posting."""
import json
import re
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[2]
AUTHORED = ROOT / "skills" / "authored"
INDEX = ROOT / "registry" / "authored-skills-index.json"
TEMPLATE = ROOT / ".github" / "ISSUE_TEMPLATE" / "agent-skill-feedback.yml"
TARGET = "https://github.com/Knapp-Kevin/skillz/issues/new?template=agent-skill-feedback.yml"
HEADING = "## Optional, anonymized-content skill feedback"
CONTINUITY = "## Multi-turn continuity when the work is not one-shot"


def packages():
    return sorted(p for p in AUTHORED.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())


def check_footer(text):
    """Returns an error code, not a claim that a remote issue is anonymous."""
    if text.count(HEADING) != 1:
        return "MISSING_OR_DUPLICATE_FEEDBACK_SECTION"
    footer = text.split(HEADING, 1)[1]
    if TARGET not in footer:
        return "MISSING_STANDALONE_ISSUE_URL"
    expected = (
        "not required", "explicitly authorized public posting",
        "otherwise offer", "fictional", "never submit",
        "only the **content** can be anonymized", "not the account identity",
        "no telemetry", "no", "automatic reporting",
    )
    for fragment in expected:
        if fragment not in footer.casefold():
            return "MISSING_AUTHORITY_OR_PRIVACY_DISCLOSURE:" + fragment
    return None


def git_sha(spec):
    proc = subprocess.run(
        ["git", "-C", str(ROOT), "rev-parse", "HEAD:" + spec],
        capture_output=True, text=True, check=False,
    )
    if proc.returncode != 0:
        raise AssertionError("Could not verify exact Git object: " + spec)
    sha = proc.stdout.strip()
    if not re.fullmatch(r"[0-9a-f]{40,64}", sha):
        raise AssertionError("Invalid Git object identity: " + spec)
    return sha


class FeedbackContractTests(unittest.TestCase):
    def test_all_authored_packages_have_portable_feedback_route(self):
        found = packages()
        self.assertGreaterEqual(len(found), 34)
        failures = {}
        for p in found:
            error = check_footer((p / "SKILL.md").read_text(encoding="utf-8"))
            if error:
                failures[p.name] = error
        self.assertEqual(failures, {})

    def test_all_authored_packages_preserve_multiturn_work_state(self):
        failures = {}
        for p in packages():
            skill = (p / "SKILL.md").read_text(encoding="utf-8")
            if skill.count(CONTINUITY) != 1 or skill.index(CONTINUITY) > skill.index(HEADING):
                failures[p.name] = "missing, duplicated or misplaced continuation"
                continue
            contract = skill.split(CONTINUITY, 1)[1].split(HEADING, 1)[0]
            required = ("follow-up messages as continuation", "objective, confirmed decisions",
                        "protected checks, blockers", "never silently remove safety",
                        "do not invent unavailable history", "actual finished outcome",
                        "no autonomous follow-up")
            missing = [term for term in required if term not in contract.casefold()]
            if missing:
                failures[p.name] = "missing: " + ", ".join(missing)
        self.assertEqual(failures, {})

    def test_multiturn_does_not_imply_replay_storage_or_auto_actions(self):
        skill = (AUTHORED / "ci-guard" / "SKILL.md").read_text(encoding="utf-8")
        chunk = skill.split(CONTINUITY, 1)[1].split(HEADING, 1)[0]
        self.assertIn("Do not invent unavailable history or claim persistent storage.", chunk)
        self.assertIn("No autonomous follow-up, session creation or background execution is implied.", chunk)
        self.assertIn("a drafted artifact, open PR, proposed test or green isolated check", chunk)

    def test_authored_registry_and_disk_package_identities_match(self):
        index = json.loads(INDEX.read_text(encoding="utf-8"))
        authored = {
            item["id"]: item for item in index["skills"]
            if item["source_class"] == "first-party-authored"
        }
        self.assertEqual(set(authored), {p.name for p in packages()})
        for p in packages():
            row = authored[p.name]
            self.assertEqual(
                row["skill_blob_sha"],
                git_sha("skills/authored/" + p.name + "/SKILL.md"),
                p.name + " stale SKILL identity",
            )
            self.assertEqual(
                row["package_tree_sha"],
                git_sha("skills/authored/" + p.name),
                p.name + " stale complete-package identity",
            )

    def test_all_provenance_and_verification_companions_match_updated_source(self):
        index = json.loads(INDEX.read_text(encoding="utf-8"))
        for row in index["skills"]:
            name = row["id"]
            for prefix in ("skills", "verification"):
                path = ROOT / "registry" / prefix / "local-skills" / (name + ".yaml")
                text = path.read_text(encoding="utf-8")
                self.assertRegex(text, r"(?m)^content_blob_sha: " +
                                 re.escape(row["skill_blob_sha"]) + r"$")
                self.assertRegex(text, r"(?m)^complete_package_tree_sha: " +
                                 re.escape(row["package_tree_sha"]) + r"$")
                if prefix == "skills":
                    self.assertRegex(text, r"(?m)^review_status: needs-re-review$")
                else:
                    self.assertRegex(text, r"(?m)^verification_status: needs-re-review$")
                    self.assertRegex(text, r"(?m)^validation_status: not-run$")
            self.assertEqual(row["review_status"], "needs-re-review")
            self.assertEqual(row["behavioral_validation"], "not-run")

    def test_no_fake_anonymous_account_guarantee(self):
        for p in packages():
            footer = (p / "SKILL.md").read_text(encoding="utf-8").split(HEADING, 1)[1]
            self.assertIn("GitHub displays the posting account", footer)
            self.assertIn("only the **content** can be anonymized", footer)
            self.assertNotIn("anonymous submission guaranteed", footer.casefold())

    def test_required_privacy_and_account_disclosure_in_issue_form(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        self.assertIn("GitHub shows the posting account", text)
        self.assertIn("Use only fictional or cleared public examples", text)
        self.assertIn("I have authorization to post publicly", text)
        self.assertIn("required: true", text)
        for key in ("id: skill", "id: kind", "id: evidence",
                    "id: expected", "id: reproduction", "id: privacy"):
            self.assertIn(key, text)

    def test_no_mandatory_or_invisible_submission_contract(self):
        for p in packages():
            footer = (p / "SKILL.md").read_text(encoding="utf-8").split(HEADING, 1)[1]
            self.assertIn("Feedback is **not required**", footer, p.name)
            self.assertIn("No telemetry, automatic reporting, or background network activity.", footer, p.name)
            self.assertIn("not the account identity", footer, p.name)

    def test_missing_url_and_false_identity_anonymity_are_rejected(self):
        good = (AUTHORED / "repository-readme-architect" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIsNone(check_footer(good))
        self.assertEqual(
            check_footer(good.replace(TARGET, "https://invalid.example/collect")),
            "MISSING_STANDALONE_ISSUE_URL",
        )
        self.assertTrue(
            check_footer(good.replace("not the account identity", "the account identity is hidden"))
            .startswith("MISSING_AUTHORITY_OR_PRIVACY_DISCLOSURE")
        )

    def test_feedback_is_never_a_skill_activation_precondition(self):
        for p in packages():
            skill = (p / "SKILL.md").read_text(encoding="utf-8")
            self.assertEqual(skill.count(HEADING), 1)
            self.assertTrue(skill.index(HEADING) > skill.index("\n---\n") if "\n---\n" in skill else True)


if __name__ == "__main__":
    unittest.main()
