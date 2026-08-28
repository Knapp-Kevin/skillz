# Roadmap

`skillz` is a reusable AI-skill library plus an engine for building and maintaining a fitted skill set for a person or team.

The roadmap is organized around **user capability**, not raw skill count. The library can grow indefinitely. The initial implementation ends when the first-visit and returning-user experiences are proven reliable.

## Current milestone: initial alpha

Status: **IMPLEMENTED, EXECUTION PROOF PENDING**

The foundational implementation is on `main`. The remaining work is deliberately narrow.

### 1. Materialized catalog proof

From a normal network-capable checkout with all pinned submodules initialized:

1. run `node scripts/initial-alpha-preflight.ts`;
2. regenerate the schema-v2 `INDEX.md` and `index.json`;
3. require byte-identical output on the second generator pass;
4. record exact local, vendored, total-entry, unique-name, and source counts;
5. reconcile README counts with generated truth.

This proof is intentionally not replaced by an estimate from GitHub search or an automatic GitHub Actions run.

### 2. First-visit journey proof

Execute the frozen synthetic scenarios in `docs/evals/fixtures/initial-alpha-scenarios.json` using the leak-safe renderer:

- **A1**: correctly reuse or minimally adapt an eligible exact-version skill;
- **A2**: refuse unverified or stale material for trusted unchanged reuse;
- **A3**: create a custom skill when forcing a library match would distort the user's actual workflow.

Each run must truthfully report evaluation and installation/handoff state.

### 3. Returning-user journey proof

Execute:

- **R1**: inventory the current fitted set, detect real drift or a gap, preserve still-valid custom behavior, and make the smallest justified change;
- **R2**: correctly conclude **NO CHANGE NEEDED** when newer material does not establish a meaningful improvement.

### 4. Alpha lock

Alpha is locked only when:

- materialized catalog preflight passes;
- all five journey scenarios pass their frozen criteria;
- result evidence is recorded under `docs/evals/results/`;
- generated counts and public documentation agree;
- `docs/alpha-lock.md` and Issue #15 are reconciled to the evidence.

See [`docs/initial-implementation.md`](docs/initial-implementation.md), [`docs/alpha-lock.md`](docs/alpha-lock.md), and [`docs/evals/run-initial-alpha.md`](docs/evals/run-initial-alpha.md).

## Post-alpha: curation and refinement

Once alpha is locked, ongoing work shifts primarily to library enrichment.

### Corpus curation

- discover high-value first-party, official, and community skills;
- preserve source, author, license, path, exact revision, and skill-specific freshness;
- characterize useful skills with controlled tags;
- verify non-governed candidates before trusted unchanged reuse;
- behaviorally validate important skills where representative evidence is practical;
- retire, quarantine, or re-review skills when content fingerprints change.

Broad corpus expansion is valuable, but it is **not** an initial-alpha blocker.

### Selection quality

- refine taxonomy coverage from real bootstrap/refinement usage;
- tune matching weights without turning tags into automatic authority;
- improve duplicate/overlap detection across sources;
- learn when composition, adaptation, supplementation, or custom creation beats unchanged reuse.

### Returning-user refinement

- improve drift and overlap diagnostics;
- strengthen portable profile versioning;
- make small-change and no-change decisions more evidence-driven;
- expand safe upgrade/retirement guidance.

### Installation portability

- add host adapters when there is a real supported installation surface;
- keep portable skill identity separate from host packaging;
- preserve explicit completion states rather than claiming installation that did not occur.

### Human library experience

- evolve category navigation as the corpus grows;
- improve direct links, browsing, filtering, and search;
- keep the README human-first while preserving an unmistakable AI-agent entry route;
- make provenance and quality state understandable without requiring users to understand repository internals.

## Durable design rules

1. **Compare before creation. User-fit before reuse.**
2. **Smallest useful set over maximum skill count.**
3. **Availability is not verification.**
4. **Exact-version evidence matters.** Fingerprint drift invalidates prior characterization until reviewed.
5. **Attribution travels with third-party material.**
6. **Engine machinery does not count as library inventory.**
7. **Indexed approved vendor skills do count as available library corpus.**
8. **Installation or a precise portable handoff is part of completion.**
9. **Returning users are refined, not reset.**
10. **No-change is a valid outcome.**

## Historical work

The July 2026 pulse, research, daily-ops, repository-hygiene, and lifecycle-tooling build series is complete historical work. Its detailed record remains in git history, `docs/BACKLOG.md` completed entries, evaluation artifacts, and the historical governance ledger. It no longer defines the product roadmap.
