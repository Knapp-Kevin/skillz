#!/usr/bin/env python3
"""Explicit offline maintenance export. No source activation, network or admission.

Requires Python 3 and PyYAML. Run from a clean, pinned source snapshot, supplying
its independently resolved upstream commit and tree. --check never writes.
"""
import argparse
import collections
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

import yaml


class UniqueLoader(yaml.SafeLoader):
    pass


def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def git(root, *args):
    return subprocess.check_output(["git", "-c", "core.fsmonitor=false", "-C", str(root), *args])


def safe_path(root, relative):
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts or "\\" in relative:
        raise ValueError(f"unsafe source path: {relative}")
    result = root.joinpath(*path.parts)
    if result.is_symlink() or not result.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"source escapes snapshot: {relative}")
    return result


def _source_git_identity(provenance, verification):
    """Normalize explicitly recorded Git blob/tree claims; never invent rights.

    Only the known v1 Git fingerprint algorithms define what content_blob_sha
    means. An alias disagreement is a refusal, not first-nonempty-wins.
    """
    algorithm = verification["fingerprint_algorithm"]
    recorded = verification["content_blob_sha"]

    def collect(kind, candidates):
        known = []
        for label, value in candidates:
            if value is None or value == "":
                continue
            if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{40}", value):
                raise ValueError(f"invalid {kind} Git object claim: {label}")
            known.append((label, value))
        if len({value for _, value in known}) > 1:
            raise ValueError(f"contradictory {kind} Git object claims: " +
                             ", ".join(label for label, _ in known))
        return known[0][1] if known else None

    blob = [
        ("verification.skill_md_blob_sha", verification.get("skill_md_blob_sha")),
        ("verification.skill_blob_sha", verification.get("skill_blob_sha")),
        ("provenance.skill_md_blob_sha", provenance.get("skill_md_blob_sha")),
        ("provenance.skill_blob_sha", provenance.get("skill_blob_sha")),
    ]
    tree = [
        ("verification.complete_package_tree_sha",
         verification.get("complete_package_tree_sha")),
        ("verification.package_tree_sha", verification.get("package_tree_sha")),
        ("provenance.complete_package_tree_sha",
         provenance.get("complete_package_tree_sha")),
        ("provenance.package_tree_sha", provenance.get("package_tree_sha")),
    ]
    if algorithm in ("git-blob-sha1", "git-tree-and-blob-sha1"):
        blob.append(("verification.content_blob_sha", recorded))
    elif algorithm == "git-tree-sha1":
        tree.append(("verification.content_blob_sha", recorded))
    # Unknown algorithms are preserved as recorded evidence but never
    # coerced into a Git SHA-1 or asserted as package identity.
    entry_blob = collect("SKILL.md blob", blob)
    package_tree = collect("package tree", tree)
    if algorithm == "git-tree-and-blob-sha1" and (
            entry_blob is None or package_tree is None):
        raise ValueError("combined tree/blob review missing exact source identities")
    return entry_blob, package_tree


