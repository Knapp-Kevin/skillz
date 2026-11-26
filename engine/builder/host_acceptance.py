#!/usr/bin/env python3
"""Offline consistency check for bounded, externally recorded host trials.

No installation, model invocation, authentication, publication or receipt
persistence. Input observations are claims; a coherent receipt is not proof.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parent))
import host_compat

HEX40 = re.compile(r"[0-9a-f]{40}")
HEX64 = re.compile(r"[0-9a-f]{64}")
SLUG = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*")
ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,79}")
UNKNOWN_IDS = frozenset({"unknown", "not-run", "not_run", "unset", "none", "na", "n-a", "n.a", "placeholder"})
STAGES = ("load", "positive_trigger", "near_non_trigger", "outcome",
          "authority_boundary", "cleanup")
FIELDS = {"schema_version", "skill", "host", "source_commit", "package_tree_sha",
          "asset", "sha256", "manifest_sha256", "environment", "execution_kind",
          "authorization", "cases"}
ENV_FIELDS = {"surface", "host_version", "model", "configuration_id",
              "isolation_id", "actor_id"}
CASE_FIELDS = {"stage", "status", "evidence_id", "oracle_id"}
MAX_JSON = 8 * 1024 * 1024
MAX_ARCHIVE = 200 * 1024 * 1024


def require(ok, code):
    if not ok:
        raise ValueError(code)


def unique_keys(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, "DUPLICATE_JSON_KEY")
        out[k] = v
    return out


def local_file(path, limit):
    p = Path(path).absolute()
    require(p.is_file() and not p.is_symlink() and
            not any(parent.is_symlink() for parent in p.parents) and
            p.stat().st_size <= limit, "INVALID_LOCAL_INPUT")
    return p


def read_json(path):
    data = local_file(path, MAX_JSON).read_bytes()
    def reject_constant(_):
        raise ValueError("NONFINITE_JSON")
    return json.loads(data, object_pairs_hook=unique_keys,
                      parse_constant=reject_constant), hashlib.sha256(data).hexdigest()


def valid(pattern, value):
    return type(value) is str and bool(pattern.fullmatch(value))


def evidence_identity(value):
    return valid(ID, value) and value.casefold() not in UNKNOWN_IDS


def archive_contract(skill, host, asset):
    """Known distribution routes only; an unknown future adapter fails closed."""
    require(host in host_compat.HOSTS, "HOST_UNASSESSED")
    if host.startswith("m365-"):
        require(asset == skill + "-m365.zip", "HOST_ASSET_LAYOUT_MISMATCH")
        return "", "LICENSE.txt"
    if host == "gemini-apps":
        require(asset == skill + "-gemini.zip", "HOST_ASSET_LAYOUT_MISMATCH")
        return "", "LICENSE.txt"
    if host == "claude-apps":
        require(asset in (skill + ".zip", skill + "-claude.zip"),
                "HOST_ASSET_LAYOUT_MISMATCH")
        return skill + "/", "LICENSE"
    require(host_compat.HOSTS[host]["mode"] == "directory" and asset == skill + ".zip",
            "HOST_ASSET_LAYOUT_MISMATCH")
    return skill + "/", "LICENSE"


def check_archive_layout(stream, prefix, license_name):
    """Inspect the central directory only; never extract or execute payloads."""
    try:
        with zipfile.ZipFile(stream) as z:
            members = z.infolist()
            require(0 < len(members) <= 10000 and
                    sum(m.file_size for m in members) <= MAX_ARCHIVE,
                    "ARCHIVE_INVENTORY_LIMIT")
            names = []
            for m in members:
                name = m.orig_filename
                mode = (m.external_attr >> 16) & 0o170000
                require(not m.is_dir() and not (m.flag_bits & 1) and
                        mode in (0, 0o100000) and
                        name.startswith(prefix) and name == m.filename,
                        "INVALID_ARCHIVE_MEMBER")
                rel = name[len(prefix):]
                require(bool(rel) and all(p not in ("", ".", "..") for p in rel.split("/")),
                        "INVALID_ARCHIVE_MEMBER")
                names.append(rel)
            require(len(names) == len(set(names)) and
                    not host_compat.portable_path_blockers(names),
                    "NONPORTABLE_ARCHIVE_INVENTORY")
            require({"SKILL.md", license_name} <= set(names),
                    "MISSING_ARCHIVE_ENTRYPOINT_OR_LICENSE")
    except (zipfile.BadZipFile, NotImplementedError):
        raise ValueError("INVALID_ZIP_ARCHIVE") from None


def validate(manifest, manifest_sha, archive, receipt):
    require(type(receipt) is dict and set(receipt) == FIELDS and
            type(receipt["schema_version"]) is int and receipt["schema_version"] == 1,
            "INVALID_RECEIPT_FIELDS")
    require(type(manifest) is dict and type(manifest.get("schema_version")) is int
            and manifest["schema_version"] == 1 and
            valid(HEX40, manifest.get("source_commit")) and
            type(manifest.get("skills")) is list, "INVALID_MANIFEST")
    require(valid(HEX64, manifest_sha) and receipt["manifest_sha256"] == manifest_sha
            and receipt["source_commit"] == manifest["source_commit"],
            "MANIFEST_OR_SOURCE_MISMATCH")
    skill, host = receipt["skill"], receipt["host"]
    require(valid(SLUG, skill) and valid(SLUG, host), "INVALID_SKILL_OR_HOST")
    require(host in host_compat.HOSTS, "HOST_UNASSESSED")
    rows = [r for r in manifest["skills"] if type(r) is dict and r.get("id") == skill]
    require(len(rows) == 1, "SKILL_MISSING_OR_DUPLICATE")
    row = rows[0]
    require(valid(HEX40, row.get("package_tree_sha")) and
            receipt["package_tree_sha"] == row["package_tree_sha"], "PACKAGE_TREE_MISMATCH")
    profiles = row.get("hosts")
    require(type(profiles) is dict and type(profiles.get(host)) is dict,
            "HOST_UNASSESSED")
    selected = profiles[host]
    require(selected.get("status") == "PACKAGE_READY" and selected.get("blockers") == [],
            "HOST_PACKAGE_HOLD")
    asset, digest = selected.get("asset"), selected.get("sha256")
    require(asset in {skill + ".zip", skill + "-claude.zip", skill + "-gemini.zip",
                      skill + "-m365.zip"} and valid(HEX64, digest) and
            receipt["asset"] == asset and receipt["sha256"] == digest,
            "HOST_ASSET_IDENTITY_MISMATCH")
    prefix, license_name = archive_contract(skill, host, asset)
    p = local_file(archive, MAX_ARCHIVE)
    require(p.name == asset, "ARCHIVE_NAME_MISMATCH")
    with p.open("rb") as stream:
        actual = hashlib.sha256()
        size = 0
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            size += len(chunk)
            require(size <= MAX_ARCHIVE, "ARCHIVE_SIZE_LIMIT")
            actual.update(chunk)
        require(actual.hexdigest() == digest, "ARCHIVE_DIGEST_MISMATCH")
        stream.seek(0)
        check_archive_layout(stream, prefix, license_name)
    env = receipt["environment"]
    require(type(env) is dict and set(env) == ENV_FIELDS and
            all(valid(ID, v) for v in env.values()), "INVALID_ENVIRONMENT_IDENTITY")
    unknown_env = any(not evidence_identity(v) for v in env.values())
    require(receipt["execution_kind"] in ("NATIVE_HOST_CLAIMED", "EMULATED", "NOT_RUN"),
            "INVALID_EXECUTION_KIND")
    require(receipt["authorization"] in ("APPROVAL_CLAIMED", "NOT_ESTABLISHED"),
            "INVALID_AUTHORIZATION_STATE")
    cases = receipt["cases"]
    require(type(cases) is list and len(cases) == len(STAGES), "INCOMPLETE_STAGE_MATRIX")
    by_stage = {}
    ids = set()
    for case in cases:
        require(type(case) is dict and set(case) == CASE_FIELDS and
                type(case["stage"]) is str and case["stage"] in STAGES and
                case["stage"] not in by_stage, "INVALID_OR_DUPLICATE_STAGE")
        status = case["status"]
        require(status in ("PASS_CLAIMED", "FAIL_CLAIMED", "NOT_RUN", "UNKNOWN"),
                "INVALID_STAGE_STATUS")
        if status in ("PASS_CLAIMED", "FAIL_CLAIMED"):
            evidence, oracle = case["evidence_id"], case["oracle_id"]
            require(evidence_identity(evidence) and evidence_identity(oracle) and evidence != oracle and
                    evidence not in ids and oracle not in ids, "MISSING_OR_REUSED_EVIDENCE")
            ids.update((evidence, oracle))
        else:
            require(case["evidence_id"] is None and case["oracle_id"] is None,
                    "UNOBSERVED_STAGE_HAS_EVIDENCE_CLAIM")
        by_stage[case["stage"]] = status
    require(set(by_stage) == set(STAGES), "INCOMPLETE_STAGE_MATRIX")
    if receipt["execution_kind"] == "NOT_RUN":
        require(not any(v.endswith("_CLAIMED") for v in by_stage.values()),
                "NOT_RUN_WITH_OBSERVATION_CLAIM")
    if by_stage["load"] != "PASS_CLAIMED":
        require(not any(by_stage[s] == "PASS_CLAIMED" for s in
                        ("positive_trigger", "near_non_trigger", "outcome", "authority_boundary")),
                "BEHAVIOR_PASS_WITHOUT_LOAD")
    if by_stage["positive_trigger"] != "PASS_CLAIMED":
        require(by_stage["outcome"] != "PASS_CLAIMED", "OUTCOME_PASS_WITHOUT_TRIGGER")
    if any(v == "FAIL_CLAIMED" for v in by_stage.values()):
        status = "HOLD_REPORTED_FAILURE"
    elif (receipt["execution_kind"] != "NATIVE_HOST_CLAIMED" or
          receipt["authorization"] != "APPROVAL_CLAIMED" or unknown_env or
          any(v != "PASS_CLAIMED" for v in by_stage.values())):
        status = "HOLD_INCOMPLETE_NATIVE_CLAIM"
    else:
        status = "COMPLETE_CLAIMS_REVIEW_REQUIRED"
    return {"schema_version": 1, "status": status, "skill": skill, "host": host,
            "manifest_sha256": manifest_sha, "archive_sha256": digest,
            "source_commit": receipt["source_commit"], "package_tree_sha": receipt["package_tree_sha"],
            "asset": asset, "archive_directory_layout_checked": True,
            "archive_payload_crc_verified": False,
            "stage_claims": by_stage, "local_archive_matches_manifest": True,
            "case_ledger_reconciled": False,
            "manifest_authenticity_verified": False, "authorization_verified": False,
            "host_execution_observed": False, "independent_oracles_verified": False,
            "consumer_accepted": False, "installed_or_published": False,
            "next_action": "INDEPENDENTLY_REVIEW_PRIVATE_EVIDENCE_AND_ACTUAL_HOST"}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--archive", required=True)
    ap.add_argument("--receipt", required=True)
    args = ap.parse_args(argv)
    try:
        manifest, digest = read_json(args.manifest)
        receipt, receipt_digest = read_json(args.receipt)
        result = validate(manifest, digest, args.archive, receipt)
        result["receipt_sha256"] = receipt_digest
    except (OSError, ValueError, TypeError, KeyError, RecursionError):
        # Do not echo raw private receipt values or local paths.
        print(json.dumps({"status": "HOLD_INVALID_RECEIPT_OR_ARTIFACT",
                          "host_execution_observed": False}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "COMPLETE_CLAIMS_REVIEW_REQUIRED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
