#!/usr/bin/env python3
"""Offline, synthetic, repository-anonymous CI Guard classification tests."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("impact", ROOT / "scripts/classify_change.py")
impact = importlib.util.module_from_spec(spec)
spec.loader.exec_module(impact)

RULES = [
    {"match": "prefix", "pattern": "docs/guides/", "category": "documentation"},
    {"match": "exact", "pattern": "README.md", "category": "documentation"},
    {"match": "prefix", "pattern": "src/", "category": "executable-code"},
    {"match": "prefix", "pattern": "model/", "category": "models"},
    {"match": "exact", "pattern": "AGENTS.md", "category": "governance"},
]


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


class PortableClassification(unittest.TestCase):
    def route(self, paths, stage="candidate", rules=RULES):
        return impact.classify(paths, rules, stage)

    def test_no_policy_fails_to_full_even_for_seemingly_passive_docs(self):
        result = impact.classify(["docs/guides/usage.md"])
        self.assertEqual(result["route"], "full")
        self.assertIn("trusted-policy-unavailable", result["reason"])

    def test_explicit_passive_documentation_targeted(self):
        d = self.route(["docs/guides/usage.md", "README.md"])
        self.assertEqual(d["route"], "targeted")
        self.assertEqual(d["categories"], ["documentation"])
        self.assertEqual((d["run_targeted"], d["run_full"]), ("true", "false"))

    def test_unmapped_markdown_fails_full(self):
        self.assertEqual(self.route(["docs/unknown.md"])["route"], "full")

    def test_unnamed_governance_markdown_cannot_be_downclassified(self):
        for path in ("AGENTS.md", "CLAUDE.md", "docs/governance/SECURITY.md",
                     "docs/api-contracts/wire.md", ".github/CODEOWNERS"):
            with self.subTest(path=path):
                self.assertEqual(self.route([path])["route"], "full")

    def test_readme_can_be_model_input_when_consumer_declares_it(self):
        model_rules = [x for x in RULES if x["pattern"] != "README.md"]
        model_rules.append({"match": "exact", "pattern": "README.md", "category": "models"})
        d = self.route(["README.md"], rules=model_rules)
        self.assertEqual(d["route"], "full")
        self.assertIn("models", d["categories"])

    def test_model_extensions_and_dependency_manifests_require_full_at_candidate(self):
        for path in ("model/weights.safetensors", "asset/model.onnx", "src/kernel.rs",
                     "src/main.ts", "Cargo.lock", "package-lock.json",
                     "requirements.txt", "pyproject.toml", "package.json"):
            with self.subTest(path=path):
                d = self.route([path])
                self.assertEqual(d["route"], "full")
                self.assertTrue(d["requires_exact_final_acceptance"])

    def test_known_executable_draft_is_fast_but_never_merge_qualified(self):
        d = self.route(["src/lib.rs"], stage="draft")
        self.assertEqual(d["route"], "targeted")
        self.assertTrue(d["deferred_full_acceptance"])
        self.assertTrue(d["requires_exact_final_acceptance"])
        self.assertFalse(d["merge_qualified"])

    def test_same_source_head_requires_new_full_gate_after_ready_transition(self):
        paths = ["src/library.rs"]
        draft = self.route(paths, stage="draft")
        candidate = self.route(paths, stage="candidate")
        self.assertEqual(draft["route"], "targeted")
        self.assertEqual(candidate["route"], "full")
        self.assertEqual(candidate["run_full"], "true")
        self.assertFalse(draft["merge_qualified"])
        self.assertFalse(candidate["merge_qualified"])

    def test_required_gate_example_rechecks_ready_for_review(self):
        text = (ROOT / "examples/classified-github-pr.yml").read_text(encoding="utf-8")
        self.assertIn("ready_for_review", text)
        self.assertIn("if: ${{ always() }}", text)
        self.assertIn("CLASSIFY_RESULT", text)
        self.assertIn("needs: [classify, docs, rust, model, trust]", text)
        self.assertIn("ci_plan.py qualify", text)
        self.assertIn("ci-evidence.json", text)
        self.assertIn("--group docs", text)
        self.assertNotIn("pull_request_target", text)

    def test_private_repo_template_uses_existing_local_base_checkout(self):
        text = (ROOT / "examples/classified-github-pr.yml").read_text(
            encoding="utf-8")
        # Both checkouts use persist-credentials:false. A later network
        # fetch from "origin" can fail on a private repository.
        self.assertIn('git -C work fetch --no-tags ../trusted "$BASE_SHA"', text)
        self.assertNotIn('git -C work fetch --no-tags --depth=1 origin "$BASE_SHA"', text)
        self.assertIn('path: trusted', text)
        self.assertIn('path: work', text)
        self.assertIn('persist-credentials: false', text)

    def test_draft_unknown_is_full(self):
        self.assertEqual(self.route(["unknown.binary"], stage="draft")["route"], "full")

    def test_workflow_and_governance_draft_stays_full(self):
        for path in (".github/workflows/check.yml", "ci/impact-policy.json",
                     "scripts/ci/runner.py", "AGENTS.md", "release/notes.md"):
            with self.subTest(path=path):
                self.assertEqual(self.route([path], stage="draft")["route"], "full")

    def test_release_stage_enforces_full_even_docs(self):
        d = self.route(["docs/guides/hello.md"], stage="release")
        self.assertEqual(d["route"], "full")

    def test_mixed_docs_and_code_union_full_on_candidate(self):
        d = self.route(["docs/guides/hello.md", "src/app.rs"])
        self.assertEqual(d["route"], "full")
        self.assertEqual(d["categories"], ["documentation", "executable-code"])

    def test_ambiguous_category_conflict_never_downgrades(self):
        rules = RULES + [
            {"match": "suffix", "pattern": ".rs", "category": "documentation"}]
        d = self.route(["src/app.rs"], rules=rules)
        self.assertEqual(d["route"], "full")
        self.assertIn("executable-code", d["categories"])

    def test_missing_unsafe_or_overlarge_diff_falls_full(self):
        cases = [[], ["../escape.md"], ["/root/README.md"],
                 ["docs/guides/injected\nline.md"], ["docs//guide.md"],
                 ["docs\\guides\\test.md"],
                 [f"docs/guides/{i}.md" for i in range(impact.MAX_FILES + 1)]]
        for paths in cases:
            with self.subTest(paths=len(paths)):
                self.assertEqual(self.route(paths)["route"], "full")

    def test_unknown_stage_is_refused(self):
        with self.assertRaises(impact.ClassificationError):
            self.route(["README.md"], stage="unsupported")

    def test_schema_rejects_unsafe_and_overpermissive_rules(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "policy.json"
            invalid = [
                {"schema_version": 1, "rules": [{"match":"prefix","pattern":"../docs","category":"documentation"}]},
                {"schema_version": 1, "rules": [{"match":"suffix","pattern":"md","category":"documentation"}]},
                {"schema_version": 1, "rules": [{"match":"exact","pattern":"README.md","category":"unknown"}]},
                {"schema_version": True, "rules": []},
                {"schema_version": 1, "rules": [], "self_approved": True},
                {"schema_version": 1, "rules": [{"match":"regex","pattern":".*","category":"documentation"}]},
            ]
            for sample in invalid:
                with self.subTest(sample=sample):
                    path.write_text(json.dumps(sample), encoding="utf-8")
                    with self.assertRaises(impact.ClassificationError):
                        impact.load_policy(path)

    def test_documentation_prefix_must_respect_directory_boundary(self):
        """A policy for docs must never classify docsecrets as passive."""
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "policy.json"
            for prefix in ("docs", "docs-private", "src", "docs//",
                           "docs/../", "docs/./"):
                with self.subTest(prefix=prefix):
                    p.write_text(json.dumps({
                        "schema_version": 1, "rules": [
                            {"match": "prefix", "pattern": prefix,
                             "category": "documentation"}]
                    }), encoding="utf-8")
                    with self.assertRaises(impact.ClassificationError):
                        impact.load_policy(p)
            p.write_text(json.dumps({
                "schema_version": 1, "rules": [
                    {"match": "prefix", "pattern": "docs/",
                     "category": "documentation"}]
            }), encoding="utf-8")
            checked = impact.load_policy(p)
            self.assertEqual(
                impact.classify(["docs/guides/usage.md"], checked)["route"],
                "targeted")
            for adjacent in ("docsecrets/incident.md",
                             "docs-private/keys.md",
                             "docs-shared/contract.md"):
                with self.subTest(adjacent=adjacent):
                    self.assertEqual(
                        impact.classify([adjacent], checked)["route"], "full")

    def test_direct_prefix_rule_cannot_bypass_directory_boundary(self):
        # Programmatic users of classify() may skip load_policy().
        bad_rule = [{"match": "prefix", "pattern": "docs",
                     "category": "documentation"}]
        self.assertEqual(
            self.route(["docsecrets/incident.md"], rules=bad_rule)["route"],
            "full")
        self.assertEqual(
            self.route(["docs/guide.md"], rules=bad_rule)["route"],
            "full")

    def test_direct_global_doc_suffix_cannot_skip_checks(self):
        # Programmatic consumers cannot bypass the trusted policy boundary.
        bypass = [{"match": "suffix", "pattern": ".md",
                   "category": "documentation"}]
        for path in ("README.md", "docs/passive.md", "docs-private/plan.md"):
            with self.subTest(path=path):
                self.assertEqual(
                    self.route([path], rules=bypass)["route"], "full")

    def test_global_markdown_suffix_cannot_claim_passive_docs(self):
        """Markdown can be a model/build input, release or governance asset."""
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "policy.json"
            p.write_text(json.dumps({
                "schema_version": 1, "rules": [
                    {"match": "suffix", "pattern": ".md",
                     "category": "documentation"}]
            }), encoding="utf-8")
            with self.assertRaises(impact.ClassificationError):
                impact.load_policy(p)
            # Explicit trusted approved directories still work.
            p.write_text(json.dumps({
                "schema_version": 1, "rules": [
                    {"match": "prefix", "pattern": "docs/passive/",
                     "category": "documentation"},
                    {"match": "suffix", "pattern": ".md",
                     "category": "governance"}]
            }), encoding="utf-8")
            checked = impact.load_policy(p)
            self.assertEqual(
                impact.classify(["docs/passive/guide.md"], checked)["route"],
                "full")  # Conservative category wins.
            self.assertEqual(
                impact.classify(["notes/manual.md"], checked)["route"], "full")

    def test_ambiguous_duplicate_json_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "policy.json"
            p.write_text('{"schema_version":1,"schema_version":1,"rules":[]}',
                         encoding="utf-8")
            with self.assertRaises(impact.ClassificationError):
                impact.load_policy(p)

    def test_non_string_policy_categories_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "policy.json"
            p.write_text(json.dumps({"schema_version":1,"rules":[
                {"match":"exact","pattern":"README.md","category":["documentation"]}
            ]}), encoding="utf-8")
            with self.assertRaises(impact.ClassificationError):
                impact.load_policy(p)

    def test_trusted_policy_file_is_parsed_without_executing_commands(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "policy.json"
            p.write_text(json.dumps({"schema_version": 1, "rules": RULES}), encoding="utf-8")
            rules = impact.load_policy(p)
            self.assertEqual(self.route(["docs/guides/usage.md"], rules=rules)["route"], "targeted")

    def test_rename_and_git_symlink_stay_conservative(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            git(repo, "init", "-q")
            git(repo, "config", "user.name", "Test")
            git(repo, "config", "user.email", "test@example.invalid")
            (repo / "README.md").write_text("first\n", encoding="utf-8")
            (repo / "copy.md").write_text("safe\n", encoding="utf-8")
            git(repo, "add", "."); git(repo, "commit", "-qm", "base")
            base = git(repo, "rev-parse", "HEAD")
            (repo / "README.md").rename(repo / "code.rs")
            git(repo, "add", "-A"); git(repo, "commit", "-qm", "rename")
            renamed = git(repo, "rev-parse", "HEAD")
            paths = impact.changed_paths(repo, base, renamed)
            self.assertIn("README.md", paths)
            self.assertIn("code.rs", paths)
            self.assertEqual(self.route(paths)["route"], "full")
            (repo / "copy.md").unlink()
            try:
                (repo / "copy.md").symlink_to("code.rs")
            except (OSError, NotImplementedError):
                self.skipTest("symlink unsupported")
            git(repo, "add", "-A"); git(repo, "commit", "-qm", "symlink")
            head = git(repo, "rev-parse", "HEAD")
            self.assertIn("__NONREGULAR_FILE_OR_MODE__", impact.changed_paths(repo, renamed, head))
            self.assertEqual(self.route(impact.changed_paths(repo, renamed, head))["route"], "full")

    def test_git_mode_requires_exact_pinned_commits(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(impact.ClassificationError):
                impact.changed_paths(Path(tmp), "main", "HEAD")

    def test_no_implicit_permission_from_successful_routing(self):
        d = self.route(["docs/guides/intro.md"])
        self.assertFalse(d["merge_qualified"])
        self.assertIn("independent required security", d["mandatory_floor"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
