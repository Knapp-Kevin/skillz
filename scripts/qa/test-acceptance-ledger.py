"""Synthetic case reconciliation; no external host or model is executed."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "engine/builder"))
import acceptance_ledger as m
spec = importlib.util.spec_from_file_location("design_cases", ROOT / "scripts/qa/test-engine-builder-design.py")
fixtures = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fixtures)


class LedgerTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.dossier = fixtures.case()
        self.skill = self.dossier["blueprint"]["name"]
        self.folder = self.root / self.skill
        m.planner.design.design_build(self.dossier, str(self.folder), write=True)
        self.host = "claude-apps"
        self.plan = m.planner.plan(self.dossier, self.folder, self.host)
        self.archive = self.root / (self.skill + ".zip")
        report = m.planner.compat.inspect(self.folder, self.host)
        m.planner.compat.write_zip(self.folder, self.host, str(self.archive), report)
        self.manifest_sha = "b" * 64
        self.manifest = {"schema_version": 1, "source_commit": "a" * 40,
                         "skills": [{"id": self.skill, "package_tree_sha": "c" * 40,
                                     "hosts": {self.host: {"status": "PACKAGE_READY",
                                                           "blockers": [], "asset": self.archive.name}}}]}
        self.receipt = {"schema_version": 1, "skill": self.skill, "host": self.host,
                        "source_commit": "a" * 40, "package_tree_sha": "c" * 40,
                        "asset": self.archive.name, "manifest_sha256": self.manifest_sha,
                        "environment": {k: "fictional-" + k for k in m.a.ENV_FIELDS},
                        "execution_kind": "NATIVE_HOST_CLAIMED", "authorization": "APPROVAL_CLAIMED",
                        "cases": [{"stage": s, "status": "PASS_CLAIMED",
                                   "evidence_id": "stage-e-" + s, "oracle_id": "stage-o-" + s}
                                  for s in m.a.STAGES]}
        self.ledger = {"schema_version": 1, "plan_sha256": self.plan["plan_sha256"],
                       "cases": [{"case_id": c["id"], "status": "PASS_CLAIMED",
                                  "fixture_id": f"fixture-{i}", "oracle_id": f"oracle-{i}",
                                  "evidence_id": f"evidence-{i}"}
                                 for i, c in enumerate(self.plan["plan"]["cases"])]}
        self.refresh_archive()

    def bind_receipt(self):
        self.receipt_sha = m.planner.canonical_sha(self.receipt)
        self.ledger["receipt_sha256"] = self.receipt_sha

    def refresh_archive(self):
        digest = hashlib.sha256(self.archive.read_bytes()).hexdigest()
        self.manifest["skills"][0]["hosts"][self.host]["sha256"] = digest
        self.receipt["sha256"] = digest
        self.bind_receipt()

    def check(self):
        return m.reconcile(self.dossier, self.folder, self.manifest, self.manifest_sha,
                           self.archive, self.receipt, self.receipt_sha, self.ledger)

    def row(self, ident):
        return next(c for c in self.ledger["cases"] if c["case_id"] == ident)

    def stage(self, name, status):
        row = next(c for c in self.receipt["cases"] if c["stage"] == name)
        row["status"] = status
        if status in ("UNKNOWN", "NOT_RUN"):
            row.update(evidence_id=None, oracle_id=None)
        self.bind_receipt()

    def test_complete_claims_still_require_independent_review(self):
        result = self.check()
        self.assertEqual(result["status"], "COMPLETE_CASE_CLAIMS_REVIEW_REQUIRED")
        self.assertTrue(result["case_ledger_reconciled"])
        self.assertTrue(result["archive_members_match_regenerated_plan"])
        self.assertTrue(result["archive_payload_crc_verified"])
        self.assertEqual(result["case_claim_counts"]["PASS_CLAIMED"], len(self.ledger["cases"]))
        for key in ("host_execution_observed", "consumer_accepted", "authorization_verified",
                    "fixture_and_oracle_contents_verified", "preregistration_time_verified"):
            self.assertIs(result[key], False)

    def test_failed_or_unrun_case_cannot_hide_behind_pass(self):
        for status in ("FAIL_CLAIMED", "UNKNOWN", "NOT_RUN"):
            with self.subTest(status=status):
                row = self.row("probe-missing-input")
                original = row.copy()
                row["status"] = status
                if status not in m.CLAIMED:
                    row["evidence_id"] = None
                with self.assertRaisesRegex(ValueError, "STAGE_SUMMARY_CONTRADICTS_CASES"):
                    self.check()
                row.update(original)

    def test_coherent_failure_and_unknown_are_holds(self):
        row = self.row("probe-false-green")
        row["status"] = "FAIL_CLAIMED"
        self.stage("outcome", "FAIL_CLAIMED")
        self.assertEqual(self.check()["status"], "HOLD_REPORTED_FAILURE")
        row.update(status="NOT_RUN", evidence_id=None)
        self.stage("outcome", "UNKNOWN")
        self.assertEqual(self.check()["status"], "HOLD_INCOMPLETE_NATIVE_CLAIM")

    def test_missing_duplicate_or_foreign_case_rejected(self):
        original = copy.deepcopy(self.ledger["cases"])
        for rows in (original[:-1], original[:-1] + [original[0]],
                     original[:-1] + [dict(original[-1], case_id="fake")]):
            self.ledger["cases"] = rows
            with self.assertRaises(ValueError):
                self.check()

    def test_plan_and_receipt_digest_mismatch(self):
        for key in ("plan_sha256", "receipt_sha256"):
            previous = self.ledger[key]
            self.ledger[key] = "d" * 64
            with self.assertRaisesRegex(ValueError, "DIGEST_MISMATCH"):
                self.check()
            self.ledger[key] = previous

    def test_rehashed_archive_with_changed_or_extra_payload_rejected(self):
        with zipfile.ZipFile(self.archive) as z:
            members = {name: z.read(name) for name in z.namelist()}
        for changed in (dict(members, **{self.skill + "/SKILL.md": b"substituted"}),
                        dict(members, **{self.skill + "/extra.txt": b"extra"})):
            with zipfile.ZipFile(self.archive, "w") as z:
                for name, data in changed.items():
                    z.writestr(name, data)
            self.refresh_archive()
            with self.assertRaisesRegex(ValueError, "PLAN_ARCHIVE_"):
                self.check()

    def test_case_evidence_reuse_and_stage_alias_rejected(self):
        rows = self.ledger["cases"]
        for key, val in (("evidence_id", rows[0]["evidence_id"]),
                         ("oracle_id", rows[0]["oracle_id"]),
                         ("fixture_id", rows[0]["evidence_id"]),
                         ("evidence_id", self.receipt["cases"][0]["evidence_id"])):
            row = rows[-1]
            old = row[key]
            row[key] = val
            with self.assertRaises(ValueError):
                self.check()
            row[key] = old

    def set_stage_cases(self, stage, status):
        for ident in self.plan["plan"]["receipt_stage_requirements"][stage]:
            row = self.row(ident)
            row["status"] = status
            if status not in m.CLAIMED:
                row.update(evidence_id=None, fixture_id=None, oracle_id=None)
        self.stage(stage, status)

    def test_mixed_outcome_cannot_hide_pass_without_trigger(self):
        self.set_stage_cases("positive_trigger", "NOT_RUN")
        self.row("probe-missing-input").update(status="NOT_RUN", evidence_id=None)
        self.stage("outcome", "UNKNOWN")
        with self.assertRaisesRegex(ValueError, "CASE_OUTCOME_PASS_WITHOUT_TRIGGER"):
            self.check()

    def test_mixed_outcome_cannot_hide_pass_without_load(self):
        self.set_stage_cases("load", "NOT_RUN")
        for stage in ("positive_trigger", "near_non_trigger", "authority_boundary"):
            self.set_stage_cases(stage, "NOT_RUN")
        self.row("probe-missing-input").update(status="NOT_RUN", evidence_id=None)
        self.stage("outcome", "UNKNOWN")
        with self.assertRaisesRegex(ValueError, "CASE_BEHAVIOR_PASS_WITHOUT_LOAD"):
            self.check()

    def test_failed_outcome_group_cannot_hide_other_pass_without_trigger(self):
        self.set_stage_cases("positive_trigger", "NOT_RUN")
        self.row("probe-false-green")["status"] = "FAIL_CLAIMED"
        self.stage("outcome", "FAIL_CLAIMED")
        with self.assertRaisesRegex(ValueError, "CASE_OUTCOME_PASS_WITHOUT_TRIGGER"):
            self.check()

    def test_failed_load_retains_failure_without_fabricated_behavior(self):
        self.set_stage_cases("load", "FAIL_CLAIMED")
        for stage in ("positive_trigger", "near_non_trigger", "outcome", "authority_boundary"):
            self.set_stage_cases(stage, "NOT_RUN")
        self.assertEqual(self.check()["status"], "HOLD_REPORTED_FAILURE")

    def test_placeholder_case_identifiers_rejected(self):
        row = self.ledger["cases"][0]
        for field in ("fixture_id", "oracle_id", "evidence_id"):
            original = row[field]
            for value in ("n.a", "UNKNOWN", "placeholder"):
                with self.subTest(field=field, value=value):
                    row[field] = value
                    with self.assertRaisesRegex(ValueError, "CASE_EVIDENCE_REQUIRED"):
                        self.check()
            row[field] = original
        self.assertEqual(self.check()["status"], "COMPLETE_CASE_CLAIMS_REVIEW_REQUIRED")

    def test_all_not_run_preserves_hold(self):
        for row in self.ledger["cases"]:
            row.update(status="NOT_RUN", evidence_id=None, fixture_id=None, oracle_id=None)
        self.receipt["execution_kind"] = "NOT_RUN"
        self.receipt["authorization"] = "NOT_ESTABLISHED"
        for stage in m.a.STAGES:
            self.stage(stage, "NOT_RUN")
        result = self.check()
        self.assertEqual(result["status"], "HOLD_INCOMPLETE_NATIVE_CLAIM")
        self.assertEqual(result["case_claim_counts"]["NOT_RUN"], len(self.ledger["cases"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
