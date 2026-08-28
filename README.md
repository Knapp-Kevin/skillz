# 🛠️ skillz

[![CI](https://github.com/Knapp-Kevin/skillz/actions/workflows/ci.yml/badge.svg)](https://github.com/Knapp-Kevin/skillz/actions/workflows/ci.yml)
![Skills](https://img.shields.io/badge/first--party_skills-49-blue)
![Sources](https://img.shields.io/badge/reference_sources-7-8A2BE2)
![Runtime](https://img.shields.io/badge/runtime-Bun_%7C_Node_22.18%2B-brightgreen)
![Install](https://img.shields.io/badge/install-zero-success)

**A portable skill library that helps AI systems learn better ways to work with you.**

## New here? Start here.

You do not need to know what an AI skill is.

You do not need to choose from hundreds of files.

You do not need to be a programmer.

Give your AI this repository and point it to **[BOOTSTRAP.md](BOOTSTRAP.md)**.

The bootstrap process helps your AI:

1. look at the work, history, memory, files, tools, and instructions it can actually access,
2. notice things you do again and again,
3. find skills in this repository that already help with those things,
4. improve or combine existing skills when that is better than starting over,
5. create a new skill only when something useful is truly missing,
6. test whether those skills actually make the AI more dependable, and
7. save the important working rules in a portable form that can help another compatible AI later.

In plain language: **instead of teaching every AI the same lessons over and over, turn the useful lessons into reusable skills.**

> **Beginner path:** [BOOTSTRAP.md](BOOTSTRAP.md)
>
> **Already know which skill you need?** Use [INDEX.md](INDEX.md) or [index.json](index.json).

---

## What is in this repository?

The repository contains first-party skills plus a curated reference library from official and selected community sources. It also contains the tools for discovering, comparing, testing, creating, auditing, and moving those skills between supported agent hosts.

The goal is not to collect the most skills. The goal is to help an agent find the **smallest useful set** for the person or system it is helping.

Reference skills do not automatically become trusted or authoritative. Agents compare them against the target workflow and may adopt, adapt, supplement, compose, benchmark, or reject them.

Third-party work keeps its attribution and license information. See [docs/third-party-provenance.md](docs/third-party-provenance.md) and [registry/sources.yaml](registry/sources.yaml).

## Quick start

### Beginner or first-time setup

Give your agent this instruction:

```
Read BOOTSTRAP.md and help me figure out which skills would make you better at helping me.
```

The full orchestration procedure lives in [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md).

### Claude Code: use a known skill directly

```
Read G:\MythologIQ\skillz\INDEX.md, then run the claude-pulse skill.
```

### Claude Code: install a skill permanently

```powershell
# personal (all projects)
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\claude-pulse" -Target "G:\MythologIQ\skillz\skills\claude-pulse"
# or deploy everything portable at once:
node skills/skill-sync/scripts/sync.ts --claude-user --apply
```

### Any other agent

Point it at the relevant `SKILL.md` and instruct it to follow the skill's execution flow. Skills are plain Markdown plus optional zero-install scripts using Bun or Node 22.18+. No framework is required.

### Clone with the vendored references

```
git clone --recurse-submodules <url>
```

## Skill series

49 first-party skills across seven series:

| Series | Skills | Cadence |
|--------|--------|---------|
| **Pulse** (17) | 11 vendor pulses (claude, openai, gemini, llama, mistral, xai, deepseek, qwen, glm, kimi, perplexity) + 6 topic pulses (`governance`, `memory`, `github`, `hf`, `mcp`, `inference`), all driven by one engine (`scripts/pulse-run.ts`) with per-skill `sources.json`; adding a pulse is a data change | weekly |
| **Research** (5) | `deep-dive`, `compare`, `fact-check`, `paper-digest`, `source-vetting`, structured inquiry with adversarial fact-checking and registry-ready verdicts | on demand |
| **Agent-ops** (5) | `skill-eval`, `mcp-vetting`, `agent-postmortem`, `handoff-writer`, `permissions-review`, running the agent fleet itself | on demand / monthly |
| **Daily-ops** (5) | `daily-briefing`, `inbox-triage`, `standup-writer`, `week-in-review`, `task-surface` (forge + operate a cross-org task-coordination repo, bound to its own governance doc), draft-only for anything that sends or writes | daily / weekly |
| **Comms & life** (8) | `brief-writer`, `decision-log`, `devlog-draft`, `deck-outline`, `finance-review`, `smallbiz-ops`, `career-radar`, `learning-plan` | on demand / monthly |
| **Repo hygiene** (3) | `repo-pulse`, `repo-doctor`, `todo-harvester`, `gh`/git-evidence based, read-only punch lists | weekly / on demand |
| **Meta** (6) | `skill-bootstrap` (personal skill discovery/onboarding), `skills-pulse` (ecosystem intake + source freshness), `skill-audit` (two-layer self-validation), `skill-sync` (deployment), `skill-forge` (scaffolding), `agent-home-doctor` (agent CLI home audit/cleanup) | onboarding / weekly / pre-commit / as-needed |

## Skill index

[INDEX.md](INDEX.md) and [index.json](index.json) are the canonical catalog: every local skill plus the indexed contents of the vendored reference corpus. Agents should resolve skills through the index rather than globbing the tree.

They are **generated, never edit them by hand**. After adding or changing a skill or reference source:

```
node scripts/build-index.ts
```

The generator scans `skills/*/SKILL.md` frontmatter and the allowed vendor/reference trees. Source trust classification lives in [registry/sources.yaml](registry/sources.yaml).

## Repository layout

```
BOOTSTRAP.md                 # beginner and agent onboarding entry point
INDEX.md / index.json        # generated skill index
skills/                      # 49 first-party skills
  skill-bootstrap/           # user-specific skill discovery/orchestration
  <vendor>-pulse/            # 11 vendor + 6 topic pulses
  deep-dive/ compare/ ...    # research series
  skill-eval/ mcp-vetting/ … # agent-ops series
  daily-briefing/ ...        # daily-ops series
  brief-writer/ decision-log/# comms & life
  skills-pulse/ skill-audit/ # meta series
  skill-sync/ skill-forge/
registry/
  candidates.yaml            # per-skill intake decisions
  sources.yaml               # reference-source trust + provenance classes
vendor/                      # pinned official + community-vetted source repos
scripts/
  build-index.ts             # index generator
  pulse-run.ts               # shared pulse collector
  lib/frontmatter.ts         # shared zero-dep frontmatter parser
tests/                       # behavior tests
.github/workflows/ci.yml     # CI: tests + audit + risk audit + index freshness
docs/
  portable-skill-profile.md  # cross-host user execution profile
  third-party-provenance.md  # attribution + adaptation rules
  skill-template.md          # local authoring scaffold
  evaluation-framework.md    # adoption/evaluation framework
ROADMAP.md                   # series status + design rules + portability contract
```

## Validation: two layers, both enforced

1. **Structural**: [`skill-audit`](skills/skill-audit/SKILL.md) (`scripts/audit.ts`) checks frontmatter conventions, script `--help` health, pulse-spec parsing, registry enums, and index freshness. Exit 1 means drift.
2. **Semantic risk**: `scripts/risk-audit.ts` catches structurally valid skills that still induce dangerous behavior. It fails high-judgment skills missing negative-rule classes (secret handling, anti-fabrication, missing-evidence fallback) and mutating actions without approval language, and warns on portable-skill operator specifics and vendor-API references without an MCP/web fallback.

Both run in CI on every PR and push to main alongside the behavior suite and index-idempotency diff. The risk layer caught six real gaps on its first live run, which is a nice reminder that syntax can be perfect while the bottle still contains poison.

## How this stays lean

The repo covers local, cloud, and cross-host agent work without becoming a junk drawer by drawing four lines:

1. **Centralize intentionally.** Official sources are preferred for vendor/platform capabilities. Selected community repositories may also be vendored when they add strong comparative or supplemental value and licensing/provenance permit it. Source class is explicit in `registry/sources.yaml`.
2. **Every third-party skill is still a decision.** [`registry/candidates.yaml`](registry/candidates.yaml) records adopt/sandbox/track/reject/quarantine decisions with permission tiers and rationale. Being present in `vendor/` makes a skill available for comparison; it does not automatically authorize use.
3. **Intake is a cadence skill.** [`skills-pulse`](skills/skills-pulse/SKILL.md) scans the watchlist, filters finds against the registry/index/gated registry/built-ins, reports upstream drift, and proposes candidates. It never installs anything.
4. **The repo maintains itself.** The audit layers plus [`skill-sync`](skills/skill-sync/SKILL.md) keep validation and distribution mechanical.

## Authoring a skill

Start from [docs/skill-template.md](docs/skill-template.md). Conventions enforced by the audit layers include:

- `skills/<name>/SKILL.md` is the single source of truth. Frontmatter `name` matches the directory, and `description` states both what it does and when to use it.
- **Script collects, model synthesizes.** Scripts fetch and structure; judgment stays in instructions. Most skills need no script.
- Scripts run on Bun or Node 22.18+ with no install step, and every scripted source documents a pure web-tool fallback.
- Read-only by default. Anything that mutates external state requires explicit approval as appropriate to the target environment.
- **Adaptive frameworks, not configurations.** Skills ship the framework; operator/org/environment specifics live in bound governance documents discovered at runtime. No hardcoded operator values in portable skill bodies.
- **Negative rules ship with the scaffold.** High-judgment skills carry explicit prohibitions against reproducing secrets, fabricating missing evidence, or turning inference into fact.
- Declare a capability floor as data when evidence supports it: `metadata.min-model-capability: haiku|sonnet|opus`.
- Recurring skills include a Scheduling section.
- If a local skill copies or materially adapts third-party work, preserve provenance per [docs/third-party-provenance.md](docs/third-party-provenance.md).
- Finish by regenerating the index.

The full portability contract is in [ROADMAP.md](ROADMAP.md#portability-contract-system-agnostic-requirements).

## Vendored reference sources

The repository currently includes six official source repositories and one community-vetted source repository as pinned submodules.

| Source | Class | Coverage |
|--------|-------|----------|
| [anthropics/skills](https://github.com/anthropics/skills) | official | Office docs, skill-creator, MCP builder, frontend design, webapp testing |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | official | Knowledge-work marketplace: productivity, sales, finance, legal, data, design, partner plugins |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | official | React/Next.js best practices, composition patterns, web design guidelines |
| [microsoft/skills](https://github.com/microsoft/skills) | official | Microsoft ecosystem: M365, Foundry, dev tooling |
| [microsoft/azure-skills](https://github.com/microsoft/azure-skills) | official | Azure plan/validate/deploy, RBAC, cost, diagnostics, AKS |
| [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | official | AWS core services, Bedrock agents, analytics, DevSecOps |
| [mattpocock/skills](https://github.com/mattpocock/skills) | community-vetted | Engineering and productivity skill patterns used for comparison, adaptation, supplementation, composition, and benchmarking |

Pins are refreshed deliberately, never automatically. [docs/vendor-freshness.md](docs/vendor-freshness.md) defines the review-first workflow. **Vendored does not mean blanket-trusted.** Write-tier skills, community skills, and source updates still receive the permission, redundancy, and behavioral evaluation appropriate to their impact.

Matt Pocock's repository is MIT-licensed and is included as an attributed source. Local skills that copy or materially adapt third-party work must preserve required notices and record their relationship to the upstream source.

Marketplace-listed Anthropic plugins can also install straight from source:

```
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install productivity@knowledge-work-plugins
```

## Governed development

Changes to this repository's tooling go through the Qor-logic S.H.I.E.L.D. lifecycle: planned, adversarially audited to a binding PASS/VETO, implemented against the sealed plan, and substantiated before merge. The governance record lives in `docs/`. The skills themselves remain ungated. Governance applies to building the repository, not to merely running a normal skill.

## Positioning in the MythologIQ ecosystem

This repo is the **ungated, system-agnostic** skill library. It deliberately does not overlap with:

- **[Qor-logic](../Qor-logic)**: the canonical gated SDLC skill registry. Anything lifecycle-governed lives there, not here. The registries are independent by construction and doctrinally aligned.
- **COREFORGE / Synapse**: a consumer of skills, not a registry. Synapse loads Claude-format `SKILL.md` directly and native skills via `manifest.json`. Skills here target Claude-format first; `skill-sync --coreforge` generates Synapse manifests from frontmatter.

Rules of the lane:

1. **No gates at runtime.** Skills here may read cadence sources and synthesize, but they do not create Qor gate artifacts or enter the Qor delegation table. A skill that needs a PASS/VETO belongs in Qor-logic.
2. **Governance-aware, not governance-bound.** A skill may read governance outputs as a source, read-only.
3. **Portable by construction.** `SKILL.md` is the source of truth, capability needs are generic, external services use swappable connectors where possible, and local convention is bound at runtime rather than hardcoded.

## Status

The repository now includes the bootstrap/onboarding architecture on the Issue #7 feature branch in addition to the previously shipped skill series. Validation, generated-index refresh, behavioral bootstrap evals, and governed substantiation remain required before this work may be merged to main.
