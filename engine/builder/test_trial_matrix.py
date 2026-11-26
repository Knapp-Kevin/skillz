import copy
import hashlib
import json
import unittest

from trial_matrix import digest, freeze, reconcile, reconcile_receipts


def inputs():
    def plan(tag):
        manifest = [{"source": "SKILL.md", "sha256": digest(tag)}]
        body = {"schema_version": 1, "status": "DESIGNED_NOT_RUN", "skill": "fictional-skill",
                "host": "claude-apps", "canonical_files_sha256": {"SKILL.md": digest(tag)},
                "host_member_manifest": manifest, "host_member_manifest_sha256": digest(manifest),
                "cases": [{"id": k, "kind": "positive", "receipt_stage": "outcome", "status": "NOT_RUN",
                           "expected_contract": "fictional outcome"}
                          for k in ("case-a", "case-b")]}
        return {"plan": body, "plan_sha256": digest(body)}
    config = {"schema_version": 1, "experiment_id": "fictional-one",
              "runtime_sha256": digest("fake-runtime"), "budget_unit": "tool-calls",
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

    def test_run_ids_bound_to_experiment_scope(self):
        original = {r["run_id"] for r in self.frozen["experiment"]["runs"]}
        for field, value in (("experiment_id", "fictional-two"),
                             ("runtime_sha256", digest("other-runtime")),
                             ("budget_unit", "tokens"), ("budget_per_trial", 20)):
            with self.subTest(field=field):
                config = {**self.config, field: value}
                other = freeze(self.b, self.c, config)
                self.assertFalse(original & {r["run_id"] for r in other["experiment"]["runs"]})
                self.ledger["experiment_sha256"] = other["experiment_sha256"]
                with self.assertRaisesRegex(ValueError, "UNKNOWN_DUPLICATE"):
                    reconcile(self.b, self.c, config, self.ledger)

    def test_same_package_new_plan_refused(self):
        self.c = copy.deepcopy(self.b)
        self.c["plan"]["dossier_sha256"] = digest("different-dossier")
        self.c["plan_sha256"] = digest(self.c["plan"])
        with self.assertRaisesRegex(ValueError, "IDENTICAL_PACKAGE"):
            freeze(self.b, self.c, self.config)

    def test_changed_expectation_refused(self):
        self.c["plan"]["cases"][0]["expected_contract"] = "weaker outcome"
        self.c["plan_sha256"] = digest(self.c["plan"])
        with self.assertRaisesRegex(ValueError, "CASE_EXPECTATION_CHANGED"):
            freeze(self.b, self.c, self.config)

    def bound_receipts(self):
        receipts, payloads = {}, {}
        for row in self.ledger["rows"]:
            run_id = row["run_id"]
            payload = b"fictional output"
            receipt = {"schema_version": 1, "experiment_sha256": self.frozen["experiment_sha256"],
                       "run_id": run_id, "status": row["status"],
                       "payload_sha256": hashlib.sha256(payload).hexdigest()}
            raw = json.dumps(receipt).encode()
            row["evidence_sha256"] = hashlib.sha256(raw).hexdigest()
            receipts[run_id], payloads[run_id] = raw, payload
        return receipts, payloads

    def receipt_result(self, receipts, payloads):
        return reconcile_receipts(self.b, self.c, self.config, self.ledger, receipts, payloads)

    def test_receipt_payload_match_not_authentication(self):
        receipts, payloads = self.bound_receipts()
        result = self.receipt_result(receipts, payloads)
        self.assertEqual(result["matched_receipts"], 12)
        self.assertTrue(result["local_receipt_payloads_matched"])
        self.assertFalse(result["evidence_authenticated"])
        self.assertFalse(result["host_execution_verified"])

    def test_payload_mutation(self):
        receipts, payloads = self.bound_receipts()
        payloads[next(iter(payloads))] = b"altered"
        with self.assertRaisesRegex(ValueError, "PAYLOAD_DIGEST_MISMATCH"):
            self.receipt_result(receipts, payloads)

    def test_status_relabel(self):
        receipts, payloads = self.bound_receipts()
        self.ledger["rows"][0]["status"] = "PASS_CLAIMED"
        with self.assertRaisesRegex(ValueError, "OBSERVATION_SUBJECT_MISMATCH"):
            self.receipt_result(receipts, payloads)

    def test_receipt_missing(self):
        receipts, payloads = self.bound_receipts()
        receipts.pop(next(iter(receipts)))
        with self.assertRaisesRegex(ValueError, "EVIDENCE_INVENTORY_MISMATCH"):
            self.receipt_result(receipts, payloads)

    def test_receipt_relabel(self):
        receipts, payloads = self.bound_receipts()
        row = self.ledger["rows"][0]
        raw = receipts[row["run_id"]].replace(row["run_id"].encode(), b"0" * 64)
        receipts[row["run_id"]] = raw
        row["evidence_sha256"] = hashlib.sha256(raw).hexdigest()
        with self.assertRaisesRegex(ValueError, "OBSERVATION_SUBJECT_MISMATCH"):
            self.receipt_result(receipts, payloads)

    def test_duplicate_receipt_key(self):
        receipts, payloads = self.bound_receipts()
        row = self.ledger["rows"][0]
        raw = receipts[row["run_id"]].replace(b'{', b'{"schema_version": 1,', 1)
        receipts[row["run_id"]] = raw
        row["evidence_sha256"] = hashlib.sha256(raw).hexdigest()
        with self.assertRaisesRegex(ValueError, "DUPLICATE_RECEIPT_KEY"):
            self.receipt_result(receipts, payloads)

    def test_input_not_modified(self):
        before = copy.deepcopy((self.b, self.c, self.config, self.ledger))
        self.result()
        self.assertEqual(before, (self.b, self.c, self.config, self.ledger))


if __name__ == "__main__":
    unittest.main()
