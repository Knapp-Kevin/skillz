#!/usr/bin/env python3
"""Verify every uploaded draft asset against the locally built bytes."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest


def verify(directory, assets, read_asset):
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
    if seen != set(expected):
        raise ValueError("release asset inventory incomplete")
    print(f"Verified actual draft bytes for {len(seen)} assets")


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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--directory", type=Path)
    parser.add_argument("--repo")
    parser.add_argument("--tag")
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReadbackTests)
        if not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful():
            raise SystemExit(1)
        return
    if not all((args.directory, args.repo, args.tag)):
        parser.error("--directory, --repo and --tag are required")
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
