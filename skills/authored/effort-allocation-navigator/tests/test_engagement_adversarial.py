"""ADHD-supportive, diagnosis-free activation and repeat-use adversarial tests.

These fictional tests challenge deterministic affordances, not clinical
effectiveness, actual user engagement or authenticated task completion.
"""
import copy
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "plan.py"
spec = importlib.util.spec_from_file_location("activation_plan", SCRIPT)
planner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planner)


def item(key, **options):
    out = {"id": key, "kind": "action", "state": "todo",
           "depends_on": [], "effort_minutes": 90, "value": 3,
           "urgency": 0}
    out.update(options)
    return out


def snapshot(*items, day="2026-11-23", scope="fictional-team",
             capacity=30, preferences=None):
    out = {"schema_version": 1, "as_of": day, "scope_id": scope,
           "capacity_minutes": capacity, "tasks": list(items)}
    if preferences is not None:
        out["preferences"] = preferences
    return out


class TestActivationAdversarial(unittest.TestCase):
    def test_default_start_is_small_not_full_25_minute_plan(self):
        outcome = planner.plan(snapshot(item("substantial")))
        action = outcome["choices"][0]
        self.assertEqual(action["first_microstep_minutes"], 5)
        self.assertEqual(action["first_slice_minutes"], 25)
        self.assertEqual(action["microstep_status"], "TIMEBOX_NOT_COMPLETION")

    def test_tiny_available_capacity_is_not_a_rejection(self):
        outcome = planner.plan(snapshot(item("substantial"),
                                        capacity=2))
        action = outcome["choices"][0]
        self.assertEqual(action["first_microstep_minutes"], 2)
        self.assertFalse(action["fits_available_capacity"])
        self.assertEqual(action["first_slice_minutes"], 2)

    def test_private_shorter_start_applies_only_current_run(self):
        data = snapshot(item("focus"),
                        preferences={"start_window_minutes": 3})
        a = planner.plan(data)["choices"][0]
        b = planner.plan(snapshot(item("focus")))["choices"][0]
        self.assertEqual(a["first_microstep_minutes"], 3)
        self.assertEqual(b["first_microstep_minutes"], 5)

    def test_invalid_start_window_is_refused_not_forced(self):
        for value in (0, 1, 11, 99, None, True, 3.5, "5"):
            with self.subTest(value=value):
                with self.assertRaises(planner.Invalid):
                    planner.plan(snapshot(item("focus"),
                                          preferences={"start_window_minutes": value}))

    def test_microstep_never_overstates_short_actual_task(self):
        action = planner.plan(snapshot(item("tiny", effort_minutes=2)))["choices"][0]
        self.assertEqual(action["first_microstep_minutes"], 2)

    def test_safety_lane_survives_low_friction_mode(self):
        output = planner.plan(snapshot(
            item("optional", value=5, effort_minutes=3),
            item("safe", value=1, effort_minutes=120, obligation="safety"),
            preferences={"pace": "short-sprints",
                         "start_window_minutes": 2}))
        self.assertEqual(output["choices"][0]["task_id"], "safe")
        self.assertEqual(output["choices"][0]["first_microstep_minutes"], 2)

    def test_first_step_does_not_fabricate_task_completion(self):
        result = planner.plan(snapshot(item("work", state="doing")))
        row = result["choices"][0]
        self.assertEqual(row["microstep_status"], "TIMEBOX_NOT_COMPLETION")
        self.assertEqual(row["resume_cue"], "PICK_NEXT_VISIBLE_ACTION")
        self.assertNotIn("completion_receipt", row)

    def test_even_two_choices_get_small_start_without_extra_options(self):
        out = planner.plan(snapshot(item("alpha"), item("beta")))
        self.assertEqual(len(out["choices"]), 2)
        self.assertTrue(all(1 <= x["first_microstep_minutes"] <= 5
                            for x in out["choices"]))

    def test_comparison_fails_cross_scope_same_task_ids(self):
        before = snapshot(item("write"), scope="fictional-a")
        after = snapshot(item("write", state="done"), scope="fictional-b",
                         day="2026-11-24")
        with self.assertRaises(planner.Invalid):
            planner.compare_snapshots(before, after)

    def test_comparison_requires_scope_on_both_snapshots(self):
        before = snapshot(item("write"))
        after = snapshot(item("write", state="done"), day="2026-11-24")
        for x, y in (({k: v for k, v in before.items() if k != "scope_id"}, after),
                     (before, {k: v for k, v in after.items() if k != "scope_id"})):
            with self.assertRaises(planner.Invalid):
                planner.compare_snapshots(x, y)

    def test_same_scope_allows_claimed_not_authenticated_progress(self):
        before = snapshot(item("write"))
        after = snapshot(item("write", state="done"), day="2026-11-24")
        delta = planner.compare_snapshots(before, after)
        self.assertEqual(delta["completed_claim_ids"], ["write"])
        self.assertEqual(delta["completion_evidence"],
                         "CALLER_ASSERTED_NOT_AUTHENTICATED")
        self.assertEqual(delta["scope_check"], "CALLER_DECLARED_MATCH_NOT_AUTHENTICATED")

    def test_unchanged_snapshot_cannot_be_called_failed_momentum(self):
        before = snapshot(item("draft", state="doing"))
        after = copy.deepcopy(before)
        after["as_of"] = "2026-11-24"
        delta = planner.compare_snapshots(before, after)
        self.assertEqual(delta["completed_claim_ids"], [])
        self.assertIn("draft", delta["resume_candidate_ids"])
        self.assertNotIn("STALLED", str(delta).upper())
        self.assertNotIn("PROCRASTINATED", str(delta).upper())

    def test_buyer_private_or_medical_fields_not_accepted(self):
        data = snapshot(item("focus"))
        data["diagnosis"] = "private"
        with self.assertRaises(planner.Invalid):
            planner.plan(data)

    def test_snapshot_scope_must_be_low_entropy_id_not_private_text(self):
        data = snapshot(item("focus"), scope="Client Name / confidential")
        with self.assertRaises(planner.Invalid):
            planner.plan(data)


if __name__ == "__main__":
    unittest.main()
