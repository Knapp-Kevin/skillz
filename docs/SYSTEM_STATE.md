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
| **Persisted third-party review companions** | 183 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS historical review** | 72 / 72 |
| **AWS current-standard companion complete** | 72 / 72 |
| **AWS current-standard gaps** | 0 |
| **Microsoft Skills current-standard companions** | 11 / 189 |
| **Microsoft Skills current-standard gaps** | 178 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical physical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material, not repository-owned execution machinery.

## Inventory boundaries

- **43 active first-party skills** are **43/43 provenance-complete** and have structured semantic review evidence.
- **12 pinned external corpora** provide the broad reference surface.
- **183 exact-version third-party verification companions** are persisted.
- `registry/sources.yaml` contains **19 unique source identities**.
- AWS Agent Toolkit has an exact eligible denominator of **72** at registered pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`. All **72/72** were historically inspected and all **72/72** now have current-standard per-skill provenance + verification companions.
- AWS completion means every eligible entry has decisive current evidence, not that every upstream procedure is approved unchanged. Rejected states remain preserved where authority, secret handling, freshness, or other quality defects require adaptation/reference-only treatment.
- Microsoft Skills has an exact eligible denominator of **189** independently front-mattered skill entry points at registered pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`; **11/189** have current-standard provenance + verification companions and **178** remain.
- Historical source-level evidence remains valid for what it establishes. Other corpora should be reconciled from prior evidence before fresh review.

## AWS curation completion

The sequential reconciliation campaign completed every AWS core and specialized package at the registered pin. Fully reconciled specialized families include analytics, database, EC2, migration/modernization, networking/content-delivery, operations, security/identity, serverless, storage, system-table, and web/mobile.

The final nine gaps were five storage skills, three system-table skills, and `aws-amplify`. Current-standard review preserved useful negative evidence rather than rubber-stamping completion:

- storage packages with useful diagnostics/design guidance were rejected unchanged when mutation/remediation paths lacked mandatory affirmative authorization;
- system-table packages retained strong SQL/query guidance but were rejected unchanged because their configure/grant modes mutate integrations or permissions without a distinct approval gate;
- `aws-amplify` was rejected unchanged because deployment paths create apps, IAM roles/policies, backend resources, domains and release jobs without a distinct infrastructure/cost authorization boundary, and one CI example exposes a GitHub token through a command argument.

All AWS verification companions explicitly distinguish structured static review from behavioral evidence; behavioral validation remains `not-run` unless representative external evidence actually exists.

## Microsoft Skills curation

Eleven current-standard Microsoft units are now persisted at the registered pin:

