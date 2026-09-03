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
| Persisted third-party exact-version reviews | 298 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 126 / 189 |
| Microsoft Skills current-standard gaps | 63 |
| Microsoft .NET direct-package companions | 29 / 29 |
| Microsoft Java direct-package companions | 26 / 26 |
| Microsoft Python direct-package companions | 40 / 40 |
| Microsoft Rust direct-package companions | 9 / 9 |
| Microsoft TypeScript direct-package companions | 19 / 25 |

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

AWS is fully reconciled at **72/72**. Microsoft Skills is active at **126/189**, leaving **63** gaps. Direct `.NET`, Java, Python, and Rust slices are complete. Direct TypeScript is **19/25** from the registered-pin tree. The TypeScript plugin README claims 24 and omits the separately present `applicationinsights-web-ts` package, so the 25-package tree controls.

The current TypeScript companion-complete slice runs through `azure-storage-file-share-ts`. All nineteen reviewed packages are rejected unchanged under current privacy, sensitive-data, secret-custody, durable-state, database/search-index/message/storage mutation, production-configuration, external-publication, identity/access, security-control, cryptographic-operation, destructive-lifecycle, cloud-testing, network-exposure, artifact-publication/retention, telemetry-disclosure, downstream-effect, delegated-credential, cost, or authority hard gates while retaining useful adaptation/reference evidence. `azure-storage-file-share-ts` specifically retains Azure Files client hierarchy, share/directory/file CRUD, quota management, uploads/downloads, streaming, copy operations, metadata/headers, range operations, snapshots, SAS generation, error handling, and authentication choices, but persistent storage mutation/deletion, local-data upload, downloaded-content materialization, quota/range mutation, snapshot deletion, account-key/connection-string/SAS credential paths, and broad delegated share SAS lack mandatory resource, data-owner/classification, per-action, destructive-action, disclosure, retention/recovery, production, and cost authorization. Behavioral validation remains `not-run` unless representative evidence is actually recorded.

The next Microsoft TypeScript unit is `azure-storage-queue-ts`.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.