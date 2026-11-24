"""Red-first adversarial tests: preserve user-selected focus and prevent reused-ID false progress.

All data are invented. Tests establish Python contract behavior only, not
diagnosed ADHD needs, measured engagement or authenticated work completion.
"""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "plan.py"
spec = importlib.util.spec_from_file_location("focus_identity_plan", SCRIPT)
planner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planner)


def task(key, **kw):
    out = {"id": key, "label": "Fictional " + key,
           "kind": "action", "state": "todo", "depends_on": [],
           "effort_minutes": 40, "value": 3, "urgency": 0}
    out.update(kw)
    return out


def snap(*items, date="2026-11-24", focus=None, goal=None):
    result = {"schema_version": 1, "as_of": date,
              "scope_id": "fictional-focus", "tasks": list(items)}
    if focus is not None:
        result["focus_task_id"] = focus
    if goal is not None:
        result["goal_id"] = goal
    return result


class TestIdentityReconciliation(unittest.TestCase):
    def test_reused_id_with_changed_label_cannot_be_claimed_completed(self):
        previous = snap(task("write", label="Draft onboarding guide"),
                        date="2026-11-23")
        current = snap(task("write", label="Archive finance documents",
                            state="done"))
        report = planner.compare_snapshots(previous, current)
        self.assertEqual(report["completed_claim_ids"], [])
        self.assertEqual(report["identity_review_ids"], ["write"])
        self.assertEqual(report["state_transition_review_ids"], ["write"])
        self.assertNotIn("Draft onboarding guide", json.dumps(report))
        self.assertNotIn("Archive finance documents", json.dumps(report))

    def test_reused_id_with_changed_kind_cannot_be_claimed_completed(self):
        old = snap(task("finish", label="Finish", kind="action"),
                   date="2026-11-23")
        new = snap(task("finish", label="Finish", kind="milestone",
                        effort_minutes=None, value=None, duration_days=0,
                        state="done"))
        delta = planner.compare_snapshots(old, new)
        self.assertEqual(delta["completed_claim_ids"], [])
        self.assertEqual(delta["identity_review_ids"], ["finish"])
        self.assertEqual(delta["state_transition_review_ids"], ["finish"])

    def test_reused_id_cannot_claim_a_new_ready_action(self):
        old = snap(task("item", label="Review contract",
                        external_blocker=True), date="2026-11-23")
        new = snap(task("item", label="Review public notes",
                        external_blocker=False))
        delta = planner.compare_snapshots(old, new)
        self.assertEqual(delta["newly_ready_ids"], [])
        self.assertEqual(delta["identity_review_ids"], ["item"])

    def test_changed_label_does_not_silently_reuse_resume_candidate(self):
        old = snap(task("write", label="Finish draft", state="doing"),
                   date="2026-11-23")
        new = snap(task("write", label="Pay invoice", state="doing"))
        delta = planner.compare_snapshots(old, new)
        self.assertEqual(delta["resume_candidate_ids"], [])
        self.assertEqual(delta["identity_review_ids"], ["write"])

    def test_stable_id_label_and_kind_preserve_legitimate_claim(self):
        old = snap(task("write"), date="2026-11-23")
        new = snap(task("write", state="done"))
        delta = planner.compare_snapshots(old, new)
        self.assertEqual(delta["completed_claim_ids"], ["write"])
        self.assertEqual(delta["identity_review_ids"], [])
        self.assertEqual(delta["state_transition_review_ids"], [])

    def test_ordinary_estimate_edit_does_not_trigger_identity_review(self):
        old = snap(task("write", effort_minutes=60, value=2),
                   date="2026-11-23")
        new = snap(task("write", effort_minutes=25, value=4))
        delta = planner.compare_snapshots(old, new)
        self.assertEqual(delta["identity_review_ids"], [])
        self.assertEqual(delta["estimate_changed_ids"], ["write"])

    def test_caller_label_change_is_not_automatic_proof_id_reuse(self):
        old = snap(task("write", label="Write page"), date="2026-11-23")
        new = snap(task("write", label="Write page 1"))
        delta = planner.compare_snapshots(old, new)
        self.assertEqual(delta["identity_review_ids"], ["write"])
        self.assertEqual(delta["completion_evidence"],
                         "CALLER_ASSERTED_NOT_AUTHENTICATED")
        self.assertIn("review", delta["identity_notice"].lower())


