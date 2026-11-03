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
  version: 1.0.1
---

# GitHub Pulse

Topic pulse for new and trending GitHub repositories, AI-centric first. Star velocity is a discovery signal, not a quality signal — the digest's job is separating durable tools from hype spikes.

## Execution Flow

1. **Collect (external host only).** Read the bundled `sources.json` beside this skill. For the requested time window (default 30 days), use the external host's browser, search, or connected read-only tools to check listed public pages, repositories and queries. Substitute the start date for `{SINCE}` where present. Cite source URLs and publication dates, distinguish official reports from community leads, and report inaccessible or rate-limited sources as gaps. Never put private context, credentials or tokens in public queries. If access is unavailable, provide an evidence-limited result, not invented freshness. **skillz has no runner, crawler, script, scheduler or background job.** GitHub rate limits can block some queries: use only existing host-authorized access, never require users to provide a GitHub token.

2. **Fill gaps.** Fetch github.com/trending (weekly view) — the search API measures new repos, trending measures acceleration of existing ones; both matter. HN/Reddit searches catch the story behind a spike.
3. **Filter.** For each candidate: real code or README-ware? active maintainer? does it duplicate something we already vendored/adopted (check INDEX.md and the registry)?
4. **Synthesize.** One line per repo max; group by category; end with at most 3 "worth a deeper look" picks and why.

## Scheduling

- **Optional cadence:** Weekly, only if the user authorizes this recurring digest. A scheduled task belongs to the external host. A one-time request never authorizes recurring checks or notifications.

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

- Cross-check picks against `registry/candidates.yaml` before recommending — a repo already rejected there needs new evidence, not a re-pitch.
- Handoff: skill-shaped finds go to skills-pulse's registry-proposal flow; tool-shaped finds can become BACKLOG items.
