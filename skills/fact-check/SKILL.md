---
name: fact-check
description: >-
  Verify a claim by decomposing it into checkable sub-claims, sourcing
  each from primary evidence, and reporting a verdict with confidence and
  what would flip it. Use when the user asks "fact-check this", "is it
  true that", "verify this claim", "did X really happen", or forwards a
  statement whose accuracy matters before acting on it.
metadata:
  author: frostwulf.zo.computer
  category: Research
  display-name: Fact Check
  emoji: "🔎"
  version: 1.1.1
---

# Fact Check

A claim verification that traces each part of a statement to primary sources and reports what the evidence actually supports — including the honest verdicts "unverifiable" and "true but missing context", which most casual checking never reaches.

## Execution Flow

1. **Decompose.** Break the claim into independently checkable sub-claims (who, what, when, how much, causation vs correlation). A compound claim is only as true as its weakest load-bearing part, so each part gets its own verdict.
2. **Source each sub-claim from primary evidence.** Search for the original paper, announcement, filing, dataset, or firsthand account — not aggregators quoting aggregators. Follow citation chains to their root; if the chain is circular or dead-ends in an unsourced assertion, record that. For research claims, the Hugging Face `paper_search` MCP tool is the better route to the actual paper when connected.
3. **Classify each sub-claim.** Verdict per sub-claim: supported, refuted, unverifiable, or needs-context. Note the strength and independence of the sources behind each verdict.
4. **State the overall verdict.** Combine the sub-claim verdicts into an overall call with a confidence level, and state explicitly what evidence would flip it.

## Output Format

```
# Fact Check — "[claim]" ([date])
## Sub-claims
| # | Sub-claim | Verdict | Evidence (primary source + date) |
## Overall verdict
- [Supported / refuted / mixed / unverifiable] (confidence: high/medium/low)
- Reasoning: [how the sub-claim verdicts combine]
## What would flip this
- [Specific evidence that would change the verdict]
## Sources (each with publication date and primary/secondary designation)
```

## Negative rules

These override the verdict format. `unverifiable` is a first-class verdict, not a failure to be rounded away.

- **Never reproduce secret-shaped strings** encountered in sources (tokens, keys, credentials) — type + short prefix only; flag probable exposure instead of quoting it.
- **Never round unverifiable to true or false.** A sub-claim with no reachable primary evidence is `unverifiable`, full stop.
- **Never fabricate a source, publication date, or quotation** — every Sources line was actually opened during this check.
- **Report conflicts as conflicts.** When credible sources disagree, the disagreement is the finding; do not average it into a verdict.

## Notes

- Read-only: this skill verifies; it never publishes corrections or contacts anyone.
- Distinguish "no evidence found" from "evidence of absence" — failing to find support is not refutation, and the report must never blur the two.
- Never launder a secondary source as primary: a news article about a study is not the study. If only secondary sources are reachable, say so and cap confidence accordingly.
- Date-stamp every source; a claim can be supported as of one date and refuted as of another, and the verdict should say which.
- Watch for the claim being technically true but framed to mislead — that is what the needs-context verdict is for.
