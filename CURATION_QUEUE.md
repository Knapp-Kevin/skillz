# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **286** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.

Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora. Recover compatible prior evidence before fresh re-review.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use `docs/candidate-intake.md`. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit. First-party is **43/43** complete. Enforcement is documentary/evidentiary through external-agent curation, never repository-owned scripts, CI, scanners, or runtime.

## Admitted-source curation

### AWS Agent Toolkit — CURRENT-STANDARD COMPLETE

- Pin: `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`
- Denominator: **72**
- Current-standard companion completeness: **72/72**
- Gaps: **0**

### Microsoft Skills — ACTIVE FRONTIER

- Pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`
- Exact eligible denominator: **189** independently front-mattered skill entry points.
- Current-standard companions: **114/189**.
- Remaining gaps: **75**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **40/40** complete.
- Direct Rust: **9/9** complete.
- Direct TypeScript: **7/25** complete.

The pinned TypeScript skill tree contains exactly **25** direct packages. Its upstream plugin README says 24 because it omits `applicationinsights-web-ts`, which is nevertheless a first-class package in the registered-pin tree. The tree controls the denominator. `applicationinsights-web-ts` was already current-standard companion-complete; the first genuine gap was therefore `azure-ai-contentsafety-ts`.

Current TypeScript decisive states:

- `applicationinsights-web-ts` — **rejected unchanged, 16/20**. Browser telemetry can leave the client before mandatory user-consent/data-governance authorization; retain telemetry/privacy mechanics for adaptation.
- `azure-ai-contentsafety-ts` — **rejected unchanged, 11/20**. Text/image moderation can disclose sensitive content externally; remote-image analysis lacks a trusted-source boundary; blocklist mutation/deletion lacks action-specific authority; recommended moderation logging lacks minimization/redaction/retention controls.
- `azure-ai-document-intelligence-ts` — **rejected unchanged, 11/20**. Document analysis can disclose identity, health-insurance, tax, banking, invoice, receipt, address, birth-date, document-number, and other sensitive content externally; remote-document analysis lacks a trusted-source boundary; custom training uses a credential-bearing storage SAS URL without a secure external credential path; and model/classifier build, compose, and delete operations lack action-specific training, destructive-action, rollback, and budget authority.
- `azure-ai-projects-ts` — **rejected unchanged, 6/20**. Foundry project/agent, connection, dataset, index, evaluation, OpenAI-client, and tool-wiring mechanics remain useful prior art, but unchanged use creates/deletes persistent resources, transmits potentially sensitive evaluation/dataset content, invokes external tools/services, and incurs service costs without adequate action-specific authority. Its bundled connections reference retrieves credentials and explicitly prints an API key, which is a direct secret-custody hard fail.
- `azure-ai-translation-ts` — **rejected unchanged, 10/20**. Text/document translation, transliteration, detection, status, and pagination mechanics remain useful prior art, but unchanged use transmits arbitrary text/documents externally without mandatory data-transfer/privacy authority. Batch document translation creates credential-bearing source/target SAS URLs, starts a billable service-side operation, and writes translated content to persistent target storage without sufficient credential-custody, storage-scope, write/downstream-effect, recovery/overwrite, or budget authority.
- `azure-ai-voicelive-ts` — **rejected unchanged, 6/20**. Real-time voice/audio, browser microphone capture/playback, VAD, transcription, session/event handling, and function-calling mechanics remain useful prior art. Unchanged use captures and transmits live microphone audio, transcripts, conversation content, locations, and tool arguments/results without mandatory subject consent, data-classification, destination/region, minimization, retention/redaction, or output-disclosure authority. The bundled function-calling reference permits model-triggered consequential external actions such as appointment booking without a real per-action authorization gate; API-key and personal/custom voice paths also need stronger credential and identity-sensitive boundaries.
- `azure-appconfiguration-ts` — **rejected unchanged, 7/20**. App Configuration CRUD, optimistic concurrency, provider loading/refresh, feature flags, labels, snapshots, and Key Vault-reference mechanics remain useful prior art. Unchanged use can create/update/delete configuration, lock/unlock settings, alter feature targeting, and archive/recover snapshots without mandatory resource/environment, per-change, rollout, rollback/recovery, or budget/service authorization. A credential-bearing connection string is presented as a normal path; Key Vault references resolve secrets into application memory; configuration values are printed; and user email addresses appear in targeting examples without required secure credential custody, secret/output redaction, or PII minimization boundaries.

All seven retain `validation_status: not-run`. Exact tree/blob identities and skill-specific freshness are retained in individual companion records.

**Next:** continue the registered-pin TypeScript tree source-order after `azure-appconfiguration-ts` in coherent batches.

### Microsoft Azure Skills — QUEUED AFTER MICROSOFT SKILLS

Pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`. Establish its exact eligible denominator before completion claims and distinguish planning/read-only guidance from deployment, RBAC, cost, identity, and other higher-authority operations.

### Other admitted/tracked sources

- Cole Medin Skills: denominator 33, selective review ongoing.
- David Ondrej Skills: denominator discrepancy still requires reconciliation.
- OpenClaw Agent Skills: denominator 8, selective review exists.
- Archie Indian OpenClaw Superpowers: denominator 56, selective review exists.
- Sabrina Ramonov historical material: canonical source identity/pin/license must be recovered before further work.

## Discovery/source-vetting frontier

Open candidate issues remain temporary evaluation workspaces. Current open bounded candidate work includes DBOS durable-workflow skills (#63) and first-party `session-continuity` derivation (#73). Do not close them merely to improve issue statistics; close them when evidence supports a decisive admission/rejection result.

Discovery surfaces include Hugging Face Skills, GitHub Awesome Copilot, Agent Skills Specification, creator/source leads, and the connected Creator Technical Resource Catalog. Popularity and reputation are omission/context signals only.

## Working rules

1. Finish admitted sources in coherent source-ordered batches.
2. Do not lower individual evidence quality for throughput.
3. Check both companion paths before every unit.
4. Search compatible prior evidence before re-reviewing.
5. Preserve rejected/retired material and reasons.
6. Keep discovery separate from admission.
7. Keep `skillz` passive. No repository-owned runtime, scripts, tests, CI, scheduler, monitor, crawler, installer, synchronizer, preflight, generator, background service, vector database, or autonomous observer.
8. Reconcile README, System State, this ledger, `INDEX.md`, and `index.json` atomically after material batches.
9. Keep issues and PRs in an explicit active, blocked, superseded, or completed state.

## Current posture

**Core:** complete and passive.  
**First-party:** 43/43 provenance-complete.  
**AWS:** 72/72 current-standard companion-complete.  
**Microsoft Skills:** **114/189**, **75 gaps**. Direct `.NET`, Java, Python, and Rust slices are complete; TypeScript is active at **7/25**.  
**Next:** continue after `azure-appconfiguration-ts` in the registered-pin TypeScript tree.