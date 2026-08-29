# Architecture Plan

## Architectural objective

Support two equally real uses without conflating them:

1. a large, directly browsable reusable skill library;
2. a self-starting engine that can discover, build, select, evaluate, install, and later refine a fitted skill set for a user.

The architecture must keep **library inventory**, **repository machinery**, **source provenance**, and **quality evidence** distinct.

## System shape

```text
README.md / skills/categories/
        │ human navigation
        ▼
INDEX.md / index.json                 generated human + machine catalog
        ▲
        │
scripts/build-index.ts               schema-v2 deterministic generator
        │
        ├── skills/                   local/imported user-facing library
        │   └── sources/              pinned third-party source corpora
        ├── registry/categories.yaml  human category assignments
        ├── registry/sources.yaml     source identity/role/pin/license
        └── registry/verification/    exact-version quality + tags

BOOTSTRAP.md / AGENTS.md
        │
        ▼
engine/skills/skill-bootstrap/        first-visit + returning-user orchestration
        │
        ├── select-candidates.ts      governed exact-version shortlisting
        ├── skill-forge              custom skill creation
        ├── skill-eval               behavioral evaluation procedure
        ├── skill-audit              structural/risk validation
        ├── skill-sync               installation/portable handoff support
        └── source-vetting           source + fingerprint integrity tooling
```

## Inventory boundaries

### `skills/`

Canonical local/imported **user-facing library skills**. These count as library inventory.

Discovery is recursive so category folders may become canonical physical paths later without breaking audit, index, or sync behavior.

### `skills/sources/`

Pinned third-party repositories represented by exact gitlinks. Approved indexed user-facing skills in these corpora are available library material and count toward the searchable corpus.

Vendored presence does **not** imply individual quality verification.

### `engine/skills/`

Skill-shaped procedures used to operate `skillz` itself. They do not count toward the user-facing library total.

Current engine responsibilities include bootstrap, evaluation, creation, audit, synchronization, ecosystem intake, and source verification.

### `registry/`

Machine-readable governance and selection metadata. It does not contain executable product logic.

- `sources.yaml`: source identity, role, inclusion, pin, license;
- `categories.yaml`: canonical local browse categories;
- `skills/`: per-skill provenance companions;
- `verification/`: exact-version quality state, fingerprints, tags, evidence;
- `taxonomy.yaml`: controlled characterization vocabulary;
- `candidates.yaml`: historical/current candidate intake data where still applicable.

## Load-bearing rules

1. **The library and engine are different populations.** Engine mechanics never inflate skill-library counts.
2. **Approved indexed vendor skills are library material.** A git submodule is not invisible merely because it is external source content.
3. **Generated catalog files are derived, never hand-maintained.** `INDEX.md` and `index.json` come from `scripts/build-index.ts`.
4. **Availability is not verification.** A skill may be searchable while remaining unverified for trusted unchanged reuse.
5. **Quality evidence is exact-version evidence.** Characterization and verification bind to the canonical `SKILL.md` fingerprint.
6. **Fingerprint drift invalidates prior characterization.** Changed content requires review before prior quality state is trusted.
7. **Attribution remains attached to third-party work.** Source, author/project, license, path, revision, and material adaptation relationship are recorded as applicable.
8. **Compare before creation. User-fit before reuse.** The corpus is design evidence, not a reuse quota.
9. **Installation state is explicit.** The system distinguishes installed, verification-pending, ready-to-upload, user-action-required, and blocked states.
10. **Returning users are refined, not reset.** Existing skills are evidence; valid custom behavior is preserved unless a concrete reason supports change.
11. **Private access is scoped.** Connector availability is capability, not blanket permission to mine unrelated private data.
12. **GitHub Actions are not an implicit runtime.** Automatic Actions are currently disabled/manual-only; local deterministic proof remains supported.

## Catalog architecture

`build-index.ts` scans the fully materialized repository and emits schema-v2 catalog data including:

- local skill identity and human category;
- indexed vendor skill identity and source;
- source role/class/license metadata;
- exact-version quality state when a verification record exists;
- controlled characterization tags;
- fingerprint metadata where characterized;
- explicit local/vendor/entry/unique/source counts.

Cross-source skills with the same name may remain separate implementations. Duplicate copies inside one source are deduplicated according to generator policy.

`verify-index-idempotency.ts` permits a stale first pass to refresh generated files, then requires the second pass to be byte-identical.

## Selection architecture

`engine/skills/skill-bootstrap/scripts/select-candidates.ts` is a deterministic **shortlisting** primitive, not the final decision-maker.

Default unchanged-reuse eligibility:

- eligible states: `trusted-baseline`, `verified`, `validated`;
- blocked states: `stale`, `rejected`, `retired`;
- `unverified`: excluded from trusted unchanged selection by default, optionally surfaced as design evidence only.

Controlled tag overlap can rank eligible candidates, but the bootstrap agent must still decide whether actual user fit calls for `ADOPT`, `ADAPT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, or no formal skill.

## First-visit and returning-user orchestration

The repository URL is sufficient invocation context for first-visit bootstrap when no more specific task is given.

Bootstrap:

1. binds to authoritative host/project instructions and legitimately accessible evidence;
2. discovers durable working methods/latent skill candidates;
3. compares needs against existing skills and governed corpus metadata;
4. designs the smallest useful fitted system;
5. adversarially reviews/evaluates as appropriate;
6. installs when supported and authorized, otherwise produces a precise portable handoff.

Returning refinement begins by inventorying the current fitted set. It checks current fit, fingerprints, overlap, gaps, and newer candidates, then makes only justified changes. `NO CHANGE NEEDED` is a valid result.

## Proof architecture

### Mechanical/static

- recursive discovery shared across index/audit/risk/sync;
- structural and semantic risk audits;
- selection fixtures;
- fingerprint-integrity checks;
- initial implementation contract tests;
- leak-safe alpha scenario renderer tests.

### Materialized runtime

`node scripts/initial-alpha-preflight.ts` runs:

1. two-pass catalog determinism;
2. structural audit;
3. risk audit;
4. repository tests;
5. characterization fingerprint integrity.

### Behavioral

Initial alpha requires five isolated synthetic journey proofs:

- A1 eligible reuse/minimal adaptation;
- A2 unverified/stale refusal;
- A3 custom creation;
- R1 returning minimal refinement;
- R2 returning no-change.

Static tests do not substitute for these behavioral results.

## Mutation boundaries

Repository inspection, comparison, characterization, and design are read-only by default.

Writes, installation, publishing, permission changes, sending, or other external side effects require the authority expected by the destination environment. Dry-run or portable handoff is preferred when authority or installation support is not established.

## Historical governance

`.qor/`, `docs/META_LEDGER.md`, and `docs/plan-qor-*.md` remain historical implementation evidence. They are not the current architecture control plane and do not override `README.md`, `AGENTS.md`, `BOOTSTRAP.md`, `docs/SYSTEM_STATE.md`, `docs/GOVERNANCE_INDEX.md`, or the current alpha checklist.
