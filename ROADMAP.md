# Roadmap — planned skill series

The repo's purpose is skills that run on a **daily or weekly cadence**, either invoked manually or wired to `/schedule` / agent automations. Four coherent series, ordered roughly by value-per-effort. Each skill follows the claude-pulse pattern: a small fetch/collect script (Bun/Node TS, zero install) plus a SKILL.md that makes the model do the synthesis.

## 1. Pulse series — external awareness (weekly)

Siblings of `claude-pulse`: same digest shape, different domain.

| Skill | What it digests | Sources |
|-------|-----------------|---------|
| `repo-pulse` | Activity across your GitHub repos: commits, PRs needing review, stale branches, CI failures, new issues | `gh` CLI (already authenticated locally) |
| `deps-pulse` | Dependency updates and CVEs across active projects | `npm outdated`/`npm audit`, `cargo audit`, GitHub advisories |
| `ai-pulse` | Broader AI ecosystem beyond Claude: notable papers, model releases, tooling | Hugging Face MCP (paper_search, hub_repo_search), web search |
| `tauri-pulse` | Tauri/Rust ecosystem releases and breaking changes (you maintain Tauri 2 projects and a large tauri2-* skill set) | GitHub releases for tauri-apps/*, crates.io, Tauri blog |

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
| `skill-audit` | Validate every `skills/*/SKILL.md`: frontmatter completeness, description quality (does it say *when* to use?), script runnability, dead links. Also lint `registry/candidates.yaml` entries against the evaluation framework. Run before syncing anywhere. |
| `skill-sync` | Deploy skills from this repo to their consumers: symlinks into `~/.claude/skills/`, per-host copies following Qor-logic's `dist_compile` pattern (`.claude/`, `.kilo/`, `.codex/`, `.gemini/`), and generated COREFORGE Synapse `manifest.json` (skillId, permissions, runtime derived from frontmatter). Idempotent; reports drift. |
| `memory-distill` | Weekly consolidation of Claude Code's persistent memory: merge duplicates, expire stale project facts, tighten the MEMORY.md index. |

## Suggested build order

1. `repo-pulse` — highest leverage, `gh` does the heavy lifting, template already exists (claude-pulse).
2. `daily-briefing` — the anchor habit the other daily skills feed into.
3. `skill-sync` + `skill-audit` — once ~3 skills exist, deployment and validation pay for themselves.
4. `repo-doctor` and `standup-writer` — both are mostly git plumbing.
5. Everything else as the cadence proves itself.

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
