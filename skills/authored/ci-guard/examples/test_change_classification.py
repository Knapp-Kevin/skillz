#!/usr/bin/env python3
"""Self-contained CPU-only classifier acceptance; no external services."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SKILL_DIR = Path(__file__).resolve().parents[1]
TARGET = SKILL_DIR / "scripts/classify_change.py"
spec = importlib.util.spec_from_file_location("classify_change", TARGET)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


class RiskBasedSelection(unittest.TestCase):
    def test_docs_only_skips_python_and_full(self):
        d = module.classify(["README.md", "docs/setup.rst"])
        self.assertEqual(d["route"], "docs")
        self.assertEqual((d["run_docs"], d["run_python"], d["run_full"]),
                         ("true", "false", "false"))

    def test_python_code_runs_python(self):
        d = module.classify(["src/runtime.py", "tests/test_runtime.py"])
        self.assertEqual(d["route"], "python")
        self.assertEqual(d["run_python"], "true")
        self.assertEqual(d["run_full"], "false")

    def test_mixed_docs_and_python_preserves_both(self):
        d = module.classify(["README.md", "src/main.py"])
        self.assertEqual(d["selected"], ["docs", "python"])

    def test_workflow_yaml_triggers_full(self):
        d = module.classify([".github/workflows/security.yml"])
        self.assertEqual(d["route"], "full")
        self.assertEqual(d["run_full"], "true")

    def test_dependency_lock_avoids_false_docs_only(self):
        for name in ("requirements.txt", "pyproject.toml",
                     "poetry.lock", "Cargo.lock", "package-lock.json"):
            with self.subTest(name=name):
                self.assertEqual(module.classify([name])["route"], "full")

    def test_release_policy_md_is_protected(self):
        for name in ("SECURITY.md", "LICENSE.md",
                     ".github/CODEOWNERS", "release/notes.md",
                     "docs/api-contracts/interface.md"):
            with self.subTest(name=name):
                self.assertEqual(module.classify([name])["route"], "full")

    def test_unknown_file_falls_back_to_full(self):
        self.assertEqual(module.classify(["model.weights"])["route"], "full")
        self.assertEqual(module.classify(["src/index.ts"])["route"], "full")

    def test_changed_classifier_itself_falls_back_full(self):
        self.assertEqual(
            module.classify(["skills/authored/ci-guard/scripts/classify_change.py"])
            ["route"], "full")
        # Consumer installations also classify their workflow policy as full.
        self.assertEqual(module.classify(["ci/classify_change.py"])["route"], "full")

    def test_unverified_empty_diff_falls_back_full(self):
        self.assertEqual(module.classify([])["route"], "full")

    def test_too_many_paths_falls_back_full(self):
        paths = [f"docs/{i}.md" for i in range(module.MAX_FILES + 1)]
        self.assertEqual(module.classify(paths)["route"], "full")

    def test_unsafe_path_falls_back_full(self):
        for path in ("../foo.md", "/tmp/safe.md", "docs/a\nfile.md"):
            with self.subTest(path=path):
                self.assertEqual(module.classify([path])["route"], "full")

    def test_untrusted_yaml_mixed_docs_is_full(self):
        self.assertEqual(
            module.classify(["README.md", ".github/workflows/ci.yml"])["route"],
            "full")

    def test_no_permissions_from_metadata(self):
        d = module.classify(["README.md"])
        self.assertIn("independent required security", d["mandatory_floor"])

    def test_git_real_docs_change_and_rename_to_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            git(repo, "init", "-q")
            git(repo, "config", "user.name", "CI Test")
            git(repo, "config", "user.email", "ci-test@example.invalid")
            (repo / "README.md").write_text("before\n", encoding="utf-8")
            git(repo, "add", "README.md")
            git(repo, "commit", "-qm", "baseline")
            base = git(repo, "rev-parse", "HEAD")
            (repo / "README.md").write_text("after\n", encoding="utf-8")
            git(repo, "commit", "-qam", "docs")
            docs_head = git(repo, "rev-parse", "HEAD")
            self.assertEqual(module.classify(module.changed_paths(repo, base, docs_head))
                             ["route"], "docs")
            (repo / "README.md").rename(repo / "runtime.py")
            git(repo, "add", "-A")
            git(repo, "commit", "-qm", "rename docs to code")
            code_head = git(repo, "rev-parse", "HEAD")
            paths = module.changed_paths(repo, docs_head, code_head)
            self.assertIn("runtime.py", paths)
            self.assertEqual(module.classify(paths)["route"], "mixed")

    def test_invalid_commit_ref_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(module.ClassificationError):
                module.changed_paths(Path(tmp), "main", "HEAD")


if __name__ == "__main__":
    unittest.main(verbosity=2)
