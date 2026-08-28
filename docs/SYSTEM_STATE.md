# System State

## Snapshot metadata

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-28 |
| **Milestone** | Initial alpha |
| **State** | Implementation foundation complete; execution proof pending |
| **Authoritative closure tracker** | GitHub Issue #15 |
| **Automatic GitHub Actions** | Disabled; workflow is manual-dispatch only |

## Current architecture

```text
skillz/
├── README.md                         human-first front door + AI jump
├── BOOTSTRAP.md                      first-visit + returning-user workflow
├── AGENTS.md                         agent operating contract
├── skills/                           local/imported user-facing library skills
│   └── categories/                   human browse-by-purpose navigation
├── engine/skills/                    repository machinery, excluded from library count
├── vendor/                           12 exact-revision pinned source corpora
├── registry/
│   ├── sources.yaml                  source identity, role, pin, license
│   ├── categories.yaml               canonical local category assignments
│   ├── skills/                       per-skill provenance companions
│   ├── verification/                 exact-version quality state + tags
│   └── taxonomy.yaml                 controlled characterization vocabulary
├── scripts/
│   ├── build-index.ts                schema-v2 catalog generator
│   ├── verify-index-idempotency.ts   two-pass deterministic catalog proof
│   ├── initial-alpha-preflight.ts    one-command runtime preflight
│   └── render-alpha-scenario.ts      leak-safe journey fixture renderer
├── docs/evals/                       alpha matrix, fixtures, runbook, evidence
└── INDEX.md / index.json             generated catalog; refresh pending
```

## Inventory boundaries

| Population | Current state |
|---|---|
| Local/imported user-facing skills | 42 canonical local library skills |
| Engine skills | 7 repository-operating skills; excluded from library inventory |
| Vendored source corpora | 12 pinned git submodules |
| Registered sources | 14 total: 12 vendored plus 2 reference/discovery sources |
| Total usable indexed library | **500+ conservatively; exact current deduplicated count pending schema-v2 materialized regeneration** |

Do not substitute the July 4 count of 524 or the temporary `500+` README badge for the next exact generated count.

## Quality and provenance state

- Source identity and individual skill quality are separate concepts.
- Missing individual quality metadata defaults to `unverified` for trusted unchanged selection.
- Characterization/quality records are bound to exact canonical `SKILL.md` Git blob fingerprints.
- A changed fingerprint makes the prior characterization stale until refreshed.
- `verified` means structured review passed.
- `validated` requires representative behavioral evidence.
- `stale`, `rejected`, and `retired` material is excluded from default governed selection.
- Third-party source, author/project, license, revision, path, freshness, and relationship are preserved in registry/notices as applicable.

## User experience state

### Human

Implemented:

- README begins with human instructions.
- first-visit and returning-user tracks are explicit;
- direct browse by purpose exists under `skills/categories/`;
- provenance, verification, curation, installation, and repository maps are linked from the front door.

### AI agent

Implemented:

- immediate README jump to agent-specific instructions;
- direct-library, first-visit, returning-user, and repository-maintenance routing;
- verification-aware candidate selector;
- user-fit-before-reuse and compare-before-creation doctrine;
- explicit install/handoff completion states;
- privacy boundary that connector availability is not consent to profile unrelated private data.

## Verification surfaces

Implemented static/mechanical proof:

- recursive local discovery shared by index, audit, risk-audit, and sync;
- schema-v2 index generator;
- verification registry parser;
- governed candidate selection fixture tests;
- initial implementation contract tests;
- five frozen synthetic alpha journey scenarios;
- leak-safe scenario renderer and anti-answer-key tests;
- two-pass catalog idempotency verifier;
- one-command initial alpha preflight;
- characterization fingerprint-integrity verifier.

Not yet established:

- schema-v2 generated catalog from a fully materialized checkout;
- exact current corpus counts;
- byte-identical materialized second-pass generation;
- behavioral PASS for A1, A2, A3, R1, or R2;
- final alpha lock.

## Runtime blocker

This conversation's execution environment cannot resolve `github.com`, so it cannot materialize the pinned submodules locally. GitHub Actions are intentionally not being used as a workaround because the repository is protecting Actions budget.

The remaining proof must run in a normal network-capable local checkout or equivalent development environment.

## Exact next action

```bash
git clone --recurse-submodules https://github.com/Knapp-Kevin/skillz.git
cd skillz
git submodule update --init --recursive
node scripts/initial-alpha-preflight.ts
```

Require the terminal state:

```text
READY FOR JOURNEY EVALUATION. This is not behavioral proof by itself.
```

Then execute isolated A1, A2, A3, R1, and R2 through `scripts/render-alpha-scenario.ts` and record actual evidence under `docs/evals/results/`.

## Alpha status

**NOT LOCKED.**

The implementation architecture is substantially complete. Remaining gates are materialized catalog proof, five isolated journey proofs, exact-count/document reconciliation, and evidence-backed closure.

See `docs/alpha-lock.md`, `docs/initial-implementation.md`, `docs/evals/run-initial-alpha.md`, and Issue #15.
