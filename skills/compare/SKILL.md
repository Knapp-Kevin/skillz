---
name: compare
description: >-
  Run a structured comparison of tools, models, vendors, or approaches:
  criteria confirmed first, evidence gathered per matrix cell, weighted
  recommendation with the runner-up's best counter-argument. Use when the
  user asks "compare X and Y", "which should I use, X or Y", "X vs Y",
  "help me choose between", or is thrashing on a which-tool decision.
metadata:
  author: frostwulf.zo.computer
  category: Research
  display-name: Compare
  emoji: "⚖️"
  version: 1.0.0
---

# Compare

A decision-grade comparison built on confirmed criteria and sourced evidence, ending in a weighted recommendation that states honestly when the runner-up wins. The discipline that kills "which X should I use" thrash is fixing the criteria before touching the evidence.

## Execution Flow

1. **Elicit criteria first.** Draft the decision criteria from the user's context (or ask if none is given), propose weights (e.g., cost 3, maturity 2, local-first 3), and get the list confirmed before gathering any evidence. Criteria decided after seeing evidence are rationalization, not evaluation.
2. **Gather evidence cell-by-cell.** For each candidate × criterion cell, search for sourced evidence: official docs and pricing pages, independent benchmarks, community experience reports. When a connected MCP tool is the better source — Hugging Face hub tools for model comparisons, Context7 for library documentation — prefer it over general web search. Mark a cell "no evidence found" rather than guessing; an honest gap beats a confident fabrication.
3. **Compute the weighted read.** Score each cell (0-3 works), multiply by weights, and total. Treat the numbers as a summary of the evidence, not an oracle — call out where a single criterion dominates the result.
4. **Recommend with the counter-argument.** State the recommendation, then state the runner-up's strongest genuine case and the concrete conditions under which the runner-up is the right pick.

## Output Format

```
# Comparison — [X] vs [Y] vs ... ([date])
## Decision criteria (confirmed with user)
| Criterion | Weight | Why it matters here |
## Evidence matrix
| Criterion | [X] | [Y] | ... |  (each cell: finding + citation, or "no evidence found")
## Weighted read
| Candidate | Score | Notes |
## Recommendation
- Pick: [candidate] because [top 2-3 evidence-backed reasons]
- Runner-up's strongest counter-argument: [stated honestly]
- When the runner-up wins: [concrete conditions]
## Sources (with dates)
```

## Notes

- Read-only: no trials signed up for, nothing installed, no external state touched.
- Never let vendor marketing fill a cell unopposed — pair every vendor claim with an independent source or mark it "vendor claim, unverified".
- If the confirmed criteria produce a near-tie, say so; a tie plus switching costs is itself a recommendation for the incumbent.
- Date-stamp pricing and benchmark evidence; both go stale fast.