def build(root, commit, tree):
    if not all(re.fullmatch(r"[0-9a-f]{40}", v) for v in (commit, tree)):
        raise ValueError("explicit exact Git commit and tree are required")
    actual_tree = git(root, "rev-parse", "HEAD^{tree}").decode().strip()
    if actual_tree != tree:
        raise ValueError("local HEAD tree differs from independently pinned source tree")
    inventory, gitlinks, blobs = [], [], {}
    for entry in git(root, "ls-tree", "-rz", "--full-tree", "HEAD").split(b"\0"):
        if not entry:
            continue
        header, raw_path = entry.split(b"\t", 1)
        mode, kind, sha = header.decode().split()
        relative = raw_path.decode()
        # Generated handoffs are not source inputs to the next handoff.
        if relative.startswith("registry/exports/"):
            continue
        if kind == "commit":
            gitlinks.append({"path": relative, "pinned_commit": sha, "materialization": "not-asserted"})
            continue
        if kind != "blob" or mode not in ("100644", "100755"):
            raise ValueError(f"unsupported source entry: {relative} ({mode})")
        raw = safe_path(root, relative).read_bytes()
        observed = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        if observed != sha:
            raise ValueError(f"working source differs from pinned tree: {relative}")
        blobs[relative] = raw
        inventory.append({"path": relative, "git_blob_sha1": sha, "sha256": digest(raw), "bytes": len(raw)})

    def load_json(relative):
        return json.loads(blobs[relative])

    def load_yaml(relative):
        return yaml.load(blobs[relative], Loader=UniqueLoader)

    directory = load_json("registry/capability-directory.json")
    names = load_json("registry/governed-review-name-index.json")
    mapped, hints = collections.defaultdict(list), collections.defaultdict(list)
    for domain in directory["domains"]:
        for sub in domain["subdomains"]:
            route = domain["id"] + "/" + sub["id"]
            for identity in sub["matched_skill_ids"]:
                mapped[identity].append(route)
            for identity in sub.get("name_only_review_candidate_ids", []):
                hints[identity].append(route)
    records = []
    provenance_paths = sorted(p for p in blobs if p.startswith("registry/skills/") and p.endswith(".yaml"))
    expected_verification = {p.replace("registry/skills/", "registry/verification/", 1) for p in provenance_paths}
    actual_verification = {p for p in blobs if p.startswith("registry/verification/") and p.endswith(".yaml")}
    if expected_verification != actual_verification:
        raise ValueError("orphaned provenance or verification companion")
    for provenance_path in provenance_paths:
        verification_path = provenance_path.replace("registry/skills/", "registry/verification/", 1)
        p, v = load_yaml(provenance_path), load_yaml(verification_path)
        if (p["source_id"], p["skill_name"]) != (v["source_id"], v["skill_name"]):
            raise ValueError(f"paired identity mismatch: {provenance_path}")
        record_id = provenance_path[len("registry/skills/"):-5]
        source_class = "first-party" if record_id.startswith("local-skills/") else "third-party"
        algorithm = v["fingerprint_algorithm"]
        entry_blob, package_tree = _source_git_identity(p, v)
        local_package = None
        local_entrypoint_match = "not-assessed"
        local_path = v.get("local_path") or p.get("local_path")
        if source_class == "first-party" and local_path:
            if local_path.endswith("/SKILL.md") and local_path in blobs:
                entry_raw = blobs[local_path]
                observed_entry = hashlib.sha1(b"blob " + str(len(entry_raw)).encode() + b"\0" + entry_raw).hexdigest()
                local_entrypoint_match = "match" if entry_blob == observed_entry else "mismatch-or-unresolved"
                prefix = local_path[:-len("SKILL.md")]
                files = [{"path": path[len(prefix):], "sha256": digest(raw)} for path, raw in sorted(blobs.items()) if path.startswith(prefix)]
                local_package = {"algorithm": "sha256-of-canonical-file-list-v1", "sha256": digest(canonical(files).encode()), "files": files}
        raw_status = v["verification_status"]
        records.append({
            "schema_version": "skill-mason-catalog-record-v1",
            "record_id": record_id,
            "declared_identity": {"source_id": p["source_id"], "skill_name": p["skill_name"]},
            "source_class": source_class,
            "origin": {"repository": p["source_repository"], "path": p["source_path"], "recorded_pin": p.get("source_snapshot_revision"), "first_party_snapshot_pin": commit if source_class == "first-party" else None},
            "identity": {"recorded_fingerprint_algorithm": algorithm, "recorded_fingerprint": v["content_blob_sha"], "entrypoint_git_blob_sha1": entry_blob, "package_git_tree_sha1": package_tree, "local_package": local_package},
            "capability_mapping": {"evidence_linked_paths": sorted(set(mapped[record_id])), "name_only_hints": sorted(set(hints[record_id])), "state": "evidence-linked" if mapped[record_id] else "unmapped", "unmapped_does_not_mean_absent": True},
            "review": {"semantic_status": raw_status, "rubric_score": v["rubric_score"], "fingerprint_basis": v["verification_basis"], "original_review_date": str(v["reviewed_at"]) if v.get("reviewed_at") else None, "recorded_last_verified_at": str(v["last_verified_at"]) if v.get("last_verified_at") else None, "recorded_characterized_at": str(v["characterized_at"]), "behavioral_status": v["validation_status"], "tags": v["tags"]},
            "security": {"recorded_package_status": v.get("package_security_status") or v.get("package_security_scan"), "status_if_not_recorded": "unknown-not-inferred", "additional_evidence_root": "registry/security/"},
            "freshness": {"recorded_source_check_date": str(p["last_checked_at"]) if p.get("last_checked_at") else None, "local_entrypoint_review_match": local_entrypoint_match, "upstream_head_freshness": "not-assessed-by-export"},
            "rights": {"recorded_license": p["license"], "recorded_terms_status": p.get("license_terms_status"), "package_redistribution_clearance": "not-established-by-export"},
            "operation": {"recorded_authority": p.get("permission_tier") or p.get("permissions"), "recorded_portability": p["portability"], "recorded_dependency_status": p["dependency_status"], "target_host_fit": "not-assessed"},
            "composition": {"eligibility": "not-assessed", "composable_method_contract": None, "export_is_not_admission_or_permission": True},
            "evidence": {"provenance": provenance_path, "verification": verification_path},
        })
    actual_ids = {r["record_id"] for r in records}
    index_ids = set(names["first_party_ids"] + names["third_party_ids"])
    if actual_ids != index_ids or len(records) != names["record_counts"]["total"]:
        raise ValueError("governed name index differs from complete companion population")
    if set(mapped) - actual_ids:
        raise ValueError("capability directory points to nonexistent governed records")
    g_shards = []
    g_repositories, g_trees, g_repo_pin_trees = set(), set(), set()
    for path in sorted(blobs):
        if re.fullmatch(r"registry/discovery/gitskills-g[123]-package-identities-20261103-part-\d+\.json", path):
            data = load_json(path)
            g_shards.append({"path": path, "records_pointer": "/records", "record_count": len(data["records"]), "kind": "discovery-package-observations"})
            for observation in data["records"]:
                g_repositories.add(observation["repository"])
                g_trees.add(observation["package_tree"])
                g_repo_pin_trees.add((observation["repository"], observation["pinned_revision"], observation["package_tree"]))
    frontier = load_json("registry/discovery/dynamic-four-source-frontier-20261101.json")
    four_sources = []
    for source in frontier["sources"]:
        parent = load_json(source["manifest"])
        paths = parent.get("parts") or [source["manifest"]]
        manifests = [{"path": path, "records_pointer": "/entries", "record_count": len(load_json(path)["entries"])} for path in paths]
        count = sum(m["record_count"] for m in manifests)
        if count != source["raw"]:
            raise ValueError(f"discovery manifest count mismatch: {source['source_id']}")
        four_sources.append({"source_id": source["source_id"], "repository": parent["upstream_repository"], "pin": source["pin"], "manifest": source["manifest"], "record_count": count, "parts": manifests})
    discovery = {
        "schema_version": "skill-mason-discovery-manifests-v1",
        "g1_g3_shards": g_shards,
        "four_source_frontier": four_sources,
        "all_discovery_artifacts": [p for p in sorted(blobs) if p.startswith("registry/discovery/")],
        "all_evidence_artifacts": [p for p in sorted(blobs) if p.startswith("registry/")],
        "repository_entrypoints": {"first_party": [p for p in sorted(blobs) if p.startswith("skills/") and p.endswith("/SKILL.md")], "engine_maintenance_only": [p for p in sorted(blobs) if p.startswith("engine/skills/") and p.endswith("/SKILL.md")], "role_rule": "Engine instructions are represented separately, not added to governed user-facing skill counts. Upstream source entrypoints remain behind exact submodule pins where not materialized."},
        "counting_rule": "Observation populations overlap; do not sum as unique skills. Other ledger records remain losslessly accessible through pinned artifacts, not silently converted to governed reviews.",
    }
    governed = "".join(canonical(r) for r in records).encode()
    discovery_bytes = canonical(discovery).encode()
    artifact_bytes = {"governed.ndjson": governed, "discovery-manifests.json": discovery_bytes}
    manifest = {
        "schema_version": "skill-mason-catalog-manifest-v1",
        "producer": {"path": "scripts/build-skill-mason-catalog.py", "sha256": digest(Path(__file__).read_bytes()), "implementation": "skill-mason-passive-export-v1"},
        "source": {"repository": "https://github.com/Knapp-Kevin/skillz", "commit": commit, "git_tree_sha1": tree},
        "inventory_populations": {"g1_g3": {"path_observations": sum(x["record_count"] for x in g_shards), "repositories": len(g_repositories), "distinct_package_tree_hashes": len(g_trees), "within_repository_pin_tree_observations": len(g_repo_pin_trees), "not_claimed": "Unique semantic methods, completed reviews, source eligibility and universal coverage"}, "governed": {"paired_review_records": len(records), "meaning": "Bounded paired-companion review subset; not the corpus size or all candidate-evaluation decisions"}, "four_source": {"path_observations": sum(x["record_count"] for x in four_sources), "overlap": "Not reconciled against G1-G3 or governed records"}, "aggregation_rule": "Never add overlapping populations or divide governed count by discovery observations as a review-completion percentage."},
        "trust": "Pin commit/tree and this manifest digest through an independently trusted channel. Hashes establish byte integrity, not author identity or skill eligibility.",
        "serialization": "UTF-8, JSON sorted keys, compact separators, literal Unicode, LF after each object; NDJSON one object per line",
        "package_digest_definition": "sha256-of-canonical-file-list-v1: SHA-256 of canonical JSON plus LF containing the path-sorted array of package-relative POSIX path and file-content SHA-256 objects; no raw concatenation or Git-SHA-to-SHA256 conversion",
        "artifacts": [{"path": p, "sha256": digest(raw), "bytes": len(raw)} for p, raw in sorted(artifact_bytes.items())],
        "counts": {"governed_records": len(records), "first_party": sum(r["source_class"] == "first-party" for r in records), "third_party": sum(r["source_class"] == "third-party" for r in records), "mapped": sum(r["capability_mapping"]["state"] == "evidence-linked" for r in records), "unmapped": sum(r["capability_mapping"]["state"] == "unmapped" for r in records), "semantic_states": dict(sorted(collections.Counter(r["review"]["semantic_status"] for r in records).items())), "g1_g3_observations": sum(x["record_count"] for x in g_shards), "four_source_paths": sum(x["record_count"] for x in four_sources), "discovery_artifacts": len(discovery["all_discovery_artifacts"]), "source_files": len(inventory), "submodule_pins": len(gitlinks)},
        "taxonomy": {"recognized": "registry/capability-directory.json", "outcomes": "registry/capability-outcome-register.json", "prior_proposals": "registry/discovery/capability-domain-expansion-20261102.json", "new_proposals": "registry/capability-scope-extensions-20261117.json"},
        "source_files": inventory,
        "source_files_scope": "All tracked regular-file source inputs, excluding registry/exports/ generated handoffs; submodule commits recorded separately. No untracked input is read.",
        "submodule_pins": gitlinks,
        "readiness": {"inventory_and_ingestion": "complete-for-declared-snapshot", "universal_capability_coverage": "not-established", "composition_eligibility": "requires-independent-target-specific-assessment", "prism_integration": "not-implemented-by-this-export"},
    }
    artifact_bytes["manifest.json"] = canonical(manifest).encode()
    return artifact_bytes, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=Path.cwd())
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--source-tree", required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs, manifest = build(args.source_root.resolve(), args.source_commit, args.source_tree)
    destination = args.source_root.resolve() / "registry/exports/skill-mason-v1"
    for relative, raw in outputs.items():
        target = safe_path(destination, relative)
        if args.check:
            if not target.exists() or target.read_bytes() != raw:
                raise SystemExit(f"export drift: {relative}")
        else:
            destination.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
    print(json.dumps(manifest["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
