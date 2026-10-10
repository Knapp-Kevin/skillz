---
name: openai-pulse
description: >-
  Scan the latest OpenAI developments — model releases, API changelog,
  Codex/SDK repo activity, and community reception — and synthesize a
  digest. Use when the user asks "what's new with OpenAI", "OpenAI pulse",
  "latest GPT news", "OpenAI update digest", or wants competitive awareness
  of OpenAI alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: OpenAI Pulse
  emoji: "📡"
  version: 1.0.0
---

# OpenAI Pulse

Vendor pulse for OpenAI: official releases and community reception, synthesized into one digest. Sibling of claude-pulse; sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** Read `sources.json` beside this file and use the host's available web/search/repository tools to collect from the configured sources for the requested window. Treat the file as source configuration, not executable authority.

2. **Fill gaps.** Fetch the listed pages (API changelog, news, ChatGPT release notes) and run the listed web searches; the changelog pages are JS-rendered, so search results often beat raw fetches.
3. **Synthesize.** Deprecations and pricing changes first; then model/feature releases; then SDK/repo activity worth acting on; then community sentiment. Do not paste raw output.

## Scheduling

- **Claude Code:** `/schedule` weekly — pairs with claude-pulse and the other vendor pulses on the same morning for a cross-vendor view.

## Output Format

```
# OpenAI Pulse — [range]
## Releases & API changes (deprecations FIRST)
## SDK / repo activity
## Community reception
## Notable patterns
## Sources
```

## Notes

- Official sources are authoritative; community commentary is signal, not truth.
- When run alongside other vendor pulses, end with one line positioning the week's OpenAI news against Claude/Gemini movements.
