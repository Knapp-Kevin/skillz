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
  version: 1.0.1
---

# Gemini Pulse

Vendor pulse for Google Gemini / DeepMind. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect (external host only).** Read the bundled `sources.json` beside this skill. For the requested window (default 30 days), use only the external host's available browser, search, or connected read-only tools to check listed public pages, repositories, searches and community leads. Where a search includes `{SINCE}`, substitute the window's start date. Cite exact source URLs and publication dates, distinguish primary announcements from community reports, and label inaccessible or rate-limited sources as gaps instead of pretending to check them. Do not reveal private project context, credentials, tokens, or unapproved user data in search queries or outbound requests. If the host lacks live access, report the gap and offer an evidence-limited summary; do not invent freshness. **skillz provides no runner, crawler, script, scheduler or background job.**

2. **Fill gaps.** Fetch the Gemini API changelog and the Google AI / DeepMind blogs; run the listed searches. Google announces across several surfaces — the searches catch what the blogs miss.
3. **Synthesize.** Deprecations/quota changes first; model releases; agent tooling (gemini-cli, ADK); community sentiment.

## Scheduling

- **Optional cadence:** Weekly, and only when the user explicitly authorizes this recurring digest. Any scheduled task belongs to the external host, not this repository. A one-time research request is not authorization for continuing checks or user communications.

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
- Flag anything relevant to the Qor-logic gemini host variant (`.gemini/commands/` distribution).
