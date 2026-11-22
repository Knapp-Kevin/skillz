"""Adversarial Python cases for observed-only policy laboratory (synthetic)."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO

import policy_lab as lab
import replay
from test_replay import BLOB, STATE, EVALUATOR, CONTEXT, node, with_receipt

FAMILIES = ("schema-compatibility", "path-isolation")


def case(suffix, split, family, *, gain=True, proposal_attack=False):
    root = node("n-root", None, kind="proposal", action="inspect")
    base = node("n-safe", "n-root", action="preservation-check",
                outcome="OBSERVED_PASS")
    probe = node("n-attack", "n-root",
                 kind="proposal" if proposal_attack else "observation",
                 action="adversarial-probe",
                 outcome="OBSERVED_FAIL" if gain else "OBSERVED_PASS")
    finish = node("n-check", "n-attack", action="preservation-check",
                  outcome="OBSERVED_PASS")
    nodes = [root, base, probe, finish]
    for item in nodes:
        item["task_family"] = family
    receipts = [with_receipt(base)]
    if not proposal_attack:
        receipts.append(with_receipt(probe))
    receipts.append(with_receipt(finish))
    trace = {"schema_version": 1, "experiment_id": "experiment-" + suffix,
             "evaluator_id": EVALUATOR, "evaluation_context_id": CONTEXT,
             "nodes": nodes, "receipts": receipts}
    return {"case_id": "case-" + suffix, "split": split, "task_family": family,
            "source": BLOB, "state": STATE,
            "required_actions": ["preservation-check"], "trace": trace}


def manifest():
    return {
        "schema_version": 1, "evaluator_id": EVALUATOR,
        "evaluator_sha256": "sha256:" + "e" * 64,
        "evaluation_context_id": CONTEXT, "budget": 3,
        "candidate": {
            "schema_version": 1, "policy_id": "adversarial-v1",
            "branch_priority": "adversarial-first",
            "verify_lane": "preservation-check",
            "max_attempts": 2, "stop_on": "recorded-blocked",
        },
        "cases": [
            case("dev-schema", "development", FAMILIES[0]),
            case("dev-path", "development", FAMILIES[1]),
            case("hold-schema", "heldout", FAMILIES[0]),
            case("hold-path", "heldout", FAMILIES[1]),
        ],
    }


class PolicyLaboratoryTests(unittest.TestCase):
    def test_candidate_only_proposed_for_heldout_two_family_gain(self):
        data = manifest()
        result = lab.evaluate(data)
        self.assertEqual(result["decision"], "PROPOSE_BOUNDED_LIVE_PILOT")
        self.assertEqual(result["incumbent"], "recorded-order")
        self.assertEqual(result["heldout_families"], sorted(FAMILIES))
        self.assertEqual(result["development_case_count"], 2)
        self.assertEqual(result["heldout_case_count"], 2)
        self.assertTrue(all(c["recorded_failure_detection_delta"] == 1
                            for c in result["cases"]))
        self.assertFalse(result["automatic_activation"])
        self.assertFalse(result["actual_host_execution_authenticated"])
        self.assertFalse(result["real_user_effectiveness_verified"])

    def test_repeat_has_identical_bounded_evidence(self):
        first = lab.evaluate(manifest())
        second = lab.evaluate(manifest())
        self.assertEqual(json.dumps(first, sort_keys=True),
                         json.dumps(second, sort_keys=True))

    def test_false_cost_saving_by_skipping_protected_verifier_is_vetoed(self):
        data = manifest()
        data["candidate"]["max_attempts"] = 1
        result = lab.evaluate(data)
        self.assertEqual(result["decision"], "REJECT_CANDIDATE")
        self.assertIn("PROTECTED_VERIFIER_SKIPPED_OR_FAILED", result["veto_reasons"])

    def test_training_gain_with_negative_heldout_is_not_promotion(self):
        data = manifest()
        data["cases"][2] = case("hold-schema", "heldout", FAMILIES[0], gain=False)
        decision = lab.evaluate(data)
        self.assertEqual(decision["decision"], "HOLD_INCUMBENT")
        self.assertEqual(decision["cases"][2]["recorded_failure_detection_delta"], 0)

    def test_failed_protected_preservation_is_vetoed(self):
        data = manifest()
        target = data["cases"][0]["trace"]
        protected = next(n for n in target["nodes"] if n["node_id"] == "n-check")
        protected["outcome"] = "OBSERVED_FAIL"
        receipts = [r for r in target["receipts"]
                    if r["payload"]["node_id"] != "n-check"]
        receipts.append(with_receipt(protected))
        target["receipts"] = receipts
        outcome = lab.evaluate(data)
        self.assertEqual(outcome["decision"], "REJECT_CANDIDATE")
        self.assertIn("PROTECTED_VERIFIER_SKIPPED_OR_FAILED",
                      outcome["veto_reasons"])

    def test_unknown_branch_does_not_gain(self):
        data = manifest()
        data["cases"][3] = case("hold-path", "heldout", FAMILIES[1],
                                proposal_attack=True)
        result = lab.evaluate(data)
        self.assertNotEqual(result["decision"], "PROPOSE_BOUNDED_LIVE_PILOT")
        self.assertTrue(result["veto_reasons"])

    def test_evaluator_artifact_digest_is_required_and_pinned(self):
        data = manifest()
        self.assertEqual(lab.evaluate(data)["evaluator_sha256"],
                         data["evaluator_sha256"])
        del data["evaluator_sha256"]
        with self.assertRaises(lab.LabError):
            lab.evaluate(data)
        data = manifest()
        data["evaluator_sha256"] = "unverifiable"
        with self.assertRaises(replay.ReplayError):
            lab.evaluate(data)

    def test_candidate_does_not_control_evaluator(self):
        data = manifest()
        data["candidate"]["evaluator_id"] = "cheaper"
        with self.assertRaises(lab.LabError):
            lab.evaluate(data)

    def test_candidate_cannot_supply_commands_permissions_or_approvals(self):
        for key, value in (("approved", True), ("shell", "rm -rf /"),
                           ("network", "example.com"),
                           ("scoring_weights", {"security": 0}),
                           ("write_path", "SKILL.md")):
            with self.subTest(key=key):
                data = manifest()
                data["candidate"][key] = value
                with self.assertRaises(lab.LabError):
                    lab.evaluate(data)

    def test_candidate_must_use_known_priority_and_stop(self):
        for key, bad in (("branch_priority", "outcome-hindsight"),
                         ("stop_on", "ignore-blocked"),
                         ("verify_lane", "inspect"),
                         ("max_attempts", 0),
                         ("max_attempts", 4)):
            with self.subTest(key=key):
                data = manifest()
                data["candidate"][key] = bad
                with self.assertRaises(lab.LabError):
                    lab.evaluate(data)

    def test_holdout_must_include_two_development_supported_families(self):
        data = manifest()
        data["cases"][3]["task_family"] = FAMILIES[0]
        for n in data["cases"][3]["trace"]["nodes"]:
            n["task_family"] = FAMILIES[0]
        with self.assertRaisesRegex(lab.LabError, "two task families"):
            lab.evaluate(data)

    def test_training_case_cannot_be_reused_as_holdout(self):
        data = manifest()
        data["cases"][2]["trace"]["experiment_id"] = data["cases"][0]["trace"]["experiment_id"]
        with self.assertRaisesRegex(lab.LabError, "reused"):
            lab.evaluate(data)

    def test_wrong_context_rejected_before_comparing(self):
        data = manifest()
        data["cases"][2]["trace"]["evaluation_context_id"] = "wrong-context"
        with self.assertRaisesRegex(replay.ReplayError, "drift"):
            lab.evaluate(data)

    def test_tampered_orphan_receipt_is_not_reward(self):
        data = manifest()
        data["cases"][1]["trace"]["receipts"][0]["payload"]["outcome"] = "OBSERVED_FAIL"
        with self.assertRaises(replay.ReplayError):
            lab.evaluate(data)

    def test_unobserved_required_verifier_is_blocked(self):
        data = manifest()
        data["cases"][1]["required_actions"] = ["run-targeted-verification"]
        with self.assertRaisesRegex(lab.LabError, "No recorded protected"):
            lab.evaluate(data)

    def test_duplicate_case_ids_rejected(self):
        data = manifest()
        data["cases"][1]["case_id"] = data["cases"][0]["case_id"]
        with self.assertRaisesRegex(lab.LabError, "Duplicate case"):
            lab.evaluate(data)

    def test_cli_requires_explicit_clearance(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "manifest.json"
            target.write_text(json.dumps(manifest()), encoding="utf-8")
            with redirect_stderr(StringIO()) as err:
                code = lab.main(["--manifest", str(target)])
            self.assertEqual(code, 2)
            self.assertIn("clearance", err.getvalue().lower())

    def test_cli_cannot_self_grant_consent_via_manifest(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "manifest.json"
            data = manifest()
            data["approved"] = True
            target.write_text(json.dumps(data), encoding="utf-8")
            with redirect_stderr(StringIO()) as err:
                code = lab.main(["--manifest", str(target), "--approved-public"])
            self.assertEqual(code, 2)
            self.assertIn("fields", err.getvalue().lower())

    def test_cli_rejects_duplicate_json_key(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "manifest.json"
            target.write_text('{"schema_version":1,"schema_version":1}')
            with redirect_stderr(StringIO()) as err:
                code = lab.main(["--manifest", str(target), "--approved-public"])
            self.assertEqual(code, 2)
            self.assertIn("duplicate", err.getvalue().lower())

    def test_cli_is_read_only_and_produces_no_trace_file(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "manifest.json"
            target.write_text(json.dumps(manifest()), encoding="utf-8")
            before = sorted(x.name for x in Path(folder).iterdir())
            with redirect_stdout(StringIO()) as out:
                code = lab.main(["--manifest", str(target), "--approved-public"])
            self.assertEqual(code, 0)
            self.assertEqual(sorted(x.name for x in Path(folder).iterdir()), before)
            self.assertEqual(json.loads(out.getvalue())["automatic_activation"], False)



    def test_cli_rejects_linked_manifest_file(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            private = root / "private.json"
            private.write_text(json.dumps(manifest()), encoding="utf-8")
            alias = root / "approved.json"
            alias.symlink_to(private)
            with redirect_stderr(StringIO()) as error:
                code = lab.main(["--manifest", str(alias), "--approved-public"])
            self.assertEqual(code, 2)
            self.assertIn("Symlinked manifest path", error.getvalue())
            self.assertNotIn(private.read_text(), error.getvalue())

    def test_cli_rejects_linked_manifest_ancestor(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "private").mkdir()
            real = root / "private" / "manifest.json"
            real.write_text(json.dumps(manifest()), encoding="utf-8")
            alias = root / "external"
            alias.symlink_to(root / "private", target_is_directory=True)
            with redirect_stderr(StringIO()) as error:
                code = lab.main(["--manifest", str(alias / "manifest.json"),
                                 "--approved-public"])
            self.assertEqual(code, 2)
            self.assertIn("Symlinked manifest path", error.getvalue())

if __name__ == "__main__":
    unittest.main()
