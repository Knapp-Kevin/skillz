"""Portable, offline adversarial checkpoint transition tests.

These exercise a deterministic verifier over fabricated state. They do not
constitute a consuming-agent behavioral trial or authenticated host result.
"""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "scripts" / "check_transition.py"
spec = importlib.util.spec_from_file_location("check_transition", SRC)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

REV = "a" * 40
NEXT = "b" * 40


def before():
    return {
        "schema_version": 1, "workstream_id": "synthetic-repo-work",
        "revision": 1, "objective": "Complete a fictional authorized repair",
        "source_revision": REV, "permission_scope": ["read_only"],
        "guardrails": [
            {"id": "required-checks", "text": "Do not remove required checks"},
            {"id": "owner-merge", "text": "No merge without owner authority"},
        ],
        "decisions": [
            {"id": "design-choice", "text": "Keep the exact source-bound checker",
             "authority_ref": "fictional-owner-decision"},
        ],
        "obligations": [
            {"id": "source-verified", "criterion": "Verify exact source checkout",
             "acceptance_kind": "local_test", "state": "completed",
             "proof": {"kind": "local_test", "ref": "fictional-local-check",
                       "source_revision": REV}},
            {"id": "host-qualified", "criterion": "Run hosted verification",
             "acceptance_kind": "host_receipt", "state": "remaining",
             "proof": None},
        ],
        "next_action": "host-qualified", "claimed_complete": False,
        "context_gap": False,
    }


def after():
    result = copy.deepcopy(before())
    result["revision"] = 2
    result["obligations"][1]["state"] = "current"
    return result


def transition():
    return {"change_type": "continue", "change_ref": None}


def complete(snapshot):
    snapshot["obligations"][1]["state"] = "completed"
    snapshot["obligations"][1]["proof"] = {
        "kind": "host_receipt", "ref": "fictional-host-run",
        "source_revision": snapshot["source_revision"],
    }
    snapshot["next_action"] = None
    snapshot["claimed_complete"] = True
    return snapshot


