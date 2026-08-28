# Governance Index

**Last reviewed:** 2026-08-28

This file maps the current control surfaces for `skillz`. Historical Qor-era plans, gate artifacts, and ledger records remain useful history, but they are no longer the live release or curation control plane.

## Tier 1: current product state

These must agree before initial alpha can be locked.

| Artifact | Path | Freshness contract |
|---|---|---|
| Human/AI front door | `README.md` | first-visit, returning-user, direct-library, current alpha status |
| Agent contract | `AGENTS.md` | routing, quality, privacy, mutation boundaries |
| Bootstrap/refinement guide | `BOOTSTRAP.md` | current executable user journeys |
| System state | `docs/SYSTEM_STATE.md` | current architecture, inventory boundaries, blockers |
| Initial implementation boundary | `docs/initial-implementation.md` | what is and is not an alpha blocker |
| Alpha lock checklist | `docs/alpha-lock.md` | every unchecked gate backed by missing evidence, never ceremony |
| Roadmap | `ROADMAP.md` | current milestone first, post-alpha enrichment second |
| Backlog | `docs/BACKLOG.md` | only current execution blockers in active section |
| Feature index | `docs/FEATURE_INDEX.md` | implementation mapped to actual proof state |

## Tier 2: library identity and provenance

These define what is available and where it came from.

| Artifact | Path | Freshness contract |
|---|---|---|
| Source registry | `registry/sources.yaml` | current source role, inclusion, exact pin/reference, license |
| Skill provenance companions | `registry/skills/` | source/path/revision/freshness/relationship for characterized third-party skills |
| Third-party notices | `THIRD_PARTY_NOTICES.md` | attribution/license notices track included third-party material |
| Provenance policy | `docs/third-party-provenance.md` | copying/adaptation/attribution rules remain consistent with registry |
| Curation policy | `docs/curation-policy.md` | availability, curation, verification, validation, refresh semantics |

## Tier 3: quality and selection

These determine what can be trusted for selection, independent of source presence.

| Artifact | Path | Freshness contract |
|---|---|---|
| Verification registry | `registry/verification/` | record applies only to its exact canonical skill fingerprint |
| Taxonomy | `registry/taxonomy.yaml` | controlled tags used consistently by characterization/selection |
| Verification standard | `docs/skill-verification.md` | status meanings and structured rubric current |
| Fingerprint integrity verifier | `engine/skills/source-vetting/scripts/verify-characterization-integrity.ts` | detects content drift before prior characterization is trusted |
| Candidate selector | `engine/skills/skill-bootstrap/scripts/select-candidates.ts` | blocked states remain blocked; unverified unchanged reuse not silently trusted |

A source can be present, reputable, and current while an individual skill remains `unverified`. Source identity does not silently upgrade individual skill quality.

## Tier 4: generated catalog and browsing

| Artifact | Path | Freshness contract |
|---|---|---|
| Human category registry | `registry/categories.yaml` | every local canonical skill has an intentional category assignment |
| Category browse surface | `skills/categories/` | human navigation agrees with canonical category registry |
| Machine catalog | `index.json` | schema-v2 generated truth after materialized refresh |
| Human catalog | `INDEX.md` | generated from the same run as `index.json` |
| Catalog generator | `scripts/build-index.ts` | deterministic against the same fully materialized repository state |
| Idempotency proof | `scripts/verify-index-idempotency.ts` | second pass must be byte-identical |

**Current exception:** checked-in `INDEX.md` / `index.json` are stale schema-v1 output until the materialized alpha preflight runs. Do not treat the old generated counts as current truth.

## Tier 5: alpha behavioral evidence

| Artifact | Path | Freshness contract |
|---|---|---|
| Alpha scenario matrix | `docs/evals/initial-alpha-matrix.md` | five required journey classes remain stable through initial alpha |
| Frozen fixtures | `docs/evals/fixtures/initial-alpha-scenarios.json` | expected decisions/criteria fixed before treatment execution |
| Leak-safe renderer | `scripts/render-alpha-scenario.ts` | treatment input never exposes answer-key fields |
| Runbook | `docs/evals/run-initial-alpha.md` | current preflight/isolation/scoring procedure |
| Result evidence | `docs/evals/results/` | contains only actual executed evidence; absence means not proven |

Static tests are not substitutes for the five behavioral journey results.

## Tier 6: operational safety

| Artifact | Path | Freshness contract |
|---|---|---|
| Structural audit | `engine/skills/skill-audit/scripts/audit.ts` | scans current recursive local skill layout |
| Risk audit | `engine/skills/skill-audit/scripts/risk-audit.ts` | current semantic-risk rules |
| Initial alpha preflight | `scripts/initial-alpha-preflight.ts` | catalog, audits, tests, fingerprint integrity all pass before journey execution |
| Installation contract | `docs/installation-handoff.md` | explicit install/handoff states; no fabricated completion |
| GitHub Actions workflow | `.github/workflows/ci.yml` | manual-dispatch only while Actions budget is protected |

## Historical records

The following may remain intentionally frozen and should not be read as live state unless a current document explicitly points to them:

- `.qor/gates/` session artifacts;
- `docs/META_LEDGER.md` historical seals/events;
- `docs/plan-qor-*.md` historical implementation plans;
- older evaluation reports under `docs/evals/`;
- git history for completed July build-series details.

Historical accuracy should be preserved. Historical documents do not override current Tier 1-6 control surfaces.

## Drift rule

When a current control surface changes:

1. update every other current artifact whose factual state is affected;
2. preserve provenance/history rather than rewriting old evidence;
3. regenerate generated artifacts with their generator rather than hand-editing them;
4. if exact evidence cannot be established, mark the state pending instead of guessing;
5. do not claim alpha lock until the evidence directory and checklist support it.
