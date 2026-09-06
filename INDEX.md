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
| Persisted third-party exact-version reviews | 370 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 186 / 186 |
| Microsoft Skills current-standard gaps | 0 |
| Microsoft Azure Skills current-standard companions | 12 / 131 |
| Microsoft Azure Skills current-standard gaps | 119 |
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

AWS is complete at **72/72**. Microsoft Skills is complete at **186/186**. Microsoft Azure Skills is the active admitted-source frontier at **12/131**, with **119** current-standard gaps.

The reconciled Azure companions are `airunway-aks-setup`, verified **17/20**; `appinsights-instrumentation`, rejected unchanged **13/20**; `azure-ai`, rejected unchanged **13/20**; `azure-aigateway`, rejected unchanged **13/20**; `azure-cloud-migrate`, verified **17/20**; `azure-compliance`, rejected unchanged **12/20**; `azure-compute`, rejected unchanged **11/20**; `azure-cost`, rejected unchanged **14/20**; `azure-deploy`, rejected unchanged **15/20**; `azure-diagnostics`, rejected unchanged **13/20**; `azure-enterprise-infra-planner`, verified **18/20**; and `azure-hosted-copilot-sdk`, rejected unchanged **13/20**. `azure-hosted-copilot-sdk` is bound to package tree `ee166d12b8f9a88a1d4d932a23e844d8203efa13` and `SKILL.md` blob `64b239df00aa320b64a9009c1875b303a87080b1`; exact identity matches the current Microsoft Skills package, so compatible complete-package review evidence was reconciled rather than repeated. Preserve its SDK-aware routing, temp-directory scaffolding safeguard, managed-identity/passwordless guidance, secure GitHub-token/Key Vault flow, and BYOM references. Unchanged adoption fails the authority hard rule because troubleshooting can expand GitHub credential scope through `gh auth refresh --scopes copilot` without a mandatory action-specific approval immediately before mutation, and the deployment path inherits the currently rejected exact-version `azure-deploy` package without a compensating boundary. Behavioral validation has not been run.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.