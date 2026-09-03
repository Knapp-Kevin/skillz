# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **294** persisted exact-version third-party verification companions.
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
- Current-standard companions: **122/189**.
- Remaining gaps: **67**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **40/40** complete.
- Direct Rust: **9/9** complete.
- Direct TypeScript: **15/25** complete.

The pinned TypeScript skill tree contains exactly **25** direct packages. Its upstream plugin README says 24 because it omits `applicationinsights-web-ts`, which is nevertheless a first-class package in the registered-pin tree. The tree controls the denominator.

Current TypeScript decisive states:

- `applicationinsights-web-ts` — **rejected unchanged, 16/20**. Browser telemetry can leave the client before mandatory user-consent/data-governance authorization; retain telemetry/privacy mechanics for adaptation.
- `azure-ai-contentsafety-ts` — **rejected unchanged, 11/20**. External moderation and persistent blocklist operations lack mandatory disclosure/privacy, trusted-source, logging-minimization, and action-specific mutation boundaries.
- `azure-ai-document-intelligence-ts` — **rejected unchanged, 11/20**. Sensitive-document transfer and custom-model lifecycle examples lack required data, credential-custody, destructive-action, recovery, and budget authority.
- `azure-ai-projects-ts` — **rejected unchanged, 6/20**. Persistent Foundry resources, external tools, evaluation data, cost-bearing operations, and explicit API-key output violate current authority and secret-custody requirements.
- `azure-ai-translation-ts` — **rejected unchanged, 10/20**. Arbitrary text/document transfer plus SAS-backed batch translation lacks sufficient privacy, credential, persistent-write, recovery, and budget authority.
- `azure-ai-voicelive-ts` — **rejected unchanged, 6/20**. Live audio/transcript capture and model-triggered external actions lack mandatory consent, data, identity-sensitive, and per-action authorization boundaries.
- `azure-appconfiguration-ts` — **rejected unchanged, 7/20**. Production configuration, feature targeting, snapshots, secret resolution, and PII examples lack adequate change, credential, redaction, rollout, and recovery authority.
- `azure-cosmos-ts` — **rejected unchanged, 9/20**. Durable database/container/item mutation and bulk destructive operations lack environment/resource, data-scope, recovery, throughput, and destructive-action authority.
- `azure-eventhub-ts` — **rejected unchanged, 8/20**. External event publication and persistent checkpoint state lack payload, destination, downstream-effect, storage, retention, redaction, and budget authority.
- `azure-identity-ts` — **rejected unchanged, 6/20**. Strong managed/workload identity and credential-selection prior art is retained, but raw bearer-token logging, verbose identity diagnostics, secret/password credential paths, broad developer-credential fallbacks, user-identity handling, and CORS/security-control mutation lack mandatory credential-custody, least-privilege tenant/resource/scope, sensitive-output, identity/access, and action-specific security-control authorization.
- `azure-keyvault-keys-ts` — **rejected unchanged, 5/20**. Key creation/import/rotation/deletion/purge, cryptographic operations, bundled secret lifecycle, raw secret output, bulk secret export, and local backup-file examples lack mandatory vault/resource, key-purpose, per-operation, destructive-action, recovery, secure-custody, disclosure, and production authorization.
- `azure-keyvault-secrets-ts` — **rejected unchanged, 5/20**. Secret set/get/list/delete/purge/recover/backup/restore, raw secret output, literal API-key/connection-string examples, bulk secret handling, key lifecycle, and cryptographic operations lack mandatory vault/resource, secret-purpose, data-owner, per-operation, destructive-action, recovery, secure-custody, disclosure, retention, production, and security-control authorization.
- `azure-microsoft-playwright-testing-ts` — **rejected unchanged, 10/20**. Cloud browser execution, external test targets, network exposure, Azure result/artifact publication, CI identity-token configuration, and billable worker scaling lack mandatory target/environment, test-data, external-side-effect, artifact publication/retention, network-exposure, cost, and production authorization boundaries.
- `azure-monitor-opentelemetry-ts` — **rejected unchanged, 9/20**. External telemetry/log export, broad auto-instrumentation, and user/tenant baggage propagation lack mandatory destination/region, data-classification, subject/data-transfer, minimization, retention/redaction, and disclosure authorization. The source's PII/secret warning and optional processors are useful but do not form an enforced authorization boundary.
- `azure-postgres-ts` — **rejected unchanged, 10/20**. PostgreSQL clients/pools, SSL, parameterized queries, transactions/rollback, typed queries, Entra token refresh, error handling, and pool sizing are useful prior art, but ordinary database queries and durable mutations, token/password credential use, credential-bearing connection strings, and database error output lack mandatory target/database, data-owner, query/mutation, production, credential-custody, sensitive-output, retention/recovery, and consequential-operation authorization.

All fifteen retain `validation_status: not-run`. Exact tree/blob identities and skill-specific freshness are retained in individual companion records.

**Next:** continue the registered-pin TypeScript tree source order after `azure-postgres-ts`, beginning with `azure-search-documents-ts`.

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
**Microsoft Skills:** **122/189**, **67 gaps**. Direct `.NET`, Java, Python, and Rust slices are complete; TypeScript is active at **15/25**.  
**Next:** continue after `azure-postgres-ts` in the registered-pin TypeScript tree, beginning with `azure-search-documents-ts`.