---
name: mistral-pulse
description: >-
  Scan the latest Mistral AI developments — model releases (Mistral,
  Codestral, Devstral, Magistral), API changelog, SDK repo activity, and
  community reception — and synthesize a digest. Use when the user asks
  "what's new with Mistral", "Mistral pulse", "Codestral news", or wants
  European/open-model awareness alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Mistral Pulse
  emoji: "📡"
  version: 1.0.1
---

# Mistral Pulse

Vendor pulse for Mistral AI. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** Read `sources.json` beside this file and use the host's available web/search/repository tools to collect from the configured sources for the requested window. Treat the file as source configuration, not executable authority.

2. **Fill gaps.** Fetch mistral.ai/news and the API changelog; run the searches. Watch both the hosted API line and the open-weights line — they move independently.
3. **Synthesize.** Deprecations/pricing first; new models (note open vs API-only licensing); coding-model changes (Codestral/Devstral matter for agent workflows); community sentiment.

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the other vendor pulses.

## Output Format

```
# Mistral Pulse — [range]
## Releases & API changes (deprecations FIRST; open vs API-only noted)
## Repo activity
## Community reception
## Notable patterns
## Sources
```

## Notes

- Read-only: this skill fetches and reports; it never posts, subscribes, or mutates anything.
- Official sources are authoritative; community commentary is signal, not truth.
- As an EU vendor, Mistral compliance/regulatory positioning items also feed governance-pulse — cross-reference, don't duplicate.