- `applicationinsights-web-ts`, package tree `cb03b364b8f9dcb5fc2ee9662758a1f949c23102`, is decisively `rejected` for unchanged adoption because its primary browser setup enables telemetry before first user interaction without making consent or approved data handling a mandatory precondition. The package retains useful privacy, PII-scrubbing, observability and GenAI tracing guidance as adaptation/reference evidence. Behavioral validation is `not-run`.
- `skill-creator`, package tree `44744c928eba10e9e69272a6bab0859b79c480c5`, is `verified` by structured static review at 18/20. It provides strong skill-authoring guidance around concise context, progressive disclosure, current-documentation verification, credential hygiene, lifecycle cleanup and portable package structure. Its bundled Python helpers mutate local skill/package files only when deliberately invoked by an authorized host and remain upstream package tooling, not `skillz` runtime. Behavioral validation is `not-run`.
- `cloud-solution-architect`, package tree `cf94add87e80c754b41298fe08dc16cd9b442531`, is `verified` by structured static review at 18/20. It provides broad Azure architecture, design-pattern, technology-selection, Well-Architected, mission-critical and ADR guidance. Its workflow is advisory/read-only: consequential deployment, identity, networking and remediation mechanisms are discussed as design considerations but are not executed by the procedure. Behavioral validation is `not-run`, and product-specific recommendations remain freshness-sensitive.
- `copilot-sdk`, package tree `dbdf15d9f078af5a2996a8b9a3bf719e80330aed`, is `verified` by structured static review at 17/20. It provides cross-language Copilot SDK guidance for sessions, streaming, custom tools, hooks, MCP integration, authentication, BYOK, persistence and deployment. Its pre-tool hook exposes explicit `allow` / `deny` / `ask` permission decisions and post-tool redaction support. Consequential effects arise only through host-defined tools, MCP servers, deployment code or application behavior and remain subject to the host application's authorization model. Behavioral validation is `not-run`.
- `azure-identity-dotnet`, nested under the `azure-sdk-dotnet` plugin, package tree `a77d4ff49b15f776a2daad5f4a59fa6561c94414`, is `verified` by structured static review at 17/20. It provides focused Azure.Identity guidance for .NET across DefaultAzureCredential, managed identity, service principals, certificate credentials, sovereign clouds, diagnostics and error handling. Secret-bearing examples use placeholders and external environment/file paths rather than soliciting real credentials into conversation. Package installation and authenticated token/service access remain host-authorized actions. Behavioral validation is `not-run`.
- `azure-ai-document-intelligence-dotnet`, nested under the `azure-sdk-dotnet` plugin, package tree `17be5880febf72e104b84d32e626197693d90e3b`, is `rejected` unchanged by structured static review at 14/20. The package contains useful document-analysis, prebuilt-model, custom-model/classifier, authentication and diagnostics guidance, but its primary workflows create custom models/classifiers and delete models without a distinct affirmative authorization gate. It also demonstrates sending potentially sensitive invoices, receipts, identity documents, tax forms, health-insurance cards and arbitrary documents to an external service without making approved data handling/privacy authorization a mandatory prerequisite. Secret examples use placeholders/environment variables. Preserve as adaptation/reference evidence with explicit mutation/cost and data-governance gates added before operational use. Behavioral validation is `not-run`.
- `azure-ai-agents-persistent-dotnet`, nested under the `azure-sdk-dotnet` plugin, package tree `62d6ee2d1e7ffe649e6bae74b9235d061b852376`, is `rejected` unchanged by structured static review at 14/20. It contains useful persistent-agent SDK guidance across agent CRUD, threads, messages, runs, streaming, function calling, file search, vector stores, Bing grounding, Azure AI Search, OpenAPI, Azure Functions, MCP, SharePoint and Fabric. The primary procedure creates and deletes remote agents, threads, files and vector stores and invokes external/function/tool paths without a distinct affirmative authorization gate; the function-calling example submits outputs with `toolApprovals: null`. Secret examples use placeholders, environment variables and Azure credential objects rather than soliciting actual secrets. Preserve as adaptation/reference evidence with explicit resource/cost/data/tool authorization gates. Behavioral validation is `not-run`.
- `azure-ai-openai-dotnet`, nested under the `azure-sdk-dotnet` plugin, package tree `38bd23798e46c5c010737ecabfcf2bc8d8033d9a`, is `rejected` unchanged by structured static review at 14/20. The package contains useful Azure OpenAI/.NET guidance for chat, streaming, structured outputs, reasoning models, Azure AI Search RAG, embeddings, image generation, audio, authentication, error handling and tool-call surfacing. Its primary examples directly invoke metered external AI services and transmit prompts, search-derived content, audio, image-generation requests and other application/user data without a distinct affirmative cost/data-transmission authorization boundary or mandatory approved-data-handling prerequisite. Function calls are surfaced rather than executed and the skill recommends validating tool arguments, which is useful safety evidence but does not authorize the external service calls themselves. Credential examples use environment variables, placeholders, DefaultAzureCredential and managed identity rather than soliciting actual secrets. Preserve as adaptation/reference evidence with explicit cost, data-governance and external-service authorization gates. Behavioral validation is `not-run`.
- `azure-ai-projects-dotnet`, nested under the `azure-sdk-dotnet` plugin, package tree `2dabc3855c1b4ea3c8bf6f855ccf310c9e36eccd`, is `rejected` unchanged by structured static review at 14/20. It contains useful Azure AI Foundry/.NET guidance for project clients, persistent/versioned agents, connections, deployments, datasets, indexes, evaluations, Azure OpenAI access, authentication and tool integrations. Its normal workflows create and delete remote agents/threads, create agent versions, upload/delete datasets, create/update/delete indexes, run evaluations, and invoke metered AI/search services without distinct resource/cost/data-transmission authorization boundaries. The connection example also exposes `includeCredentials: true` without a separate credential-access authorization gate. Credential setup otherwise uses placeholders, environment variables, DefaultAzureCredential and managed identity. Preserve as adaptation/reference evidence with explicit mutation, cost, data-governance, credential-access and external-service authorization gates. Behavioral validation is `not-run`.
- `azure-ai-voicelive-dotnet`, nested under the `azure-sdk-dotnet` plugin, package tree `5569dda3e6dba27f9101b32be55992a6f62443c9`, is `rejected` unchanged by structured static review at 14/20. It provides useful real-time Voice Live guidance across session setup, authenticated WebSocket communication, text/audio modalities, voices/models, VAD, event handling, function-call integration, audio configuration and disposal. The core workflow starts a metered external AI session and transmits user audio/text without a distinct affirmative cost/data-transmission authorization boundary or mandatory recording/privacy/data-governance prerequisite. Its function-calling example also tells the host to call an external weather service without a separate action approval gate. Credential examples use placeholders/environment variables, DefaultAzureCredential and managed-identity guidance. Preserve as adaptation/reference evidence with explicit recording/privacy, cost, external-service, data-governance and function/tool authorization gates. Behavioral validation is `not-run`.
- `azure-eventgrid-dotnet`, nested under the `azure-sdk-dotnet` plugin, package tree `482dbcdcc9a1108a63e53395c16d08ac5b3fef22`, is `rejected` unchanged by structured static review at 14/20. It provides useful Event Grid guidance across topics/domains, namespace pull delivery, CloudEvents/EventGridEvent schemas, Entra/key/SAS authentication, publishing, receive/acknowledge/release/reject flows, parsing, system events, Azure Functions triggers, error handling and regional failover. Normal workflows publish event payloads and mutate external broker state through acknowledgement, release and rejection without a distinct affirmative side-effect/cost/data-transmission authorization boundary or mandatory approved-data-handling prerequisite. The failover pattern can resend event batches to a secondary region. Credential guidance is comparatively strong through managed-identity/DefaultAzureCredential recommendations and placeholder key examples. Preserve as adaptation/reference evidence with explicit publish/message-state, cost, data-governance and cross-region failover authorization gates. Behavioral validation is `not-run`.

