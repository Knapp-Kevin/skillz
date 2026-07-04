# 🛠️ skillz

**System-agnostic agent skills for MythologIQ agents and Claude Code alike** — recurring awareness (pulses, briefings), on-demand judgment (research, decision briefs), agent fleet operations, and the meta-tooling that keeps it all validated and deployed. Ungated by design: work that runs on a schedule or a question, not through a gate.

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
# or deploy everything portable at once:
node skills/skill-sync/scripts/sync.ts --claude-user --apply
```

**Any other agent:** point it at the skill's `SKILL.md` (paths in the index) and instruct it to follow the **Execution Flow** section. Skills are plain markdown plus optional zero-install scripts (Bun or Node 22.18+) — no framework required.

**Clone with the vendored plugins:**

```
git clone --recurse-submodules <url>
```

## Skill series

35 first-party skills across six series:

| Series | Skills | Cadence |
|--------|--------|---------|
| **Pulse** (16) | `claude-pulse` + 10 more vendor pulses (openai, gemini, llama, mistral, xai, deepseek, qwen, glm, kimi, perplexity) + 5 topic pulses (`governance`, `memory`, `github`, `hf`, `mcp`) — all driven by one engine (`scripts/pulse-run.ts`) with per-skill `sources.json`; adding a pulse is a data change | weekly |
| **Research** (5) | `deep-dive`, `compare`, `fact-check`, `paper-digest`, `source-vetting` — structured inquiry with adversarial fact-checking and registry-ready verdicts | on demand |
| **Agent-ops** (5) | `skill-eval`, `mcp-vetting`, `agent-postmortem`, `handoff-writer`, `permissions-review` — running the agent fleet itself | on demand / monthly |
| **Daily-ops** (4) | `daily-briefing`, `inbox-triage`, `standup-writer`, `week-in-review` — via connected Gmail/Calendar/Slack MCPs, draft-only for anything that sends | daily / weekly |
| **Comms & life** (2) | `brief-writer`, `decision-log` | on demand |
| **Meta** (3) | `skills-pulse` (ecosystem intake), `skill-audit` (repo self-validation), `skill-sync` (deployment) — the last two are repo-bound and never deploy | weekly / pre-commit |

## Skill index

[INDEX.md](INDEX.md) and [index.json](index.json) are the canonical registry: every local skill (name, description, category, entry point, scripts) plus the full contents of the vendored official sources. Agents should resolve skills through the index rather than globbing the tree.

They are **generated — never edit by hand**. After adding or changing a skill:

```
node scripts/build-index.ts
```

The generator scans `skills/*/SKILL.md` frontmatter (warning on name/directory mismatches) and all vendor trees.

## Repository layout

```
INDEX.md / index.json        # generated skill index — start here
skills/                      # 35 first-party skills, one directory each
  <vendor>-pulse/            #   11 vendor + 5 topic pulses (SKILL.md + sources.json)
  deep-dive/ compare/ ...    #   research series (5)
  skill-eval/ mcp-vetting/ … #   agent-ops series (5)
  daily-briefing/ ...        #   daily-ops series (4)
  brief-writer/ decision-log/#   comms & life
  skills-pulse/ skill-audit/ #   meta series (audit + sync are repo-bound,
  skill-sync/                #   with scripts; all other skills are markdown-only)
registry/
  candidates.yaml            # intake decisions: adopted/sandbox/track/rejected/quarantined
vendor/                      # official skill sources, as git submodules (6)
scripts/
  build-index.ts             # index generator (scans skills/ + all of vendor/)
  pulse-run.ts               # shared pulse collector, driven by sources.json specs
  lib/frontmatter.ts         # shared zero-dep frontmatter parser
tests/                       # behavior tests: node --test "tests/*.test.mjs"
docs/                        # skill template, evaluation framework, governance artifacts
ROADMAP.md                   # series status + build order + portability contract
```

## How this stays lean

The repo covers the full agentic surface — local, cloud, and everything between — without becoming a junk drawer, by drawing four lines:

1. **Vendor only official sources.** Anthropic (general + office + marketplace), Vercel (frontend), Microsoft/Azure and AWS (cloud) come in as submodules, deduplicated upstream and indexed here. Community skills are *registered*, not copied.
2. **Every third-party skill is a decision, not a download.** [`registry/candidates.yaml`](registry/candidates.yaml) records adopt/sandbox/track/reject/quarantine per candidate with a permission tier and rationale, scored per [docs/evaluation-framework.md](docs/evaluation-framework.md). Redundancy with Qor-logic or a Claude Code built-in is a rejection reason on its own (`covered_by`).
3. **Intake is a cadence skill.** [`skills-pulse`](skills/skills-pulse/SKILL.md) scans the watchlist weekly, filters finds against the registry/index/Qor-logic/built-ins, and proposes registry entries — it never installs anything.
4. **The repo maintains itself.** [`skill-audit`](skills/skill-audit/SKILL.md) validates conventions, script health, registry enums, and index freshness (`node skills/skill-audit/scripts/audit.ts`, exit 1 on drift). [`skill-sync`](skills/skill-sync/SKILL.md) deploys portable skills — junction into `~/.claude/skills`, copy anywhere, or COREFORGE Synapse manifests — dry-run by default. Behavior tests: `node --test "tests/*.test.mjs"`.

## Governed development

Changes to this repo's tooling go through the Qor-logic S.H.I.E.L.D. lifecycle: planned, adversarially audited to a binding PASS/VETO, implemented against the sealed plan, and substantiated before merge. The governance record lives in `docs/` (META_LEDGER, SHADOW_GENOME, SYSTEM_STATE, BACKLOG, FEATURE_INDEX). The *skills themselves* remain ungated — governance applies to building the repo, never to running a pulse.

## Authoring a skill

Start from [docs/skill-template.md](docs/skill-template.md). Conventions (mechanically enforced by `skill-audit`):

- `skills/<name>/SKILL.md` is the single source of truth; frontmatter `name` matches the directory, and `description` states both *what it does* and *when to use it* (that's what models match against).
- **Script collects, model synthesizes** — scripts fetch and structure; judgment stays in the instructions. Most skills need no script at all.
- Scripts run on Bun **or** Node 22.18+ with no install step, and every scripted source documents a pure web-tool fallback.
- Read-only by default; anything that mutates (send, push, delete) requires explicit approval per action.
- Recurring skills include a Scheduling section (`/schedule` pairing for Claude Code).
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
- **COREFORGE / Synapse** — a *consumer* of skills, not a registry. Synapse loads Claude-format `SKILL.md` directly and native skills via `manifest.json`. Skills here target Claude-format first; `skill-sync --coreforge` generates Synapse manifests from frontmatter.

Rules of the lane:

1. **No gates.** Skills here read cadence sources (releases, repos, inbox, calendar) and synthesize. They never write `.qor/gates/` artifacts and never enter the Qor delegation table. A skill that needs a PASS/VETO belongs in Qor-logic.
2. **Governance-aware, not governance-bound.** A skill MAY read governance outputs (e.g., `docs/META_LEDGER.md`, shadow genome) as a *source* for a digest — read-only.
3. **Portable by construction.** Markdown SKILL.md as single source of truth; capability needs declared generically in frontmatter (no platform permissions like elevation or process spawn); external services via MCP; web-tool fallback for every scripted source.

## Roadmap

Shipped: the pulse fleet (16), research (5), agent-ops (5), daily-ops (4), comms/life core, and the self-maintaining meta series. Next per build order: `skill-eval` in anger on registry candidates, `devlog-draft`/`deck-outline`, `finance-review`, `inference-pulse`, and the `gh`-based repo-hygiene cluster. Details, series tables, and the portability contract in [ROADMAP.md](ROADMAP.md).
