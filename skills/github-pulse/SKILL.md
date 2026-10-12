---
name: github-pulse
description: >-
  Scan GitHub for the week's hottest new repositories — overall and
  AI-centric (LLM tooling, agent frameworks, MCP servers, dev tools) —
  and synthesize a digest of what's worth attention. Use when the user
  asks "github pulse", "what's trending on GitHub", "new AI repos this
  week", "top new repositories", or wants a repo-radar feeding the skills
  registry and tooling decisions.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: GitHub Pulse
  emoji: "⭐"
  version: 1.0.0
---

# GitHub Pulse

Topic pulse for new and trending GitHub repositories, AI-centric first. Star velocity is a discovery signal, not a quality signal — the digest's job is separating durable tools from hype spikes.

## Execution Flow

1. **Collect.** Read the bundled `sources.json` beside this SKILL.md as a source list. The authorized external host agent fetches or searches selected sources with capabilities it actually has, records source URLs and dates, and respects access and privacy boundaries. If browsing is unavailable, report the unverified gaps. This repository provides no runner, fetcher, scheduler, or automated collection process.

2. **Fill gaps.** Fetch github.com/trending (weekly view) — the search API measures new repos, trending measures acceleration of existing ones; both matter. HN/Reddit searches catch the story behind a spike.
3. **Filter.** For each candidate: real code or README-ware? active maintainer? does it duplicate something we already vendored/adopted (check INDEX.md and the registry)?
4. **Synthesize.** One line per repo max; group by category; end with at most 3 "worth a deeper look" picks and why.

## Scheduling

- **Claude Code:** `/schedule` weekly — pairs naturally with skills-pulse (repos found here often become skill/tool intake candidates there). Schedule only when the user explicitly authorizes it and the external host supports scheduling; this skill does not create a scheduled job.

## Output Format

```
# GitHub Pulse — [range]
## Hottest new repos (overall)
## AI / LLM / agents
## MCP & dev tooling
## Worth a deeper look (max 3, with reasons)
## Sources
```

## Notes

- When the host has access to the current skillz candidate-intake registry, cross-check picks against its rejected and already-reviewed entries before recommending. Without access, mark the duplicate/rejection check `not-run` and offer a bounded intake proposal; do not assume the registry is bundled with this skill.
- Handoff: skill-shaped finds go to skills-pulse's registry-proposal flow; tool-shaped finds can become BACKLOG items.
