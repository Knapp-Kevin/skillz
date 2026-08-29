# System State

## Snapshot metadata

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-28 |
| **Milestone** | Initial alpha |
| **State** | Implementation foundation and proof hardening complete; external execution proof pending |
| **Authoritative closure tracker** | GitHub Issue #15 |
| **Automatic GitHub Actions** | Disabled; workflow is manual-dispatch only |

## Current architecture

```text
skillz/
├── README.md                         human-first front door + AI jump
├── BOOTSTRAP.md                      first-visit + returning-user workflow
├── AGENTS.md                         agent operating contract
├── skills/                           local/imported user-facing library skills
│   ├── categories/                   human browse-by-purpose navigation
│   └── sources/                      12 exact-revision pinned source corpora
├── engine/skills/                    repository machinery, excluded from library count
├── registry/
│   ├── sources.yaml                  source identity, role, pin, license
│   ├── categories.yaml               canonical local category assignments
│   ├── skills/                       per-skill provenance companions
│   ├── verification/                 exact-version quality state + tags
│   └── taxonomy.yaml                 controlled characterization vocabulary
├── scripts/
│   ├── build-index.ts                schema-v2 catalog generator
│   ├── verify-vendor-materialization.ts exact source-state gate
│   ├── verify-index-idempotency.ts   semantic + two-pass catalog proof
│   ├── initial-alpha-preflight.ts    one-command runtime preflight
│   ├── render-alpha-scenario.ts      public-only treatment renderer
│   └── verify-alpha-evaluator-bundle.mjs private rubric/fixture binding proof
├── docs/evals/                       public matrix, v2 treatment fixtures, runbook, evidence
└── INDEX.md / index.json             generated catalog; refresh pending
```

The scenario-specific v2 evaluator rubric is intentionally **not** part of the repository. It must remain outside any treatment-agent-accessible surface and is bound to the public fixture by set ID and SHA-256 before scoring.

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

- README begins with human instructions;
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
- exact superproject + vendored-submodule materialization verifier;
- schema-v2 index generator;
- semantic catalog invariants plus two-pass idempotency verifier;
- verification registry parser;
- governed candidate selection fixture tests;
- initial implementation contract tests;
- rotated public-only v2 journey scenarios with neutral IDs;
- public fixture tests that forbid evaluator answer-key fields;
- public treatment renderer;
- private evaluator-bundle verifier bound to public set ID, exact SHA-256, and complete scenario coverage;
- one-command initial alpha preflight;
- strict characterization fingerprint-integrity verifier.

Invalidated evidence architecture:

- the original public v1 journey set used the identifiers A1/A2/A3/R1/R2 and committed evaluator-only expected decisions and scoring criteria;
- those mappings remain recoverable from Git history, so that set is permanently invalid as blind behavioral evidence;
- the v2 set rotates both scenario contexts and neutral IDs, while evaluator-only mappings remain outside the repository.

Not yet established:

- exact source-state PASS on the current commit from a fully materialized checkout;
- schema-v2 generated catalog from that checkout;
- exact current corpus counts;
- byte-identical materialized second-pass generation;
- verified private v2 evaluator bundle at execution time;
- behavioral PASS for all five rotated v2 treatment scenarios;
- final alpha lock.

## Runtime blocker

This conversation's execution environment cannot resolve `github.com`/`api.github.com`, so it cannot materialize the pinned submodules locally. GitHub Actions are intentionally not being used as a workaround because the repository is protecting Actions budget. A connected Hugging Face CPU Job was also tested and returned `402 Payment Required` for a trivial job.

The remaining full-corpus proof must run in a normal network-capable local checkout or equivalent development environment.

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

Then verify the separately held private evaluator bundle with `scripts/verify-alpha-evaluator-bundle.mjs`, execute the five neutral v2 scenario IDs listed by `docs/evals/run-initial-alpha.md` in fresh treatment contexts, and record actual evidence under `docs/evals/results/`.

## Alpha status

**NOT LOCKED.**

The implementation and proof architecture are substantially complete. Remaining gates are materialized source/catalog proof, five genuinely blind v2 journey proofs, exact-count/document reconciliation, and evidence-backed closure.

See `docs/alpha-lock.md`, `docs/initial-implementation.md`, `docs/evals/run-initial-alpha.md`, and Issue #15.
