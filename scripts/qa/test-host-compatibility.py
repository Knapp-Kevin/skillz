#!/usr/bin/env python3
"""Offline adversarial checks for host packaging; no model or installation."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "engine" / "builder" / "host_compat.py"
spec = importlib.util.spec_from_file_location("host_compat", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class HostCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.skill = self.root / "demo-skill"
        self.skill.mkdir()
        (self.skill / "SKILL.md").write_text(
            "---\nname: demo-skill\ndescription: >-\n"
            "  Work with source-controlled public release notes.\n"
            "---\n\n# Demo\n\nRead [guide](references/guide.md) before writing.\n",
            encoding="utf-8")
        (self.skill / "references").mkdir()
        (self.skill / "references" / "guide.md").write_text(
            "# Release notes\n\nPreserve tests and citations.\n", encoding="utf-8")
        (self.skill / "LICENSE").write_text(
            "Original example permission text.\n", encoding="utf-8")

    def test_single_canonical_package_is_directory_ready(self):
        for host in ("github-copilot", "claude-code", "openai-codex",
                     "gemini-cli", "hermes-agent"):
            with self.subTest(host=host):
                result = module.inspect(self.skill, host)
                self.assertTrue(result["format_valid"])
                self.assertTrue(result["package_ready"], result["blockers"])
                self.assertEqual(result["host_loaded"], "NOT_TESTED")
                self.assertEqual(result["behavior_tested"], "NOT_TESTED")
                self.assertEqual(result["consumer_accepted"], "NOT_TESTED")

    def test_microsoft_license_is_safe_and_lossless(self):
        result = module.inspect(self.skill, "m365-agent-builder")
        self.assertTrue(result["package_ready"], result["blockers"])
        files = {x["source"]: x["output"] for x in result["manifest"]}
        self.assertEqual(files["LICENSE"], "LICENSE.txt")
        dest = self.root / "upload.zip"
        module.write_zip(self.skill, "m365-agent-builder", str(dest), result)
        self.assertEqual(result["artifact_status"], "CREATED_NOT_UPLOADED")
        with zipfile.ZipFile(dest) as archive:
            self.assertIn("SKILL.md", archive.namelist())
            self.assertNotIn("demo-skill/SKILL.md", archive.namelist())
            self.assertEqual(archive.read("LICENSE.txt"),
                             (self.skill / "LICENSE").read_bytes())
        with self.assertRaisesRegex(ValueError, "MUST_BE_NEW_ZIP"):
            module.write_zip(self.skill, "m365-agent-builder", str(dest), result)

    def test_microsoft_hard_limit_and_chat_guidance_are_separate(self):
        source = (self.skill / "SKILL.md").read_text(encoding="utf-8")
        (self.skill / "SKILL.md").write_text(source + "\n" + "a" * 21000, encoding="utf-8")
        strict = module.inspect(self.skill, "m365-agent-builder")
        chat = module.inspect(self.skill, "m365-copilot-chat")
        self.assertIn("SKILL_MD_OVER_HOST_HARD_LIMIT", strict["blockers"])
        self.assertTrue(chat["package_ready"])
        self.assertIn("SKILL_MD_OVER_HOST_RECOMMENDATION", chat["warnings"])

    def test_broken_local_link_blocks_package(self):
        (self.skill / "references" / "guide.md").unlink()
        actual = module.inspect(self.skill, "github-copilot")
        self.assertFalse(actual["package_ready"])
        self.assertTrue(any(x.startswith("BROKEN_LOCAL_LINK:") for x in actual["blockers"]))

    def test_microsoft_unknown_extension_holds_not_silently_drops(self):
        (self.skill / "payload.bin").write_bytes(b"\x01\x02")
        actual = module.inspect(self.skill, "m365-agent-builder")
        self.assertFalse(actual["package_ready"])
        self.assertIn("UNSUPPORTED_EXTENSION:payload.bin", actual["blockers"])
        self.assertTrue(module.inspect(self.skill, "claude-code")["package_ready"])

    def test_microsoft_license_reference_cannot_break_silently(self):
        skillfile = self.skill / "SKILL.md"
        skillfile.write_text(skillfile.read_text(encoding="utf-8") +
                             "\nSee [license](LICENSE).\n", encoding="utf-8")
        actual = module.inspect(self.skill, "m365-agent-builder")
        self.assertIn("TRANSFORM_REQUIRES_LINK_REWRITE:SKILL.md", actual["blockers"])

    def test_symlink_in_package_fails_closed(self):
        try:
            (self.skill / "trap").symlink_to(self.skill / "SKILL.md")
        except (OSError, NotImplementedError):
            self.skipTest("Host cannot create symlinks")
        actual = module.inspect(self.skill, "github-copilot")
        self.assertFalse(actual["format_valid"])
        self.assertIn("SYMLINK_OR_SPECIAL_FILE", actual["blockers"])

    def test_scripts_never_become_host_execution_claims(self):
        (self.skill / "scripts").mkdir()
        (self.skill / "scripts" / "run.py").write_text("print('fixture')\n")
        actual = module.inspect(self.skill, "m365-agent-builder")
        self.assertTrue(actual["package_ready"])
        self.assertIn("SCRIPT_RUNTIME_AND_PERMISSIONS_REQUIRE_HOST_TEST",
                      actual["warnings"])
        self.assertEqual(actual["behavior_tested"], "NOT_TESTED")

    def test_source_changed_after_preflight_cannot_be_uploaded(self):
        receipt = module.inspect(self.skill, "m365-agent-builder")
        (self.skill / "references" / "guide.md").write_text(
            "Changed instructions since inspection.\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "ZIP_SOURCE_CHANGED_SINCE_PREFLIGHT"):
            module.write_zip(self.skill, "m365-agent-builder",
                             str(self.root / "stale.zip"), receipt)
        self.assertFalse((self.root / "stale.zip").exists())

    def test_secret_shaped_input_is_not_packaged_for_any_host(self):
        (self.skill / ".env").write_text("DUMMY=not-a-real-secret\n", encoding="utf-8")
        for host in ("github-copilot", "m365-agent-builder"):
            with self.subTest(host=host):
                actual = module.inspect(self.skill, host)
                self.assertFalse(actual["package_ready"])
                self.assertIn("POTENTIALLY_SENSITIVE_FILE:.env", actual["blockers"])

    def test_slug_traversal_is_rejected_at_cli_boundary(self):
        with self.assertRaisesRegex(ValueError, "INVALID_SKILL_SLUG"):
            module.main(["--skill", "../private"])

    def test_repo_navigator_entrypoint_limit_and_reference_closure(self):
        navigator = ROOT / "skills" / "authored" / "effort-allocation-navigator"
        if not navigator.exists():
            self.skipTest("Repository package unavailable")
        actual = module.inspect(navigator, "m365-agent-builder")
        self.assertTrue(actual["format_valid"], actual["blockers"])
        self.assertLess(actual["entrypoint_characters"], 20000)
        self.assertTrue(actual["package_ready"], actual["blockers"])
        self.assertEqual(actual["host_loaded"], "NOT_TESTED")


if __name__ == "__main__":
    unittest.main()
