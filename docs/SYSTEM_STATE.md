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
| **Persisted third-party review companions** | 288 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 116 / 189 |
| **Microsoft Skills current-standard gaps** | 73 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 40 / 40 |
| **Microsoft Rust direct-package companions** | 9 / 9 |
| **Microsoft TypeScript direct-package companions** | 9 / 25 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **43/43 provenance-complete** with structured semantic review evidence.
- AWS Agent Toolkit: exact denominator **72**, **72/72 current-standard companion-complete** at pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Microsoft Skills: exact denominator **189**, **116/189 companion-complete**, **73 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **9/25** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Active Microsoft frontier

The registered-pin TypeScript tree contains exactly **25** first-class packages. Its upstream plugin README says 24 because it omits `applicationinsights-web-ts`, which nevertheless exists as a separate first-class package at the same pin. Tree truth controls the denominator.

`applicationinsights-web-ts` was already current-standard companion-complete. `azure-ai-contentsafety-ts` is **rejected unchanged, 11/20**, with `validation_status: not-run`, because its text/image moderation and persistent blocklist operations lack mandatory disclosure/privacy, trusted-source, logging-minimization, and action-specific mutation boundaries.

`azure-ai-document-intelligence-ts` is **rejected unchanged, 11/20**, with `validation_status: not-run`. Its prebuilt document extraction, layout/table analysis, batching, error handling, and custom-model mechanics remain useful prior art, but unchanged examples transmit identity, health-insurance, tax, banking, invoice, receipt, address, birth-date, document-number, and other potentially sensitive document data to Azure without mandatory subject/data authority, destination/region, minimization, retention/redaction, or output-disclosure controls. Remote-document analysis lacks an explicit trusted-source boundary; custom model training uses a credential-bearing storage SAS URL without a secure external credential path; and build/compose/delete operations mutate persistent billable service state without action-specific model, destructive-action, rollback, or budget authority.

`azure-ai-projects-ts` is **rejected unchanged, 6/20**, with `validation_status: not-run`. Its Foundry project client, agent/version, connection, deployment, dataset, index, evaluation, OpenAI-client, and tool-wiring mechanics remain useful prior art. Unchanged examples create and delete persistent service-side resources, transmit datasets and evaluation content, invoke external tools/services, expose location context to web search, and can incur inference/storage/evaluation costs without sufficient action-specific resource, publication, destructive-action, downstream-effect, data-transfer, rollback, or budget authorization. The bundled connections reference also retrieves project connection credentials and explicitly prints an API key, directly violating the secret-custody rule; evaluation examples print row-level content without mandatory minimization/redaction/retention controls.

`azure-ai-translation-ts` is **rejected unchanged, 10/20**, with `validation_status: not-run`. Its text translation, transliteration, language detection, single-document translation, batch document translation, status/pagination, and Azure identity mechanics remain useful prior art. Unchanged examples transmit arbitrary text and document content to Azure without mandatory data-classification, subject/data-transfer, destination/region, minimization, retention, or output-disclosure authority. Batch document translation generates credential-bearing source and target container SAS URLs and starts a billable operation that writes translated content to persistent target storage without sufficient credential-custody, storage-scope, write/downstream-effect, overwrite/recovery, or budget authorization. API-key authentication is also presented without a repository-enforced secure external credential path.

`azure-ai-voicelive-ts` is **rejected unchanged, 6/20**, with `validation_status: not-run`. Its real-time WebSocket voice session, browser microphone capture/playback, VAD, transcription, event handling, cleanup, and function-calling mechanics remain useful prior art. Unchanged examples capture and transmit live microphone audio, transcripts, conversation content, locations, and tool arguments/results to Azure or downstream services without mandatory subject consent, data classification, approved destination/region, minimization, retention/redaction, or output-disclosure controls. The bundled function-calling reference permits model-triggered external actions, including appointment booking and other API calls, without a real per-action authorization gate; a system prompt to confirm details is not action authorization. API-key authentication and personal/custom voice identifiers also require stronger credential and identity/biometric-sensitive boundaries than the unchanged package provides.

`azure-appconfiguration-ts` is **rejected unchanged, 7/20**, with `validation_status: not-run`. Its App Configuration CRUD, optimistic-concurrency, provider-loading, dynamic-refresh, feature-flag, labels, snapshots, and Key Vault reference mechanics remain useful prior art. Unchanged examples create/update/delete production configuration, lock/unlock settings, change feature targeting, and archive/recover persistent snapshots without mandatory resource/environment, per-change, rollout, rollback/recovery, or budget/service authorization. The package presents a credential-bearing connection string as a normal path, automatically resolves Key Vault secrets into application memory, prints configuration values, and uses user email addresses in targeting examples without mandatory secure credential custody, secret/output redaction, or PII minimization boundaries.

`azure-cosmos-ts` is **rejected unchanged, 9/20**, with `validation_status: not-run`. Its Entra-first client setup, partition design, point reads, parameterized queries, pagination, CRUD, bulk operations, indexing, diagnostics, retry handling, and client-lifecycle patterns remain useful prior art. Unchanged examples create databases and containers, create/replace/upsert/delete durable items, and perform bulk destructive operations without mandatory environment/resource, data-scope, mutation, destructive-action, recovery/retention, or budget/throughput authorization. The package's instruction to confirm destructive actions is not itself action authorization. Query and diagnostic patterns can also surface item content or operational detail without mandatory classification, minimization, or output-disclosure controls.

`azure-eventhub-ts` is **rejected unchanged, 8/20**, with `validation_status: not-run`. Its producer/consumer setup, batching, partition targeting, consumer groups, event positions, Blob checkpointing, load balancing, lag monitoring, graceful shutdown, and retry/error patterns remain useful prior art. Unchanged flows publish arbitrary event payloads to an external Event Hub, create/update persistent Blob checkpoint state, and may drive downstream processing without mandatory destination, payload-classification/disclosure, environment/resource, write, downstream-effect, retention/recovery, or budget/throughput authorization. The bundled checkpointing material also presents storage and Event Hubs connection strings as normal credential paths, while event-processing examples log event bodies, properties, and system properties without mandatory secret/PII minimization or redaction.

Microsoft Skills remains active with **73** gaps. Continue TypeScript source-order after `azure-eventhub-ts`, while preserving the complete `.NET`, Java, Python, and Rust slices.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in coherent source-ordered batches; direct `.NET`, Java, Python, and Rust are complete, TypeScript is active at 9/25.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
4. Continue governed discovery/source-vetting and omission recovery.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.