# Local Skill Library

This directory contains the first-party/local user-facing portion of the `skillz` library.

## Browse by purpose

Humans can start with [`categories/`](categories/):

- [Planning & Productivity](categories/planning-productivity/)
- [Writing & Communication](categories/writing-communication/)
- [Research & Analysis](categories/research-analysis/)
- [Software & Repositories](categories/software-repositories/)
- [Agent Operations & Security](categories/agent-operations-security/)
- [Monitoring & Intelligence](categories/monitoring-intelligence/)
- [Business & Career](categories/business-career/)

Category folders are a human navigation layer. Canonical active local skill content is the discovered `SKILL.md` material under `skills/`.

## Counting boundary

Every active user-facing local skill counts, but `skills/` is not the whole reference ecosystem.

The repository also carries approved vendored/tracked third-party reference material. Repository machinery under [`../engine/skills/`](../engine/skills/) does not count as user-facing inventory.

Broad third-party source presence means **referenceable**, not automatically **trusted unchanged**.

## First-party quality records

Active local skills are not exempt from the same quality discipline applied to third-party work merely because we wrote them ourselves. Home-field advantage is not a verification method.

Their exact-version review manifest is:

[`../registry/local-verification.json`](../registry/local-verification.json)

For every active local `SKILL.md`, that manifest records:

- exact Git blob fingerprint;
- individual structured rubric score;
- current quality state;
- behavioral-validation status;
- controlled use-case/lifecycle/characteristic tags;
- authority and portability;
- material review notes.

`node scripts/verify-share-ready-corpus.ts` compares the manifest against every active local skill and fails when:

- a local skill is missing an individual review;
- a reviewed local skill no longer exists;
- canonical content changed without a refreshed fingerprint/review;
- an active local skill is below the current verified quality threshold;
- controlled metadata is incomplete or invalid.

Behavioral validation is separate. `validation_status: not-run` is an explicit limitation, not a euphemism for "probably fine."

## Third-party quality states

Individually governed third-party skills use provenance under [`../registry/skills/`](../registry/skills/) and exact-version quality records under [`../registry/verification/`](../registry/verification/).

Current unchanged-reuse semantics are:

- `verified`: exact version passed the structured review and may be considered when operational/user fit matches;
- `validated`: `verified` plus representative behavioral evidence;
- `unverified`: design/reference evidence only;
- `trusted-baseline`: legacy schema compatibility only, not current unchanged-selection eligibility;
- `stale`: prior exact-version evidence no longer applies;
- `rejected` / `retired`: excluded from normal unchanged selection.

A reference can still contribute a useful mechanism without becoming the final workflow. Material adaptation remains subject to provenance, licensing, dependency, authority, and rejection/staleness constraints.

See [`../docs/skill-verification.md`](../docs/skill-verification.md), [`../docs/curation-policy.md`](../docs/curation-policy.md), and [`../registry/verification/README.md`](../registry/verification/README.md).