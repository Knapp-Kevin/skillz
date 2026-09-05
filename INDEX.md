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
| Persisted third-party exact-version reviews | 344 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 172 / 189 |
| Microsoft Skills current-standard gaps | 17 |
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

AWS is fully reconciled at **72/72**. Microsoft Skills is active at **172/189**, leaving **17** gaps. Direct `.NET`, Java, Python, Rust, and TypeScript slices are complete.

A 2026-09-05 contract repair restored ten genuinely missing Microsoft YAML companion pairs from the auxiliary Markdown review wave beginning with `kql`. `skill-creator` already had a canonical YAML pair, so its re-review refreshed that pair rather than adding another companion. Canonical counts are derived from `registry/`, not auxiliary review prose.

Latest non-direct Microsoft closure: `wiki-llms-txt` is **rejected unchanged, 15/20**, bound to package tree `b3a045c0f510f263fc05abba5daccaab4efcf164` and `SKILL.md` blob `f9eaf717a42a1206bdde938219f1d8cfbb1c64c4`; freshness is revision `67ae723a23ba880e3e5c8a3e5e2320092024476e` from 2026-04-02. Preserve its spec-aware llms.txt structure, repository-context resolution, evidence-derived summaries, citation/Mermaid/table preservation, unrelated-root-file non-overwrite safeguard, and validation checklist. Unchanged adoption is rejected because it directs persistent creation of three llms.txt artifacts without a mandatory action-specific authorization checkpoint immediately before mutation. Behavioral validation is `not-run`.

The next Microsoft Skills gap should be established from the exact registered-pin `deep-wiki` skill tree after `wiki-llms-txt`; `wiki-onboarding` is next in source order but is not a gap until canonical companions and repository history are checked.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.