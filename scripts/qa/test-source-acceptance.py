"""Source-pinned manual acceptance pilot and negative tests; no host invocation."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "engine/builder"))
import source_acceptance as m
import acceptance_ledger as ledger

CONTRACT = ROOT / "engine/builder/examples/scheduled-work-source-contract.json"
PACKAGE = ROOT / "skills/authored/scheduled-work-proof-auditor"


class SourceTests(unittest.TestCase):
    def setUp(self):
        self.contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)

    def test_real_authored_pilot_exact_pins_and_all_assessed_hosts(self):
        self.assertEqual(m.inventory(PACKAGE)["source_blobs"], self.contract["source_blobs"])
        for host in m.compat.HOSTS:
            with self.subTest(host=host):
                p = m.plan(self.contract, PACKAGE, host)
                self.assertEqual(p, m.plan(self.contract, PACKAGE, host))
                self.assertEqual(set(p["plan"]["receipt_stage_requirements"]), set(m.a.STAGES))
                self.assertEqual({c["status"] for c in p["plan"]["cases"]}, {"NOT_RUN"})
                self.assertFalse(p["plan"]["host_execution_observed"])

    def copy_package(self):
        import shutil
        return Path(shutil.copytree(PACKAGE, self.root / PACKAGE.name))

    def test_source_change_or_extra_member_rejected(self):
        folder = self.copy_package()
        extra = folder / "extra.txt"
        extra.write_text("extra")
        with self.assertRaisesRegex(ValueError, "SOURCE_INVENTORY_MISMATCH"):
            m.plan(self.contract, folder, "claude-code")
        extra.unlink()
        p = folder / "examples/synthetic-cases.md"
        p.write_bytes(p.read_bytes() + b"changed")
        with self.assertRaisesRegex(ValueError, "SOURCE_BLOB_MISMATCH"):
            m.plan(self.contract, folder, "claude-code")

    def test_missing_case_and_invalid_anchor_rejected(self):
        for mutation in ("remove", "anchor", "duplicate"):
            c = copy.deepcopy(self.contract)
            if mutation == "remove":
                c["cases"].pop()
            elif mutation == "anchor":
                c["cases"][0]["anchor"] = "Invented source text not found."
            else:
                c["cases"][-1]["id"] = c["cases"][0]["id"]
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                m.plan(c, PACKAGE, "claude-code")

    def test_example_cannot_replace_normative_anchor(self):
        self.contract["cases"][0].update(source="examples/synthetic-cases.md",
            anchor="These are hand-authored expected cases, not executed validation.")
        with self.assertRaisesRegex(ValueError, "CORE_CASE_REQUIRES_NORMATIVE_SOURCE"):
            m.plan(self.contract, PACKAGE, "claude-code")

    def test_unknown_host_and_unknown_contract_fields_rejected(self):
        with self.assertRaises(ValueError):
            m.plan(self.contract, PACKAGE, "chatgpt")
        self.contract["validated"] = True
        with self.assertRaises(ValueError):
            m.plan(self.contract, PACKAGE, "claude-code")

    def test_real_source_plan_to_ledger_handoff_preserves_not_run(self):
        host = "gemini-apps"
        p = m.plan(self.contract, PACKAGE, host)
        slug = PACKAGE.name
        archive = self.root / (slug + "-gemini.zip")
        m.compat.write_zip(PACKAGE, host, str(archive), m.compat.inspect(PACKAGE, host))
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        manifest = {"schema_version": 1, "source_commit": "a"*40,
                    "skills": [{"id": slug, "package_tree_sha": "b"*40,
                                "hosts": {host: {"status": "PACKAGE_READY", "blockers": [],
                                                 "asset": archive.name, "sha256": digest}}}]}
        manifest_sha = "c"*64
        receipt = {"schema_version": 1, "skill": slug, "host": host, "source_commit": "a"*40,
                   "package_tree_sha": "b"*40, "asset": archive.name, "sha256": digest,
                   "manifest_sha256": manifest_sha, "environment": {k: "UNKNOWN" for k in m.a.ENV_FIELDS},
                   "execution_kind": "NOT_RUN", "authorization": "NOT_ESTABLISHED",
                   "cases": [{"stage": s, "status": "NOT_RUN", "evidence_id": None, "oracle_id": None}
                             for s in m.a.STAGES]}
        receipt_sha = m.generated.canonical_sha(receipt)
        rows = {"schema_version": 1, "plan_sha256": p["plan_sha256"], "receipt_sha256": receipt_sha,
                "cases": [{"case_id": c["id"], "status": "NOT_RUN", "fixture_id": None,
                           "oracle_id": None, "evidence_id": None} for c in p["plan"]["cases"]]}
        result = ledger.reconcile(self.contract, PACKAGE, manifest, manifest_sha, archive, receipt,
                                  receipt_sha, rows, source_contract=True)
        self.assertEqual(result["status"], "HOLD_INCOMPLETE_NATIVE_CLAIM")
        self.assertTrue(result["archive_members_match_regenerated_plan"])
        self.assertFalse(result["host_execution_observed"])
        self.assertEqual(result["case_claim_counts"]["NOT_RUN"], len(rows["cases"]))
        rows["cases"].pop()
        with self.assertRaisesRegex(ValueError, "INCOMPLETE_CASE_LEDGER"):
            ledger.reconcile(self.contract, PACKAGE, manifest, manifest_sha, archive, receipt,
                             receipt_sha, rows, source_contract=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
