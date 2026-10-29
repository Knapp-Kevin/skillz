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

   **Resolve source-query windows.** `sources.json` is inert source configuration. For each `github_search[].q` containing `{SINCE}`, substitute a UTC `YYYY-MM-DD` date at the beginning of the requested report window before querying GitHub. If the user supplied no window, use the preceding seven days and label that default in the report. GitHub date-only `created:>` filters are approximate window boundaries, not proof of complete coverage. Never submit a literal `{SINCE}` placeholder, execute the source file, or imply an unexecuted search succeeded; record unavailable tools and incomplete results as evidence gaps.

2. **Fill gaps.** Fetch github.com/trending (weekly view) — the search API measures new repos, trending measures acceleration of existing ones; both matter. HN/Reddit searches catch the story behind a spike.
3. **Filter.** For each candidate: real code or README-ware? active maintainer? does it duplicate something we already vendored/adopted (check INDEX.md and the registry)?
4. **Synthesize.** One line per repo max; group by category; end with at most 3 "worth a deeper look" picks and why.

## Optional recurrence (external host only)

Weekly review is a suggestion, not a standing instruction. This skill defaults to **one requested read-only digest**. Do not invoke `/schedule`, `/loop`, scheduler APIs, or notification tools merely because a cadence is mentioned.

Before an external host creates a recurring run, obtain **separate explicit user approval** for frequency, local time and timezone, end/expiry condition, exact future public and private source/account/workspace access scope, report recipients and delivery channel (including notifications), data minimization and retention/deletion, recurring cost or external egress, and pause/revocation controls. Private or gated content and any disclosure of user/workspace context require their own scoped approval. Recheck authorization and access at each future run; stop rather than silently broaden scope.

Only an authorized external host with a suitable capability may configure the approved routine. If unavailable, provide a reusable one-time prompt or manual reminder instead. Never persist credentials, token-bearing URLs, sensitive documents, or private message bodies in schedule prompts, logs, or reports. `skillz` has no scheduler, runner, or delivery service.

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
- Handoff: skill-shaped finds go to governed skill-source intake's registry-proposal flow; tool-shaped finds can become BACKLOG items.
