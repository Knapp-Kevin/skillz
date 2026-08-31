# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-31 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 128 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS historical review** | 72 / 72 |
| **AWS current-standard companion complete** | 28 / 72 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

```text
skillz/
├── README.md
├── AGENT_START_HERE.md
├── BOOTSTRAP.md
├── AGENTS.md
├── INDEX.md                         passive human catalog snapshot
├── index.json                       passive machine catalog snapshot
├── CURATED.md
├── CURATION_QUEUE.md                living curation evidence ledger
├── skills/                          43 first-party user-facing skill packages
│   ├── categories/                  human browse-by-purpose navigation
│   └── sources/                     12 intact exact-revision third-party corpora
├── engine/skills/                   passive repository-use/curation procedures
├── registry/
│   ├── sources.yaml                 19 unique source identities/roles/pins
│   ├── source-signals.yaml          volatile source-level context
│   ├── skills/                      mandatory per-skill provenance companions
│   ├── verification/                exact-version semantic review companions
│   ├── local-verification.json      first-party structured reviews
│   ├── categories.yaml              canonical first-party category assignments
│   └── taxonomy.yaml                controlled metadata vocabulary
└── docs/                            governance, provenance, curation, evidence, history
```

The canonical physical boundary is reflected in the live tree: user-facing first-party material is under `skills/`, intact pinned third-party corpora are under `skills/sources/<source-id>/`, and passive repository-use/curation instructions are under `engine/skills/` and excluded from user-facing counts.

There is no repository-owned runtime, root scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Pinned third-party repositories may contain their own code or tooling; those remain intact upstream package components and are not repository-owned execution machinery.

## Inventory boundaries

- **43 active first-party user-facing skills** have structured semantic review records and **43/43 provenance companions** under `registry/skills/local-skills/`.
- **12 pinned external corpora** provide the broad 500+ reference surface.
- **128 current exact-version third-party verification companion files** are persisted.
- `registry/sources.yaml` contains **19 unique source identities**.
- AWS Agent Toolkit has an established eligible denominator of **72 skills** and prior full-pass evidence of **70 verified / 2 rejected**. All 72 were historically inspected at the registered pin. **28/72** now have current-standard per-skill provenance + verification companion pairs; **44** reconciliation gaps remain.
- Historical source-level curation evidence remains valid for what it establishes. Companion reconciliation searches existing records and recoverable historical evidence before performing a fresh exact-version review.
- `engine/skills/` procedures do not count as user-facing inventory.

## Latest sequential AWS reconciliation batch

This batch closed seven genuine companion gaps without changing the registered AWS source pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`:

| Skill | Exact package tree | State | Score | Authority | Portability |
|---|---|---|---:|---|---|
| `managing-amazon-msk` | `b16afcc92da29d85d0e610d38a1c49b20e5e32e8` | verified | 16/20 | mutating | low |
| `migrate-to-msk` | `a4e9b51d24f59d5bfc0bbb7bf234a2d096163911` | verified | 17/20 | mutating | low |
| `querying-data-lake` | `a619aa25a608b7efac3d5439b1e9c5a0d303defc` | verified | 18/20 | mutating | low |
| `amazon-aurora-mysql` | `0e3f93d02d0bff4d76ae31f425527441989717e1` | verified | 18/20 | mutating | low |
| `amazon-aurora-postgresql` | `eb9414ad02354efaa482cb24003af763030ec00d` | verified | 18/20 | mutating | low |
| `amazon-documentdb` | `4fc95aee114b9b6911dcdfc1d41a9715c3df4e62` | verified | 16/20 | mutating | low |
| `amazon-elasticache` | `7ab33b79df92988e90fe25e9318fe748c7d15149` | verified | 17/20 | mutating | low |

Behavioral evidence remains `not-run` for this static curation batch. The reviews preserve upstream scripts/assets/references as package dependencies rather than treating them as `skillz` runtime.

## Source lifecycle

The repository distinguishes:

**discovery surface → candidate issue/source → source-vetting → admitted corpus/reference/tracked source → individual exact-version review → user-fit decision**

Newly discovered third-party candidates use the issue-first intake workflow before admission. The candidate issue is the pre-admission evidence workspace; finalized provenance and verification companions are persisted only after a justified admission decision.

Intentional discovery surfaces are documented in `docs/discovery-surfaces.md`. The connected Creator Technical Resource Catalog is discovery intelligence only; its rows, scores, verification labels, creator attributions, and recommendations are not `skillz` provenance or individual quality evidence.

## Quality model

- Source identity and individual skill quality are separate.
- Every governed user-facing skill must have truthful provenance and applicable exact-version review evidence before the corpus can describe it as companion-complete.
- Pinned/tracked material is reference/design evidence unless an exact-version record establishes stronger eligibility.
- `verified` means structured semantic review passed for the exact bound material.
- `validated` means representative external scenario/adversarial evidence was also recorded.
- `unverified` and legacy `trusted-baseline` are not unchanged-reuse states.
- `stale`, `rejected`, and `retired` are excluded from normal unchanged selection.
- Fingerprints identify reviewed material. They are provenance/bookkeeping evidence, not executable proof.
- Static source completion requires an exact eligible denominator and a decisive current state for every in-scope skill.

Interpret candidates in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue AWS Agent Toolkit current-standard companion reconciliation sequentially until the remaining 44 gaps are closed, preserving historical evidence and avoiding duplicate review.
2. Complete Microsoft Skills.
3. Complete Microsoft Azure Skills.
4. Continue remaining admitted creator/registered-source curation to the same mandatory standard.
5. Continue governed discovery/source-vetting in parallel when evidence supports useful candidates.
6. Keep README, governance, category navigation, source registry, catalog snapshots, and public counts aligned with material corpus changes.

The current living work surface is `CURATION_QUEUE.md` plus provenance audit issue #66. Closed historical Wayfinder/issues/PRs remain evidence, not active execution plans.
