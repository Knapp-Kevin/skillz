#!/usr/bin/env python3
"""Optional offline structural check of a composable Skillz pack.

This validates *claimed* manifest shape and local file closure only.
It does not run modules, evaluate actual outcomes, authorize tools, verify
license rights, install packages, store preferences or grant approval.
Python 3.9+ standard library; no network, repository mutation or imports
from the pack being checked.
"""
import argparse
import json
from pathlib import Path, PurePosixPath
import re
import sys

MAX_MANIFEST = 128 * 1024
MAX_FILE = 1024 * 1024
MAX_FILES = 256
MAX_MODULES = 64
MAX_PREFERENCES = 32
MAX_TEXT = 2048
MODULE_KINDS = {"skill", "phase", "component"}
AUTHORITY = {"read-only": 0, "approval-gated": 1}
PACK_FIELDS = {"schema_version", "pack_id", "capability", "entrypoint",
               "completion", "authority", "license", "files", "modules",
               "preference_slots", "feedback_policy"}
MODULE_FIELDS = {"id", "kind", "path", "requires", "required", "fallback",
                 "authority", "output", "origin", "source_identity",
                 "rights_basis"}
PREFERENCE_FIELDS = {"key", "kind", "choices", "default", "scope"}
POLICY = {"canonical": "maintainer-review", "consumer": "private-opt-in",
          "mixed": "split", "iteration": "bounded"}
SLUG = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
FORBIDDEN_PREFERENCE_TOKENS = {
    "auth", "token", "secret", "password", "user", "account", "identity",
    "security", "safety", "policy", "required", "skip", "bypass", "check",
    "validation", "verification", "permission", "network", "tool", "execute",
    "send", "publish", "install", "schedule", "filesystem", "write",
}


class PackHold(ValueError):
    pass


def require(ok, message):
    if not ok:
        raise PackHold(message)


def fields(value, expected, label):
    require(type(value) is dict and set(value) == set(expected),
            "INVALID_FIELDS:" + label)


def short_text(value, label):
    require(type(value) is str and bool(value.strip()) and
            len(value) <= MAX_TEXT and
            not any(ord(c) < 32 and c not in "\n\t" for c in value),
            "INVALID_TEXT:" + label)


def slug(value, label):
    require(type(value) is str and bool(SLUG.fullmatch(value)),
            "INVALID_IDENTIFIER:" + label)


def relative_path(value):
    require(type(value) is str and len(value) <= 240 and
            value and not value.startswith("/") and
            "\\" not in value and "://" not in value and
            "\0" not in value and "//" not in value,
            "UNSAFE_PACKAGE_PATH")
    pieces = value.split("/")
    require(all(piece not in {"", ".", ".."} and
                not piece.startswith(".") and
                re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", piece)
                for piece in pieces),
            "UNSAFE_PACKAGE_PATH")
    return value


def contained_file(root, name):
    rel=relative_path(name)
    current=root
    for part in rel.split("/"):
        current=current / part
        require(not current.is_symlink(), "SYMLINKED_PACKAGE_PATH:" + rel)
    require(current.is_file(), "MISSING_PACKAGE_FILE:" + rel)
    require(current.stat().st_size <= MAX_FILE,
            "OVERSIZED_PACKAGE_FILE:" + rel)
    return current