The Microsoft source's exact eligible denominator is **189**. The accounting unit is an independently front-mattered `SKILL.md` entry point at the registered pin. The pinned topology contributes 129 language-SDK plugin entries; 13 real canonical `.github/skills` packages with duplicate exposure de-duplicated; 28 Azure-plugin top-level packages with the duplicate `entra-agent-id` exposure de-duplicated; 10 Deep Wiki entries; 5 Microsoft 365 Agents Toolkit top-level entries; and 6 additional nested skill entry points: `microsoft-foundry/finetuning`, `models/deploy-model`, `models/deploy-model/capacity`, `models/deploy-model/customize`, `models/deploy-model/preset`, and `teams-app-developer/slack-to-teams`. Symlink mirrors and duplicate exposure paths do not create additional units, and ordinary workflow/reference `.md` files remain dependencies of their parent skill. The upstream README's inconsistent 174/175 counts are therefore not used as corpus truth.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use issue-first intake. Discovery surfaces, including the connected Creator Technical Resource Catalog, provide leads only. Their scores, labels, creator attributions, popularity, and recommendations do not establish `skillz` provenance or individual quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means the exact material passed structured static semantic review. `validated` additionally requires representative external scenario/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Complete Microsoft Skills at its registered pin against the exact **189-entry** denominator.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora whose prior review evidence is broader than their current one-file companion shelf.
4. Continue admitted/tracked creator-source curation and denominator reconciliation.
5. Continue governed discovery/source-vetting through issue-first intake and omission recovery.
6. Keep README, this System State, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The current living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.