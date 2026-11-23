"""Adversarial stage after the v0.1.0 bounded-choice refinement.

This module plants conflicting states, urgency propagation, a tempting
near-clone alternative, and malicious/unknown inputs. It is synthetic
algorithm evidence, not an actual consuming agent/user outcome.
"""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "plan.py"
spec = importlib.util.spec_from_file_location("refinement_plan", SCRIPT)
planner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planner)


def action(name, **kwargs):
    row = {"id": name, "state": "todo", "kind": "action",
           "depends_on": [], "effort_minutes": 45, "value": 3,
           "urgency": 0}
    row.update(kwargs)
    return row


def milestone(name, deps, **kwargs):
    row = {"id": name, "kind": "milestone", "state": "todo",
           "depends_on": deps, "duration_days": 0}
    row.update(kwargs)
    return row


def data(*tasks, goal_id=None, **kwargs):
    result = {"schema_version": 1, "as_of": "2026-11-23",
              "goal_id": goal_id, "tasks": list(tasks)}
    result.update(kwargs)
    return result


class TestRefinementAdversarial(unittest.TestCase):
    def test_done_child_with_undone_parent_refused(self):
        with self.assertRaises(planner.Invalid):
            planner.plan(data(action("source"),
                              action("deliver", state="done", depends_on=["source"])))

    def test_done_milestone_with_unfinished_parent_refused(self):
        with self.assertRaises(planner.Invalid):
            planner.plan(data(action("source"),
                              milestone("goal", ["source"], state="done"),
                              goal_id="goal"))

    def test_outside_goal_invalid_done_still_refused(self):
        with self.assertRaises(planner.Invalid):
            planner.plan(data(action("scoped"),
                              milestone("goal", ["scoped"]),
                              action("elsewhere"),
                              action("forged-done", state="done",
                                     depends_on=["elsewhere"]), goal_id="goal"))

    def test_valid_done_with_completed_dependencies_still_accepted(self):
        result = planner.plan(data(action("source", state="done"),
                                   milestone("goal", ["source"], state="done"),
                                   goal_id="goal"))
        self.assertEqual(result["mode"], "COMPLETE")
        self.assertEqual(result["completion_status"],
                         "CALLER_ASSERTED_NOT_INDEPENDENTLY_VERIFIED")

    def test_deadline_on_goal_prioritizes_its_ready_prerequisite(self):
        project = data(action("mandatory-step", value=1,
                              effort_minutes=120),
                       milestone("goal", ["mandatory-step"],
                                 due_date="2026-11-24",
                                 deadline_evidence="owner-confirmed"),
                       action("pleasant", value=5, effort_minutes=15),
                       goal_id=None)
        output = planner.plan(project)
        self.assertEqual(output["choices"][0]["task_id"], "mandatory-step")
        self.assertIn("UNLOCKS_OWNER_CONFIRMED_DEADLINE",
                      output["choices"][0]["reasons"])
        self.assertEqual(output["choices"][0]["confirmed_deadline_source_id"], "goal")
        self.assertEqual(output["choices"][0]["priority_lane"],
                         "CONFIRMED_IMMINENT_DEADLINE")

    def test_missing_elapsed_days_does_not_suppress_real_deadline(self):
        x = data(action("parent", value=1, duration_days=None),
                 milestone("goal", ["parent"], due_date="2026-11-24",
                           deadline_evidence="owner-confirmed"),
                 goal_id="goal")
        output = planner.plan(x)
        self.assertEqual(output["choices"][0]["priority_lane"],
                         "CONFIRMED_IMMINENT_DEADLINE")
        self.assertEqual(output["critical_path"]["status"], "DURATION_DATA_INCOMPLETE")

    def test_safety_descendant_propagates_hard_lane(self):
        output = planner.plan(data(action("check", value=1, effort_minutes=240),
                                   action("safety-step", obligation="safety",
                                          depends_on=["check"]),
                                   action("bonus", value=5, effort_minutes=15)))
        self.assertEqual(output["choices"][0]["task_id"], "check")
        self.assertEqual(output["choices"][0]["priority_lane"], "MANDATORY_SAFETY")
        self.assertIn("UNLOCKS_DECLARED_SAFETY_OBLIGATION",
                      output["choices"][0]["reasons"])

    def test_off_goal_safety_is_not_hidden_by_focus(self):
        output = planner.plan(data(action("writing", effort_minutes=15, value=5),
                                   milestone("finish", ["writing"]),
                                   action("audit", obligation="safety",
                                          effort_minutes=120, value=1),
                                   goal_id="finish"))
        self.assertEqual(output["choices"][0]["task_id"], "audit")
        self.assertIn("audit", output["scope_extension_ids"])

    def test_off_goal_imminent_deadline_is_not_hidden(self):
        output = planner.plan(data(action("writing", effort_minutes=15),
                                   milestone("finish", ["writing"]),
                                   action("report", due_date="2026-11-24",
                                          deadline_evidence="owner-confirmed",
                                          effort_minutes=120, value=1),
                                   goal_id="finish"))
        self.assertEqual(output["choices"][0]["task_id"], "report")
        self.assertIn("report", output["scope_extension_ids"])

    def test_off_goal_deadline_ancestor_is_included(self):
        output = planner.plan(data(action("writing"),
                                   milestone("finish", ["writing"]),
                                   action("gather", effort_minutes=180,
                                          value=1),
                                   milestone("compliance", ["gather"],
                                             due_date="2026-11-24",
                                             deadline_evidence="owner-confirmed"),
                                   goal_id="finish"))
        self.assertEqual(output["choices"][0]["task_id"], "gather")
        self.assertEqual(output["choices"][0]["confirmed_deadline_source_id"],
                         "compliance")
        self.assertIn("compliance", output["scope_extension_ids"])

    def test_claimed_due_date_not_a_focus_exception(self):
        output = planner.plan(data(action("writing"),
                                   milestone("finish", ["writing"]),
                                   action("claim", due_date="2026-11-23",
                                          deadline_evidence="claimed",
                                          value=5),
                                   goal_id="finish"))
        self.assertEqual(output["scope_extension_ids"], [])
        self.assertEqual(output["choices"][0]["task_id"], "writing")

    def test_optional_off_goal_task_ignored(self):
        output = planner.plan(data(action("writing"),
                                   milestone("finish", ["writing"]),
                                   action("distraction", value=5,
                                          effort_minutes=5), goal_id="finish"))
        self.assertEqual(output["scope_extension_ids"], [])
        self.assertEqual(output["choices"][0]["task_id"], "writing")

    def test_off_goal_blocked_safety_is_visible_not_executable(self):
        output = planner.plan(data(action("writing"),
                                   milestone("finish", ["writing"]),
                                   action("safety", obligation="safety",
                                          external_blocker=True),
                                   goal_id="finish"))
        self.assertIn("safety", output["scope_extension_ids"])
        self.assertIn("safety", [r["task_id"] for r in output["blocked"]])
        self.assertNotIn("safety", [c["task_id"] for c in output["choices"]])

    def test_short_sprints_cannot_downrank_safety_prerequisite(self):
        output = planner.plan(data(action("check", value=1, effort_minutes=240),
                                   action("safety", obligation="safety",
                                          depends_on=["check"]),
                                   action("tiny-win", value=5, effort_minutes=5),
                                   preferences={"pace": "short-sprints"}))
        self.assertEqual(output["choices"][0]["task_id"], "check")

    def test_alternative_in_lower_lane_discloses_deferral(self):
        output = planner.plan(data(action("safety", obligation="safety",
                                          value=1, effort_minutes=120),
                                   action("optional", value=5,
                                          effort_minutes=10)))
        self.assertEqual(output["choices"][0]["priority_lane"], "MANDATORY_SAFETY")
        self.assertEqual(output["choices"][1]["task_id"], "optional")
        self.assertTrue(output["choices"][1]["requires_deferral_of_primary"])

    def test_same_lane_alternative_does_not_claim_mandatory_deferral(self):
        output = planner.plan(data(action("alpha", effort_minutes=30),
                                   action("beta", effort_minutes=60)))
        self.assertFalse(output["choices"][1]["requires_deferral_of_primary"])

    def test_choose_distinct_comparable_strategy_for_second_choice(self):
        output = planner.plan(data(
            action("unlock-a", value=5, urgency=1, effort_minutes=20),
            action("unlock-b", value=5, urgency=1, effort_minutes=25),
            action("quick", value=4, urgency=2, effort_minutes=20),
            action("child-a", depends_on=["unlock-a"]),
            action("child-b", depends_on=["unlock-b"])))
        self.assertEqual(output["choices"][0]["task_id"], "unlock-a")
        self.assertEqual(output["choices"][1]["task_id"], "quick")
        self.assertEqual(output["choices"][0]["strategy"], "UNBLOCK")
        self.assertEqual(output["choices"][1]["strategy"], "SHORT_WIN")

    def test_do_not_promote_terrible_alternative_just_for_novelty(self):
        output = planner.plan(data(
            action("unlock-a", value=5, effort_minutes=15),
            action("unlock-b", value=5, effort_minutes=20),
            action("quick", value=1, effort_minutes=90),
            action("child-a", depends_on=["unlock-a"]),
            action("child-b", depends_on=["unlock-b"])))
        self.assertEqual(output["choices"][1]["task_id"], "unlock-b")

    def test_unknown_effort_on_prerequisite_of_safety_holds_ranking(self):
        output = planner.plan(data(action("assess", effort_minutes=None,
                                          value=1),
                                   action("safety", obligation="safety",
                                          depends_on=["assess"]),
                                   action("nice", effort_minutes=10, value=5)))
        self.assertEqual(output["mode"], "NEEDS_PRIORITY_EVIDENCE")
        self.assertEqual(output["choices"][0]["task_id"], "assess")
        self.assertEqual(output["choices"][0]["action"], "ESTIMATE_OR_CONFIRM")

    def test_unknown_effort_on_prerequisite_of_urgent_deadline_holds(self):
        output = planner.plan(data(action("assess", effort_minutes=None),
                                   milestone("deadline", ["assess"],
                                             due_date="2026-11-24",
                                             deadline_evidence="owner-confirmed"),
                                   action("pleasant", effort_minutes=10,
                                          value=5)))
        self.assertEqual(output["mode"], "NEEDS_PRIORITY_EVIDENCE")
        self.assertEqual(output["choices"][0]["task_id"], "assess")

    def test_no_mandatory_outside_scope_is_added_if_already_done(self):
        output = planner.plan(data(action("writing"),
                                   milestone("finish", ["writing"]),
                                   action("past-safety", state="done",
                                          obligation="safety"),
                                   goal_id="finish"))
        self.assertEqual(output["scope_extension_ids"], [])

    def test_unhashable_state_is_refused_with_contract_error(self):
        with self.assertRaises(planner.Invalid):
            planner.plan(data(action("a", state=["todo"])))

    def test_unhashable_kind_is_refused_with_contract_error(self):
        with self.assertRaises(planner.Invalid):
            planner.plan(data(action("a", kind=["milestone"])))

    def test_unhashable_obligation_is_refused_with_contract_error(self):
        with self.assertRaises(planner.Invalid):
            planner.plan(data(action("a", obligation={"bypass": True})))

    def test_unhashable_pace_is_refused_with_contract_error(self):
        with self.assertRaises(planner.Invalid):
            planner.plan(data(action("a"), preferences={"pace": ["short-sprints"]}))

    def test_heuristic_score_not_displayed_with_fake_precision(self):
        output = planner.plan(data(action("example", effort_minutes=33)))
        score = output["choices"][0]["score"]
        self.assertEqual(score, round(score, 1))

    def test_no_labels_leave_private_source(self):
        output = planner.plan(data(action("secret-id", label="PRIVATE USER DATA",
                                          value=5, effort_minutes=15)))
        self.assertNotIn("PRIVATE USER DATA", json.dumps(output))
        self.assertIn("secret-id", output["choices"][0]["task_id"])

    def test_permutations_do_not_bias_equal_scores_by_input_order(self):
        tasks = [action("zed"), action("alpha"), action("middle")]
        first = planner.plan(data(*tasks))
        second = planner.plan(data(*reversed(tasks)))
        self.assertEqual(first, second)

    def test_critical_path_goes_with_focus_goal_not_external_override(self):
        output = planner.plan(data(action("a", duration_days=2),
                                   milestone("focus", ["a"]),
                                   action("safety", obligation="safety",
                                          duration_days=30),
                                   goal_id="focus"))
        self.assertEqual(output["critical_path"]["duration_days"], 2)
        self.assertEqual(output["critical_path"]["path"], ["a", "focus"])
        self.assertIn("safety", output["scope_extension_ids"])

    def test_unknown_downstream_deadline_is_not_invented(self):
        output = planner.plan(data(action("a"), milestone("goal", ["a"],
                                                       due_date="2026-11-23",
                                                       deadline_evidence="claimed"),
                                   goal_id="goal"))
        self.assertEqual(output["choices"][0]["priority_lane"], "DISCRETIONARY")
        self.assertIsNone(output["choices"][0]["confirmed_deadline_source_id"])

    def test_approved_three_choice_setting_not_silently_reset(self):
        output = planner.plan(data(action("first"), action("second"),
                                   action("third"), preferences={"choice_count": 3}))
        self.assertEqual(len(output["choices"]), 3)

    def test_only_one_ready_still_has_no_fabricated_alternative(self):
        output = planner.plan(data(action("first"),
                                   action("waiting", depends_on=["first"])))
        self.assertEqual(len(output["choices"]), 1)

    def test_urgent_deadline_on_blocked_child_requires_real_prerequisite(self):
        output = planner.plan(data(action("prep", value=1, effort_minutes=60),
                                   action("blocked", value=5,
                                          depends_on=["prep"],
                                          due_date="2026-11-24",
                                          deadline_evidence="owner-confirmed"),
                                   action("other", value=5, effort_minutes=15)))
        self.assertEqual(output["choices"][0]["task_id"], "prep")
        self.assertIn("blocked", [x["task_id"] for x in output["blocked"])

    def test_older_completed_task_with_future_due_no_extra_focus(self):
        output = planner.plan(data(action("focus"),
                                   milestone("goal", ["focus"]),
                                   action("done-date", state="done",
                                          due_date="2026-11-24",
                                          deadline_evidence="owner-confirmed"),
                                   goal_id="goal"))
        self.assertEqual(output["scope_extension_ids"], [])

    def test_reordering_no_safety_bypass_for_long_prerequisite(self):
        x = data(action("long", effort_minutes=600, value=1),
                 action("finish-safe", obligation="safety",
                        depends_on=["long"]),
                 action("easy", effort_minutes=15, value=5),
                 preferences={"pace": "short-sprints"})
        one = planner.plan(x)["choices"][0]["task_id"]
        x["tasks"] = list(reversed(x["tasks"]))
        two = planner.plan(x)["choices"][0]["task_id"]
        self.assertEqual(one, two)
        self.assertEqual(two, "long")

    def test_all_output_remains_sanitized_enum_and_identifiers(self):
        output = planner.plan(data(action("one", label="API key is imaginary",
                                          effort_minutes=60, value=4),
                                   action("two", label="Confidential email",
                                          effort_minutes=10, value=2)))
        flat = json.dumps(output)
        for phrase in ("API key is imaginary", "Confidential email"):
            self.assertNotIn(phrase, flat)


if __name__ == "__main__":
    unittest.main(verbosity=2)
