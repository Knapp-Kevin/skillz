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
  version: 1.0.1
---

# xAI Pulse

Vendor pulse for xAI's Grok family. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect (external host only).** Read `sources.json` bundled beside this skill. For the requested window (default 30 days), use the external host's browser, search, or connected read-only tools to check listed public pages, repositories and queries. Substitute the date for `{SINCE}` in search templates. Cite exact URLs and publication dates; treat community posts as leads to verify and report inaccessible or rate-limited sources as gaps. Never send secrets, user memory or private project data in public queries. If live sources cannot be checked, disclose missing evidence rather than claiming freshness. **skillz provides no runner, crawler, script, scheduler or background service.**

2. **Fill gaps.** Fetch x.ai/news and the API release notes; run the searches. Much xAI news lands on X itself — the web searches are the primary channel, not a fallback.
3. **Synthesize.** API changes and pricing first; model releases; community reception (note: Grok discourse is noisy — weight technical threads over culture-war ones).

## Scheduling

- **Optional cadence:** Weekly only with explicit user authorization for this specific recurring digest; external host scheduling only. A one-time request does not authorize repeated checks or notifications.

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
