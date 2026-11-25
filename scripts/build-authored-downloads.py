#!/usr/bin/env python3
"""Maintainer-only release artifact builder. No network, install or skill execution."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "engine" / "builder"))
import host_compat

# Share the same assessed/unassessed boundary as the authoring engine.
MANUAL_HOSTS = host_compat.UNASSESSED_HOSTS

def add_manual_host_statuses(hosts):
    if set(hosts) & MANUAL_HOSTS.keys():
        raise ValueError("manual host status would overwrite a checked profile")
    hosts.update(host_compat.unassessed_host_statuses())

class ManualHostTests(unittest.TestCase):
    def test_unassessed_routes_fail_closed(self):
        hosts = {}
        add_manual_host_statuses(hosts)
        self.assertEqual(set(hosts), {"chatgpt", "openclaude-other"})
        for row in hosts.values():
            self.assertEqual(row["status"], "HOLD")
            self.assertIsNone(row["asset"])
            self.assertIsNone(row["sha256"])
            self.assertTrue(row["blockers"])
            self.assertEqual(row["behavior"], "NOT_TESTED")

    def test_checked_profile_preserved(self):
        row = {"status": "PACKAGE_READY"}
        hosts = {"claude-code": row}
        add_manual_host_statuses(hosts)
        self.assertIs(hosts["claude-code"], row)

    def test_collision_never_overwrites(self):
        hosts = {"chatgpt": {"status": "PACKAGE_READY"}}
        with self.assertRaises(ValueError):
            add_manual_host_statuses(hosts)
        self.assertEqual(hosts, {"chatgpt": {"status": "PACKAGE_READY"}})

def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def blob_tree(commit, prefix):
    raw = git("ls-tree", "-r", "-z", commit, "--", prefix + "/")
    result = {}
    for item in raw.split(b"\0"):
        if not item:
            continue
        meta, name = item.split(b"\t", 1)
        mode, kind, oid = meta.decode("ascii").split()
        path = name.decode("utf-8")
        if not path.startswith(prefix + "/") or kind != "blob" or mode not in {"100644", "100755"}:
            raise ValueError("unsafe package member")
        rel = path[len(prefix)+1:]
        p = PurePosixPath(rel)
        if p.is_absolute() or ".." in p.parts or "\\" in rel or any(x.startswith(".") for x in p.parts):
            raise ValueError("unsafe package path")
        result[rel] = (mode, git("cat-file", "blob", oid))
    return result

def build(output):
    commit = git("rev-parse", "HEAD").decode().strip()
    if git("status", "--porcelain", "--untracked-files=no").strip():
        raise ValueError("tracked checkout differs from commit")
    output = output.absolute()
    if output.exists() or output.is_relative_to(ROOT) or any(p.is_symlink() for p in output.parents):
        raise ValueError("output must be new and outside repository")
    index = json.loads(git("show", commit + ":registry/authored-skills-index.json"))
    rows = index["skills"]
    ids = [r["id"] for r in rows]
    disk = {p.name for p in host_compat.AUTHORED.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}
    if len(ids) != len(set(ids)) or set(ids) != disk:
        raise ValueError("authored package index mismatch")
    output.mkdir()
    manifest = {"schema_version": 1, "source_commit": commit,
                "claim": "AUTHORED_SOURCE_ARCHIVES_ONLY_HOST_BEHAVIOR_NOT_TESTED", "skills": []}
    for row in sorted(rows, key=lambda r:r["id"]):
        slug = row["id"]
        prefix = "skills/authored/" + slug
        if not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", slug) or row["source_class"] != "first-party-authored" or row["license_spdx"] != "MIT" or row["package_path"] != prefix or row["entrypoint"] != prefix + "/SKILL.md" or row["license_file"] != prefix + "/LICENSE":
            raise ValueError("noncanonical or unlicensed package")
        tree = git("rev-parse", commit + ":" + prefix).decode().strip()
        blob = git("rev-parse", commit + ":" + prefix + "/SKILL.md").decode().strip()
        if tree != row["package_tree_sha"] or blob != row["skill_blob_sha"]:
            raise ValueError("stale package identity: " + slug)
        files = blob_tree(commit, prefix)
        if len(files) != row["package_file_count"] or "SKILL.md" not in files or "LICENSE" not in files:
            raise ValueError("incomplete package: " + slug)
        if b"Permission is hereby granted" not in files["LICENSE"][1] or b"Copyright" not in files["LICENSE"][1]:
            raise ValueError("missing MIT permission notice")
        folder = ROOT / prefix
        actual = {p.relative_to(folder).as_posix(): p for p in host_compat.source_files(folder)}
        if set(actual) != set(files) or any(actual[n].read_bytes() != b for n, (_, b) in files.items()):
            raise ValueError("checkout bytes differ: " + slug)
        archive = output / (slug + ".zip")
        with zipfile.ZipFile(archive, "x", compression=zipfile.ZIP_DEFLATED) as z:
            for name, (mode, data) in sorted(files.items()):
                info = zipfile.ZipInfo(slug + "/" + name, date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = int(mode, 8) << 16
                z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED)
        with zipfile.ZipFile(archive) as z:
            if sorted(z.namelist()) != sorted(slug + "/" + n for n in files) or z.testzip() or any(z.read(slug + "/" + n) != b for n, (_, b) in files.items()):
                raise ValueError("canonical archive readback failed")
        entry = {"id": slug, "package_tree_sha": tree, "skill_blob_sha": blob,
                 "license": "MIT", "canonical": {"asset": archive.name, "sha256": digest(archive)}, "hosts": {}}
        profiles = {h: host_compat.inspect(folder, h) for h in host_compat.HOSTS}
        admission = host_compat.authored_admission(profiles.values())
        if admission["unexpected_holds"]:
            raise ValueError("authored portability admission failed: " + json.dumps(admission["unexpected_holds"]))
        ms = profiles["m365-copilot-chat"]
        # Chat and Builder share the same adapter; toolkit consumes the extracted adapted directory.
        variant = None
        if ms["package_ready"]:
            variant = output / (slug + "-m365.zip")
            host_compat.write_zip(folder, "m365-copilot-chat", str(variant), ms)
        claude = None
        claude_report = profiles["claude-apps"]
        if claude_report["package_ready"] and any(
                member["sha256"] != member["output_sha256"] for member in claude_report["manifest"]):
            claude = output / (slug + "-claude.zip")
            host_compat.write_zip(folder, "claude-apps", str(claude), claude_report)
        gemini = None
        if profiles["gemini-apps"]["package_ready"]:
            gemini = output / (slug + "-gemini.zip")
            host_compat.write_zip(folder, "gemini-apps", str(gemini), profiles["gemini-apps"])
        for h, report in profiles.items():
            ready = report["package_ready"]
            microsoft = h.startswith("m365-")
            asset = (variant.name if variant is not None else None) if microsoft else archive.name
            if h == "claude-apps" and claude is not None:
                asset = claude.name
            if h == "gemini-apps":
                asset = gemini.name if gemini is not None else None
            if ready and asset is None:
                raise ValueError("host adapter unexpectedly unavailable")
            entry["hosts"][h] = {"status": "PACKAGE_READY" if ready else "HOLD",
                "asset": asset if ready else None, "sha256": digest(output / asset) if ready else None,
                "blockers": report["blockers"], "warnings": report["warnings"], "behavior": "NOT_TESTED"}
        add_manual_host_statuses(entry["hosts"])
        manifest["skills"].append(entry)
    (output / "authored-download-manifest.json").write_text(json.dumps(manifest, indent=2)+"\n", encoding="utf-8")
    print(f"Verified {len(rows)} canonical authored ZIPs; {len(list(output.glob('*-m365.zip')))} Microsoft variants; {len(list(output.glob('*-claude.zip')))} Claude variants; {len(list(output.glob('*-gemini.zip')))} Gemini variants; source {commit}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(ManualHostTests)
        if not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful():
            raise SystemExit(1)
    elif args.output is None:
        parser.error("--output is required unless --self-test is selected")
    else:
        build(args.output)
