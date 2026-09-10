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
| Persisted third-party exact-version reviews | 436 |
| Anthropic Skills current-standard companions | 17 / 17 |
| Anthropic Skills current-standard gaps | 0 |
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
| Cloudflare Skills current-standard companions | 13 / 13 |
| Cloudflare Skills current-standard gaps | 0 |
| Addy Osmani Agent Skills current-standard companions | 24 / 24 |
| Addy Osmani Agent Skills current-standard gaps | 0 |
| Vercel Agent Skills current-standard companions | 9 / 9 |
| Vercel Agent Skills current-standard gaps | 0 |
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

The latest first-party admission is `session-continuity`, statically verified **19/20** with behavioral validation `not-run`.

Current-standard complete admitted families explicitly accounted here are Anthropic Skills **17/17**, AWS **72/72**, Microsoft Skills **186/186**, Microsoft Azure Skills **34/34**, Cole Medin Skills **33/33**, Matt Pocock Skills **29/29**, Cloudflare Skills **13/13**, Addy Osmani Agent Skills **24/24**, and Vercel Agent Skills **9/9**. Each has **0** current-standard gaps at its registered exact pin.

Vercel Agent Skills is pinned at `f8a72b9603728bb92a217a879b7e62e43ad76c81`. The complete pinned tree contains exactly **9** first-class `skills/*/SKILL.md` packages; canonical provenance and verification shelves expose the same **9/9** identities. Historical issue #27 records **6 verified / 3 rejected unchanged**. All live companion paths now resolve under `skills/sources/vercel-agent-skills/`; no companion retains obsolete `vendor/vercel-agent-skills/...` metadata. `vercel-cli-with-tokens` remains rejected unchanged for credential-exposure/solicitation and consequential-operation defects. `web-design-guidelines` and `writing-guidelines` remain rejected unchanged because their governing instructions come from mutable unpinned remote `main` documents outside the recorded exact-version fingerprints. Behavioral validation remains `not-run` across all nine.

The Anthropic Skills family is pinned at `9d2f1ae187231d8199c64b5b762e1bdf2244733d`, with **17/17** companion pairs and historical distribution **10 verified / 7 rejected unchanged**. The Azure denominator is **34**, comprising 28 canonical plugin roots, one nested Kubernetes automatic-readiness package, and five additional nested Foundry packages. Matt Pocock's denominator is **29** after excluding `deprecated` and `in-progress`. Cloudflare remains **13/13**, with `web-perf` and `wrangler` intentionally rejected unchanged. Addy Osmani remains **24/24**, with compatible historical evidence recovered only where exact fingerprints matched the registered pinned tree.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.
