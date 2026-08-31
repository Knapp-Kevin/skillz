# Skill Catalog Snapshot

**Snapshot date:** 2026-08-31

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, or reconciliation.

Canonical sources for this snapshot:

- first-party category assignments: [`registry/categories.yaml`](registry/categories.yaml)
- third-party source identities and roles: [`registry/sources.yaml`](registry/sources.yaml)
- first-party review evidence: [`registry/local-verification.json`](registry/local-verification.json)
- provenance companions: [`registry/skills/`](registry/skills/)
- exact-version third-party review evidence: [`registry/verification/`](registry/verification/)

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 43 |
| First-party provenance-complete | 43 / 43 |
| Pinned external corpora | 12 |
| Unique registered source identities | 19 |
| Persisted third-party exact-version reviews | 178 |
| AWS historical reviewed denominator | 72 / 72 |
| AWS current-standard companion-complete | 72 / 72 |
| AWS current-standard gaps | 0 |
| Microsoft Skills current-standard companions | 6 / denominator reconciliation in progress |

## First-party skills by purpose

### Planning & Productivity
- `daily-briefing`
- `decision-log`
- `inbox-triage`
- `learning-plan`
- `task-surface`
- `week-in-review`

### Writing & Communication
- `brief-writer`
- `deck-outline`
- `devlog-draft`
- `handoff-writer`
- `standup-writer`

### Research & Analysis
- `compare`
- `deep-dive`
- `fact-check`
- `paper-digest`

### Software & Repositories
- `repo-doctor`
- `repo-pulse`
- `todo-harvester`

### Agent Operations & Security
- `agent-home-doctor`
- `agent-postmortem`
- `automation-receipts`
- `mcp-vetting`
- `permissions-review`

### Monitoring & Intelligence
- `claude-pulse`
- `deepseek-pulse`
- `gemini-pulse`
- `github-pulse`
- `glm-pulse`
- `governance-pulse`
- `hf-pulse`
- `inference-pulse`
- `kimi-pulse`
- `llama-pulse`
- `mcp-pulse`
- `memory-pulse`
- `mistral-pulse`
- `openai-pulse`
- `perplexity-pulse`
- `qwen-pulse`
- `xai-pulse`

### Business & Career
- `career-radar`
- `finance-review`
- `smallbiz-ops`

## Registered source roles

### Pinned reference corpora
1. `anthropic-skills`
2. `anthropic-knowledge-work-plugins`
3. `vercel-agent-skills`
4. `microsoft-skills`
5. `microsoft-azure-skills`
6. `aws-agent-toolkit`
7. `mattpocock-skills`
8. `addyosmani-agent-skills`
9. `openhands-extensions`
10. `cline-skills`
11. `cloudflare-skills`
12. `google-agents-cli`

### Tracked corpora
- `cole-medin-skills`
- `david-ondrej-skills`
- `bm629-agent-skills`
- `openclaw-agent-skills`
- `archieindian-superpowers`

### Normative / discovery references
- `agentskills-spec` — normative specification
- `github-awesome-copilot` — dynamic discovery surface

## Interpretation

Physical presence or registration does not establish individual skill quality. For unchanged third-party consideration, use the exact-version companion evidence and apply:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

AWS accounting is fully reconciled: **72/72 historical inspection and 72/72 current-standard companion completeness** at the registered pin. Rejected exact versions remain excluded from normal unchanged reuse; completion means every eligible package has decisive current evidence, not that every package passed unchanged.

Microsoft Skills is the active admitted-source frontier. It currently has **6** current-standard exact-version companion pairs persisted at the registered pin. `applicationinsights-web-ts` is rejected unchanged under the privacy/authorization rule; `skill-creator`, `cloud-solution-architect`, `copilot-sdk`, and nested plugin package `azure-identity-dotnet` are verified by structured static review; nested plugin package `azure-ai-document-intelligence-dotnet` is rejected unchanged because custom-model/classifier creation and model deletion lack a distinct affirmative authorization gate and sensitive document transmission lacks a mandatory data-governance precondition. The exact Microsoft eligible denominator is still being reconciled across canonical packages, plugin-hosted skills, nested skills and symlink mirrors, so no completion percentage is claimed. Microsoft Azure Skills follows.

This file has no generator contract. When repository-maintenance work materially changes the live corpus, the external host agent reconciles this snapshot directly from current evidence.