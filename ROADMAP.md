# Roadmap

`skillz` is a reusable AI-skill library plus an engine for building and maintaining a fitted skill set for a person or team.

The roadmap is organized around **user capability**, not raw skill count. The library can grow indefinitely. The initial implementation ends when the first-visit and returning-user experiences are proven reliable.

## Current milestone: initial alpha

Status: **IMPLEMENTED, EXECUTION PROOF PENDING**

The foundational implementation and final proof-harness hardening are on `main` or the active alpha-isolation repair. The remaining work is deliberately narrow.

### 1. Materialized catalog proof

From a normal network-capable checkout with all pinned submodules initialized:

1. run `node scripts/initial-alpha-preflight.ts`;
2. require the exact source-state gate to prove a clean superproject plus all 12 initialized clean submodules at their superproject gitlink SHAs;
3. regenerate schema-v2 `INDEX.md` and `index.json`;
4. require semantic catalog invariants and byte-identical output on the second generator pass;
5. record exact local, vendored, total-entry, unique-name, and source counts;
6. reconcile README counts with generated truth.

This proof is intentionally not replaced by an estimate from GitHub search or an automatic GitHub Actions run.

### 2. Blind first-visit journey proof

Execute the three rotated public-only v2 first-visit scenarios from `docs/evals/fixtures/initial-alpha-scenarios.json` through `scripts/render-alpha-scenario.ts` in fresh treatment contexts.

Collectively, the three runs must demonstrate:

- correct reuse or minimal adaptation of an eligible exact-version skill when it genuinely fits;
- refusal to treat unverified or stale material as trusted unchanged reuse;
- custom creation when forcing a library match would distort the user's stable workflow.

The public repository does not reveal which neutral scenario maps to which outcome. Frozen evaluator-only mappings and scoring criteria remain in a private bundle fingerprint-bound to the public fixture.

Each run must truthfully report evaluation and installation/handoff state.

### 3. Blind returning-user journey proof

Execute the two rotated public-only v2 returning-user scenarios in fresh treatment contexts.

Collectively, the runs must demonstrate:

- inventory-first minimal refinement when one real drift/gap exists while most fitted behavior remains valid;
- an explicit **NO CHANGE NEEDED** outcome when newer material does not establish a meaningful improvement.

The treatment agent must not receive the private evaluator mapping before its output is frozen.

### 4. Alpha lock

Alpha is locked only when:

- materialized source/catalog preflight passes;
- the private evaluator bundle verifies against the exact public v2 fixture before treatment execution;
- all five rotated blind journey scenarios pass their frozen private criteria;
- result evidence is recorded under `docs/evals/results/` without republishing the still-active answer key;
- generated counts and public documentation agree;
- `docs/alpha-lock.md` and Issue #15 are reconciled to the evidence.

The original public v1 A1/A2/A3/R1/R2 set is retired and cannot satisfy the behavioral gate because its answer keys remain recoverable from Git history.

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
11. **Blind behavioral evidence requires evaluator isolation.** Public treatment context must not contain the active answer key.

## Historical work

The July 2026 pulse, research, daily-ops, repository-hygiene, and lifecycle-tooling build series is complete historical work. Its detailed record remains in git history, `docs/BACKLOG.md` completed entries, evaluation artifacts, and the historical governance ledger. It no longer defines the product roadmap.
