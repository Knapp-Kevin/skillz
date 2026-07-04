# Roadmap — planned skill series

The repo's purpose is skills that run on a **daily or weekly cadence**, either invoked manually or wired to `/schedule` / agent automations. Four coherent series, ordered roughly by value-per-effort. Each skill follows the claude-pulse pattern: a small fetch/collect script (Bun/Node TS, zero install) plus a SKILL.md that makes the model do the synthesis.

## 1. Pulse series — external awareness (weekly)

Siblings of `claude-pulse`: same digest shape, different domain.

All pulses share one collector (`scripts/pulse-run.ts`) driven by a per-skill `sources.json` — adding a pulse is a data change, not new code.

**Shipped — vendor pulses** ✅: `claude-pulse` (bespoke script, predates the engine), `openai-pulse`, `gemini-pulse`, `llama-pulse`, `mistral-pulse`, `xai-pulse`, `deepseek-pulse`, `qwen-pulse`, `glm-pulse` (z.ai/Zhipu), `kimi-pulse` (Moonshot), `perplexity-pulse`.

Vendor watchlist (add a `sources.json` when they ship something load-bearing): MiniMax, ByteDance Seed/Doubao, Tencent Hunyuan, Baidu Ernie, Cohere, AI2 (OLMo), NVIDIA (Nemotron).

**Shipped — topic pulses** ✅: `governance-pulse` (EU AI Act / NIST / OWASP / governance-tooling market + optional read-only local ledger drift), `memory-pulse` (agentic memory & context engineering → COREFORGE Vault), `github-pulse` (new & trending repos, AI-centric), `hf-pulse` (Hugging Face cross-vendor view; prefers the connected HF MCP tools), `mcp-pulse` (protocol spec/SDK/servers/security — the portability layer itself).

Remaining candidates, in rough priority order:

**Also shipped** ✅ (1.0 cycle): `inference-pulse` (llama.cpp/Ollama/vLLM → GG-CORE relevance verdicts), `repo-pulse` (`gh`-based own-repo digest).

| Skill | What it digests | Why / why not yet |
|-------|-----------------|-------------------|
| `deps-pulse` | Dependency updates and CVEs across active projects | Needs per-project scanners (`npm audit`, `cargo audit`), not the generic engine |
| `tauri-pulse` | Tauri/Rust ecosystem releases and breaking changes | A `sources.json` away; ship when a Tauri upgrade cycle nears |
| `voice-pulse` | Voice-AI ecosystem: ElevenLabs, realtime speech APIs, TTS/STT models | You maintain ElevenLabs integrations; ship if voice work resumes |
| `benchmark-pulse` | New evals, leaderboard movement (LMArena, SWE-bench, agentic benchmarks) | Useful but vendor pulses already carry the headline results — watch for redundancy |
| `market-pulse` | AI business news: funding, M&A, enterprise adoption, competitor moves in agent governance | Feeds Qortara GTM; lower cadence (monthly), mostly web-search driven |

Considered and skipped for now: `robotics-pulse`, `image/video-gen-pulse` (no active product need — registry `track` at most), `arxiv-pulse` as a standalone (memory-pulse and hf-pulse's paper themes cover the agent-relevant slice; a general paper firehose is noise).

## 2. Daily ops series — personal cadence (daily)

These lean on the already-connected Gmail/Calendar/Slack MCP servers.

**Shipped** ✅: `daily-briefing` (action-first morning brief), `inbox-triage` (act/delegate/read-later/archive, draft-only replies), `standup-writer` (evidence-only worklog from git + tasks), `week-in-review` (Friday retro feeding Monday's briefing).

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

Pulses answer "what changed"; these answer "what should I believe / choose."

**Shipped** ✅: `deep-dive` (multi-source dossier with adversarial fact-check), `compare` (criteria-first comparison matrices), `fact-check` (sub-claim decomposition, primary sources), `paper-digest` (claims/method/evidence-quality/relevance), `source-vetting` (trust evaluation → registry entry proposal).

## 6. Agent-ops series — running the fleet itself (recurring + on-demand)

**Shipped** ✅: `skill-eval` (before/after effectiveness testing — operationalizes the evaluation framework's `eval_plan`), `mcp-vetting` (pre-connection security review of MCP servers), `agent-postmortem` (root cause + lessons → proposed memory/shadow-genome homes), `handoff-writer` (continuation context), `permissions-review` (monthly agent-access audit).

## 7. Comms & writing series (on-demand)

**Shipped** ✅: `brief-writer` (one-page decision briefs), `devlog-draft` (voice-preserving founder content from real git history), `deck-outline` (narrative-first outlines; vendored pptx executes).

## 8. Life-ops series — personal & small-business (recurring)

**Shipped** ✅: `decision-log` (personal/business ADR with revisit dates), `finance-review` (monthly money digest, read-only), `smallbiz-ops` (family-business site upkeep cadence), `career-radar` (role/rate market scan), `learning-plan` (structured skill acquisition with `/schedule` cadence).

## Build order (complete — 2026-07-04)

The original seven-step build order shipped in full across sessions ca9b2c and 927a53 (close-out: docs/BACKLOG.md D03-D08): skill-eval, deep-dive + compare, daily-briefing, mcp-vetting, the git-plumbing cluster (repo-pulse, repo-doctor, standup-writer), brief-writer + handoff-writer, and the life-ops series starting with finance-review. This section is a historical record, not a queue — current open work lives in docs/BACKLOG.md §Open and the repo's GitHub issues.

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
