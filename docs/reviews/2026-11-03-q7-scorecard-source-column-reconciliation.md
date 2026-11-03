# Q7 source workbook correction: gate answers were in the wrong column

**High-priority correction:** In the actual source-pinned [Grant Go/No-Go Scorecard](https://github.com/zicula/skills/blob/ec7f94f84916be7bb25ec38752c24176330065a7/grant-writing-kit/references/2-go-no-go/go-no-go-scorecard.xlsx), the user enters Yes/No eligibility answers in **Gates!B2:B7**. Column **C2:C7 contains explanatory notes**. But `Scorecard!F18` checks `COUNTIF(Gates!C2:C7,"No")>0`. The pinned example has an explicit **No in B4** and a note in C4. The published formula can therefore ignore a failed eligibility gate and return a `GO` decision when the score is high.

This is worse than the earlier blank-only problem. In addition, any simplistic check for No still misses blank or unrecognized mandatory answers. We propose counting **all six Yes answers in B2:B7** and requiring `ISNUMBER(F17)` before score thresholds are evaluated. The public package remains held.

## Evidence and repairs

- **Original-source evidence actually inspected:** Connected GitHub's Base64 response for the exact pinned 10,048-byte XLSX was decoded and the OOXML structures read without executing macros or importing the workbook into a calculation engine. Exact connector-declared Git blob `a58d34344847a73440cb8ded6be88a3e87cc093d`. Workbook sheets Scorecard, Gates, Log; `Gates!B2:B7` dropdown list Yes/No permits blanks; `B4=No`; `C4` is narrative context; `Scorecard!F18` includes long labels such as `GO — commit the hours`, not the bare word `GO`.
- **Old test correction:** Earlier [18-case replay](../../registry/discovery/q7-grant-scorecard-engine-replay-20261103.json) and [9-case acceptance fixture](../../registry/discovery/q7-pinned-scorecard-acceptance-harness-20261103.json) incorrectly populated column C. Preserve these as historical tests of the wrong-column simulation, **not** evidence of actual input handling.
- **New source-faithful synthetic tests:** The updated independent replay passed **18/18** scenarios. The revised [pinned acceptance harness](../../scripts/qa/check_pinned_grant_scorecard.py) passed **10/10** synthetic workbook scenarios with B input/C notes, including explicit No producing source GO while the proposed formula returns WAIT. Local wrong-Git-hash admission was correctly rejected; Python compile passed.
- **Still not qualified:** We have NOT imported the original source XLSX into the local spreadsheet calculation engine because source bytes cannot be mounted from the connected GitHub response into that runtime here. No Excel/LibreOffice compatibility, real financial inputs, funder eligibility checks, security clearance or unchanged-use approval is claimed.

**Current disposition:** Source workbook **HOLD / do not use its GO outcome**. Correct an authorized copy in isolation and run the exact pinned-source harness, including data-validation UX, before any promotion. The unrelated Nonprofit Budget Narrative conceptual reference remains independently selected; 20-method consumer catalog and 33-domain dashboard counts do not change.

[Structured source and test evidence](../../registry/discovery/q7-scorecard-source-column-reconciliation-20261103.json).
