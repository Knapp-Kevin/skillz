# Roadmap — planned skill series

The repo's purpose is skills that run on a **daily or weekly cadence**, either invoked manually or wired to `/schedule` / agent automations. Four coherent series, ordered roughly by value-per-effort. Each skill follows the claude-pulse pattern: a small fetch/collect script (Bun/Node TS, zero install) plus a SKILL.md that makes the model do the synthesis.

## 1. Pulse series — external awareness (weekly)

Siblings of `claude-pulse`: same digest shape, different domain.

All pulses share one collector (`scripts/pulse-run.ts`) driven by a per-skill `sources.json` — adding a pulse is a data change, not new code.

**Shipped — vendor pulses** ✅: `claude-pulse` (bespoke script, predates the engine), `openai-pulse`, `gemini-pulse`, `llama-pulse`, `mistral-pulse`, `xai-pulse`, `deepseek-pulse`, `qwen-pulse`, `glm-pulse` (z.ai/Zhipu), `kimi-pulse` (Moonshot), `perplexity-pulse`.

Vendor watchlist (add a `sources.json` when they ship something load-bearing): MiniMax, ByteDance Seed/Doubao, Tencent Hunyuan, Baidu Ernie, Cohere, AI2 (OLMo), NVIDIA (Nemotron).

**Shipped — topic pulses** ✅: `governance-pulse` (EU AI Act / NIST / OWASP / governance-tooling market + optional read-only local ledger drift), `memory-pulse` (agentic memory & context engineering → COREFORGE Vault), `github-pulse` (new & trending repos, AI-centric), `hf-pulse` (Hugging Face cross-vendor view; prefers the connected HF MCP tools), `mcp-pulse` (protocol spec/SDK/servers/security — the portability layer itself).

Remaining candidates, in rough priority order:

| Skill | What it digests | Why / why not yet |
|-------|-----------------|-------------------|
| `inference-pulse` | Local-inference runtimes: llama.cpp, Ollama, vLLM, quantization formats, GPU/NPU support | Strong GG-CORE fit — a `sources.json` away; next up when local-runtime decisions get active |
| `repo-pulse` | Activity across your own GitHub repos: commits, PRs needing review, stale branches, CI failures | Needs `gh` CLI integration, not the generic engine |
| `deps-pulse` | Dependency updates and CVEs across active projects | Needs per-project scanners (`npm audit`, `cargo audit`), not the generic engine |
| `tauri-pulse` | Tauri/Rust ecosystem releases and breaking changes | A `sources.json` away; ship when a Tauri upgrade cycle nears |
| `voice-pulse` | Voice-AI ecosystem: ElevenLabs, realtime speech APIs, TTS/STT models | You maintain ElevenLabs integrations; ship if voice work resumes |
| `benchmark-pulse` | New evals, leaderboard movement (LMArena, SWE-bench, agentic benchmarks) | Useful but vendor pulses already carry the headline results — watch for redundancy |
| `market-pulse` | AI business news: funding, M&A, enterprise adoption, competitor moves in agent governance | Feeds Qortara GTM; lower cadence (monthly), mostly web-search driven |

