"""Second adversarial pass against the already merged v0.1.0 baseline.

Planted cases are written BEFORE the corresponding refinement. A failure on
the baseline is an observed source-level gap, not independently observed
agent behavior or measured task outcomes. All records are synthetic.
"""
import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "plan.py"
spec = importlib.util.spec_from_file_location("effort_adv2", SCRIPT)
planner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planner)


def task(name, **changes):
    row = {"id": name, "kind": "action", "state": "todo", "depends_on": [],
           "effort_minutes": 30, "value": 3, "urgency": 0}
    row.update(changes)
    return row


def goal(name, dependencies=(), **changes):
    row = {"id": name, "kind": "milestone", "state": "todo",
           "depends_on": list(dependencies), "duration_days": 0}
    row.update(changes)
    return row


def snapshot(*entries, goal_id=None):
    return {"schema_version": 1, "as_of": "2026-11-23",
            "goal_id": goal_id, "tasks": list(entries)}


class SecondAdversarialPass(unittest.TestCase):
    # These cases are intended to break the initial method, then become
    # non-regressing acceptance obligations after a bounded correction.
    def test_external_milestone_blocker_is_representable(self):
        result = planner.plan(snapshot(
            goal("approval", external_blocker=True), goal_id="approval"))
        self.assertEqual(result["mode"], "BLOCKED")
        self.assertEqual(result["blocked"][0]["task_id"], "approval")
        self.assertTrue(result["blocked"][0]["external_blocker"])
        self.assertEqual(result["critical_path"]["status"], "EXTERNAL_DURATION_UNBOUNDED")

    def test_external_milestone_with_ready_predecessor_still_offers_work(self):
        result = planner.plan(snapshot(
            task("prepare"), goal("approval", ["prepare"], external_blocker=True),
            goal_id="approval"))
        self.assertEqual(result["mode"], "EXECUTE")
        self.assertEqual(result["choices"][0]["task_id"], "prepare")
        self.assertEqual(result["critical_path"]["status"], "EXTERNAL_DURATION_UNBOUNDED")

    def test_unexpanded_milestone_is_not_falsely_called_blocked(self):
        result = planner.plan(snapshot(goal("undetailed"), goal_id="undetailed"))
        self.assertEqual(result["mode"], "NEEDS_DECOMPOSITION")
        self.assertEqual(result["blocked"], [])
        self.assertEqual(result["needs_decomposition_ids"], ["undetailed"])
        self.assertEqual(result["choices"][0]["action"], "DEFINE_REQUIRED_NEXT_STEP")

    def test_unexpanded_safety_milestone_needs_decomposition(self):
        result = planner.plan(snapshot(goal("obligation", obligation="safety")))
        self.assertEqual(result["mode"], "NEEDS_DECOMPOSITION")
        self.assertIn("obligation", result["needs_decomposition_ids"])

    def test_positive_milestone_elapsed_duration_not_silently_discarded(self):
        with self.assertRaises(planner.Invalid):
            planner.plan(snapshot(goal("approval", duration_days=5), goal_id="approval"))

    def test_two_urgent_safety_starts_are_not_substitutable(self):
        result = planner.plan(snapshot(
            task("mitigation", obligation="safety", value=5, effort_minutes=20),
            task("audit", obligation="safety", value=3, effort_minutes=30)))
        self.assertEqual(result["choices"][0]["priority_lane"], "MANDATORY_SAFETY")
        self.assertEqual(result["choices"][1]["priority_lane"], "MANDATORY_SAFETY")
        self.assertTrue(result["choices"][1]["requires_deferral_of_primary"])

    def test_two_imminent_deadlines_cannot_replace_each_other(self):
        result = planner.plan(snapshot(
            task("invoice", due_date="2026-11-24",
                 deadline_evidence="owner-confirmed", value=5, effort_minutes=20),
            task("response", due_date="2026-11-25",
                 deadline_evidence="owner-confirmed", value=4, effort_minutes=25)))
        self.assertEqual(result["choices"][0]["priority_lane"], "CONFIRMED_IMMINENT_DEADLINE")
        self.assertEqual(result["choices"][1]["priority_lane"], "CONFIRMED_IMMINENT_DEADLINE")
        self.assertTrue(result["choices"][1]["requires_deferral_of_primary"])

    # Preservation and near-miss cases: no motivation to weaken guards.
    def test_discretionary_alternative_does_not_claim_mandatory_deferral(self):
        result = planner.plan(snapshot(task("alpha"), task("beta")))
        self.assertFalse(result["choices"][1]["requires_deferral_of_primary"])

    def test_external_action_blocker_preserved(self):
        result = planner.plan(snapshot(task("approval-wait", external_blocker=True)))
        self.assertEqual(result["mode"], "BLOCKED")
        self.assertEqual(result["blocked"][0]["task_id"], "approval-wait")

    def test_missing_required_dependency_cannot_be_invented(self):
        with self.assertRaises(planner.Invalid):
            planner.plan(snapshot(goal("approval", ["imaginary"]), goal_id="approval"))

    def test_milestone_zero_elapsed_duration_preserved(self):
        result = planner.plan(snapshot(
            task("prepare", duration_days=3), goal("approval", ["prepare"]),
            goal_id="approval"))
        self.assertEqual(result["critical_path"]["duration_days"], 3)

    def test_done_milestone_with_unfinished_hard_dependency_is_rejected(self):
        with self.assertRaises(planner.Invalid):
            planner.plan(snapshot(task("prepare"),
                goal("approval", ["prepare"], state="done"), goal_id="approval"))

    def test_completed_goal_without_dependencies_is_allowed(self):
        result = planner.plan(snapshot(goal("approval", state="done"), goal_id="approval"))
        self.assertEqual(result["mode"], "COMPLETE")

    def test_off_goal_safety_remains_visible(self):
        result = planner.plan(snapshot(
            task("focus"), goal("focus-goal", ["focus"]),
            task("security", obligation="safety"), goal_id="focus-goal"))
        self.assertEqual(result["choices"][0]["task_id"], "security")
        self.assertIn("security", result["scope_extension_ids"])

    def test_short_sprints_cannot_hide_safety(self):
        project = snapshot(task("audit", obligation="safety",
                                effort_minutes=300, value=1),
                           task("easy", effort_minutes=10, value=5))
        project["preferences"] = {"pace": "short-sprints"}
        self.assertEqual(planner.plan(project)["choices"][0]["task_id"], "audit")

    def test_no_fabricated_alternative_if_one_ready(self):
        result = planner.plan(snapshot(task("prepare"), goal("approval", ["prepare"]),
                                       goal_id="approval"))
        self.assertEqual(len(result["choices"]), 1)

    def test_unverified_deadline_does_not_override_choice(self):
        result = planner.plan(snapshot(
            task("critical", value=5, effort_minutes=10),
            task("claim", due_date="2026-11-23", deadline_evidence="claimed",
                 value=1, effort_minutes=200)))
        self.assertEqual(result["choices"][0]["task_id"], "critical")

    def test_unknown_effort_on_safety_never_treated_as_zero(self):
        result = planner.plan(snapshot(
            task("audit", obligation="safety", effort_minutes=None),
            task("pleasant", value=5, effort_minutes=10)))
        self.assertEqual(result["mode"], "NEEDS_PRIORITY_EVIDENCE")
        self.assertEqual(result["choices"][0]["task_id"], "audit")


    # Refinement follow-up guards for the newly distinguished non-action
    # milestone states, added AFTER the red adversarial evidence.
    def test_all_prerequisites_done_milestone_needs_acceptance(self):
        output = planner.plan(snapshot(
            task("prepare", state="done"), goal("ready", ["prepare"]),
            goal_id="ready"))
        self.assertEqual(output["mode"], "NEEDS_VERIFICATION")
        self.assertEqual(output["choices"][0]["action"],
                         "CONFIRM_MILESTONE_COMPLETION")
        self.assertEqual(output["needs_verification_ids"], ["ready"])

    def test_mandatory_verification_preempts_unrelated_easy_work(self):
        output = planner.plan(snapshot(
            task("prepare", state="done"),
            goal("audit-gate", ["prepare"], obligation="safety"),
            task("optional", effort_minutes=5, value=5)))
        self.assertEqual(output["mode"], "NEEDS_VERIFICATION")
        self.assertEqual(output["choices"][0]["task_id"], "audit-gate")

    def test_mandatory_decomposition_preempts_unrelated_easy_work(self):
        output = planner.plan(snapshot(
            goal("safety-gate", obligation="safety"),
            task("optional", effort_minutes=5, value=5)))
        self.assertEqual(output["mode"], "NEEDS_DECOMPOSITION")
        self.assertEqual(output["choices"][0]["task_id"], "safety-gate")

    def test_optional_milestone_gap_visible_while_work_progresses(self):
        output = planner.plan(snapshot(
            goal("unexpanded"), task("useful", value=4, effort_minutes=20)))
        self.assertEqual(output["mode"], "EXECUTE")
        self.assertEqual(output["choices"][0]["task_id"], "useful")
        self.assertIn("unexpanded", output["needs_decomposition_ids"])

    def test_blocked_external_gate_not_falsely_marked_verified(self):
        output = planner.plan(snapshot(
            task("prepare", state="done"),
            goal("approval", ["prepare"], external_blocker=True),
            goal_id="approval"))
        self.assertEqual(output["mode"], "BLOCKED")
        self.assertNotIn("approval", output["needs_verification_ids"])
        self.assertEqual(output["blocked"][0]["task_id"], "approval")


if __name__ == "__main__":
    unittest.main(verbosity=2)
