#!/usr/bin/env python3
"""Public synthetic fixture checker. Exit 1 for duplicates, 0 for valid input.

This is a fixture to produce actual observed local test outcomes. The
host/agent and user decide which outcomes should be recorded.
"""
import json
from pathlib import Path
import sys


def check(path):
    document = json.loads(Path(path).read_text(encoding="utf-8"))
    assert document.get("skill_id") == "demo-skill", "Unexpected skill identity"
    prefs = document["preferences"]
    keys = [p["key"] for p in prefs]
    assert len(set(keys)) == len(keys), "Duplicate preference key detected"
    return {"result": "PASS", "checks": ["identity", "unique-preference-keys"]}


if __name__ == "__main__":
    try:
        print(json.dumps(check(sys.argv[1]), sort_keys=True))
        raise SystemExit(0)
    except (AssertionError, KeyError, ValueError) as exc:
        print(json.dumps({"result": "FAIL", "reason": str(exc)}, sort_keys=True))
        raise SystemExit(1)
