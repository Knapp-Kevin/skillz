#!/usr/bin/env python3
"""Conservative offline Gold/Platinum README preflight, Python 3.9+ stdlib.

Checks visible structure and referenced local assets. Never self-approves a
brand, external badge, semantic quality, rendered view, generated source,
actual first-user outcome, or provider CI. No network, command execution, writes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit
import check_readme as local

REQUIRED = {"schema_version", "profile", "project_identity", "banner_path",
            "required_badge_labels", "allowed_badge_targets", "journey_mode",
            "asset_inventory", "exceptions"}
IMAGE = re.compile(r'!\[([^\]\n]*)\]\(([^)\n]+)\)')
HTML_IMAGE = re.compile(r'<img\b[^>]*>', re.I)
ATTRIBUTE = re.compile(r'\b(src|alt)\s*=\s*["\x27]([^"\x27]+)["\x27]', re.I)
BADGE = re.compile(r'\[!\[([^\]\n]+)\]\(([^)\n]+)\)\]\(([^)\n]+)\)')
TOC_HEAD = re.compile(r'^\s{0,3}#{1,4}\s+(?:table of contents|contents|on this page|navigation)\s*#*\s*$', re.I)
TOC_LINK = re.compile(r'^\s*[-*+]\s+\[([^\]]+)\]\(#([^)]+)\)\s*$')
START_HEAD = re.compile(r'^\s{0,3}#{1,4}\s+(?:quick start|getting started|start here|first steps|try it|usage|how to use|explore|reading path)\b', re.I)
TECH_HEAD = re.compile(r'^\s{0,3}#{1,4}\s+(?:documentation|technical (?:reference|documentation)|architecture|api|developer (?:guide|documentation)|reference|further reading)\b', re.I)
NONFINAL = {"proposed-placeholder", "temporary-placeholder", "draft"}
STATES = NONFINAL | {"verified-existing", "newly-committed", "approved-final"}


class InputError(ValueError):
    pass


def _unique(pairs):
    result = {}
    for key, val in pairs:
        if key in result:
            raise InputError("duplicate contract key")
        result[key] = val
    return result


def _path(root, name):
    if not isinstance(name, str) or not name or name.startswith("/") or "\\" in name or "\x00" in name:
        raise InputError("unsafe file path")
    if re.match(r"^[A-Za-z]:", name) or any(x in ("", ".", "..") for x in name.split("/")):
        raise InputError("path traversal or ambiguous relative path")
    node = root
    for part in name.split("/"):
        node = node / part
        if node.is_symlink():
            raise InputError("symlinked file path")
    return node


def _read(path):
    if not path.is_file() or path.stat().st_size > 1_048_576:
        raise InputError("missing, nonregular or oversized file")
    return path.read_text(encoding="utf-8")


def contract_from(path):
    cfg = json.loads(_read(path), object_pairs_hook=_unique)
    if not isinstance(cfg, dict) or set(cfg) != REQUIRED:
        raise InputError("unknown or incomplete contract fields")
    if type(cfg["schema_version"]) is not int or cfg["schema_version"] != 1:
        raise InputError("unsupported contract schema")
    if cfg["profile"] not in ("gold", "platinum"):
        raise InputError("Gold/Platinum required")
    if not isinstance(cfg["project_identity"], str) or len(cfg["project_identity"].strip()) < 2:
        raise InputError("verified project identity required")
    if not isinstance(cfg["banner_path"], str):
        raise InputError("banner path required")
    if cfg["journey_mode"] not in ("execute", "read"):
        raise InputError("unknown reader journey")
    for key in ("required_badge_labels", "allowed_badge_targets", "asset_inventory", "exceptions"):
        if not isinstance(cfg[key], list):
            raise InputError("expected list: " + key)
    if not cfg["required_badge_labels"] or not cfg["allowed_badge_targets"] or not cfg["asset_inventory"]:
        raise InputError("mandatory Gold evidence fields empty")
    if not all(isinstance(x, str) and x.strip() for x in cfg["required_badge_labels"]):
        raise InputError("invalid badge labels")
    if not all(isinstance(x, str) and x.startswith("https://") and urlsplit(x).netloc
               for x in cfg["allowed_badge_targets"]):
        raise InputError("invalid badge destinations")
    if not all(isinstance(a, dict) and set(a) ==
               {"path", "status", "owner", "purpose", "alt", "replacement", "sha256"}
               and all(isinstance(v, str) and v.strip() for v in a.values())
               and a["status"] in STATES
               and bool(re.fullmatch(r"[a-f0-9]{64}", a["sha256"]))
               for a in cfg["asset_inventory"]):
        raise InputError("invalid asset lifecycle inventory")
    if not all(isinstance(a, dict) and set(a) == {"requirement", "reason", "evidence_ref"}
               and all(isinstance(v, str) and v.strip() for v in a.values())
               for a in cfg["exceptions"]):
        raise InputError("unjustified or malformed exception")
    return cfg


def _image_digest(path):
    if not path.is_file() or path.stat().st_size > 16_777_216:
        raise InputError("asset missing or exceeds 16 MiB review limit")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1_048_576), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _image_geometry(path):
    """Reject impossible raster dimensions and active/external SVG.

    This is NOT a decode or visual review. Actual render remains HOLD.
    """
    suffix = path.suffix.lower()
    if suffix == ".png":
        with path.open("rb") as stream:
            hdr = stream.read(24)
        if len(hdr) < 24 or hdr[:8] != b"\x89PNG\r\n\x1a\n" or hdr[12:16] != b"IHDR":
            raise InputError("invalid PNG identity/header")
        return (int.from_bytes(hdr[16:20], "big"), int.from_bytes(hdr[20:24], "big"))
    if suffix == ".svg":
        markup = path.read_text(encoding="utf-8")
        if re.search(r"(?i)<\s*(?:script|foreignObject)\b|\bon\w+\s*=|(?:href|xlink:href)\s*=\s*['\"]\s*(?:https?:|//|javascript:|data:)", markup):
            raise InputError("SVG active or remote dependencies are not trusted assets")
        m = re.search(r"\bviewBox\s*=\s*['\"]\s*[\d.]+\s+[\d.]+\s+([\d.]+)\s+([\d.]+)\s*['\"]", markup)
        if not m:
            raise InputError("SVG banner viewBox absent or unrecognized")
        return (float(m.group(1)), float(m.group(2)))
    # JPEG/WebP/other formats require an authenticated decoder at visual review.
    return None


def _slug(text):
    text = re.sub(r"[*_\x60~]", "", text.strip().rstrip("#").strip()).lower()
    return re.sub(r"\s+", "-", re.sub(r"[^\w\- ]", "", text))


def _headings(cleaned):
    heads = {}
    counts = {}
    for line in cleaned:
        match = local.HEAD.match(line)
        if match:
            h = match.group(2).rstrip("#").strip()
            if re.search(r"[<>\[\]{}\\]", h):
                continue
            base = _slug(h)
            if base:
                index = counts.get(base, 0)
                heads[base if not index else "%s-%s" % (base, index)] = h
                counts[base] = index + 1
    return heads


def _section(cleaned, pattern):
    for i, line in enumerate(cleaned):
        if pattern.match(line):
            end = next((j for j in range(i + 1, len(cleaned)) if local.HEAD.match(cleaned[j])), len(cleaned))
            return "\n".join(cleaned[i + 1:end])
    return None


def _opening(cleaned):
    """Collect the first public-facing paragraph, not title/banner/badges."""
    seen_title = False
    result = []
    for line in cleaned:
        heading = local.HEAD.match(line)
        if heading and len(heading.group(1)) == 1 and not seen_title:
            seen_title = True
            continue
        if not seen_title:
            continue
        if heading:
            break
        item = line.strip()
        if not item or item.startswith(("![", "[![", "<picture", "<img", "|", "---")):
            continue
        if item.startswith(("-", "*", "+")) and not result:
            continue
        result.append(item)
        if len(" ".join(result).split()) >= 130:
            break
    return " ".join(result)


def audit(root, readme, cfg):
    raw = _read(_path(root, readme))
    cleaned = local.clean_lines(raw)
    text = "\n".join(cleaned)
    checks = []
    def check(key, status, note):
        checks.append({"key": key, "status": status, "note": note})

    title = next((m.group(2) for line in cleaned if (m := local.HEAD.match(line)) and len(m.group(1)) == 1), "")
    check("identity", "PASS" if title.strip().casefold() == cfg["project_identity"].strip().casefold() else "FAIL",
          "H1 must identify the verified target product, not another repository")

    if len({a["path"] for a in cfg["asset_inventory"]}) != len(cfg["asset_inventory"]):
        raise InputError("duplicate asset inventory paths")
    for entry in cfg["asset_inventory"]:
        item = _path(root, entry["path"])  # Reject traversal and symlink ownership aliases.
        if item.is_file() and _image_digest(item) != entry["sha256"]:
            check("asset-digest", "FAIL", "asset bytes differ from declared SHA-256: " + entry["path"][:120])
        elif not item.is_file():
            check("asset-digest", "FAIL", "declared asset does not exist: " + entry["path"][:120])
    inventory = {a["path"]: a for a in cfg["asset_inventory"]}
    banner = cfg["banner_path"]
    # Badges are metadata with accessible labels, not decorative image assets.
    presentation = BADGE.sub("", text)
    images = [(m.group(1).strip(), m.group(2).strip()) for m in IMAGE.finditer(presentation)]
    html_items = [{k.lower(): v for k, v in ATTRIBUTE.findall(m.group(0))}
                  for m in HTML_IMAGE.finditer(text)]
    for item in html_items:
        images.append((item.get("alt", ""), item.get("src", "")))
    selected = next(((alt, src) for alt, src in images if src == banner), None)
    if selected is None or banner not in inventory:
        check("banner", "FAIL", "required project-specific banner missing or not in asset inventory")
    elif inventory[banner]["status"] in NONFINAL:
        check("banner", "FAIL", "placeholder cannot stand in for a final committed banner")
    elif not _path(root, banner).is_file() or _path(root, banner).stat().st_size == 0:
        check("banner", "FAIL", "banner file missing or empty")
    elif len(selected[0]) < 6:
        check("banner", "FAIL", "banner alt text is not descriptive")
    elif cfg["project_identity"].casefold() not in selected[0].casefold():
        check("banner", "FAIL", "banner alt identity does not name this project")
    else:
        try:
            dims = _image_geometry(_path(root, banner))
            if dims and (dims[0] < 480 or dims[1] < 100 or not 1.5 <= dims[0] / dims[1] <= 9.0):
                check("banner", "FAIL", "banner intrinsic size/aspect ratio is unsuitable for a README hero")
            else:
                check("banner", "HOLD", "plausible local asset; brand rights, actual rendering and responsive quality unverified")
        except (OSError, UnicodeError, ValueError, ZeroDivisionError) as e:
            check("banner", "FAIL", "banner image integrity: " + str(e))
    for alt, src in images:
        if len(alt) < 6 or alt.casefold() in ("banner", "logo", "image", "screenshot"):
            check("image-alt", "FAIL", "non-descriptive image alt: " + src[:120])
        if src.startswith(("https://", "http://")):
            check("asset-status", "HOLD", "remote image needs identity, accessibility and provenance review: " + src[:120])
        elif src not in inventory:
            check("asset-status", "FAIL", "displayed asset is missing from the ownership inventory: " + src[:120])
        elif inventory[src]["status"] in NONFINAL:
            check("asset-status", "FAIL", "nonfinal asset presented in README: " + src[:120])
        else:
            try:
                if not _path(root, src).is_file():
                    check("asset-status", "FAIL", "displayed asset is missing: " + src[:120])
            except InputError:
                check("asset-status", "FAIL", "unsafe/symlinked displayed asset: " + src[:120])
    if re.search(r"<(?:picture|img)\b", text, re.I):
        check("html-images", "HOLD", "HTML/picture image handling requires rendered visual review")

    badges = {m.group(1).strip().casefold(): m for m in BADGE.finditer(text)}
    for label in cfg["required_badge_labels"]:
        badge = badges.get(label.casefold())
        if badge is None:
            check("badge:" + label, "FAIL", "missing required meaningful badge")
        elif not badge.group(2).startswith("https://") or not urlsplit(badge.group(2)).netloc:
            check("badge:" + label, "FAIL", "badge image source must be HTTPS")
        elif badge.group(3) not in cfg["allowed_badge_targets"]:
            check("badge:" + label, "FAIL", "badge link does not target the actual project")
        else:
            check("badge:" + label, "HOLD", "badge source/target declared; remote service, meaning and status not authenticated")

    toc = _section(cleaned, TOC_HEAD)
    heads = _headings(cleaned)
    if toc is None:
        check("toc", "FAIL", "required linked contents section missing")
    else:
        items = [m for l in toc.splitlines() if (m := TOC_LINK.match(l))]
        if len(items) < 2:
            check("toc", "FAIL", "contents lacks two meaningful linked headings")
        elif any(m.group(2) not in heads or _slug(m.group(1)) != _slug(heads.get(m.group(2), ""))
                 for m in items):
            check("toc", "FAIL", "contents link points to missing or wrong heading")
        else:
            check("toc", "PASS", "common local heading links and labels match")

    step = _section(cleaned, START_HEAD)
    if step is None:
        check("first-success", "FAIL", "no usable first-reader journey section")
    elif cfg["journey_mode"] == "execute":
        has_command = bool(re.search(r"(?m)^ {0,3}(?:\x60{3,}|~{3,})", raw))
        only_tests = bool(re.search(r"(?im)^\s*(?:cargo test|npm test|pytest|go test|make test)\s*$", step))
        observable = bool(re.search(r"\b(?:expected|you should see|output|result|prints|creates|opens|displays|shows)\b", step, re.I))
        if not has_command or (only_tests and not observable) or not observable:
            check("first-success", "FAIL", "example must enable an observable user outcome, not only developer checks")
        else:
            check("first-success", "HOLD", "command and expected result present; safety, correctness and actual execution unverified")
    elif not re.search(r"\[[^\]]+\]\([^)]+\)", step) or not re.search(
            r"\b(?:read|open|follow|explore|start|see)\b", step, re.I):
        check("first-success", "FAIL", "documentation-first path needs a concrete next reading action")
    else:
        check("first-success", "HOLD", "reading path present; newcomer outcome not observed")

    check("technical-navigation", "HOLD" if any(TECH_HEAD.match(l) for l in cleaned) else "FAIL",
          "technical references require source-bound verification, not just headings")
    # Obvious defects may FAIL mechanically. A good heuristic result is never
    # a semantic PASS: Why/What/How and comprehension require editorial review.
    opening = _opening(cleaned)
    if len(opening.split()) < 22:
        check("opening-meaning", "FAIL", "first-screen narrative is missing or too short to explain a reader problem")
    elif re.search(r"[∑∫∂∀∃⊗∈⊂]|\\\\begin\\{|\\$\\$", opening):
        check("opening-meaning", "FAIL", "unexplained equations or dense notation lead the public introduction")
    else:
        check("opening-meaning", "HOLD", "independently verify Why→What→How, 30-second purpose and Grade-10 comprehension")
    local_report = local.audit(root, _path(root, readme))
    if local_report["local_blockers"]:
        check("local-links", "FAIL", "%d broken local links/anchors" % local_report["local_blockers"])
    else:
        check("local-links", "HOLD", "supported local links checked; remote and complex links remain unverified")
    if re.search(r"(?i)(do not edit|auto.generated|<!--\s*generated:begin)", raw):
        check("generated-owner", "HOLD", "update generator/templates and verify parity through separate delivery preflight")
    if cfg["exceptions"]:
        check("exceptions", "HOLD", "exceptions need independent review; profile cannot self-approve")
    check("visual", "HOLD", "final committed README rendering, responsive layout and branded asset must be inspected")
    check("editorial", "HOLD", "independent reader/comprehension, source claims and first-use evidence required")
    if cfg["profile"] == "platinum":
        check("independent-reader", "HOLD", "independent newcomer task acceptance is required")
    failures = sum(x["status"] == "FAIL" for x in checks)
    return {
        "profile": cfg["profile"], "checks": checks, "failed": failures,
        "quality_status": "FAIL" if failures else "HOLD",
        "technical_delivery_status": "NOT_RUN",
        "editorial_acceptance_status": "HOLD", "completion_permitted": False,
        "source_claims_authenticated": False, "external_badges_authenticated": False,
        "assets_approved": False, "rendered_review_completed": False,
        "generated_parity_qualified": False, "reader_task_verified": False
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", required=True)
    p.add_argument("--readme", default="README.md")
    p.add_argument("--contract", required=True)
    p.add_argument("--profile", required=True, choices=("gold", "platinum"))
    args = p.parse_args(argv)
    try:
        root = Path(args.root).absolute()
        if not root.is_dir() or any(x.is_symlink() for x in (root, *root.parents)):
            raise InputError("invalid or symlinked root")
        cfg = contract_from(_path(root, args.contract))
        if cfg["profile"] != args.profile:
            raise InputError("command/contract profile mismatch")
        report = audit(root, args.readme, cfg)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as e:
        print("INVALID_INPUT: " + str(e), file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1  # Mechanical PASS cannot clear independent editorial/delivery HOLD.


if __name__ == "__main__":
    sys.exit(main())
