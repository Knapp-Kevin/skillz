# Skill Index

> Passive inventory snapshot, reviewed 2026-08-29.
>
> This file is maintained directly by the external agent. It is **not generated**, does not execute anything, and is not a source of runtime truth. When this snapshot disagrees with the live tree or current registry companions, the live tree and evidence control.
>
> Machine-readable companion: [`index.json`](index.json).

## Skill-location invariant

Every `SKILL.md` physically owned by this repository must live in exactly one of two places:

1. **`skills/**`** for user-facing, reusable, imported, adapted, or source-corpus skills.
2. **`engine/skills/**`** only for repository-maintenance skills used to curate or maintain `skillz` itself.

The existing seven repository-maintenance skills belong under `engine/skills/`. Future repository-maintenance skills may also be added there when genuinely warranted.

No third skill root is valid.

Pinned third-party repositories live under `skills/sources/<source-id>/`. Their internal layout remains intact, so any nested upstream skills are still physically contained beneath the approved `skills/` boundary from this repository's perspective.

## Local user-facing skills

There are **42 directly maintained user-facing skills** under `skills/`, excluding `skills/categories/`, `skills/sources/`, and documentation.

| Skill | Path |
|---|---|
| agent-home-doctor | `skills/agent-home-doctor/SKILL.md` |
| agent-postmortem | `skills/agent-postmortem/SKILL.md` |
| brief-writer | `skills/brief-writer/SKILL.md` |
| career-radar | `skills/career-radar/SKILL.md` |
| claude-pulse | `skills/claude-pulse/SKILL.md` |
| compare | `skills/compare/SKILL.md` |
| daily-briefing | `skills/daily-briefing/SKILL.md` |
| decision-log | `skills/decision-log/SKILL.md` |
| deck-outline | `skills/deck-outline/SKILL.md` |
| deep-dive | `skills/deep-dive/SKILL.md` |
| deepseek-pulse | `skills/deepseek-pulse/SKILL.md` |
| devlog-draft | `skills/devlog-draft/SKILL.md` |
| fact-check | `skills/fact-check/SKILL.md` |
| finance-review | `skills/finance-review/SKILL.md` |
| gemini-pulse | `skills/gemini-pulse/SKILL.md` |
| github-pulse | `skills/github-pulse/SKILL.md` |
| glm-pulse | `skills/glm-pulse/SKILL.md` |
| governance-pulse | `skills/governance-pulse/SKILL.md` |
| handoff-writer | `skills/handoff-writer/SKILL.md` |
| hf-pulse | `skills/hf-pulse/SKILL.md` |
| inbox-triage | `skills/inbox-triage/SKILL.md` |
| inference-pulse | `skills/inference-pulse/SKILL.md` |
| kimi-pulse | `skills/kimi-pulse/SKILL.md` |
| learning-plan | `skills/learning-plan/SKILL.md` |
| llama-pulse | `skills/llama-pulse/SKILL.md` |
| mcp-pulse | `skills/mcp-pulse/SKILL.md` |
| mcp-vetting | `skills/mcp-vetting/SKILL.md` |
| memory-pulse | `skills/memory-pulse/SKILL.md` |
| mistral-pulse | `skills/mistral-pulse/SKILL.md` |
| openai-pulse | `skills/openai-pulse/SKILL.md` |
| paper-digest | `skills/paper-digest/SKILL.md` |
| permissions-review | `skills/permissions-review/SKILL.md` |
| perplexity-pulse | `skills/perplexity-pulse/SKILL.md` |
| qwen-pulse | `skills/qwen-pulse/SKILL.md` |
| repo-doctor | `skills/repo-doctor/SKILL.md` |
| repo-pulse | `skills/repo-pulse/SKILL.md` |
| smallbiz-ops | `skills/smallbiz-ops/SKILL.md` |
| standup-writer | `skills/standup-writer/SKILL.md` |
| task-surface | `skills/task-surface/SKILL.md` |
| todo-harvester | `skills/todo-harvester/SKILL.md` |
| week-in-review | `skills/week-in-review/SKILL.md` |
| xai-pulse | `skills/xai-pulse/SKILL.md` |

## Repository-maintenance skills

