"""Deterministic in-memory controller and planted-failure tests."""
import copy
import json
import unittest
from unittest.mock import patch

import trial_fake as fake
from test_trial_matrix import inputs


class FakeTrialTests(unittest.TestCase):
    def setUp(self):
        self.b, self.c, self.config = inputs()
        self.runtime = {"schema_version": 1, "adapter": "synthetic-in-memory-v1",
                        "initial_state": "empty-v1",
                        "modes": {"control": "wrong", "baseline": "correct", "candidate": "correct"}}
        self.fixtures = {"case-a": fake.encode({"values": [3, 1, 3, 2]}),
                         "case-b": fake.encode({"values": [0, -2, 0, 1]})}
        self.oracles = {k: fake.encode({"rule": "ascending-unique-permutation-v1"})
                        for k in self.fixtures}
        for f in self.config["fixtures"]:
            k = f["case_id"]
            f.update(fixture_sha256=fake.sha(self.fixtures[k]), oracle_sha256=fake.sha(self.oracles[k]))
        self.bind_runtime()

    def bind_runtime(self):
        self.runtime_bytes = fake.encode(self.runtime)
        self.config["runtime_sha256"] = fake.sha(self.runtime_bytes)

    def run_trial(self, execute=False):
        return fake.run(self.b, self.c, self.config, self.runtime_bytes, self.fixtures, self.oracles,
                        execute=execute)

    def test_default_never_invokes_adapter(self):
        with patch.object(fake, "emulate", side_effect=AssertionError("must not execute")):
            r = self.run_trial()
        self.assertEqual(r["status"], "DESIGNED_NOT_RUN")
        self.assertEqual(len(r["ledger"]["rows"]), 12)
        self.assertEqual({x["status"] for x in r["ledger"]["rows"]}, {"NOT_RUN"})
        self.assertEqual(r["receipts"], {})
        self.assertEqual(r["reconciliation"]["status"], "HOLD_INCOMPLETE_TRIALS")

    def test_positive_and_planted_failure_deterministic(self):
        r = self.run_trial(True)
        self.assertEqual(r, self.run_trial(True))
        self.assertEqual(r["reason_counts"], {"SYNTHETIC_ORACLE_PASS": 8, "SYNTHETIC_ORACLE_FAIL": 4})
        self.assertEqual(r["reconciliation"]["matched_receipts"], 12)
        self.assertEqual(r["reconciliation"]["status"], "COMPLETE_COMPARATIVE_CLAIMS_REVIEW_REQUIRED")
        self.assertEqual(r["native_host_runs"], 0)
        self.assertFalse(r["actual_skill_effectiveness_measured"])
        self.assertFalse(r["promotion_authorized"])
        self.assertFalse(r["real_isolation_verified"])
        for payload in r["payloads"].values():
            self.assertEqual(json.loads(payload)["evidence_kind"], "SYNTHETIC_FAKE_ONLY")

    def test_failures_distinguished_and_hold(self):
        for mode, reason, status in (
            ("setup-failure", "SETUP_FAILED", "INVALID"),
            ("timeout", "BUDGET_OR_TIMEOUT_SIMULATED", "TIMEOUT"),
            ("missing-trace", "TRACE_INCOMPLETE", "INVALID"),
            ("unauthorized-effect", "AUTHORITY_VIOLATION_SIMULATED", "INVALID"),
            ("dirty-cleanup", "CLEANUP_FAILED_SIMULATED", "INVALID"),
        ):
            with self.subTest(mode=mode):
                self.runtime["modes"]["candidate"] = mode
                self.bind_runtime()
                r = self.run_trial(True)
                self.assertEqual(r["reason_counts"][reason], 4)
                self.assertEqual(r["reconciliation"]["status"], "HOLD_INCOMPLETE_TRIALS")
                self.assertEqual(r["reconciliation"]["counts"]["held-out"]["candidate"][status], 2)

    def test_budget_exhaustion_preserves_all_runs(self):
        self.config["budget_per_trial"] = 1
        r = self.run_trial(True)
        self.assertEqual(r["reason_counts"], {"BUDGET_OR_TIMEOUT_SIMULATED": 12})
        self.assertEqual(len(r["ledger"]["rows"]), 12)
        self.assertEqual(r["reconciliation"]["status"], "HOLD_INCOMPLETE_TRIALS")
        self.assertTrue(all(json.loads(p)["observation"]["simulated_steps"] <= 1
                            for p in r["payloads"].values()))

    def test_fixture_or_oracle_drift_rejected_before_execution(self):
        for mapping in (self.fixtures, self.oracles):
            with self.subTest(mapping=list(mapping)):
                old = mapping["case-b"]
                mapping["case-b"] = old + b" "
                with patch.object(fake, "emulate", side_effect=AssertionError("no execute")):
                    with self.assertRaisesRegex(ValueError, "DIGEST_MISMATCH"):
                        self.run_trial(True)
                mapping["case-b"] = old

    def test_runtime_drift_and_unknown_adapter_rejected(self):
        self.runtime_bytes += b" "
        with self.assertRaisesRegex(ValueError, "DIGEST_MISMATCH"):
            self.run_trial(True)
        self.runtime["adapter"] = "real-shell"
        self.bind_runtime()
        with self.assertRaisesRegex(ValueError, "UNSUPPORTED_SYNTHETIC_RUNTIME"):
            self.run_trial(True)

    def test_missing_extra_and_partition_leakage_rejected(self):
        original = self.oracles.pop("case-b")
        with self.assertRaisesRegex(ValueError, "INVENTORY_MISMATCH"):
            self.run_trial(True)
        self.oracles["case-b"] = original
        self.fixtures["extra"] = b"{}"
        with self.assertRaisesRegex(ValueError, "INVENTORY_MISMATCH"):
            self.run_trial(True)
        self.fixtures.pop("extra")
        self.config["fixtures"][1]["family"] = self.config["fixtures"][0]["family"]
        with self.assertRaisesRegex(ValueError, "PARTITION_LEAKAGE"):
            self.run_trial(True)

    def test_independent_oracle_detects_false_green_and_accepts_valid_output(self):
        self.assertTrue(fake.oracle_accepts([2, 1, 2], [1, 2]))
        for output in ([2, 1], [1, 2, 2], [1, 3], [True, 2]):
            self.assertFalse(fake.oracle_accepts([2, 1, 2], output))
        with patch.object(fake, "emulate", wraps=fake.emulate) as adapter:
            r = self.run_trial(True)
            self.assertEqual(adapter.call_count, 12)
            self.assertEqual(r["reason_counts"]["SYNTHETIC_ORACLE_FAIL"], 4)

    def test_unknown_oracle_and_non_boolean_switch_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "INVALID_EXECUTION_SWITCH"):
            self.run_trial("yes")
        self.oracles["case-a"] = fake.encode({"rule": "always-pass"})
        self.config["fixtures"][0]["oracle_sha256"] = fake.sha(self.oracles["case-a"])
        with self.assertRaisesRegex(ValueError, "UNSUPPORTED_SYNTHETIC_FIXTURE_OR_ORACLE"):
            self.run_trial(True)

    def test_plan_drift_refused(self):
        self.c["plan"]["canonical_files_sha256"]["SKILL.md"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "ACCEPTANCE_PLAN_DIGEST_MISMATCH"):
            self.run_trial(True)
