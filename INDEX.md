# Skill Catalog Snapshot

**Snapshot date:** 2026-09-03

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, or reconciliation.

Canonical inputs are `registry/categories.yaml`, `registry/sources.yaml`, `registry/local-verification.json`, `registry/skills/`, and `registry/verification/`.

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 43 |
| First-party provenance-complete | 43 / 43 |
| Pinned external corpora | 12 |
| Unique registered source identities | 19 |
| Persisted third-party exact-version reviews | 307 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 135 / 189 |
| Microsoft Skills current-standard gaps | 54 |
| Microsoft .NET direct-package companions | 29 / 29 |
| Microsoft Java direct-package companions | 26 / 26 |
| Microsoft Python direct-package companions | 40 / 40 |
| Microsoft Rust direct-package companions | 9 / 9 |
| Microsoft TypeScript direct-package companions | 25 / 25 |

## First-party skills by purpose

### Planning & Productivity
`daily-briefing`, `decision-log`, `inbox-triage`, `learning-plan`, `task-surface`, `week-in-review`

### Writing & Communication
`brief-writer`, `deck-outline`, `devlog-draft`, `handoff-writer`, `standup-writer`

### Research & Analysis
`compare`, `deep-dive`, `fact-check`, `paper-digest`

### Software & Repositories
`repo-doctor`, `repo-pulse`, `todo-harvester`

### Agent Operations & Security
`agent-home-doctor`, `agent-postmortem`, `automation-receipts`, `mcp-vetting`, `permissions-review`

### Monitoring & Intelligence
`claude-pulse`, `deepseek-pulse`, `gemini-pulse`, `github-pulse`, `glm-pulse`, `governance-pulse`, `hf-pulse`, `inference-pulse`, `kimi-pulse`, `llama-pulse`, `mcp-pulse`, `memory-pulse`, `mistral-pulse`, `openai-pulse`, `perplexity-pulse`, `qwen-pulse`, `xai-pulse`

### Business & Career
`career-radar`, `finance-review`, `smallbiz-ops`

## Registered source roles

**Pinned reference corpora:** `anthropic-skills`, `anthropic-knowledge-work-plugins`, `vercel-agent-skills`, `microsoft-skills`, `microsoft-azure-skills`, `aws-agent-toolkit`, `mattpocock-skills`, `addyosmani-agent-skills`, `openhands-extensions`, `cline-skills`, `cloudflare-skills`, `google-agents-cli`.

**Tracked corpora:** `cole-medin-skills`, `david-ondrej-skills`, `bm629-agent-skills`, `openclaw-agent-skills`, `archieindian-superpowers`.

**Normative/discovery:** `agentskills-spec` is a normative specification; `github-awesome-copilot` is a dynamic discovery surface.

## Interpretation

Physical presence or registration does not establish individual skill quality. For unchanged third-party consideration, use exact-version companion evidence and apply:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

AWS is fully reconciled at **72/72**. Microsoft Skills is active at **135/189**, leaving **54** gaps. Direct `.NET`, Java, Python, Rust, and TypeScript slices are complete. Direct TypeScript is **25/25** from the registered-pin tree. The TypeScript plugin README claims 24 and omits the separately present `applicationinsights-web-ts` package, so the 25-package tree controls.

The completed TypeScript slice contains twenty-two packages rejected unchanged under current privacy, sensitive-data, secret-custody, durable-state, database/search-index/message/storage mutation, production-configuration, external-publication, identity/access, security-control, cryptographic-operation, destructive-lifecycle, cloud-testing, network-exposure, artifact-publication/retention, telemetry-disclosure, downstream-effect, delegated-credential, notification, cost, communication, model-data-transfer, or authority hard gates while retaining useful adaptation/reference evidence. Three bounded local implementation packages are verified: `frontend-ui-dark-ts` **15/20**, `react-flow-node-ts` **15/20**, and `zustand-store-ts` **16/20**. The final consequential TypeScript package, `m365-agents-ts`, is **rejected unchanged, 13/20** because ordinary M365/Teams/Copilot Studio messaging, Azure OpenAI/Copilot data transfer, remote conversations, and tenant/client credential use lack mandatory tenant, audience, data, communication, production, and credential-custody authorization. Behavioral validation remains `not-run` for all twenty-five unless representative evidence is actually recorded.

The non-direct Microsoft plugin frontier has started with `airunway-aks-setup`, **rejected unchanged, 15/20**. Its exact package tree is `72ec58c0a7c574dc71e14c63feb3d2aa529849ac`; the package includes strong cluster-context reporting, install/deployment confirmations, GPU cost awareness, model-choice confirmation, and terminal-only Hugging Face secret handling, but rollback permits destructive model/secret deletion and provider/controller undeploy without a fresh destructive-action authorization boundary. Preserve those mechanics for adaptation/reference use.

`appinsights-instrumentation` is **rejected unchanged, 12/20** at package tree `8f6b0c9b5af9ab5bbd69d25d58071c9034221eb0`. Its App Insights/OpenTelemetry selection, SDK setup, tracing, resource-topology, secret-reference, and KQL mechanics remain useful, but the package directly instructs cloud resource creation, application/configuration/IaC mutation, telemetry export, and deployment-affecting operations without mandatory target/resource, production-change, cost, telemetry-data/disclosure, deployment, or credential-custody authorization. Behavioral validation is `not-run`.

`azure-ai` is **rejected unchanged, 10/20** at package tree `8a168336305c56e0eea0d89aced7d8a0001de3b5`. It is a useful Azure AI router and condensed reference across Search, Speech, OpenAI, Document Intelligence, Vision, Translation, Transcription, and Content Safety, with strong managed-identity and least-privilege guidance. Unchanged adoption fails because bundled references instruct persistent search-index/document writes and external processing of audio, documents, text, images, and other potentially sensitive content without mandatory data-owner/classification, disclosure/model-transfer, target-resource, mutation, production, retention, cost, or credential-custody authorization. Behavioral validation is `not-run`.

The next Microsoft Skills gap in registered-pin source order is `.github/plugins/azure-skills/skills/azure-aigateway`.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.