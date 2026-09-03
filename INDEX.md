# Skill Catalog Snapshot

**Snapshot date:** 2026-09-02

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, or reconciliation.

Canonical inputs are `registry/categories.yaml`, `registry/sources.yaml`, `registry/local-verification.json`, `registry/skills/`, and `registry/verification/`.

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 43 |
| First-party provenance-complete | 43 / 43 |
| Pinned external corpora | 12 |
| Unique registered source identities | 19 |
| Persisted third-party exact-version reviews | 293 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 121 / 189 |
| Microsoft Skills current-standard gaps | 68 |
| Microsoft .NET direct-package companions | 29 / 29 |
| Microsoft Java direct-package companions | 26 / 26 |
| Microsoft Python direct-package companions | 40 / 40 |
| Microsoft Rust direct-package companions | 9 / 9 |
| Microsoft TypeScript direct-package companions | 14 / 25 |

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

AWS is fully reconciled at **72/72**. Microsoft Skills is active at **121/189**, leaving **68** gaps. Direct `.NET`, Java, Python, and Rust slices are complete. Direct TypeScript is **14/25** from the registered-pin tree. The TypeScript plugin README claims 24 and omits the separately present `applicationinsights-web-ts` package, so the 25-package tree controls.

The current TypeScript companion-complete slice runs through `azure-monitor-opentelemetry-ts`. All fourteen reviewed packages are rejected unchanged under current privacy, sensitive-data, secret-custody, durable-state, production-configuration, external-publication, identity/access, security-control, cryptographic-operation, destructive-lifecycle, cloud-testing, network-exposure, artifact-publication/retention, telemetry-disclosure, cost, or authority hard gates while retaining useful adaptation/reference evidence. `azure-monitor-opentelemetry-ts` specifically retains Azure Monitor initialization, deprecated-package migration, custom spans/metrics, logging integration, auto-instrumentation, sampling, processors, context/baggage propagation, cloud-role metadata, correlation, and graceful-shutdown mechanics, but external telemetry/log export, broad automatic capture, and user/tenant baggage propagation lack mandatory destination/region, data-classification, subject/data-transfer, minimization, retention/redaction, and disclosure authorization. Behavioral validation remains `not-run` unless representative evidence is actually recorded.

The next Microsoft TypeScript unit is `azure-postgres-ts`.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.