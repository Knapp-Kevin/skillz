#!/usr/bin/env python3
"""Offline evidence-lineage consistency audit. Never treats citations as truth."""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys

MAX_SIZE = 1024 * 1024
MAX_SOURCES = 200
MAX_CLAIMS = 50
MAX_REFS = 100
ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.:-]{0,95}$")
DAY = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class InvalidInput(ValueError):
    pass


def check(ok: bool, detail: str) -> None:
    if not ok:
        raise InvalidInput(detail)


def fields(row: object, keys: set[str], where: str, required: set[str] | None = None) -> dict:
    check(isinstance(row, dict), f"{where}: object required")
    check(not (row.keys() - keys), f"{where}: unknown fields")
    if required is not None:
        check(required <= row.keys(), f"{where}: required fields missing")
    return row


def ident(value: object, where: str) -> str:
    check(isinstance(value, str) and bool(ID.fullmatch(value)), f"{where}: invalid identifier")
    return value


def day(value: object, where: str, nullable: bool = False) -> date | None:
    if nullable and value is None:
        return None
    check(isinstance(value, str) and bool(DAY.fullmatch(value)), f"{where}: ISO date required")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise InvalidInput(f"{where}: invalid calendar date") from exc


def string(value: object, where: str, maximum: int = 240) -> str:
    check(isinstance(value, str) and 0 < len(value.strip()) and len(value) <= maximum, f"{where}: bounded nonempty string required")
    return value


def ids(value: object, where: str, maximum: int = MAX_SOURCES) -> list[str]:
    check(isinstance(value, list) and len(value) <= maximum, f"{where}: bounded list required")
    result = [ident(x, where) for x in value]
    check(len(result) == len(set(result)), f"{where}: duplicate identifiers")
    return result


