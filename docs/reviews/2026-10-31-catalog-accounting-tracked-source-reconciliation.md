# Public catalog accounting and tracked-source visibility reconciliation

**Date:** 2026-10-31  
**Base main:** `597d0044e75e5cf6a85a0d0022fb37bd4001caa7`  
**Exact Git tree:** `dce1342217143525ed20e91e37ba946210c91c28`

## Independent evidence

GitHub's complete recursive tree returned `2519` entries with `truncated=false`. Counted **1039** `registry/verification/**/*.yaml` blobs and **1039** matching `registry/skills/**/*.yaml` blobs, including **44** first-party `skills/<name>/SKILL.md` manifests. The existing JSON catalog reports **995** third-party persisted reviews: **874** registered/tracked and **121** candidate-only. Individual registered companion pairs were checked for Bhushan Modi **68/68**, OpenClaw **8/8**, and Archie Indian **56/56**. All three are static-review complete at their registered pins; no new reviews or approvals were created.

## Defects and correction

- `docs/SYSTEM_STATE.md` current snapshot table incorrectly showed **989 / 1033** while its own current summary correctly showed **995 / 1039**.
- `INDEX.md` current totals table incorrectly showed **989 / 1025**, while `index.json` correctly showed **995 / 1039**. These were current-label errors, not historical checkpoints.
- Current source-family tables in README, SYSTEM_STATE and CURATION_QUEUE omitted the three newly complete tracked families, despite individual exact-version companions and current JSON counters.
- README and INDEX presented long chronological tranche histories ahead of current navigation and accounting. Those historical records remain available in CURATION_QUEUE and dated review receipts; the front doors now prioritize current facts.

## Scope and safeguards

Changed only passive documentation/catalog text. `index.json` was independently checked and is already correct; no JSON mutation is necessary. No source pin, review identity, package, security evidence, taxonomy, skill manifest, first-party inventory or denominator changed. **Admitted-source denominator delta: 0. New review pairs: 0.** No scanner, behavioral test, CI, runtime, scheduler, generator, background service, or upstream package tooling was executed or added.

Archie's source terms remain unresolved in [#544](https://github.com/Knapp-Kevin/skillz/issues/544). The 36 changed first-party package trees across drafts [#489](https://github.com/Knapp-Kevin/skillz/pull/489), [#492](https://github.com/Knapp-Kevin/skillz/pull/492) and [#496](https://github.com/Knapp-Kevin/skillz/pull/496) remain external security/adversarial qualification holds; admissions #412/#413 remain separate holds. None of these drafts is modified or merge-approved by this documentation reconciliation.
