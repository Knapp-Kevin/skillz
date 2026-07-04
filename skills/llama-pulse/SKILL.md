---
name: llama-pulse
description: >-
  Scan the latest Meta AI / Llama developments — new open weights, llama-stack
  and cookbook repo activity, research announcements, and r/LocalLLaMA
  reception — and synthesize a digest. Use when the user asks "what's new
  with Llama", "llama pulse", "Meta AI news", "new open weights from Meta",
  or wants open-model awareness alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Llama Pulse
  emoji: "📡"
  version: 1.1.0
---

# Llama Pulse

Vendor pulse for Meta AI's Llama family and its open-weights ecosystem. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** From the skillz repo root:

   ```
   node scripts/pulse-run.ts --sources skills/llama-pulse/sources.json [--since 30d]
   ```

   If the engine is unavailable (skill deployed standalone), read `sources.json` beside this file and fetch/search those sources directly with web tools.

2. **Fill gaps.** Fetch the Meta AI blog; run the searches. r/LocalLLaMA is the highest-signal community source for open-weights news — if the Reddit API was blocked, the site-scoped search is mandatory, not optional.
3. **Synthesize.** New weights and licenses first (license terms matter for local deployment); llama-stack/tooling changes; benchmark and quantization chatter.

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the other vendor pulses.

## Output Format

```
# Llama Pulse — [range]
## New weights & licenses
## Tooling / repo activity (llama-stack, cookbook)
## Community reception (r/LocalLLaMA)
## Notable patterns
## Sources
```

## Notes

- License changes on open weights are the deprecation-equivalent here — flag them first.
- Note anything affecting local-runtime model choices (scored against the bound runtime target, when one is bound — see inference-pulse's Bind pattern).
