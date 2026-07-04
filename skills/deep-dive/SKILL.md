---
name: deep-dive
description: >-
  Build a multi-source research dossier on any topic: scope it, sweep
  sources in parallel angles, adversarially fact-check the load-bearing
  claims, and synthesize a cited report. Use when the user asks
  "deep dive on X", "research X thoroughly", "give me a dossier on X",
  "what's the real story with X", or wants a fact-checked, multi-source
  answer rather than a quick summary.
metadata:
  author: frostwulf.zo.computer
  category: Research
  display-name: Deep Dive
  emoji: "🔬"
  version: 1.0.0
---

# Deep Dive

A research dossier that separates what is established from what is opinion and what is still open. The value over a plain web search is the adversarial pass: every claim the conclusion rests on gets an active refutation attempt before it is allowed in.

## Execution Flow

1. **Scope.** If the question is genuinely ambiguous, ask 2-3 clarifying questions (time horizon, decision at stake, depth wanted) and agree on success criteria. If the question is already specific, skip this — do not interrogate a clear request.
2. **Sweep in parallel angles.** Search and fetch across four distinct source lanes rather than one query rephrased four ways: official documentation and primary announcements; independent analyses and benchmarks; community experience (issues, forums, practitioner posts); contrarian or critical takes. When a connected MCP tool covers a lane better — e.g., Hugging Face `paper_search` for research literature — use it instead of general web search.
3. **Fact-check adversarially.** List the load-bearing claims (the ones the conclusion would collapse without) and try to REFUTE each: search for counter-evidence, check the primary source behind secondary reports, check dates for staleness. A claim survives only if the refutation attempt fails.
4. **Synthesize.** Write the dossier with every finding labeled as established fact, informed opinion, or open question, each with citations. Confidence labels reflect the fact-check results, not source enthusiasm.

## Output Format

```
# Deep Dive — [topic] ([date])
## TL;DR (3-5 sentences, confidence stated)
## Findings by theme
### [Theme]
- [Finding] — [fact | opinion | open question] (confidence: high/medium/low) [citations]
## What would change this
- [Evidence that would overturn each major conclusion]
## Open questions
## Sources (with dates)
```

## Notes

- Read-only: this skill searches and reads; it never posts, subscribes, or mutates anything.
- Source authority ordering: primary sources > independent analyses > community reports > aggregators. Never cite an aggregator when its primary source is reachable.
- If two credible sources conflict, report the conflict as a finding — do not silently pick a side.
- Date-stamp sources; in fast-moving areas, anything older than six months gets flagged as possibly stale.
- Inside Claude Code the built-in deep-research harness covers similar ground; this skill is the system-agnostic sibling for hosts without it.
