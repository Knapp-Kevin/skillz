# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills, **43/43** provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **308** persisted exact-version third-party verification companions.
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
- Current-standard companions: **136/189**.
- Remaining gaps: **53**.
- Direct `.NET`: **29/29** complete.
- Direct Java: **26/26** complete.
- Direct Python: **40/40** complete.
- Direct Rust: **9/9** complete.
- Direct TypeScript: **25/25** complete.

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
- `azure-search-documents-ts` — **rejected unchanged, 9/20**. Azure AI Search index configuration, document indexing, full-text/vector/hybrid/semantic search, filtering/facets, suggestions, integrated vectorization, captions/answers, and query tuning are useful prior art, but persistent index/document mutation, content/query transfer, admin-key handling, destructive document actions, and returned-content/debug output lack mandatory service/index, data-owner/classification, mutation/deletion, production, credential-custody, external-disclosure, retention/recovery, and sensitive-output authorization.
- `azure-servicebus-ts` — **rejected unchanged, 8/20**. Service Bus queues/topics/subscriptions, batching, sessions/session state, scheduling, receive modes, settlement, dead-letter handling, retries, lock renewal, graceful shutdown, idempotency, and poison-message patterns are useful prior art, but external message publication, settlement/deletion, dead-letter/defer/abandon actions, scheduled delivery, durable session-state mutation, DLQ reprocessing, downstream business handlers, and raw message/error logging lack mandatory destination/resource, payload/data-owner, per-action/downstream-effect, destructive-action, production, retention/recovery, budget, and sensitive-output authorization.
- `azure-storage-blob-ts` — **rejected unchanged, 6/20**. Blob Storage clients, container/blob CRUD, streaming, staged block uploads, browser uploads, copy operations, metadata/headers, SAS mechanics, progress/range downloads, and abort handling are useful prior art, but persistent storage mutation/deletion, local/browser data upload, downloaded-content materialization, account-key/connection-string/SAS credential paths, broad delegated SAS permissions, and printed credential-bearing SAS URLs lack mandatory storage-resource, data-owner/classification, per-action/destructive-action, disclosure, retention/recovery, production, and cost authorization.
- `azure-storage-file-share-ts` — **rejected unchanged, 6/20**. Azure Files clients, share/directory/file CRUD, quota management, local-file/buffer/stream uploads, downloads, copy operations, metadata/headers, range operations, snapshots, SAS generation, error handling, and authentication choices are useful prior art, but persistent share/file mutation and deletion, local-data upload, downloaded-content materialization, quota/range mutation, snapshot deletion, account-key/connection-string/SAS credential paths, and broad 24-hour read/create/write/delete/list share SAS lack mandatory resource, data-owner/classification, per-action/destructive-action, disclosure, retention/recovery, production, and cost authorization.
- `azure-storage-queue-ts` — **rejected unchanged, 6/20**. Queue Storage clients, queue CRUD/metadata, send/receive/peek/update/delete/clear operations, visibility timeout handling, poison-message routing, worker/batch patterns, encoding, SAS generation, error handling, and authentication choices are useful prior art, but persistent queue/message mutation, arbitrary payload publication, message-content/pop-receipt output, downstream handler execution, poison-payload transfer, destructive clear/delete operations, account-key/connection-string/SAS credential paths, and broad delegated queue/account SAS lack mandatory resource, payload/data-owner/classification, downstream-effect, per-action/destructive-action, disclosure, retention/recovery, production, and cost authorization.
- `azure-web-pubsub-ts` — **rejected unchanged, 6/20**. Web PubSub service/client setup, Entra-first authentication, client-token generation, targeted/broadcast/group messaging, group and connection lifecycle, permission management, reconnect handling, Express event handlers, and negotiate endpoints are useful prior art, but credential-bearing access-URL output, external messaging, group-membership mutation, forced disconnects, permission grants/revocations, client events, and raw user/message logging lack mandatory hub/resource, recipient/audience, message/data-owner/classification, identity/access, per-action/disconnect, downstream-effect, disclosure, production, and credential-custody authorization.
- `frontend-ui-dark-ts` — **verified, 15/20**. The complete package provides differentiated local React/Vite/Tailwind dark-UI construction guidance with design tokens, reusable components, responsive/mobile shells, touch-target guidance, routing, glass effects, Framer Motion patterns, three supporting Markdown references, four Segoe UI TTF assets, and two Foundry logo PNG assets. Ordinary authority is local project creation and npm package installation rather than consequential infrastructure/external-state operation. Limitations are explicit: examples target the reviewed React 18/React Router 6/Framer Motion 11/Tailwind 3/Vite 5 generation, some copied component patterns need accessibility hardening such as modal focus management and reduced-motion behavior, and bundled font/logo assets have medium portability and must retain applicable upstream terms. No current hard fail remains for the exact pinned package.
- `m365-agents-ts` — **rejected unchanged, 13/20**. M365 Agents SDK routing, Express hosting, streaming, sensitivity labeling, invoke handling, Copilot Studio clients/WebChat, API freshness checks, and secret-hygiene guidance are useful prior art, but ordinary user messaging, generated-content streaming, invoke acknowledgement, remote Copilot Studio conversations/questions, WebChat connections, Azure OpenAI data transfer, and tenant/client secret or bearer-token use lack mandatory tenant/environment, audience, message/data-owner/classification, identity/access, model-data-transfer, production, per-action communication, and credential-custody authorization.
- `react-flow-node-ts` — **verified, 15/20**. The complete package provides focused local React Flow custom-node prior art with TypeScript typing, handles, resizing, selector-based Zustand integration, registration/menu steps, and two reusable templates. Authority is local source mutation. Portability is medium because the templates assume project-local aliases, useAppStore/updateNode/canvasMode semantics, Frontier CSS custom properties, and a source-specific directory layout; those assumptions must be mapped but do not create a consequential external-state hard fail.
- `zustand-store-ts` — **verified, 16/20**. The complete package provides focused local Zustand prior art for typed state/action separation, subscribeWithSelector, individual selectors, subscriptions outside React, loading/error/reset state, and immutable add/remove operations. Authority is local source and in-memory application-state mutation. The async loadItems body is intentionally a placeholder, not an external request. Portability is medium because the integration path is source-specific and the categorical subscribeWithSelector rule is intentionally opinionated.

