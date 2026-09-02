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
| **Persisted third-party review companions** | 263 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 91 / 189 |
| **Microsoft Skills current-standard gaps** | 98 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 32 / 40 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **43/43 provenance-complete** with structured semantic review evidence.
- AWS Agent Toolkit: exact denominator **72**, **72/72 current-standard companion-complete** at pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Microsoft Skills: exact denominator **189**, **91/189 companion-complete**, **98 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **32/40** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Active Microsoft frontier

Python is active and now runs source-order through `azure-servicebus-py`.

Latest tranche, with `validation_status: not-run`:

- `azure-search-documents-py` — **rejected unchanged, 10/20**. Exact complete-package review covers three references and two setup scripts. Useful Entra-first search, vector/semantic ranking, agentic retrieval, batching, and lifecycle patterns remain prior art. Unchanged adoption creates/deletes indexes and knowledge resources, mutates indexed documents/data-source configuration, and can invoke Azure OpenAI-backed vectorization and answer synthesis without explicit resource/data scope, disclosure, destructive-action, rollback, service-impact, or budget authority.
- `azure-servicebus-py` — **rejected unchanged, 9/20**. Exact complete-package review covers two substantial references and an administrative setup CLI. Useful Entra-first messaging, retry, batching, sessions, DLQ, transaction, and orchestration patterns remain prior art. Unchanged adoption publishes messages, destructively settles/reprocesses/discards queued data, cancels scheduled sends, mutates session state, and creates/deletes Service Bus entities without explicit entity/downstream, data-disclosure, settlement/destructive-action, rollback, or budget authority; the CLI also permits a connection-string credential path.

The exact pinned Python denominator is **40 direct skill directories**; the source-order frontier after this tranche is `azure-speech-to-text-rest-py`.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in coherent source-ordered batches, with Python at **32/40**.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
4. Continue governed discovery/source-vetting and omission recovery.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.