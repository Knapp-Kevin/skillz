---
name: claude-pulse
description: >-
  Research and synthesize the latest Claude developments from official Anthropic
  sources plus relevant community discussion. Use when the user asks what is new
  with Claude, requests a Claude update digest, wants recent model or product
  changes, or wants community reception summarized.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Claude Pulse
  emoji: "📡"
  version: 2.0.0
---

# Claude Pulse

This skill is a passive research procedure. `skillz` does not fetch, monitor, schedule, or execute anything. The external agent performs the research using whatever current web/search/repository capabilities its host provides.

## Source priority

Use four evidence layers:

1. **Official Anthropic sources**
   - Claude/Anthropic release notes and documentation;
   - Claude Code changelog and releases;
   - Anthropic product/model announcements and blog posts;
   - official deprecation or migration notices.

2. **Current model and feature changes**
   - new models or model revisions;
   - API/product feature changes;
   - pricing, limits, compatibility, or migration changes when material;
   - deprecations and end-of-life notices.

3. **Community commentary**
   - relevant practitioner discussion on Reddit, Hacker News, GitHub, or other credible community surfaces;
   - recurring bugs, workarounds, workflow observations, praise, criticism, and disagreements.

4. **Synthesis**
   - what materially changed;
   - what users appear to notice in practice;
   - which claims are official fact versus community experience;
   - what may affect the user's workflows.

## Procedure

1. Resolve the requested time window.
2. Search official sources first and establish the dated factual changes.
3. Prioritize deprecations, migrations, security changes, pricing/limit changes, and workflow-breaking changes.
4. Search community sources for reactions specifically tied to those changes.
5. Separate repeated community patterns from isolated anecdotes.
6. Verify important claims against primary sources when possible.
7. Synthesize rather than dumping links or search results.
8. Cite the sources used according to the host agent's normal citation capabilities.

## Output

```text
# Claude Pulse — [Date Range]

## What changed
- [material official change]

## What matters
- [workflow/compatibility/deprecation implication]

## Community reception
- [recurring pattern, with appropriate uncertainty]

## Watch items
- [things announced but not yet settled, verified, or broadly available]

## Sources
- [primary and community evidence]
```

## Rules

- Official sources control factual product/model claims.
- Community commentary is experience evidence, not canonical truth.
- Do not invent dates, release numbers, adoption levels, scores, or sentiment.
- Do not treat a single popular thread as consensus.
- When the requested answer depends on current information, the external agent must retrieve current sources rather than rely on stale memory.
- Scheduling, if the user requests it, is created by the external host agent. Nothing inside `skillz` runs on a schedule.
