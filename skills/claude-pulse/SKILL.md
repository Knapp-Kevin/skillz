---
name: claude-pulse
description: >-
  Scan the latest Claude updates directly from Anthropic's official release
  notes, blog posts, and announcements, plus top community commentary from
  Claude- and AI-coding-focused subreddits. Use when the user asks "what's
  new with Claude", "latest Claude features", "Claude update digest", "check
  Claude changelog", "Claude pulse", or wants a synthesized read on new
  Claude models, features, and community reception.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Claude Pulse
  emoji: "📡"
  version: 1.1.0
---

# Claude Pulse

Scan and synthesize the latest Claude developments from official sources and community discussion into a single digest.

## What This Does

Pulls from four source layers and synthesizes them:

1. **Official Anthropic sources** (canonical truth)
   - Claude Code CHANGELOG.md (GitHub)
   - Claude Code GitHub Releases
   - Claude Developer Platform release notes
   - Anthropic blog (claude.com/blog)

2. **Model and feature news** (official announcements)
   - New model releases (Fable/Mythos, Opus, Sonnet, Haiku)
   - Feature launches (Cowork, Managed Agents, Artifacts, plugins, etc.)
   - Deprecation and EOL notices — flag these prominently; they break active workflows

3. **Community commentary** (reception and real-world use)
   - r/ClaudeAI
   - r/coding (Claude-relevant threads)
   - r/LocalLLaMA (Claude-relevant threads)

4. **Synthesis** (the value-add — the script does NOT do this part; you do)
   - What changed since the last scan
   - What the community is saying about new features/models
   - Notable bugs, workarounds, and tips surfacing in discussion

## Execution Flow

1. **Run the fetch script** from this skill's directory. Either runtime works:

   ```
   bun run scripts/pulse.ts              # default: last 7 days
   node scripts/pulse.ts --since 30d     # Node 22.18+ runs TS natively
   ```

   The script prints a structured markdown skeleton (releases, changelog entries, Reddit threads) to stdout and diagnostics to stderr.

2. **Fill the gaps the script can't reach:**
   - If stderr notes Reddit was blocked (403 on data-center IPs), run the web-search fallback below.
   - Skim the Anthropic blog / platform notes output for anything major the changelog missed (new models, pricing, deprecations).

3. **Synthesize.** Do not just paste script output. Write the "Notable Patterns" section yourself: recurring complaints, emerging consensus, workflow tips, and anything that affects the user's active setup (deprecations first).

4. **Present the digest** in the output format below.

### If no JS runtime is available

Fall back to pure web tools: fetch the source URLs from the table below directly, and use web search for the Reddit layer. The output format is the same.

## Customizing the window

- "Claude updates from the last week" → `--since 7d` (default)
- "Claude updates from the last month" → `--since 30d`

## Reddit Discourse (web-search fallback)

Reddit's JSON API blocks data-center IPs (403). The script attempts the direct API first; when blocked, use web search to surface Reddit commentary instead. Run these searches and filter results to the `--since` window:

- `Claude site:reddit.com/r/ClaudeAI` — Claude-specific features, bugs, reactions
- `Claude Code site:reddit.com/r/coding` — coding-agent workflows and comparisons
- `Claude site:reddit.com/r/LocalLLaMA` — technical model analysis and benchmarks

Focus on: new-feature reactions, model quality comparisons, workflow tips, breaking-change complaints, and notable praise or criticism. Quote scores/upvotes when visible. Link the original threads.

## Scheduling

This skill pairs well with a recurring run (e.g., every Monday morning):

- **Claude Code:** use `/schedule` to create a weekly routine that runs this skill and posts the digest, or `/loop` for an in-session interval.
- **Other agent platforms:** create a scheduled task/automation whose instruction is "Run the claude-pulse skill and post the digest."

## Output Format

```
# Claude Pulse — [Date Range]

## Official Releases
### Claude Code
- v2.1.199 (Jul 2): [key changes]
- v2.1.198 (Jul 1): [key changes]

### Models & Platform
- [New model/feature announcement]
- [Deprecation notice if any — put these FIRST]

## Community Commentary
### r/ClaudeAI (top threads)
- [Thread title] — [key insight from discussion]

### r/coding & r/LocalLLaMA (Claude-relevant)
- [Thread title] — [key insight]

## Notable Patterns
- [Recurring theme across sources: bug reports, praise, tips]
- [Emerging consensus or disagreement]

## Sources
- [Links to all primary sources scanned]
```

## Source URLs (canonical)

| Source | URL |
|--------|-----|
| Claude Code CHANGELOG | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md |
| Claude Code Releases | https://github.com/anthropics/claude-code/releases |
| Claude Dev Platform Notes | https://platform.claude.com/docs/en/release-notes/overview.md |
| Anthropic Blog | https://claude.com/blog |
| Releasebot (aggregator) | https://releasebot.io/updates/anthropic/claude |
| r/ClaudeAI | https://www.reddit.com/r/ClaudeAI/ |
| r/coding | https://www.reddit.com/r/coding/ |
| r/LocalLLaMA | https://www.reddit.com/r/LocalLLaMA/ |

## Notes

- Official sources are authoritative. Community commentary is signal, not truth.
- The script filters Reddit by relevance (Claude, Anthropic, coding-agent mentions) to avoid noise.
- Model deprecations and EOL dates are flagged prominently since they affect active workflows.