def validate(root, manifest):
    """Return a non-authorizing structural receipt, never an install result."""
    root=Path(root).absolute()
    require(root.is_dir() and not root.is_symlink(), "INVALID_PACKAGE_ROOT")
    fields(manifest, PACK_FIELDS, "pack")
    require(type(manifest["schema_version"]) is int and
            manifest["schema_version"] == 1, "UNSUPPORTED_PACK_SCHEMA")
    slug(manifest["pack_id"], "pack_id")
    for label in ("capability", "completion", "license"):
        short_text(manifest[label], label)
    require(manifest["entrypoint"] == "SKILL.md",
            "PACK_ENTRYPOINT_MUST_BE_SKILL")
    require(type(manifest["authority"]) is str and
            manifest["authority"] in AUTHORITY, "UNSUPPORTED_PACK_AUTHORITY")
    files=manifest["files"]
    require(type(files) is list and 3 <= len(files) <= MAX_FILES,
            "INVALID_FILE_INVENTORY")
    require(all(type(v) is str for v in files) and len(set(files)) == len(files),
            "DUPLICATE_PACKAGE_FILE")
    for name in files:
        contained_file(root, name)
    declared=set(files)
    require({"pack.json", "SKILL.md", "LICENSE"} <= declared,
            "MISSING_PACK_ENTRYPOINT_OR_LICENSE")

    modules=manifest["modules"]
    require(type(modules) is list and 2 <= len(modules) <= MAX_MODULES,
            "PACK_NOT_COMPOSITION_WORTHY")
    by_id={}
    owned=set()
    for m in modules:
        fields(m, MODULE_FIELDS, "module")
        slug(m["id"], "module.id")
        require(m["id"] not in by_id, "DUPLICATE_MODULE_ID")
        require(type(m["kind"]) is str and m["kind"] in MODULE_KINDS,
                "UNSUPPORTED_MODULE_KIND")
        path=relative_path(m["path"])
        require(path in declared and path not in owned and
                path not in {"pack.json", "SKILL.md", "LICENSE"},
                "UNDECLARED_OR_DUPLICATED_MODULE_PATH")
        require(path.endswith(".md") and
                (path.endswith("/SKILL.md") if m["kind"]=="skill"
                 else not path.endswith("/SKILL.md")),
                "MODULE_KIND_PATH_MISMATCH")
        owned.add(path)
        require(type(m["requires"]) is list and
                all(type(x) is str and SLUG.fullmatch(x) for x in m["requires"]) and
                len(m["requires"]) == len(set(m["requires"])),
                "INVALID_MODULE_DEPENDENCIES")
        require(type(m["required"]) is bool, "INVALID_REQUIRED_FLAG")
        if m["required"]:
            require(m["fallback"] is None, "REQUIRED_MODULE_HAS_FALLBACK")
        else:
            short_text(m["fallback"], "optional.fallback")
        require(type(m["authority"]) is str and m["authority"] in AUTHORITY and
                AUTHORITY[m["authority"]] <= AUTHORITY[manifest["authority"]],
                "MODULE_AUTHORITY_EXCEEDS_PACK")
        short_text(m["output"], "module.output")
        require(type(m["origin"]) is str and
                m["origin"] in {"original", "authorized-adaptation"},
                "INVALID_ORIGIN")
        for key in ("source_identity", "rights_basis"):
            short_text(m[key], "module."+key)
        if m["origin"] == "original":
            require(m["source_identity"] == "NONE" and
                    m["rights_basis"] == "ORIGINAL",
                    "ORIGINAL_MODULE_SOURCE_CONTRADICTION")
        else:
            require(m["source_identity"] not in {"NONE", "UNKNOWN"} and
                    m["rights_basis"] not in {"ORIGINAL", "UNKNOWN"},
                    "ADAPTATION_LACKS_RIGHTS_RECEIPT")
        by_id[m["id"]]=m

    visiting=set()
    visited=set()
    ordering=[]
    def visit(node):
        require(node not in visiting, "CYCLIC_MODULE_DEPENDENCY")
        if node in visited:
            return
        visiting.add(node)
        m=by_id[node]
        for dep in m["requires"]:
            require(dep in by_id, "UNKNOWN_MODULE_DEPENDENCY")
            if m["required"]:
                require(by_id[dep]["required"],
                        "REQUIRED_MODULE_DEPENDS_ON_OPTIONAL")
            visit(dep)
        visiting.remove(node)
        visited.add(node)
        ordering.append(node)
    for node in by_id:
        visit(node)

    preferences=manifest["preference_slots"]
    require(type(preferences) is list and len(preferences)<=MAX_PREFERENCES,
            "INVALID_PREFERENCE_SLOTS")
    preference_keys=set()
    for slot in preferences:
        fields(slot, PREFERENCE_FIELDS, "preference")
        require(type(slot["key"]) is str, "INVALID_PREFERENCE_KEY")
        slug(slot["key"].replace("_","-"),"preference.key")
        require(slot["key"] not in preference_keys, "DUPLICATE_PREFERENCE_SLOT")
        preference_keys.add(slot["key"])
        terms=set(re.split(r"[-_]",slot["key"]))
        require(not (terms & FORBIDDEN_PREFERENCE_TOKENS),
                "UNSAFE_PREFERENCE_SLOT")
        require(slot["kind"] == "enum" and
                slot["scope"] == "user-private-opt-in",
                "PREFERENCE_MUST_BE_PRIVATE_OPT_IN_ENUM")
        choices=slot["choices"]
        require(type(choices) is list and 2 <= len(choices) <= 16 and
                all(type(x) is str and SLUG.fullmatch(x) for x in choices) and
                len(set(choices)) == len(choices),
                "INVALID_PREFERENCE_CHOICES")
        require(slot["default"] in choices, "PREFERENCE_DEFAULT_NOT_ALLOWED")
    fields(manifest["feedback_policy"], POLICY, "feedback_policy")
    require(manifest["feedback_policy"] == POLICY,
            "UNSAFE_FEEDBACK_ROUTING_POLICY")

    # Check only simple local Markdown link destinations. This cannot prove
    # complete bundled-script dependencies, which need whole-package review.
    for name in files:
        if not name.endswith(".md"):
            continue
        body=(root/name).read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)\n]+)\)",body):
            link=target.split("#",1)[0]
            if not link or link.startswith(("https://","http://","mailto:","data:")):
                continue
            base=PurePosixPath(name).parent
            parts=[]
            for seg in list(base.parts)+link.split("/"):
                if seg in {"", "."}:
                    continue
                if seg=="..":
                    require(bool(parts), "LINK_LEAVES_PACK:"+name)
                    parts.pop()
                else:
                    parts.append(seg)
            candidate="/".join(parts)
            require(candidate in declared, "UNINVENTORIED_LOCAL_LINK:"+name)
            contained_file(root,candidate)
    return {
        "schema_version":1,
        "status":"PACK_STRUCTURE_VALID_NOT_EXECUTED",
        "pack_id":manifest["pack_id"],
        "modules_order":ordering,
        "required_modules":sum(1 for m in modules if m["required"]),
        "optional_modules":sum(1 for m in modules if not m["required"]),
        "declared_local_files":len(files),
        "declared_preference_slots":len(preferences),
        "actual_user_preferences_present":False,
        "source_rights_authenticated":False,
        "semantic_quality_verified":False,
        "agent_or_consumer_outcome_observed":False,
        "installed_or_published":False,
        "execution_or_mutation_performed":False,
    }


def unique_keys(pairs):
    out={}
    for key,value in pairs:
        require(key not in out,"DUPLICATE_JSON_KEY")
        out[key]=value
    return out


def load(root):
    root=Path(root).absolute()
    require(root.is_dir() and not root.is_symlink(), "INVALID_PACKAGE_ROOT")
    file=contained_file(root,"pack.json")
    require(file.stat().st_size <= MAX_MANIFEST,
            "PACK_MANIFEST_TOO_LARGE")
    with file.open(encoding="utf-8") as stream:
        return json.load(stream,object_pairs_hook=unique_keys,
                         parse_constant=lambda _: (_ for _ in ()).throw(
                             PackHold("NONFINITE_MANIFEST_VALUE")))


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root",required=True)
    args=ap.parse_args(argv)
    try:
        report=validate(args.root,load(args.root))
        print(json.dumps(report,indent=2,sort_keys=True))
        return 0
    except (PackHold,ValueError,TypeError,OSError,UnicodeError) as exc:
        print("PACK_STRUCTURE_HOLD:"+str(exc),file=sys.stderr)
        return 2


if __name__=="__main__":
    raise SystemExit(main())
