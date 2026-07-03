# 🛠️ skillz

**System-agnostic agent skills for daily and weekly cadence work** — built for MythologIQ agents and Claude Code alike. Pulse digests, briefings, repo hygiene, and skill-lifecycle tooling: the ungated work that runs on a schedule, not through a gate.

> 📇 **Looking for a skill? Start at [INDEX.md](INDEX.md)** (human/agent-readable) or [index.json](index.json) (machine-readable). Both are generated — see [Skill index](#skill-index).

---

## Quick start

**Claude Code — use a skill from this repo directly:**

```
Read G:\MythologIQ\skillz\INDEX.md, then run the claude-pulse skill.
```

**Claude Code — install a skill permanently:**

```powershell
# personal (all projects)
New-Item -ItemType SymbolicLink -Path "$env:USERPROFILE\.claude\skills\claude-pulse" -Target "G:\MythologIQ\skillz\skills\claude-pulse"
# or per-project: link into <project>\.claude\skills\ instead
```

**Any other agent:** point it at the skill's `SKILL.md` (paths in the index) and instruct it to follow the **Execution Flow** section. Skills are plain markdown plus optional zero-install scripts (Bun or Node 22.18+) — no framework required.

**Clone with the vendored plugins:**

```
git clone --recurse-submodules <url>
```

## Skill index

[INDEX.md](INDEX.md) and [index.json](index.json) are the canonical registry: every local skill (name, description, category, entry point, scripts) plus the full contents of the vendored Anthropic marketplace. Agents should resolve skills through the index rather than globbing the tree.

They are **generated — never edit by hand**. After adding or changing a skill:

```
node scripts/build-index.ts
```

The generator scans `skills/*/SKILL.md` frontmatter (warning on name/directory mismatches) and the vendor marketplace manifest.

## Repository layout

```
INDEX.md / index.json        # generated skill index — start here
skills/                      # first-party skills, one directory each
  claude-pulse/              #   weekly Claude release + community digest
  skills-pulse/              #   weekly ecosystem intake scan → registry proposals
registry/
  candidates.yaml            # intake decisions: adopted/sandbox/track/rejected/quarantined
vendor/                      # official skill sources, as git submodules
  anthropic-skills/          #   github.com/anthropics/skills
  knowledge-work-plugins/    #   github.com/anthropics/knowledge-work-plugins
  vercel-agent-skills/       #   github.com/vercel-labs/agent-skills
  microsoft-skills/          #   github.com/microsoft/skills
  azure-skills/              #   github.com/microsoft/azure-skills
  aws-agent-toolkit/         #   github.com/aws/agent-toolkit-for-aws
scripts/
  build-index.ts             # index generator (scans skills/ + all of vendor/)
docs/
  skill-template.md          # starting point for new skills
  evaluation-framework.md    # scoring rubric, statuses, permission tiers
  agent-skills-longlist.md   # ecosystem horizon scan (research input)
ROADMAP.md                   # planned skill series + portability contract
```

## How this stays lean

The repo covers the full agentic surface — local, cloud, and everything between — without becoming a junk drawer, by drawing three lines:

1. **Vendor only official sources.** Anthropic (general + office + marketplace), Vercel (frontend), Microsoft/Azure and AWS (cloud) come in as submodules, deduplicated upstream and indexed here. Community skills are *registered*, not copied.
2. **Every third-party skill is a decision, not a download.** [`registry/candidates.yaml`](registry/candidates.yaml) records adopt/sandbox/track/reject/quarantine per candidate with a permission tier and rationale, scored per [docs/evaluation-framework.md](docs/evaluation-framework.md). Redundancy with Qor-logic or a Claude Code built-in is a rejection reason on its own (`covered_by`).
3. **Intake is a cadence skill.** [`skills-pulse`](skills/skills-pulse/SKILL.md) scans the watchlist weekly, filters finds against the registry/index/Qor-logic/built-ins, and proposes registry entries — it never installs anything.

## Authoring a skill

Start from [docs/skill-template.md](docs/skill-template.md). Conventions:

- `skills/<name>/SKILL.md` is the single source of truth; frontmatter `name` matches the directory, and `description` states both *what it does* and *when to use it* (that's what models match against).
- **Script collects, model synthesizes** — scripts fetch and structure; judgment stays in the instructions.
- Scripts run on Bun **or** Node 22.18+ with no install step, and every scripted source documents a pure web-tool fallback.
- Read-only by default; anything that mutates (send, push, delete) requires explicit approval per action.
- Every skill includes a Scheduling section (`/schedule` pairing for Claude Code).
- Finish by regenerating the index.

The full portability contract (capability declarations, MCP-only external services, tiered content) is in [ROADMAP.md](ROADMAP.md#portability-contract-system-agnostic-requirements).

## Vendored official sources

Six official skill repos are vendored as submodules and fully enumerated in [INDEX.md](INDEX.md):

| Source | Coverage | Skills |
|--------|----------|--------|
| [anthropics/skills](https://github.com/anthropics/skills) | Office docs (docx/pdf/pptx/xlsx), skill-creator, mcp-builder, frontend design, webapp testing | 18 |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Knowledge-work marketplace: productivity, sales, finance, legal, data, design + 60 partner plugins | 185 |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | React/Next.js best practices, composition patterns, web design guidelines | 9 |
| [microsoft/skills](https://github.com/microsoft/skills) | Microsoft ecosystem: M365, Foundry, dev tooling | ~190 |
| [microsoft/azure-skills](https://github.com/microsoft/azure-skills) | Azure: plan/validate/deploy, RBAC, cost, diagnostics, AKS | ~68 |
| [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws) | AWS: core services, Bedrock agents, data analytics, DevSecOps | ~115 |

Marketplace-listed plugins install straight from source (no submodule needed):

```
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install productivity@knowledge-work-plugins
```

Refresh all vendored copies: `git submodule update --remote`, then regenerate the index. **Vendored ≠ blanket-trusted:** write-tier skills inside these repos (deploys, RBAC, cost changes) still require the permission gates in [docs/evaluation-framework.md](docs/evaluation-framework.md).

## Positioning in the MythologIQ ecosystem

This repo is the **ungated, system-agnostic** skill library. It deliberately does NOT overlap with:

- **[Qor-logic](../Qor-logic)** — the canonical *gated* SDLC skill registry (30 skills, phase-gate chain, Cedar policies, Merkle ledger). Anything lifecycle-governed lives there, not here. Qor-logic already compiles one SKILL.md source to per-host variants (`.claude/`, `.kilo/`, `.codex/`, `.gemini/`) — this repo borrows that single-source/compile-to-host pattern without the gates.
- **COREFORGE / Synapse** — a *consumer* of skills, not a registry. Synapse loads Claude-format `SKILL.md` directly and native skills via `manifest.json`. Skills here target Claude-format first; a Synapse manifest can be generated from frontmatter (see ROADMAP `skill-sync`).

Rules of the lane:

1. **No gates.** Skills here read cadence sources (releases, repos, inbox, calendar) and synthesize. They never write `.qor/gates/` artifacts and never enter the Qor delegation table. A skill that needs a PASS/VETO belongs in Qor-logic.
2. **Governance-aware, not governance-bound.** A skill MAY read governance outputs (e.g., `docs/META_LEDGER.md`, shadow genome) as a *source* for a digest — read-only.
3. **Portable by construction.** Markdown SKILL.md as single source of truth; capability needs declared generically in frontmatter (no platform permissions like elevation or process spawn); external services via MCP; web-tool fallback for every scripted source.

## Roadmap

Four planned series — **Pulse** (weekly external-awareness digests), **Daily ops** (briefing, triage, standup), **Repo hygiene** (doctor, changelog, TODO harvest), and **Meta** (forge, audit, sync, memory-distill) — plus ecosystem-specific candidates like `governance-pulse` and `coreforge-pulse`. Details and build order in [ROADMAP.md](ROADMAP.md).
