# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-02 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 268 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 96 / 189 |
| **Microsoft Skills current-standard gaps** | 93 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 37 / 40 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **43/43 provenance-complete** with structured semantic review evidence.
- AWS Agent Toolkit: exact denominator **72**, **72/72 current-standard companion-complete** at pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Microsoft Skills: exact denominator **189**, **96/189 companion-complete**, **93 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **37/40** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Active Microsoft frontier

Python is active and now runs source-order through `azure-storage-queue-py`.

Latest tranche, with `validation_status: not-run`:

- `azure-storage-blob-py` — **rejected unchanged, 10/20**. Useful Entra-first auth, upload/download, listing, performance, metadata and user-delegation SAS patterns remain prior art. Unchanged use creates persistent containers, overwrites/deletes blob data including snapshots, downloads data, mutates metadata/headers, and creates delegated SAS access without explicit storage/data scope, destructive-action, retention/recovery, disclosure, delegated-access custody, or budget authority.
- `azure-storage-file-datalake-py` — **rejected unchanged, 7/20**. Useful hierarchical storage and append/flush patterns remain prior art. Unchanged use creates/deletes file systems and directories, mutates durable files and metadata, and changes owner/permission ACLs recursively without explicit resource/data scope, destructive-action, access-control, retention/recovery, disclosure, service-impact, or budget authority.
- `azure-storage-file-share-py` — **rejected unchanged, 10/20**. Useful Entra-first, streaming/range, snapshot, and quota patterns remain prior art. Unchanged use creates/deletes shares/directories/files, uploads/copies/downloads data, and creates billable snapshots without explicit resource/data scope, destructive-action, copy-source trust, retention/recovery, disclosure, service-impact, or budget authority.
- `azure-storage-queue-py` — **rejected unchanged, 9/20**. Useful visibility-timeout, poison-message, TTL, peek, update and async patterns remain prior art. Unchanged use creates/deletes queues, publishes messages, prints message content, deletes/updates messages, clears whole queues, and mutates metadata without explicit scope, publication/downstream-effect, destructive-settlement, disclosure, retention/recovery, or budget authority. Its async example also omits closing the async credential despite the package's stated cleanup rule.

All four are one-file packages and bind freshness to Microsoft revision `df52e9a69b78c2759553efafe2f937fc53c1cbd1` from 2026-05-18.

The exact pinned Python denominator remains **40 direct skill directories**; the source-order frontier after this tranche is `fastapi-router-py`.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in coherent source-ordered batches, with Python at **37/40**.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
4. Continue governed discovery/source-vetting and omission recovery.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.