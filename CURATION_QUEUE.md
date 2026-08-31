# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository is entirely passive; the external host agent performs curation under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills.
- **43/43** first-party provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **183** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.
- Historical source-level review evidence remains broader than the one-file companion shelf for some completed corpora and must be reconciled rather than discarded or blindly repeated.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use the issue-first workflow in `docs/candidate-intake.md`. Intentional discovery inputs are documented in `docs/discovery-surfaces.md`, including the connected Creator Technical Resource Catalog. Discovery intelligence never substitutes for canonical upstream identity, license/terms, exact version, or individual quality evidence.

Every governed user-facing skill must retain truthful provenance and exact-version evidence appropriate to its relationship. Missing provenance is a corpus-completeness defect.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit.

- First-party denominator: **43**.
- First-party structured semantic reviews: **43/43**.
- First-party standalone provenance companions: **43/43** under `registry/skills/local-skills/`.
- Enforcement is documentary/evidentiary through external-agent curation, not repository-owned scripts, CI, scanners, or runtime.

## Completed historical source-level review evidence

| Source | Historical reviewed denominator | Recorded result/state |
|---|---:|---|
| Anthropic Skills | 17 / 17 | 10 verified, 7 rejected |
| Anthropic Knowledge Work Plugins | 74 / 74 | 36 verified, 38 rejected unchanged |
| Matt Pocock Skills | 29 / 29 | Complete |
| OpenHands Extensions | 1 / 1 | `theme-factory` rejected unchanged |
| Vercel Agent Skills | 9 / 9 | 6 verified, 3 rejected |
| Cloudflare Skills | 13 / 13 | 11 verified, 2 rejected |
| Google Agents CLI | 7 / 7 | All verified |
| Cline Skills | 36 / 36 | 19 verified, 17 rejected unchanged, plus one separately characterized internal/unlisted skill |
| Addy Osmani Agent Skills | 24 / 24 | Complete with decisive exact-version static states |

Search and reconcile this prior evidence before fresh re-review.

## Admitted-source curation

### AWS Agent Toolkit — CURRENT-STANDARD COMPLETE

