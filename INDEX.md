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
| Persisted third-party exact-version reviews | 371 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 186 / 186 |
| Microsoft Skills current-standard gaps | 0 |
| Microsoft Azure Skills current-standard companions | 13 / 131 |
| Microsoft Azure Skills current-standard gaps | 118 |
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

AWS is complete at **72/72**. Microsoft Skills is complete at **186/186**. Microsoft Azure Skills is the active admitted-source frontier at **13/131**, with **118** current-standard gaps.

The reconciled Azure companions are `airunway-aks-setup`, verified **17/20**; `appinsights-instrumentation`, rejected unchanged **13/20**; `azure-ai`, rejected unchanged **13/20**; `azure-aigateway`, rejected unchanged **13/20**; `azure-cloud-migrate`, verified **17/20**; `azure-compliance`, rejected unchanged **12/20**; `azure-compute`, rejected unchanged **11/20**; `azure-cost`, rejected unchanged **14/20**; `azure-deploy`, rejected unchanged **15/20**; `azure-diagnostics`, rejected unchanged **13/20**; `azure-enterprise-infra-planner`, verified **18/20**; `azure-hosted-copilot-sdk`, rejected unchanged **13/20**; and `azure-kubernetes`, rejected unchanged **12/20**. `azure-kubernetes` is bound to package tree `bab7f5eab9e8e1c311ef1fc29b419963903fbe09` and `SKILL.md` blob `3c5a448a679dafed5e0e747d28bd95cead4e8dec`; exact identity matches the completed Microsoft Skills package, so compatible complete-package review evidence was reconciled rather than repeated. Preserve Day-0/Day-1 framing, conservative AKS Automatic defaults, security/reliability guidance, secret non-disclosure, and scenario deep dives. Unchanged adoption fails because bundled CLI guidance performs consequential cluster creation/configuration without action-specific approval immediately before mutation. Behavioral validation has not been run. The nested `azure-kubernetes-automatic-readiness` remains independently eligible.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.