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
import unicodedata
import zipfile

ROOT = Path(__file__).resolve().parents[2]
AUTHORED = ROOT / "skills" / "authored"
MAX_ENTRYPOINT = 20000
MAX_SKILL_NAME = 64
BASE_DESCRIPTION_LIMIT = 1024
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
                        folder_wrapped=True, description_limit=200, curated_discovery=True),
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
# These are documented routes, not assessed package profiles. Keep them visible
# in all receipts and release manifests without inventing host requirements.
UNASSESSED_HOSTS = {
    "chatgpt": "HOST_UPLOAD_PROFILE_NOT_ASSESSED",
    "openclaude-other": "EXACT_HOST_IDENTITY_NOT_ESTABLISHED",
}

# Narrow existing exception: functional PowerShell dependencies are essential
# to the Windows Hyper-V skill. No wildcard, new skill or additional blocker
# is covered. Changing this policy requires explicit maintainer review.
HYPERV_REQUIRED_FILES = frozenset({
    "UNSUPPORTED_EXTENSION:scripts/Connect-QualVm.ps1",
    "UNSUPPORTED_EXTENSION:scripts/New-OfflineQualVm.ps1",
    "UNSUPPORTED_EXTENSION:tests/fake/Hyper-V/Hyper-V.psm1",
    "UNSUPPORTED_EXTENSION:tests/test_synthetic_host.ps1",
})
AUTHORED_HOLD_EXCEPTIONS = {
    ("offline-hyperv-qual-vm", host): HYPERV_REQUIRED_FILES
    for host in ("gemini-apps", "m365-copilot-chat", "m365-agent-builder",
                 "m365-agents-toolkit")
}


def authored_admission(reports, skills=None):
    """Classify assessed pairs; require complete coverage when skills are supplied."""
    expected, unexpected, seen = [], [], set()
    for report in reports:
        pair = (report["skill"], report["host"])
        if pair in seen or pair[1] not in HOSTS:
            unexpected.append({"skill": pair[0], "host": pair[1],
                               "blockers": ["DUPLICATE_OR_UNKNOWN_MATRIX_PAIR"]})
        seen.add(pair)
        reasons = set(report["blockers"])
        if report["package_ready"]:
            if not report["format_valid"] or reasons:
                unexpected.append({"skill": pair[0], "host": pair[1],
                                   "blockers": ["CONTRADICTORY_PACKAGE_READY_RECEIPT"]})
            continue
        row = {"skill": pair[0], "host": pair[1], "blockers": sorted(reasons)}
        allowed = AUTHORED_HOLD_EXCEPTIONS.get(pair, frozenset())
        if report["format_valid"] and reasons and reasons <= allowed:
            expected.append(row)
        else:
            unexpected.append(row)
    if skills is not None:
        required = {(skill, host) for skill in skills for host in HOSTS}
        for slug in asset_namespace_conflicts(skills):
            unexpected.append({"skill": slug, "host": "distribution",
                               "blockers": ["RELEASE_ASSET_NAMESPACE_COLLISION"]})
        for skill, host in sorted(required - seen):
            unexpected.append({"skill": skill, "host": host, "blockers": ["MISSING_MATRIX_PAIR"]})
        for skill, host in sorted(seen - required):
            unexpected.append({"skill": skill, "host": host, "blockers": ["UNDECLARED_MATRIX_PAIR"]})
    return {
        "status": "HOLD_UNEXPECTED_PACKAGE_BLOCKERS" if unexpected else
                  "STATIC_ADMISSION_READY_WITH_DOCUMENTED_HOLDS" if expected else
                  "STATIC_ADMISSION_READY",
        "documented_holds": expected,
        "unexpected_holds": unexpected,
        "host_behavior": "NOT_TESTED",
    }