class TestSelectedFocus(unittest.TestCase):
    def test_explicit_still_ready_focus_wins_near_equivalent_choice(self):
        data = snap(task("alpha"), task("beta"), focus="beta")
        baseline = copy.deepcopy(data)
        baseline.pop("focus_task_id")
        self.assertEqual(planner.plan(baseline)["choices"][0]["task_id"],
                         "alpha")
        out = planner.plan(data)
        self.assertEqual(out["choices"][0]["task_id"], "beta")
        self.assertEqual(out["focus_resolution"], "CONTINUED_ELIGIBLE_SELECTION")
        self.assertIn("PRESERVE_USER_SELECTED_FOCUS",
                      out["choices"][0]["reasons"])
        self.assertEqual(len(out["choices"]), 2)
        self.assertEqual(out["choices"][0]["microstep_status"],
                         "TIMEBOX_NOT_COMPLETION")

    def test_safety_obligation_overrides_optional_focus(self):
        out = planner.plan(snap(
            task("short", value=5, effort_minutes=4),
            task("safety", obligation="safety", value=1,
                 effort_minutes=90), focus="short"))
        self.assertEqual(out["choices"][0]["task_id"], "safety")
        self.assertEqual(out["focus_resolution"], "PROTECTED_PRIORITY_FIRST")

    def test_confirmed_deadline_overrides_optional_focus(self):
        out = planner.plan(snap(
            task("focus", value=5), task(
                "deadline", due_date="2026-11-25",
                deadline_evidence="owner-confirmed", value=1),
            focus="focus"))
        self.assertEqual(out["choices"][0]["task_id"], "deadline")
        self.assertEqual(out["focus_resolution"], "PROTECTED_PRIORITY_FIRST")

    def test_blocked_focus_is_not_given_execution_choice(self):
        out = planner.plan(snap(
            task("focus", external_blocker=True),
            task("other"), focus="focus"))
        self.assertEqual(out["choices"][0]["task_id"], "other")
        self.assertEqual(out["focus_resolution"], "BLOCKED_OR_NOT_ACTIONABLE")
        self.assertIn("focus", [x["task_id"] for x in out["blocked"]])

    def test_done_focus_is_not_recommended_as_new_work(self):
        out = planner.plan(snap(
            task("focus", state="done"), task("other"), focus="focus"))
        self.assertEqual(out["choices"][0]["task_id"], "other")
        self.assertEqual(out["focus_resolution"], "CLAIMED_DONE_NOT_RESUMABLE")

    def test_unavailable_focus_id_is_not_falsely_declared_completed(self):
        out = planner.plan(snap(task("other"), focus="missing-task"))
        self.assertEqual(out["choices"][0]["task_id"], "other")
        self.assertEqual(out["focus_resolution"], "MISSING_FROM_SNAPSHOT")
        self.assertNotIn("missing-task", json.dumps(out))

    def test_unscored_focus_does_not_invent_value_or_skip_evidence(self):
        out = planner.plan(snap(task("focus", value=None),
                                task("other", value=3), focus="focus"))
        self.assertEqual(out["choices"][0]["task_id"], "other")
        self.assertEqual(out["focus_resolution"], "REQUIRES_ESTIMATE_OR_REVIEW")

    def test_far_inferior_focus_is_not_silently_promoted_by_heuristic(self):
        out = planner.plan(snap(
            task("focus", value=1, effort_minutes=300),
            task("high-impact", value=5, effort_minutes=10),
            focus="focus"))
        self.assertEqual(out["choices"][0]["task_id"], "high-impact")
        self.assertEqual(out["focus_resolution"], "MATERIAL_PRIORITY_DIFFERENCE")

    def test_no_focus_input_keeps_original_ranking_unchanged(self):
        out = planner.plan(snap(task("alpha"), task("beta")))
        self.assertEqual(out["choices"][0]["task_id"], "alpha")
        self.assertNotIn("focus_resolution", out)

    def test_one_available_action_is_not_padded_with_fake_alternative(self):
        out = planner.plan(snap(task("only"), focus="only"))
        self.assertEqual([x["task_id"] for x in out["choices"]], ["only"])
        self.assertEqual(out["focus_resolution"], "CONTINUED_ELIGIBLE_SELECTION")

    def test_invalid_focus_token_refused_before_ranking(self):
        for invalid in (True, 123, "", "Customer Name / notes", "../secret"):
            with self.subTest(invalid=invalid):
                doc = snap(task("other"))
                doc["focus_task_id"] = invalid
                with self.assertRaises(planner.Invalid):
                    planner.plan(doc)


if __name__ == "__main__":
    unittest.main()
