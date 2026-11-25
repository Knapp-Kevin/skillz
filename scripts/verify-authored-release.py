#!/usr/bin/env python3
"""Verify every uploaded draft asset against the locally built bytes."""
import argparse
import hashlib
import json
import re
from pathlib import Path
import subprocess
import tempfile
import unittest


def verify(directory, assets, read_asset, allow_missing=False):
    expected = {p.name: p for p in directory.iterdir()}
    if not expected or any(p.is_symlink() or not p.is_file() for p in expected.values()):
        raise ValueError("invalid local asset inventory")
    seen = set()
    ids = set()
    for asset in assets:
        name = asset["name"]
        aid = asset["id"]
        if name not in expected or name in seen or type(aid) is not int or aid <= 0 or aid in ids:
            raise ValueError("unexpected or duplicate release asset")
        seen.add(name)
        ids.add(aid)
        path = expected[name]
        if asset["state"] != "uploaded" or asset["size"] != path.stat().st_size:
            raise ValueError("release asset state or size mismatch")
        local = path.read_bytes()
        remote = read_asset(aid)
        if local != remote:
            raise ValueError("release asset byte mismatch: " + name)
        print(f"Verified {name}: {hashlib.sha256(remote).hexdigest()}")
    missing = sorted(set(expected) - seen)
    if missing and not allow_missing:
        raise ValueError("release asset inventory incomplete")
    print(f"Verified actual remote bytes for {len(seen)} assets")
    return missing


def gh_command(*args, timeout=60):
    return subprocess.check_output(["gh", *args], timeout=timeout)


def find_release(gh, repo, tag, commit):
    pages = json.loads(gh("api", "--paginate", "--slurp",
                          f"repos/{repo}/releases?per_page=100"))
    matches = [row for page in pages for row in page if row["tag_name"] == tag]
    if len(matches) > 1:
        raise ValueError("duplicate release tag")
    if not matches:
        return None
    release = matches[0]
    if (type(release["id"]) is not int or release["id"] <= 0 or
            type(release["draft"]) is not bool or release["prerelease"] is not False or
            release["target_commitish"] != commit):
        raise ValueError("release identity, target or state mismatch")
    return release


def release_assets(gh, repo, rid):
    pages = json.loads(gh("api", "--paginate", "--slurp",
                          f"repos/{repo}/releases/{rid}/assets?per_page=100"))
    return [asset for page in pages for asset in page]


def prepare_snapshot(directory, repo, tag, commit, gh=gh_command):
    """Create or resume only the exact source-bound release, never clobber assets."""
    if not re.fullmatch(r"[0-9a-f]{40}", commit) or tag != "authored-" + commit:
        raise ValueError("invalid source-bound release tag")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise ValueError("invalid repository name")
    # Validate the local inventory before performing any remote write.
    verify(directory, [], lambda _: None, allow_missing=True)
    release = find_release(gh, repo, tag, commit)
    if release is None:
        gh("release", "create", tag, "--repo", repo, "--target", commit,
           "--draft", "--title", f"Authored skill downloads ({commit})",
           "--notes", "Original MIT skill packages, source-pinned manifest and SHA-256 hashes. Static packaging only; no host installation or behavior claim.")
        release = find_release(gh, repo, tag, commit)
        if release is None or release["draft"] is not True:
            raise ValueError("new draft release not observed")
    rid = release["id"]

    def read_asset(aid):
        return gh("api", "-H", "Accept: application/octet-stream",
                  f"repos/{repo}/releases/assets/{aid}", timeout=30)

    missing = verify(directory, release_assets(gh, repo, rid), read_asset,
                     allow_missing=release["draft"])
    if missing:
        # Never delete, replace, or upload to a previously published release.
        current = find_release(gh, repo, tag, commit)
        if current is None or current["id"] != rid or current["draft"] is not True:
            raise ValueError("draft state changed before resume")
        gh("release", "upload", tag, "--repo", repo,
           *(str(directory / name) for name in missing), timeout=180)
        current = find_release(gh, repo, tag, commit)
        if current is None or current["id"] != rid or current["draft"] is not True:
            raise ValueError("draft state changed during resume")
        verify(directory, release_assets(gh, repo, rid), read_asset)
    current = find_release(gh, repo, tag, commit)
    if current is None or current["id"] != rid or current["draft"] != release["draft"]:
        raise ValueError("release state changed during verification")
    print("Verified existing published snapshot" if not current["draft"] else
          "Verified complete draft snapshot")
    return current["draft"]


class ReadbackTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.directory = Path(self.tmp.name)
        (self.directory / "a.zip").write_bytes(b"abc")
        (self.directory / "manifest.json").write_bytes(b"{}")
        self.assets = [
            {"name": "a.zip", "id": 1, "state": "uploaded", "size": 3},
            {"name": "manifest.json", "id": 2, "state": "uploaded", "size": 2},
        ]
        self.remote = {1: b"abc", 2: b"{}"}

    def check(self):
        verify(self.directory, self.assets, self.remote.__getitem__)

    def test_identical(self):
        self.check()

    def test_same_size_corruption(self):
        self.remote[1] = b"xyz"
        with self.assertRaises(ValueError):
            self.check()

    def test_missing(self):
        self.assets.pop()
        with self.assertRaises(ValueError):
            self.check()

    def test_duplicate_name(self):
        self.assets.append(self.assets[0].copy())
        with self.assertRaises(ValueError):
            self.check()

    def test_duplicate_id(self):
        self.assets[1]["id"] = 1
        with self.assertRaises(ValueError):
            self.check()

    def test_extra(self):
        self.assets.append({"name": "../outside", "id": 3, "state": "uploaded", "size": 0})
        with self.assertRaises(ValueError):
            self.check()

    def test_upload_incomplete(self):
        self.assets[0]["state"] = "starter"
        with self.assertRaises(ValueError):
            self.check()

    def test_readback_failure(self):
        del self.remote[1]
        with self.assertRaises(KeyError):
            self.check()


