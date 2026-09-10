# Skill Catalog Snapshot

**Snapshot date:** 2026-09-10

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, and reconciliation.

Canonical inputs are `registry/categories.yaml`, `registry/sources.yaml`, `registry/local-verification.json`, `registry/skills/`, and `registry/verification/`.

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 44 |
| First-party provenance-complete | 44 / 44 |
| Pinned external corpora | 12 |
| Unique registered source identities | 19 |
| Persisted third-party exact-version reviews | 553 |
| Anthropic Skills current-standard companions | 17 / 17 |
| Anthropic Knowledge Work Plugins current-standard companions | 74 / 74 |
| Anthropic Knowledge Work Plugins current-standard gaps | 0 |
| AWS current-standard companion-complete | 72 / 72 |
| Microsoft Skills current-standard companions | 186 / 186 |
| Microsoft Azure Skills current-standard companions | 34 / 34 |
| Cole Medin Skills current-standard companions | 33 / 33 |
| David Ondrej Skills current-standard companions | 16 / 55 |
| David Ondrej Skills current-standard gaps | 39 |
| Matt Pocock Skills current-standard companions | 29 / 29 |
| Cloudflare Skills current-standard companions | 13 / 13 |
| Addy Osmani Agent Skills current-standard companions | 24 / 24 |
| Vercel Agent Skills current-standard companions | 9 / 9 |
| OpenHands Extensions current-standard companions | 1 / 1 |
| OpenHands Extensions current-standard gaps | 0 |
| Google Agents CLI current-standard companions | 7 / 7 |
| Google Agents CLI current-standard gaps | 0 |
| Cline Skills published current-standard companions | 36 / 36 |
| Cline Skills published current-standard gaps | 0 |
| Microsoft .NET direct-package companions | 29 / 29 |
| Microsoft Java direct-package companions | 26 / 26 |
| Microsoft Python direct-package companions | 40 / 40 |
| Microsoft Rust direct-package companions | 9 / 9 |
| Microsoft TypeScript direct-package companions | 25 / 25 |

Every explicitly current-standard-complete family above has **0** current-standard gaps at its registered exact pin. David Ondrej Skills is tracked and only partially curated.

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

Anthropic Knowledge Work Plugins is current-standard complete for its exact **74-skill denominator** at registered pin `ca3e3fb2c4a1d3eea73fc003998faef6daa650b8`. Package-level companions recovered from superseded PR #42 preserve **36 verified / 38 rejected unchanged** historical dispositions and do not infer behavioral validation.

David Ondrej Skills is tracked at pin `7d0ef87dad1f638cab58995eead9e0e6e3fae237`, with **55** first-class packages. Current companions cover **16/55**, leaving **39** gaps and decisive states **9 verified / 7 rejected unchanged**. Skill authoring is **4/4** complete; agent orchestration is **12/17** reviewed. The prior 10/17 subtotal omitted the already reviewed `goal-loop`. Newly reviewed `handoff` is verified 18/20 because implicit invocation is disabled in both skill and bundled OpenAI policy, handoff content must redact secrets and PII, claims are framed for verification rather than blind trust, and its default write is limited to a temporary handoff file. Behavioral validation remains `not-run`.

OpenHands Extensions is current-standard complete for its exact **1-skill denominator** at registered pin `87959a7da3e75445647e77b2fbf5bf5b66fb037b`. `theme-factory` remains **rejected unchanged 14/20** with behavioral validation `not-run`.

Cline Skills is current-standard complete for its finite **36-skill published denominator** at registered pin `26378461e978f2b4e2e6d67b57121b86b2a79ba5`; the separate internal/unlisted `review-team` record is outside that denominator.

Other explicitly complete families remain Anthropic Skills **17/17**, AWS **72/72**, Microsoft Skills **186/186**, Microsoft Azure Skills **34/34**, Cole Medin Skills **33/33**, Matt Pocock Skills **29/29**, Cloudflare Skills **13/13**, Addy Osmani Agent Skills **24/24**, Vercel Agent Skills **9/9**, OpenHands Extensions **1/1**, Google Agents CLI **7/7**, and Cline Skills **36/36 published**.

This file has no generator contract. Under explicit repository-maintenance authority, the external host agent reconciles this snapshot directly from live evidence.