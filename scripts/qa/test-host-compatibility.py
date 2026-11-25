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

    def test_authored_admission_rejects_new_holds_and_only_allows_exact_exceptions(self):
        known = {"skill": "offline-hyperv-qual-vm", "host": "gemini-apps",
                 "format_valid": True, "package_ready": False,
                 "blockers": sorted(module.HYPERV_REQUIRED_FILES)}
        result = module.authored_admission([known])
        self.assertEqual(len(result["documented_holds"]), 1)
        self.assertEqual(result["unexpected_holds"], [])
        for changed in (dict(known, skill="new-skill"), dict(known, host="claude-apps"),
                        dict(known, blockers=known["blockers"] + ["BROKEN_LOCAL_LINK:fixture"]),
                        dict(known, blockers=[]), dict(known, format_valid=False)):
            with self.subTest(changed=changed):
                self.assertEqual(module.authored_admission([changed])["status"],
                                 "HOLD_UNEXPECTED_PACKAGE_BLOCKERS")
        self.assertEqual(module.authored_admission([dict(known, package_ready=True)])["status"],
                         "STATIC_ADMISSION_READY")

    def test_new_authored_skill_cannot_pass_admission_with_unsupported_file(self):
        (self.skill / "fixture.bin").write_bytes(b"fictional")
        reports = [module.inspect(self.skill, host) for host in module.HOSTS]
        result = module.authored_admission(reports)
        self.assertTrue(result["unexpected_holds"])
        self.assertFalse(result["documented_holds"])

    def test_unassessed_receipts_never_claim_ready(self):
        statuses = module.unassessed_host_statuses()
        self.assertEqual(set(statuses), set(module.UNASSESSED_HOSTS))
        self.assertFalse(set(statuses) & set(module.HOSTS))
        for entry in statuses.values():
            self.assertEqual(entry["status"], "HOLD")
            self.assertIsNone(entry["asset"])
            self.assertIsNone(entry["sha256"])
            self.assertEqual(entry["behavior"], "NOT_TESTED")

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

    def test_upload_zip_rebuild_is_byte_stable_across_clock_and_sorted_members(self):
        from unittest.mock import patch
        for host, profile in module.HOSTS.items():
            if profile["mode"] != "zip":
                continue
            with self.subTest(host=host):
                first = self.root / (host + "-first.zip")
                second = self.root / (host + "-second.zip")
                receipt = module.inspect(self.skill, host)
                self.assertTrue(receipt["package_ready"], receipt["blockers"])
                with patch("zipfile.time.localtime", return_value=(2025, 1, 1, 0, 0, 0, 0, 1, 0)):
                    module.write_zip(self.skill, host, str(first), receipt)
                # A future wall-clock time must not alter otherwise identical bytes.
                with patch("zipfile.time.localtime", return_value=(2026, 11, 25, 12, 0, 0, 2, 329, 0)):
                    module.write_zip(self.skill, host, str(second), module.inspect(self.skill, host))
                self.assertEqual(first.read_bytes(), second.read_bytes())
                with zipfile.ZipFile(first) as archive:
                    names = archive.namelist()
                    self.assertEqual(names, sorted(names))
                    for item in archive.infolist():
                        self.assertEqual(item.date_time, (1980, 1, 1, 0, 0, 0))
                        self.assertEqual(item.create_system, 3)
                        self.assertEqual(item.external_attr, 0o600 << 16)
                        self.assertEqual(item.compress_type, zipfile.ZIP_DEFLATED)

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

    def test_directory_handoff_is_prepared_not_installed(self):
        skillfile = self.skill / "SKILL.md"
        skillfile.write_text(skillfile.read_text(encoding="utf-8") +
                             "\nSee [license](LICENSE).\n", encoding="utf-8")
        receipt = module.inspect(self.skill, "m365-agents-toolkit")
        self.assertTrue(receipt["package_ready"], receipt["blockers"])
        destination = self.root / "prepared"
        module.write_directory(self.skill, "m365-agents-toolkit",
                               str(destination), receipt)
        self.assertEqual(receipt["artifact_status"], "PREPARED_NOT_INSTALLED")
        self.assertIn("](LICENSE.txt)",
                      (destination / "SKILL.md").read_text(encoding="utf-8"))
        self.assertEqual((destination / "LICENSE.txt").read_bytes(),
                         (self.skill / "LICENSE").read_bytes())
        with self.assertRaisesRegex(ValueError, "MUST_BE_NEW_OUTSIDE_REPO"):
            module.write_directory(self.skill, "m365-agents-toolkit",
                                   str(destination), receipt)

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

    def test_microsoft_license_reference_is_rewritten_losslessly(self):
        skillfile = self.skill / "SKILL.md"
        skillfile.write_text(skillfile.read_text(encoding="utf-8") +
                             "\nSee [license](LICENSE).\n", encoding="utf-8")
        actual = module.inspect(self.skill, "m365-agent-builder")
        self.assertTrue(actual["package_ready"], actual["blockers"])
        self.assertIn("LOSSLESS_LICENSE_LINK_REWRITE_FOR_HOST", actual["warnings"])
        zippath = self.root / "reference-adapter.zip"
        module.write_zip(self.skill, "m365-agent-builder", str(zippath), actual)
        with zipfile.ZipFile(zippath) as archive:
            self.assertIn("](LICENSE.txt)", archive.read("SKILL.md").decode("utf-8"))
            self.assertEqual(archive.read("LICENSE.txt"),
                             (self.skill / "LICENSE").read_bytes())
        self.assertIn("](LICENSE)", skillfile.read_text(encoding="utf-8"))

    def test_valid_bundled_directory_link_is_not_broken(self):
        skillfile = self.skill / "SKILL.md"
        skillfile.write_text(skillfile.read_text(encoding="utf-8") +
                             "\nBrowse [references](references/).\n", encoding="utf-8")
        actual = module.inspect(self.skill, "github-copilot")
        self.assertTrue(actual["package_ready"], actual["blockers"])

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

    def test_nested_entrypoint_hard_limit_cannot_hide_inside_pack(self):
        nested = self.skill / "skills" / "nested" / "SKILL.md"
        nested.parent.mkdir(parents=True)
        nested.write_text("---\nname: nested\ndescription: A fictional skill.\n---\n" +
                          "x" * 21000, encoding="utf-8")
        strict = module.inspect(self.skill, "m365-agent-builder")
        self.assertIn("NESTED_SKILL_MD_OVER_HOST_HARD_LIMIT:skills/nested/SKILL.md",
                      strict["blockers"])
        other = module.inspect(self.skill, "claude-code")
        self.assertTrue(other["package_ready"], other["blockers"])
        self.assertIn("NESTED_SKILL_DISCOVERY_REQUIRES_HOST_TEST", other["warnings"])

    def test_custom_package_cli_preflights_and_writes_without_install(self):
        import contextlib
        import io
        import json
        output = io.StringIO()
        destination = self.root / "custom.zip"
        with contextlib.redirect_stdout(output):
            rc = module.main(["--package", str(self.skill), "--host",
                              "m365-agent-builder", "--zip-output", str(destination)])
        self.assertEqual(rc, 0)
        self.assertTrue(destination.is_file())
        result = json.loads(output.getvalue())["results"][0]
        self.assertEqual(result["artifact_status"], "CREATED_NOT_UPLOADED")
        self.assertEqual(result["host_loaded"], "NOT_TESTED")

    def test_claude_upload_preserves_folder_wrapper(self):
        result = module.inspect(self.skill, "claude-apps")
        self.assertTrue(result["package_ready"], result["blockers"])
        dest = self.root / "claude.zip"
        module.write_zip(self.skill, "claude-apps", str(dest), result)
        with zipfile.ZipFile(dest) as archive:
            self.assertEqual(set(archive.namelist()), {
                "demo-skill/SKILL.md", "demo-skill/LICENSE",
                "demo-skill/references/guide.md"})
        self.assertEqual(result["behavior_tested"], "NOT_TESTED")

    def test_claude_description_limit_does_not_apply_to_gemini(self):
        file = self.skill / "SKILL.md"
        file.write_text("---\nname: demo-skill\ndescription: >-\n  " +
                        "x" * 201 + "\n---\n\n# Demo\n")
        self.assertIn("DESCRIPTION_OVER_HOST_LIMIT",
                      module.inspect(self.skill, "claude-apps")["blockers"])
        self.assertTrue(module.inspect(self.skill, "gemini-apps")["package_ready"])

    def test_builder_json_quoted_description_and_exact_limit(self):
        import json
        file = self.skill / "SKILL.md"
        for text, ready in (('A "quoted" description ' + "x" * (200 - len('A "quoted" description ')), True),
                            ("x" * 201, False)):
            self.assertEqual(len(text), 200 if ready else 201)
            file.write_text("---\nname: demo-skill\ndescription: " +
                            json.dumps(text, ensure_ascii=False) + "\n---\n")
            report = module.inspect(self.skill, "claude-apps")
            self.assertEqual(report["package_ready"], ready, report["blockers"])
        file.write_text('---\nname: demo-skill\ndescription: "valid" # extra\n---\n')
        self.assertIn("DESCRIPTION_METADATA_NOT_ASSESSED",
                      module.inspect(self.skill, "claude-apps")["blockers"])

    def test_ambiguous_description_not_treated_as_valid(self):
        file = self.skill / "SKILL.md"
        file.write_text("---\nname: demo-skill\ndescription: *alias\n---\n\n# Demo\n")
        for host in ("claude-apps", "gemini-apps"):
            self.assertIn("DESCRIPTION_METADATA_NOT_ASSESSED",
                          module.inspect(self.skill, host)["blockers"])

    def test_gemini_upload_root_and_license_link(self):
        file = self.skill / "SKILL.md"
        file.write_text(file.read_text() + "\nSee [license](LICENSE).\n")
        result = module.inspect(self.skill, "gemini-apps")
        self.assertTrue(result["package_ready"], result["blockers"])
        dest = self.root / "gemini.zip"
        module.write_zip(self.skill, "gemini-apps", str(dest), result)
        with zipfile.ZipFile(dest) as archive:
            self.assertEqual(set(archive.namelist()),
                             {"SKILL.md", "LICENSE.txt", "references/guide.md"})
            self.assertIn("](LICENSE.txt)", archive.read("SKILL.md").decode())
            self.assertEqual(archive.read("LICENSE.txt"),
                             (self.skill / "LICENSE").read_bytes())
        self.assertIn("](LICENSE)", file.read_text())

    def test_gemini_unsupported_content_and_file_count_hold(self):
        (self.skill / "app.ts").write_text("export const n = 1;")
        for i in range(98):
            (self.skill / f"ref-{i}.txt").write_text("fictional")
        result = module.inspect(self.skill, "gemini-apps")
        self.assertIn("UNSUPPORTED_EXTENSION:app.ts", result["blockers"])
        self.assertIn("MAX_FILES_EXCEEDED", result["blockers"])
        self.assertFalse(result["package_ready"])

    def test_gemini_script_constraint_is_not_execution_proof(self):
        (self.skill / "tool.py").write_text("print('fictional')\n")
        result = module.inspect(self.skill, "gemini-apps")
        self.assertIn("NO_EXTERNAL_SCRIPT_REQUESTS_HOST_RUNTIME_NOT_TESTED",
                      result["warnings"])
        self.assertEqual(result["host_loaded"], "NOT_TESTED")
        self.assertEqual(result["behavior_tested"], "NOT_TESTED")

    def test_curated_claude_adaptation_preserves_scope_and_canonical_bytes(self):
        import hashlib
        from unittest.mock import patch
        entry = self.skill / "SKILL.md"
        original_description = "Analyze fictional evidence without claiming authorization. " * 5
        source = ("---\nname: demo-skill\ndescription: >-\n  " +
                  original_description.strip() + "\n---\n\n# Demo\n\nRead [guide](references/guide.md).\n\n").encode()
        entry.write_bytes(source)
        blob = hashlib.sha1(b"blob " + str(len(source)).encode() + b"\0" + source,
                            usedforsecurity=False).hexdigest()
        short = "Analyze fictional evidence; preserve authorization boundaries."
        with patch.object(module, "AUTHORED", self.root), patch.dict(
                module.CLAUDE_DISCOVERY, {"demo-skill": (blob, short)}, clear=True):
            report = module.inspect(self.skill, "claude-apps")
            self.assertTrue(report["package_ready"], report["blockers"])
            self.assertIn("CLAUDE_DISCOVERY_DESCRIPTION_ADAPTED_CANONICAL_SCOPE_PRESERVED", report["warnings"])
            self.assertEqual(module.render_package_bytes(self.skill, "SKILL.md",
                             module.HOSTS["claude-code"]), source)
            dest = self.root / "curated.zip"
            module.write_zip(self.skill, "claude-apps", str(dest), report)
            with zipfile.ZipFile(dest) as archive:
                output = archive.read("demo-skill/SKILL.md")
                self.assertEqual(module.bounded_description(output.decode()), short)
                self.assertIn(source.split(b"\n---\n", 1)[1], output)
                self.assertIn(original_description.strip().encode(), output)
                self.assertEqual(archive.read("demo-skill/LICENSE"),
                                 (self.skill / "LICENSE").read_bytes())
                self.assertEqual(archive.read("demo-skill/references/guide.md"),
                                 (self.skill / "references/guide.md").read_bytes())
            self.assertEqual(entry.read_bytes(), source)
            entry.write_bytes(source + b"Changed source.\n")
            stale = module.inspect(self.skill, "claude-apps")
            self.assertIn("DESCRIPTION_OVER_HOST_LIMIT", stale["blockers"])
            with self.assertRaisesRegex(ValueError, "ZIP_SOURCE_CHANGED_SINCE_PREFLIGHT"):
                module.write_zip(self.skill, "claude-apps",
                                 str(self.root / "stale.zip"), report)
        entry.write_bytes(source)
        with patch.dict(module.CLAUDE_DISCOVERY, {"demo-skill": (blob, short)}, clear=True):
            self.assertIn("DESCRIPTION_OVER_HOST_LIMIT",
                          module.inspect(self.skill, "claude-apps")["blockers"])

    def test_curated_records_cover_only_exact_authored_sources(self):
        if not module.AUTHORED.is_dir():
            self.skipTest("Repository packages unavailable")
        for slug, (blob, short) in module.CLAUDE_DISCOVERY.items():
            with self.subTest(skill=slug):
                import hashlib
                source = (module.AUTHORED / slug / "SKILL.md").read_bytes()
                current = hashlib.sha1(b"blob " + str(len(source)).encode() + b"\0" + source,
                                       usedforsecurity=False).hexdigest()
                self.assertEqual(current, blob, "Re-review discovery summary against changed canonical source")
                self.assertLessEqual(len(short), 200)
                report = module.inspect(module.AUTHORED / slug, "claude-apps")
                self.assertTrue(report["package_ready"], report["blockers"])
                self.assertEqual(report["behavior_tested"], "NOT_TESTED")

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