Considered and skipped for now: `robotics-pulse`, `image/video-gen-pulse` (no active product need — registry `track` at most), `arxiv-pulse` as a standalone (memory-pulse and hf-pulse's paper themes cover the agent-relevant slice; a general paper firehose is noise).

## 2. Daily ops series — personal cadence (daily)

These lean on the already-connected Gmail/Calendar/Slack MCP servers.

| Skill | What it does |
|-------|--------------|
| `daily-briefing` | Morning brief: today's calendar, unread email worth acting on, open tasks, yesterday's loose ends. One screen, action-first. |
| `inbox-triage` | Classify inbox into act / delegate / read-later / archive; draft replies for the "act" pile, never send without approval. |
| `standup-writer` | Generate a standup/worklog entry from git commits across MythologIQ repos since yesterday + task list changes. |
| `week-in-review` | Friday retrospective: what shipped, what stalled, what to carry forward. Input: git history, task states, memory files. Output feeds Monday's briefing. |

## 3. Repo hygiene series — project upkeep (weekly, per-repo)

| Skill | What it does |
|-------|--------------|
| `repo-doctor` | One-shot health check: stale branches, uncommitted work, TODO/FIXME inventory, failing CI, README drift, missing licenses. Emits a punch list, fixes nothing without approval. |
| `changelog-writer` | Draft CHANGELOG entries from commits since the last tag, grouped and human-readable (Keep-a-Changelog format). |
| `release-notes` | Turn a tag range into audience-facing release notes (distinct from changelog: written for users, not maintainers). |
| `todo-harvester` | Sweep TODO/FIXME/HACK comments across a repo into a triaged task list with file:line links and age (via git blame). |

## 4. Meta series — skill lifecycle (as-needed)

This repo maintaining itself.

| Skill | What it does |
|-------|--------------|
| `skills-pulse` ✅ | **Shipped.** Weekly ecosystem intake scan: watchlist repo activity, marketplace sweep, redundancy filter, registry candidate proposals. |
| `skill-forge` | Scaffold a new skill in this repo from `docs/skill-template.md`: prompts for name/description/cadence, creates the directory, regenerates the index. |
| `skill-audit` ✅ | **Shipped.** Mechanical repo validation: SKILL.md conventions, script `--help` health, registry enum/rationale/resolved_path lint, index freshness. `node skills/skill-audit/scripts/audit.ts`. |
| `skill-sync` ✅ | **Shipped.** Deploys portable skills (dry-run default, `--apply` to execute): junctions into `~/.claude/skills/` (`--claude-user`), copies to any path (`--dest`), COREFORGE Synapse `manifest.json` bundles (`--coreforge`). Repo-bound meta-skills excluded by construction. Per-host `dist_compile`-style variants remain future work. |
| `memory-distill` | Weekly consolidation of Claude Code's persistent memory: merge duplicates, expire stale project facts, tighten the MEMORY.md index. |

## 5. Research series — structured inquiry (on-demand)

The biggest unshipped category. Pulses answer "what changed"; these answer "what should I believe / choose."

| Skill | What it does |
|-------|--------------|
| `deep-dive` | Multi-source research dossier on any topic: scope → parallel source sweep → adversarial fact-check → cited report. System-agnostic sibling of Claude Code's deep-research harness. |
| `compare` | Structured comparison (tools, models, vendors, approaches): criteria elicited first, evidence per cell, weighted recommendation. Kills "which X should I use" thrash. |
| `fact-check` | Claim verification: decompose into checkable sub-claims, source each, report confidence + what would change the verdict. |
| `paper-digest` | Read a paper properly: claims, method, evidence quality, limitations, replication status, relevance to our stack. Feeds memory-pulse/hf-pulse finds. |
| `source-vetting` | Trust evaluation of a repo/vendor/dataset before it enters the registry: maintainer history, activity authenticity, license, security posture. Operationalizes the evaluation framework's source-trust criterion. |

## 6. Agent-ops series — running the fleet itself (recurring + on-demand)

| Skill | What it does |
|-------|--------------|
| `skill-eval` | Before/after effectiveness testing for a candidate skill: sample tasks with and without the skill loaded, scored comparison → registry evidence. Closes the loop the evaluation framework declares (`eval_plan`) but nothing runs today. **Highest-leverage gap in the repo.** |
| `mcp-vetting` | Security review of an MCP server before connecting: tool surface, permissions, network behavior, injection exposure, provenance. Pairs with mcp-pulse finds and the registry's quarantine tier. |
| `agent-postmortem` | After a failed/expensive agent session: extract root cause, cost drivers, and lessons → memory files or shadow-genome entries. Bridges to Qor-logic without touching its gates. |
| `handoff-writer` | Continuation context for cross-session/cross-agent work: state, decisions, open threads, next actions. (Registry `sandbox` candidate exists; build first-party.) |
| `permissions-review` | Periodic audit of what agents can touch: MCP servers, allowlists, credentials, hooks. Read-only report with tightening recommendations. |

## 7. Comms & writing series (on-demand)

| Skill | What it does |
|-------|--------------|
| `brief-writer` | One-page decision brief: situation, options, recommendation, risks. The default artifact for asking a human to decide something. |
| `devlog-draft` | Founder-led content from real work: turn a week of git history + decisions into a devlog/blog draft that preserves voice. Constraints per registry marketing rules (no synthetic authority, no fake traction). |
| `deck-outline` | Narrative-first deck outlines (pitch, update, launch); execution hands off to the vendored pptx skill. |

## 8. Life-ops series — personal & small-business (recurring)

Extends the Daily-ops series beyond the workday.

| Skill | What it does |
|-------|--------------|
| `finance-review` | Monthly money digest: statements/exports in, categorized trends + anomalies out (vendored xlsx skill does the mechanics). Read-only; never initiates transactions. |
| `smallbiz-ops` | Upkeep cadence for the family business sites (Hill House Transport, Neat & Clean, Chesapeake Moms Club): content freshness, uptime, listings/SEO drift, seasonal to-dos. |
| `career-radar` | Periodic market scan for roles/rates matching a profile; builds on the job-ranger/career-ops work already in the ecosystem. |
| `learning-plan` | Structured skill acquisition: goal → curriculum from real sources → weekly cadence with checkpoints; pairs with `/schedule`. |
| `decision-log` | Personal ADR: capture non-code life/business decisions with context and revisit dates. Life-side sibling of qor-meta-log-decision. |

## Suggested build order (updated 2026-07-03)

Shipped so far: the pulse fleet (16), skill-audit, skill-sync, skills-pulse. Next:

1. `skill-eval` — closes the registry's evaluate loop; every later adoption decision gets cheaper and more honest.
2. `deep-dive` + `compare` — the research core; highest daily utility across work and life.
3. `daily-briefing` — the anchor habit the other daily skills feed into (Gmail/Calendar MCPs already connected).
4. `mcp-vetting` — before the next MCP server gets connected, not after.
5. `repo-pulse` + `repo-doctor` + `standup-writer` — the git-plumbing cluster, built together.
6. `brief-writer` + `handoff-writer` — small, immediately useful, exercise the comms patterns.
7. Life-ops as cadence proves itself; `finance-review` first (xlsx machinery already vendored).

## Design rules for every new skill

- **Script collects, model synthesizes.** Scripts fetch and structure; judgment stays in the SKILL.md instructions.
- **Zero-install.** Bun or Node 22.18+, standard library + `fetch` only.
- **Graceful degradation.** Document a web-tool fallback for every scripted source.
- **Read-only by default.** Skills that mutate (send email, push, delete) must require explicit approval per action.
- **Schedulable.** Every skill's SKILL.md includes a Scheduling section showing the `/schedule` pairing.
- **Ungated.** No `.qor/gates/` reads/writes, no delegation-table entries, no PASS/VETO semantics. Lifecycle-governed skills belong in Qor-logic. Reading governance artifacts (META_LEDGER, shadow genome) as a digest *source* is fine — read-only.

## Portability contract (system-agnostic requirements)

Derived from what COREFORGE's Synapse loader and Qor-logic's host compiler each need. A skill in this repo must satisfy all of:

1. **SKILL.md is the single source of truth**, Claude Code format (frontmatter `name` + `description`). COREFORGE already loads this format directly; other hosts get compiled variants via `skill-sync`.
2. **Declare capability needs generically** in frontmatter metadata: tools as abstract categories (`web-fetch`, `web-search`, `file-read`, `shell-read`), never platform permissions (elevation, process spawn, git-local). This maps forward onto COREFORGE's planned `requires_tools` / `requires_connections` manifest fields and Qor-logic's `permitted_tools`.
3. **External services via MCP** (Gmail, Calendar, Slack, HF) so connectors are swappable per platform — never direct vendor API calls baked into instructions.
4. **Tiered content**: frontmatter description (~1 sentence, matchable) → core instructions (<5k words) → `references/`/`scripts/` for the rest. Matches COREFORGE's AISkillLoader tiers (metadata / core / full) and keeps Claude Code context cost low.
5. **No host-conditional logic in instructions.** Where behavior must differ per host (e.g., scheduling), give a labeled per-host section like claude-pulse's Scheduling block — the model picks its own row.

### Ecosystem-specific pulse candidates (added after repo survey)

| Skill | What it digests |
|-------|-----------------|
| `governance-pulse` | Weekly read-only digest across repos with `.qor/` state: ledger growth, shadow-genome events, gate overrides, VETO streaks. Surfaces process drift without touching the gates. |
| `coreforge-pulse` | COREFORGE dev status: test counts (Rust/Jest), open research briefs, skill-registry drift between `src/skills/native/registry` and `.claude/skills/`. |
