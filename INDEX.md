# Skill Catalog Snapshot

**Snapshot date:** 2026-09-09

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, and reconciliation.

Canonical inputs are `registry/categories.yaml`, `registry/sources.yaml`, `registry/local-verification.json`, `registry/skills/`, and `registry/verification/`.

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 44 |
| First-party provenance-complete | 44 / 44 |
| Pinned external corpora | 12 |
| Unique registered source identities | 19 |
| Persisted third-party exact-version reviews | 422 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 186 / 186 |
| Microsoft Skills current-standard gaps | 0 |
| Microsoft Azure Skills current-standard companions | 34 / 34 |
| Microsoft Azure Skills current-standard gaps | 0 |
| Cole Medin Skills current-standard companions | 33 / 33 |
| Cole Medin Skills current-standard gaps | 0 |
| Matt Pocock Skills current-standard companions | 29 / 29 |
| Matt Pocock Skills current-standard gaps | 0 |
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
`agent-home-doctor`, `agent-postmortem`, `automation-receipts`, `mcp-vetting`, `permissions-review`, `session-continuity`

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

The latest first-party admission is `session-continuity`, statically verified **19/20** with behavioral validation `not-run`. It is a substrate-agnostic continuity procedure: relevant recall is scoped and read-only, prior memory does not authorize new actions, and persistent continuity capture requires current or standing authority with secret and sensitive-data minimization.

AWS is complete at **72/72**. Microsoft Skills is complete at **186/186**. Microsoft Azure Skills is complete at **34/34**, with **0** current-standard gaps. Cole Medin Skills is complete at **33/33**, with **0** gaps. Matt Pocock Skills is complete at **29/29**, with **0** gaps after excluding `deprecated` and `in-progress` per source policy.

The Azure denominator is the exact set of independently eligible `SKILL.md` packages at registered pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`: 28 canonical plugin skill roots, one nested Kubernetes automatic-readiness package, and five nested Foundry packages beyond the Foundry root. Ordinary workflow, procedure, reference, example, and SDK Markdown is retained as package evidence but does not count as an independent skill.

The final Cole reconciliation is `worktree-merge`, rejected unchanged **15/20**, bound to package tree `150cb167cb6c0bd703e3ba5b05330aa7f9db9861` and `SKILL.md` blob `9912484e1f99ce5ae7f5fd25f88a3d60f3e61c2b`. Behavioral validation has not been run. Its disposable integration-branch staging, repository-detected validation, per-branch test localization, conflict stop, full-suite gate, rollback guidance, and explicit cleanup choice are useful adaptation/extraction evidence. Unchanged use remains rejected because it creates and merges branches, including the final merge into the original branch, without mandatory action-specific authorization immediately before mutation, and because repository-controlled CI workflows, Makefiles, manifests, and discovered validation commands lack an explicit hostile-instruction boundary.

The Matt Pocock family is pinned at `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`; provenance and verification expose matching 29-file companion sets, and live companion metadata contains no obsolete `vendor/mattpocock-skills/...` path.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.
