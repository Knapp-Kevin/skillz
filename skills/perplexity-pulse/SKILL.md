---
name: perplexity-pulse
description: >-
  Scan the latest Perplexity developments — Sonar API and model changes,
  Comet browser, product launches, and community reception — and synthesize
  a digest. Use when the user asks "what's new with Perplexity",
  "Perplexity pulse", "Sonar API update", "Comet news", or wants
  answer-engine/search-AI awareness alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Perplexity Pulse
  emoji: "📡"
  version: 1.0.1
---

# Perplexity Pulse

Vendor pulse for Perplexity — the answer-engine/search-AI lane (Sonar API, Comet browser, enterprise search). Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect (external host only).** Read `sources.json` bundled beside this skill. For the requested window (default 30 days), use the external host's browser, search, or connected read-only tools to check listed public pages, repositories and queries. Substitute the date for `{SINCE}` in search templates. Cite exact URLs and publication dates; treat community posts as leads to verify and report inaccessible or rate-limited sources as gaps. Never send secrets, user memory or private project data in public queries. If live sources cannot be checked, disclose missing evidence rather than claiming freshness. **skillz provides no runner, crawler, script, scheduler or background service.**

2. **Fill gaps.** Fetch the API changelog and hub blog; run the searches. Perplexity ships product faster than models — separate product news (Comet, integrations) from API/model news (Sonar line, deprecations).
3. **Synthesize.** API/model deprecations and pricing first; Sonar capability changes (relevant to research-skill design — it's a search-grounding option); product moves; community sentiment.

## Scheduling

- **Optional cadence:** Weekly only with explicit user authorization for this specific recurring digest; external host scheduling only. A one-time request does not authorize repeated checks or notifications.

## Output Format

```
# Perplexity Pulse — [range]
## Sonar API & model changes (deprecations FIRST)
## Product moves (Comet, enterprise, integrations)
## Community reception
## Notable patterns
## Sources
```

## Notes

- Official sources are authoritative; community commentary is signal, not truth.
- Sonar-grounded search is a candidate backend for this repo's research series — flag API changes that affect that option.
