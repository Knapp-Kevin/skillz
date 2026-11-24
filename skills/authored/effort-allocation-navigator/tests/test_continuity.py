"""Adversarial repeat-use checks of the optional stateless task comparison.

These cases use fictional user-supplied snapshots. They cannot attest task
completion, host permission, private source identity, or actual human progress.
"""
import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "plan.py"
spec = importlib.util.spec_from_file_location("continuity_plan", SCRIPT)
planner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planner)


def task(key, **kw):
    value = {"id": key, "state": "todo", "kind": "action",
             "depends_on": [], "effort_minutes": 25, "value": 3}
    value.update(kw)
    return value


def snap(*tasks, day="2026-11-23", goal=None):
    return {"schema_version": 1, "as_of": day,
            "scope_id": "fictional-continuity",
            "goal_id": goal, "tasks": list(tasks)}


class TestContinuity(unittest.TestCase):
    def test_completion_is_claim_only_and_dependent_becomes_ready(self):
        before = snap(task("prepare"), task("verify", depends_on=["prepare"]))
        after = snap(task("prepare", state="done"),
                     task("verify", depends_on=["prepare"]), day="2026-11-24")
        delta = planner.compare_snapshots(before, after)
        self.assertEqual(delta["completed_claim_ids"], ["prepare"])
        self.assertEqual(delta["newly_ready_ids"], ["verify"])
        self.assertEqual(delta["completion_evidence"], "CALLER_ASSERTED_NOT_AUTHENTICATED")
        self.assertEqual(planner.plan(after)["choices"][0]["task_id"], "verify")

    def test_removal_is_not_completion_even_if_item_looks_done(self):
        before = snap(task("first"), task("retired"))
        after = snap(task("first"), day="2026-11-24")
        delta = planner.compare_snapshots(before, after)
        self.assertEqual(delta["removed_unreconciled_ids"], ["retired"])
        self.assertEqual(delta["completed_claim_ids"], [])
        self.assertIn("does not prove completion", delta["notice"])

    def test_reopened_task_is_not_a_new_done_claim(self):
        before = snap(task("verify", state="done"), task("next-step"))
        after = snap(task("verify"), task("next-step"), day="2026-11-24")
        delta = planner.compare_snapshots(before, after)
        self.assertEqual(delta["reopened_ids"], ["verify"])
        self.assertEqual(delta["completed_claim_ids"], [])
        self.assertIn("verify", delta["state_changed_ids"])

    def test_dependency_change_can_make_a_task_blocked(self):
        before = snap(task("approve"), task("ship"))
        after = snap(task("approve"), task("ship", depends_on=["approve"]),
                     day="2026-11-24")
        delta = planner.compare_snapshots(before, after)
        self.assertEqual(delta["dependency_changed_ids"], ["ship"])
        self.assertEqual(delta["newly_blocked_ids"], ["ship"])

    def test_external_blocker_release_is_provisional(self):
        before = snap(task("review", external_blocker=True))
        after = snap(task("review", external_blocker=False),
                     day="2026-11-24")
        delta = planner.compare_snapshots(before, after)
        self.assertEqual(delta["blocker_changed_ids"], ["review"])
        self.assertEqual(delta["newly_ready_ids"], ["review"])
        self.assertEqual(delta["source_and_viewer_permission"],
                         "HOST_MUST_VERIFY_BOTH_SNAPSHOTS")

    def test_changed_priority_estimate_and_added_task(self):
        before = snap(task("plan", obligation="discretionary", value=2))
        after = snap(task("plan", obligation="safety", value=4),
                     task("new-task"), day="2026-11-24")
        delta = planner.compare_snapshots(before, after)
        self.assertEqual(delta["priority_changed_ids"], ["plan"])
        self.assertEqual(delta["estimate_changed_ids"], ["plan"])
        self.assertEqual(delta["added_ids"], ["new-task"])
        self.assertEqual(delta["counts"]["added"], 1)

    def test_identical_snapshot_is_not_falsely_progress(self):
        before = snap(task("plan"), task("review"))
        after = copy.deepcopy(before)
        after["as_of"] = "2026-11-24"
        delta = planner.compare_snapshots(before, after)
        self.assertEqual(delta["completed_claim_ids"], [])
        self.assertEqual(delta["state_changed_ids"], [])
        self.assertEqual(delta["removed_unreconciled_ids"], [])
        self.assertEqual(delta["newly_ready_ids"], [])

    def test_same_day_is_not_claimed_source_chronology(self):
        before = snap(task("plan"))
        after = snap(task("plan", state="done"))
        self.assertEqual(planner.compare_snapshots(before, after)["date_order"],
                         "SAME_DAY_CALLER_ORDER_ONLY")

    def test_reversed_date_refused_even_when_progress_looks_good(self):
        before = snap(task("plan"), day="2026-11-24")
        after = snap(task("plan", state="done"), day="2026-11-23")
        with self.assertRaises(planner.Invalid):
            planner.compare_snapshots(before, after)

    def test_goal_change_is_exposed_not_as_milestone_success(self):
        before = snap(task("alpha"), task("old-goal", kind="milestone",
                                         depends_on=["alpha"],
                                         effort_minutes=None, value=None),
                      goal="old-goal")
        after = snap(task("alpha"), task("new-goal", kind="milestone",
                                        depends_on=["alpha"],
                                        effort_minutes=None, value=None),
                     goal="new-goal", day="2026-11-24")
        delta = planner.compare_snapshots(before, after)
        self.assertTrue(delta["goal_changed"])
        self.assertIn("old-goal", delta["removed_unreconciled_ids"])
        self.assertEqual(delta["completed_claim_ids"], [])

    def test_source_labels_and_private_paths_are_not_echoed(self):
        before = snap(task("plan", label="SECRET_OPPORTUNITY_441"))
        after = snap(task("plan", label="ANOTHER_CUSTOMER_908"),
                     day="2026-11-24")
        report = json.dumps(planner.compare_snapshots(before, after))
        self.assertNotIn("SECRET_OPPORTUNITY_441", report)
        self.assertNotIn("ANOTHER_CUSTOMER_908", report)

    def test_both_snapshots_are_independently_validated(self):
        before = snap(task("plan", depends_on=["missing"]))
        after = snap(task("plan"), day="2026-11-24")
        with self.assertRaises(planner.Invalid):
            planner.compare_snapshots(before, after)

    def test_cli_snapshot_pair_is_stateless_and_id_only(self):
        before = snap(task("plan", label="PRIVATE_ACCOUNT_8"))
        after = snap(task("plan", state="done",
                          label="PRIVATE_ACCOUNT_8"), day="2026-11-24")
        with tempfile.TemporaryDirectory() as root:
            p, c = Path(root) / "before.json", Path(root) / "after.json"
            p.write_text(json.dumps(before))
            c.write_text(json.dumps(after))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rc = planner.main(["--input", str(c), "--previous", str(p)])
        self.assertEqual(rc, 0)
        payload = json.loads(out.getvalue())
        self.assertIn("transition", payload)
        self.assertEqual(payload["transition"]["completed_claim_ids"], ["plan"])
        self.assertNotIn("PRIVATE_ACCOUNT_8", out.getvalue())

    def test_default_single_snapshot_has_no_transition_or_side_effect(self):
        current = snap(task("plan"))
        output = planner.plan(current)
        self.assertNotIn("transition", output)
        self.assertEqual(output["choices"][0]["task_id"], "plan")

    def test_rejected_stale_previous_is_not_ignored_by_cli(self):
        before = snap(task("plan"), day="2026-11-24")
        after = snap(task("plan", state="done"), day="2026-11-23")
        with tempfile.TemporaryDirectory() as root:
            p, c = Path(root) / "before.json", Path(root) / "after.json"
            p.write_text(json.dumps(before))
            c.write_text(json.dumps(after))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                rc = planner.main(["--input", str(c), "--previous", str(p)])
        self.assertEqual(rc, 2)
        self.assertEqual(json.loads(out.getvalue())["status"], "INVALID_INPUT")


if __name__ == "__main__":
    unittest.main()
