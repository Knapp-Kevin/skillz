#!/usr/bin/env python3
"""Compare sanitized MCP tool inventory observations without contacting any server.

The three stages are caller-provided assertions, NOT independently authenticated
network/host receipts. This is a bounded, read-only evidence reconciler.
Python 3.9+ standard library only.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 1_048_576
MAX_TOOLS = 256
MAX_PAGES = 64
SKEW_SECONDS = 300
STAGES = ("backend_registry", "mcp_list", "host_visible")
NAME = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9_.:/-]{0,127}$")
PROTOCOLS = {"2025-06-18", "2025-11-25", "2026-07-28"}


class EvidenceHold(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise EvidenceHold(message)


def fields(obj, required, optional=(), label="object"):
    require(isinstance(obj, dict), label + ": dictionary required")
    require(set(required).issubset(obj), label + ": missing required fields")
    require(not (set(obj) - set(required) - set(optional)),
            label + ": unexpected fields")


def identifier(value, label, limit=128):
    require(isinstance(value, str) and 0 < len(value) <= limit and
            NAME.fullmatch(value) is not None, label + ": invalid identifier")
    return value


def timestamp(value):
    require(isinstance(value, str) and len(value) <= 40, "invalid capture timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as err:
        raise EvidenceHold("invalid capture timestamp") from err
    require(parsed.tzinfo is not None and parsed.utcoffset() is not None,
            "capture timestamp missing timezone")
    return parsed.astimezone(timezone.utc)


def no_duplicates(pairs):
    result = {}
    for k, v in pairs:
        require(k not in result, "duplicate JSON key")
        result[k] = v
    return result


def load(path):
    path = Path(path).absolute()
    require(path.is_file() and not any(p.is_symlink() for p in (path, *path.parents)),
            "missing or symlinked input")
    require(path.stat().st_size <= MAX_BYTES, "input exceeds one MiB")
    with path.open("rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
        require(len(raw) <= MAX_BYTES, "input exceeds one MiB")
        return json.loads(raw.decode("utf-8"), object_pairs_hook=no_duplicates,
                         parse_constant=lambda _: (_ for _ in ()).throw(
                             EvidenceHold("nonfinite JSON value")))


def tool_map(tools):
    require(isinstance(tools, list) and len(tools) <= MAX_TOOLS,
            "unbounded or invalid tool list")
    result = {}
    for tool in tools:
        fields(tool, ("name", "inputSchema"), ("outputSchema",), "tool")
        name = identifier(tool["name"], "tool name")
        require(name not in result, "duplicate tool name")
        require(isinstance(tool["inputSchema"], dict),
                "inputSchema must be a JSON object")
        output = tool.get("outputSchema")
        require(output is None or isinstance(output, dict),
                "outputSchema must be JSON object or absent")
        payload = {"inputSchema": tool["inputSchema"],
                   "outputSchema": output}
        try:
            canonical = json.dumps(payload, sort_keys=True,
                                   separators=(",", ":"), ensure_ascii=True,
                                   allow_nan=False)
        except (TypeError, ValueError) as err:
            raise EvidenceHold("invalid JSON schema") from err
        result[name] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return result


def stage_common(stage, evidence, revision, context):
    fields(evidence, ("source_revision", "context_tag", "captured_at", "complete"),
           ("tools", "pages"), stage)
    identifier(evidence["source_revision"], "revision", 128)
    identifier(evidence["context_tag"], "context", 128)
    require(type(evidence["complete"]) is bool, "nonboolean completeness: " + stage)
    return (evidence["source_revision"] == revision,
            evidence["context_tag"] == context,
            timestamp(evidence["captured_at"]))


def mcp_pages(pages, modern):
    require(isinstance(pages, list) and 1 <= len(pages) <= MAX_PAGES,
            "MCP pages must be bounded and nonempty")
    seen_cursors = set()
    all_tools = []
    cursor = None
    scopes = []
    incomplete = False
    for i, page in enumerate(pages):
        fields(page, ("request_cursor", "next_cursor", "tools"),
               ("ttlMs", "cacheScope"), "MCP page")
        require(page["request_cursor"] == cursor,
                "MCP pagination cursor chain mismatch at page " + str(i + 1))
        token = page["next_cursor"]
        require(token is None or
                (isinstance(token, str) and 0 < len(token) <= 256),
                "invalid MCP next cursor")
        if modern:
            require("ttlMs" in page and "cacheScope" in page,
                    "MCP 2026-07-28 cache hints missing")
        if "ttlMs" in page:
            ttl = page["ttlMs"]
            require(type(ttl) is int and 0 <= ttl <= 604800000,
                    "invalid ttlMs")
        if "cacheScope" in page:
            require(page["cacheScope"] in ("public", "private"),
                    "invalid cacheScope")
            scopes.append(page["cacheScope"])
        # Per-page collision and malformed-schema checks happen before any
        # stage is considered complete.
        tool_map(page["tools"])
        all_tools.extend(page["tools"])
        require(len(all_tools) <= MAX_TOOLS,
                "total MCP tools exceed bound")
        if token is not None:
            require(token not in seen_cursors, "MCP pagination cursor cycle")
            seen_cursors.add(token)
        cursor = token
        if i < len(pages) - 1:
            require(cursor is not None, "extra page after terminal MCP page")
    if cursor is not None:
        incomplete = True
    require(len(set(scopes)) <= 1, "MCP page cacheScope drift")
    return tool_map(all_tools), incomplete, (
        scopes[0] if scopes else None)


def diff(left, right, boundary):
    result = []
    for name in sorted(set(left) - set(right)):
        result.append({"boundary": boundary, "finding": "NOT_VISIBLE_DOWNSTREAM",
                       "name": name})
    for name in sorted(set(right) - set(left)):
        result.append({"boundary": boundary, "finding": "ONLY_VISIBLE_DOWNSTREAM",
                       "name": name})
    for name in sorted(set(left) & set(right)):
        if left[name] != right[name]:
            result.append({"boundary": boundary, "finding": "SCHEMA_FINGERPRINT_DIFF",
                           "name": name, "upstream_sha256": left[name],
                           "downstream_sha256": right[name]})
    return result


def audit(data):
    fields(data, ("schema_version", "protocol_revision", "source_revision",
                  "context_tag", "stages"), label="bundle")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1,
            "unsupported bundle schema")
    protocol = data["protocol_revision"]
    require(protocol in PROTOCOLS, "unsupported protocol revision")
    revision = identifier(data["source_revision"], "revision", 128)
    context = identifier(data["context_tag"], "context", 128)
    observed = data["stages"]
    require(isinstance(observed, dict) and
            not (set(observed) - set(STAGES)), "unknown observation stage")
    maps = {}
    complete = {}
    times = []
    reasons = []
    advisories = []
    for stage in STAGES:
        evidence = observed.get(stage)
        if evidence is None:
            complete[stage] = False
            reasons.append("STAGE_NOT_OBSERVED:" + stage)
            continue
        fields(evidence, ("source_revision", "context_tag", "captured_at",
                          "complete", "pages" if stage == "mcp_list" else "tools"),
               label=stage)
        revision_match, context_match, when = stage_common(
            stage, evidence, revision, context)
        times.append(when)
        if not revision_match:
            reasons.append("SOURCE_REVISION_DIFFERENCE:" + stage)
        if not context_match:
            reasons.append("AUTH_CONTEXT_DIFFERENCE:" + stage)
        if stage == "mcp_list":
            mapping, unfinished, cache_scope = mcp_pages(
                evidence["pages"], protocol == "2026-07-28")
            if unfinished:
                reasons.append("INCOMPLETE_MCP_PAGINATION")
            if cache_scope == "public":
                advisories.append("REVIEW_PUBLIC_CACHE_SCOPE_FOR_AUTH_DEPENDENCE")
            complete[stage] = evidence["complete"] and not unfinished
        else:
            mapping = tool_map(evidence["tools"])
            complete[stage] = evidence["complete"]
        if not evidence["complete"]:
            reasons.append("STAGE_DECLARED_INCOMPLETE:" + stage)
        maps[stage] = mapping
    if times and (max(times) - min(times)).total_seconds() > SKEW_SECONDS:
        reasons.append("CAPTURE_WINDOW_TOO_WIDE")
    # Never infer cause or absent tools from an incomplete, different revision
    # or different authorization context. The mismatch could be the capture.
    comparable = not reasons
    differences = []
    if comparable:
        differences.extend(diff(maps["backend_registry"], maps["mcp_list"],
                                "backend_registry_to_mcp_list"))
        differences.extend(diff(maps["mcp_list"], maps["host_visible"],
                                "mcp_list_to_host_visible"))
    status = ("INCONCLUSIVE" if not comparable else
              "OBSERVED_DIFFERENCE" if differences else "OBSERVED_PARITY")
    return {
        "schema_version": 1, "status": status,
        "protocol_revision_claim": protocol,
        "source_revision_claim": revision,
        "counts": {stage: (len(maps[stage]) if stage in maps else None)
                   for stage in STAGES},
        "inconclusive_reasons": sorted(set(reasons)),
        "observed_differences": differences,
        "advisories": sorted(set(advisories)),
        "backend_revision_authenticated": False,
        "mcp_transport_observed": False,
        "host_behavior_independently_observed": False,
        "host_or_server_fault_assigned": False,
        "tool_invocations_tested": False,
        "scope": "CALLER_SUPPLIED_NORMALIZED_CAPTURES_ONLY",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--require-parity", action="store_true",
                        help="Exit 3 unless all provided stages establish parity")
    args = parser.parse_args()
    try:
        result = audit(load(args.input))
        print(json.dumps(result, indent=2, sort_keys=True))
        return 3 if args.require_parity and result["status"] != "OBSERVED_PARITY" else 0
    except EvidenceHold as exc:
        print("CAPTURE_HOLD: " + str(exc), file=sys.stderr)
        return 2
    except (TypeError, KeyError, ValueError, OSError, UnicodeError, RecursionError):
        print("CAPTURE_HOLD: malformed or unreadable input", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
