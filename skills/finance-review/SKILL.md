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
  version: 1.1.0
---

# Finance Review

Turn operator-provided statement exports (CSV/XLSX) into a monthly digest a human can act on: where money went by category, how that compares with the prior month, anomalies worth a second look with exact evidence rows, and known charges likely to recur. This skill never touches an account. It reads only files the operator deliberately supplies for this review.

## Execution Flow

1. **Inventory the provided files.** List the CSV/XLSX files in the folder or artifact set the operator identifies. If files are missing for the period, report the gap and ask for the missing export. Never connect to an account or log in somewhere to fill it.
2. **Resolve a safe parsing capability.** Use the active host's available spreadsheet/file tools when they can read the supplied format without mutating the source. A local CSV/XLSX parser is also acceptable when already available. Do not route automatically to a vendored spreadsheet skill merely because one exists in the reference corpus. If the host cannot safely parse a required file, report that file as `UNREADABLE IN THIS HOST` and do not invent its rows.
3. **Parse and normalize.** Unify date, merchant, and amount fields while retaining the original row identity/source file so every downstream claim can trace back to source data.
4. **Categorize.** Reuse the prior digest's category mapping when one exists. Put genuinely ambiguous merchants in `uncategorized` and ask rather than guessing.
5. **Compare with the prior month.** Compute per-category totals and deltas from the available rows. Call out the two or three moves that matter, not every fluctuation.
6. **Hunt anomalies.** Flag new merchants, likely duplicate charges (same merchant/amount near each other), and size outliers versus that merchant's observed history. Every flag cites the source row(s).
7. **Project known charges conservatively.** From recurring patterns in the supplied data, list likely charges in the coming month. Label amount/date as an estimate unless the data establishes a fixed schedule.
8. **Present** in the Output Format below, ending with questions only the operator can answer.

## Output Format

```text
# Finance Review — [month]
**Files reviewed:** [list] · **Missing/unreadable:** [list or none]

## Summary
[3-5 sentences: total in/out, biggest category moves, headline anomaly.]

## Categories vs prior month
| Category | This month | Prior month | Delta | Note |
|----------|-----------:|------------:|------:|------|

## Anomalies
- [new merchant / duplicate / outlier] — [source file + exact row evidence]

## Upcoming known charges
- [merchant] ~[amount] around [date] — [evidence / confidence]

## Questions for you
- [ambiguous merchant / unexplained anomaly needing operator input]
```

## Negative rules

- Read-only, absolutely: never initiate transactions, connect to financial accounts, or fetch statements from an account.
- Never invent or interpolate missing statement rows to make totals look complete.
- An anomalies claim without exact source-row evidence is not an anomaly finding.
- Do not expose full account numbers or credential-like values found in exports; minimize or redact sensitive identifiers in the report.
- A recurring-pattern projection is an estimate unless a supplied statement/source establishes the schedule.

## Notes

- File-format support is a host capability, not a reason to import an unrelated vendor workflow.
- Sending the digest anywhere is a separate action and requires the user's explicit authorization.
- Behavioral validation remains separate from this skill's static safety/quality contract.