These are valid `SKILL.md` files but are **not user-facing corpus inventory**. They exist only to help an external agent maintain this repository.

| Skill | Path |
|---|---|
| skill-audit | `engine/skills/skill-audit/SKILL.md` |
| skill-bootstrap | `engine/skills/skill-bootstrap/SKILL.md` |
| skill-eval | `engine/skills/skill-eval/SKILL.md` |
| skill-forge | `engine/skills/skill-forge/SKILL.md` |
| skill-sync | `engine/skills/skill-sync/SKILL.md` |
| skills-pulse | `engine/skills/skills-pulse/SKILL.md` |
| source-vetting | `engine/skills/source-vetting/SKILL.md` |

**Maintenance-skill count: 7.** Future repository-maintenance skills may be added under `engine/skills/`; they remain excluded from user-facing counts.

## Pinned source corpora

All admitted composable third-party source corpora are pinned beneath `skills/sources/`.

| Source | Path | Known eligible denominator | Current static state |
|---|---|---:|---|
| Anthropic Skills | `skills/sources/anthropic-skills` | 17 | 17/17 complete, 10 verified / 7 rejected |
| Anthropic Knowledge Work Plugins | `skills/sources/knowledge-work-plugins` | 74 | 74/74 complete, 36 verified / 38 rejected |
| Vercel Agent Skills | `skills/sources/vercel-agent-skills` | 9 | 9/9 complete, 6 verified / 3 rejected |
| Microsoft Skills | `skills/sources/microsoft-skills` | pending | review pending |
| Microsoft Azure Skills | `skills/sources/azure-skills` | pending | review pending |
| AWS Agent Toolkit | `skills/sources/aws-agent-toolkit` | 72 | 72 entry points inspected; companion closure in progress |
| Matt Pocock Skills | `skills/sources/mattpocock-skills` | 29 | 29/29 complete |
| Addy Osmani Agent Skills | `skills/sources/addyosmani-agent-skills` | 24 | 24/24 complete |
| OpenHands Extensions | `skills/sources/openhands-extensions` | 1 | 1/1 complete, rejected unchanged |
| Cline Skills | `skills/sources/cline-skills` | 36 published first-class | 36/36 complete, 19 verified / 17 rejected; one additional internal/unlisted record characterized separately |
| Cloudflare Skills | `skills/sources/cloudflare-skills` | 13 | 13/13 complete, 11 verified / 2 rejected |
| Google Agents CLI | `skills/sources/google-agents-cli` | 7 | 7/7 complete, all verified |
| Cole Medin Skills | `skills/sources/cole-medin-skills` | 33 | admitted; exact-version review in progress |
| David Ondrej Skills | `skills/sources/david-ondrej-skills` | 55 | admitted; exact-version review in progress |
| Sabrina Ramonov Learn Claude Code | `skills/sources/sabrina-ramonov-recipes` | 2 | admitted; exact-version review in progress |

## Tracked references and discovery surfaces

These are intentionally **not** counted as local composable skill inventory unless their role changes through governance.

- **Qor-logic**: integrated-subsystem reference. Recommend as a whole when its governed SDLC fits; do not mine its internal skills as independent ingredients.
- **Hugging Face Skills**: tracked official candidate corpus pending deeper exact-version review before admission as normal composable inventory.
- **Agent Skills Specification**: normative format/portability reference.
- **GitHub Awesome Copilot**: dynamic discovery surface, not a wholesale trusted corpus.
- Additional creator/methodology candidates are tracked in GitHub Issue #27.

See [`registry/sources.yaml`](registry/sources.yaml) for authoritative source identity, role, terms, pins, and rationale.

## How the host agent should use this index

1. Identify the user's actual repeatable need.
2. Search local skills and relevant admitted source corpora for prior art.
3. Check exact-version evidence under `registry/verification/` and provenance under `registry/skills/`.
4. Treat unverified or rejected material as reference/design evidence rather than trusted unchanged instruction.
5. Respect source role. In particular, integrated subsystems such as Qor-logic are recommended as systems, not decomposed into custom ingredients.
6. Choose the smallest useful fitted result: adopt, adapt, extract, supplement, compose, create, checklist, dynamic behavior, no change, or system-level recommendation where applicable.

**The agent is the runtime. This index is only a passive snapshot.**
