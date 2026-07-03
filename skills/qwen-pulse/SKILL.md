---
name: qwen-pulse
description: >-
  Scan the latest Qwen (Alibaba) developments — new open weights, QwenLM
  org repo activity, blog posts, and r/LocalLLaMA reception — and
  synthesize a digest. Use when the user asks "what's new with Qwen",
  "Qwen pulse", "new Qwen model", or wants open-model awareness alongside
  the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Qwen Pulse
  emoji: "📡"
  version: 1.0.0
---

# Qwen Pulse

Vendor pulse for Alibaba's Qwen family. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** From the skillz repo root:

   ```
   node scripts/pulse-run.ts --sources skills/qwen-pulse/sources.json [--since 30d]
   ```

   If the engine is unavailable (skill deployed standalone), read `sources.json` beside this file and fetch/search those sources directly with web tools.

2. **Fill gaps.** Fetch the Qwen blog and Hugging Face org page (weights often land there first); run the searches. QwenLM org activity is broad — filter to model releases, agent tooling (qwen-code), and inference kernels.
3. **Synthesize.** New weights/licenses first; agent-tooling changes; community benchmarks and quantization results.

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the other vendor pulses.

## Output Format

```
# Qwen Pulse — [range]
## New weights & licenses
## Tooling / repo activity (qwen-code, kernels)
## Community reception (r/LocalLLaMA)
## Notable patterns
## Sources
```

## Notes

- Hugging Face uploads frequently precede blog posts — treat the org page as a primary source.
- Note anything affecting local-runtime (GG-CORE) model choices.
