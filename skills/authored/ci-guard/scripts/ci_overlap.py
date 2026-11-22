#!/usr/bin/env python3
"""Audit an analyst-expanded, repository-neutral CI execution graph.

This is a deterministic overlap *candidate* finder, not a YAML interpreter,
semantic-equivalence oracle, trusted receipt verifier, or GitHub cost source.
"""
import argparse
import itertools
import json
import sys
from pathlib import Path

DISPOSITIONS = {"CONSOLIDATE", "KEEP", "RELOCATE", "VERIFY"}


def required(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}: nonempty string required")
    return value


def audit(graph):
    """Return terminal-command overlaps between comparable entrypoints.

    Input schema:
      nodes: {node_id: {calls: [node_id]} OR
                       {command: str, obligation: str, inputs: str}}
      entrypoints: [{id, cohort, environment, trust_boundary,
                     invokes: [node_id], independence?: {reason, evidence}}]
      decisions: {"alpha|beta": {disposition, evidence}}
    Caller must establish that a cohort represents the same candidate
    revision and event purpose. Different runs may be incomparable.
    """
    nodes = graph.get("nodes")
    entries = graph.get("entrypoints")
    if not isinstance(nodes, dict) or not isinstance(entries, list):
        raise ValueError("nodes must be an object and entrypoints an array")
    if not isinstance(graph.get("decisions", {}), dict):
        raise ValueError("decisions must be an object")
    seen = set()

    def expand(name, trail=()):
        required(name, "node ID")
        if name not in nodes:
            raise ValueError(f"unresolved invocation: {name}")
        if name in trail:
            raise ValueError(f"invocation cycle: {' -> '.join((*trail, name))}")
        node = nodes[name]
        if not isinstance(node, dict):
            raise ValueError(f"invalid node: {name}")
        if "calls" in node:
            if ("command" in node or not isinstance(node["calls"], list)
                    or not node["calls"]):
                raise ValueError(f"invalid nonterminal: {name}")
            return [leaf for child in node["calls"]
                    for leaf in expand(child, (*trail, name))]
        return [tuple(required(node.get(field), f"{name}.{field}")
                      for field in ("command", "obligation", "inputs"))]

    expanded = []
    for e in entries:
        if not isinstance(e, dict):
            raise ValueError("invalid entrypoint")
        for field in ("id", "cohort", "environment", "trust_boundary"):
            required(e.get(field), f"entrypoint.{field}")
        if e["id"] in seen:
            raise ValueError(f"duplicate entrypoint ID: {e['id']}")
        seen.add(e["id"])
        if not isinstance(e.get("invokes"), list) or not e["invokes"]:
            raise ValueError(f"entrypoint {e['id']}: invokes must be nonempty")
        leaves = set(leaf for root in e["invokes"] for leaf in expand(root))
        ind = e.get("independence") or {}
        if not isinstance(ind, dict):
            raise ValueError(f"entrypoint {e['id']}: independence must be object")
        expanded.append((e, leaves, ind))

    findings = []
    for (a, aa, a_ind), (b, bb, b_ind) in itertools.combinations(expanded, 2):
        if a["cohort"] != b["cohort"]:
            continue
        ac = {(cmd, obligation) for cmd, obligation, _ in aa}
        bc = {(cmd, obligation) for cmd, obligation, _ in bb}
        common = ac & bc
        if not common:
            continue
        same_boundary = (a["environment"] == b["environment"]
                         and a["trust_boundary"] == b["trust_boundary"]
                         and "UNKNOWN" not in (a["environment"],
                                               b["environment"],
                                               a["trust_boundary"],
                                               b["trust_boundary"]))
        common_a = {x for x in aa if x[:2] in common}
        common_b = {x for x in bb if x[:2] in common}
        same_inputs = (common_a == common_b
                       and all(x[2] != "UNKNOWN" for x in common_a))
        independence_claim = any(
            isinstance(ind.get("reason"), str) and ind["reason"].strip()
            and isinstance(ind.get("evidence"), str) and ind["evidence"].strip()
            for ind in (a_ind, b_ind)
        )
        if independence_claim:
            classification = "JUSTIFIED_REPETITION_CLAIM"
        elif not (same_boundary and same_inputs):
            classification = "UNPROVEN"
        elif aa == bb:
            classification = "EXACT_DUPLICATE_CANDIDATE"
        else:
            classification = "PARTIAL_OVERLAP"
        pair = "|".join(sorted((a["id"], b["id"])))
        decision = graph.get("decisions", {}).get(pair, {})
        if not isinstance(decision, dict):
            raise ValueError(f"{pair}: decision must be object")
        disposition = decision.get("disposition")
        evidence = decision.get("evidence")
        resolved = (disposition in DISPOSITIONS
                    and isinstance(evidence, str) and bool(evidence.strip()))
        # An unsupported equivalence cannot authorize deleting a control.
        if classification == "UNPROVEN" and disposition == "CONSOLIDATE":
            resolved = False
        findings.append({
            "pair": pair,
            "cohort": a["cohort"],
            "classification": classification,
            "terminal_commands": sorted(cmd for cmd, _ in common),
            "disposition": disposition if resolved else "UNDISPOSED",
            "evidence": evidence if resolved else None,
            "resolved": resolved,
        })
    return {
        "status": "ANALYST_GRAPH_ONLY_NOT_HOST_VERIFIED",
        "entrypoints": len(entries),
        "findings": findings,
        "unresolved": sum(not finding["resolved"] for finding in findings),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph", type=Path, help="trusted analyst-expanded graph JSON")
    parser.add_argument("--enforce", action="store_true",
                        help="exit 2 if evidenced dispositions are missing")
    args = parser.parse_args(argv)
    try:
        result = audit(json.loads(args.graph.read_text(encoding="utf-8")))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f"INVALID_GRAPH: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 2 if args.enforce and result["unresolved"] else 0


if __name__ == "__main__":
    sys.exit(main())