def pairs(items: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in items:
        check(key not in result, "duplicate JSON field")
        result[key] = value
    return result


def nonfinite(value: str) -> object:
    raise InvalidInput("nonfinite JSON value")


def validate(doc: object) -> tuple[dict, dict, date]:
    root = fields(doc, {"schema_version", "reviewed_on", "sources", "claims"}, "input", {"schema_version", "reviewed_on", "sources", "claims"})
    check(type(root["schema_version"]) is int and root["schema_version"] == 1, "schema_version: expected 1")
    reviewed = day(root["reviewed_on"], "reviewed_on")
    source_rows = root["sources"]
    claim_rows = root["claims"]
    check(isinstance(source_rows, list) and 1 <= len(source_rows) <= MAX_SOURCES, "sources: expected 1..200 entries")
    check(isinstance(claim_rows, list) and 1 <= len(claim_rows) <= MAX_CLAIMS, "claims: expected 1..50 entries")
    sources = {}
    source_fields = {"id", "source_kind", "consultation", "access", "source_ref", "publication_date", "event_start", "event_end", "scope_id", "origin_id", "derived_from", "lineage_complete"}
    for i, raw in enumerate(source_rows):
        src = fields(raw, source_fields, f"sources[{i}]", source_fields)
        sid = ident(src["id"], "source id")
        check(sid not in sources, "duplicate source id")
        check(src["source_kind"] in ("PRIMARY", "SECONDARY"), "source_kind: invalid")
        check(src["consultation"] in ("DIRECT", "CITED_NOT_READ"), "consultation: invalid")
        check(src["access"] in ("AUTHORIZED", "INACCESSIBLE", "UNKNOWN"), "access: invalid")
        ident(src["source_ref"], "source_ref (opaque handle, not URL)")
        ident(src["scope_id"], "source scope_id")
        publication = day(src["publication_date"], "publication_date", nullable=True)
        start = day(src["event_start"], "event_start", nullable=True)
        end = day(src["event_end"], "event_end", nullable=True)
        check(start is None or end is None or start <= end, "source event range inverted")
        parents = ids(src["derived_from"], "derived_from")
        check(sid not in parents, "self-derived source")
        check(type(src["lineage_complete"]) is bool, "lineage_complete: explicit boolean required")
        if parents:
            check(src["origin_id"] is None, "derived source cannot claim a new independent root")
        else:
            ident(src["origin_id"], "root origin_id")
        sources[sid] = {**src, "publication_date_parsed": publication, "start_parsed": start, "end_parsed": end, "parents": parents}
    for sid, src in sources.items():
        check(all(p in sources for p in src["parents"]), f"source {sid}: missing upstream source")
    # Reject any lineage cycle instead of manufacturing a root.
    traversing, completed = set(), set()
    def visit(sid: str) -> None:
        if sid in completed:
            return
        check(sid not in traversing, "source lineage cycle")
        traversing.add(sid)
        for pid in sources[sid]["parents"]:
            visit(pid)
        traversing.remove(sid)
        completed.add(sid)
    for sid in sources:
        visit(sid)
    claims = {}
    claim_fields = {"id", "proposition", "scope_id", "period_start", "period_end", "load_bearing", "evidence"}
    for i, raw in enumerate(claim_rows):
        cl = fields(raw, claim_fields, f"claims[{i}]", claim_fields)
        cid = ident(cl["id"], "claim id")
        check(cid not in claims, "duplicate claim id")
        string(cl["proposition"], "proposition", 600)
        ident(cl["scope_id"], "claim scope_id")
        start = day(cl["period_start"], "claim period_start")
        end = day(cl["period_end"], "claim period_end")
        check(start <= end, "claim interval inverted")
        check(type(cl["load_bearing"]) is bool, "load_bearing: explicit boolean required")
        ev = cl["evidence"]
        check(isinstance(ev, list) and len(ev) <= MAX_REFS, "claim evidence: bounded list required")
        seen = set()
        for j, observation in enumerate(ev):
            fields(observation, {"source_id", "stance", "locator_ref"}, f"claim {cid} evidence {j}", {"source_id", "stance", "locator_ref"})
            sid = ident(observation["source_id"], "evidence source_id")
            check(sid in sources, "evidence points to unknown source")
            check(observation["stance"] in ("SUPPORT", "REFUTE", "CONTEXT"), "evidence stance invalid")
            ident(observation["locator_ref"], "evidence locator_ref (opaque handle)")
            key = (sid, observation["stance"], observation["locator_ref"])
            check(key not in seen, "duplicate evidence record")
            seen.add(key)
        claims[cid] = {**cl, "start_parsed": start, "end_parsed": end}
    return sources, claims, reviewed


def audit(doc: object) -> dict:
    sources, claims, reviewed = validate(doc)
    root_cache = {}
    def roots(sid: str) -> tuple[set[str], bool]:
        if sid in root_cache:
            return root_cache[sid]
        src = sources[sid]
        if not src["parents"]:
            result = ({src["origin_id"]}, src["lineage_complete"])
        else:
            upstream = [roots(pid) for pid in src["parents"]]
            result = (set().union(*(r for r, _ in upstream)), src["lineage_complete"] and all(ok for _, ok in upstream))
        root_cache[sid] = result
        return result

    findings = []
    for cid, cl in claims.items():
        use, gaps, by_direction = [], [], {"SUPPORT": [], "REFUTE": [], "CONTEXT": []}
        for obs in cl["evidence"]:
            src = sources[obs["source_id"]]
            reasons = []
            if src["access"] != "AUTHORIZED":
                reasons.append("ACCESS_NOT_CONFIRMED")
            if src["consultation"] != "DIRECT":
                reasons.append("SOURCE_NOT_DIRECTLY_CONSULTED")
            if src["publication_date_parsed"] is None:
                reasons.append("PUBLICATION_DATE_UNKNOWN")
            elif src["publication_date_parsed"] > reviewed:
                reasons.append("PUBLISHED_AFTER_REVIEW")
            if src["scope_id"] != cl["scope_id"]:
                reasons.append("POPULATION_OR_SCOPE_MISMATCH")
            if (src["start_parsed"] is None or src["end_parsed"] is None):
                reasons.append("EVENT_PERIOD_UNKNOWN")
            elif src["start_parsed"] > cl["start_parsed"] or src["end_parsed"] < cl["end_parsed"]:
                reasons.append("EVENT_PERIOD_NOT_FULLY_COVERED")
            lineage, known = roots(src["id"])
            if not known:
                reasons.append("LINEAGE_INCOMPLETE")
            result = {
                "source_id": src["id"], "stance": obs["stance"],
                "locator_ref": obs["locator_ref"],
                "recorded_origin_ids": sorted(lineage) if known else [],
                "eligible": not bool(reasons), "exclusions": reasons,
                "direct_primary_root": not reasons and not src["parents"] and src["source_kind"] == "PRIMARY",
            }
            use.append(result)
            if reasons:
                gaps.append({"source_id": src["id"], "reasons": reasons})
            else:
                by_direction[obs["stance"]].append(result)
        summaries = {}
        for stance in ("SUPPORT", "REFUTE"):
            valid = by_direction[stance]
            roots_reported = set().union(*(set(x["recorded_origin_ids"]) for x in valid)) if valid else set()
            direct_origins = set().union(*(set(x["recorded_origin_ids"]) for x in valid if x["direct_primary_root"])) if valid else set()
            summaries[stance] = {
                "eligible_citation_count": len(valid),
                "recorded_origin_ids": sorted(roots_reported),
                "reported_origin_count": len(roots_reported),
                "direct_primary_origin_ids": sorted(direct_origins),
                "direct_primary_origin_count": len(direct_origins),
                "direct_source_ids": sorted({x["source_id"] for x in valid}),
            }
        support = summaries["SUPPORT"]
        refute = summaries["REFUTE"]
        if support["eligible_citation_count"] and refute["eligible_citation_count"]:
            overlap = set(support["recorded_origin_ids"]) & set(refute["recorded_origin_ids"])
            if overlap:
                pattern = "CONFLICT_WITH_SHARED_RECORDED_ORIGIN"
            elif support["direct_primary_origin_count"] and refute["direct_primary_origin_count"]:
                pattern = "CONFLICT_BETWEEN_DISTINCT_RECORDED_PRIMARY_ROOTS"
            else:
                pattern = "CONFLICT_WITH_INDEPENDENCE_UNVERIFIED"
        elif support["direct_primary_origin_count"] >= 2:
            pattern = "MULTIPLE_RECORDED_DIRECT_PRIMARY_SUPPORT_ROOTS"
        elif refute["direct_primary_origin_count"] >= 2:
            pattern = "MULTIPLE_RECORDED_DIRECT_PRIMARY_REFUTE_ROOTS"
        elif support["direct_primary_origin_count"] or refute["direct_primary_origin_count"]:
            pattern = "SINGLE_RECORDED_DIRECT_PRIMARY_ROOT"
        elif support["eligible_citation_count"] or refute["eligible_citation_count"]:
            pattern = "SECONDARY_OR_DERIVATIVE_ONLY"
        else:
            pattern = "NO_ELIGIBLE_DIRECTIONAL_EVIDENCE"
        findings.append({
            "claim_id": cid, "load_bearing": cl["load_bearing"],
            "pattern": pattern, "status": "HUMAN_OR_HOST_ADJUDICATION_REQUIRED",
            "counts": summaries, "source_checks": use, "evidence_gaps": gaps,
            "independence_not_authenticated": True,
        })
    return {
        "schema_version": 1,
        "reviewed_on": doc["reviewed_on"],
        "claims": findings,
        "global_verdict": "NOT_DETERMINED_BY_LINEAGE_AUDIT",
        "source_authenticity_verified": False,
        "warning": "Source identity, lineage, independence, dates and scope are caller assertions. Counts are not votes or truth; independent host authentication and substantive causal/denominator review remain required.",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.input.stat().st_size > MAX_SIZE:
            raise InvalidInput("input exceeds 1MiB")
        with args.input.open("r", encoding="utf-8") as file:
            doc = json.load(file, object_pairs_hook=pairs, parse_constant=nonfinite)
        result = audit(doc)
    except InvalidInput as err:
        print("INVALID_INPUT: " + str(err), file=sys.stderr)
        return 2
    except (OSError, UnicodeError, ValueError):
        print("INVALID_INPUT: unable to read or parse supplied file", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
