# Skill Catalog Snapshot

**Snapshot date:** 2026-09-08

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, and reconciliation.

Canonical inputs are `registry/categories.yaml`, `registry/sources.yaml`, `registry/local-verification.json`, `registry/skills/`, and `registry/verification/`.

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 43 |
| First-party provenance-complete | 43 / 43 |
| Pinned external corpora | 12 |
| Unique registered source identities | 19 |
| Persisted third-party exact-version reviews | 413 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 186 / 186 |
| Microsoft Skills current-standard gaps | 0 |
| Microsoft Azure Skills current-standard companions | 34 / 34 |
| Microsoft Azure Skills current-standard gaps | 0 |
| Cole Medin Skills current-standard companions | 24 / 33 |
| Cole Medin Skills current-standard gaps | 9 |
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

AWS is complete at **72/72**. Microsoft Skills is complete at **186/186**. Microsoft Azure Skills is complete at **34/34**, with **0** current-standard gaps. Cole Medin Skills is the active frontier at **24/33**, with **9** gaps.

The Azure denominator is the exact set of independently eligible `SKILL.md` packages at registered pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`: 28 canonical plugin skill roots, one nested Kubernetes automatic-readiness package, and five nested Foundry packages beyond the Foundry root. Ordinary workflow, procedure, reference, example, and SDK Markdown is retained as package evidence but does not count as an independent skill.

The latest Cole reconciliation is `prime-backend`, rejected unchanged **16/20**, bound to package tree `3b4d38dbee11e02ec4f9edb02f1f2ce18ed0e91e` and `SKILL.md` blob `f42e8ee67b35027ffe4e580ff82b41b363e5a6f0`. Behavioral validation has not been run. Its backend-scoped context loading, representative feature-slice sampling, current-state inspection, architecture summarization, and context-window discipline are useful adaptation/extraction evidence. Unchanged use remains rejected because Jira/Confluence and repository-controlled content lack an explicit hostile-instruction boundary, and externally retrieved task material can be summarized without mandatory secret/PII/sensitive-data minimization or redaction.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.