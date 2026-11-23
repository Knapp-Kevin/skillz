#!/usr/bin/env python3
"""Offline release chain reconciliation for supplied claims + actual local bytes.

No network, package installation, signature verification, GitHub access,
release publication, executable extraction, or automatic writes.
Python >=3.9 standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys

MAX_JSON = 1_048_576
MAX_ARTIFACT_BYTES = 134_217_728
MAX_CHANNELS = 32
SHA1 = re.compile(r"^[0-9a-f]{40}$")
SHA256 = re.compile(r"^[0-9a-f]{64}$")
IDENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_+./:@-]{0,127}$")
FILENAME = re.compile(r"^[A-Za-z0-9._@+-][A-Za-z0-9._@+/-]{0,254}$")
CHECK_STATES = {"success", "failure", "pending", "cancelled", "skipped", "unknown"}
INSTALL_STATES = {"reported_pass", "reported_fail", "not_run"}
ATTEST_STATES = {"reported_verified", "reported_failed", "not_run"}


class Invalid(ValueError):
    pass


def need(ok, error):
    if not ok:
        raise Invalid(error)


def fields(value, required, optional=(), where="record"):
    need(isinstance(value, dict), where + ": object required")
    need(set(required).issubset(value), where + ": missing required fields")
    need(not (set(value) - set(required) - set(optional)),
         where + ": unexpected field")


def ident(v, label):
    need(isinstance(v, str) and IDENT.fullmatch(v) is not None,
         label + ": invalid identifier")
    return v


def sha(v, regex, label):
    need(isinstance(v, str) and regex.fullmatch(v) is not None,
         label + ": full lowercase digest required")
    return v


def safe_filename(name):
    need(isinstance(name, str) and FILENAME.fullmatch(name) is not None and
         not name.startswith("/") and "\\" not in name and
         all(p not in ("", ".", "..") for p in name.split("/")),
         "INVALID_LOCAL_ARTIFACT_PATH")
    return name


def unique_json_keys(pairs):
    obj = {}
    for k, v in pairs:
        need(k not in obj, "DUPLICATE_JSON_KEY")
        obj[k] = v
    return obj


def read_json(path):
    p = Path(path).absolute()
    need(p.is_file() and not any(a.is_symlink() for a in (p, *p.parents)),
         "JSON_PATH_MISSING_OR_SYMLINKED")
    need(p.stat().st_size <= MAX_JSON, "INPUT_JSON_TOO_LARGE")
    with p.open(encoding="utf-8") as stream:
        return json.load(stream, object_pairs_hook=unique_json_keys,
                         parse_constant=lambda _: (_ for _ in ()).throw(
                             Invalid("NONFINITE_JSON")))


def local_digest(root, relative):
    """Hash regular local bytes from a non-symlinked bounded directory.

    Not a sandbox: callers must provide an authorized *stable/isolated*
    local snapshot. Directory-write races require host containment.
    """
    name = safe_filename(relative)
    base = Path(root).absolute()
    need(base.is_dir() and not any(p.is_symlink() for p in (base, *base.parents)),
         "ARTIFACT_ROOT_MISSING_OR_SYMLINKED")
    parent = base
    for component in name.split("/")[:-1]:
        parent = parent / component
        need(parent.is_dir() and not parent.is_symlink(),
             "ARTIFACT_PARENT_MISSING_OR_SYMLINKED")
    p = parent / name.split("/")[-1]
    need(not p.is_symlink(), "ARTIFACT_SYMLINK_REFUSED")
    # O_NOFOLLOW is available on supported hosted Linux. Never silently
    # follow a leaf symlink on systems that lack this flag.
    need(hasattr(os, "O_NOFOLLOW"), "NOFOLLOW_UNAVAILABLE")
    flags = os.O_RDONLY | os.O_NOFOLLOW
    if hasattr(os, "O_NONBLOCK"):
        flags |= os.O_NONBLOCK
    fd = os.open(str(p), flags)
    try:
        info = os.fstat(fd)
        need(stat.S_ISREG(info.st_mode), "ARTIFACT_NOT_REGULAR_FILE")
        need(0 <= info.st_size <= MAX_ARTIFACT_BYTES,
             "ARTIFACT_TOO_LARGE")
        digest = hashlib.sha256()
        size = 0
        with os.fdopen(os.dup(fd), "rb", closefd=True) as f:
            while True:
                chunk = f.read(min(1 << 20, MAX_ARTIFACT_BYTES + 1 - size))
                if not chunk:
                    break
                size += len(chunk)
                need(size <= MAX_ARTIFACT_BYTES, "ARTIFACT_TOO_LARGE")
                digest.update(chunk)
        need(size == info.st_size, "ARTIFACT_SIZE_CHANGED_DURING_READ")
        return digest.hexdigest(), size
    finally:
        os.close(fd)


def inspect(data, root):
    fields(data, ("schema_version", "source", "build", "channels"),
           where="release")
    need(type(data["schema_version"]) is int and data["schema_version"] == 1,
         "UNSUPPORTED_SCHEMA")
    source = data["source"]
    fields(source, ("repository", "commit", "tag", "tag_target"), where="source")
    ident(source["repository"], "repository")
    ident(source["tag"], "tag")
    sha(source["commit"], SHA1, "source commit")
    sha(source["tag_target"], SHA1, "tag target")
    build = data["build"]
    fields(build, ("source_commit", "run_id", "conclusion", "checks_complete",
                   "required_checks", "checks"), where="build")
    sha(build["source_commit"], SHA1, "build source commit")
    ident(build["run_id"], "run ID")
    need(build["conclusion"] in ("success", "failure", "pending", "unknown"),
         "INVALID_BUILD_CONCLUSION")
    need(type(build["checks_complete"]) is bool, "INVALID_CHECK_COMPLETENESS")
    need(isinstance(build["required_checks"], list) and
         0 < len(build["required_checks"]) <= 64, "INVALID_REQUIRED_CHECKS")
    required = set()
    for check in build["required_checks"]:
        fields(check, ("name", "app"), where="required check")
        key = (ident(check["name"], "check name"), ident(check["app"], "check app"))
        need(key not in required, "DUPLICATE_REQUIRED_CHECK")
        required.add(key)
    need(isinstance(build["checks"], list) and len(build["checks"]) <= 128,
         "INVALID_OBSERVED_CHECKS")
    observed = {}
    for check in build["checks"]:
        fields(check, ("name", "app", "state", "head_sha"), where="observed check")
        key = (ident(check["name"], "check name"), ident(check["app"], "check app"))
        need(key not in observed, "DUPLICATE_OBSERVED_CHECK")
        need(check["state"] in CHECK_STATES, "INVALID_CHECK_STATE")
        sha(check["head_sha"], SHA1, "check HEAD")
        observed[key] = check

    blocked = []
    holds = []
    if source["tag_target"] != source["commit"]:
        blocked.append("TAG_TARGET_DIFFERS_FROM_SOURCE")
    if build["source_commit"] != source["commit"]:
        blocked.append("BUILD_SOURCE_DIFFERS_FROM_RELEASE")
    if build["conclusion"] == "failure":
        blocked.append("BUILD_REPORTED_FAILED")
    elif build["conclusion"] != "success":
        holds.append("BUILD_SUCCESS_NOT_OBSERVED")
    if not build["checks_complete"]:
        holds.append("REQUIRED_CHECK_INVENTORY_INCOMPLETE")
    for name, app in sorted(required):
        key = (name, app)
        label = name + "@" + app
        check = observed.get(key)
        if check is None:
            holds.append("REQUIRED_CHECK_MISSING:" + label)
        elif check["head_sha"] != source["commit"]:
            holds.append("REQUIRED_CHECK_STALE_HEAD:" + label)
        elif check["state"] == "failure":
            blocked.append("REQUIRED_CHECK_REPORTED_FAILED:" + label)
        elif check["state"] != "success":
            holds.append("REQUIRED_CHECK_NOT_SUCCESS:" + label)

    channels = data["channels"]
    need(isinstance(channels, list) and 0 < len(channels) <= MAX_CHANNELS,
         "INVALID_CHANNEL_COUNT")
    seen = set()
    output = []
    for item in channels:
        fields(item, ("id", "platform", "architecture", "filename",
                      "build_sha256", "published_sha256_claim",
                      "provenance", "install"), where="channel")
        key = ident(item["id"], "channel")
        need(key not in seen, "DUPLICATE_CHANNEL_ID")
        seen.add(key)
        ident(item["platform"], "platform")
        ident(item["architecture"], "architecture")
        safe_filename(item["filename"])
        for field_name in ("build_sha256", "published_sha256_claim"):
            sha(item[field_name], SHA256, field_name)
        if item["build_sha256"] != item["published_sha256_claim"]:
            blocked.append("DECLARED_BUILD_PUBLISH_DIGEST_DIFFER:" + key)
        provenance = item["provenance"]
        fields(provenance, ("status", "subject_sha256", "source_commit",
                           "repository", "verifier_receipt"), where="provenance")
        need(provenance["status"] in ATTEST_STATES, "INVALID_ATTEST_STATUS")
        sha(provenance["subject_sha256"], SHA256, "provenance subject digest")
        sha(provenance["source_commit"], SHA1, "provenance source")
        ident(provenance["repository"], "provenance repository")
        if provenance["status"] == "reported_failed":
            blocked.append("ATTESTATION_REPORTED_FAILED:" + key)
        elif provenance["status"] != "reported_verified":
            holds.append("ATTESTATION_NOT_VERIFIED_EXTERNALLY:" + key)
        if provenance["verifier_receipt"] is None:
            holds.append("ATTESTATION_VERIFIER_RECEIPT_MISSING:" + key)
        else:
            ident(provenance["verifier_receipt"], "verifier receipt")
        if provenance["subject_sha256"] != item["build_sha256"]:
            blocked.append("ATTESTATION_SUBJECT_DIGEST_DIFFERS:" + key)
        if provenance["source_commit"] != source["commit"] or (
                provenance["repository"] != source["repository"]):
            blocked.append("ATTESTATION_SOURCE_OR_REPO_DIFFERS:" + key)
        install = item["install"]
        fields(install, ("status", "artifact_sha256", "receipt"), where="install")
        need(install["status"] in INSTALL_STATES, "INVALID_INSTALL_STATUS")
        sha(install["artifact_sha256"], SHA256, "install artifact digest")
        if install["artifact_sha256"] != item["build_sha256"]:
            blocked.append("INSTALL_ARTIFACT_DIGEST_DIFFERS:" + key)
        if install["status"] == "reported_fail":
            blocked.append("INSTALL_REPORTED_FAILED:" + key)
        elif install["status"] != "reported_pass":
            holds.append("INSTALL_NOT_TESTED:" + key)
        if install["receipt"] is None:
            holds.append("INSTALL_RECEIPT_MISSING:" + key)
        else:
            ident(install["receipt"], "install receipt")
        local = None
        try:
            local, size = local_digest(root, item["filename"])
            if local != item["published_sha256_claim"]:
                blocked.append("LOCAL_PUBLISHED_BYTES_DIGEST_DIFFERS:" + key)
            output.append({"id": key, "file_size": size,
                           "actual_local_sha256": local,
                           "matches_published_claim": (
                               local == item["published_sha256_claim"])})
        except (Invalid, OSError) as exc:
            holds.append("LOCAL_ARTIFACT_UNAVAILABLE_OR_UNSAFE:" + key)
            output.append({"id": key, "file_size": None,
                           "actual_local_sha256": None,
                           "matches_published_claim": False})
    status = ("BLOCKED_CONTRADICTORY_EVIDENCE" if blocked else
              "HOLD_INCOMPLETE_EVIDENCE" if holds else
              "LOCAL_BYTE_CHAIN_MATCHED_UNTRUSTED_RECEIPTS")
    return {"schema_version": 1, "status": status,
            "claimed_repository": source["repository"],
            "claimed_source_commit": source["commit"],
            "declared_channel_count": len(channels),
            "local_artifacts": output,
            "blockers": sorted(set(blocked)),
            "holds": sorted(set(holds)),
            "build_provider_authenticated": False,
            "external_attestation_signature_verified_by_this_tool": False,
            "publisher_or_download_origin_authenticated": False,
            "installer_execution_observed_by_this_tool": False,
            "installed_product_accepted": False,
            "release_authorized": False,
            "scope": "LOCAL_BYTES_PLUS_CALLER_ASSERTED_RELEASE_CHAIN_ONLY"}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manifest", required=True)
    p.add_argument("--artifact-root", required=True)
    p.add_argument("--require-local-match", action="store_true")
    args = p.parse_args()
    try:
        result = inspect(read_json(args.manifest), args.artifact_root)
        print(json.dumps(result, sort_keys=True, indent=2))
        return 3 if args.require_local_match and result["status"] != (
            "LOCAL_BYTE_CHAIN_MATCHED_UNTRUSTED_RECEIPTS") else 0
    except (Invalid, ValueError, TypeError, KeyError, OSError, UnicodeError) as exc:
        print("RELEASE_HOLD: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