All twenty-five retain `validation_status: not-run`. Exact tree/blob identities and skill-specific freshness are retained in individual companion records.

Non-direct Microsoft plugin frontier:

- `airunway-aks-setup` — **rejected unchanged, 15/20**. Exact package tree `72ec58c0a7c574dc71e14c63feb3d2aa529849ac`, `SKILL.md` blob `26bbd92815116826696fb6380d37446a285496b9`, and skill-specific freshness revision `951d18d43210f0d93a931ae5d5c2a774f63d5faf` from 2026-04-21. The package contains strong staged AKS onboarding mechanics, explicit current-context reporting, prerequisite stop conditions, confirmation before install/deployment, GPU-cost awareness, model-choice confirmation, secure no-echo Hugging Face token handling, provider selection, readiness checks, and rollback guidance. Unchanged adoption is rejected because rollback explicitly instructs deletion of ModelDeployment resources and Hugging Face token secrets plus provider/controller undeploy without requiring a fresh destructive-action authorization boundary. The main confirmation rule covers install/deployment actions, not rollback/delete/undeploy. Preserve the setup, secret-custody, sizing, provider, readiness, and rollback mechanics for adaptation/reference use with an added target/resource and destructive-action approval gate. Behavioral validation is `not-run`.

- `appinsights-instrumentation` — **rejected unchanged, 12/20**. Exact package tree `8f6b0c9b5af9ab5bbd69d25d58071c9034221eb0`, `SKILL.md` blob `ca55c310862cb95b5ebcc1f10a070f312718d1cb`, and skill-specific freshness revision `2d821920c717bcdd5ee4e287a41205c07e43cb0a` from 2026-05-05. The complete package includes `LICENSE.txt`, Bicep and PowerShell/Azure CLI examples, five platform/reference guides, and four SDK quick references. Application Insights/OpenTelemetry selection, SDK initialization, tracing, resource-topology, secret-reference, and KQL mechanics are useful prior art. Unchanged adoption is rejected because the package directly instructs creation of Log Analytics and Application Insights resources, App Service/Container App/Function App configuration mutation, application/IaC changes, telemetry export, and deployment-affecting operations without mandatory target/resource, production-change, cost, telemetry-data/disclosure, or deployment authorization. The Container Apps reference also retrieves the workspace primary shared key into a shell variable and performs secret/configuration mutation without a credential-custody authorization boundary. Behavioral validation is `not-run`.

- `azure-ai` — **rejected unchanged, 10/20**. Exact package tree `8a168336305c56e0eea0d89aced7d8a0001de3b5`, `SKILL.md` blob `6cce5b319f57f98f81772e4c8627c573d89e8571`, and skill-specific freshness revision `951d18d43210f0d93a931ae5d5c2a774f63d5faf` from 2026-04-21. The package includes `references/auth-best-practices.md` and 15 SDK quick references spanning Azure AI Search, OpenAI-related access, Document Intelligence, Vision, Translation, Transcription, and Content Safety. It has useful managed-identity/RBAC guidance and condensed service-selection/SDK mechanics, but unchanged adoption is rejected because bundled references direct persistent Azure AI Search index/document mutation and external processing of audio, documents, text, images, and other potentially sensitive content without mandatory data-owner/classification, disclosure/model-transfer, target-resource, mutation, production, retention, cost, or credential-custody authorization. The transcription quick reference also consumes a subscription key string from an environment variable and sends files/content URLs to the external service. Behavioral validation is `not-run`.

- `azure-aigateway` — **rejected unchanged, 8/20**. Exact package tree `fb881f68bdc6d638438b46b04ab6d81f91e985ba`, `SKILL.md` blob `a8df9f45fae25501acf7fee988047f808d191fa5`, and skill-specific freshness revision `951d18d43210f0d93a931ae5d5c2a774f63d5faf` from 2026-04-21. The complete package includes authentication guidance, configuration patterns, policy and troubleshooting references, plus four SDK quick references. It preserves useful managed-identity/RBAC, token/rate-control, semantic-cache, content-safety, load-balancing, MCP, multi-tenant metering, and troubleshooting prior art. Unchanged adoption is rejected because normal flows enable APIM identity, create RBAC role assignments and APIM backends, import APIs, modify routing and security policies, expose APIs as MCP-compatible agent tools, test live AI endpoints, and emit usage metrics without mandatory target/resource, identity/access, production-change, security-control, downstream-effect, data/disclosure, or cost authorization. `SKILL.md` also instructs listing APIM subscription keys, which can expose live credential material into tool/conversational output. Behavioral validation is `not-run`.

**Next:** continue Microsoft Skills registered-pin source order with `.github/plugins/azure-skills/skills/azure-cloud-migrate`.

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
**Microsoft Skills:** **136/189**, **53 gaps**. Direct `.NET`, Java, Python, Rust, and TypeScript slices are complete; TypeScript is **25/25**.  
**Next:** continue Microsoft Skills source order with `.github/plugins/azure-skills/skills/azure-cloud-migrate`.