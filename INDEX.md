# Skill Catalog Snapshot

**Snapshot date:** 2026-09-29

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, and reconciliation.

Canonical inputs are `registry/categories.yaml`, `registry/sources.yaml`, `registry/local-verification.json`, `registry/skills/`, and `registry/verification/`.

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 44 |
| First-party provenance-complete | 44 / 44 |
| Pinned external corpora | 12 |
| Unique registered source identities | 21 |
| Persisted third-party exact-version reviews | 650 |
| Jwynia Agent Skills selectively reviewed units | 8 |
| Anthropic Skills current-standard companions | 17 / 17 |
| Anthropic Knowledge Work Plugins current-standard companions | 74 / 74 |
| AWS current-standard companion-complete | 72 / 72 |
| Microsoft Skills current-standard companions | 186 / 186 |
| Microsoft Azure Skills current-standard companions | 34 / 34 |
| Cole Medin Skills current-standard companions | 33 / 33 |
| David Ondrej Skills current-standard companions | 55 / 55 |
| Corey Haines Marketing Skills current-standard companions | 50 / 50 |
| Matt Pocock Skills current-standard companions | 29 / 29 |
| Cloudflare Skills current-standard companions | 13 / 13 |
| Addy Osmani Agent Skills current-standard companions | 24 / 24 |
| Vercel Agent Skills current-standard companions | 9 / 9 |
| OpenHands Extensions current-standard companions | 1 / 1 |
| Google Agents CLI current-standard companions | 7 / 7 |
| Cline Skills published current-standard companions | 36 / 36 |

Every explicitly current-standard-complete family above has **0** current-standard gaps at its registered exact pin. Selectively tracked corpora are bounded to the individually governed units and are not silently treated as whole-family complete.

`jwynia/agent-skills` is tracked at `e02ec7e226a6e4f8419fd3b88a1d8e472d421b32` for selective curation. Eight units are now governed: `story-collaborator`, `story-sense`, `story-zoom`, `worldbuilding`, `character-arc`, `dialogue`, `scene-sequencing`, and `prose-style`. Six of the seven-unit follow-up tranche are VERIFIED; `story-zoom` is REJECTED unchanged because persistent `story-state/` mutation and a background watcher daemon lack an action-appropriate authorization boundary. Behavioral validation remains `not-run`.

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

**Tracked corpora:** `cole-medin-skills`, `david-ondrej-skills`, `bm629-agent-skills`, `openclaw-agent-skills`, `archieindian-superpowers`, `corey-haines-marketing-skills`, `jwynia-agent-skills`.

**Normative/discovery:** `agentskills-spec` is a normative specification; `github-awesome-copilot` is a dynamic discovery surface.

## Interpretation

Physical presence, registration, or a `verified` static review does not by itself establish behavioral validation or automatic unchanged-use eligibility. For unchanged third-party consideration, use exact-version companion evidence and apply:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**