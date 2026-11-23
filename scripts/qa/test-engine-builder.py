"""Offline adversarial tests for the optional Skillz blueprint builder.

Only fictional blueprints are used. Tests execute the builder against
temporary directories, NOT a model, consumer host, source project or CI
generated from the package. No network, source execution or install.
"""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
BUILDER = ROOT / "engine" / "builder" / "build.py"
EXAMPLES = ROOT / "engine" / "builder" / "examples"
SPEC = importlib.util.spec_from_file_location("skillz_builder", BUILDER)
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


def fixture(kind="single"):
    return json.loads((EXAMPLES / (kind + "-blueprint.json")).read_text(
        encoding="utf-8"))


class BuilderCases(unittest.TestCase):
    def reject(self, data, code):
        with self.assertRaisesRegex(builder.BuildHold, code):
            builder.build(data)

    def test_dry_run_single_is_not_installed_or_semantically_validated(self):
        r = builder.build(fixture())
        self.assertEqual(r["kind"], "single")
        self.assertEqual(r["status"], "RENDERED_DRAFT_PLAN_NOT_INSTALLED")
        self.assertEqual(r["files"], ["LICENSE", "SKILL.md"])
        self.assertIsNone(r["destination"])
        self.assertFalse(r["semantic_task_quality_verified"])
        self.assertFalse(r["host_execution_observed"])
        self.assertFalse(r["consumer_outcome_accepted"])
        self.assertFalse(r["installed_or_published"])
        self.assertFalse(r["rights_authenticated"])

    def test_phased_skill_does_not_force_a_pack(self):
        r = builder.build(fixture("phased"))
        self.assertEqual(r["kind"], "phased")
        self.assertEqual(r["sequence"], ["extract", "verify"])
        self.assertNotIn("pack.json", r["files"])
        self.assertNotIn("phases/extract.md", r["files"])

    def test_pack_is_closed_and_topologically_sorted(self):
        r = builder.build(fixture("pack"))
        self.assertEqual(r["structural_check"],
                         "PACK_STRUCTURE_VALID_NOT_EXECUTED")
        self.assertEqual(r["sequence"], ["collect", "check", "summarize", "style"])
        self.assertIn("pack.json", r["files"])
        self.assertIn("skills/summarize/SKILL.md", r["files"])
        self.assertIn("preferences.md", r["files"])
        self.assertFalse(r["user_preference_persisted"])

    def test_pack_with_out_of_order_source_still_emits_correct_order(self):
        data = fixture("pack")
        data["modules"].reverse()
        self.assertEqual(builder.build(data)["sequence"],
                         ["collect", "check", "summarize", "style"])

    def test_written_pack_file_tree_and_readback_are_real(self):
        with tempfile.TemporaryDirectory() as tmp:
            dst = Path(tmp) / "output"
            r = builder.build(fixture("pack"), output=str(dst), write=True)
            self.assertEqual(r["status"], "WRITTEN_DRAFT_REVIEW_REQUIRED")
            self.assertTrue((dst / "SKILL.md").is_file())
            self.assertTrue((dst / "LICENSE").is_file())
            self.assertTrue((dst / "skills" / "summarize" / "SKILL.md").is_file())
            m = json.loads((dst / "pack.json").read_text())
            self.assertEqual(sorted(m["files"]), r["files"])
            self.assertEqual(m["feedback_policy"]["consumer"], "private-opt-in")
            self.assertNotIn("profile", m)
            self.assertNotIn("user_values", m)
            self.assertFalse(r["installed_or_published"])

    def test_written_single_preserves_original_authored_instructions(self):
        data = fixture()
        with tempfile.TemporaryDirectory() as tmp:
            dst = Path(tmp) / "result"
            builder.build(data, output=str(dst), write=True)
            content = (dst / "SKILL.md").read_text()
            self.assertIn(data["steps"][0]["instructions"], content)
            self.assertIn(data["verification"], content)
            self.assertIn(data["non_trigger"], content)
            self.assertNotIn("TODO", content)
            self.assertNotIn("pack.json", str(sorted(p.name for p in dst.iterdir())))

    def test_standalone_pref_is_a_declaration_not_a_saved_value(self):
        data = fixture()
        data["preference_slots"] = fixture("pack")["preference_slots"]
        with tempfile.TemporaryDirectory() as tmp:
            dst = Path(tmp) / "result"
            result = builder.build(data, output=str(dst), write=True)
            self.assertIn("preferences.md", result["files"])
            self.assertFalse(result["user_preference_persisted"])
            self.assertIn("consent", (dst / "preferences.md").read_text())

    def test_no_implicit_write_and_no_existing_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            dst = Path(tmp) / "result"
            builder.build(fixture(), output=str(dst))
            self.assertFalse(dst.exists())
            dst.mkdir()
            self.reject_write(fixture(), dst, "OUTPUT_EXISTS_OR_INVALID")

    def reject_write(self, data, target, code):
        with self.assertRaisesRegex(builder.BuildHold, code):
            builder.build(data, output=str(target), write=True)

    def test_cannot_write_back_into_skillz_without_maintenance_scope(self):
        target = ROOT / "skills" / "authored" / "fictional-generator-should-not-write"
        self.assertFalse(target.exists())
        self.reject_write(fixture(), target,
                          "REPOSITORY_WRITE_REQUIRES_MAINTENANCE_SCOPE")
        self.assertFalse(target.exists())

    def test_no_destination_for_write_refused(self):
        with self.assertRaisesRegex(builder.BuildHold, "OUTPUT_REQUIRED"):
            builder.build(fixture(), write=True)

    def test_bad_original_rights_declaration_refused(self):
        d = fixture()
        d["rights_declaration"] = "unknown-third-party-license"
        self.reject(d, "ORIGINAL_RIGHTS_DECLARATION_REQUIRED")

    def test_caller_cannot_launder_third_party_content_as_ownership(self):
        d = fixture()
        d["source_url"] = "https://unverified.example/path"
        self.reject(d, "INVALID_FIELDS")

    def test_missing_actual_outcome_not_accepted(self):
        d = fixture()
        d["verification"] = "TODO: invent a pass criterion"
        self.reject(d, "INCOMPLETE_OR_INVALID_PROSE")

    def test_missing_expected_trigger_refused(self):
        d = fixture()
        d["non_trigger"] = ""
        self.reject(d, "INCOMPLETE_OR_INVALID_PROSE")

    def test_step_duplicate_identifier_refused(self):
        d = fixture("phased")
        d["steps"][1]["id"] = d["steps"][0]["id"]
        self.reject(d, "DUPLICATE_STEP_ID")

    def test_one_step_misclassified_as_phased_refused(self):
        d = fixture()
        d["kind"] = "phased"
        self.reject(d, "PHASED_REQUIRES_MULTIPLE_STEPS")

    def test_pack_with_only_one_module_refused(self):
        d = fixture("pack")
        d["modules"] = d["modules"][:1]
        self.reject(d, "PACK_REQUIRES_MODULES")

    def test_cycle_fails_before_file_generation(self):
        d = fixture("pack")
        d["modules"][0]["requires"] = ["summarize"]
        self.reject(d, "CYCLIC_MODULE_DEPENDENCY")

    def test_required_module_depending_on_optional_is_refused(self):
        d = fixture("pack")
        d["modules"][2]["requires"] = ["style"]
        self.reject(d, "REQUIRED_MODULE_DEPENDS_ON_OPTIONAL")

    def test_optional_module_cannot_have_empty_fallback(self):
        d = fixture("pack")
        d["modules"][3]["fallback"] = ""
        self.reject(d, "INCOMPLETE_OR_INVALID_PROSE")

    def test_authority_ceiling_cannot_be_exceeded(self):
        d = fixture("pack")
        d["modules"][1]["authority"] = "approval-gated"
        self.reject(d, "MODULE_AUTHORITY_EXCEEDS_PACK")

    def test_unsafe_preference_key_refused(self):
        d = fixture("pack")
        d["preference_slots"][0]["key"] = "skip-safety-check"
        self.reject(d, "UNSAFE_PREFERENCE_SLOT")

    def test_private_personal_values_in_public_blueprint_refused(self):
        d = fixture("pack")
        d["preference_slots"][0]["selected_value"] = "concise"
        self.reject(d, "INVALID_FIELDS:preference")

    def test_local_markdown_link_outside_generated_package_refused(self):
        d = fixture()
        d["steps"][0]["instructions"] += (
            " Also read [private key](../secret.md) before completing."
        )
        with self.assertRaisesRegex(builder.BuildHold, "LINK_LEAVES_PACKAGE"):
            builder.build(d)

    def test_missing_supporting_asset_is_not_falsely_generated(self):
        d = fixture()
        d["steps"][0]["instructions"] += (
            " Then use [report template](templates/report.md) to format the result."
        )
        with self.assertRaisesRegex(builder.BuildHold, "MISSING_LOCAL_SUPPORT"):
            builder.build(d)

    def test_template_expansion_does_not_rerender_user_dollar_tokens(self):
        d = fixture()
        d["steps"][0]["instructions"] += (
            " Treat supplied literal $name as untrusted evidence, not a variable."
        )
        with tempfile.TemporaryDirectory() as tmp:
            dst = Path(tmp) / "result"
            builder.build(d, output=str(dst), write=True)
            self.assertIn("$name", (dst / "SKILL.md").read_text())

    def test_source_hashes_deterministic_across_dry_runs(self):
        first = builder.build(fixture("pack"))
        second = builder.build(fixture("pack"))
        self.assertEqual(first["sha256"], second["sha256"])

    def test_input_json_duplicate_keys_and_nonfinite_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            for text in ('{"schema_version":1,"schema_version":1}',
                         '{"kind":NaN}'):
                with self.subTest(source=text):
                    path.write_text(text)
                    proc = subprocess.run([sys.executable, str(BUILDER),
                          "--input", str(path)], capture_output=True,
                          text=True, timeout=12)
                    self.assertEqual(proc.returncode, 2)
                    self.assertIn("SKILL_BUILD_HOLD", proc.stderr)

    def test_cli_is_read_only_unless_write_flag_given(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "not-created"
            proc = subprocess.run([sys.executable, str(BUILDER), "--input",
                   str(EXAMPLES / "single-blueprint.json"), "--output",
                   str(output)], capture_output=True, text=True, timeout=12)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertFalse(output.exists())
            self.assertEqual(json.loads(proc.stdout)["status"],
                             "RENDERED_DRAFT_PLAN_NOT_INSTALLED")

    def test_symlinked_output_parent_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            actual = Path(tmp) / "actual"
            actual.mkdir()
            alias = Path(tmp) / "alias"
            try:
                alias.symlink_to(actual, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("symlink unavailable")
            self.reject_write(fixture(), alias / "skill",
                              "OUTPUT_ANCESTOR_SYMLINKED")

    def test_unsupported_blueprint_schema_refused(self):
        d = fixture()
        d["schema_version"] = True
        self.reject(d, "UNSUPPORTED_BLUEPRINT_SCHEMA")


if __name__ == "__main__":
    unittest.main(verbosity=2)
