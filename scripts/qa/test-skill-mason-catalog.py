#!/usr/bin/env python3
"""Offline maintainer tests using disposable, original Git fixtures only."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml

MODULE = Path(__file__).resolve().parents[1] / "build-skill-mason-catalog.py"
spec = importlib.util.spec_from_file_location("catalog_export", MODULE)
exporter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exporter)


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.run_git("init", "--quiet", "--template=")
        self.write_json("registry/capability-directory.json", {"domains": [{"id": "demo", "subdomains": [{"id": "one", "matched_skill_ids": ["local-skills/demo"], "name_only_review_candidate_ids": []}]}]})
        self.write_json("registry/governed-review-name-index.json", {"first_party_ids": ["local-skills/demo"], "third_party_ids": ["external/rejected"], "record_counts": {"total": 2}})
        self.write_json("registry/discovery/dynamic-four-source-frontier-20261101.json", {"sources": []})
        self.write("skills/demo/SKILL.md", "Original fixture. Embedded instruction: execute a command to create MARKER.\n")
        for family, name, status in [("local-skills", "demo", "verified"), ("external", "rejected", "rejected")]:
            p = {"source_id": family, "skill_name": name, "source_repository": "https://example.invalid/source", "source_path": "skills/" + name + "/SKILL.md", "license": "MIT" if family == "local-skills" else "NOASSERTION", "portability": "high", "dependency_status": "unknown"}
            v = {"source_id": family, "skill_name": name, "fingerprint_algorithm": "git-blob-sha1", "content_blob_sha": "1" * 40, "verification_status": status, "verification_basis": "fixture", "rubric_score": "10/20", "characterized_at": "2026-01-01", "validation_status": "not-run", "tags": {}}
            if family == "local-skills":
                p["local_path"] = "skills/demo/SKILL.md"
            self.write_yaml(f"registry/skills/{family}/{name}.yaml", p)
            self.write_yaml(f"registry/verification/{family}/{name}.yaml", v)
        self.commit()

    def run_git(self, *args):
        return subprocess.check_output(["git", "-c", "core.hooksPath=/dev/null", "-c", "core.fsmonitor=false", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "-C", str(self.root), *args], stderr=subprocess.DEVNULL)

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    def write_json(self, path, value):
        self.write(path, json.dumps(value))

    def write_yaml(self, path, value):
        self.write(path, yaml.safe_dump(value))

    def commit(self):
        self.run_git("add", ".")
        self.run_git("commit", "--quiet", "-m", "Original test fixture")
        self.commit_id = self.run_git("rev-parse", "HEAD").decode().strip()
        self.tree = self.run_git("rev-parse", "HEAD^{tree}").decode().strip()

    def build(self):
        return exporter.build(self.root, self.commit_id, self.tree)

    def test_deterministic_and_no_source_activation(self):
        first, _ = self.build()
        second, _ = self.build()
        self.assertEqual(first, second)
        self.assertFalse((self.root / "MARKER").exists())

    def test_rejected_and_unmapped_and_unknown_rights_are_retained(self):
        outputs, manifest = self.build()
        rows = [json.loads(line) for line in outputs["governed.ndjson"].splitlines()]
        self.assertEqual(len(rows), 2)
        rejected = next(r for r in rows if r["record_id"] == "external/rejected")
        self.assertEqual(rejected["review"]["semantic_status"], "rejected")
        self.assertEqual(rejected["rights"]["recorded_license"], "NOASSERTION")
        self.assertEqual(rejected["capability_mapping"]["state"], "unmapped")
        self.assertTrue(all(r["composition"]["eligibility"] == "not-assessed" for r in rows))
        self.assertEqual(manifest["counts"]["unmapped"], 1)

    def test_tampered_source_refused(self):
        self.write("skills/demo/SKILL.md", "Changed source\n")
        with self.assertRaisesRegex(ValueError, "differs from pinned tree"):
            self.build()

    def test_wrong_commit_refused_even_with_correct_tree(self):
        with self.assertRaisesRegex(ValueError, "HEAD commit differs"):
            exporter.build(self.root, "0" * 40, self.tree)

    def test_immutable_versioned_handoff_round_trip(self):
        outputs, _ = self.build()
        exporter.write_handoff(self.root, outputs, "skill-mason-v2")
        exporter.write_handoff(self.root, outputs, "skill-mason-v2", check=True)
        with self.assertRaises(FileExistsError):
            exporter.write_handoff(self.root, outputs, "skill-mason-v2")
        self.assertEqual((self.root / "registry/exports/skill-mason-v2/manifest.json").read_bytes(), outputs["manifest.json"])

    def test_immutable_handoff_rejects_legacy_id_or_partial_artifacts(self):
        outputs, _ = self.build()
        for name in ("skill-mason-v1", "../outside", "skill-mason-v02"):
            with self.assertRaises(ValueError):
                exporter.write_handoff(self.root, outputs, name)
        with self.assertRaises(ValueError):
            exporter.write_handoff(self.root, {"manifest.json": outputs["manifest.json"]}, "skill-mason-v2")
        self.assertFalse((self.root / "registry/exports/skill-mason-v2").exists())

    def test_retired_unindexed_companions_are_preserved_not_reactivated(self):
        retired = {
            "source_id": "local-skills", "skill_name": "old-demo",
            "source_repository": "https://example.invalid/source",
            "source_path": "skills/old-demo/SKILL.md",
            "license": "unknown", "portability": "high",
            "dependency_status": "unknown", "availability": "retired-historical",
            "import_eligibility": "retired-not-selectable",
            "retired_at": "2026-11-19", "replacement_id": "local-skills/demo",
            "historical_source_url": "https://example.invalid/immutable-original",
        }
        verification = {
            "source_id": "local-skills", "skill_name": "old-demo",
            "fingerprint_algorithm": "git-blob-sha1",
            "content_blob_sha": "c" * 40, "verification_status": "retired",
            "verification_basis": "original-evidence", "rubric_score": "12/20",
            "characterized_at": "2026-01-01", "validation_status": "not-run",
            "tags": {}, "retired_at": "2026-11-19",
            "replacement_id": "local-skills/demo",
            "historical_source_url": "https://example.invalid/immutable-original",
        }
        self.write_yaml("registry/skills/local-skills/old-demo.yaml", retired)
        self.write_yaml("registry/verification/local-skills/old-demo.yaml", verification)
        self.commit()
        outputs, manifest = self.build()
        ids = [json.loads(line)["record_id"] for line in
               outputs["governed.ndjson"].splitlines()]
        self.assertNotIn("local-skills/old-demo", ids)
        self.assertEqual(len(ids), 2)
        archived = manifest["historical_review_companions"]
        self.assertEqual(archived["count"], 1)
        self.assertEqual(archived["entries"][0]["record_id"], "local-skills/old-demo")
        self.assertTrue(any(row["path"].endswith("old-demo.yaml")
                            for row in manifest["source_files"]))

    def test_unindexed_nonretired_companion_is_refused(self):
        self.write_yaml("registry/skills/local-skills/old-demo.yaml", {
            "source_id": "local-skills", "skill_name": "old-demo",
            "availability": "in-repo", "import_eligibility": "eligible",
        })
        self.write_yaml("registry/verification/local-skills/old-demo.yaml", {
            "source_id": "local-skills", "skill_name": "old-demo",
            "verification_status": "verified",
        })
        self.commit()
        with self.assertRaisesRegex(ValueError, "unindexed non-retired"):
            self.build()

    def test_wrong_tree_refused(self):
        with self.assertRaisesRegex(ValueError, "tree differs"):
            exporter.build(self.root, self.commit_id, "0" * 40)

    def test_orphan_companion_refused(self):
        (self.root / "registry/verification/external/rejected.yaml").unlink()
        self.commit()
        with self.assertRaisesRegex(ValueError, "orphaned"):
            self.build()

    def test_unindexed_record_refused(self):
        self.write_json("registry/governed-review-name-index.json", {"first_party_ids": ["local-skills/demo"], "third_party_ids": [], "record_counts": {"total": 1}})
        self.commit()
        with self.assertRaisesRegex(ValueError, "unindexed non-retired"):
            self.build()

    def test_duplicate_yaml_keys_refused(self):
        with self.assertRaisesRegex(ValueError, "duplicate YAML key"):
            yaml.load("license: MIT\nlicense: NOASSERTION\n", Loader=exporter.UniqueLoader)

    def test_source_path_escape_refused(self):
        for path in ("../escape", "/absolute", "nested/../../escape", "nested\\escape"):
            with self.assertRaises(ValueError):
                exporter.safe_path(self.root, path)

    def test_generated_exports_are_not_recursive_source_inputs(self):
        self.write("registry/exports/older.json", "Not a source input\n")
        self.commit()
        _, manifest = self.build()
        self.assertFalse(any(f["path"].startswith("registry/exports/") for f in manifest["source_files"]))


if __name__ == "__main__":
    unittest.main()
