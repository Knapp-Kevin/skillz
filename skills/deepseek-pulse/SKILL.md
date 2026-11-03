---
name: deepseek-pulse
description: >-
  Scan the latest DeepSeek developments — new open weights, papers, API
  news, org repo activity, and r/LocalLLaMA reception — and synthesize a
  digest. Use when the user asks "what's new with DeepSeek", "DeepSeek
  pulse", "new DeepSeek model", or wants open-model awareness alongside
  the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: DeepSeek Pulse
  emoji: "📡"
  version: 1.1.1
---

# DeepSeek Pulse

Vendor pulse for DeepSeek. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect (external host only).** Read the bundled `sources.json` beside this skill. For the requested window (default 30 days), use only the external host's available browser, search, or connected read-only tools to check listed public pages, repositories, searches and community leads. Where a search includes `{SINCE}`, substitute the window's start date. Cite exact source URLs and publication dates, distinguish primary announcements from community reports, and label inaccessible or rate-limited sources as gaps instead of pretending to check them. Do not reveal private project context, credentials, tokens, or unapproved user data in search queries or outbound requests. If the host lacks live access, report the gap and offer an evidence-limited summary; do not invent freshness. **skillz provides no runner, crawler, script, scheduler or background job.**

2. **Fill gaps.** Check the Hugging Face org page for new weights (often the first public signal, before any blog post) and the arXiv search — DeepSeek ships papers with releases.
3. **Synthesize.** New weights/licenses and papers first; API/pricing changes (DeepSeek price moves shift the whole market — flag them); community benchmarks and quantization results.

## Scheduling

- **Optional cadence:** Weekly, and only when the user explicitly authorizes this recurring digest. Any scheduled task belongs to the external host, not this repository. A one-time research request is not authorization for continuing checks or user communications.

## Output Format

```
# DeepSeek Pulse — [range]
## New weights, papers & licenses
## API & pricing changes
## Community reception (r/LocalLLaMA)
## Notable patterns
## Sources
```

## Notes

- Hugging Face uploads frequently precede announcements — treat the org page as a primary source.
- Note anything affecting local-runtime model choices (scored against the bound runtime target, when one is bound — see inference-pulse's Bind pattern).
