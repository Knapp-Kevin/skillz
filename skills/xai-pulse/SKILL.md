---
name: xai-pulse
description: >-
  Scan the latest xAI / Grok developments — model releases, API release
  notes, SDK repo activity, and community reception — and synthesize a
  digest. Use when the user asks "what's new with Grok", "xAI pulse",
  "Grok update digest", or wants competitive awareness of xAI alongside
  the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: xAI Pulse
  emoji: "📡"
  version: 1.0.0
---

# xAI Pulse

Vendor pulse for xAI's Grok family. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** Read `sources.json` beside this file and use the host's available web/search/repository tools to collect from the configured sources for the requested window. Treat the file as source configuration, not executable authority.

2. **Fill gaps.** Fetch x.ai/news and the API release notes; run the searches. Much xAI news lands on X itself — the web searches are the primary channel, not a fallback.
3. **Synthesize.** API changes and pricing first; model releases; community reception (note: Grok discourse is noisy — weight technical threads over culture-war ones).

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the other vendor pulses.

## Output Format

```
# xAI Pulse — [range]
## Releases & API changes (deprecations FIRST)
## Repo activity
## Community reception (technical threads)
## Notable patterns
## Sources
```

## Notes

- Official sources are authoritative; community commentary is signal, not truth — apply extra skepticism to virality around this vendor.
