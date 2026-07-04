---
name: hf-pulse
description: >-
  Scan the Hugging Face ecosystem — trending models/datasets/spaces, daily
  papers, HF blog, and library releases (transformers, smolagents, hub) —
  and synthesize a digest. Use when the user asks "huggingface pulse",
  "what's trending on Hugging Face", "HF papers this week", "new models on
  the hub", or wants open-model ecosystem awareness across all vendors at
  once.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Hugging Face Pulse
  emoji: "🤗"
  version: 1.0.0
---

# Hugging Face Pulse

Topic pulse for the Hugging Face ecosystem — the cross-vendor view: what's actually trending in open models, papers, and tooling regardless of which shop shipped it.

## Execution Flow

1. **Prefer the HF MCP tools when connected** — they beat the generic engine here:
   - `paper_search` — this window's notable papers (query by topic: agents, memory, reasoning)
   - `hub_repo_search` / `hub_repo_details` — trending models and datasets
   - `space_search` — trending spaces (often the earliest demo signal)

2. **Collect the rest** with the shared engine, from the skillz repo root:

   ```
   node scripts/pulse-run.ts --sources skills/hf-pulse/sources.json [--since 30d]
   ```

   If MCP tools are absent and the engine is unavailable (skill deployed standalone), read `sources.json` beside this file and fetch/search those sources directly with web tools.

3. **Fill gaps.** Fetch the HF blog and daily-papers page; run the searches.
4. **Synthesize.** Trending models with *why* they're trending (new SOTA? small-and-runnable? meme?); paper themes, not paper lists; library releases that affect downstream tooling.

## Scheduling

- **Claude Code:** `/schedule` weekly, same morning as the vendor pulses — this is the cross-vendor summary that ties them together.

## Output Format

```
# Hugging Face Pulse — [range]
## Trending models (with the why)
## Papers: this week's themes
## Library & platform releases (transformers, hub, smolagents)
## Trending spaces / demos
## Notable patterns
## Sources
```

## Notes

- Trending is engagement, not quality — say which it is per item.
- Cross-reference vendor pulses: a model trending here usually has a home in one of them; link, don't duplicate.
