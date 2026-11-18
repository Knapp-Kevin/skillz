#!/usr/bin/env python3
"""Maintainer-run pure offline exporter fingerprint tests. No skills activated."""
import importlib.util
from pathlib import Path
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "scripts/build-skill-mason-catalog.py"
spec = importlib.util.spec_from_file_location("skill_mason_passive_export", PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

BLOB = "a" * 40
TREE = "b" * 40


class ExportSourceIdentityTests(unittest.TestCase):
    def test_combined_algorithm_reconciles_provenance_skill_blob(self):
        p = {"skill_blob_sha": BLOB, "package_tree_sha": TREE}
        v = {"fingerprint_algorithm": "git-tree-and-blob-sha1",
             "content_blob_sha": BLOB, "package_tree_sha": TREE}
        self.assertEqual(mod._source_git_identity(p, v), (BLOB, TREE))

    def test_combined_algorithm_reconciles_dedicated_entrypoint_aliases(self):
        p = {"skill_md_blob_sha": BLOB, "complete_package_tree_sha": TREE}
        v = {"fingerprint_algorithm": "git-tree-and-blob-sha1",
             "content_blob_sha": BLOB, "skill_md_blob_sha": BLOB,
             "package_tree_sha": TREE}
        self.assertEqual(mod._source_git_identity(p, v), (BLOB, TREE))

    def test_simple_blob_algorithm_uses_content_blob_only_for_entrypoint(self):
        self.assertEqual(
            mod._source_git_identity(
                {}, {"fingerprint_algorithm": "git-blob-sha1",
                     "content_blob_sha": BLOB}), (BLOB, None))

    def test_simple_tree_algorithm_uses_content_blob_only_for_package(self):
        self.assertEqual(
            mod._source_git_identity(
                {}, {"fingerprint_algorithm": "git-tree-sha1",
                     "content_blob_sha": TREE}), (None, TREE))

    def test_unknown_fingerprint_algorithm_never_coerces_content(self):
        self.assertEqual(
            mod._source_git_identity(
                {}, {"fingerprint_algorithm": "sha256",
                     "content_blob_sha": "a" * 64}), (None, None))

    def test_explicit_blob_alias_conflict_is_refused(self):
        with self.assertRaisesRegex(ValueError, "contradictory SKILL.md blob"):
            mod._source_git_identity(
                {"skill_blob_sha": BLOB},
                {"fingerprint_algorithm": "git-blob-sha1",
                 "content_blob_sha": "c" * 40})

    def test_explicit_tree_alias_conflict_is_refused(self):
        with self.assertRaisesRegex(ValueError, "contradictory package tree"):
            mod._source_git_identity(
                {"package_tree_sha": TREE},
                {"fingerprint_algorithm": "git-tree-sha1",
                 "content_blob_sha": "c" * 40})

    def test_malformed_git_claim_refused(self):
        with self.assertRaisesRegex(ValueError, "invalid SKILL.md blob"):
            mod._source_git_identity(
                {"skill_blob_sha": "../unsafe"},
                {"fingerprint_algorithm": "git-blob-sha1",
                 "content_blob_sha": BLOB})

    def test_combined_algorithm_missing_tree_refused(self):
        with self.assertRaisesRegex(ValueError, "combined tree/blob review missing"):
            mod._source_git_identity(
                {}, {"fingerprint_algorithm": "git-tree-and-blob-sha1",
                     "content_blob_sha": BLOB})

    def test_combined_algorithm_missing_entrypoint_refused(self):
        with self.assertRaisesRegex(ValueError, "combined tree/blob review missing"):
            mod._source_git_identity(
                {"package_tree_sha": TREE},
                {"fingerprint_algorithm": "git-tree-and-blob-sha1",
                 "content_blob_sha": ""})

    def test_exact_original_anthropic_frontend_review(self):
        p = yaml.load((ROOT / "registry/skills/anthropic-skills/frontend-design.yaml").read_bytes(),
                      Loader=mod.UniqueLoader)
        v = yaml.load((ROOT / "registry/verification/anthropic-skills/frontend-design.yaml").read_bytes(),
                      Loader=mod.UniqueLoader)
        self.assertEqual(
            mod._source_git_identity(p, v),
            ("a5333457c414d20d625f307df945842c0952ecc3",
             "d79e2a5bb4df4a386c2adcdd9ab8709bba28c3f6"))

    def test_never_promotes_rights_or_behavior(self):
        p = {"skill_blob_sha": BLOB, "package_tree_sha": TREE,
             "license": "unknown", "permission_tier": "unapproved"}
        v = {"fingerprint_algorithm": "git-tree-and-blob-sha1",
             "content_blob_sha": BLOB, "validation_status": "not-run"}
        self.assertEqual(mod._source_git_identity(p, v), (BLOB, TREE))
        self.assertEqual(v["validation_status"], "not-run")
        self.assertEqual(p["license"], "unknown")


if __name__ == "__main__":
    unittest.main()
