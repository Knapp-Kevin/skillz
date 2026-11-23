"""Synthetic adversarial PR integration plan tests; no GitHub calls or writes."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "plan.py"
spec = importlib.util.spec_from_file_location("integration_plan", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
A, B, C = "a" * 40, "b" * 40, "c" * 40


def pr(number, head=B, **updates):
    value = {"number": number, "head_sha": head, "base_sha": A, "draft": False,
             "mergeability": "clean", "review": {"state": "approved", "head_sha": head},
             "checks": [{"name": "unit", "app": "actions", "state": "success", "head_sha": head},
                        {"name": "security", "app": "security", "state": "success", "head_sha": head}],
             "depends_on": [], "touched_paths": ["src/component_%s.py" % number],
             "paths_complete": True, "issue_refs": [number + 300]}
    value.update(updates)
    return value


def data(*prs):
    return {"schema_version": 1, "repository": "fictional/example", "observed_at": "2026-11-22T21:00:00Z",
            "base_branch": "main", "base_sha": A,
            "policy": {"observed_complete": True, "merge_queue": "none", "review_required": True,
                       "required_checks": [{"name": "unit", "app": "actions"},
                                           {"name": "security", "app": "security"}]},
            "prs": list(prs) if prs else [pr(101)]}


class IntegrationTest(unittest.TestCase):
    def result(self, d=None):
        return mod.plan(data() if d is None else d)

    def hold(self, needle, d):
        with self.assertRaisesRegex(mod.Hold, needle):
            mod.plan(d)

    def test_only_live_recheck_candidate_never_a_merged_outcome(self):
        r = self.result()
        self.assertEqual(r["prs"][0]["state"], "LIVE_RECHECK_CANDIDATE")
        self.assertEqual(r["first_recheck_candidate"], 101)
        for k in ("live_provider_verified", "actual_merge_eligibility_verified",
                  "review_and_security_rules_independently_verified",
                  "merge_queue_group_ci_verified", "merge_performed",
                  "postmerge_delivery_verified", "issues_closed"):
            self.assertFalse(r[k], k)
        self.assertEqual(r["prs"][0]["declared_issue_refs_not_closed"], [401])

    def test_draft_requires_blocker_fix(self):
        result = self.result(data(pr(1, draft=True)))["prs"][0]
        self.assertEqual(result["state"], "BLOCKED")
        self.assertIn("DRAFT_PR", result["blocking_reasons"])

    def test_reported_merge_conflict_requires_fix(self):
        self.assertIn("OBSERVED_CONFLICT_NEEDS_REPAIR",
                      self.result(data(pr(1, mergeability="conflicting")))["prs"][0]["blocking_reasons"])

    def test_unknown_mergeability_must_not_recommend_merge(self):
        r = self.result(data(pr(1, mergeability="unknown")))["prs"][0]
        self.assertEqual(r["state"], "HOLD_RECHECK")
        self.assertIn("MERGEABILITY_NOT_ESTABLISHED", r["unverified_requirements"])

    def test_provider_reported_blocked_kept_distinct(self):
        r = self.result(data(pr(1, mergeability="blocked")))["prs"][0]
        self.assertIn("PROVIDER_REPORTED_BLOCKED", r["blocking_reasons"])

    def test_stale_check_at_previous_head_is_held(self):
        p = pr(1)
        p["checks"][0]["head_sha"] = C
        r = self.result(data(p))["prs"][0]
        self.assertIn("STALE_CHECK_HEAD:unit@actions", r["unverified_requirements"])
        self.assertEqual(r["state"], "HOLD_RECHECK")

    def test_missing_required_security_check_holds(self):
        p = pr(1)
        p["checks"].pop()
        self.assertIn("REQUIRED_CHECK_NOT_OBSERVED:security@security",
                      self.result(data(p))["prs"][0]["unverified_requirements"])

    def test_failed_required_check_is_blocked(self):
        p = pr(1)
        p["checks"][0]["state"] = "failure"
        r = self.result(data(p))["prs"][0]
        self.assertIn("REQUIRED_CHECK_FAILED:unit@actions", r["blocking_reasons"])

    def test_neutral_skipped_and_pending_are_not_silent_success(self):
        for status in ("neutral", "skipped", "pending", "cancelled", "unknown"):
            with self.subTest(status=status):
                p = pr(1)
                p["checks"][0]["state"] = status
                r = self.result(data(p))["prs"][0]
                self.assertIn("REQUIRED_CHECK_NOT_CONFIRMED_SUCCESS:unit@actions",
                              r["unverified_requirements"])

    def test_same_check_name_different_app_is_not_equivalent(self):
        d = data()
        d["policy"]["required_checks"][0]["app"] = "trusted-app"
        self.assertIn("REQUIRED_CHECK_NOT_OBSERVED:unit@trusted-app",
                      self.result(d)["prs"][0]["unverified_requirements"])

    def test_approval_on_old_head_is_not_accepted(self):
        p = pr(1)
        p["review"]["head_sha"] = C
        self.assertIn("REVIEW_NOT_BOUND_TO_CURRENT_HEAD",
                      self.result(data(p))["prs"][0]["unverified_requirements"])

    def test_changes_requested_blocks_instead_of_counting_approval(self):
        p = pr(1)
        p["review"]["state"] = "changes_requested"
        self.assertIn("REVIEW_CHANGES_REQUESTED",
                      self.result(data(p))["prs"][0]["blocking_reasons"])

    def test_unknown_or_pending_review_holds(self):
        for state in ("pending", "unknown"):
            p = pr(1)
            p["review"]["state"] = state
            self.assertIn("REQUIRED_REVIEW_NOT_APPROVED",
                          self.result(data(p))["prs"][0]["unverified_requirements"])

    def test_explicit_no_review_policy_with_verified_policy_is_allowed_as_candidate(self):
        d = data()
        d["policy"]["review_required"] = False
        d["prs"][0]["review"] = {"state": "unknown", "head_sha": None}
        self.assertEqual(self.result(d)["prs"][0]["state"], "LIVE_RECHECK_CANDIDATE")

    def test_unverified_branch_policy_blocks_eligibility_inference(self):
        d = data()
        d["policy"]["observed_complete"] = False
        self.assertIn("BRANCH_POLICY_NOT_COMPLETELY_OBSERVED",
                      self.result(d)["prs"][0]["unverified_requirements"])

    def test_merge_queue_unknown_blocks_eligibility_inference(self):
        d = data()
        d["policy"]["merge_queue"] = "unknown"
        self.assertIn("MERGE_QUEUE_POLICY_UNKNOWN",
                      self.result(d)["prs"][0]["unverified_requirements"])

    def test_merge_queue_required_is_candidate_only_not_queue_pass(self):
        d = data()
        d["policy"]["merge_queue"] = "required"
        r = self.result(d)
        self.assertEqual(r["first_recheck_candidate"], 101)
        self.assertFalse(r["merge_queue_group_ci_verified"])

    def test_base_sha_not_equal_snapshot_requires_recheck(self):
        p = pr(1, base_sha=C)
        self.assertIn("BASE_REVISION_MISMATCH",
                      self.result(data(p))["prs"][0]["unverified_requirements"])

    def test_simple_dependency_orders_parent_but_blocks_child(self):
        d = data(pr(103, depends_on=[102]), pr(102))
        r = self.result(d)
        self.assertEqual(r["plan_order"], [102, 103])
        self.assertEqual(r["first_recheck_candidate"], 102)
        self.assertEqual(r["prs"][1]["state"], "HOLD_RECHECK")
        self.assertIn("WAIT_FOR_PARENT_INTEGRATION_AND_REFRESH:#102",
                      r["prs"][1]["unverified_requirements"])

    def test_multiple_stacked_dependencies_ordered_deterministically(self):
        d = data(pr(4, depends_on=[3, 2]), pr(3, depends_on=[2]), pr(2))
        self.assertEqual(self.result(d)["plan_order"], [2, 3, 4])

    def test_missing_dependency_needs_evidence_not_automatic_assumption(self):
        r = self.result(data(pr(2, depends_on=[1])))
        self.assertIn("DEPENDENCY_NOT_IN_OPEN_SNAPSHOT_OR_PROVEN_MERGED:#1",
                      r["prs"][0]["unverified_requirements"])

    def test_cycle_is_invalid_even_if_every_pr_has_green_checks(self):
        self.hold("DEPENDENCY_CYCLE", data(pr(1, depends_on=[2]), pr(2, depends_on=[1])))

    def test_self_dependency_holds(self):
        self.hold("invalid/self PR dependency", data(pr(1, depends_on=[1])))

    def test_duplicate_dependency_is_rejected(self):
        self.hold("duplicate entries", data(pr(2, depends_on=[1, 1])))

    def test_same_file_modified_by_two_prs_is_only_advisory(self):
        p1 = pr(1, touched_paths=["src/core.py"])
        p2 = pr(2, touched_paths=["src/core.py"])
        rows = self.result(data(p1, p2))["prs"]
        self.assertEqual(rows[0]["state"], "LIVE_RECHECK_CANDIDATE")
        self.assertEqual(rows[0]["overlapping_paths_advisory"],
                         [{"with_pr": 2, "paths": ["src/core.py"]}])
        self.assertEqual(rows[1]["overlapping_paths_advisory"][0]["with_pr"], 1)

    def test_incomplete_paths_hold_without_false_no_collision(self):
        row = self.result(data(pr(1, paths_complete=False), pr(2)))["prs"][0]
        self.assertEqual(row["overlapping_paths_advisory"], [])
        self.assertIn("CHANGED_PATH_INVENTORY_INCOMPLETE", row["unverified_requirements"])

    def test_invalid_traversal_and_absolute_paths_are_refused(self):
        for path in ("../private", "src/../private", "/etc/passwd", "./src/a.py", "src//a.py", "C:\\secrets"):
            with self.subTest(path=path):
                self.hold("unsafe or ambiguous touched path", data(pr(1, touched_paths=[path])))

    def test_duplicate_changed_paths_refused(self):
        self.hold("duplicate entries", data(pr(1, touched_paths=["src/a", "src/a"])))

    def test_duplicate_pr_number_is_refused(self):
        self.hold("duplicate PR number", data(pr(2), pr(2)))

    def test_invalid_head_sha_refused(self):
        self.hold("exact 40-char lowercase SHA", data(pr(1, head_sha="fake")))

    def test_wrong_review_sha_refused(self):
        self.hold("review HEAD", data(pr(1, review={"state": "approved", "head_sha": "a"})))

    def test_malformed_required_app_identity_refused(self):
        d = data()
        d["policy"]["required_checks"][0]["app"] = ""
        self.hold("invalid label", d)

    def test_unknown_policy_fields_refused(self):
        d = data()
        d["policy"]["override_merge_checks"] = True
        self.hold("unexpected fields", d)

    def test_unknown_PR_fields_refused(self):
        d = data()
        d["prs"][0]["close_all_issues"] = True
        self.hold("unexpected fields", d)

    def test_duplicate_check_name_and_app_refused(self):
        p = pr(1)
        p["checks"].append(copy.deepcopy(p["checks"][0]))
        self.hold("duplicate check identity", data(p))

    def test_issue_reference_never_closes_issue(self):
        r = self.result(data(pr(1, issue_refs=[500, 501])))
        self.assertEqual(r["prs"][0]["declared_issue_refs_not_closed"], [500, 501])
        self.assertFalse(r["issues_closed"])

    def test_empty_pr_snapshot_has_no_auto_merge(self):
        d = data()
        d["prs"] = []
        r = self.result(d)
        self.assertEqual(r["plan_order"], [])
        self.assertIsNone(r["first_recheck_candidate"])

    def test_exact_snapshot_time_requires_timezone(self):
        d = data()
        d["observed_at"] = "2026-11-22T21:00:00"
        self.hold("requires timezone", d)

    def test_nonboolean_draft_refused(self):
        self.hold("nonboolean draft", data(pr(1, draft="false")))

    def test_nonboolean_policy_completeness_refused(self):
        d = data()
        d["policy"]["observed_complete"] = 1
        self.hold("nonboolean policy completeness", d)

    def test_normalized_fictional_fixture(self):
        fixture = mod.read_json(ROOT / "examples" / "synthetic-backlog.json")
        r = mod.plan(fixture)
        self.assertEqual(r["plan_order"], [101, 102, 103, 104, 105, 106])
        self.assertEqual(r["first_recheck_candidate"], 101)
        self.assertEqual(r["prs"][1]["state"], "HOLD_RECHECK")
        self.assertEqual(r["prs"][2]["state"], "BLOCKED")
        self.assertEqual(r["prs"][3]["state"], "BLOCKED")
        self.assertEqual(r["prs"][4]["state"], "HOLD_RECHECK")
        self.assertEqual(r["prs"][5]["state"], "HOLD_RECHECK")
        self.assertFalse(r["live_provider_verified"])

    def test_cli_return_zero_for_plan_but_not_merge_authority(self):
        path = ROOT / "examples" / "synthetic-backlog.json"
        p = subprocess.run([sys.executable, str(SCRIPT), "--input", str(path)], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        r = json.loads(p.stdout)
        self.assertFalse(r["merge_performed"])

    def test_cli_require_candidate_exits_three_on_all_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "blocked.json"
            path.write_text(json.dumps(data(pr(1, draft=True))), encoding="utf8")
            p = subprocess.run([sys.executable, str(SCRIPT), "--input", str(path), "--require-candidate"], capture_output=True, text=True)
            self.assertEqual(p.returncode, 3, p.stderr)

    def test_json_duplicate_keys_refused(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "dup.json"
            path.write_text('{"key": 1, "key": 2}', encoding="utf8")
            with self.assertRaisesRegex(mod.Hold, "duplicate JSON key"):
                mod.read_json(path)

    def test_symlinked_input_refused(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "input.json"
            path.write_text(json.dumps(data()), encoding="utf8")
            link = Path(td) / "alias.json"
            try:
                link.symlink_to(path)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable")
            with self.assertRaisesRegex(mod.Hold, "symlinked"):
                mod.read_json(link)

    def test_oversized_input_refused(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "oversize.json"
            path.write_bytes(b"x" * (mod.MAX_BYTES + 1))
            with self.assertRaisesRegex(mod.Hold, "one MiB"):
                mod.read_json(path)

    def test_nonfinite_json_refused(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "nonfinite.json"
            path.write_text('{"n":NaN}', encoding="utf8")
            with self.assertRaisesRegex(mod.Hold, "nonfinite JSON"):
                mod.read_json(path)

    def test_unbounded_prs_refused(self):
        d = data()
        d["prs"] = [pr(n) for n in range(1, 258)]
        self.hold("too many PRs", d)

    def test_integration_after_merge_requires_new_live_snapshot(self):
        row = self.result()["prs"][0]
        self.assertEqual(row["next_required_action"], "FETCH_LIVE_PR_HEAD_RULESETS_CHECKS_REVIEWS_AND_MERGE_QUEUE")
        self.assertIn("After any merge", self.result()["mandatory_follow_up"])


if __name__ == "__main__":
    unittest.main()
