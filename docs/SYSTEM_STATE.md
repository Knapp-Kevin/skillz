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
| **Persisted third-party review companions** | 293 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 121 / 189 |
| **Microsoft Skills current-standard gaps** | 68 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 40 / 40 |
| **Microsoft Rust direct-package companions** | 9 / 9 |
| **Microsoft TypeScript direct-package companions** | 14 / 25 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **43/43 provenance-complete** with structured semantic review evidence.
- AWS Agent Toolkit: exact denominator **72**, **72/72 current-standard companion-complete** at pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Microsoft Skills: exact denominator **189**, **121/189 companion-complete**, **68 gaps** at pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Microsoft direct `.NET`: **29/29** complete.
- Microsoft direct Java: **26/26** complete.
- Microsoft direct Python: **40/40** complete.
- Microsoft direct Rust: **9/9** complete.
- Microsoft direct TypeScript: **14/25** complete.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Active Microsoft frontier

The registered-pin TypeScript tree contains exactly **25** first-class packages. Its upstream plugin README says 24 because it omits `applicationinsights-web-ts`, which nevertheless exists as a separate first-class package at the same pin. Tree truth controls the denominator.

Current companion-complete TypeScript packages are:

1. `applicationinsights-web-ts` — rejected unchanged, 16/20.
2. `azure-ai-contentsafety-ts` — rejected unchanged, 11/20.
3. `azure-ai-document-intelligence-ts` — rejected unchanged, 11/20.
4. `azure-ai-projects-ts` — rejected unchanged, 6/20.
5. `azure-ai-translation-ts` — rejected unchanged, 10/20.
6. `azure-ai-voicelive-ts` — rejected unchanged, 6/20.
7. `azure-appconfiguration-ts` — rejected unchanged, 7/20.
8. `azure-cosmos-ts` — rejected unchanged, 9/20.
9. `azure-eventhub-ts` — rejected unchanged, 8/20.
10. `azure-identity-ts` — rejected unchanged, 6/20.
11. `azure-keyvault-keys-ts` — rejected unchanged, 5/20.
12. `azure-keyvault-secrets-ts` — rejected unchanged, 5/20.
13. `azure-microsoft-playwright-testing-ts` — rejected unchanged, 10/20.
14. `azure-monitor-opentelemetry-ts` — rejected unchanged, 9/20.

`azure-monitor-opentelemetry-ts` is bound to single-file package tree `745333bd43aa40a5a5639af738ade6ae35426c08` and `SKILL.md` blob `538f028b72746103fa2314ba625acad23c934fce`. Skill-specific freshness is anchored to Microsoft revision `ee33ce9d2b4372b0cfe58375bebbf0bd989e3ac9` from 2026-04-22. Its Azure Monitor initialization, deprecated-package migration, custom spans and metrics, logging integration, auto-instrumentation, sampling, processors, baggage/context propagation, correlation, role metadata, and graceful-shutdown mechanics remain useful prior art. Unchanged adoption fails because normal flows export telemetry and logs to Azure Monitor, auto-instrumentation can collect HTTP, Azure SDK, database, Redis, exception, request, and response metadata, and examples propagate `user.id` and `tenant.id` across service boundaries without mandatory destination/region, data-classification, subject/data-transfer, minimization, retention/redaction, or disclosure authorization. The source's instruction not to log PII or secrets is valuable guidance but is not an enforced authorization boundary. Behavioral validation is `not-run`.

Microsoft Skills remains active with **68** gaps. Continue TypeScript source order after `azure-monitor-opentelemetry-ts`, beginning with `azure-postgres-ts`, while preserving the complete `.NET`, Java, Python, and Rust slices.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in coherent source-ordered batches; direct `.NET`, Java, Python, and Rust are complete, TypeScript is active at 14/25.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
4. Continue governed discovery/source-vetting and omission recovery.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.