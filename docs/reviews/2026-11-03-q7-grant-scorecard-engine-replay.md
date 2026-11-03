# Q7: spreadsheet-engine reproduction of grant scorecard decision defect

**CORRECTION (2026-11-03): This earlier fixture is superseded for source fidelity.** The original publisher's dropdown inputs live in `Gates!B2:B7`, not `Gates!C2:C7` (the notes column). Its F18 status includes descriptive text. [Corrected source inspection and test results](2026-11-03-q7-scorecard-source-column-reconciliation.md). The earlier receipt is preserved as history and must not be treated as a validated source-UI test.

**Result:** The pinned original source formula returns `GO` at score 75 when five of the six mandatory gates are unanswered. We reproduced that result in an independent local **artifact_tool spreadsheet engine**, then tested two proposed replacement formulas using **18 fictional inputs**.

The stricter variant, which requires every gate to explicitly count as Yes **and** requires a numeric score, passed **18/18** cases. This includes blank/No/Unknown/numeric/whitespace gate answers, missing and text-valued scores, and boundaries at 49/50/69/70. In the original formula, **six** of these scenarios produce an unsafe GO against our deliberately conservative hold expectation (including unanswered/unknown gates).

**The test is reproducible:** `python scripts/qa/verify_grant_scorecard_gates.py` (optional local `artifact_tool` dependency). [Machine-readable independent result](../../registry/discovery/q7-grant-scorecard-engine-replay-20261103.json). The script creates a small isolated in-memory spreadsheet with the original and proposed formula in cells; it does not open or mutate the original XLSX.

**Important qualification boundary:** This verifies engine evaluation of *transcribed original and proposed formulas*, **not** actual execution of the pinned XLSX in Excel or LibreOffice. The publisher workbook's exact references, validations, conditional formatting, saved results, hidden behavior, and UX have not received full interactive acceptance. Source workbook hash: `a58d34344847a73440cb8ded6be88a3e87cc093d` at `zicula/skills@ec7f94f84916be7bb25ec38752c24176330065a7`. Neither the original source workbook nor a corrected derivative has been submitted, published, or installed.

**Disposition:** Continue to **HOLD** unchanged use of the Grant Go/No-Go Scorecard. The separate `Nonprofit Budget Narrative` method remains a reference for study only and is not implicated by this workbook bug. No change to the 20-method selected shelf, 33-domain graph or zero unchanged-use approvals.

**Remaining acceptance:** Patch an authorized non-production *copy* of the workbook and run its validations with an Excel/LibreOffice-compatible engine; qualify meaningful gate-entry behavior, formula propagation, document metadata, and actual funder rule compliance before considering promotion.
