#!/usr/bin/env python3
"""Optional, offline manager for a single user's skill preference overlay.

No execution on skill load. Writes require an explicit user/host-approved
operation, a pre-existing private POSIX configuration root, and a narrowly
allowlisted value. The --approved flag is a guard, not proof of consent.
Windows ACL verification is not available from the stdlib: fail closed there
and use an authorized host-native private store instead.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import secrets
import stat
import sys

SKILL_ID = "evidence-driven-refinement-loop"
# Fixed code-level allowlist; declarative schema must agree exactly.
# A modified schema alone must never expand the manager's permissions.
SAFE_VALUES = {
    "response.detail": {"concise", "standard", "detailed"},
    "response.format": {"paragraphs", "checklist", "table"},
    "examples.focus": {"general", "documentation", "code", "ci"},
}
MAX_BYTES = 8192
PACKAGE = Path(__file__).resolve().parent.parent
SCHEMA_FILE = Path(__file__).with_name("schema.json")


class PreferenceError(Exception):
    pass


def current_version() -> str:
    text = (PACKAGE / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"(?m)^  version: ([0-9]+\.[0-9]+\.[0-9]+)$", text)
    if not match:
        raise PreferenceError("Cannot verify canonical skill version")
    return match.group(1)


def allowed_keys() -> dict[str, set[str]]:
    spec = json.loads(SCHEMA_FILE.read_text(encoding="utf-8"))
    if spec["properties"]["skill_id"].get("const") != SKILL_ID:
        raise PreferenceError("Bundled schema is for a different skill")
    entries = spec["properties"]["preferences"]["items"]["oneOf"]
    result = {}
    for entry in entries:
        props = entry["properties"]
        key = props["key"]["const"]
        vals = props["value"]["enum"]
        if key in result or not vals or not all(isinstance(v, str) for v in vals):
            raise PreferenceError("Invalid bundled preference schema")
        if props["source"].get("const") != "explicit-user-confirmation":
            raise PreferenceError("Schema would accept unapproved preference")
        result[key] = set(vals)
    if result != SAFE_VALUES:
        raise PreferenceError("Bundled schema differs from fixed safe preference allowlist")
    return result


def validate_document(doc: object, *, version: str, allowlist: dict[str, set[str]]) -> dict:
    if not isinstance(doc, dict) or set(doc) != {
        "schema_version", "skill_id", "base_skill_version", "scope", "preferences"
    }:
        raise PreferenceError("Unexpected overlay fields")
    if doc["schema_version"] != 1 or type(doc["schema_version"]) is not int:
        raise PreferenceError("Unsupported overlay schema version")
    if doc["skill_id"] != SKILL_ID or doc["scope"] != "user-local":
        raise PreferenceError("Wrong skill identity or scope")
    if doc["base_skill_version"] != version:
        raise PreferenceError("Canonical skill version changed; manual preference reconciliation required")
    prefs = doc["preferences"]
    if not isinstance(prefs, list) or len(prefs) > len(allowlist):
        raise PreferenceError("Invalid preference list")
    seen = set()
    for item in prefs:
        if not isinstance(item, dict) or set(item) != {"key", "value", "source"}:
            raise PreferenceError("Unexpected preference fields")
        k, v, source = item["key"], item["value"], item["source"]
        if not isinstance(k, str) or k in seen or k not in allowlist:
            raise PreferenceError("Unknown or duplicate preference key")
        if not isinstance(v, str) or v not in allowlist[k]:
            raise PreferenceError("Preference value not allowed")
        if source != "explicit-user-confirmation":
            raise PreferenceError("Preference lacks explicit confirmation")
        seen.add(k)
    return doc


def check_private_dir(path: Path, *, allow_create: bool) -> None:
    if allow_create:
        try:
            path.mkdir(mode=0o700)
        except FileExistsError:
            pass
    try:
        info = path.lstat()
    except FileNotFoundError as exc:
        raise PreferenceError("Host must provide an existing user-private --root") from exc
    if not stat.S_ISDIR(info.st_mode):
        raise PreferenceError("Overlay directory is not a real directory")
    if info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
        raise PreferenceError("Overlay directory is not private to the current user")


def reject_checkout_root(root: Path) -> None:
    # Do not silently create user data in this package or the containing
    # source checkout. A standalone installed copy has no .git boundary.
    actual = root.resolve()
    if actual == PACKAGE or PACKAGE in actual.parents:
        raise PreferenceError("Local preferences cannot be written inside the skill package")
    for ancestor in (PACKAGE, *PACKAGE.parents):
        if (ancestor / ".git").exists() and (actual == ancestor or ancestor in actual.parents):
            raise PreferenceError("Local preferences cannot be stored in a source checkout")


def overlay_file(root_arg: str, *, create_dirs: bool) -> Path:
    if os.name != "posix" or not hasattr(os, "O_NOFOLLOW"):
        raise PreferenceError("Private filesystem/ACL cannot be verified here; use host-native storage")
    root = Path(root_arg).expanduser()
    if root.is_symlink():
        raise PreferenceError("Private root must not be a symlink")
    reject_checkout_root(root)
    check_private_dir(root, allow_create=False)
    intermediate = root / "skill-overlays"
    skilldir = intermediate / SKILL_ID
    for directory in (intermediate, skilldir):
        if not create_dirs and not directory.exists() and not directory.is_symlink():
            # An unseen overlay is a normal first-run state, never an
            # instruction to create storage during a read-only operation.
            return skilldir / "preferences.local.json"
        check_private_dir(directory, allow_create=create_dirs)
    return skilldir / "preferences.local.json"


def reject_duplicate_fields(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise PreferenceError("Duplicate JSON field rejected")
        result[key] = value
    return result


def load(path: Path, *, version: str, allowlist: dict[str, set[str]]) -> dict:
    fresh = {
        "schema_version": 1,
        "skill_id": SKILL_ID,
        "base_skill_version": version,
        "scope": "user-local",
        "preferences": [],
    }
    try:
        info = path.lstat()
    except FileNotFoundError:
        return fresh
    if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid():
        raise PreferenceError("Preference file is not a user-owned regular file")
    if stat.S_IMODE(info.st_mode) & 0o077 or info.st_size > MAX_BYTES:
        raise PreferenceError("Preference file permissions/size unsafe")
    flags = os.O_RDONLY | os.O_NOFOLLOW
    fd = os.open(path, flags)
    with os.fdopen(fd, "rb") as stream:
        # Re-check the OPEN descriptor: lstat followed by open is a
        # separate operation and cannot defend against file swaps.
        opened = os.fstat(stream.fileno())
        if (not stat.S_ISREG(opened.st_mode)
                or opened.st_uid != os.getuid()
                or stat.S_IMODE(opened.st_mode) & 0o077
                or opened.st_size > MAX_BYTES):
            raise PreferenceError("Opened preference file is unsafe")
        raw = stream.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise PreferenceError("Preference file too large")
    try:
        doc = json.loads(raw.decode("utf-8"),
                         object_pairs_hook=reject_duplicate_fields)
    except (UnicodeError, ValueError) as exc:
        raise PreferenceError("Invalid preference JSON") from exc
    return validate_document(doc, version=version, allowlist=allowlist)


def write_atomic(path: Path, doc: dict) -> None:
    # Parents have been checked private. Do not follow destination symlinks.
    if path.is_symlink():
        raise PreferenceError("Refusing preference symlink")
    raw = (json.dumps(doc, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if len(raw) > MAX_BYTES:
        raise PreferenceError("Preference payload too large")
    tmp = path.with_name(".preferences-" + secrets.token_hex(12) + ".tmp")
    fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp, path)
        # Persist the directory entry as well as the file contents.
        parent_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            os.fsync(parent_fd)
        finally:
            os.close(parent_fd)
    finally:
        try:
            tmp.unlink()
        except FileNotFoundError:
            pass


def revoke_overlay(path: Path) -> dict:
    """Revoke private preference data even if its JSON/version is invalid.

    Revocation must not depend on successfully interpreting potentially
    stale, hostile, or corrupted preference content. Do NOT follow links.
    """
    try:
        item = path.lstat()
    except FileNotFoundError:
        return {"status": "NOT_FOUND", "remaining": 0}
    if (not stat.S_ISREG(item.st_mode) or item.st_uid != os.getuid()
            or stat.S_IMODE(item.st_mode) & 0o077):
        raise PreferenceError("Refusing to delete unsafe preference file")
    path.unlink()
    if path.is_symlink() or path.exists():
        raise PreferenceError("Post-delete verification failed; no success asserted")
    parent_fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        os.fsync(parent_fd)
    finally:
        os.close(parent_fd)
    return {"status": "REMOVED", "remaining": 0}


def execute(args: argparse.Namespace) -> dict:
    if args.action not in ("show", "validate", "set", "remove", "clear"):
        raise PreferenceError("Unknown action; no file operation authorized")
    if args.action in ("set", "remove", "clear") and not args.approved:
        raise PreferenceError("Mutation requires explicit user approval; --approved is not proof of consent")
    version = current_version()
    allow = allowed_keys()
    if args.action == "set" and (
        args.key not in allow or args.value not in allow.get(args.key, set())
    ):
        raise PreferenceError("Unknown preference or disallowed value")
    target = overlay_file(args.root, create_dirs=args.action == "set")
    if args.action == "clear":
        # An owner may revoke an obsolete or malformed overlay. Do not
        # block deletion on a schema or canonical version mismatch.
        return revoke_overlay(target)
    doc = load(target, version=version, allowlist=allow)
    if args.action == "show":
        return {"status": "LOADED" if target.exists() else "ABSENT",
                "preferences": doc["preferences"], "base_skill_version": version}
    if args.action == "validate":
        return {"status": "VALID" if target.exists() else "ABSENT",
                "count": len(doc["preferences"]), "base_skill_version": version}
    if args.action == "set":
        if args.key not in allow or args.value not in allow[args.key]:
            raise PreferenceError("Unknown preference or disallowed value")
        entries = {p["key"]: p for p in doc["preferences"]}
        entries[args.key] = {
            "key": args.key, "value": args.value,
            "source": "explicit-user-confirmation",
        }
        doc["preferences"] = [entries[k] for k in sorted(entries)]
        validate_document(doc, version=version, allowlist=allow)
        write_atomic(target, doc)
        if load(target, version=version, allowlist=allow) != doc:
            raise PreferenceError("Post-write verification failed; no success asserted")
        return {"status": "SAVED", "key": args.key, "base_skill_version": version}
    if args.action == "remove":
        kept = [p for p in doc["preferences"] if p["key"] != args.key]
        if len(kept) == len(doc["preferences"]):
            return {"status": "NOT_FOUND", "key": args.key}
        doc["preferences"] = kept
    if doc["preferences"]:
        write_atomic(target, doc)
        if load(target, version=version, allowlist=allow) != doc:
            raise PreferenceError("Post-write verification failed; no success asserted")
    else:
        if target.is_symlink():
            raise PreferenceError("Refusing to delete a preference symlink")
        target.unlink(missing_ok=True)
        if target.is_symlink() or target.exists():
            raise PreferenceError("Post-delete verification failed; no success asserted")
    return {"status": "REMOVED", "remaining": len(doc["preferences"])}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, help="Existing owner-private host configuration directory")
    commands = parser.add_subparsers(dest="action", required=True)
    commands.add_parser("show")
    commands.add_parser("validate")
    setter = commands.add_parser("set")
    setter.add_argument("key")
    setter.add_argument("value")
    setter.add_argument("--approved", action="store_true")
    remover = commands.add_parser("remove")
    remover.add_argument("key")
    remover.add_argument("--approved", action="store_true")
    clear = commands.add_parser("clear")
    clear.add_argument("--approved", action="store_true")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(execute(args), sort_keys=True))
        return 0
    except (PreferenceError, OSError) as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