- Registered pin: `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Exact eligible denominator: **72**.
- Historical inspection: **72/72**.
- Current-standard provenance + verification companion completeness: **72/72**.
- Remaining current-standard gaps: **0**.

The sequential campaign reconciled every core and specialized package, including analytics, database, EC2, migration/modernization, networking/content delivery, operations, security/identity, serverless, storage, system-table, and web/mobile. Completion preserves decisive negative states rather than converting everything to approval. Rejected packages remain reference/adaptation evidence when useful.

Representative authority findings from the final tranche:

- Storage packages retained valuable diagnostics and safety mechanisms but were rejected unchanged where create/remediate paths lacked a mandatory affirmative mutation gate.
- The three system-table packages contain useful read/query cores but also configuration/access-grant paths that mutate integrations or permissions without plan authorization, so the unchanged packages are rejected.
- `aws-amplify` contains strong Gen2/framework/deployment guidance but is rejected unchanged because deployment paths create apps, IAM roles/policies, resources, domains and release jobs without a distinct infrastructure/cost approval boundary; one example also passes a GitHub auth token in a command argument.

Behavioral evidence remains `not-run` unless representative external evaluation actually occurred. Upstream scripts, assets, references, templates and examples remain intact package dependencies rather than `skillz` execution machinery.

### Microsoft Skills — ACTIVE FRONTIER

- Registered pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Exact eligible denominator: **189** independently front-mattered skill entry points.
- Current-standard provenance + verification companions persisted: **11/189**.
- Remaining current-standard gaps: **178**.
- `applicationinsights-web-ts`: package tree `cb03b364b8f9dcb5fc2ee9662758a1f949c23102`; `rejected` unchanged because browser telemetry is initialized before user interaction without mandatory consent/data-governance authorization. Retain as adaptation/reference evidence. Behavioral validation is `not-run`.
- `skill-creator`: package tree `44744c928eba10e9e69272a6bab0859b79c480c5`; `verified` 18/20 by structured static review. Strong on concise authoring, progressive disclosure, exact SDK source context, current-documentation checks, credential hygiene and lifecycle cleanup. Bundled Python helpers perform local skill/package file operations only when invoked by an authorized host and remain upstream source tooling. Behavioral validation is `not-run`.
- `cloud-solution-architect`: package tree `cf94add87e80c754b41298fe08dc16cd9b442531`; `verified` 18/20 by structured static review. Strong advisory coverage of Azure architecture principles, design patterns, technology tradeoffs, mission-critical design, Well-Architected review and ADR capture. Consequential cloud operations are referenced as architecture considerations rather than executed by the workflow, so implementation remains behind separate host authorization. Behavioral validation is `not-run`.
- `copilot-sdk`: package tree `dbdf15d9f078af5a2996a8b9a3bf719e80330aed`; `verified` 17/20 by structured static review. Strong cross-language SDK coverage for sessions, streaming, custom tools, hooks, MCP, authentication, BYOK, persistence, agents/skills and deployment. The pre-tool hook exposes `allow` / `deny` / `ask` permission decisions and post-tool redaction. Consequential behavior is delegated to host-defined tools, MCP servers or application/deployment code and remains subject to the host application's authorization model. Behavioral validation is `not-run`.
- `azure-identity-dotnet`: nested plugin package tree `a77d4ff49b15f776a2daad5f4a59fa6561c94414`; `verified` 17/20 by structured static review. Focused Azure.Identity guidance for .NET covering credential chains, managed identities, service principals, certificates, sovereign clouds, diagnostics and error handling. Secret examples use placeholders/external credential paths; package installation and authenticated token/service access remain host-authorized actions. Behavioral validation is `not-run`.
- `azure-ai-document-intelligence-dotnet`: nested plugin package tree `17be5880febf72e104b84d32e626197693d90e3b`; `rejected` unchanged at 14/20. Useful document-analysis and SDK guidance is retained, but custom model/classifier creation and model deletion lack a distinct affirmative authorization gate, and potentially sensitive document transmission lacks a mandatory approved data-handling/privacy prerequisite. Secret examples use placeholders/environment variables. Preserve as adaptation/reference evidence with explicit mutation/cost and data-governance gates before operational use. Behavioral validation is `not-run`.
- `azure-ai-agents-persistent-dotnet`: nested plugin package tree `62d6ee2d1e7ffe649e6bae74b9235d061b852376`; `rejected` unchanged at 14/20. Useful persistent-agent SDK guidance is retained across agent CRUD, threads, messages, runs, streaming, function calling, file search/vector stores, Bing, Azure AI Search, OpenAPI, Azure Functions, MCP, SharePoint and Fabric. The primary workflow creates and deletes remote resources and invokes tool/external-service paths without a distinct affirmative authorization gate; function execution is submitted with `toolApprovals: null`. Credential examples use placeholders/environment variables and Azure credential objects. Preserve as adaptation/reference evidence with explicit resource/cost/data/tool authorization gates before operational use. Behavioral validation is `not-run`.
- `azure-ai-openai-dotnet`: nested plugin package tree `38bd23798e46c5c010737ecabfcf2bc8d8033d9a`; `rejected` unchanged at 14/20. Useful Azure OpenAI/.NET guidance is retained across chat, streaming, structured outputs, reasoning models, Azure AI Search RAG, embeddings, image generation, audio, authentication, error handling and tool-call surfacing. The primary examples directly invoke metered external AI services and transmit prompts, search-derived content, audio, image-generation requests and other application/user data without a distinct affirmative cost/data-transmission authorization boundary or mandatory approved-data-handling prerequisite. Function calls are surfaced rather than executed and the skill recommends validating tool arguments, which is useful safety evidence but does not authorize the external service calls themselves. Credential examples use environment variables, placeholders, DefaultAzureCredential and managed identity. Preserve as adaptation/reference evidence with explicit cost, data-governance and external-service authorization gates before operational use. Behavioral validation is `not-run`.
- `azure-ai-projects-dotnet`: nested plugin package tree `2dabc3855c1b4ea3c8bf6f855ccf310c9e36eccd`; `rejected` unchanged at 14/20. Useful Azure AI Foundry/.NET guidance is retained across project clients, persistent/versioned agents, connections, deployments, datasets, indexes, evaluations, Azure OpenAI access, authentication and available tool integrations. The normal workflows create/delete agents and threads, create agent versions, upload/delete datasets, create/update/delete indexes, run evaluations, and invoke metered AI/search services without distinct resource/cost/data-transmission authorization gates; a connection retrieval example also uses `includeCredentials: true` without a separate credential-access authorization gate. Credential setup otherwise uses placeholders/environment variables, DefaultAzureCredential and managed identity. Preserve as adaptation/reference evidence with explicit mutation, cost, data-governance, credential-access and external-service authorization gates before operational use. Behavioral validation is `not-run`.
- `azure-ai-voicelive-dotnet`: nested plugin package tree `5569dda3e6dba27f9101b32be55992a6f62443c9`; `rejected` unchanged at 14/20. Useful real-time Voice Live guidance is retained across authenticated session setup, bidirectional WebSocket events, text/audio modalities, model and voice selection, VAD, audio configuration, error handling and function-call integration. The core workflow starts a metered external AI session and transmits user audio/text without a distinct affirmative cost/data-transmission authorization boundary or mandatory recording/privacy/data-governance prerequisite; its function-calling example directs an external weather-service call without a separate action approval gate. Credential examples use placeholders/environment variables, DefaultAzureCredential and managed-identity guidance. Preserve as adaptation/reference evidence with explicit recording/privacy, cost, external-service, data-governance and function/tool authorization gates before operational use. Behavioral validation is `not-run`.
- `azure-eventgrid-dotnet`: nested plugin package tree `482dbcdcc9a1108a63e53395c16d08ac5b3fef22`; `rejected` unchanged at 14/20. Useful Event Grid guidance is retained across topics/domains, namespace pull delivery, CloudEvents/EventGridEvent schemas, Entra/key/SAS authentication, publishing, receive/acknowledge/release/reject flows, parsing, system events, Azure Functions triggers, error handling and regional failover. Normal workflows publish event payloads and mutate external broker state through acknowledgement, release and rejection without a distinct affirmative side-effect/cost/data-transmission authorization boundary or mandatory approved-data-handling prerequisite. The failover pattern can resend event batches to a secondary region. Credential guidance is comparatively strong through managed-identity/DefaultAzureCredential recommendations and placeholder key examples. Preserve as adaptation/reference evidence with explicit publish/message-state, cost, data-governance and cross-region failover authorization gates. Behavioral validation is `not-run`.
- Denominator accounting is now closed at the exact registered pin. The unit is an independently front-mattered `SKILL.md` entry point. The count includes 129 language-SDK plugin entries; real canonical `.github/skills` packages; 28 Azure-plugin top-level packages; 10 Deep Wiki entries; 5 Microsoft 365 Agents Toolkit top-level entries; and 6 additional nested skill entry points (`microsoft-foundry/finetuning`, `models/deploy-model`, `models/deploy-model/capacity`, `models/deploy-model/customize`, `models/deploy-model/preset`, and `teams-app-developer/slack-to-teams`). Duplicate exposure paths are de-duplicated by skill identity, `.github/skills` symlink mirrors and plugin symlink aliases do not create additional units, and ordinary workflow/reference `.md` files remain part of their parent package. The upstream README's conflicting 174/175 headlines are not used as denominator evidence.
- Continue sequential review from the pinned tree and check both companion paths before every unit. The `.github/plugins/azure-sdk-dotnet/skills/` slice contains **29** direct skill-package directories; seven currently have current-standard companions (`azure-identity-dotnet`, `azure-ai-document-intelligence-dotnet`, `azure-ai-agents-persistent-dotnet`, `azure-ai-openai-dotnet`, `azure-ai-projects-dotnet`, `azure-ai-voicelive-dotnet`, `azure-eventgrid-dotnet`).
- Favor differentiated Microsoft/M365/Foundry/developer-platform mechanisms rather than assuming official branding proves value.

### Microsoft Azure Skills — QUEUED AFTER MICROSOFT SKILLS

- Registered pin: `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Establish the exact eligible denominator before completion claims.
- Distinguish planning/read-only guidance from deployment, RBAC, cost, identity and other higher-authority operations.

