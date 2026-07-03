---
name: kimi-pulse
description: >-
  Scan the latest Moonshot AI / Kimi developments — new open weights (K2
  line), org repo activity, API changes, and r/LocalLLaMA reception — and
  synthesize a digest. Use when the user asks "what's new with Kimi",
  "Kimi pulse", "Moonshot news", "Kimi K2 update", or wants open-model
  awareness alongside the other vendor pulses.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Kimi Pulse
  emoji: "📡"
  version: 1.0.0
---

# Kimi Pulse

Vendor pulse for Moonshot AI's Kimi family. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** From the skillz repo root:

   ```
   node scripts/pulse-run.ts --sources skills/kimi-pulse/sources.json [--since 30d]
   ```

   If the engine is unavailable (skill deployed standalone), read `sources.json` beside this file and fetch/search those sources directly with web tools.

2. **Fill gaps.** Check the MoonshotAI GitHub org and Hugging Face org page (weights land there first); run the searches. Kimi releases tend to arrive with strong agentic/tool-use claims — pull the community benchmark threads to test them.
3. **Synthesize.** New weights/licenses and agentic capabilities first; API/pricing changes; community verification of benchmark claims.

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the other vendor pulses.

## Output Format

```
# Kimi Pulse — [range]
## New weights, licenses & agentic claims
## API & pricing changes
## Community reception (benchmark verification)
## Notable patterns
## Sources
```

## Notes

- Hugging Face uploads frequently precede announcements — treat the org page as a primary source.
- Kimi's agentic/tool-use positioning makes it directly relevant to coding-agent model choices — flag head-to-head results against Claude/GPT/GLM when the community produces them.
