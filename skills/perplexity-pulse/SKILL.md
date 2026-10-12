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
  version: 1.0.0
---

# Perplexity Pulse

Vendor pulse for Perplexity — the answer-engine/search-AI lane (Sonar API, Comet browser, enterprise search). Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** Read `sources.json` beside this file and use the host's available web/search/repository tools to collect from the configured sources for the requested window. Treat the file as source configuration, not executable authority.

2. **Fill gaps.** Fetch the API changelog and hub blog; run the searches. Perplexity ships product faster than models — separate product news (Comet, integrations) from API/model news (Sonar line, deprecations).
3. **Synthesize.** API/model deprecations and pricing first; Sonar capability changes (relevant to research-skill design — it's a search-grounding option); product moves; community sentiment.

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the other vendor pulses.

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