def portability_envelope():
    """Compute broad design bounds from the same assessed profile definitions."""
    def strictest(key, default=None):
        values = [p[key] for p in HOSTS.values() if key in p]
        if default is not None:
            values.append(default)
        return min(values) if values else None
    restrictions = [set(p["extensions"]) for p in HOSTS.values() if "extensions" in p]
    return {
        "name_max_characters": MAX_SKILL_NAME,
        "description_max_characters": strictest("description_limit", BASE_DESCRIPTION_LIMIT),
        "entrypoint_characters_exclusive": strictest("strict_char_limit"),
        "entrypoint_max_bytes": strictest("max_entrypoint_bytes"),
        "max_files": strictest("max_files"),
        "max_directory_depth": strictest("max_depth"),
        "max_uncompressed_package_bytes": strictest("max_package_bytes"),
        "max_file_bytes": strictest("max_file_bytes"),
        "shared_extensions": sorted(set.intersection(*restrictions)) if restrictions else None,
        "license_adapter": "LICENSE_TO_LICENSE_TXT_WHERE_REQUIRED",
        "scope": "STATIC_DESIGN_TARGETS_NOT_NATIVE_EXECUTION_OR_TOOL_AVAILABILITY",
    }


def unassessed_host_statuses():
    return {host: {"status": "HOLD", "asset": None, "sha256": None,
                   "blockers": [reason], "warnings": [], "behavior": "NOT_TESTED"}
            for host, reason in UNASSESSED_HOSTS.items()}


