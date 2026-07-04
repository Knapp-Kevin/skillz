---
name: glm-pulse
description: >-
  Scan the latest z.ai / Zhipu GLM developments — new open weights, org
  repo activity (zai-org, THUDM), API and coding-plan changes, and
  r/LocalLLaMA reception — and synthesize a digest. Use when the user asks
  "what's new with GLM", "GLM pulse", "z.ai news", "Zhipu update", or wants
  open-model awareness alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: GLM Pulse
  emoji: "📡"
  version: 1.1.0
---

# GLM Pulse

Vendor pulse for z.ai (Zhipu) and the GLM family. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** From the skillz repo root:

   ```
   node scripts/pulse-run.ts --sources skills/glm-pulse/sources.json [--since 30d]
   ```

   If the engine is unavailable (skill deployed standalone), read `sources.json` beside this file and fetch/search those sources directly with web tools.

2. **Fill gaps.** Check both GitHub orgs (releases have moved between THUDM and zai-org) and the Hugging Face org page — weights often land there before the blog post. Run the searches; the coding-plan/API-pricing one matters because GLM competes aggressively on price.
3. **Synthesize.** New weights/licenses first; API and coding-plan pricing moves (these shift agent-runtime economics); agent/coding tooling; community benchmarks.

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the other vendor pulses.

## Output Format

```
# GLM Pulse — [range]
## New weights & licenses
## API & pricing moves
## Community reception (r/LocalLLaMA)
## Notable patterns
## Sources
```

## Notes

- Hugging Face uploads frequently precede announcements — treat the org page as a primary source.
- Note anything affecting local-runtime model choices or coding-agent cost baselines (scored against the bound runtime target, when one is bound — see inference-pulse's Bind pattern).
