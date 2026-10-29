---
name: gemini-pulse
description: >-
  Scan the latest Google Gemini / DeepMind developments — model releases,
  Gemini API changelog, gemini-cli and SDK repo activity, and community
  reception — and synthesize a digest. Use when the user asks "what's new
  with Gemini", "Gemini pulse", "Google AI news", "DeepMind update digest",
  or wants competitive awareness of Google alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Gemini Pulse
  emoji: "📡"
  version: 1.0.0
---

# Gemini Pulse

Vendor pulse for Google Gemini / DeepMind. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** Read the bundled `sources.json` beside this SKILL.md as a source list. The authorized external host agent fetches or searches selected sources with capabilities it actually has, records source URLs and dates, and respects access and privacy boundaries. If browsing is unavailable, report the unverified gaps. This repository provides no runner, fetcher, scheduler, or automated collection process.

2. **Fill gaps.** Fetch the Gemini API changelog and the Google AI / DeepMind blogs; run the listed searches. Google announces across several surfaces — the searches catch what the blogs miss.
3. **Synthesize.** Deprecations/quota changes first; model releases; agent tooling (gemini-cli, ADK); community sentiment.

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the other vendor pulses for a cross-vendor view. Schedule only when the user explicitly authorizes it and the external host supports scheduling; this skill does not create a scheduled job.

## Output Format

```
# Gemini Pulse — [range]
## Releases & API changes (deprecations FIRST)
## Tooling / repo activity (gemini-cli, ADK, SDKs)
## Community reception
## Notable patterns
## Sources
```

## Notes

- Official sources are authoritative; community commentary is signal, not truth.
- When the user actually uses Gemini CLI, ADK, or another Gemini integration, flag changes affecting that authorized environment. Do not assume a Qor distribution, local command layout, or installed integration.
