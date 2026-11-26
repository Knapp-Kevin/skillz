"""Integration against actual authored-downloads builder outputs; never installs."""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "engine/builder"))
import release_handoff as m

DIRECTORY = Path(sys.argv.pop(1)).absolute()
MANIFEST = DIRECTORY / "authored-download-manifest.json"


class ReleaseHandoffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest, cls.manifest_sha = m.a.read_json(MANIFEST)
        cls.registry, _ = m.a.read_json(ROOT / "registry/authored-skills-index.json")
        cls.contracts = {}
        for p in sorted((ROOT / "engine/builder/examples").glob("*-source-contract.json")):
            contract, _ = m.a.read_json(p)
            if contract["skill"] in cls.contracts:
                raise ValueError("duplicate contract")
            cls.contracts[contract["skill"]] = contract

    def test_real_builder_output_all_registered_profiles(self):
        head = subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"],
                                       text=True).strip()
        self.assertEqual(self.manifest["source_commit"], head)
        registered = {row["id"]: row for row in self.registry["skills"]}
        rows = self.manifest["skills"]
        self.assertEqual(len(rows), len(registered))
        self.assertEqual({row["id"] for row in rows}, set(registered))
        self.assertEqual(set(self.contracts), set(registered))
        ready, holds = set(), set()
        assets = {MANIFEST.name}
        for row in rows:
            slug = row["id"]
            package = ROOT / "skills/authored" / slug
            self.assertEqual(row["package_tree_sha"], registered[slug]["package_tree_sha"])
            self.assertEqual(row["skill_blob_sha"], registered[slug]["skill_blob_sha"])
            canonical = row["canonical"]
            self.assertEqual(canonical["asset"], slug + ".zip")
            self.assertEqual(hashlib.sha256((DIRECTORY / canonical["asset"]).read_bytes()).hexdigest(),
                             canonical["sha256"])
            assets.add(canonical["asset"])
            self.assertEqual(set(row["hosts"]), set(m.source.compat.HOSTS) |
                             set(m.source.compat.UNASSESSED_HOSTS))
            for host, profile in row["hosts"].items():
                with self.subTest(skill=slug, host=host):
                    self.assertEqual(profile["behavior"], "NOT_TESTED")
                    if host in m.source.compat.UNASSESSED_HOSTS:
                        self.assertEqual(profile["status"], "HOLD")
                        self.assertIsNone(profile["asset"])
                        self.assertIsNone(profile["sha256"])
                        with self.assertRaisesRegex(ValueError, "^INVALID_SKILL_OR_HOST$"):
                            m.prepare(self.contracts[slug], package, MANIFEST, DIRECTORY / canonical["asset"], host)
                        continue
                    pair = (slug, host)
                    allowed = m.source.compat.AUTHORED_HOLD_EXCEPTIONS.get(pair)
                    if allowed is not None:
                        self.assertEqual(profile["status"], "HOLD")
                        self.assertEqual(set(profile["blockers"]), set(allowed))
                        self.assertIsNone(profile["asset"])
                        self.assertIsNone(profile["sha256"])
                        with self.assertRaisesRegex(ValueError, "^HOST_PACKAGE_HOLD$"):
                            m.prepare(self.contracts[slug], package, MANIFEST, DIRECTORY / canonical["asset"], host)
                        holds.add(pair)
                        continue
                    self.assertEqual(profile["status"], "PACKAGE_READY")
                    self.assertEqual(profile["blockers"], [])
                    archive = DIRECTORY / profile["asset"]
                    result = m.prepare(self.contracts[slug], package, MANIFEST, archive, host)
                    validation = result["validation"]
                    self.assertEqual(result["status"], "LOCAL_RELEASE_BYTES_BOUND_DESIGNED_NOT_RUN")
                    self.assertEqual(validation["archive_sha256"], profile["sha256"])
                    self.assertEqual(validation["manifest_sha256"], self.manifest_sha)
                    self.assertTrue(validation["archive_members_match_regenerated_plan"])
                    self.assertTrue(validation["archive_payload_crc_verified"])
                    self.assertEqual(validation["case_claim_counts"]["NOT_RUN"],
                                     len(self.contracts[slug]["cases"]))
                    for key in ("host_execution_observed", "consumer_accepted",
                                "manifest_authenticity_verified", "authorization_verified",
                                "installed_or_published", "independent_oracles_verified"):
                        self.assertFalse(validation[key])
                    self.assertFalse(result["trial_execution_authorized"])
                    self.assertEqual(hashlib.sha256(result["receipt_json"].encode("utf-8")).hexdigest(),
                                     json.loads(result["ledger_json"])["receipt_sha256"])
                    ready.add(pair)
                    assets.add(profile["asset"])
        self.assertEqual(holds, set(m.source.compat.AUTHORED_HOLD_EXCEPTIONS))
        self.assertEqual(ready | holds, {(slug, host) for slug in registered for host in m.source.compat.HOSTS})
        self.assertEqual({p.name for p in DIRECTORY.iterdir()}, assets)
        print(f"Actual built archives: {len(assets)-1}; bound ready pairs: {len(ready)}; documented holds: {len(holds)}; native runs: 0")

    def test_forged_manifest_digest_cannot_hide_changed_archive_member(self):
        slug = "scheduled-work-proof-auditor"
        host = "github-copilot"
        package = ROOT / "skills/authored" / slug
        manifest = copy.deepcopy(self.manifest)
        row = next(r for r in manifest["skills"] if r["id"] == slug)
        profile = row["hosts"][host]
        source_archive = DIRECTORY / profile["asset"]
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            archive = folder / profile["asset"]
            with zipfile.ZipFile(source_archive) as original, zipfile.ZipFile(archive, "w") as altered:
                for member in original.infolist():
                    data = original.read(member)
                    if member.filename == slug + "/SKILL.md":
                        data += b"\nFictional tamper negative control.\n"
                    altered.writestr(member, data)
            profile["sha256"] = hashlib.sha256(archive.read_bytes()).hexdigest()
            path = folder / MANIFEST.name
            path.write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "^PLAN_ARCHIVE_MEMBER_DIGEST_MISMATCH$"):
                m.prepare(self.contracts[slug], package, path, archive, host)

    def test_actual_manifest_cannot_be_replaced_by_wrong_skill_or_host(self):
        slug = "scheduled-work-proof-auditor"
        package = ROOT / "skills/authored" / slug
        wrong = DIRECTORY / "ci-guard.zip"
        with self.assertRaisesRegex(ValueError, "^ARCHIVE_NAME_MISMATCH$"):
            m.prepare(self.contracts[slug], package, MANIFEST, wrong, "github-copilot")
        wrong = DIRECTORY / (slug + ".zip")
        with self.assertRaisesRegex(ValueError, "^ARCHIVE_NAME_MISMATCH$"):
            m.prepare(self.contracts[slug], package, MANIFEST, wrong, "gemini-apps")


if __name__ == "__main__":
    unittest.main(verbosity=2)
