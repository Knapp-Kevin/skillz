#!/usr/bin/env python3
"""Offline reference-graph integrity checks over explicitly supplied evidence.

Never resolves URLs, follows paths, authenticates receipt claims, or mutates input.
"""
from __future__ import annotations

import argparse
from collections import deque
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 1024 * 1024
MAX_NODES = 300
MAX_EDGES = 1000
MAX_CHANGES = 30
ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,95}$")
REV = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:/@-]{0,159}$")
KINDS = {"RELATIVE_MARKDOWN", "GITHUB_BRANCH", "GITHUB_COMMIT", "HEADING_ANCHOR", "CITATION", "DRIVE_SHORTCUT", "METADATA_EDGE"}
LOOKUPS = {"FOUND", "ABSENT", "DENIED", "NOT_RUN", "UNKNOWN", "REDIRECT", "HTTP_404"}
ANCHORS = {"VALID", "MISSING", "NOT_CHECKED", "NOT_APPLICABLE"}


class InvalidInput(ValueError):
    pass


def require(condition, error):
    if not condition:
        raise InvalidInput(error)


def fields(value, allowed, name):
    require(isinstance(value, dict), f"{name}: expected object")
    require(not set(value).difference(allowed), f"{name}: unknown fields")


def ident(value, name, pattern=ID):
    require(isinstance(value, str) and bool(pattern.fullmatch(value)), f"{name}: invalid identifier")
    return value


def boolean(value, name):
    require(type(value) is bool, f"{name}: expected boolean")
    return value


def pairs_no_duplicates(pairs):
    output = {}
    for key, value in pairs:
        require(key not in output, "duplicate JSON field")
        output[key] = value
    return output


def parse(doc):
    fields(doc, {"schema_version", "scope_id", "snapshot_revision", "enumeration", "nodes", "edges", "changes"}, "root")
    require(type(doc.get("schema_version")) is int and doc["schema_version"] == 1, "schema_version: expected 1")
    ident(doc.get("scope_id"), "scope_id")
    ident(doc.get("snapshot_revision"), "snapshot_revision", REV)
    enum = doc.get("enumeration")
    fields(enum, {"sources_complete", "visibility_complete"}, "enumeration")
    for key in ("sources_complete", "visibility_complete"):
        boolean(enum.get(key), f"enumeration.{key}")
    entries = doc.get("nodes")
    require(isinstance(entries, list) and 1 <= len(entries) <= MAX_NODES, "nodes: 1..300 required")
    nodes = {}
    for i, node in enumerate(entries):
        fields(node, {"id", "visible", "revision"}, f"nodes[{i}]")
        nid = ident(node.get("id"), f"nodes[{i}].id")
        require(nid not in nodes, "duplicate node id")
        boolean(node.get("visible"), f"node {nid}.visible")
        ident(node.get("revision"), f"node {nid}.revision", REV)
        nodes[nid] = node
    edge_data = doc.get("edges")
    require(isinstance(edge_data, list) and len(edge_data) <= MAX_EDGES, "edges: max 1000")
    edges, seen_edges = [], set()
    for i, edge in enumerate(edge_data):
        fields(edge, {"id", "source", "target", "kind", "evidence_ref", "lookup"}, f"edges[{i}]")
        eid = ident(edge.get("id"), f"edges[{i}].id")
        require(eid not in seen_edges, "duplicate edge id")
        seen_edges.add(eid)
        source = ident(edge.get("source"), "edge.source")
        require(source in nodes, f"edge {eid}: unknown source")
        target = edge.get("target")
        if target is not None:
            ident(target, "edge.target")
        require(edge.get("kind") in KINDS, f"edge {eid}: unsupported kind")
        ident(edge.get("evidence_ref"), "edge.evidence_ref", REV)
        lookup = edge.get("lookup")
        fields(lookup, {"state", "authorized", "complete", "absence_proven", "source_current", "target_current", "anchor", "anchor_renderer_verified", "redirect_verified"}, f"edge {eid}.lookup")
        require(lookup.get("state") in LOOKUPS, f"edge {eid}: invalid lookup state")
        for field in ("authorized", "complete", "absence_proven", "redirect_verified", "anchor_renderer_verified"):
            boolean(lookup.get(field), f"edge {eid}.{field}")
        for field in ("source_current", "target_current"):
            require(lookup.get(field) is None or type(lookup[field]) is bool, f"edge {eid}.{field}: bool or null")
        require(lookup.get("anchor") in ANCHORS, f"edge {eid}: invalid anchor state")
        if lookup["state"] == "ABSENT":
            require(lookup["target_current"] is None, f"edge {eid}: absent target cannot have a current target revision")
        if lookup["state"] != "ABSENT":
            require(not lookup["absence_proven"], f"edge {eid}: absence proof only applies to ABSENT lookup")
        if lookup["state"] != "REDIRECT":
            require(not lookup["redirect_verified"], f"edge {eid}: redirect proof only applies to REDIRECT lookup")
        edges.append(edge)
    changes = doc.get("changes", [])
    require(isinstance(changes, list) and len(changes) <= MAX_CHANGES, "changes: max 30")
    seen_change = set()
    for i, change in enumerate(changes):
        fields(change, {"id", "node", "operation"}, f"changes[{i}]")
        cid = ident(change.get("id"), "change.id")
        require(cid not in seen_change, "duplicate change id")
        seen_change.add(cid)
        nid = ident(change.get("node"), "change.node")
        require(nid in nodes, "change.node: not in authorized snapshot")
        require(change.get("operation") in {"MOVE", "RENAME", "DELETE_PROPOSAL"}, "change.operation: unsupported")
    return nodes, edges, changes, enum


