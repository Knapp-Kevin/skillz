# 🛠️ skillz

[![CI](https://github.com/Knapp-Kevin/skillz/actions/workflows/ci.yml/badge.svg)](https://github.com/Knapp-Kevin/skillz/actions/workflows/ci.yml)
![Skills](https://img.shields.io/badge/first--party_skills-48-blue)
![Vendored](https://img.shields.io/badge/vendored_skills-524_across_6_sources-8A2BE2)
![Runtime](https://img.shields.io/badge/runtime-Bun_%7C_Node_22.18%2B-brightgreen)
![Install](https://img.shields.io/badge/install-zero-success)

**System-agnostic agent skills for MythologIQ agents and Claude Code alike** — recurring awareness (pulses, briefings), on-demand judgment (research, decision briefs), agent fleet operations, and the meta-tooling that keeps it all validated and deployed. Ungated by design: work that runs on a schedule or a question, not through a gate.

> 📇 **Looking for a skill? Start at [INDEX.md](INDEX.md)** (human/agent-readable) or [index.json](index.json) (machine-readable). Both are generated — see [Skill index](#skill-index).

*Count badges are maintained by the same state-alignment discipline as the docs (verified against `skill-audit` output at every governed cycle); the CI badge is live.*

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

48 first-party skills across seven series:

| Series | Skills | Cadence |
|--------|--------|---------|
| **Pulse** (17) | 11 vendor pulses (claude, openai, gemini, llama, mistral, xai, deepseek, qwen, glm, kimi, perplexity) + 6 topic pulses (`governance`, `memory`, `github`, `hf`, `mcp`, `inference`) — all driven by one engine (`scripts/pulse-run.ts`) with per-skill `sources.json`; adding a pulse is a data change | weekly |
| **Research** (5) | `deep-dive`, `compare`, `fact-check`, `paper-digest`, `source-vetting` — structured inquiry with adversarial fact-checking and registry-ready verdicts | on demand |
| **Agent-ops** (5) | `skill-eval`, `mcp-vetting`, `agent-postmortem`, `handoff-writer`, `permissions-review` — running the agent fleet itself | on demand / monthly |
| **Daily-ops** (5) | `daily-briefing`, `inbox-triage`, `standup-writer`, `week-in-review`, `task-surface` (forge + operate a cross-org task-coordination repo, bound to its own governance doc) — draft-only for anything that sends or writes | daily / weekly |
| **Comms & life** (8) | `brief-writer`, `decision-log`, `devlog-draft`, `deck-outline`, `finance-review`, `smallbiz-ops`, `career-radar`, `learning-plan` | on demand / monthly |
| **Repo hygiene** (3) | `repo-pulse`, `repo-doctor`, `todo-harvester` — `gh`/git-evidence based, read-only punch lists | weekly / on demand |
| **Meta** (5) | `skills-pulse` (ecosystem intake + vendor freshness), `skill-audit` (two-layer self-validation), `skill-sync` (deployment: junction/copy/COREFORGE/multi-host), `skill-forge` (scaffolding), `agent-home-doctor` (audit/clean any agent CLI's home dir — pathology library + tiered remediation) — audit/sync/forge are repo-bound and never deploy | weekly / pre-commit / as-needed |

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
skills/                      # 48 first-party skills, one directory each
  <vendor>-pulse/            #   11 vendor + 6 topic pulses (SKILL.md + sources.json)
  deep-dive/ compare/ ...    #   research series (5)
  skill-eval/ mcp-vetting/ … #   agent-ops series (5)
  daily-briefing/ ...        #   daily-ops series (5)
  brief-writer/ decision-log/#   comms & life (8)
  skills-pulse/ skill-audit/ #   meta series (audit/sync/forge are repo-bound;
  skill-sync/ skill-forge/   #   skill-audit ships audit.ts + risk-audit.ts)
registry/
  candidates.yaml            # intake decisions: adopted/sandbox/track/rejected/quarantined
vendor/                      # official skill sources, as git submodules (6)
scripts/
  build-index.ts             # index generator (scans skills/ + all of vendor/)
  pulse-run.ts               # shared pulse collector, driven by sources.json specs
  lib/frontmatter.ts         # shared zero-dep frontmatter parser
tests/                       # 15 behavior tests: node --test "tests/*.test.mjs"
.github/workflows/ci.yml     # CI: tests + audit + risk audit + index freshness
docs/                        # skill template, evaluation framework, eval reports,
                             #   vendor-freshness workflow, governance artifacts
ROADMAP.md                   # series status + design rules + portability contract
```

## Validation: two layers, both enforced

1. **Structural** — [`skill-audit`](skills/skill-audit/SKILL.md) (`scripts/audit.ts`): frontmatter conventions, script `--help` health, pulse-spec parsing, registry enums, index freshness. Exit 1 on drift.
2. **Semantic risk** — `scripts/risk-audit.ts`: a structurally valid skill can still induce dangerous behavior, so this layer FAILs high-judgment skills missing negative-rule classes (secret handling, anti-fabrication, missing-evidence fallback) and mutating actions without approval language, and WARNs on portable-skill operator specifics and vendor-API references without an MCP/web fallback.

Both run in [CI](.github/workflows/ci.yml) on every PR and push to main, alongside the 15-test behavior suite and an index-idempotency diff. The risk layer earned its keep on its first live run: it caught six real gaps in already-audited skills.

## How this stays lean

The repo covers the full agentic surface — local, cloud, and everything between — without becoming a junk drawer, by drawing four lines:

1. **Vendor only official sources.** Anthropic (general + office + marketplace), Vercel (frontend), Microsoft/Azure and AWS (cloud) come in as submodules, deduplicated upstream and indexed here. Community skills are *registered*, not copied.
2. **Every third-party skill is a decision, not a download.** [`registry/candidates.yaml`](registry/candidates.yaml) records adopt/sandbox/track/reject/quarantine per candidate with a permission tier and rationale, scored per [docs/evaluation-framework.md](docs/evaluation-framework.md). Redundancy with Qor-logic or a Claude Code built-in is a rejection reason on its own (`covered_by`).
3. **Intake is a cadence skill.** [`skills-pulse`](skills/skills-pulse/SKILL.md) scans the watchlist weekly, filters finds against the registry/index/gated-registry/built-ins, reports per-source vendor freshness, and proposes registry entries — it never installs anything.
4. **The repo maintains itself.** The two audit layers above plus [`skill-sync`](skills/skill-sync/SKILL.md) deployment (junction into `~/.claude/skills`, copy anywhere, COREFORGE Synapse manifests, multi-host — dry-run by default) keep validation and distribution mechanical.

## Authoring a skill

Start from [docs/skill-template.md](docs/skill-template.md). Conventions (mechanically enforced by the two audit layers):

- `skills/<name>/SKILL.md` is the single source of truth; frontmatter `name` matches the directory, and `description` states both *what it does* and *when to use it* (that's what models match against).
- **Script collects, model synthesizes** — scripts fetch and structure; judgment stays in the instructions. Most skills need no script at all.
- Scripts run on Bun **or** Node 22.18+ with no install step, and every scripted source documents a pure web-tool fallback.
- Read-only by default; anything that mutates (send, push, delete) requires explicit approval per action.
- **Adaptive frameworks, not configurations.** Skills ship the framework; operator/org/environment specifics live in *bound governance documents* discovered at runtime (a Bind step early in the flow; the bound document wins over memory; elicit + offer to persist when none exists). No hardcoded operator values in portable skill bodies.
- **Negative rules ship with the scaffold.** High-judgment skills (mandatory evidence/decision slots) carry explicit prohibitions: never reproduce secret-shaped strings (type + short prefix only, rotation on exposure), write `not established` for evidence-free slots, mark inference as inference, empty sections are valid. Evidence: the [weak-model eval pair](docs/evals/) — structure alone *redistributed* failure modes at Haiku tier until the negative rules shipped, after which the degradation reversed (treatment 29/30 vs baseline 26/30, zero treatment security violations).
- Declare the capability floor as data when evidence supports it: `metadata.min-model-capability: haiku|sonnet|opus` (hosts and routers enforce it; models never self-assess).
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

Pins are refreshed deliberately, never automatically: [docs/vendor-freshness.md](docs/vendor-freshness.md) is the review-first workflow and per-source freshness table (one source at a time, classify the delta, re-index in the same commit); CI validates the pinned state only, and `skills-pulse` reports upstream drift on cadence. **Vendored ≠ blanket-trusted:** write-tier skills inside these repos (deploys, RBAC, cost changes) still require the permission gates in [docs/evaluation-framework.md](docs/evaluation-framework.md).

Marketplace-listed plugins install straight from source (no submodule needed):

```
/plugin marketplace add anthropics/knowledge-work-plugins
/plugin install productivity@knowledge-work-plugins
```

## Governed development

Changes to this repo's tooling go through the Qor-logic S.H.I.E.L.D. lifecycle: planned, adversarially audited to a binding PASS/VETO, implemented against the sealed plan, and substantiated before merge. The governance record lives in `docs/` (META_LEDGER — 21 chain-verified entries and counting, SHADOW_GENOME, SYSTEM_STATE, BACKLOG, FEATURE_INDEX). The *skills themselves* remain ungated — governance applies to building the repo, never to running a pulse.

## Positioning in the MythologIQ ecosystem

This repo is the **ungated, system-agnostic** skill library. It deliberately does NOT overlap with:

- **[Qor-logic](../Qor-logic)** — the canonical *gated* SDLC skill registry (30 skills, phase-gate chain, Cedar policies, Merkle ledger). Anything lifecycle-governed lives there, not here. The two registries are **independent by construction** (no runtime dependency in either direction) and **doctrinally aligned** (same negative-rules vocabulary, adaptive-frameworks pattern, capability-floor metadata). Qor-logic already compiles one SKILL.md source to per-host variants (`.claude/`, `.kilo/`, `.codex/`, `.gemini/`) — this repo borrows that single-source/compile-to-host pattern without the gates.
- **COREFORGE / Synapse** — a *consumer* of skills, not a registry. Synapse loads Claude-format `SKILL.md` directly and native skills via `manifest.json`. Skills here target Claude-format first; `skill-sync --coreforge` generates Synapse manifests from frontmatter.

Rules of the lane:

1. **No gates.** Skills here read cadence sources (releases, repos, inbox, calendar) and synthesize. They never write `.qor/gates/` artifacts and never enter the Qor delegation table. A skill that needs a PASS/VETO belongs in Qor-logic.
2. **Governance-aware, not governance-bound.** A skill MAY read governance outputs (e.g., a workspace's META_LEDGER, shadow genome) as a *source* for a digest — read-only.
3. **Portable by construction.** Markdown SKILL.md as single source of truth; capability needs declared generically in frontmatter (no platform permissions like elevation or process spawn); external services via MCP; web-tool fallback for every scripted source; local convention via Bind, never via hardcoding.

## Status

All seven series are shipped and validated (48 skills, 15/15 behavior tests, both audit layers clean, index idempotent — re-proven by CI on every push). The original build order completed 2026-07-04; current open work lives in [docs/BACKLOG.md](docs/BACKLOG.md) §Open (min-model-capability rollout, Gemini host target, sandbox evals) and the repo's GitHub issues. The eval program has its first full loop closed: frontier ceiling → weak-tier failure discovery → negative rules → mechanical enforcement → weak-tier reversal confirmed ([docs/evals/](docs/evals/)). Design rules, series detail, and the portability contract: [ROADMAP.md](ROADMAP.md).
