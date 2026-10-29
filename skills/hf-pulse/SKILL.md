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

1. **Prefer connected HF MCP tools** for relevant source-specific retrieval:
   - `paper_search` — this window's notable papers (query by topic: agents, memory, reasoning)
   - `hub_repo_search` / `hub_repo_details` — trending models and datasets
   - `space_search` — trending spaces (often the earliest demo signal)

   Limit routine discovery to public Hub metadata. A connected tool may expose private or gated repositories, account history, or restricted datasets; tool access is not permission to inspect them. Do not retrieve private content, token-bearing links, or personal account details without separately approved scope. If public-only filtering cannot be established, use public browsing and report the connected-tool coverage gap.

2. **Collect remaining sources** using the external host's authorized tools:

   Read the bundled `sources.json` in this skill folder. Use authorized host browsing or connected search tools to inspect selected sources, keep source dates and URLs, and state which sources were unavailable. No repository-owned runner, script, or automatic collection process exists.

   The external host selects the available approved web/API capabilities; unavailable retrieval is reported as an evidence gap, not silently filled.

3. **Fill gaps.** Fetch the HF blog and daily-papers page; run the searches.
4. **Synthesize.** Trending models with *why* they're trending (new SOTA? small-and-runnable? meme?); paper themes, not paper lists; library releases that affect downstream tooling.

## Optional recurrence (external host only)

Weekly review is a suggestion, not a standing instruction. This skill defaults to **one requested read-only digest**. Do not invoke `/schedule`, `/loop`, scheduler APIs, or notification tools merely because a cadence is mentioned.

Before an external host creates a recurring run, obtain **separate explicit user approval** for frequency, local time and timezone, end/expiry condition, exact future public and private source/account/workspace access scope, report recipients and delivery channel (including notifications), data minimization and retention/deletion, recurring cost or external egress, and pause/revocation controls. Private or gated content and any disclosure of user/workspace context require their own scoped approval. Recheck authorization and access at each future run; stop rather than silently broaden scope.

Only an authorized external host with a suitable capability may configure the approved routine. If unavailable, provide a reusable one-time prompt or manual reminder instead. Never persist credentials, token-bearing URLs, sensitive documents, or private message bodies in schedule prompts, logs, or reports. `skillz` has no scheduler, runner, or delivery service.

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