### Other admitted/tracked sources

- **Cole Medin Skills**: pin `fb2e876f057c5356d6603ba0c52d6b4418d893ba`; denominator 33; selective reviews exist.
- **David Ondrej Skills**: public pin `7d0ef87dad1f638cab58995eead9e0e6e3fae237`; current evidence describes 44 canonical `SKILL.md` files while a historical tracker recorded 55. Reconcile denominator before completion claims.
- **OpenClaw Agent Skills**: pin `6cd3366b10e2a8c5608265f692acf9f5da2b2448`; denominator 8; selective `handoff` review exists.
- **Archie Indian OpenClaw Superpowers**: pin `a95a59d221d44b89d4fc27a52934e24fb2060ddb`; denominator 56; selective `secrets-hygiene` review exists.
- **Sabrina Ramonov Learn Claude Code Skills**: historical denominator 2; canonical source identity/pin/license must be recovered before further work.

## Evidence-reconciliation lane

Historically completed corpora with broader prior review evidence than their current one-file companion shelf should be reconciled without automatic re-review. High-value targets include Anthropic Knowledge Work Plugins, Cline, Addy Osmani, and any completed Vercel/Cloudflare/Google/Matt records not represented one-for-one today.

## Discovery/source-vetting frontier

Discovery proceeds in parallel but does not interrupt admitted-source completion merely to increase issue counts.

