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
INDEX.md / index.json        # generated skill registry — start here
skills/                      # one directory per skill
  claude-pulse/
    SKILL.md                 #   frontmatter (name, description) + instructions
    scripts/pulse.ts         #   optional zero-install support scripts
scripts/
  build-index.ts             # index generator
vendor/
  knowledge-work-plugins/    # git submodule: Anthropic's plugin marketplace
docs/
  skill-template.md          # starting point for new skills
ROADMAP.md                   # planned skill series + portability contract
```

## Authoring a skill

Start from [docs/skill-template.md](docs/skill-template.md). Conventions:

- `skills/<name>/SKILL.md` is the single source of truth; frontmatter `name` matches the directory, and `description` states both *what it does* and *when to use it* (that's what models match against).
- **Script collects, model synthesizes** — scripts fetch and structure; judgment stays in the instructions.
- Scripts run on Bun **or** Node 22.18+ with no install step, and every scripted source documents a pure web-tool fallback.
- Read-only by default; anything that mutates (send, push, delete) requires explicit approval per action.
- Every skill includes a Scheduling section (`/schedule` pairing for Claude Code).
- Finish by regenerating the index.

The full portability contract (capability declarations, MCP-only external services, tiered content) is in [ROADMAP.md](ROADMAP.md#portability-contract-system-agnostic-requirements).

## Vendored: Anthropic knowledge-work-plugins

[`vendor/knowledge-work-plugins`](https://github.com/anthropics/knowledge-work-plugins) is Anthropic's official marketplace of knowledge-work plugins — productivity, enterprise search, sales, finance, data, design, engineering, legal, marketing, HR, operations, bio-research, and more, plus 60 partner-built plugins. Each bundles skills as `<plugin>/skills/<name>/SKILL.md`; all are enumerated in [INDEX.md](INDEX.md). Useful both to install and as reference implementations.

Install into Claude Code straight from the source (no submodule needed):

```
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install productivity@knowledge-work-plugins
```

Refresh the vendored copy: `git submodule update --remote vendor/knowledge-work-plugins`, then regenerate the index.

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
