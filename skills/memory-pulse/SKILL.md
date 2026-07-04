---
name: memory-pulse
description: >-
  Scan the agentic-memory and context-engineering ecosystem — memory
  frameworks (Letta, Mem0, Zep, cognee), new papers, new repos, and
  community discussion — and synthesize a digest. Use when the user asks
  "memory pulse", "what's new in agent memory", "context engineering news",
  "agentic memory papers", or wants ecosystem awareness feeding the
  operator's bound memory-layer project and agent memory architecture
  decisions.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Memory Pulse
  emoji: "🧠"
  version: 1.1.0
---

# Memory Pulse

Topic pulse for agentic memory: long-term memory frameworks, context engineering, knowledge-graph memory, and the research frontier. Feeds the operator's bound memory-layer project and agent-architecture decisions. **Bind:** discover the memory-layer project from an operator profile or project governance doc — when none is bound, the verdict goes generic (relevance to a typical agent-memory layer) and the skill offers to bind one for next time.

## Execution Flow

1. **Collect.** From the skillz repo root:

   ```
   node scripts/pulse-run.ts --sources skills/memory-pulse/sources.json [--since 30d]
   ```

   If the engine is unavailable (skill deployed standalone), read `sources.json` beside this file and fetch/search those sources directly with web tools.

2. **Fill gaps.** Run the arXiv/paper searches (the Hugging Face MCP `paper_search` tool is ideal when connected); fetch the Letta/Mem0 blogs; review the new-repo search hits for genuinely novel approaches vs wrappers.
3. **Synthesize.** Breaking architecture ideas first (temporal KGs, memory consolidation, sleep-time compute); framework releases and API changes; benchmarks; what's hype vs load-bearing.

## Scheduling

- **Claude Code:** `/schedule` weekly or biweekly — the research cadence justifies weekly, framework churn does not.

## Output Format

```
# Memory Pulse — [range]
## Research frontier (papers, with one-line takeaways)
## Framework releases (Letta, Mem0, Zep, cognee, new entrants)
## New repos worth a look (filtered from search hits)
## Relevance to the bound memory layer / agent memory
## Notable patterns
## Sources
```

## Notes

- The relevance section is the point — every digest ends with "what, if anything, should change in our memory architecture" (usually: nothing yet).
- Promising frameworks become registry `track` candidates, not immediate adoptions.
