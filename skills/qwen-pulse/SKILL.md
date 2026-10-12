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
  version: 1.1.0
---

# Qwen Pulse

Vendor pulse for Alibaba's Qwen family. Sources are data (`sources.json`), synthesis is yours.

## Execution Flow

1. **Collect.** From the skillz repo root:

   Read the bundled `sources.json` in this skill folder. Use authorized host browsing or connected search tools to inspect selected sources, keep source dates and URLs, and state which sources were unavailable. No repository-owned runner, script, or automatic collection process exists.

   The external host selects the available approved web/API capabilities; unavailable retrieval is reported as an evidence gap, not silently filled.

2. **Fill gaps.** Fetch the Qwen blog and Hugging Face org page (weights often land there first); run the searches. QwenLM org activity is broad — filter to model releases, agent tooling (qwen-code), and inference kernels.
3. **Synthesize.** New weights/licenses first; agent-tooling changes; community benchmarks and quantization results.

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the other vendor pulses. Scheduling is a separate host action requiring explicit user authorization; the repository never schedules runs.

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
- Note anything affecting local-runtime model choices (scored against the bound runtime target, when one is bound — see inference-pulse's Bind pattern).
