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
| **Persisted third-party review companions** | 140 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS historical review** | 72 / 72 |
| **AWS current-standard companion complete** | 40 / 72 |
| **AWS current-standard gaps** | 32 |
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

The canonical physical boundary is reflected in the live tree. `skillz` owns no runtime, root scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Pinned third-party repositories may contain their own code or tooling; those remain intact upstream package components rather than repository-owned execution machinery.

## Inventory boundaries

- **43 active first-party user-facing skills** have structured semantic review records and **43/43 provenance companions** under `registry/skills/local-skills/`.
- **12 pinned external corpora** provide the broad 500+ reference surface.
- **140 current exact-version third-party verification companion files** are persisted.
- `registry/sources.yaml` contains **19 unique source identities**.
- AWS Agent Toolkit has an established eligible denominator of **72 skills** and prior full-pass evidence of **70 verified / 2 rejected**. All 72 were historically inspected at the registered pin. **40/72** now have current-standard per-skill provenance + verification companion pairs; **32** reconciliation gaps remain.
- Historical source-level evidence remains valid for what it establishes. Companion reconciliation searches existing records and recoverable prior evidence before performing a fresh exact-version review.
- `engine/skills/` procedures do not count as user-facing inventory.

## Sequential AWS curation progress

The current high-throughput reconciliation pass preserves the registered AWS pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546` and has now completed three specialized families at the current standard:

- **Database skills:** 11/11 companion-complete. `exporting-rds-to-s3`, `rds-db2`, `rds-oss`, and `creating-amazon-aurora-db-cluster-with-instances` are rejected unchanged where their mutation procedures lack a sufficient explicit consent boundary; other records retain their actual verified/rejected dispositions.
- **EC2 skills:** 3/3 companion-complete. `creating-ec2-image-builder-pipeline` is rejected unchanged for compulsory resource mutation without a pre-mutation authorization gate; the EC2 launch and instance-profile packages are verified because they establish meaningful user confirmation boundaries.
- **Migration and modernization:** 2/2 companion-complete. `aws-transform` is rejected unchanged because it mandates an unconditional `atx update` without user consent; `dms-schema-conversion` is verified because project creation, action selection, live-target application, and overwrite behavior are explicitly user-gated.

All exact-version records retain package tree identity, source revision/freshness, dependencies, authority, portability, controlled taxonomy tags, decisive static state, and behavioral status. Behavioral validation remains `not-run` unless representative external evidence actually exists.

## Source lifecycle

The repository distinguishes:

**discovery surface → candidate issue/source → source-vetting → admitted corpus/reference/tracked source → individual exact-version review → user-fit decision**

New third-party candidates use issue-first intake. The connected Creator Technical Resource Catalog is discovery intelligence only; its rows, scores, verification labels, creator attributions, and recommendations are not `skillz` provenance or individual quality evidence.

## Quality model

- Source identity and individual skill quality are separate.
- Every governed user-facing skill must have truthful provenance and applicable exact-version review evidence before being described as companion-complete.
- `verified` means structured semantic review passed for the exact bound material.
- `validated` means representative external scenario/adversarial evidence was also recorded.
- `unverified` and legacy `trusted-baseline` are not unchanged-reuse states.
- `stale`, `rejected`, and `retired` are excluded from normal unchanged selection.
- Fingerprints identify reviewed material. They are provenance/bookkeeping evidence, not executable proof.
- Static source completion requires an exact eligible denominator and a decisive current state for every in-scope skill.

Interpret candidates in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue AWS Agent Toolkit sequential reconciliation through the remaining **32** gaps, beginning with the networking/content-delivery family, while checking live companions before every unit.
2. Complete Microsoft Skills.
3. Complete Microsoft Azure Skills.
4. Continue remaining admitted creator/registered-source curation to the same mandatory standard.
5. Continue governed discovery/source-vetting in parallel when evidence supports useful candidates.
6. Keep README, governance, category navigation, source registry, catalog snapshots, and public counts aligned after each material batch.

The current living work surface is `CURATION_QUEUE.md` plus provenance audit issue #66. Closed historical Wayfinder/issues/PRs remain evidence, not active execution plans.
