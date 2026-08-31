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
| **Persisted third-party review companions** | 215 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS historical review** | 72 / 72 |
| **AWS current-standard companion complete** | 72 / 72 |
| **AWS current-standard gaps** | 0 |
| **Microsoft Skills current-standard companions** | 43 / 189 |
| **Microsoft Skills current-standard gaps** | 146 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 10 / 26 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical physical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material, not repository-owned execution machinery.

## Inventory boundaries

- **43 active first-party skills** are **43/43 provenance-complete** and have structured semantic review evidence.
- **12 pinned external corpora** provide the broad reference surface.
- **215 exact-version third-party verification companions** are persisted.
- `registry/sources.yaml` contains **19 unique source identities**.
- AWS Agent Toolkit has an exact eligible denominator of **72** at registered pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`. All **72/72** were historically inspected and all **72/72** now have current-standard per-skill provenance + verification companions.
- AWS completion means every eligible entry has decisive current evidence, not that every upstream procedure is approved unchanged. Rejected states remain preserved where authority, secret handling, freshness, or other quality defects require adaptation/reference-only treatment.
- Microsoft Skills has an exact eligible denominator of **189** independently front-mattered skill entry points at registered pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`; **43/189** have current-standard provenance + verification companions and **146** remain.
- The direct `.github/plugins/azure-sdk-dotnet/skills/` slice contains **29** packages and is **29/29 current-standard companion-complete**.
- The direct `.github/plugins/azure-sdk-java/skills/` slice contains **26** packages and is **10/26 current-standard companion-complete**.
- Historical source-level evidence remains valid for what it establishes. Other corpora should be reconciled from prior evidence before fresh review.

## AWS curation completion

The sequential reconciliation campaign completed every AWS core and specialized package at the registered pin. Fully reconciled specialized families include analytics, database, EC2, migration/modernization, networking/content-delivery, operations, security/identity, serverless, storage, system-table, and web/mobile.

The final AWS tranche preserved useful negative evidence rather than rubber-stamping completion. Behavioral evidence remains `not-run` unless representative external evaluation actually occurred. Upstream scripts, assets, references, templates and examples remain intact package dependencies rather than `skillz` execution machinery.

## Microsoft Skills curation

Microsoft Skills is the active admitted-source frontier. The denominator is **189** independently front-mattered `SKILL.md` entry points at the exact registered pin; duplicate exposure paths and symlink mirrors are de-duplicated, while ordinary workflow/reference `.md` files remain dependencies of their parent package.

Current progress is **43/189** current-standard companion-complete. Previously reconciled units include root/cross-language packages and the complete direct `.NET` SDK plugin slice. Java is now the active coherent plugin/language family at **10/26**.

### .NET direct plugin slice — CURRENT-STANDARD COMPLETE

