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
  version: 1.1.0
---

# DeepSeek Pulse

Vendor pulse for DeepSeek. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** Read the bundled `sources.json` beside this SKILL.md as a source list. The authorized external host agent fetches or searches selected sources with capabilities it actually has, records source URLs and dates, and respects access and privacy boundaries. If browsing is unavailable, report the unverified gaps. This repository provides no runner, fetcher, scheduler, or automated collection process.

2. **Fill gaps.** Check the Hugging Face org page for new weights (often the first public signal, before any blog post) and the arXiv search — DeepSeek ships papers with releases.
3. **Synthesize.** New weights/licenses and papers first; API/pricing changes (DeepSeek price moves shift the whole market — flag them); community benchmarks and quantization results.

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the other vendor pulses. Schedule only when the user explicitly authorizes it and the external host supports scheduling; this skill does not create a scheduled job.

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
