import copy
import unittest

from trial_matrix import digest, freeze, reconcile


def inputs():
    def plan(tag):
        manifest = [{"source": "SKILL.md", "sha256": digest(tag)}]
        body = {"schema_version": 1, "status": "DESIGNED_NOT_RUN", "skill": "fictional-skill",
                "host": "claude-apps", "canonical_files_sha256": {"SKILL.md": digest(tag)},
                "host_member_manifest": manifest, "host_member_manifest_sha256": digest(manifest),
                "cases": [{"id": k, "kind": "positive", "receipt_stage": "outcome", "status": "NOT_RUN"}
                          for k in ("case-a", "case-b")]}
        return {"plan": body, "plan_sha256": digest(body)}
    config = {"schema_version": 1, "runtime_sha256": digest("fake-runtime"),
              "budget_per_trial": 10, "repetitions": 2,
              "fixtures": [{"case_id": k, "family": k, "partition": p,
                            "fixture_sha256": digest(k), "oracle_sha256": digest(k + "-oracle")}
                           for k, p in (("case-a", "development"), ("case-b", "held-out"))]}
    return plan("base"), plan("candidate"), config


def fake_ledger(frozen):
    return {"experiment_sha256": frozen["experiment_sha256"], "rows": [
        {"run_id": r["run_id"], "status": "FAIL_CLAIMED" if r["arm"] == "control" else "PASS_CLAIMED",
         "evidence_sha256": digest(["fictional-observation", r["run_id"]])}
        for r in frozen["experiment"]["runs"]]}


class TrialMatrixTests(unittest.TestCase):
    def setUp(self):
        self.b, self.c, self.config = inputs()
        self.frozen = freeze(self.b, self.c, self.config)
        self.ledger = fake_ledger(self.frozen)

    def result(self):
        return reconcile(self.b, self.c, self.config, self.ledger)

    def test_deterministic_and_complete(self):
        self.assertEqual(self.frozen, freeze(self.b, self.c, self.config))
        r = self.result()
        self.assertEqual(r["expected_runs"], 12)
        self.assertEqual(r["status"], "COMPLETE_COMPARATIVE_CLAIMS_REVIEW_REQUIRED")
        self.assertEqual(r["counts"]["held-out"]["control"]["FAIL_CLAIMED"], 2)
        self.assertFalse(r["host_execution_verified"])
        self.assertFalse(r["promotion_authorized"])

    def test_missing(self):
        self.ledger["rows"].pop()
        self.assertEqual(self.result()["status"], "HOLD_INCOMPLETE_TRIALS")

    def test_duplicate(self):
        self.ledger["rows"][-1] = self.ledger["rows"][0]
        with self.assertRaisesRegex(ValueError, "DUPLICATE"):
            self.result()

    def test_timeout(self):
        self.ledger["rows"][0]["status"] = "TIMEOUT"
        self.assertEqual(self.result()["status"], "HOLD_INCOMPLETE_TRIALS")

    def test_not_run_no_evidence(self):
        self.ledger["rows"][0]["status"] = "NOT_RUN"
        with self.assertRaisesRegex(ValueError, "NOT_RUN_WITH_EVIDENCE"):
            self.result()

    def test_evidence_reuse(self):
        self.ledger["rows"][1]["evidence_sha256"] = self.ledger["rows"][0]["evidence_sha256"]
        with self.assertRaisesRegex(ValueError, "REUSED_EVIDENCE"):
            self.result()

    def test_plan_drift(self):
        self.c["plan"]["canonical_files_sha256"]["SKILL.md"] = digest("changed")
        with self.assertRaisesRegex(ValueError, "PLAN_DIGEST_MISMATCH"):
            self.result()

    def test_oracle_drift(self):
        self.config["fixtures"][0]["oracle_sha256"] = digest("changed")
        with self.assertRaisesRegex(ValueError, "EXPERIMENT_DIGEST_MISMATCH"):
            self.result()

    def test_partition_leakage(self):
        self.config["fixtures"][1]["family"] = self.config["fixtures"][0]["family"]
        with self.assertRaisesRegex(ValueError, "PARTITION_LEAKAGE"):
            self.result()

    def test_fixture_leakage(self):
        self.config["fixtures"][1]["fixture_sha256"] = self.config["fixtures"][0]["fixture_sha256"]
        with self.assertRaisesRegex(ValueError, "PARTITION_LEAKAGE"):
            self.result()

    def test_failure_retained(self):
        self.ledger["rows"][2]["status"] = "FAIL_CLAIMED"
        self.assertEqual(self.result()["counts"]["development"]["candidate"]["FAIL_CLAIMED"], 1)

    def test_input_not_modified(self):
        before = copy.deepcopy((self.b, self.c, self.config, self.ledger))
        self.result()
        self.assertEqual(before, (self.b, self.c, self.config, self.ledger))


if __name__ == "__main__":
    unittest.main()
