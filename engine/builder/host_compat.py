#!/usr/bin/env python3
"""Offline host package preflight for the existing Skillz builder and corpus.

A structural PASS is not an installed, loaded, executed, or user-accepted skill.
Source content is untrusted; do not execute scripts during inspection.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[2]
AUTHORED = ROOT / "skills" / "authored"
MAX_ENTRYPOINT = 20000
MICROSOFT_EXTENSIONS = frozenset((
    ".json .xml .yaml .yml .ini .config .utf8 .docx .doc .docm "
    ".pdf .txt .rtf .md .ppt .pptx .ppsm .xlsx .xls .xlsm .csv .tsv "
    ".html .htm .png .jpg .jpeg .gif .bmp .log "
    ".py .js .mjs .cjs .ts .mts .sh .bash"
).split())
SCRIPT_EXTENSIONS = frozenset((".py", ".js", ".mjs", ".cjs", ".ts", ".mts", ".sh", ".bash"))
# Profile paths are *target examples*, not a claim of local host installation.
HOSTS = {
    "github-copilot": dict(mode="directory", destination=".github/skills/<skill>/"),
    "claude-code": dict(mode="directory", destination=".claude/skills/<skill>/"),
    "openai-codex": dict(mode="directory", destination=".agents/skills/<skill>/"),
    "gemini-cli": dict(mode="directory", destination=".gemini/skills/<skill>/"),
    "hermes-agent": dict(mode="directory", destination="~/.hermes/skills/<skill>/"),
    "m365-copilot-chat": dict(mode="zip", destination="Copilot Chat > Agents > More agents > Add > Upload skill",
                             advisory_char_limit=MAX_ENTRYPOINT, extensions=MICROSOFT_EXTENSIONS),
    "m365-agent-builder": dict(mode="zip", destination="Agent Builder > Skills > Upload ZIP",
                              strict_char_limit=MAX_ENTRYPOINT, extensions=MICROSOFT_EXTENSIONS,
                              max_files=350, max_depth=3, max_file_bytes=25*1024*1024,
                              max_package_bytes=50*1024*1024),
    "m365-agents-toolkit": dict(mode="directory", destination="appPackage/skills/<skill>/",
                               strict_char_limit=MAX_ENTRYPOINT, extensions=MICROSOFT_EXTENSIONS,
                               max_files=350, max_depth=3, max_package_bytes=10*1024*1024),
}
NAME = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
MARKDOWN_LINK = re.compile(r"\]\(([^)\n]+)\)")


def source_files(folder):
    if not folder.is_dir() or folder.is_symlink():
        raise ValueError("SKILL_DIRECTORY_MISSING_OR_SYMLINKED")
    children = sorted(folder.rglob("*"))
    if any(p.is_symlink() or not (p.is_file() or p.is_dir()) for p in children):
        raise ValueError("SYMLINK_OR_SPECIAL_FILE")
    found = [p for p in children if p.is_file()]
    if not found or not (folder / "SKILL.md").is_file():
        raise ValueError("SKILL_MD_MISSING")
    return found


def read_entrypoint(folder):
    instructions = (folder / "SKILL.md").read_text(encoding="utf-8")
    header = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", instructions, re.S)
    if not header:
        raise ValueError("YAML_FRONTMATTER_MISSING")
    name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", header.group(1))
    desc = re.search(r"(?m)^description:\s*(?:\S|[>|])", header.group(1))
    if not name or not NAME.fullmatch(name.group(1)) or name.group(1) != folder.name:
        raise ValueError("SKILL_NAME_MISMATCH")
    if len(folder.name) > 64 or not desc:
        raise ValueError("INVALID_NAME_OR_DESCRIPTION")
    return instructions


def package_name(source, profile):
    """Microsoft accepts LICENSE.txt but not extensionless LICENSE."""
    if source == "LICENSE" and "extensions" in profile:
        return "LICENSE.txt"
    return source


def inspect(folder, host):
    if host not in HOSTS:
        raise ValueError("UNKNOWN_HOST")
    profile = HOSTS[host]
    result = dict(
        host=host, skill=folder.name, target=profile["destination"],
        package_mode=profile["mode"], format_valid=False, package_ready=False,
        blockers=[], warnings=[], host_loaded="NOT_TESTED",
        behavior_tested="NOT_TESTED", consumer_accepted="NOT_TESTED",
    )
    try:
        files = source_files(folder)
        entrypoint = read_entrypoint(folder)
    except (OSError, UnicodeError, ValueError) as exc:
        result["blockers"].append(str(exc))
        return result
    result["format_valid"] = True
    src_names = [f.relative_to(folder).as_posix() for f in files]
    dst_names = [package_name(p, profile) for p in src_names]
    blockers, warnings = [], []
    if len(set(dst_names)) != len(dst_names):
        blockers.append("TRANSFORMED_NAME_COLLISION")
    length = len(entrypoint)
    if length >= profile.get("strict_char_limit", float("inf")):
        blockers.append("SKILL_MD_OVER_HOST_HARD_LIMIT")
    if length >= profile.get("advisory_char_limit", float("inf")):
        warnings.append("SKILL_MD_OVER_HOST_RECOMMENDATION")
    if len(files) > profile.get("max_files", float("inf")):
        blockers.append("MAX_FILES_EXCEEDED")
    total = sum(f.stat().st_size for f in files)
    if total > profile.get("max_package_bytes", float("inf")):
        blockers.append("MAX_PACKAGE_BYTES_EXCEEDED")
    source_names = set(src_names)
    for f, src, dst in zip(files, src_names, dst_names):
        if len(Path(dst).parts) - 1 > profile.get("max_depth", float("inf")):
            blockers.append("MAX_DEPTH:" + dst)
        if f.stat().st_size > profile.get("max_file_bytes", float("inf")):
            blockers.append("MAX_FILE_BYTES:" + dst)
        if "extensions" in profile and Path(dst).suffix.lower() not in profile["extensions"]:
            blockers.append("UNSUPPORTED_EXTENSION:" + dst)
        if Path(src).suffix.lower() in SCRIPT_EXTENSIONS:
            warnings.append("SCRIPT_RUNTIME_AND_PERMISSIONS_REQUIRE_HOST_TEST")
        if f.suffix.lower() != ".md":
            continue
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeError:
            blockers.append("INVALID_UTF8_MARKDOWN:" + src)
            continue
        for raw in MARKDOWN_LINK.findall(text):
            link = raw.split("#", 1)[0].strip()
            if not link or link.startswith(("https://", "http://", "mailto:", "data:")):
                continue
            if link.startswith("/") or "://" in link:
                blockers.append("NONPORTABLE_LOCAL_LINK:" + src)
                continue
            resolved = (f.parent / link).resolve()
            if not resolved.is_relative_to(folder.resolve()) or not resolved.is_file():
                blockers.append("BROKEN_LOCAL_LINK:" + src + ":" + link)
                continue
            referent = resolved.relative_to(folder).as_posix()
            if referent not in source_names:
                blockers.append("LINKED_RESOURCE_NOT_IN_PACKAGE:" + src)
            if package_name(referent, profile) != referent:
                blockers.append("TRANSFORM_REQUIRES_LINK_REWRITE:" + src)
    result["blockers"] = sorted(set(blockers))
    result["warnings"] = sorted(set(warnings))
    result["package_ready"] = not blockers
    result["source_sha256"] = hashlib.sha256((folder / "SKILL.md").read_bytes()).hexdigest()
    result["entrypoint_characters"] = length
    result["file_count"] = len(files)
    result["package_bytes"] = total
    result["manifest"] = [
        {"source": s, "output": d, "sha256": hashlib.sha256(f.read_bytes()).hexdigest()}
        for f, s, d in zip(files, src_names, dst_names)
    ]
    return result


def write_zip(folder, host, output, receipt):
    if HOSTS[host]["mode"] != "zip" or not receipt["package_ready"]:
        raise ValueError("ZIP_REQUIRES_PACKAGE_READY_ZIP_HOST")
    destination = Path(output).expanduser().absolute()
    if destination.suffix.lower() != ".zip" or destination.exists() or destination.is_symlink():
        raise ValueError("ZIP_DESTINATION_MUST_BE_NEW_ZIP")
    if not destination.parent.is_dir() or destination.parent.is_symlink():
        raise ValueError("ZIP_PARENT_MISSING_OR_SYMLINKED")
    # zip entries are rooted at SKILL.md, NOT nested under skill-name/.
    with destination.open("xb") as fd:
        with zipfile.ZipFile(fd, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
            for row in receipt["manifest"]:
                archive.write(folder / row["source"], arcname=row["output"])
    with zipfile.ZipFile(destination) as archive:
        actual = sorted(archive.namelist())
        expected = sorted(row["output"] for row in receipt["manifest"])
        if actual != expected or archive.testzip() is not None:
            destination.unlink()
            raise ValueError("ZIP_READBACK_FAILED")
    receipt["artifact"] = str(destination)
    receipt["artifact_status"] = "CREATED_NOT_UPLOADED"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--skill", help="First-party authored skill slug")
    choice.add_argument("--all", action="store_true", help="Audit every authored package")
    parser.add_argument("--host", choices=sorted(HOSTS), help="Default: all host profiles")
    parser.add_argument("--zip-output", help="Explicit NEW ZIP output, single skill and ZIP host only")
    args = parser.parse_args(argv)
    if args.zip_output and (args.all or not args.host or HOSTS[args.host]["mode"] != "zip"):
        parser.error("--zip-output requires --skill and a ZIP-based --host")
    packages = (
        sorted(p for p in AUTHORED.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
        if args.all else [AUTHORED / args.skill]
    )
    results = [inspect(p, h) for p in packages for h in ([args.host] if args.host else HOSTS)]
    if args.zip_output:
        write_zip(packages[0], args.host, args.zip_output, results[0])
    summary = {h: {
        "ready": sum(r["package_ready"] for r in results if r["host"] == h),
        "hold": sum(not r["package_ready"] for r in results if r["host"] == h),
    } for h in ([args.host] if args.host else HOSTS)}
    print(json.dumps({
        "schema_version": 1, "claim": "STATIC_PACKAGE_PREFLIGHT_ONLY",
        "canonical_skill_count": len(packages),
        "host_qualification": "NOT_TESTED",
        "summary": summary, "results": results,
    }, indent=2))
    return 0 if all(r["package_ready"] for r in results) else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print("HOST_PACKAGE_HOLD: " + str(error), file=sys.stderr)
        raise SystemExit(2)