# Curated Claude Apps discovery summaries, bound to exact canonical Git blobs.
# Do not truncate, infer or silently refresh descriptions after a source change.
CLAUDE_DISCOVERY = {
    "agent-failure-boundary-analysis": (
        "40d8925b488329613289cfa056ec293485687b7e",
        "Diagnose failed, costly or drifting agent sessions from evidence and authority boundaries; identify plausible causes and testable lessons. Read-only, not incident repair or memory writes.",
    ),
    "character-motivation-interview": (
        "42d10d987e3f430bb2c17aa4e0f1b3fc0a44ad33",
        "Interview writers to deepen fictional characters, motives, choices and relationships; create a cited character card separating canon from proposals. Never overwrite canon.",
    ),
    "ci-guard": (
        "3468bea1ddd8492a9cb2593efea841194c082be7",
        "Audit, repair or optimize CI reliability, cost and workflow obligations; preserve proven safeguards and validate evidence before changing merge requirements.",
    ),
    "claim-evidence-adjudicator": (
        "8c347e81615e1bdb711267d692b57f759062a16b",
        "Adjudicate contested factual claims with falsifiable subclaims, independently identified sources, contradictions and explicit confidence. Not for publishing corrections.",
    ),
    "decision-record-steward": (
        "a1f59719466000dd76b717db0c812712e5b54a49",
        "Capture or reconcile decision records with owner authority, sourced rationale, supersession and revisit rules. Never silently create policy.",
    ),
    "decision-tradeoff-workbench": (
        "409f03db70691591bdd7cf6bbd543343bb59b8a0",
        "Compare alternatives or write decision briefs using sourced criteria, evidence, uncertainty, sensitivity and reversibility. Recommend without deciding or purchasing for the user.",
    ),
    "develop-melodic-motif": (
        "78a870045b8f8e1a18ad4f4fd64cd461a35397bb",
        "Compose or revise original melodic motifs and phrases with explicit notes, rhythmic and range constraints, variations and musical checks. No mastered audio or originality guarantee.",
    ),
    "effort-allocation-navigator": (
        "72bb115f17aa720c6d5025407a435d47b9aa0bb7",
        "Turn task dumps into dependencies, blockers, effort/payoff tradeoffs and one recommended next action plus a viable alternative. Preserve user choice and private preferences.",
    ),
    "evidence-driven-refinement-loop": (
        "cf159bfd76551698567e5b3972a7e2cb79c5335d",
        "Refine or harden actual skills, prompts, documents, code and workflows via bounded repairs, adversarial tests and regression evidence. Do not equate checklists with improvement.",
    ),
    "federated-source-catalog": (
        "86b97ccdf0db845e5061af5f00470ac44cf9435b",
        "Discover, inventory, reconcile, search and cite authorized local, cloud and repository sources using native identities, tags, freshness and permission boundaries. Read-only by default.",
    ),
    "file-lifecycle-curator": (
        "5a8dd109c88b118e6ccb6371901ba0b316de58fd",
        "Organize authorized files, classify, summarize, index, tag, deduplicate and plan reversible archives; visualize progress and maintain opt-in checkpoints. Read-only by default.",
    ),
    "first-run-experience-validator": (
        "e2d2ec6367e97dd4008488f2098b5b90b9d7b8fd",
        "Validate fresh-user onboarding against published instructions and a meaningful first outcome. Distinguish desk review, author tests, clean-host and novice evidence from green CI.",
    ),
    "healthcare-contract-forensics": (
        "6d8303ac175a5ca5bc76b895a22870f17a2a5872",
        "Audit authorized employer healthcare, PBM and benefits contracts for fees, rebates, opaque compensation, billing and audit restrictions. Not clinical advice or personal plan selection.",
    ),
    "mcp-tool-surface-auditor": (
        "12bc7486b76aec0f39584b5b2c512e56103aaa7f",
        "Compare captured backend tool registry, complete MCP tools/list and host-visible tool inventories. Locate observed differences without inventing cause, access or host support.",
    ),
    "meddpicc-opportunity-assurance": (
        "c1ab2990fa71d29283a5cba21ec012e443a48c28",
        "Review complex B2B deals with independently authored MEDDPICC-aligned evidence checks, stakeholder mapping, qualification, disconfirmation and honest forecasts. No invented odds or CRM access.",
    ),
    "metadata-taxonomy-steward": (
        "f2ff7f8c98ea78091c51e55782b43fd5faadfc5b",
        "Design, audit and evolve authorized cross-collection metadata vocabularies, tags and aliases; preserve source labels and test migrations. Read-only proposals, not single-file classification.",
    ),
    "narrative-scene-gap-audit": (
        "864417c74ff1f8a5969d4b29774b09695f685b09",
        "Audit supplied story outlines or scenes for causal gaps, missing setup/payoff, continuity, character decisions and unresolved threads. Do not rewrite or modify the manuscript.",
    ),
    "pr-integration-surgeon": (
        "bd3d30d5ed64f9e0948d88089b892763ca3bf66a",
        "Plan dependency-safe PR backlog recovery using exact-head evidence, conflicts, stale checks, review holds, stacks and postmerge proof. A snapshot grants no merge authority.",
    ),
    "recursive-refinement-trace": (
        "82820fec6f9244ecb940796b2b06f910a906940a",
        "Record and verify authorized public or synthetic skill-refinement attempts in a bounded tamper-evident tree; compare observed branches. No autonomous learning or private history capture.",
    ),
    "reference-integrity-auditor": (
        "d5acaf61f86a1c5465d91fb708b8a60b0387018d",
        "Audit authorized cross-document references, citations, paths and dependency edges for broken, stale, inaccessible or changed targets and impact. No private target leaks or writes.",
    ),
    "repository-readme-architect": (
        "fae8ef92b4c95127842f303e214caec055ea3821",
        "Create, improve or audit repository READMEs, onboarding, badges, navigation, links and evidence-backed claims. Not for changing product features, governance or releases.",
    ),
    "research-methods-appraiser": (
        "96330d08e0b4f7dc4d252b0f4d12ebb9ff112cd3",
        "Appraise scientific or technical research design, measurements, baselines and replication evidence for engineering adoption decisions. Not abstract paraphrasing.",
    ),
    "sandler-conversation-strategist": (
        "4bab4ca1f5ac1a184ed4f38bb3f87d1fb5479ed6",
        "Coach ethical Sandler-aligned buyer conversations: meeting outcomes, discovery, investment, decisions, objections and follow-through. Independent guidance, not licensed training or CRM automation.",
    ),
    "skill-trial-evidence-auditor": (
        "dbfd874c69dec19a04fc0f8d35bc7ed598275d87",
        "Audit claimed skill effectiveness using comparable paired trials, verified outcomes, trigger controls, leakage, configurations and uncertainty. Not a benchmark runner or host proof.",
    ),
    "source-debt-triage": (
        "e7a20e87ec8b5514e4eafc0658ab23b71c60b1c7",
        "Audit codebase maintenance annotations as risk-ranked evidence-bound work; distinguish actionable defects, uncertain markers and obsolete remarks. No automatic edits.",
    ),
    "technology-change-intelligence": (
        "cea048fbe0e74de7f5e508e988e6c5f077bb3a5e",
        "Deliver interest-led, evidence-grounded technology updates on models, providers, protocols, research, tools or standards. Optional portable profiles, no implied scheduling or subscriptions.",
    ),
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


def check_entrypoint_metadata(instructions, directory_name):
    """Check the supported required-field subset, not arbitrary YAML syntax."""
    header = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", instructions, re.S)
    if not header:
        raise ValueError("YAML_FRONTMATTER_MISSING")
    # A deliberately conservative top-level YAML subset. Ambiguous quoted
    # keys, explicit keys, merge keys and duplicates must not masquerade as
    # ordinary required fields. This does not certify arbitrary nested YAML.
    keys = set()
    lines = header.group(1).splitlines()
    for i, line in enumerate(lines):
        if not line.strip() or line.startswith((" ", "#")):
            continue
        match = re.fullmatch(r"([A-Za-z][A-Za-z0-9_-]*):[ \t]*(.*)", line)
        if not match or match.group(1) in keys:
            raise ValueError("AMBIGUOUS_FRONTMATTER_KEYS")
        key, value = match.groups()
        keys.add(key)
        if key == "name" and (not NAME.fullmatch(value.strip()) or
                              value.strip() != directory_name or
                              (i+1 < len(lines) and lines[i+1].startswith((" ", "\t")))):
            raise ValueError("SKILL_NAME_MISMATCH")
    if "name" not in keys or len(directory_name) > MAX_SKILL_NAME:
        raise ValueError("SKILL_NAME_MISMATCH")
    desc = bounded_description(instructions)
    if desc is None:
        raise ValueError("DESCRIPTION_METADATA_NOT_ASSESSED")
    if len(desc) > BASE_DESCRIPTION_LIMIT:
        raise ValueError("DESCRIPTION_OVER_BASE_LIMIT")


def read_entrypoint(folder):
    instructions = (folder / "SKILL.md").read_text(encoding="utf-8")
    check_entrypoint_metadata(instructions, folder.name)
    return instructions


def bounded_description(instructions):
    """Recognize plain, JSON-quoted or simple folded scalar; other YAML stays on HOLD."""
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
    if value.startswith('"'):
        # The engine emits JSON-quoted scalars, a supported YAML subset.
        # Do not interpret arbitrary YAML escapes, aliases or trailing tokens.
        if following:
            return None
        try:
            decoded = json.loads(value)
        except (ValueError, TypeError):
            return None
        if not isinstance(decoded, str) or not decoded.strip() or any(
                ord(c) < 32 or 0xD800 <= ord(c) <= 0xDFFF for c in decoded):
            return None
        return decoded
    if (following or not value or value[0] in "'\\\"|>&*!{[?#@\x60" or
            ": " in value or " #" in value):
        return None
    if not any(c.isalpha() for c in value) or value.lower() in {
            "true", "false", "yes", "no", "on", "off", "null", "~"}:
        return None
    return value

def portable_path_blockers(names):
    """Reject paths that alias or cannot be materialized on common filesystems."""
    seen, blockers = {}, set()
    reserved = {"con", "prn", "aux", "nul", "conin$", "conout$"}
    reserved.update(prefix + digit for prefix in ("com", "lpt")
                    for digit in "123456789¹²³")
    for name in names:
        parts = name.split("/")
        for i, part in enumerate(parts):
            if (not part or part.startswith(".") or part == "__pycache__" or
                    part.endswith((" ", ".")) or
                    any(ord(c) < 32 or c in '<>:"\\|?*' for c in part) or
                    part.split(".", 1)[0].rstrip().casefold() in reserved):
                blockers.add("NONPORTABLE_MEMBER_PATH:" + name)
            prefix = "/".join(parts[:i+1])
            key = unicodedata.normalize("NFC", unicodedata.normalize("NFC", prefix).casefold())
            role = "file" if i == len(parts)-1 else "directory"
            prior = seen.get(key)
            if prior is not None and prior != (prefix, role):
                blockers.add("PORTABLE_PATH_COLLISION:" + name)
            seen[key] = (prefix, role)
    return sorted(blockers)


def asset_namespace_conflicts(skills):
    """Reserve possible variant basenames so future profiles cannot shadow skills."""
    names = set(skills)
    return sorted({slug + suffix for slug in names for suffix in
                   ("-claude", "-gemini", "-m365") if slug + suffix in names})


def package_name(source, profile):
    """Preserve the license under a supported text extension for upload hosts."""
    if source == "LICENSE" and "extensions" in profile:
        return "LICENSE.txt"
    return source


def claude_discovery_bytes(folder, raw):
    """Adapt only a maintained, exact canonical entrypoint; preserve its full scope."""
    if folder.resolve().parent != AUTHORED.resolve():
        return raw
    record = CLAUDE_DISCOVERY.get(folder.name)
    if record is None:
        return raw
    expected, short = record
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw,
                        usedforsecurity=False).hexdigest()
    if blob != expected or not short.strip() or len(short) > 200:
        return raw
    original = raw.decode("utf-8")
    description = bounded_description(original)
    if description is None or len(description) <= 200:
        return raw
    if "\n---\n" not in original:
        return raw
    header, body = original.split("\n---\n", 1)
    header, count = re.subn(r"(?m)^description: >-\n(?:  [^\n]+\n)+",
                            lambda _: "description: " + json.dumps(short, ensure_ascii=False) + "\n",
                            header + "\n")
    if count != 1:
        return raw
    adapted = (header + "---\n" + body +
               "\n\n## Canonical activation scope (preserved)\n\n" + description + "\n")
    if bounded_description(adapted) != short:
        return raw
    return adapted.encode("utf-8")


