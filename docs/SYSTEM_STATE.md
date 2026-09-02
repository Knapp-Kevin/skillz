# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-01 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 249 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 77 / 189 |
| **Microsoft Skills current-standard gaps** | 112 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 18 / 40 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **43/43 provenance-complete** with structured semantic review evidence.
- AWS Agent Toolkit: exact denominator **72**, **72/72 current-standard companion-complete** at pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Microsoft Skills: exact denominator **189**, **77/189 companion-complete**, **112 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **18/40** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Active Microsoft frontier

Python is active and now runs source-order through `azure-eventgrid-py`.

Latest tranche, all with `validation_status: not-run`:

- `azure-cosmos-py` — **rejected unchanged, 9/20**. Complete-package review includes partitioning/query references and a setup CLI. Useful Cosmos design and SDK guidance is outweighed for unchanged adoption by unguarded database/container provisioning, throughput/index changes, durable CRUD/delete, transactional financial mutation, billable resource creation, and an account-key fallback in the CLI. Adaptation requires explicit environment/data/destructive/financial/cost authority, recovery/retention, least-privilege RBAC, and pinned dependencies.
- `azure-data-tables-py` — **rejected unchanged, 12/20**. Useful Entra-first table/entity patterns, partition-aware queries, transactions, async use, and client lifecycle, but table/entity creation/update/delete lacks distinct account/table/data-scope, destructive, retention, rollback, and cost authorization boundaries.
- `azure-eventgrid-py` — **rejected unchanged, 13/20**. Useful CloudEvents/EventGridEvent, batching, namespace-topic, and Entra-first guidance, but event publication can disclose payloads and trigger downstream external effects without explicit topic/audience, disclosure, publication, downstream-impact, or budget authority. The async credential lifecycle also contradicts the package's cleanup rule.

The next source-ordered package is `azure-eventhub-py`. It contains references and scripts and should receive complete-package review before disposition.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in coherent source-ordered batches, with Python at **18/40**.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
4. Continue governed discovery/source-vetting and omission recovery.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.