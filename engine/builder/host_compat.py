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
# Google Gemini Apps upload requirements and transfer guide, checked 2026-11-25.
GEMINI_EXTENSIONS = frozenset((
    ".docx .pdf .rtf .tex .log .md .rst .txt .markdown .odt "
    ".csv .ods .xlsx .odp .pptx .jpg .png .svg .gif .heic .ico .jpeg "
    ".tif .webp .py .sh .ipynb .js .css .html .htm .json .toml .xml .yaml .yml"
).split())
SCRIPT_EXTENSIONS = frozenset((".py", ".js", ".mjs", ".cjs", ".ts", ".mts", ".sh", ".bash"))
# Profile paths are *target examples*, not a claim of local host installation.
HOSTS = {
    "github-copilot": dict(mode="directory", destination=".github/skills/<skill>/"),
    "claude-code": dict(mode="directory", destination=".claude/skills/<skill>/"),
    "openai-codex": dict(mode="directory", destination=".agents/skills/<skill>/"),
    "gemini-cli": dict(mode="directory", destination=".gemini/skills/<skill>/"),
    "hermes-agent": dict(mode="directory", destination="~/.hermes/skills/<skill>/"),
    # Claude Help Center custom skills: folder-wrapped ZIP and 200-char description.
    "claude-apps": dict(mode="zip", destination="Claude Customize > Skills > Upload",
                        folder_wrapped=True, description_limit=200),
    "gemini-apps": dict(mode="zip", destination="Gemini Customize > Skills > Upload",
                        extensions=GEMINI_EXTENSIONS, description_limit=1024,
                        max_files=100, max_package_bytes=100_000_000,
                        max_entrypoint_bytes=10_000_000),
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
    if (not folder.is_dir() or folder.is_symlink() or
            any(p.is_symlink() for p in folder.absolute().parents)):
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


def bounded_description(instructions):
    """Recognize plain or simple folded scalar; unsupported YAML stays on HOLD."""
    header = instructions.splitlines()[1:]
    header = header[:header.index("---")] if "---" in header else []
    matches = [i for i, line in enumerate(header) if line.startswith("description:")]
    if len(matches) != 1:
        return None
    i = matches[0]
    value = header[i].split(":", 1)[1].strip()
    following = []
    for line in header[i+1:]:
        if line and not line.startswith(" "):
            break
        following.append(line)
    if value in {">", ">-"}:
        if not following or any(not line.strip() or not line.startswith("  ") or
                                line.startswith("   ") for line in following):
            return None
        folded = " ".join(line.strip() for line in following)
        if any(ord(c) < 32 for c in folded):
            return None
        return folded + ("\n" if value == ">" else "")
    if (following or not value or value[0] in "'\\\"|>&*!{[?#@\x60" or
            ": " in value or " #" in value):
        return None
    if not any(c.isalpha() for c in value) or value.lower() in {
            "true", "false", "yes", "no", "on", "off", "null", "~"}:
        return None
    return value

def package_name(source, profile):
    """Preserve the license under a supported text extension for upload hosts."""
    if source == "LICENSE" and "extensions" in profile:
        return "LICENSE.txt"
    return source


def render_package_bytes(folder, source, profile):
    """Return host-specific bytes without changing the canonical source."""
    raw = (folder / source).read_bytes()
    if "extensions" not in profile or not source.endswith(".md"):
        return raw
    text = raw.decode("utf-8")
    def rewrite(match):
        original = match.group(1)
        link, marker, fragment = original.partition("#")
        if not link or link.startswith(("https://", "http://", "mailto:", "data:")):
            return match.group(0)
        resolved = ((folder / source).parent / link).resolve()
        if resolved == (folder / "LICENSE").resolve() and (folder / "LICENSE").is_file():
            return "](" + link + ".txt" + (marker + fragment if marker else "") + ")"
        return match.group(0)
    return MARKDOWN_LINK.sub(rewrite, text).encode("utf-8")


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
    if "description_limit" in profile:
        desc = bounded_description(entrypoint)
        if desc is None:
            blockers.append("DESCRIPTION_METADATA_NOT_ASSESSED")
        elif len(desc) > profile["description_limit"]:
            blockers.append("DESCRIPTION_OVER_HOST_LIMIT")
    if len(set(dst_names)) != len(dst_names):
        blockers.append("TRANSFORMED_NAME_COLLISION")
    # Enforce host limits on the actual transformed entrypoint, not source.
    length = len(render_package_bytes(folder, "SKILL.md", profile).decode("utf-8"))
    if len(render_package_bytes(folder, "SKILL.md", profile)) > profile.get("max_entrypoint_bytes", float("inf")):
        blockers.append("SKILL_MD_OVER_HOST_BYTE_LIMIT")
    if host == "gemini-apps":
        warnings.append("NO_EXTERNAL_SCRIPT_REQUESTS_HOST_RUNTIME_NOT_TESTED")
    if length >= profile.get("strict_char_limit", float("inf")):
        blockers.append("SKILL_MD_OVER_HOST_HARD_LIMIT")
    if length >= profile.get("advisory_char_limit", float("inf")):
        warnings.append("SKILL_MD_OVER_HOST_RECOMMENDATION")
    if len(files) > profile.get("max_files", float("inf")):
        blockers.append("MAX_FILES_EXCEEDED")
    total = sum(len(render_package_bytes(folder, src, profile)) for src in src_names)
    if total > profile.get("max_package_bytes", float("inf")):
        blockers.append("MAX_PACKAGE_BYTES_EXCEEDED")
    source_names = set(src_names)
    nested = [name for name in src_names if name != "SKILL.md" and
              Path(name).name == "SKILL.md"]
    if nested:
        warnings.append("NESTED_SKILL_DISCOVERY_REQUIRES_HOST_TEST")
    for name in nested:
        try:
            n = len(render_package_bytes(folder, name, profile).decode("utf-8"))
        except UnicodeError:
            blockers.append("INVALID_UTF8_MARKDOWN:" + name)
            continue
        if n >= profile.get("strict_char_limit", float("inf")):
            blockers.append("NESTED_SKILL_MD_OVER_HOST_HARD_LIMIT:" + name)
        if n >= profile.get("advisory_char_limit", float("inf")):
            warnings.append("NESTED_SKILL_MD_OVER_HOST_RECOMMENDATION:" + name)
    for f, src, dst in zip(files, src_names, dst_names):
        if host == "gemini-apps" and any(part.startswith(".") or part == "__pycache__" for part in Path(dst).parts):
            blockers.append("HIDDEN_OR_CACHE_FILE:" + dst)
        if len(Path(dst).parts) - 1 > profile.get("max_depth", float("inf")):
            blockers.append("MAX_DEPTH:" + dst)
        if f.stat().st_size > profile.get("max_file_bytes", float("inf")):
            blockers.append("MAX_FILE_BYTES:" + dst)
        if "extensions" in profile and Path(dst).suffix.lower() not in profile["extensions"]:
            blockers.append("UNSUPPORTED_EXTENSION:" + dst)
        sensitive_name = Path(src).name.lower()
        if (sensitive_name == ".env" or sensitive_name.startswith(".env.local") or
                sensitive_name in {"id_rsa", "id_ed25519", "credentials.json", "secrets.json"} or
                sensitive_name.endswith((".pem", ".p12", ".pfx", ".key"))):
            blockers.append("POTENTIALLY_SENSITIVE_FILE:" + src)
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
            if not resolved.is_relative_to(folder.resolve()) or not resolved.exists():
                blockers.append("BROKEN_LOCAL_LINK:" + src + ":" + link)
                continue
            if resolved.is_dir():
                if not any(p.is_relative_to(resolved) for p in files):
                    blockers.append("EMPTY_LINKED_DIRECTORY:" + src + ":" + link)
                continue
            if not resolved.is_file():
                blockers.append("BROKEN_LOCAL_LINK:" + src + ":" + link)
                continue
            referent = resolved.relative_to(folder).as_posix()
            if referent not in source_names:
                blockers.append("LINKED_RESOURCE_NOT_IN_PACKAGE:" + src)
            if package_name(referent, profile) != referent:
                if referent == "LICENSE":
                    warnings.append("LOSSLESS_LICENSE_LINK_REWRITE_FOR_HOST")
                else:
                    blockers.append("TRANSFORM_REQUIRES_LINK_REWRITE:" + src)
    result["blockers"] = sorted(set(blockers))
    result["warnings"] = sorted(set(warnings))
    result["package_ready"] = not blockers
    result["source_sha256"] = hashlib.sha256((folder / "SKILL.md").read_bytes()).hexdigest()
    result["entrypoint_characters"] = length
    result["file_count"] = len(files)
    result["package_bytes"] = total
    result["manifest"] = [
        {"source": src, "output": dst,
         "sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
         "output_sha256": hashlib.sha256(render_package_bytes(folder, src, profile)).hexdigest()}
        for f, src, dst in zip(files, src_names, dst_names)
    ]
    return result


def write_zip(folder, host, output, receipt):
    if HOSTS[host]["mode"] != "zip" or not receipt["package_ready"]:
        raise ValueError("ZIP_REQUIRES_PACKAGE_READY_ZIP_HOST")
    destination = Path(output).expanduser().absolute()
    if destination.suffix.lower() != ".zip" or destination.exists() or destination.is_symlink():
        raise ValueError("ZIP_DESTINATION_MUST_BE_NEW_ZIP")
    if (not destination.parent.is_dir() or
            any(p.is_symlink() for p in (destination.parent, *destination.parent.parents))):
        raise ValueError("ZIP_PARENT_MISSING_OR_SYMLINKED")
    if destination.is_relative_to(ROOT):
        raise ValueError("REPOSITORY_ZIP_WRITE_NOT_ALLOWED")
    # Refresh the exact package identity before output. A preflight report
    # is not a durable authorization for source files changed afterward.
    current = inspect(folder, host)
    if not current["package_ready"] or current["manifest"] != receipt["manifest"]:
        raise ValueError("ZIP_SOURCE_CHANGED_SINCE_PREFLIGHT")
    payload = []
    for row in receipt["manifest"]:
        p = folder / row["source"]
        if p.is_symlink() or not p.is_file():
            raise ValueError("ZIP_SOURCE_FILE_INVALID")
        data = p.read_bytes()
        if hashlib.sha256(data).hexdigest() != row["sha256"]:
            raise ValueError("ZIP_SOURCE_CHANGED_DURING_READ")
        adapted = render_package_bytes(folder, row["source"], HOSTS[host])
        if hashlib.sha256(adapted).hexdigest() != row["output_sha256"]:
            raise ValueError("ZIP_ADAPTER_DIGEST_MISMATCH")
        payload.append((row["output"], adapted))
    if HOSTS[host].get("folder_wrapped"):
        payload = [(folder.name + "/" + name, data) for name, data in payload]
    # Upload layout follows the target profile; preserve every member.
    # Preloaded bytes ensure the output never silently changes after hashing.
    with destination.open("xb") as fd:
        with zipfile.ZipFile(fd, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, data in payload:
                archive.writestr(name, data)
    with zipfile.ZipFile(destination) as archive:
        expected = sorted(name for name, _ in payload)
        if (sorted(archive.namelist()) != expected or archive.testzip() is not None or
                any(archive.read(name) != data for name, data in payload)):
            destination.unlink()
            raise ValueError("ZIP_READBACK_FAILED")
    receipt["artifact"] = str(destination)
    receipt["artifact_status"] = "CREATED_NOT_UPLOADED"


def write_directory(folder, host, output, receipt):
    """Prepare an exclusive, transformed folder; NEVER install into the host."""
    if HOSTS[host]["mode"] != "directory" or not receipt["package_ready"]:
        raise ValueError("DIRECTORY_REQUIRES_READY_DIRECTORY_HOST")
    destination = Path(output).expanduser().absolute()
    if destination.exists() or destination.is_symlink() or destination.is_relative_to(ROOT):
        raise ValueError("DIRECTORY_DESTINATION_MUST_BE_NEW_OUTSIDE_REPO")
    if (not destination.parent.is_dir() or
            any(p.is_symlink() for p in (destination.parent, *destination.parent.parents))):
        raise ValueError("DIRECTORY_PARENT_MISSING_OR_SYMLINKED")
    current = inspect(folder, host)
    if not current["package_ready"] or current["manifest"] != receipt["manifest"]:
        raise ValueError("DIRECTORY_SOURCE_CHANGED_SINCE_PREFLIGHT")
    payload = []
    for row in receipt["manifest"]:
        p = folder / row["source"]
        if p.is_symlink() or not p.is_file():
            raise ValueError("DIRECTORY_SOURCE_FILE_INVALID")
        raw = p.read_bytes()
        if hashlib.sha256(raw).hexdigest() != row["sha256"]:
            raise ValueError("DIRECTORY_SOURCE_CHANGED_DURING_READ")
        data = render_package_bytes(folder, row["source"], HOSTS[host])
        if hashlib.sha256(data).hexdigest() != row["output_sha256"]:
            raise ValueError("DIRECTORY_ADAPTER_DIGEST_MISMATCH")
        payload.append((row["output"], data))
    # Exclusive new handoff folder; a failed mid-copy operation leaves a
    # partial candidate, never an installed or completed skill.
    destination.mkdir(mode=0o700)
    for name, data in payload:
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as fd:
            fd.write(data)
    for name, data in payload:
        if (destination / name).read_bytes() != data:
            raise ValueError("DIRECTORY_READBACK_FAILED")
    receipt["artifact"] = str(destination)
    receipt["artifact_status"] = "PREPARED_NOT_INSTALLED"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--skill", help="First-party authored skill slug")
    choice.add_argument("--all", action="store_true", help="Audit every authored package")
    choice.add_argument("--package", help="Explicit user-authorized custom package directory; no discovery")
    parser.add_argument("--host", choices=sorted(HOSTS), help="Default: all host profiles")
    parser.add_argument("--zip-output", help="Explicit NEW ZIP output, single skill and ZIP host only")
    parser.add_argument("--directory-output", help="Explicit NEW handoff directory, not host installation")
    args = parser.parse_args(argv)
    if args.skill and (not NAME.fullmatch(args.skill) or len(args.skill) > 64):
        raise ValueError("INVALID_SKILL_SLUG")
    if args.zip_output and args.directory_output:
        parser.error("Choose only one output artifact")
    if args.zip_output and (args.all or not args.host or HOSTS[args.host]["mode"] != "zip"):
        parser.error("--zip-output requires --skill or --package and a ZIP-based --host")
    if args.directory_output and (args.all or not args.host or HOSTS[args.host]["mode"] != "directory"):
        parser.error("--directory-output requires --skill or --package and a directory-based --host")
    packages = (
        sorted(p for p in AUTHORED.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
        if args.all else [Path(args.package).expanduser().absolute() if args.package
                          else AUTHORED / args.skill]
    )
    results = [inspect(p, h) for p in packages for h in ([args.host] if args.host else HOSTS)]
    if args.zip_output:
        write_zip(packages[0], args.host, args.zip_output, results[0])
    if args.directory_output:
        write_directory(packages[0], args.host, args.directory_output, results[0])
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
