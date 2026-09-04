# Skill Catalog Snapshot

**Snapshot date:** 2026-09-04

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, or reconciliation.

Canonical inputs are `registry/categories.yaml`, `registry/sources.yaml`, `registry/local-verification.json`, `registry/skills/`, and `registry/verification/`.

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 43 |
| First-party provenance-complete | 43 / 43 |
| Pinned external corpora | 12 |
| Unique registered source identities | 19 |
| Persisted third-party exact-version reviews | 323 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 151 / 189 |
| Microsoft Skills current-standard gaps | 38 |
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

AWS is fully reconciled at **72/72**. Microsoft Skills is active at **151/189**, leaving **38** gaps. Direct `.NET`, Java, Python, Rust, and TypeScript slices are complete.

The non-direct Microsoft plugin frontier currently includes `airunway-aks-setup` (15/20), `appinsights-instrumentation` (12/20), `azure-ai` (10/20), `azure-aigateway` (8/20), `azure-cloud-migrate` (9/20), `azure-compliance` (12/20), `azure-compute` (11/20), `azure-cost` (14/20), `azure-deploy` (15/20), `azure-diagnostics` (13/20), `azure-enterprise-infra-planner` (verified, 18/20), `azure-hosted-copilot-sdk` (13/20), `azure-kubernetes` (12/20), `azure-kubernetes-automatic-readiness` (15/20), `azure-kusto` (14/20), `azure-messaging` (13/20), `azure-prepare` (16/20), `azure-quotas` (14/20), and `azure-rbac` (**verified, 17/20**). `azure-rbac` is bound to exact package tree `b52d696609b18a5dc2bae21e368812fe7b020ec5`, `SKILL.md` blob `02ac75d2ba22b4d7aa1e74469b01575281f05ddc`, and freshness revision `951d18d43210f0d93a931ae5d5c2a774f63d5faf` from 2026-04-21. Preserve least-privilege-first role selection, built-in-before-custom discipline, the `Microsoft.Authorization/roleAssignments/write` prerequisite, and preference for User Access Administrator over Owner for assignment-only needs. The reviewed package is generate-only and does not execute role assignments or mutate Azure, so unchanged use does not trigger the mutation-authorization hard fail; execution of generated artifacts remains separately authority-gated by the host. Behavioral validation is `not-run`.

The next Microsoft Skills gap must be established from the registered-pin tree after `azure-rbac`.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.