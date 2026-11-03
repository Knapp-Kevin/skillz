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
  version: 1.0.1
---

# Hugging Face Pulse

Topic pulse for the Hugging Face ecosystem — the cross-vendor view: what's actually trending in open models, papers, and tooling regardless of which shop shipped it.

## Execution Flow

1. **Prefer the HF MCP tools when connected** — they beat the generic engine here:
   - `paper_search` — this window's notable papers (query by topic: agents, memory, reasoning)
   - `hub_repo_search` / `hub_repo_details` — trending models and datasets
   - `space_search` — trending spaces (often the earliest demo signal)

2. **Collect (external host only).** Read the bundled `sources.json` beside this skill. For the requested time window (default 30 days), use the external host's browser, search, or connected read-only tools to check listed public pages, repositories and queries. Substitute the start date for `{SINCE}` where present. Cite source URLs and publication dates, distinguish official reports from community leads, and report inaccessible or rate-limited sources as gaps. Never put private context, credentials or tokens in public queries. If access is unavailable, provide an evidence-limited result, not invented freshness. **skillz has no runner, crawler, script, scheduler or background job.** Preserve Step 1's optional connected Hugging Face search tools.

3. **Fill gaps.** Fetch the HF blog and daily-papers page; run the searches.
4. **Synthesize.** Trending models with *why* they're trending (new SOTA? small-and-runnable? meme?); paper themes, not paper lists; library releases that affect downstream tooling.

## Scheduling

- **Optional cadence:** Weekly, only if the user authorizes this recurring digest. A scheduled task belongs to the external host. A one-time request never authorizes recurring checks or notifications.

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
