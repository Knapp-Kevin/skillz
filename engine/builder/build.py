#!/usr/bin/env python3
"""Optional offline builder for user-authored single skills, phases, and packs.

Caller supplies the actual task instructions. This tool verifies only local
structure, never semantic quality, license title, host behavior, consent,
installation or publication. No network, shell, or generated-code execution.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
from string import Template
import sys
import tempfile

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
TEMPLATES = HERE / "templates"
sys.path.insert(0, str(REPO_ROOT / "engine" / "packs"))
import check_pack

MAX_BLUEPRINT = 192 * 1024
MAX_PROSE = 16000
MAX_MODULES = 32
MAX_STEPS = 32
ALLOWED_KINDS = {"single", "phased", "pack"}
BASE_FIELDS = {
    "schema_version", "kind", "name", "description", "outcome", "trigger",
    "non_trigger", "inputs", "verification", "failure_handling", "authority",
    "copyright_holder", "rights_declaration", "steps", "modules",
    "preference_slots",
}
STEP_FIELDS = {"id", "title", "instructions", "output"}
MODULE_FIELDS = {
    "id", "kind", "requires", "required", "fallback", "authority", "output",
    "instructions",
}
PLACEHOLDERS = re.compile(r"\b(?:TODO|TBD|FIXME|lorem ipsum|fill in later)\b|<[^>\n]{1,70}>", re.I)
SLUG = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
ALLOWED_AUTHORITY = {"read-only", "approval-gated"}
POLICY = {"canonical": "maintainer-review", "consumer": "private-opt-in",
          "mixed": "split", "iteration": "bounded"}

class BuildHold(ValueError):
    pass

def need(ok, message):
    if not ok:
        raise BuildHold(message)

def fields(value, expected, label):
    need(type(value) is dict and set(value) == set(expected),
         "INVALID_FIELDS:" + label)

def slug(value, label):
    need(type(value) is str and bool(SLUG.fullmatch(value)),
         "INVALID_SLUG:" + label)

def prose(value, label, minimum=12, maximum=MAX_PROSE):
    need(type(value) is str and minimum <= len(value.strip()) <= maximum and
         not PLACEHOLDERS.search(value) and "\0" not in value,
         "INCOMPLETE_OR_INVALID_PROSE:" + label)
    return value.strip()

def authority(value, label):
    need(type(value) is str and value in ALLOWED_AUTHORITY,
         "INVALID_AUTHORITY:" + label)

def read_json(path):
    p = Path(path).absolute()
    need(p.is_file() and not p.is_symlink() and p.stat().st_size <= MAX_BLUEPRINT,
         "BLUEPRINT_MISSING_OR_OVERSIZED")
    with p.open(encoding="utf-8") as h:
        return json.load(h, object_pairs_hook=check_pack.unique_keys,
                         parse_constant=lambda _: (_ for _ in ()).throw(
                             BuildHold("NONFINITE_JSON_NOT_ALLOWED")))

def validate_blueprint(b):
    fields(b, BASE_FIELDS, "blueprint")
    need(type(b["schema_version"]) is int and b["schema_version"] == 1,
         "UNSUPPORTED_BLUEPRINT_SCHEMA")
    need(type(b["kind"]) is str and b["kind"] in ALLOWED_KINDS,
         "INVALID_BUILD_KIND")
    slug(b["name"], "name")
    prose(b["description"], "description", 12, 300)
    for key in ("outcome", "trigger", "non_trigger", "inputs",
                "verification", "failure_handling", "copyright_holder"):
        prose(b[key], key, 4 if key == "copyright_holder" else 12)
    # Keep YAML and the original-author license attribution single-line.
    need("\n" not in b["description"] and "\r" not in b["description"] and
         "\n" not in b["copyright_holder"] and
         "\r" not in b["copyright_holder"],
         "HEADER_OR_LICENSE_LINE_BREAK")
    authority(b["authority"], "authority")
    need(b["rights_declaration"] == "caller-asserts-original-content",
         "ORIGINAL_RIGHTS_DECLARATION_REQUIRED")
    steps, modules = b["steps"], b["modules"]
    need(type(steps) is list and type(modules) is list,
         "INVALID_STEP_OR_MODULE_LIST")
    if b["kind"] == "single":
        need(1 <= len(steps) <= MAX_STEPS and not modules,
             "SINGLE_REQUIRES_STEPS_NOT_MODULES")
    elif b["kind"] == "phased":
        need(2 <= len(steps) <= MAX_STEPS and not modules,
             "PHASED_REQUIRES_MULTIPLE_STEPS")
    else:
        need(not steps and 2 <= len(modules) <= MAX_MODULES,
             "PACK_REQUIRES_MODULES_NOT_STEPS")
    seen = set()
    for item in steps:
        fields(item, STEP_FIELDS, "step")
        slug(item["id"], "step.id")
        need(item["id"] not in seen, "DUPLICATE_STEP_ID")
        seen.add(item["id"])
        for key in ("title", "instructions", "output"):
            prose(item[key], "step." + key, 6 if key == "title" else 12)
    seen.clear()
    for item in modules:
        fields(item, MODULE_FIELDS, "module")
        slug(item["id"], "module.id")
        need(item["id"] not in seen, "DUPLICATE_MODULE_ID")
        seen.add(item["id"])
        need(type(item["kind"]) is str and item["kind"] in check_pack.MODULE_KINDS,
             "INVALID_MODULE_KIND")
        authority(item["authority"], "module.authority")
        need(check_pack.AUTHORITY[item["authority"]] <=
             check_pack.AUTHORITY[b["authority"]],
             "MODULE_AUTHORITY_EXCEEDS_PACK")
        need(type(item["required"]) is bool, "INVALID_MODULE_REQUIRED")
        if item["required"]:
            need(item["fallback"] is None, "REQUIRED_MODULE_HAS_FALLBACK")
        else:
            prose(item["fallback"], "module.fallback")
        deps = item["requires"]
        need(type(deps) is list and
             all(type(d) is str and SLUG.fullmatch(d) for d in deps) and
             len(set(deps)) == len(deps), "INVALID_MODULE_REQUIRES")
        prose(item["output"], "module.output")
        prose(item["instructions"], "module.instructions", 20)
    prefs = b["preference_slots"]
    need(type(prefs) is list and len(prefs) <= check_pack.MAX_PREFERENCES,
         "INVALID_PREFERENCE_SLOT_LIST")
    names = set()
    for slot in prefs:
        fields(slot, check_pack.PREFERENCE_FIELDS, "preference")
        need(type(slot["key"]) is str, "INVALID_PREFERENCE_KEY")
        slug(slot["key"].replace("_", "-"), "preference.key")
        need(slot["key"] not in names, "DUPLICATE_PREFERENCE_SLOT")
        names.add(slot["key"])
        terms = set(re.split(r"[-_]", slot["key"]))
        need(not terms.intersection(check_pack.FORBIDDEN_PREFERENCE_TOKENS),
             "UNSAFE_PREFERENCE_SLOT")
        need(slot["kind"] == "enum" and
             slot["scope"] == "user-private-opt-in",
             "PREFERENCE_MUST_BE_PRIVATE_OPT_IN_ENUM")
        choices = slot["choices"]
        need(type(choices) is list and 2 <= len(choices) <= 16 and
             all(type(c) is str and SLUG.fullmatch(c) for c in choices) and
             len(set(choices)) == len(choices),
             "INVALID_PREFERENCE_CHOICES")
        need(slot["default"] in choices, "INVALID_PREFERENCE_DEFAULT")

def template(template_filename, **values):
    p = TEMPLATES / template_filename
    need(p.is_file() and not p.is_symlink(),
         "TEMPLATE_MISSING_OR_SYMLINKED")
    return Template(p.read_text(encoding="utf-8")).substitute(**values)

def title(value):
    return " ".join(p.capitalize() for p in value.split("-"))

def module_path(m):
    k, ident = m["kind"], m["id"]
    return ("skills/" + ident + "/SKILL.md" if k == "skill" else
            ("phases/" if k == "phase" else "components/") + ident + ".md")

def preferences_markdown(slots):
    quote = chr(96)
    out = [
        "# Optional private presentation preferences", "",
        "This is a public **allowlist of possible options**, not a user profile.",
        "Honor safe current-task preferences. Persist only with explicit consent",
        "and an actual private host store; never package consumer values.",
        "Canonical accuracy, evidence and permission rules cannot be overridden.", "",
    ]
    for slot in slots:
        out.append("- " + quote + slot["key"] + quote + ": " +
                   ", ".join(quote + v + quote for v in slot["choices"]) +
                   "; default " + quote + slot["default"] + quote + ".")
    return "\n".join(out) + "\n"


def ordered_modules(modules):
    by_id = {m["id"]: m for m in modules}
    visiting, visited, result = set(), set(), []
    def visit(name):
        need(name in by_id, "UNKNOWN_MODULE_DEPENDENCY")
        need(name not in visiting, "CYCLIC_MODULE_DEPENDENCY")
        if name in visited:
            return
        visiting.add(name)
        for dep in by_id[name]["requires"]:
            if by_id[name]["required"]:
                need(dep in by_id and by_id[dep]["required"],
                     "REQUIRED_MODULE_DEPENDS_ON_OPTIONAL")
            visit(dep)
        visiting.remove(name)
        visited.add(name)
        result.append(name)
    for name in by_id:
        visit(name)
    return result


def generate_files(b):
    validate_blueprint(b)
    files = {"LICENSE": template("LICENSE.tmpl",
                                 copyright_holder=b["copyright_holder"])}
    preference_note = "No consumer preferences are stored by this skill."
    if b["preference_slots"]:
        files["preferences.md"] = preferences_markdown(b["preference_slots"])
        preference_note = (
            "[Allowed presentation options](preferences.md) describe possible "
            "settings, not saved user preferences.")
    if b["kind"] == "pack":
        ordered = ordered_modules(b["modules"])
        by_id = {m["id"]: m for m in b["modules"]}
        procedure = [
            "## Ordered module execution", "",
            "The pack has one required user outcome. Each module must produce",
            "its declared handoff; a green module alone cannot satisfy it.", "",
        ]
        normalized = []
        for name in ordered:
            m = by_id[name]
            path = module_path(m)
            data = {
                "name": m["id"], "kind": m["kind"], "title": title(m["id"]),
                "dependencies": ", ".join(m["requires"]) or "None",
                "authority": m["authority"],
                "instructions": m["instructions"], "output": m["output"],
                "fallback_note": ("**Optional fallback:** " + m["fallback"]
                                  if not m["required"] else
                                  "**Required:** HOLD when this handoff is unavailable."),
                "pack_name": b["name"],
                "qualified_name": b["name"] + "-" + m["id"],
                "description_yaml": json.dumps(
                    "Within " + b["name"] + ", " + m["output"].rstrip("."),
                    ensure_ascii=False),
                "trigger": b["trigger"], "non_trigger": b["non_trigger"],
            }
            files[path] = template(
                "subskill.md.tmpl" if m["kind"] == "skill" else
                "module.md.tmpl", **data)
            procedure.append(
                "- " + ("**Required** " if m["required"] else "**Optional** ") +
                "[" + name + "](" + path + "), after " +
                (", ".join(m["requires"]) or "the supplied input") + ": " +
                m["output"] + ("; fallback: " + m["fallback"]
                                if not m["required"] else ""))
            normalized.append({
                "id": name, "kind": m["kind"], "path": path,
                "requires": m["requires"], "required": m["required"],
                "fallback": m["fallback"], "authority": m["authority"],
                "output": m["output"], "origin": "original",
                "source_identity": "NONE", "rights_basis": "ORIGINAL",
            })
        manifest = {
            "schema_version": 1, "pack_id": b["name"],
            "capability": b["outcome"], "entrypoint": "SKILL.md",
            "completion": b["verification"], "authority": b["authority"],
            "license": "MIT", "files": [],
            "modules": normalized, "preference_slots": b["preference_slots"],
            "feedback_policy": dict(POLICY),
        }
        files["pack.json"] = ""
    else:
        procedure = ["## Procedure", ""]
        for i, step in enumerate(b["steps"], start=1):
            procedure += [
                "### " + str(i) + ". " + step["title"], "",
                step["instructions"], "",
                "**Handoff:** " + step["output"], "",
            ]
        manifest = None
    files["SKILL.md"] = template(
        "skill.md.tmpl", name=b["name"], title=title(b["name"]),
        description_yaml=json.dumps(b["description"], ensure_ascii=False),
        outcome=b["outcome"], trigger=b["trigger"],
        non_trigger=b["non_trigger"], inputs=b["inputs"],
        authority=b["authority"], procedure="\n".join(procedure),
        verification=b["verification"], failure_handling=b["failure_handling"],
        preference_note=preference_note)
    if manifest is not None:
        manifest["files"] = sorted(files)
        files["pack.json"] = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    return files


def write_files(root, files):
    root.mkdir(mode=0o700)
    for name, content in sorted(files.items()):
        parts = name.split("/")
        folder = root
        for part in parts[:-1]:
            folder = folder / part
            folder.mkdir(exist_ok=True)
            need(not folder.is_symlink(), "OUTPUT_PATH_SYMLINKED")
        with (root / name).open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
    for name, content in files.items():
        need((root / name).read_text(encoding="utf-8") == content,
             "OUTPUT_READBACK_FAILED:" + name)


def check_local_links(root, files):
    for name in files:
        if not name.endswith(".md"):
            continue
        text = (root / name).read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)\n]+)\)", text):
            relative = target.split("#", 1)[0]
            if not relative or relative.startswith(
                    ("https://", "http://", "mailto:", "data:")):
                continue
            parts = list(Path(name).parent.parts)
            if parts == ["."]:
                parts = []
            for part in relative.split("/"):
                if part in {"", "."}:
                    continue
                if part == "..":
                    need(bool(parts), "LINK_LEAVES_PACKAGE:" + name)
                    parts.pop()
                else:
                    parts.append(part)
            path = "/".join(parts)
            need(path in files, "MISSING_LOCAL_SUPPORT:" + name)
            check_pack.contained_file(root, path)


def verify_layout(root, b, files):
    for name in files:
        check_pack.contained_file(root, name)
    check_local_links(root, files)
    if b["kind"] == "pack":
        receipt = check_pack.validate(
            root, json.loads((root / "pack.json").read_text(encoding="utf-8")))
        return {"status": receipt["status"],
                "sequence": receipt["modules_order"]}
    return {"status": "SKILL_FILES_STRUCTURALLY_PRESENT_NOT_EXECUTED",
            "sequence": [s["id"] for s in b["steps"]]}


def output_target(raw, maintainer):
    need(raw is not None, "OUTPUT_REQUIRED_FOR_WRITE")
    target = Path(raw).expanduser().absolute()
    need(target.name not in {"", ".", ".."} and
         not target.exists() and not target.is_symlink(),
         "OUTPUT_EXISTS_OR_INVALID")
    parent = target.parent
    need(parent.is_dir(), "OUTPUT_PARENT_MISSING")
    for ancestor in (parent, *parent.parents):
        need(not ancestor.is_symlink(), "OUTPUT_ANCESTOR_SYMLINKED")
    if not maintainer:
        need(not target.is_relative_to(REPO_ROOT),
             "REPOSITORY_WRITE_REQUIRES_MAINTENANCE_SCOPE")
    return target


def build(blueprint, output=None, write=False, maintainer=False):
    files = generate_files(blueprint)
    with tempfile.TemporaryDirectory(prefix="skillz-build-") as folder:
        stage = Path(folder) / blueprint["name"]
        write_files(stage, files)
        evidence = verify_layout(stage, blueprint, files)
        digests = {
            name: hashlib.sha256(data.encode("utf-8")).hexdigest()
            for name, data in sorted(files.items())
        }
        destination = None
        if write:
            target = output_target(output, maintainer)
            # The new directory is exclusive, and individual files use
            # exclusive-create. Never overwrite even an empty target.
            # On a mid-copy error, a partial directory may remain and MUST
            # NOT be reported as a successful delivery.
            write_files(target, files)
            verify_layout(target, blueprint, files)
            destination = str(target)
        return {
            "schema_version": 1,
            "status": ("WRITTEN_DRAFT_REVIEW_REQUIRED" if write else
                       "RENDERED_DRAFT_PLAN_NOT_INSTALLED"),
            "kind": blueprint["kind"], "name": blueprint["name"],
            "files": sorted(files), "sha256": digests,
            "structural_check": evidence["status"],
            "sequence": evidence["sequence"], "destination": destination,
            "rights_authenticated": False,
            "semantic_task_quality_verified": False,
            "host_execution_observed": False,
            "consumer_outcome_accepted": False,
            "installed_or_published": False,
            "user_preference_persisted": False,
            "next_action": "REVIEW_WHOLE_PACKAGE_RIGHTS_AND_REAL_TASK_OUTCOMES",
        }


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", required=True)
    ap.add_argument("--output")
    ap.add_argument("--write", action="store_true",
                    help="Explicitly create a NEW output directory")
    ap.add_argument("--repository-maintenance", action="store_true",
                    help="Scope marker only, NOT proof of user or maintainer permission")
    args = ap.parse_args(argv)
    try:
        need(not args.repository_maintenance or args.write,
             "MAINTENANCE_FLAG_WITHOUT_WRITE")
        result = build(read_json(args.input), args.output, args.write,
                       args.repository_maintenance)
        print(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False))
        return 0
    except (BuildHold, check_pack.PackHold, ValueError, TypeError,
            OSError, UnicodeError, KeyError) as exc:
        print("SKILL_BUILD_HOLD: " + str(exc), file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
