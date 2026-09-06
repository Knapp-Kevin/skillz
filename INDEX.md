# Skill Catalog Snapshot

**Snapshot date:** 2026-09-06

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, and reconciliation.

Canonical inputs are `registry/categories.yaml`, `registry/sources.yaml`, `registry/local-verification.json`, `registry/skills/`, and `registry/verification/`.

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 43 |
| First-party provenance-complete | 43 / 43 |
| Pinned external corpora | 12 |
| Unique registered source identities | 19 |
| Persisted third-party exact-version reviews | 367 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 186 / 186 |
| Microsoft Skills current-standard gaps | 0 |
| Microsoft Azure Skills current-standard companions | 9 / 131 |
| Microsoft Azure Skills current-standard gaps | 122 |
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

AWS is complete at **72/72**. Microsoft Skills is complete at **186/186**. Microsoft Azure Skills is the active admitted-source frontier at **9/131**, with **122** current-standard gaps.

The reconciled Azure companions are `airunway-aks-setup`, verified **17/20**; `appinsights-instrumentation`, rejected unchanged **13/20**; `azure-ai`, rejected unchanged **13/20**; `azure-aigateway`, rejected unchanged **13/20**; `azure-cloud-migrate`, verified **17/20**; `azure-compliance`, rejected unchanged **12/20**; `azure-compute`, rejected unchanged **11/20**; `azure-cost`, rejected unchanged **14/20**; and `azure-deploy`, rejected unchanged **15/20**. `azure-deploy` is bound to package tree `e4d47784cfeba4f942bca41a909c957e65562fd7` and `SKILL.md` blob `23815db4c7c5946913b10ac1cd706ea2bf6727fe`; compatible prior review evidence was reconciled because the exact package identity matches the earlier Microsoft Skills package. Preserve prerequisite validation, target confirmation, conflict detection, destructive/security/cost confirmation, RBAC health checks, recipe selection, recovery, and verification mechanics, but require action-specific authority before post-deployment SQL permission and EF schema-migration changes. Behavioral validation has not been run.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.