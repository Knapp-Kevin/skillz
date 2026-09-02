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
| **Persisted third-party review companions** | 280 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 108 / 189 |
| **Microsoft Skills current-standard gaps** | 81 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 40 / 40 |
| **Microsoft Rust direct-package companions** | 9 / 9 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **43/43 provenance-complete** with structured semantic review evidence.
- AWS Agent Toolkit: exact denominator **72**, **72/72 current-standard companion-complete** at pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Microsoft Skills: exact denominator **189**, **108/189 companion-complete**, **81 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Active Microsoft frontier

The direct Rust slice is complete at **9/9** after recomputing the registered-pin tree. The pinned `.github/plugins/azure-sdk-rust/skills/` directory contains nine first-class packages even though its upstream README says seven; `azure-servicebus-rust` and `azure-storage-queue-rust` are omitted from that README count.

All nine exact packages are single-file `SKILL.md` packages and are **rejected unchanged** with `validation_status: not-run`:

- `azure-cosmos-rust`: durable item create/replace/patch/delete without resource/data, destructive-action, recovery, or cost authority.
- `azure-eventhub-rust`: external event publication and payload output without destination/audience, disclosure, downstream-impact, or budget authority.
- `azure-identity-rust`: retrieves and prints a secret value and demonstrates client-secret handling without adequate tenant/scope, redaction, or credential-custody boundaries.
- `azure-keyvault-certificates-rust`: certificate lifecycle and signing operations without certificate, cryptographic-use, destructive-action, or production authorization.
- `azure-keyvault-keys-rust`: key create/delete and wrap/unwrap operations without key-purpose, cryptographic-operation, destructive-action, or recovery authorization.
- `azure-keyvault-secrets-rust`: literal/retrieved secret values, secret output, mutation, and deletion without secret-custody, redaction, or destructive-action authorization.
- `azure-servicebus-rust`: pre-production SDK plus message publication, content output, and permanent settlement without communication/disclosure/destructive-settlement authority.
- `azure-storage-blob-rust`: durable upload/delete/container mutation and content download without resource/data, destructive-action, recovery/retention, disclosure, or budget authority.
- `azure-storage-queue-rust`: message publication, content output, and permanent deletion without destination/downstream, disclosure, or destructive-settlement authority.

The exact package tree/blob fingerprints and skill-specific freshness revisions live in the companion records. Static rejection preserves useful SDK mechanics as adaptation/extraction evidence and does not imply behavioral validation.

Microsoft Skills remains active with **81** gaps after completed direct `.NET`, Java, Python, and Rust slices. Select the next tranche from live registered-pin companion gaps, not historical structure artifacts.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in coherent source-ordered batches; direct `.NET`, Java, Python, and Rust are complete.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
4. Continue governed discovery/source-vetting and omission recovery.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.