def edge_status(edge, nodes):
    """Conservative evidence classifier. Does not verify supplied attestation."""
    source = nodes[edge["source"]]
    target_id = edge["target"]
    target = nodes.get(target_id)
    if not source["visible"] or (target is not None and not target["visible"]):
        return "WITHHELD", "PRIVACY_LIMIT"
    lk = edge["lookup"]
    if not lk["authorized"]:
        return "BLOCKED", "LOOKUP_NOT_AUTHORIZED"
    if lk["state"] == "DENIED":
        return "INACCESSIBLE", "TARGET_NOT_DISCLOSED"
    if lk["source_current"] is False or lk["target_current"] is False:
        return "STALE_VERSION", "REVISION_DRIFT_REPORTED"
    if lk["source_current"] is None or (lk["target_current"] is None and lk["state"] != "ABSENT"):
        return "UNRESOLVED", "REVISION_BINDING_UNVERIFIED"
    if lk["state"] in {"NOT_RUN", "UNKNOWN", "HTTP_404"}:
        return "UNRESOLVED", "LOOKUP_NOT_PROVEN"
    if not lk["complete"]:
        return "UNRESOLVED", "LOOKUP_INCOMPLETE"
    if lk["state"] == "ABSENT":
        if lk["absence_proven"]:
            return "BROKEN_CONFIRMED", "AUTHORIZED_ABSENCE_AT_BOUND_REVISION_RECORDED"
        return "UNRESOLVED", "ABSENCE_NOT_PROVEN"
    if lk["state"] == "REDIRECT":
        if lk["redirect_verified"]:
            return "MOVED_OR_REDIRECT", "PROVIDER_MOVE_RECORDED"
        return "BLOCKED", "UNVERIFIED_REDIRECT"
    if lk["state"] == "FOUND":
        if target is None:
            return "UNRESOLVED", "TARGET_IDENTITY_NOT_IN_APPROVED_GRAPH"
        if lk["anchor"] == "MISSING":
            if not lk["anchor_renderer_verified"]:
                return "UNRESOLVED", "HEADING_RENDERER_NOT_VERIFIED"
            return "BROKEN_CONFIRMED", "CHECKED_ANCHOR_MISSING_AT_BOUND_REVISION"
        if lk["anchor"] == "VALID" and edge["kind"] == "HEADING_ANCHOR" and not lk["anchor_renderer_verified"]:
            return "UNRESOLVED", "HEADING_RENDERER_NOT_VERIFIED"
        if lk["anchor"] == "NOT_CHECKED" and edge["kind"] == "HEADING_ANCHOR":
            return "UNRESOLVED", "ANCHOR_NOT_VALIDATED"
        if lk["anchor"] == "NOT_APPLICABLE" and edge["kind"] == "HEADING_ANCHOR":
            return "UNRESOLVED", "ANCHOR_VALIDATION_NOT_ESTABLISHED"
        return "VERIFIED_CURRENT", "MATCHING_RESOLUTION_RECORDED"
    raise InvalidInput("unhandled status")


