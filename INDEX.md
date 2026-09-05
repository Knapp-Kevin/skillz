# Skill Catalog Snapshot

**Snapshot date:** 2026-09-05

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, or reconciliation.

Canonical inputs are `registry/categories.yaml`, `registry/sources.yaml`, `registry/local-verification.json`, `registry/skills/`, and `registry/verification/`.

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 43 |
| First-party provenance-complete | 43 / 43 |
| Pinned external corpora | 12 |
| Unique registered source identities | 19 |
| Persisted third-party exact-version reviews | 354 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 182 / 189 |
| Microsoft Skills current-standard gaps | 7 |
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

AWS is fully reconciled at **72/72**. Microsoft Skills is active at **182/189**, leaving **7** gaps. Direct `.NET`, Java, Python, Rust, and TypeScript slices are complete.

A 2026-09-05 contract repair restored ten genuinely missing Microsoft YAML companion pairs from the auxiliary Markdown review wave beginning with `kql`. `skill-creator` already had a canonical YAML pair, so its re-review refreshed that pair rather than adding another companion. Canonical counts are derived from `registry/`, not auxiliary review prose.

Latest non-direct Microsoft closure: `ui-widget-developer` is **rejected unchanged, 11/20**, bound to package tree `782d9f253d9bf51bf98a274d6c4e0d262bc1b54c` and `SKILL.md` blob `1240df9af50396f6420e83ea7fad62a920edbbb0`; freshness is revision `a43d2c6a69fac2298ac0f301419931b39d996c6b` from 2026-06-15. Preserve OAI Apps versus MCP Apps routing, MCP resource/widget protocol guidance, React + Fluent UI constraints, MCP Inspector schema synchronization, local widget links, E2E/health verification, and delegation boundaries. Unchanged adoption fails the authority hard rule because it mandates automatic plugin/package/tool installation, authentication, detached service/devtunnel startup, filesystem mutation, public tunnel exposure, tenant/AAD provisioning, and auto-deployment without distinct action-specific authorization checkpoints. Behavioral validation is `not-run`.

The `microsoft-365-agents-toolkit` family is now companion-complete. Establish the next genuine Microsoft Skills gap from the exact registered-pin source tree before review.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.