class TransitionTests(unittest.TestCase):
    def check(self, old=None, new=None, route=None):
        return mod.reconcile(before() if old is None else old,
                             after() if new is None else new,
                             transition() if route is None else route)

    def refuse(self, code, old=None, new=None, route=None):
        with self.assertRaisesRegex(mod.Hold, code):
            self.check(old, new, route)

    def test_continuation_with_open_host_verification_passes_structurally(self):
        result = self.check()
        self.assertEqual(result["status"], "STATIC_TRANSITION_RECONCILED")
        self.assertEqual(result["changed_obligation_ids"], ["host-qualified"])
        self.assertEqual(result["carried_obligations"], 2)
        self.assertFalse(result["source_and_proofs_authenticated"])
        self.assertFalse(result["model_agent_behavior_observed"])
        self.assertFalse(result["automatic_side_effect_authorized"])

    def test_declared_complete_is_not_production_completion_proof(self):
        result = self.check(new=complete(after()))
        self.assertEqual(result["status"], "STATIC_TRANSITION_RECONCILED")
        self.assertTrue(result["claimed_complete"])
        self.assertFalse(result["host_test_execution_verified"])
        self.assertFalse(result["provider_or_merge_outcome_verified"])

    def test_open_pr_or_unrun_host_verifier_cannot_claim_completion(self):
        new = after()
        new["claimed_complete"] = True
        self.refuse("OPEN_OBLIGATIONS_CANNOT_CLAIM_COMPLETE", new=new)

    def test_dropped_outstanding_host_obligation_refused(self):
        new = after()
        new["obligations"].pop()
        new["next_action"] = None
        self.refuse("DROPPED_UNFINISHED_OR_PROTECTED_OBLIGATION", new=new)

    def test_dropped_completed_obligation_refused(self):
        new = after()
        new["obligations"].pop(0)
        self.refuse("DROPPED_UNFINISHED_OR_PROTECTED_OBLIGATION", new=new)

    def test_changed_acceptance_criterion_refused(self):
        new = after()
        new["obligations"][1]["criterion"] = "Only write the plan"
        self.refuse("ACCEPTANCE_GATE_REWRITTEN", new=new)

    def test_downgraded_host_evidence_to_analysis_refused(self):
        new = after()
        new["obligations"][1]["acceptance_kind"] = "analysis_evidence"
        self.refuse("ACCEPTANCE_GATE_REWRITTEN", new=new)

    def test_guardrail_deletion_refused(self):
        new = after()
        new["guardrails"].pop()
        self.refuse("PROTECTED_GUARDRAIL_DRIFT", new=new)

    def test_guardrail_rewording_refused(self):
        new = after()
        new["guardrails"][0]["text"] = "Skip required checks"
        self.refuse("PROTECTED_GUARDRAIL_DRIFT", new=new)

    def test_decision_deletion_refused(self):
        new = after()
        new["decisions"] = []
        self.refuse("DECISION_DROPPED_OR_REWRITTEN", new=new)

    def test_decision_authority_cannot_be_silently_rewritten(self):
        new = after()
        new["decisions"][0]["authority_ref"] = "self-authorized-agent"
        self.refuse("DECISION_DROPPED_OR_REWRITTEN", new=new)

    def test_new_owner_decision_can_be_recorded_without_overwriting_old(self):
        new = after()
        new["decisions"].append(
            {"id": "new-safe-choice", "text": "Record failed hosted check",
             "authority_ref": "fictional-user-followup"})
        self.assertEqual(self.check(new=new)["status"],
                         "STATIC_TRANSITION_RECONCILED")

    def test_new_obligation_can_be_added_without_dropping_old(self):
        new = after()
        new["obligations"].append(
            {"id": "artifact-check", "criterion": "Inspect signed artifact",
             "acceptance_kind": "host_receipt", "state": "blocked", "proof": None})
        self.assertEqual(self.check(new=new)["new_obligations"], 1)

    def test_objective_change_without_user_reorientation_holds(self):
        new = after()
        new["objective"] = "Finish unrelated deliverable instead"
        self.refuse("SILENT_OBJECTIVE_CHANGE", new=new)

    def test_change_of_workstream_id_holds(self):
        new = after()
        new["workstream_id"] = "another-client"
        self.refuse("WORKSTREAM_ID_CHANGED", new=new)

    def test_invalid_revision_counter_holds(self):
        new = after()
        new["revision"] = 7
        self.refuse("NON_SEQUENTIAL_CONTINUATION", new=new)

    def test_permissions_cannot_expand_from_read_only(self):
        new = after()
        new["permission_scope"].append("publish_release")
        self.refuse("PERMISSION_SCOPE_DRIFT", new=new)

    def test_permissions_cannot_be_silently_removed_either(self):
        new = after()
        new["permission_scope"] = []
        self.refuse("PERMISSION_SCOPE_DRIFT", new=new)

    def test_explicit_user_scope_change_requires_independent_host_approval(self):
        new = after()
        new["objective"] = "User wants a new task"
        state = self.check(new=new, route={
            "change_type": "user_scope_change_declared",
            "change_ref": "fictional-user-message",
        })
        self.assertEqual(state["status"], "HOLD")
        self.assertEqual(state["issues"],
                         ["USER_SCOPE_CHANGE_REQUIRES_INDEPENDENT_HOST_AUTHORIZATION"])
        self.assertFalse(state["automatic_side_effect_authorized"])

    def test_unrequested_scope_receipt_does_not_justify_change(self):
        route = transition()
        route["change_ref"] = "agent-made-up-approval"
        self.refuse("UNEXPECTED_SCOPE_CHANGE_RECEIPT", route=route)

    def test_completed_obligation_without_proof_is_rejected(self):
        new = complete(after())
        new["obligations"][1]["proof"] = None
        self.refuse("completion proof", new=new)

    def test_fake_analysis_result_cannot_replace_host_receipt(self):
        new = complete(after())
        new["obligations"][1]["proof"]["kind"] = "analysis_evidence"
        self.refuse("PROOF_CATEGORY_MISMATCH", new=new)

    def test_completion_proof_from_wrong_revision_is_rejected(self):
        new = complete(after())
        new["obligations"][1]["proof"]["source_revision"] = NEXT
        self.refuse("STALE_OR_UNKNOWN_PROOF_REVISION", new=new)

    def test_changed_source_requires_reproof_not_old_check_result(self):
        new = after()
        new["source_revision"] = NEXT
        self.refuse("STALE_OR_UNKNOWN_PROOF_REVISION", new=new)

    def test_changed_source_with_new_receipts_is_structurally_accepted(self):
        new = after()
        new["source_revision"] = NEXT
        new["obligations"][0]["proof"]["source_revision"] = NEXT
        result = self.check(new=new)
        self.assertEqual(result["status"], "STATIC_TRANSITION_RECONCILED")
        self.assertFalse(result["source_and_proofs_authenticated"])

    def test_reopening_completed_check_requires_reason(self):
        new = after()
        new["obligations"][0]["state"] = "remaining"
        new["obligations"][0]["proof"] = None
        self.refuse("REOPENED_WITHOUT_REASON", new=new)

    def test_reopening_completed_check_with_reason_is_accepted(self):
        new = after()
        new["obligations"][0]["state"] = "remaining"
        new["obligations"][0]["proof"] = None
        new["obligations"][0]["reopened_reason"] = "Fictional regression detected"
        self.assertEqual(self.check(new=new)["status"],
                         "STATIC_TRANSITION_RECONCILED")

    def test_unblocking_without_evidence_is_rejected(self):
        old = before()
        old["obligations"][1]["state"] = "blocked"
        old["next_action"] = None
        new = after()
        self.refuse("UNBLOCKED_WITHOUT_EVIDENCE", old=old, new=new)

    def test_unblocking_with_explicit_reference_is_accepted(self):
        old = before()
        old["obligations"][1]["state"] = "blocked"
        old["next_action"] = None
        new = after()
        new["obligations"][1]["unblocked_ref"] = "fictional-permission-receipt"
        self.assertEqual(self.check(old, new)["status"],
                         "STATIC_TRANSITION_RECONCILED")

    def test_next_action_must_be_executable_not_blocked(self):
        new = after()
        new["obligations"][1]["state"] = "blocked"
        self.refuse("NEXT_ACTION_NOT_EXECUTABLE", new=new)

    def test_all_blocked_has_no_executable_next_step(self):
        new = after()
        new["obligations"][1]["state"] = "blocked"
        new["next_action"] = None
        self.assertEqual(self.check(new=new)["status"],
                         "STATIC_TRANSITION_RECONCILED")

    def test_pending_work_cannot_omit_next_action(self):
        new = after()
        new["next_action"] = None
        self.refuse("EXECUTABLE_OBLIGATION_WITHOUT_NEXT_ACTION", new=new)

    def test_finished_work_cannot_retain_open_next_action(self):
        new = complete(after())
        new["next_action"] = "host-qualified"
        self.refuse("COMPLETED_TASK_HAS_PENDING_NEXT_ACTION", new=new)

    def test_context_gap_cannot_claim_finished_task(self):
        new = complete(after())
        new["context_gap"] = True
        self.refuse("CONTEXT_GAP_CANNOT_CLAIM_COMPLETE", new=new)

    def test_unknown_source_cannot_claim_technical_proof(self):
        new = after()
        new["source_revision"] = "UNKNOWN"
        self.refuse("STALE_OR_UNKNOWN_PROOF_REVISION", new=new)

    def test_duplicate_guards_decisions_and_obligations_are_refused(self):
        for collection in ("guardrails", "decisions", "obligations"):
            with self.subTest(collection=collection):
                new = after()
                new[collection].append(copy.deepcopy(new[collection][0]))
                self.refuse("duplicated", new=new)

    def test_unknown_fields_are_rejected(self):
        new = after()
        new["automatic_posting_allowed"] = True
        self.refuse("unexpected fields", new=new)

    def test_false_boolean_fields_cannot_be_strings(self):
        new = after()
        new["claimed_complete"] = "true"
        self.refuse("boolean completion", new=new)

    def test_domain_specific_synthetic_hazards_stay_present(self):
        scenarios = (
            ("CI", "Do not drop native/security CI check", "Host gates must pass"),
            ("README", "Preserve generated README block", "Rendered navigation accepted"),
            ("Delivery", "Keep original release evidence", "Merged implementation verified"),
            ("Refinement", "Preserve adversarial falsifier", "Improved outcome measured"),
        )
        for name, guard, criterion in scenarios:
            with self.subTest(domain=name):
                old = before()
                old["guardrails"][0]["text"] = guard
                old["obligations"][1]["criterion"] = criterion
                new = copy.deepcopy(old)
                new["revision"] = 2
                new["obligations"][1]["state"] = "current"
                self.assertEqual(self.check(old, new)["status"],
                                 "STATIC_TRANSITION_RECONCILED")
                bad = copy.deepcopy(new)
                bad["guardrails"] = bad["guardrails"][1:]
                self.refuse("PROTECTED_GUARDRAIL_DRIFT", old=old, new=bad)

    def test_cli_pass_and_planted_failure_and_no_network(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            for name, obj in (
                ("previous.json", before()),
                ("updated.json", after()),
                ("transition.json", transition()),
            ):
                (d / name).write_text(json.dumps(obj), encoding="utf-8")
            cmd = [sys.executable, str(SRC), "--previous", str(d / "previous.json"),
                   "--updated", str(d / "updated.json"),
                   "--transition", str(d / "transition.json"), "--require-pass"]
            good = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(good.returncode, 0, good.stderr)
            result = json.loads(good.stdout)
            self.assertEqual(result["status"], "STATIC_TRANSITION_RECONCILED")
            self.assertFalse(result["user_authorization_authenticated"])
            bad = after()
            bad["guardrails"] = []
            (d / "updated.json").write_text(json.dumps(bad), encoding="utf-8")
            failure = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(failure.returncode, 2)
            self.assertIn("CONTINUATION_HOLD", failure.stderr)

    def test_cli_declared_scope_change_exits_3_if_pass_required(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            for name, obj in (
                ("previous.json", before()),
                ("updated.json", after()),
                ("transition.json", {
                    "change_type": "user_scope_change_declared",
                    "change_ref": "fictional-user-message",
                }),
            ):
                (d / name).write_text(json.dumps(obj), encoding="utf-8")
            p = subprocess.run(
                [sys.executable, str(SRC), "--previous", str(d / "previous.json"),
                 "--updated", str(d / "updated.json"),
                 "--transition", str(d / "transition.json"), "--require-pass"],
                capture_output=True, text=True)
            self.assertEqual(p.returncode, 3, p.stderr)
            self.assertEqual(json.loads(p.stdout)["status"], "HOLD")

    def test_duplicate_json_keys_cannot_shadow_old_guardrails(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "duplicate.json"
            p.write_text('{"scope":1,"scope":2}', encoding="utf8")
            with self.assertRaisesRegex(mod.Hold, "duplicate JSON key"):
                mod.read_json(str(p))

    def test_symlinked_json_input_is_refused(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            target = root / "actual.json"
            target.write_text(json.dumps(before()), encoding="utf-8")
            link = root / "alias.json"
            try:
                link.symlink_to(target)
            except (OSError, NotImplementedError):
                self.skipTest("No symlink permission")
            with self.assertRaisesRegex(mod.Hold, "symlinked"):
                mod.read_json(str(link))

    def test_oversized_json_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "oversized.json"
            path.write_bytes(b"x" * (mod.MAX_BYTES + 1))
            with self.assertRaisesRegex(mod.Hold, "too large"):
                mod.read_json(str(path))



def chain_fixture():
    first = before()
    second = after()
    third = copy.deepcopy(second)
    third["revision"] = 3
    return {
        "schema_version": 1,
        "checkpoints": [first, second, third],
        "transitions": [transition(), transition()],
    }


class MultiTurnChainTests(unittest.TestCase):
    def test_three_turn_valid_chain_replays_every_step(self):
        result = mod.reconcile_chain(chain_fixture())
        self.assertEqual(result["status"], "STATIC_CHAIN_RECONCILED")
        self.assertEqual(result["qualified_steps"], 2)
        self.assertEqual(result["first_revision"], 1)
        self.assertEqual(result["last_revision"], 3)
        self.assertEqual(result["last_next_action"], "host-qualified")
        self.assertFalse(result["model_agent_behavior_observed"])
        self.assertFalse(result["source_and_proofs_authenticated"])
        self.assertFalse(result["automatic_side_effect_authorized"])

    def test_more_than_two_steps_with_new_blocked_obligation_can_pass(self):
        data = chain_fixture()
        item = {"id": "new-regression", "criterion": "Check fictional guard",
                "acceptance_kind": "local_test", "state": "blocked", "proof": None}
        data["checkpoints"][1]["obligations"].append(copy.deepcopy(item))
        data["checkpoints"][2]["obligations"].append(copy.deepcopy(item))
        result = mod.reconcile_chain(data)
        self.assertEqual(result["status"], "STATIC_CHAIN_RECONCILED")

    def test_missing_guardrail_in_middle_is_not_laundered_by_restoration(self):
        data = chain_fixture()
        data["checkpoints"][1]["guardrails"].pop()
        with self.assertRaisesRegex(mod.Hold,
                                    "CHAIN_STEP_1: PROTECTED_GUARDRAIL_DRIFT"):
            mod.reconcile_chain(data)

    def test_missing_obligation_in_middle_is_not_laundered_by_restoration(self):
        data = chain_fixture()
        data["checkpoints"][1]["obligations"].pop()
        data["checkpoints"][1]["next_action"] = None
        with self.assertRaisesRegex(mod.Hold,
                                    "CHAIN_STEP_1: DROPPED_UNFINISHED"):
            mod.reconcile_chain(data)

    def test_rewritten_acceptance_in_middle_cannot_be_restored_silently(self):
        data = chain_fixture()
        data["checkpoints"][1]["obligations"][1]["criterion"] = "Only draft a plan"
        with self.assertRaisesRegex(mod.Hold,
                                    "CHAIN_STEP_1: ACCEPTANCE_GATE_REWRITTEN"):
            mod.reconcile_chain(data)

    def test_dropped_decision_in_middle_detected_even_if_restored(self):
        data = chain_fixture()
        data["checkpoints"][1]["decisions"] = []
        with self.assertRaisesRegex(mod.Hold,
                                    "CHAIN_STEP_1: DECISION_DROPPED"):
            mod.reconcile_chain(data)

    def test_unauthorized_privilege_expansion_midchain_refused(self):
        data = chain_fixture()
        data["checkpoints"][1]["permission_scope"] = ["read_only", "release_publish"]
        with self.assertRaisesRegex(mod.Hold,
                                    "CHAIN_STEP_1: PERMISSION_SCOPE_DRIFT"):
            mod.reconcile_chain(data)

    def test_second_turn_revision_jump_identifies_exact_failing_transition(self):
        data = chain_fixture()
        data["checkpoints"][2]["revision"] = 100
        with self.assertRaisesRegex(mod.Hold,
                                    "CHAIN_STEP_2: NON_SEQUENTIAL_CONTINUATION"):
            mod.reconcile_chain(data)

    def test_second_turn_workstream_swap_is_refused(self):
        data = chain_fixture()
        data["checkpoints"][2]["workstream_id"] = "another-fictional-team"
        with self.assertRaisesRegex(mod.Hold,
                                    "CHAIN_STEP_2: WORKSTREAM_ID_CHANGED"):
            mod.reconcile_chain(data)

    def test_middle_source_change_requires_revalidation_immediately(self):
        data = chain_fixture()
        data["checkpoints"][1]["source_revision"] = NEXT
        with self.assertRaisesRegex(mod.Hold,
                                    "CHAIN_STEP_1: STALE_OR_UNKNOWN_PROOF_REVISION"):
            mod.reconcile_chain(data)

    def test_middle_fake_completion_is_held_not_reported_success(self):
        data = chain_fixture()
        data["checkpoints"][1]["claimed_complete"] = True
        with self.assertRaisesRegex(mod.Hold,
                                    "CHAIN_STEP_1: OPEN_OBLIGATIONS_CANNOT_CLAIM_COMPLETE"):
            mod.reconcile_chain(data)

    def test_explicit_scope_change_ends_replay_without_looking_past_hold(self):
        data = chain_fixture()
        data["transitions"][0] = {
            "change_type": "user_scope_change_declared",
            "change_ref": "fictional-new-owner-message"}
        data["checkpoints"][1]["objective"] = "New fictional task"
        result = mod.reconcile_chain(data)
        self.assertEqual(result["status"], "HOLD")
        self.assertEqual(result["held_step"], 1)
        self.assertEqual(result["qualified_steps"], 0)
        self.assertEqual(result["unexamined_steps"], 1)
        self.assertFalse(result["user_authorization_authenticated"])

    def test_scope_change_on_last_transition_reports_prior_qualification_only(self):
        data = chain_fixture()
        data["transitions"][1] = {
            "change_type": "user_scope_change_declared",
            "change_ref": "fictional-change-request"}
        data["checkpoints"][2]["objective"] = "Changed assignment"
        result = mod.reconcile_chain(data)
        self.assertEqual(result["status"], "HOLD")
        self.assertEqual(result["held_step"], 2)
        self.assertEqual(result["qualified_steps"], 1)
        self.assertEqual(result["unexamined_steps"], 0)

    def test_route_count_cannot_hide_a_middle_transition(self):
        data = chain_fixture()
        data["transitions"].pop()
        with self.assertRaisesRegex(mod.Hold, "CHAIN_ROUTE_COUNT_MISMATCH"):
            mod.reconcile_chain(data)

    def test_chain_rejects_empty_singleton_and_33_checkpoints(self):
        for count in (0, 1, 33):
            with self.subTest(count=count):
                data = {"schema_version": 1,
                        "checkpoints": [before()] * count,
                        "transitions": [transition()] * max(0, count - 1)}
                with self.assertRaisesRegex(mod.Hold, "CHAIN_LENGTH_OUT_OF_BOUNDS"):
                    mod.reconcile_chain(data)

    def test_chain_rejects_unrecognized_version_and_extra_fields(self):
        for change, marker in (
                ({"schema_version": 2}, "unsupported chain schema"),
                ({"agent_has_authority": True}, "unexpected fields")):
            with self.subTest(change=change):
                data = chain_fixture()
                data.update(change)
                with self.assertRaisesRegex(mod.Hold, marker):
                    mod.reconcile_chain(data)

    def test_chain_requires_actual_sequence_not_only_passing_endpoints(self):
        data = chain_fixture()
        data["checkpoints"][1]["revision"] = 99
        # Caller can provide a clean final checkpoint: the replay still
        # fails on the bad middle checkpoint's true turn number.
        with self.assertRaisesRegex(mod.Hold,
                                    "CHAIN_STEP_1: NON_SEQUENTIAL_CONTINUATION"):
            mod.reconcile_chain(data)

    def test_chain_rejects_non_dict_snapshot_without_model_execution(self):
        data = chain_fixture()
        data["checkpoints"][1] = "an agent claimed this was fine"
        with self.assertRaisesRegex(mod.Hold, "CHAIN_STEP_1: checkpoint"):
            mod.reconcile_chain(data)

    def test_chain_cli_accepts_valid_bundle_and_rejects_unsafe_middle(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "chain.json"
            data = chain_fixture()
            p.write_text(json.dumps(data), encoding="utf8")
            cmd = [sys.executable, str(SRC), "--chain", str(p), "--require-pass"]
            success = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(success.returncode, 0, success.stderr)
            self.assertEqual(json.loads(success.stdout)["qualified_steps"], 2)
            data["checkpoints"][1]["guardrails"].pop()
            p.write_text(json.dumps(data), encoding="utf8")
            failure = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(failure.returncode, 2)
            self.assertIn("CHAIN_STEP_1: PROTECTED_GUARDRAIL_DRIFT",
                          failure.stderr)

    def test_chain_cli_scope_change_holds_and_exits_3(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "chain.json"
            data = chain_fixture()
            data["transitions"][1] = {"change_type": "user_scope_change_declared",
                                      "change_ref": "fictional-message"}
            p.write_text(json.dumps(data), encoding="utf8")
            cmd = [sys.executable, str(SRC), "--chain", str(p), "--require-pass"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(result.returncode, 3, result.stderr)
            self.assertEqual(json.loads(result.stdout)["status"], "HOLD")

    def test_old_cli_triplet_cannot_be_mixed_with_chain(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "chain.json"
            p.write_text(json.dumps(chain_fixture()), encoding="utf8")
            cmd = [sys.executable, str(SRC), "--chain", str(p),
                   "--previous", str(p)]
            result = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn("either --chain or all", result.stderr)

    def test_old_cli_triplet_remains_optional_but_complete(self):
        result = subprocess.run([sys.executable, str(SRC), "--updated", "test.json"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn("either --chain or all", result.stderr)

if __name__ == "__main__":
    unittest.main()
