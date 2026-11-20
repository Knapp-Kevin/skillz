#!/usr/bin/env python3
"""Check passive, exact-version model compatibility profiles. Stdlib only.

Manual maintainer command, NOT a CI job or model runner:
  python3 scripts/qa/check-model-compatibility-profiles.py
  python3 scripts/qa/check-model-compatibility-profiles.py --self-test

Reads checked-in JSON, existing YAML scalar companions, Git objects and skill
texts. Never edits sources, installs dependencies, runs models or calls network.
"""
import argparse
import copy
import datetime as dt
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "registry/model-compatibility"
SCHEMA_ID = "skillz/model-compatibility-profile/1"
UNKNOWN = "UNKNOWN"
CLAIMS = {"AUTHOR_CLAIM", "THIRD_PARTY_CLAIM",
          "STATIC_ASSESSMENT", "OBSERVED_TEST", "UNKNOWN"}


class ProfileError(ValueError):
    pass


def fail(message):
    raise ProfileError(message)


def require(condition, message):
    if not condition:
        fail(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def git(*args):
    return subprocess.check_output(
        ["git", "-C", str(ROOT), *args], text=True, timeout=15
    ).strip()


def check_date(text, field):
    try:
        parsed = dt.date.fromisoformat(text)
        require(parsed.isoformat() == text, f"{field}: use YYYY-MM-DD")
    except (ValueError, TypeError) as exc:
        fail(f"{field}: invalid YYYY-MM-DD: {exc}")


def check_schema(value, schema, location="$"):
    """Small explicit JSON Schema subset used by the checked-in schema.

    This is an additive integrity check, not a general-purpose JSON Schema
    implementation. It refuses unknown keys and exercises every keyword
    currently used by profile.schema.json.
    """
    if "oneOf" in schema:
        successful = 0
        for option in schema["oneOf"]:
            try:
                check_schema(value, option, location)
            except ProfileError:
                continue
            successful += 1
        require(successful == 1, f"{location}: exactly one schema branch required")
    kind = schema.get("type")
    if kind == "object":
        require(isinstance(value, dict), f"{location}: object expected")
        props = schema.get("properties", {})
        for key in schema.get("required", []):
            require(key in value, f"{location}.{key}: required")
        if schema.get("additionalProperties") is False:
            require(not (set(value) - set(props)),
                    f"{location}: unexpected fields {sorted(set(value) - set(props))}")
        for key, item in value.items():
            if key in props:
                check_schema(item, props[key], f"{location}.{key}")
    elif kind == "array":
        require(isinstance(value, list), f"{location}: array expected")
        require(len(value) >= schema.get("minItems", 0),
                f"{location}: too few entries")
        if schema.get("uniqueItems"):
            serialized = [json.dumps(x, sort_keys=True) for x in value]
            require(len(set(serialized)) == len(value),
                    f"{location}: duplicate entries")
        for index, item in enumerate(value):
            check_schema(item, schema["items"], f"{location}[{index}]")
    elif kind == "string":
        require(isinstance(value, str), f"{location}: string expected")
        require(len(value) >= schema.get("minLength", 0), f"{location}: too short")
        if "pattern" in schema:
            require(re.fullmatch(schema["pattern"], value) is not None,
                    f"{location}: invalid format")
        if schema.get("format") == "date":
            check_date(value, location)
    elif kind == "integer":
        require(type(value) is int, f"{location}: integer expected")
        require(value >= schema.get("minimum", value), f"{location}: below minimum")
    if "const" in schema:
        require(value == schema["const"], f"{location}: wrong immutable value")
    if "enum" in schema:
        require(value in schema["enum"], f"{location}: invalid vocabulary")


def scalar_yaml(path, field):
    text = path.read_text(encoding="utf-8")
    lines = [
        line.split(":", 1)[1].strip().strip('"').strip("'")
        for line in text.splitlines()
        if line.startswith(field + ":")
    ]
    require(len(lines) == 1, f"{path}: expected one {field}")
    return lines[0]


def markdown_slug(header):
    value = header.lower().strip()
    # GitHub headings: punctuation removed, spaces become hyphens.
    value = re.sub(r"[^\\w -]", "", value, flags=re.UNICODE)
    return value.replace(" ", "-")


def anchored_skill_pointer(pointer, path):
    prefix, divider, anchor = pointer.partition("#")
    require(divider == "#" and prefix == path and anchor,
            f"source_pointer must identify the pinned SKILL.md section: {pointer}")
    text = (ROOT / path).read_text(encoding="utf-8")
    headings = {markdown_slug(line.lstrip("#").strip()) for line in text.splitlines()
                if line.startswith("#")}
    require(anchor in headings, f"broken skill section #{anchor} at {path}")


def compatibility_freshness(source_changed=False, model_changed=False):
    """Return separate source review and model-claim freshness dimensions."""
    return {
        "source_review": "NEEDS-RE-REVIEW" if source_changed else "PIN_MATCH",
        "model_claim": "RECHECK_MODEL_CLAIM" if model_changed else "UNCHANGED_OR_UNKNOWN",
    }


def index_from_profiles(profiles):
    facets = {}
    for p in profiles:
        for path in p["capability_paths"]:
            facets.setdefault(path, []).append({
                "skill_identity": p["skill_identity"],
                "profile_revision": p["profile_revision"],
                "observed_effectiveness": p["observed_effectiveness"],
            })
    for items in facets.values():
        items.sort(key=lambda x: x["skill_identity"])
    return {k: facets[k] for k in sorted(facets)}


def check_profile(profile, schema, directory):
    check_schema(profile, schema)
    require(profile["schema_version"] == SCHEMA_ID, "wrong profile schema")
    ident = profile["skill_identity"]
    source = profile["source"]
    slug = ident.split("/")[-1]
    require(ident == "local-skills/" + slug, "source namespace mismatch")
    skillpath = f"skills/authored/{slug}/SKILL.md"
    require(source["skill_path"] == skillpath, f"{ident}: wrong path")
    companion_path = f"registry/verification/local-skills/{slug}.yaml"
    require(source["verification_companion"] == companion_path,
            f"{ident}: foreign verification companion")
    verify = ROOT / companion_path
    for field, value in [
        ("skill_name", slug),
        ("skill_version", profile["skill_version"]),
        ("content_blob_sha", source["skill_blob_sha1"]),
        ("complete_package_tree_sha", source["package_tree_sha1"]),
        ("reviewed_at", source["reviewed_at"]),
    ]:
        require(scalar_yaml(verify, field) == value,
                f"{ident}: verification companion {field} mismatch")
    require(source["checked_at"] >= source["reviewed_at"],
            f"{ident}: checked_at before reviewed_at")
    packagepath = f"skills/authored/{slug}"
    commit = source["snapshot_commit"]
    require(git("rev-parse", commit + ":" + skillpath) == source["skill_blob_sha1"],
            f"{ident}: PINNED SKILL.MD BLOB DOES NOT MATCH")
    require(git("rev-parse", commit + ":" + packagepath) ==
            source["package_tree_sha1"],
            f"{ident}: PINNED PACKAGE TREE DOES NOT MATCH")
    current_tree = git("rev-parse", "HEAD:" + packagepath)
    require(current_tree == source["package_tree_sha1"],
            f"{ident}: NEEDS-RE-REVIEW: current complete package changed")

    mapped = set()
    for domain in directory["domains"]:
        for sub in domain["subdomains"]:
            if ident in sub.get("matched_skill_ids", []):
                mapped.add(domain["id"] + "/" + sub["id"])
    for path in profile["capability_paths"]:
        require(path in mapped, f"{ident}: unverified capability route {path}")

    levels = []
    assertion_ids = set()
    for a in profile["assertions"]:
        require(a["id"] not in assertion_ids, f"{ident}: duplicate claim ID")
        assertion_ids.add(a["id"])
        require(a["evidence_level"] in CLAIMS, f"{ident}: invalid claim level")
        anchored_skill_pointer(a["source_pointer"], skillpath)
        has_test = "observed_test" in a
        require((a["evidence_level"] == "OBSERVED_TEST") == has_test,
                f"{ident}: test receipt must only accompany OBSERVED_TEST")
        if has_test:
            require(profile["model_context"]["exact_model"] != UNKNOWN,
                    f"{ident}: observed model version must be pinned")
            test = a["observed_test"]
            require(test["model_revision"] == profile["model_context"]["exact_model"],
                    f"{ident}: observed test model revision mismatch")
            receipt = test["execution_receipt"]
            require(not Path(receipt).is_absolute() and ".." not in Path(receipt).parts,
                    f"{ident}: unsafe test receipt path")
            require((ROOT / receipt).is_file(), f"{ident}: missing host test receipt")
        levels.append(a["evidence_level"])
    has_observed = "OBSERVED_TEST" in levels
    require((profile["observed_effectiveness"] != UNKNOWN) <= has_observed,
            f"{ident}: invented observed effectiveness")
    if not has_observed:
        require(profile["observed_effectiveness"] == UNKNOWN,
                f"{ident}: no observed execution is UNKNOWN")
    return {"identity": ident, "capabilities": profile["capability_paths"],
            "observed_effectiveness": profile["observed_effectiveness"],
            "source_review": "PIN_MATCH", "model_claim": "UNKNOWN"}


def validate():
    schema = read_json(BASE / "profile.schema.json")
    raw = read_json(BASE / "profiles.json")
    require(raw["schema_version"] ==
            "skillz/model-compatibility-profile-collection/1",
            "invalid collection schema")
    require(set(raw) == {"schema_version", "profiles"},
            "collection has unexpected fields")
    profiles = raw["profiles"]
    require(len(profiles) >= 3, "example tranche too small")
    ids = [p["skill_identity"] for p in profiles]
    require(len(ids) == len(set(ids)), "duplicate skill identity profiles")

    index = read_json(BASE / "by-capability.json")
    require(index["schema_version"] ==
            "skillz/model-compatibility-capability-facets/1", "index schema mismatch")
    require(index["canonical_capability_source"] ==
            "registry/capability-directory.json", "index source mismatch")
    require(index["profiles_source"] ==
            "registry/model-compatibility/profiles.json", "index profile source mismatch")
    require(index["facets"] == index_from_profiles(profiles),
            "capability browse facets stale or inflated")

    directory = read_json(ROOT / "registry/capability-directory.json")
    results = [check_profile(profile, schema, directory) for profile in profiles]

    presenter = read_json(BASE / "unverified-presenter-guidance.json")
    require(presenter["schema_version"] ==
            "skillz/unverified-presenter-prompting-leads/1", "presenter schema mismatch")
    for flag in ("model_identity_verified", "vendor_attribution_verified",
                 "video_content_independently_verified"):
        require(presenter[flag] is False, "presenter claim improperly promoted: " + flag)
    require(presenter["compatibility_evidence"] == "THIRD_PARTY_CLAIM" and
            presenter["effectiveness"] == UNKNOWN,
            "presenter claim improperly promoted to observed evidence")
    leads = presenter["guidance_leads"]
    require(len(leads) == 10 and {r["id"] for r in leads} == set(range(1, 11)),
            "owner-supplied ten claims missing/duplicated")
    return results


def self_test():
    schema = read_json(BASE / "profile.schema.json")
    original = read_json(BASE / "profiles.json")["profiles"][0]
    check_schema(original, schema)
    checks = 0
    def reject(mutator):
        nonlocal checks
        changed = copy.deepcopy(original)
        mutator(changed)
        try:
            check_schema(changed, schema)
        except ProfileError:
            checks += 1
            return
        fail("negative control unexpectedly accepted")
    reject(lambda p: p.update({"authority": "EXECUTE_ANYTHING"}))
    reject(lambda p: p.update({"unrecognized_runtime_permission": True}))
    reject(lambda p: p["source"].update({"skill_blob_sha1": "not-a-git-blob"}))
    reject(lambda p: p["source"].update({"reviewed_at": "yesterday"}))
    reject(lambda p: p["assertions"][0].update({"evidence_level": "PROVEN_FOR_ALL_MODELS"}))
    reject(lambda p: p["model_context"].update({"context_window_tokens": -1}))
    reject(lambda p: p["assertions"][0].update({"observed_test": {"fake": True}}))
    reject(lambda p: p["capability_paths"].append(p["capability_paths"][0]))
    require(compatibility_freshness(True, False) == {
        "source_review": "NEEDS-RE-REVIEW", "model_claim": "UNCHANGED_OR_UNKNOWN"},
        "source change wrongly treated as model-only drift")
    require(compatibility_freshness(False, True) == {
        "source_review": "PIN_MATCH", "model_claim": "RECHECK_MODEL_CLAIM"},
        "model change wrongly staled the immutable skill")
    checks += 2
    print(json.dumps({"negative_and_freshness_controls": checks, "status": "PASS"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            self_test()
        print(json.dumps({"profiles": validate(), "status": "PASS"},
                         indent=2, sort_keys=True))
    except (ProfileError, ValueError, subprocess.CalledProcessError,
            FileNotFoundError, KeyError, TypeError) as exc:
        print(f"MODEL_COMPATIBILITY_PROFILE_CHECK_FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
