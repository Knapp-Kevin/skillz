---
name: paper-digest
description: >-
  Read a research paper properly: extract the actual claim, plain-language
  method, evidence quality, admitted and unadmitted limitations, and a
  relevance verdict for the MythologIQ stack. Use when the user asks
  "digest this paper", "read this arXiv link", "is this paper any good",
  "summarize this paper for us", or drops a PDF, arXiv, or HF papers URL.
metadata:
  author: frostwulf.zo.computer
  category: Research
  display-name: Paper Digest
  emoji: "📄"
  version: 1.0.0
---

# Paper Digest

A critical read of one paper that separates what the authors demonstrated from what the abstract markets, and ends with whether it matters for the MythologIQ stack (agent governance, memory, local inference). Feeds the finds surfaced by memory-pulse and hf-pulse.

## Execution Flow

1. **Obtain the paper.** Works from a PDF, an arXiv link, or a Hugging Face papers page. Prefer the connected Hugging Face MCP tools when available — `paper_search` to locate the paper and its discussion, `hf_doc_fetch` or web fetch for the full text. Read the body, not just the abstract.
2. **Identify the actual claim.** State what the results actually establish, which is routinely narrower than the abstract's marketing — note the gap when there is one (e.g., "beats baselines" means "beats three chosen baselines on two chosen benchmarks").
3. **Summarize the method in plain language.** A paragraph a practitioner can act on: what was built, trained, or measured, and against what.
4. **Check evidence quality.** Are benchmarks cherry-picked or standard? Are baselines fair and current, or strawmen? Is code released and runnable? Has anyone replicated it — search for independent reproductions, critiques, and follow-up citations rather than trusting the paper's own framing.
5. **List limitations, admitted and unadmitted.** What the authors concede in the limitations section, and what they do not: scale gaps, compute assumptions, distribution shift, evaluation blind spots.
6. **Deliver the relevance verdict.** So-what for the MythologIQ stack: does this change anything for agent governance, memory architecture, or local inference — and if promising, whether it warrants a registry `track` entry.

## Output Format

```
# Paper Digest — [title] ([venue/arXiv id], [date])
## Actual claim (vs the abstract's framing)
## Method in plain language
## Evidence quality
- Benchmarks: [standard / cherry-picked — details]
- Baselines: [fair / weak — details]
- Code released: [yes + link / no]
## Limitations
- Admitted: [...]
- Unadmitted: [...]
## Replication status
## So what for us (agent governance / memory / local inference)
```

## Notes

- Read-only: reads and reports; never posts reviews or contacts authors.
- The unadmitted-limitations section is the point — anyone can restate an abstract.
- If the full text is paywalled and no preprint exists, digest what is available and flag the confidence ceiling rather than extrapolating from the abstract.
- Replication status defaults to "none found" — absence of replication is a finding, not a gap to skip.
