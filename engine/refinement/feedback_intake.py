#!/usr/bin/env python3
"""Untrusted, source-blind feedback shape gate for maintainer review.

Accept only categorical, public-skill-referenced signals. Raw transcripts,
URLs, payloads, account identities, usernames, logs, and proposed agent
instructions do not belong in this schema. No network, writes, execution,
publication, or automatic skill modification.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
MAX_BYTES = 8192
FIELDS = {
    "schema_version", "skill_id", "layer", "failure_class", "scenario",
    "expected", "observed", "evidence_tier", "routing", "preference_class",
}
SLUG = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$", flags=re.ASCII)
LAYER = {"skill", "phase", "component", "pack", "engine"}
FAILURES = {
    "none", "incorrect-result", "false-success", "wrong-trigger",
    "missing-handoff", "missing-dependency", "authorization-boundary",
    "privacy-boundary", "unsafe-instruction-following", "source-rights",
    "unverified-claim", "portability", "regression",
}
SCENARIOS = {
    "positive", "near-non-trigger", "missing-input",
    "authority-boundary", "false-green", "pack-handoff",
    "regression", "other",
}
BEHAVIOR = {
    "correct", "incorrect", "not-triggered", "unintended-trigger",
    "halted", "continued-incorrectly", "insufficient-evidence", "unknown",
}
LEVELS = {"reported-claim", "static-review-claim", "local-test-claim",
          "host-observed-claim", "not-tested"}
ROUTES = {"canonical-candidate", "local-preference", "mixed", "hold",
          "no-action"}
PREFERENCES = {"none", "language", "presentation", "detail",
               "ordering", "optional-workflow-style"}


class FeedbackHold(ValueError):
    pass


def require(ok, code):
    if not ok:
        raise FeedbackHold(code)


def clean_code(value, choices, field):
    require(type(value) is str and value in choices,
            "INVALID_ENUM:" + field)


def known_target(skill):
    """Bound identities to existing first-party skill names only."""
    return any(
        (ROOT / parent / skill / "SKILL.md").is_file()
        for parent in (Path("skills/authored"), Path("engine/skills"))
    )


def validate(signal):
    require(type(signal) is dict and set(signal) == FIELDS,
            "UNEXPECTED_FIELD_OR_MISSING_FIELD")
    require(type(signal["schema_version"]) is int and
            signal["schema_version"] == 1, "UNSUPPORTED_SCHEMA")
    target = signal["skill_id"]
    require(type(target) is str and 1 <= len(target) <= 80 and
            bool(SLUG.fullmatch(target)) and known_target(target),
            "UNKNOWN_OR_UNSAFE_TARGET")
    for key, choices in (
        ("layer", LAYER),
        ("failure_class", FAILURES),
        ("scenario", SCENARIOS),
        ("expected", BEHAVIOR),
        ("observed", BEHAVIOR),
        ("evidence_tier", LEVELS),
        ("routing", ROUTES),
        ("preference_class", PREFERENCES),
    ):
        clean_code(signal[key], choices, key)

    route, failure, pref = (
        signal["routing"], signal["failure_class"], signal["preference_class"]
    )
    require(route != "mixed", "MIXED_REQUIRES_TWO_SEPARATE_SIGNAL_ROUTES")
    require(route != "local-preference", "PREFERENCE_REMAINS_PRIVATE")
    if route == "canonical-candidate":
        require(failure != "none" and pref == "none",
                "CANONICAL_CANNOT_INCLUDE_PERSONAL_PREFERENCE")
        require(signal["expected"] != signal["observed"],
                "NO_DEMONSTRATED_BEHAVIOR_DIFFERENCE")
    elif route == "no-action":
        require(failure == "none" and pref == "none",
                "UNRESOLVED_FEEDBACK_NOT_NO_ACTION")
    elif route == "hold":
        # Unresolved competing interpretations can remain held, but a
        # user-specific preference must never become public canonical source.
        require(pref == "none", "PRIVATE_PREFERENCE_NOT_PUBLIC_FEEDBACK")

    # No server-side identity inference, source weighting, automatic promotion
    # or textual rephrasing. Codebook values are the *only* accepted content.
    # Even HOST_OBSERVED is merely a claim supplied by an untrusted caller.
    return {
        "schema_version": 1,
        "status": "STRUCTURED_UNTRUSTED_FEEDBACK_REVIEW_REQUIRED",
        "skill_id": target,
        "layer": signal["layer"],
        "failure_class": failure,
        "scenario": signal["scenario"],
        "expected": signal["expected"],
        "observed": signal["observed"],
        "evidence_tier_as_claimed": signal["evidence_tier"],
        "routing_requested": route,
        "canonical_change_authorized": False,
        "evidence_independently_verified": False,
        "external_source_weight_applied": False,
        "source_identity_recorded": False,
        "preferences_saved_or_published": False,
        "public_identity_anonymity_guaranteed": False,
        "reproduction_required_for_promotion": True,
    }



def prepare_public_draft(signal):
    """Only canonical candidates; fixed text, no issue submission or network."""
    result = validate(signal)
    require(result["routing_requested"] == "canonical-candidate",
            "PUBLIC_DRAFT_REQUIRES_CANONICAL_CANDIDATE")
    require(signal["skill_id"] in authored_targets(), "PUBLIC_TARGET_NOT_AUTHORED")
    # Values were independently allowlisted by validate. Never copy arbitrary keys.
    return {
        "status": "DRAFT_ONLY_PRIVACY_AND_AUTHORIZATION_REVIEW_REQUIRED",
        "title": "[Skill feedback] Canonical defect",
        "template_url": "https://github.com/Knapp-Kevin/skillz/issues/new?template=agent-skill-feedback.yml",
        "fields": {key: signal[key] for key in ("skill_id", "layer", "failure_class",
                   "scenario", "expected", "observed", "evidence_tier")},
        "post_authorized": False,
        "account_anonymity_guaranteed": False,
    }


def authored_targets():
    parent = ROOT / "skills" / "authored"
    return {p.name for p in parent.iterdir() if p.is_dir() and not p.is_symlink()
            and (p / "SKILL.md").is_file() and not (p / "SKILL.md").is_symlink()}


def pairs_unique(pairs):
    value = {}
    for key, item in pairs:
        require(key not in value, "DUPLICATE_JSON_KEY")
        value[key] = item
    return value


def load(path):
    p = Path(path).absolute()
    require(p.is_file() and not any(x.is_symlink() for x in (p, *p.parents))
            and p.stat().st_size <= MAX_BYTES,
            "MISSING_UNSAFE_OR_OVERSIZED_INPUT")
    with p.open(encoding="utf-8") as handle:
        return json.load(handle, object_pairs_hook=pairs_unique,
                         parse_constant=lambda _: (_ for _ in ()).throw(
                             FeedbackHold("NONFINITE_JSON_NOT_ALLOWED")))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--public-draft", action="store_true", help="Prepare a categorical draft only; never submit.")
    args = parser.parse_args(argv)
    try:
        signal = load(args.input)
        result = prepare_public_draft(signal) if args.public_draft else validate(signal)
        print(json.dumps(result, sort_keys=True, indent=2))
        return 0
    except (FeedbackHold, ValueError, OSError, TypeError, UnicodeError, RecursionError) as exc:
        # Emit only fixed diagnostic codes, never rejected input contents.
        message = str(exc) if isinstance(exc, FeedbackHold) else "INVALID_JSON_OR_INPUT"
        if not re.fullmatch(r"[A-Z0-9_:-]+", message, re.ASCII):
            message = "INVALID_JSON_OR_INPUT"
        print("FEEDBACK_INTAKE_HOLD:" + message, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
