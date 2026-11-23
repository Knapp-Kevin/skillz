"""Offline adversarial tests of Skill Pack structural metadata only.

All content is invented. These tests do not run a pack or qualify any
consumer's actual behavior, preferences, installations or source rights.
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

ROOT=Path(__file__).resolve().parents[2]
PATH=ROOT/"engine"/"packs"/"check_pack.py"
EXAMPLE=ROOT/"engine"/"packs"/"fictional-evidence-brief"
SPEC=importlib.util.spec_from_file_location("skillz_pack_contract",PATH)
checker=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


def example():
    return json.loads((EXAMPLE/"pack.json").read_text(encoding="utf-8"))


class PackStructureTests(unittest.TestCase):
    def check(self,manifest=None):
        return checker.validate(EXAMPLE,manifest if manifest is not None else example())

    def reject(self,case,needle):
        with self.assertRaisesRegex(checker.PackHold,needle):
            self.check(case)

    def test_valid_pack_is_not_runtime_or_installed_proof(self):
        result=self.check()
        self.assertEqual(result["status"],"PACK_STRUCTURE_VALID_NOT_EXECUTED")
        self.assertEqual(result["required_modules"],3)
        self.assertEqual(result["optional_modules"],1)
        self.assertEqual(result["modules_order"],["collect","check","summary","style"])
        for key in ("source_rights_authenticated",
                    "semantic_quality_verified","agent_or_consumer_outcome_observed",
                    "installed_or_published","execution_or_mutation_performed"):
            self.assertFalse(result[key])

    def test_single_skill_not_forced_into_pack(self):
        case=example()
        case["modules"]=case["modules"][:1]
        self.reject(case,"PACK_NOT_COMPOSITION_WORTHY")

    def test_missing_required_file_is_hold(self):
        case=example()
        case["files"].append("components/absent.md")
        self.reject(case,"MISSING_PACKAGE_FILE")

    def test_declared_module_path_must_be_pack_local(self):
        case=example()
        case["modules"][0]["path"]="../private.md"
        self.reject(case,"UNSAFE_PACKAGE_PATH")

    def test_duplicate_pack_inventory_refused(self):
        case=example()
        case["files"].append(case["files"][-1])
        self.reject(case,"DUPLICATE_PACKAGE_FILE")

    def test_module_path_must_be_in_inventory(self):
        case=example()
        case["files"].remove("phases/style.md")
        self.reject(case,"UNDECLARED_OR_DUPLICATED_MODULE_PATH")

    def test_one_path_cannot_have_two_module_owners(self):
        case=example()
        case["modules"][1]["path"]=case["modules"][0]["path"]
        self.reject(case,"UNDECLARED_OR_DUPLICATED_MODULE_PATH")

    def test_cycle_is_refused(self):
        case=example()
        case["modules"][0]["requires"]=["summary"]
        self.reject(case,"CYCLIC_MODULE_DEPENDENCY")

    def test_unknown_dependency_is_refused(self):
        case=example()
        case["modules"][0]["requires"]=["no-such-phase"]
        self.reject(case,"UNKNOWN_MODULE_DEPENDENCY")

    def test_required_must_not_depend_on_optional(self):
        case=example()
        case["modules"][2]["requires"]=["style"]
        self.reject(case,"REQUIRED_MODULE_DEPENDS_ON_OPTIONAL")

    def test_optional_branch_without_safe_fallback_holds(self):
        case=example()
        case["modules"][3]["fallback"]=None
        self.reject(case,"INVALID_TEXT")

    def test_pack_authority_is_a_ceiling_not_permission(self):
        case=example()
        case["modules"][1]["authority"]="approval-gated"
        self.reject(case,"MODULE_AUTHORITY_EXCEEDS_PACK")

    def test_skill_module_must_have_skill_entrypoint(self):
        case=example()
        case["modules"][2]["kind"]="phase"
        self.reject(case,"MODULE_KIND_PATH_MISMATCH")

    def test_unknown_rights_cannot_be_called_authorized_adaptation(self):
        case=example()
        case["modules"][1]["origin"]="authorized-adaptation"
        self.reject(case,"ADAPTATION_LACKS_RIGHTS_RECEIPT")

    def test_declared_rights_are_not_authenticated(self):
        case=example()
        case["modules"][1]["origin"]="authorized-adaptation"
        case["modules"][1]["source_identity"]="fictional-identity@pinned"
        case["modules"][1]["rights_basis"]="synthetic-permission-claim"
        result=self.check(case)
        self.assertFalse(result["source_rights_authenticated"])

    def test_consumer_value_inside_manifest_is_refused(self):
        case=example()
        case["preference_slots"][0]["value"]="concise"
        self.reject(case,"INVALID_FIELDS:preference")

    def test_consumer_profile_at_pack_root_is_refused(self):
        case=example()
        case["user_profiles"]={"someone":"concise"}
        self.reject(case,"INVALID_FIELDS:pack")

    def test_unsafe_override_cannot_be_a_preference(self):
        case=example()
        case["preference_slots"][0]["key"]="skip-validation"
        self.reject(case,"UNSAFE_PREFERENCE_SLOT")

    def test_preference_requires_opt_in_private_scope(self):
        case=example()
        case["preference_slots"][0]["scope"]="public-global"
        self.reject(case,"PREFERENCE_MUST_BE_PRIVATE_OPT_IN_ENUM")

    def test_preference_choice_cannot_override_safety_policy(self):
        case=example()
        case["feedback_policy"]["consumer"]="auto-upstream"
        self.reject(case,"UNSAFE_FEEDBACK_ROUTING_POLICY")

    def test_optional_may_not_have_nonexistent_default(self):
        case=example()
        case["preference_slots"][0]["default"]="unavailable"
        self.reject(case,"PREFERENCE_DEFAULT_NOT_ALLOWED")

    def test_signed_claim_does_not_create_host_authority(self):
        case=example()
        case["host_qualified"]=True
        self.reject(case,"INVALID_FIELDS:pack")

    def test_manifest_rejects_boolean_version(self):
        case=example()
        case["schema_version"]=True
        self.reject(case,"UNSUPPORTED_PACK_SCHEMA")

    def test_missing_local_markdown_link_is_refused(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)/"pack"
            shutil.copytree(EXAMPLE,folder)
            with (folder/"SKILL.md").open("a",encoding="utf-8") as stream:
                stream.write("\n[Unsafe link](../outside.md)\n")
            with self.assertRaisesRegex(checker.PackHold,"LINK_LEAVES_PACK"):
                checker.validate(folder,example())

    def test_symlink_in_fictional_bundle_is_refused(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)/"pack"
            shutil.copytree(EXAMPLE,folder)
            target=folder/"phases"/"style.md"
            target.unlink()
            try:
                target.symlink_to(folder/"phases"/"collect.md")
            except (OSError,NotImplementedError):
                self.skipTest("test host cannot create a symlink")
            with self.assertRaisesRegex(checker.PackHold,"SYMLINKED_PACKAGE_PATH"):
                checker.validate(folder,example())

    def test_cli_accepts_structure_without_executing_pack(self):
        run=subprocess.run([sys.executable,str(PATH),"--root",str(EXAMPLE)],
                           capture_output=True,text=True,timeout=8)
        self.assertEqual(run.returncode,0,run.stderr)
        r=json.loads(run.stdout)
        self.assertEqual(r["status"],"PACK_STRUCTURE_VALID_NOT_EXECUTED")
        self.assertFalse(r["installed_or_published"])

    def test_cli_rejects_duplicate_and_nonfinite_json(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)/"pack"
            shutil.copytree(EXAMPLE,folder)
            target=folder/"pack.json"
            for text in ('{"id":1,"id":2}', '{"unexpected":NaN}'):
                with self.subTest(text=text):
                    target.write_text(text,encoding="utf-8")
                    run=subprocess.run(
                        [sys.executable,str(PATH),"--root",str(folder)],
                        capture_output=True,text=True,timeout=8)
                    self.assertEqual(run.returncode,2)
                    self.assertIn("PACK_STRUCTURE_HOLD",run.stderr)

    def test_pack_documentation_preserves_routing_and_stop_rules(self):
        guide=(ROOT/"engine"/"packs"/"README.md").read_text()
        tree=(ROOT/"engine"/"packs"/"feedback-decision-tree.md").read_text()
        for fragment in ("CANONICAL_IMPROVEMENT", "LOCAL_PREFERENCE", "MIXED",
                         "NO_ACTION","STOP_NO_CHANGE","user-private",
                         "shared component", "source fingerprints"):
            self.assertIn(fragment.casefold(),(guide+"\n"+tree).casefold())
        self.assertIn("not another user-facing skill",guide.lower())
        self.assertIn("current user",tree.lower())
        self.assertIn("consent",tree.lower())
        self.assertIn("revoked",tree.lower())

if __name__=="__main__":
    unittest.main(verbosity=2)
