#!/usr/bin/env python3
"""Bounded independent spreadsheet-engine reproduction of a pinned grant scorecard defect.

Reference: zicula/skills @ ec7f94f84916be7bb25ec38752c24176330065a7
Workbook: grant-writing-kit/references/2-go-no-go/go-no-go-scorecard.xlsx
Source logic was inspected from pinned workbook XML in Q7; no source workbook bytes
are embedded, downloaded, changed, submitted, or executed here.

Usage: python scripts/qa/verify_grant_scorecard_gates.py
Dependency: artifact_tool (local optional QA only, not a repository runtime).
"""

import json
from artifact_tool import Workbook

SOURCE_FORMULA = '=IF(COUNTIF(Gates!C2:C7,"No")>0,"WAIT — a gate is not met",IF(F17>=70,"GO — commit the hours",IF(F17>=50,"CONDITIONAL — fix low scorers first","NO-GO — pass this round")))'
ALL_GATES_FORMULA = '=IF(COUNTIF(Gates!B2:B7,"Yes")<ROWS(Gates!B2:B7),"WAIT",IF(F17>=70,"GO",IF(F17>=50,"CONDITIONAL","NO-GO")))'
RECOMMENDED_FORMULA = '=IF(OR(COUNTIF(Gates!B2:B7,"Yes")<ROWS(Gates!B2:B7),NOT(ISNUMBER(F17))),"WAIT",IF(F17>=70,"GO",IF(F17>=50,"CONDITIONAL","NO-GO")))'

# FICTIONAL decision inputs. The actual grant requirements and source workbook
# data validations have not been accepted or used.
CASES = [
    ("all_yes_go", ["Yes"] * 6, 75, "GO"),
    ("five_unanswered_go_score", ["Yes", "", "", "", "", ""], 75, "WAIT"),
    ("all_unanswered_high_score", [""] * 6, 90, "WAIT"),
    ("explicit_no_high_score", ["Yes", "Yes", "No", "Yes", "Yes", "Yes"], 95, "WAIT"),
    ("unknown_answer_high_score", ["Yes"] * 5 + ["Unknown"], 95, "WAIT"),
    ("numeric_answer_high_score", ["Yes"] * 5 + [1], 99, "WAIT"),
    ("whitespace_answer", ["Yes"] * 5 + ["Yes "], 99, "WAIT"),
    ("lowercase_yes_excel_countif", ["yes"] * 6, 95, "GO"),
    ("score_49", ["Yes"] * 6, 49, "NO-GO"),
    ("score_50", ["Yes"] * 6, 50, "CONDITIONAL"),
    ("score_69", ["Yes"] * 6, 69, "CONDITIONAL"),
    ("score_70", ["Yes"] * 6, 70, "GO"),
    ("score_zero", ["Yes"] * 6, 0, "NO-GO"),
    ("score_negative", ["Yes"] * 6, -1, "NO-GO"),
    ("score_100", ["Yes"] * 6, 100, "GO"),
    ("score_missing", ["Yes"] * 6, None, "WAIT"),
    ("score_text", ["Yes"] * 6, "70", "WAIT"),
    ("missing_score_and_gate", ["Yes"] * 5 + [""], None, "WAIT"),
]


def main():
    wb = Workbook.create()
    gates = wb.worksheets.add("Gates")
    score = wb.worksheets.add("Scorecard")
    gates.get_range("C2:C7").values = [["evidence note"], ["location note"], ["Worked example: vote pending"], ["program note"], ["match note"], ["owner note"]]
    score.get_range("F18:F20").formulas = [[SOURCE_FORMULA], [ALL_GATES_FORMULA], [RECOMMENDED_FORMULA]]
    rows = []
    for name, answers, points, expected in CASES:
        gates.get_range("B2:B7").values = [[v] for v in answers]
        score.get_range("F17").values = [[points]]
        source_result, basic_result, recommended_result = [row[0] for row in score.get_range("F18:F20").values]
        if recommended_result != expected:
            raise AssertionError(f"{name}: expected {expected!r}, got {recommended_result!r}")
        rows.append({"case": name, "source": source_result, "basic_fix": basic_result,
                     "recommended_fix": recommended_result, "expected": expected,
                     "pass": recommended_result == expected})

    assert next(r for r in rows if r["case"] == "five_unanswered_go_score")["source"].startswith("GO"), "Source defect not reproduced"
    assert next(r for r in rows if r["case"] == "explicit_no_high_score")["source"].startswith("GO"), "Source ignored explicit No in user input column"
    assert next(r for r in rows if r["case"] == "score_missing")["recommended_fix"] == "WAIT", "Unscored state not held"
    report = {"status": "PASS", "case_count": len(rows), "passed": len(rows),
              "reproduced_source_blank_gate_go": True,
              "reproduced_source_wrong_column_false_go": True,
              "method": "Source-faithful synthetic workbook: user answers B2:B7, source F18 incorrectly reads C2:C7 explanatory notes. Not original XLSX execution.",
              "source_formula": SOURCE_FORMULA, "proposed_formula": RECOMMENDED_FORMULA,
              "limitations": ["Original downloaded workbook was not executed or modified",
                              "Formula semantics reproduced in artifact_tool, not Microsoft Excel",
                              "Pinned source OOXML verified B2:B7 validation and C2:C7 notes; test workbook synthetic",
                              "Upstream data-validation UX and real grant requirements not tested",
                              "COUNTIF compares Yes case-insensitively by engine convention"],
              "results": rows}
    print(json.dumps(report, indent=2))
    return report


if __name__ == "__main__":
    main()