Current intentional surfaces/candidates include Hugging Face Skills, Selamy Labs Agent Skills, Hypergiant Agent Skills, BCGov Agent Skills, GitHub Awesome Copilot, Agent Skills Specification, the connected Creator Technical Resource Catalog, and open candidate-evaluation issues.

New discoveries are queued as issues before admission. Restricted or unclear-license material remains reference-only unless terms later support a different relationship. Popularity and creator reputation are omission/context signals only.

## Working rules

1. **Finish the admitted corpus.** Sequential curation remains the default.
2. **Do not lower the bar for throughput.** Every unit gets duplication checking, exact identity, provenance, license/terms, dependency context, authority, portability, freshness, controlled tags, decisive static state and explicit behavioral-evidence status.
3. **Search before re-reviewing.** Recover compatible prior evidence first.
4. **Do not erase negative evidence.** Rejection/retirement reasons prevent repeated mistakes.
5. **Preserve complete upstream packages.** Their tooling is source context, not repository runtime.
6. **Keep discovery separate from admission.** Discovery intelligence is not proof.
7. **Keep `skillz` passive.** No repository-owned runtime, scripts, tests, CI, scheduler, monitor, crawler, installer, synchronizer, preflight, generator, background service, vector database, or autonomous observer.
8. **Keep public accounting synchronized.** README, System State, this ledger, `INDEX.md`, and `index.json` must agree after each material batch.
9. **Keep issues/PRs honest.** Every open item should have an active, blocked/waiting, superseded, or completed disposition rather than indefinite stale status.

## Current posture

**Core:** complete and passive.

**First-party:** 43/43 provenance-complete.

**AWS:** 72/72 historically inspected and **72/72 current-standard companion-complete**.

**Active frontier:** Microsoft Skills, now **11/189** current-standard companion-complete with **178** gaps. Microsoft Azure Skills follows. Discovery and issue/PR hygiene continue in parallel.