def audit(doc):
    nodes, edges, changes, enum = parse(doc)
    findings, reverse, possible_reverse, inbound = [], {}, {}, {k: 0 for k, v in nodes.items() if v["visible"]}
    privacy_limited = False
    for edge in edges:
        status, reason = edge_status(edge, nodes)
        if status == "WITHHELD":
            privacy_limited = True
            continue  # neither source, target, edge ID nor hidden-edge count disclosed
        row = {"edge_id": edge["id"], "source_id": edge["source"], "kind": edge["kind"], "status": status, "reason": reason}
        # Never expose an unapproved target ID in an audit report.
        target = nodes.get(edge["target"])
        if target is not None and target["visible"] and status not in {"INACCESSIBLE", "BLOCKED"}:
            row["target_id"] = edge["target"]
        findings.append(row)
        if target is not None and target["visible"]:
            if status in {"VERIFIED_CURRENT", "STALE_VERSION", "MOVED_OR_REDIRECT"}:
                reverse.setdefault(edge["target"], set()).add(edge["source"])
                inbound[edge["target"]] += 1
            elif status == "UNRESOLVED":
                possible_reverse.setdefault(edge["target"], set()).add(edge["source"])
    # A bounded graph yields only within-scope candidates, never deletion permission.
    full_local = enum["sources_complete"] and enum["visibility_complete"] and not privacy_limited and all(n["visible"] for n in nodes.values())
    orphans = sorted(k for k, value in inbound.items() if value == 0) if full_local else []
    impacts = []
    for change in changes:
        root = change["node"]
        if not nodes[root]["visible"]:
            privacy_limited = True
            continue
        distance, seen = {root: 0}, {root}
        queue = deque([root])
        while queue:
            node = queue.popleft()
            for parent in sorted(reverse.get(node, ())):
                if parent not in seen:
                    seen.add(parent)
                    distance[parent] = distance[node] + 1
                    queue.append(parent)
        possible = sorted(possible_reverse.get(root, set()) - seen)
        impacts.append({"change_id": change["id"], "operation": change["operation"], "direct_dependents": sorted(k for k, v in distance.items() if v == 1),
                        "unverified_direct_dependents": possible,
                        "transitive_dependents": sorted(k for k, v in distance.items() if v > 1),
                        "coverage": "BOUNDED_GRAPH_ONLY" if full_local else "PARTIAL_GRAPH_UNKNOWN_EXTERNAL_DEPENDENTS",
                        "status": "PROPOSED_ONLY_REVALIDATE_BEFORE_ANY_WRITE"})
    return {"schema_version": 1, "scope_id": doc["scope_id"], "snapshot_revision": doc["snapshot_revision"],
            "target_evidence_authenticated": False, "writes_performed": False,
            "findings": findings, "privacy_limited": privacy_limited,
            "orphan_candidates_within_approved_scope": orphans,
            "orphan_coverage": "BOUNDED_COMPLETE_WITHIN_SCOPE" if full_local else "UNDETERMINED_INCOMPLETE_ENUMERATION",
            "impacts": impacts,
            "limitations": ["Input visibility, revision, authorized lookup and absence receipts are host-supplied assertions, not authenticated by this tool.",
                            "No external discovery or repair; no globally safe orphan/deletion finding can be derived from this graph."]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        if any(path.is_symlink() for path in (args.input, *args.input.parents)):
            raise InvalidInput("symlinked input path or parent is not allowed")
        if args.input.stat().st_size > MAX_BYTES:
            raise InvalidInput("input exceeds 1 MiB")
        with args.input.open("r", encoding="utf-8") as file:
            doc = json.load(file, object_pairs_hook=pairs_no_duplicates,
                            parse_constant=lambda value: (_ for _ in ()).throw(InvalidInput("nonfinite JSON constant")))
        result = audit(doc)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"INVALID_INPUT: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
