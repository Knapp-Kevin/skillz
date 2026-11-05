---
name: skill-eval
description: >-
  Perform a structured semantic evaluation of a first-party or third-party skill
  against the repository's current quality rubric, recording strengths,
  limitations, metadata, and a decisive disposition. Use for repository curation.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Eval
  emoji: "⚖️"
  version: 2.0.1
  repo-bound: true
---

# Skill Eval

**Repository-curation procedure only.**

`skillz` evaluates instruction artifacts semantically. This procedure does not benchmark multiple models, compare baseline/treatment token counts, or claim behavioral success rates.

## Procedure

1. Establish the exact artifact being reviewed:
   - source/repository;
   - canonical path;
   - revision or other exact identity when available;
   - complete package Git tree and SKILL.md blob fingerprints when establishable (do not confuse the two);
   - applicable license and attribution.
2. Read the complete skill package, including any skill-owned scripts, references, templates, examples, fixtures, or other components that materially affect behavior.
3. Identify the capability the skill claims to provide and its expected triggers/non-triggers.
4. Review against `docs/skill-verification.md`, including:
   - clarity and procedural completeness;
   - evidence discipline;
   - authority and side effects;
   - dependencies and host assumptions;
   - privacy/security implications;
   - portability;
   - failure handling;
   - provenance/licensing;
   - overlap and differentiated value.
5. Read the instructions adversarially using representative **static semantic** scenarios:
   - a normal positive trigger;
   - an obvious non-trigger;
   - the most important pressure/failure case.
   These are reviewer interpretations, not observed host behavior.
6. Separate whole-skill quality from component value. A skill unsuitable for unchanged reuse may still contain a useful mechanism, provided its constraints and provenance follow that mechanism.
7. Assign a rubric score and decisive disposition using `docs/skill-verification.md`. `verified` requires an exact-version structured semantic review with no hard fail and the rubric thresholds met. `validated` additionally requires **actual representative external host-executed behavioral/adversarial evidence bound to that exact package**. Static scenarios, plans, and written acceptance cases never qualify.
8. Record behavioral validation as `not-run` when no qualifying execution evidence exists. Keep package-security state separate under `docs/security-scanning.md`; a semantic pass never implies a scanner pass or unchanged-use eligibility. A historical `incomplete` scan stays `incomplete` even if a complete direct content review succeeds.
9. Record material caveats, including missing evidence, honestly. Do not convert unknowns into a positive assumption.
10. Record the original `reviewed_at` and the separate latest exact-identity `checked_at`, together with `current-reviewed`, `needs-re-review`, `not-yet-reviewed`, or `source-unavailable` freshness. A changed material file requires an actual new review; never transfer the previous grade by filename or mutate its historical date.
11. Update the appropriate exact-version review/provenance records and controlled tags only when authorized. If a referenced directory is too large to inspect in full, list the bounded scope reviewed and do not imply all contents were read.

## Output

```text
Skill: <name>
Exact identity: <revision, SKILL.md blob, complete package tree, or not established>
Reviewed at: <date of actual semantic review>
Checked at: <latest exact-identity verification, if any>
Freshness: current-reviewed | needs-re-review | not-yet-reviewed | source-unavailable
Material references inspected: <exact files and any bounded directory scope>
Capability: <one sentence>
Rubric score: <score>
Quality state: verified | validated | unverified | stale | rejected | retired
Authority: <classification>
Portability: <classification>
Dependencies/license: <material notes>
Semantic scenarios: <positive / non-trigger / pressure findings; static interpretation only>
Behavioral validation: <not-run / exact external executed evidence reference>
Package security: <separate exact-package state/evidence or not-run>
Differentiated value: <what it adds or duplicates>
Component value: <useful mechanisms, if any>
Disposition: <adopt unchanged / adapt / compose / reference-only / reject / retire>
Material uncertainty: <only unresolved facts>
```

## Negative rules

- Do not make model competency, benchmark success rates, token deltas, or multi-model testing a repository quality requirement.
- Do not fabricate provenance, fingerprints, license terms, dependencies, or review evidence.
- Do not treat source popularity or official branding as proof of individual skill quality.
- Do not discard skill-owned supporting components merely because they are executable or non-Markdown; evaluate them as part of the skill package.
- Do not promote an artifact beyond the evidence actually reviewed.
- Do not call a static scenario review `validated`, or inherit security approval from semantic `verified`.