All **29/29 direct `.github/plugins/azure-sdk-dotnet/skills/` packages** now have exact-version provenance + verification companions at registered Microsoft pin `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.

The prior management-plane tranche reconciled fifteen packages, all rejected unchanged with scores from **11/20 to 14/20**, preserving specific resource, cost, secret, network, identity, data, dependency, destructive-action and freshness findings rather than applying a family-level verdict.

The closing five direct packages are likewise individually resolved:

- `azure-search-documents-dotnet` — rejected unchanged, **13/20**. Useful full-text/vector/semantic/hybrid search guidance, but normal index mutation, document CRUD and query/embedding/indexed-content transmission lack distinct mutation, data-governance and cost gates. Integrated vectorization can also route text to Azure OpenAI.
- `azure-security-keyvault-keys-dotnet` — rejected unchanged, **12/20**. Useful key-management/cryptography guidance, but key creation/rotation/policy mutation, delete-and-purge, decrypt/sign/unwrap and local backup-file handling lack distinct key-lifecycle, destructive, crypto-use and secret-file authorization gates.
- `azure-servicebus-dotnet` — rejected unchanged, **13/20**. Useful enterprise messaging guidance, but send/settlement, background processors, session-state mutation, messaging-entity CRUD and cross-entity transactions lack distinct data/message-state/background/resource/cost gates.
- `m365-agents-dotnet` — rejected unchanged, **13/20**. Useful Microsoft 365 Agents SDK hosting/routing/authentication prior art, but normal handlers send external activities, the Copilot Studio client starts conversations and transmits prompts, and error handling deletes conversation state without distinct communication/data/state authorization boundaries.
- `microsoft-azure-webjobs-extensions-authentication-events-dotnet` — rejected unchanged, **11/20**. Useful Entra Authentication Events prior art, but normal examples alter issued-token claims, block sign-up, modify identity attributes, transmit user IDs to an external profile service, and send OTP secrets with phone numbers to external messaging providers without mandatory identity/token, PII/privacy, OTP and external-message gates; examples also log user identifiers and phone numbers.

Every direct `.NET` package retains exact tree/blob identity, exact source revision/date, dependencies, portability, current authority classification, controlled taxonomy tags, decisive static state and `validation_status: not-run`. Completion means decisive current evidence for every package, not universal approval.

### Java plugin slice — ACTIVE

The direct Java plugin has an exact denominator of **26** packages and is now **10/26 current-standard companion-complete** at the registered Microsoft pin. Each reviewed Java package retains its own exact package-tree, `SKILL.md` fingerprint, source-path revision/freshness evidence, dependencies, authority, portability, controlled tags, decisive state, and explicit behavioral-evidence status.

- `azure-ai-agents-persistent-java` — rejected unchanged, **14/20**. Remote agent/thread/run/file/vector-store mutation, local-file upload, metered execution, and downstream function/tool effects lack distinct authority gates.
- `azure-ai-anomalydetector-java` — rejected unchanged, **13/20**. Time-series transmission, SAS-backed multivariate training/inference, model lifecycle and deletion lack data, cost and destructive-action boundaries.
- `azure-ai-contentsafety-java` — rejected unchanged, **12/20**. Text/image moderation sends content to an external metered service and mutates blocklist state without privacy/data, mutation and cost gates; the top-level SDK version also conflicts with its bundled examples.
- `azure-ai-formrecognizer-java` — rejected unchanged, **12/20**. Document Intelligence can transmit local files and sensitive IDs/invoices/receipts/tax/insurance documents and create/delete custom models/classifiers without mandatory sensitive-data, lifecycle and cost gates; implementation guidance is version-sensitive.
- `azure-ai-projects-java` — rejected unchanged, **13/20**. Foundry dataset/index mutation, local-file upload, credential-bearing connection access and external evaluation operations lack distinct resource, credential, data and cost authorization.
- `azure-ai-vision-imageanalysis-java` — rejected unchanged, **13/20**. Local images/document images and remote URLs are sent to an external metered service; OCR and people detection increase personal/sensitive-data exposure without a mandatory privacy/data boundary.
- `azure-ai-voicelive-java` — rejected unchanged, **12/20**. Metered live sessions, transcription, microphone capture, continuous audio transmission and function execution lack recording/privacy, cost, external-service and tool-action authorization gates.
- `azure-appconfiguration-java` — rejected unchanged, **13/20**. Production setting CRUD, feature rollout and explicit-user targeting, secret-reference metadata, read-only protection and snapshot state changes lack distinct configuration, targeting, sensitive-metadata and destructive/state-transition authorization gates.
- `azure-communication-callautomation-java` — rejected unchanged, **11/20**. PSTN call origination/answering, speech and DTMF processing, audio/video recording and download, call transfers, participant changes and termination lack mandatory telephony, participant-consent, recording/privacy, data, cost and destructive-action boundaries. The top-level dependency is 1.6.0 while bundled examples use 1.5.2.
- `azure-communication-callingserver-java` — **retired, 14/20**. Microsoft explicitly marks the CallingServer SDK deprecated and directs new development to Call Automation. The package remains useful migration and legacy-maintenance evidence, but normal unchanged selection is inappropriate; its legacy recording example also lacks a distinct participant-consent/privacy authorization gate.

Behavioral validation remains `not-run` for all ten because no separate representative external scenario/adversarial evidence has been recorded.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use issue-first intake. Discovery surfaces, including the connected Creator Technical Resource Catalog, provide leads only. Their scores, labels, creator attributions, popularity, and recommendations do not establish `skillz` provenance or individual quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means the exact material passed structured static semantic review. `validated` additionally requires representative external scenario/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Microsoft Skills in coherent plugin/language batches against the exact **189-entry** denominator, with the remaining **16 Java direct packages** next after the current 10/26 tranche.
2. Complete Microsoft Azure Skills.
3. Reconcile historically completed external corpora whose prior review evidence is broader than their current one-file companion shelf.
4. Continue admitted/tracked creator-source curation and denominator reconciliation.
5. Continue governed discovery/source-vetting through issue-first intake and omission recovery.
6. Keep README, this System State, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The current living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.