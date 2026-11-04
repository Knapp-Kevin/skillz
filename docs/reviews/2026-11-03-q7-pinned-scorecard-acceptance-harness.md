# Q7 pinned grant-scorecard workbook acceptance harness

**LATEST EVIDENCE (2026-11-03):** [The actual SHA-matching publisher XLSX has now been imported and tested](2026-11-03-q7-original-pinned-scorecard-engine-acceptance.md): its own B4=No example calculates 76 points and wrongly says GO; 25 candidate-repair scenarios passed in the local engine. The earlier transfer-blocked state below is historical. Source unchanged-use remains HOLD.

**CORRECTION (2026-11-03): This earlier fixture is superseded for source fidelity.** The original publisher's dropdown inputs live in `Gates!B2:B7`, not `Gates!C2:C7` (the notes column). Its F18 status includes descriptive text. [Corrected source inspection and test results](2026-11-03-q7-scorecard-source-column-reconciliation.md). The earlier receipt is preserved as history and must not be treated as a validated source-UI test.

The new [read-only acceptance script](../../scripts/qa/check_pinned_grant_scorecard.py) rejects the wrong XLSX using the **exact Git blob hash**, inspects bounded OOXML parts, identifies the source No-only gate formula, and can compare it against the proposed all-Yes plus numeric-score formula within an imported workbook **without saving modifications**.

**What ran:** `python scripts/qa/check_pinned_grant_scorecard.py --fixture-test` completed **9/9 cases** in artifact_tool on a **synthetic workbook**, including reproducing the unsafe original `GO` with unanswered eligibility gates. The synthetic file was built in memory and exported only as a temporary test fixture. This validates the harness mechanics, not the upstream XLSX.

**What remains blocked:** The original exact-pinned [Grant Go/No-Go Scorecard](https://github.com/zicula/skills/blob/ec7f94f84916be7bb25ec38752c24176330065a7/grant-writing-kit/references/2-go-no-go/go-no-go-scorecard.xlsx) is retrievable as Base64 through GitHub integration, but that connector does not mount its binary bytes into the isolated local spreadsheet runtime and public raw downloads were blocked. **The original workbook has not been executed or patched**.

To complete the actual pinned-source test in an authorized local checkout, obtain the original XLSX and run:

```bash
python scripts/qa/check_pinned_grant_scorecard.py /path/to/go-no-go-scorecard.xlsx
```

The runner checks the expected blob SHA before inspecting or importing. A mismatch is a **failure**, never a reason to trust an arbitrary replacement file. It does not send data externally, execute macro code, or write an output workbook.

**Still held:** The workbook's unsafe `GO` logic, UI data validation, Excel/LibreOffice compatibility, official funder terms, and approved budget operations. The separate 20-method Valuable Reference shelf and capability graph are unchanged because a test harness is not a newly approved skill.

[Machine-readable test scope and limitation](../../registry/discovery/q7-pinned-scorecard-acceptance-harness-20261103.json) · [Previous 18-case isolated formula replay](2026-11-03-q7-grant-scorecard-engine-replay.md).
