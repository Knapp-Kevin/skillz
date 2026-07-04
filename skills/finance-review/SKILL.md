---
name: finance-review
description: >-
  Produce a monthly money digest from statement exports the operator drops
  in a folder: category trends vs the prior month, anomalies with their
  evidence rows, and upcoming known charges. Use when the user asks "review
  my finances", "monthly money digest", "go through these statements", or
  drops CSV/XLSX bank exports for analysis. Strictly read-only.
metadata:
  author: frostwulf.zo.computer
  category: Productivity
  display-name: Finance Review
  emoji: "💰"
  version: 1.0.0
---

# Finance Review

Turn a folder of operator-provided statement exports (CSV/XLSX) into a monthly digest a human can act on: where money went by category, how that compares to last month, anomalies worth a second look with the exact rows that triggered them, and known charges coming up. This skill never touches an account — it only reads files the operator has already exported and dropped.

## Execution Flow

1. **Inventory the provided files.** List the CSV/XLSX files in the folder the operator names. If files are missing for the period (an account's export absent, a month gap), ask for them — never fetch, connect to, or log into anything to fill the gap.
2. **Parse and normalize.** Read each export; unify date, merchant, and amount columns. For heavy lifting (large XLSX workbooks, multi-sheet exports, formula cells), use the vendored xlsx skill's mechanics rather than hand-parsing.
3. **Categorize.** Assign each transaction a category. Reuse the prior digest's category mapping when one exists; put genuinely ambiguous merchants in an "uncategorized" bucket and ask, rather than guessing.
4. **Compare to prior month.** Compute per-category totals and deltas vs the previous digest or previous month's rows. Call out the two or three moves that matter, not every fluctuation.
5. **Hunt anomalies.** Flag new merchants never seen before, likely duplicate charges (same merchant, same amount, close dates), and size outliers vs that merchant's history. Every flag must cite the evidence row(s) verbatim.
6. **Project known charges.** From recurring patterns in the data, list charges expected in the coming month with expected amounts.
7. **Present** in the Output Format below, ending with questions only the operator can answer.

## Scheduling

- **Claude Code:** create a monthly `/schedule` routine that reminds the operator to drop fresh exports into the folder, then runs this skill on them.
- The reminder matters: the skill can only be as current as the exports it is handed.

## Output Format

```
# Finance Review — [month]
**Files reviewed:** [list] · **Missing:** [list or none]

## Summary
[3-5 sentences: total in/out, biggest category moves, headline anomaly.]

## Categories vs prior month
| Category | This month | Prior month | Delta | Note |
|----------|-----------:|------------:|------:|------|

## Anomalies
- [flag type: new merchant / duplicate / outlier] — [evidence row(s), verbatim]

## Upcoming known charges
- [merchant] ~[amount] around [date]

## Questions for you
- [ambiguous merchant / unexplained anomaly needing operator input]
```

## Notes

- Read-only, absolutely: NEVER initiates transactions, connects to accounts, or fetches statements. All data arrives as files the operator provides.
- Anomalies without evidence rows are rumors — every flag quotes the row that triggered it.
- Sending the digest anywhere (email, Slack) is draft-only: prepare and show it, send nothing without explicit approval.