class ResumeTests(unittest.TestCase):
    def setUp(self):
        ReadbackTests.setUp(self)
        self.repo = "fictional/repo"
        self.commit = "a" * 40
        self.tag = "authored-" + self.commit
        self.release = {"id": 10, "tag_name": self.tag, "draft": True,
                        "prerelease": False, "target_commitish": self.commit}
        self.releases = [self.release]
        self.calls = []

    def gh(self, *args, timeout=60):
        self.calls.append(args)
        if args[:3] == ("api", "--paginate", "--slurp"):
            if args[3].endswith("/releases?per_page=100"):
                return json.dumps([self.releases]).encode()
            if args[3].endswith("/releases/10/assets?per_page=100"):
                return json.dumps([self.assets]).encode()
        if args[:3] == ("api", "-H", "Accept: application/octet-stream"):
            return self.remote[int(args[3].split("/")[-1])]
        if args[:2] == ("release", "create"):
            self.releases.append(self.release)
            return b"created"
        if args[:2] == ("release", "upload"):
            if not self.release["draft"] or "--clobber" in args:
                raise AssertionError("unsafe write")
            for raw in args[5:]:
                p = Path(raw)
                if any(a["name"] == p.name for a in self.assets):
                    raise AssertionError("asset overwrite")
                aid = max(self.remote, default=0) + 1
                self.remote[aid] = p.read_bytes()
                self.assets.append({"name": p.name, "id": aid, "state": "uploaded",
                                    "size": p.stat().st_size})
            return b"uploaded"
        raise AssertionError(args)

    def prepare(self):
        return prepare_snapshot(self.directory, self.repo, self.tag, self.commit, self.gh)

    def writes(self):
        return [call for call in self.calls if call[0] == "release"]

    def test_new_snapshot_creates_draft_and_uploads_complete_inventory(self):
        self.releases.clear()
        self.assets.clear()
        self.remote.clear()
        self.assertTrue(self.prepare())
        self.assertEqual([call[1] for call in self.writes()], ["create", "upload"])
        self.assertEqual({a["name"] for a in self.assets}, {"a.zip", "manifest.json"})

    def test_partial_draft_resumes_only_missing_asset(self):
        self.assets.pop()
        self.assertTrue(self.prepare())
        self.assertEqual(len(self.writes()), 1)
        self.assertEqual(Path(self.writes()[0][-1]).name, "manifest.json")

    def test_complete_draft_needs_no_write(self):
        self.assertTrue(self.prepare())
        self.assertEqual(self.writes(), [])

    def test_existing_published_release_is_read_only(self):
        self.release["draft"] = False
        self.assertFalse(self.prepare())
        self.assertEqual(self.writes(), [])

    def test_incomplete_published_release_cannot_be_repaired(self):
        self.release["draft"] = False
        self.assets.pop()
        with self.assertRaises(ValueError):
            self.prepare()
        self.assertEqual(self.writes(), [])

    def test_corrupt_draft_cannot_be_clobbered(self):
        self.remote[1] = b"xyz"
        self.assets.pop()
        with self.assertRaises(ValueError):
            self.prepare()
        self.assertEqual(self.writes(), [])

    def test_wrong_target_or_duplicate_release_blocks_all_writes(self):
        self.release["target_commitish"] = "b" * 40
        with self.assertRaises(ValueError):
            self.prepare()
        self.release["target_commitish"] = self.commit
        self.releases.append(dict(self.release, id=11))
        with self.assertRaises(ValueError):
            self.prepare()
        self.assertEqual(self.writes(), [])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--directory", type=Path)
    parser.add_argument("--repo")
    parser.add_argument("--tag")
    parser.add_argument("--prepare", action="store_true", help="Create or resume the exact draft; never promote")
    parser.add_argument("--commit")
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromTestCase(cls)
                                   for cls in (ReadbackTests, ResumeTests))
        if not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful():
            raise SystemExit(1)
        return
    if not all((args.directory, args.repo, args.tag)):
        parser.error("--directory, --repo and --tag are required")
    if args.prepare:
        if not args.commit:
            parser.error("--prepare requires --commit")
        prepare_snapshot(args.directory, args.repo, args.tag, args.commit)
        return
    release = json.loads(subprocess.check_output([
        "gh", "release", "view", args.tag, "--repo", args.repo,
        "--json", "databaseId,isDraft,tagName"
    ], timeout=30))
    if not release["isDraft"] or release["tagName"] != args.tag:
        raise ValueError("release is not the expected draft")
    rid = release["databaseId"]
    if type(rid) is not int or rid <= 0:
        raise ValueError("invalid release identity")
    pages = json.loads(subprocess.check_output([
        "gh", "api", "--paginate", "--slurp",
        f"repos/{args.repo}/releases/{rid}/assets?per_page=100"
    ], timeout=60))
    assets = [asset for page in pages for asset in page]

    def read_asset(aid):
        return subprocess.check_output([
            "gh", "api", "-H", "Accept: application/octet-stream",
            f"repos/{args.repo}/releases/assets/{aid}"
        ], timeout=30)

    verify(args.directory, assets, read_asset)


if __name__ == "__main__":
    main()