def render_package_bytes(folder, source, profile):
    """Return host-specific bytes without changing the canonical source."""
    raw = (folder / source).read_bytes()
    if profile.get("curated_discovery") and source == "SKILL.md":
        return claude_discovery_bytes(folder, raw)
    if "extensions" not in profile or not source.lower().endswith(".md"):
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
    blockers = portable_path_blockers([folder.name]) + portable_path_blockers(dst_names)
    warnings = []
    for f in files:
        if f.suffix.lower() == ".md":
            try:
                f.read_text(encoding="utf-8")
            except UnicodeError:
                blockers.append("INVALID_UTF8_MARKDOWN:" + f.relative_to(folder).as_posix())
    if any(b.startswith("INVALID_UTF8_MARKDOWN:") for b in blockers):
        result["blockers"] = sorted(set(blockers))
        return result
    rendered_entrypoint = render_package_bytes(folder, "SKILL.md", profile)
    adapted_entrypoint = rendered_entrypoint.decode("utf-8")
    if profile.get("curated_discovery") and rendered_entrypoint != (folder / "SKILL.md").read_bytes():
        warnings.append("CLAUDE_DISCOVERY_DESCRIPTION_ADAPTED_CANONICAL_SCOPE_PRESERVED")
    if "description_limit" in profile:
        desc = bounded_description(adapted_entrypoint)
        if desc is None:
            blockers.append("DESCRIPTION_METADATA_NOT_ASSESSED")
        elif len(desc) > profile["description_limit"]:
            blockers.append("DESCRIPTION_OVER_HOST_LIMIT")
    if len(set(dst_names)) != len(dst_names):
        blockers.append("TRANSFORMED_NAME_COLLISION")
    # Enforce host limits on the actual transformed entrypoint, not source.
    length = len(adapted_entrypoint)
    if len(rendered_entrypoint) > profile.get("max_entrypoint_bytes", float("inf")):
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
        data = render_package_bytes(folder, name, profile)
        text = data.decode("utf-8")
        try:
            check_entrypoint_metadata(text, Path(name).parent.name)
        except ValueError as exc:
            blockers.append("NESTED_" + str(exc) + ":" + name)
        desc = bounded_description(text)
        if "description_limit" in profile and desc is not None and len(desc) > profile["description_limit"]:
            blockers.append("NESTED_DESCRIPTION_OVER_HOST_LIMIT:" + name)
        if len(data) > profile.get("max_entrypoint_bytes", float("inf")):
            blockers.append("NESTED_SKILL_MD_OVER_HOST_BYTE_LIMIT:" + name)
        n = len(text)
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
            for name, data in sorted(payload):
                # Match canonical archives' stable timestamp; do not encode
                # wall-clock time, host platform, or output path in the ZIP.
                info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o600 << 16
                archive.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED)
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
    choice.add_argument("--profiles", action="store_true", help="Read current static host constraints before authoring")
    choice.add_argument("--package", help="Explicit user-authorized custom package directory; no discovery")
    parser.add_argument("--host", choices=sorted(HOSTS), help="Default: all assessed host profiles")
    parser.add_argument("--require-authored-ready", action="store_true",
                        help="Require all assessed authored pairs except exact documented holds")
    parser.add_argument("--zip-output", help="Explicit NEW ZIP output, single skill and ZIP host only")
    parser.add_argument("--directory-output", help="Explicit NEW handoff directory, not host installation")
    args = parser.parse_args(argv)
    if args.profiles:
        if args.host or args.zip_output or args.directory_output or args.require_authored_ready:
            parser.error("--profiles is a read-only authoring reference, not a package operation")
        print(json.dumps({
            "schema_version": 1,
            "claim": "STATIC_HOST_CONSTRAINTS_NOT_RUNTIME_CAPABILITIES",
            "assessed_profiles": {
                name: {key: sorted(value) if isinstance(value, (set, frozenset)) else value
                       for key, value in profile.items()}
                for name, profile in HOSTS.items()
            },
            "portable_authoring_envelope": portability_envelope(),
            "unassessed_hosts": unassessed_host_statuses(),
            "host_behavior": "NOT_TESTED",
            "next_action": "VERIFY_CURRENT_OFFICIAL_HOST_RULES_AND_REQUIRED_CAPABILITIES",
        }, indent=2))
        return 0
    if args.skill and (not NAME.fullmatch(args.skill) or len(args.skill) > 64):
        raise ValueError("INVALID_SKILL_SLUG")
    if args.require_authored_ready and (args.package or args.host or args.zip_output or args.directory_output):
        parser.error("--require-authored-ready requires --all or --skill with all profiles and no output")
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
    admission = None
    if not args.package and not args.host:
        skills = [p.name for p in packages]
        if args.all:
            index = json.loads((ROOT / "registry" / "authored-skills-index.json").read_text(encoding="utf-8"))
            indexed = [row["id"] for row in index["skills"]]
            if len(indexed) != len(set(indexed)) or set(indexed) != set(skills):
                raise ValueError("AUTHORED_INDEX_PACKAGE_INVENTORY_MISMATCH")
        admission = authored_admission(results, skills)
    print(json.dumps({
        "schema_version": 1, "claim": "STATIC_PACKAGE_PREFLIGHT_ONLY",
        "unassessed_hosts": unassessed_host_statuses(),
        "authored_admission": admission,
        "canonical_skill_count": len(packages),
        "host_qualification": "NOT_TESTED",
        "summary": summary, "results": results,
    }, indent=2))
    if args.require_authored_ready:
        return 3 if not packages or admission["unexpected_holds"] else 0
    return 0 if all(r["package_ready"] for r in results) else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print("HOST_PACKAGE_HOLD: " + str(error), file=sys.stderr)
        raise SystemExit(2)
