---
name: skills-pulse
description: >-
  Scan the agent-skills ecosystem for new and updated skills across the
  official vendor repos (Anthropic, Vercel, Microsoft, Azure, AWS) and
  community marketplaces, then propose intake candidates for the registry.
  Use when the user asks "skills pulse", "any new agent skills", "scan the
  skill watchlist", "update the skill registry", or on a weekly intake
  schedule.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skills Pulse
  emoji: "🧭"
  version: 1.1.0
---

# Skills Pulse

Weekly intake scan of the agent-skills ecosystem. Finds what's new, filters it against what we already have, and proposes registry candidates — it does **not** install anything.

## What This Does

1. **Watchlist repo scan** (script) — commits and releases on the official skill repos, flagging vendored submodules that have upstream activity.
2. **Marketplace sweep** (web search) — new/trending skills on the directories that have no API.
3. **Redundancy filter** (you) — drop anything already covered by Qor-logic, Claude Code built-ins, vendored repos, or this repo's roadmap.
4. **Candidate proposals** (you) — ready-to-paste YAML entries for `registry/candidates.yaml`, scored per the evaluation framework.

## Execution Flow

1. **Run the scan script** from this skill's directory (either runtime works; set `GITHUB_TOKEN` to avoid rate limits):

   ```
   node scripts/scout.ts               # default: last 7 days
   bun run scripts/scout.ts --since 30d
   ```

2. **Sweep the no-API marketplaces** with web search, filtered to the window:
   - `new agent skills site:skills.sh`
   - `Claude skills site:mcpmarket.com`
   - `site:awesomeclaude.ai skills` — new entries
   - `agent skills site:agentskills.io OR site:skills-directory.com`
   - `Claude Code skills` on Hacker News / Reddit for notable community launches

3. **Filter for redundancy** — this is the step that keeps the repo from becoming counterproductive by excess. For each find, check in order (reject with a `covered_by` note if matched):
   1. `registry/candidates.yaml` — already decided?
   2. `INDEX.md` — already vendored or local?
   3. Qor-logic (`../Qor-logic/qor/skills/`) — gated/SDLC territory?
   4. Claude Code built-ins (`/code-review`, `/security-review`, `/verify`)
   5. This repo's ROADMAP — planned first-party?

4. **Submodule freshness.** Report per vendored source: current pinned SHA, latest upstream SHA or release where detectable (`git ls-remote <url> HEAD`; releases via `gh api repos/<owner>/<repo>/releases/latest` when `gh` is available), a refresh-needed verdict, and the likely classification of the delta — docs-only / skill-content / tooling — inferred from upstream commit paths. Refreshing itself follows `docs/vendor-freshness.md` (the governing workflow: one source at a time, review before commit, re-index in the same commit, registry re-check on skill-content or tooling deltas):

   ```
   git submodule update --remote vendor/<source>
   git -C vendor/<source> log --oneline --stat <old-pin>..HEAD
   node scripts/build-index.ts
   ```

5. **Propose candidates.** For each genuinely new, non-redundant find, draft a registry entry (id, name, source, category, status — usually `track` or `sandbox` — permission_tier, rationale) per `docs/evaluation-framework.md`. Do NOT edit the registry without presenting the proposals first, and never install or symlink anything as part of this skill.

### If no JS runtime is available

Fetch each watchlist repo's releases/commits pages on GitHub directly and do the marketplace sweep via web search; the rest of the flow is unchanged.

## Scheduling

- **Claude Code:** `/schedule` weekly (pairs well with claude-pulse on Monday mornings).
- **Other agent platforms:** scheduled automation whose instruction is "Run the skills-pulse skill and present the intake digest."

## Output Format

```
# Skills Pulse — [Date Range]

## Watchlist activity
- [repo]: [n commits / release vX.Y] — [what changed, one line]

## Submodule freshness
| Source | Pinned | Upstream | Refresh? | Likely delta |
|--------|--------|----------|----------|--------------|
| [vendor/x] | [sha] | [sha / release] | [yes/no] | [docs-only / skill-content / tooling] |

## New candidates (non-redundant)
### [skill name] — [source]
[what it does, one line]
Proposed registry entry:
​```yaml
- id: ...
  status: track
  ...
​```

## Filtered out (redundant)
- [name] — covered by [Qor-logic skill / built-in / vendored path]
```

## Notes

- Discovery signals (stars, installs) are not quality signals. Default new candidates to `track`, not `sandbox`, unless there's a concrete recurring workflow waiting.
- Anything touching browser sessions, payments, identity, or credentials is proposed as `quarantined` regardless of appeal.
- This skill is read-only: it proposes registry entries and submodule refreshes; a human (or an explicitly approved follow-up) applies them.
