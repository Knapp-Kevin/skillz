#!/usr/bin/env python3
"""Read-only pinned-source acceptance harness for the Skillz Q7 grant scorecard.

Required source: zicula/skills @ ec7f94f84916be7bb25ec38752c24176330065a7
Use: python scripts/qa/check_pinned_grant_scorecard.py /path/to/go-no-go-scorecard.xlsx
The upstream workbook is never modified or exported. --fixture-test constructs an
original-column-shaped synthetic workbook, explicitly NOT a source qualification.
"""

import argparse
import hashlib
import io
import json
import re
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from artifact_tool import Blob, SpreadsheetFile, Workbook

EXPECTED_SHA = "a58d34344847a73440cb8ded6be88a3e87cc093d"
SOURCE_FORMULA = '=IF(COUNTIF(Gates!C2:C7,"No")>0,"WAIT — a gate is not met",IF(F17>=70,"GO — commit the hours",IF(F17>=50,"CONDITIONAL — fix low scorers first","NO-GO — pass this round")))' 
RECOMMENDED_FORMULA = '=IF(OR(COUNTIF(Gates!B2:B7,"Yes")<ROWS(Gates!B2:B7),NOT(ISNUMBER(F17))),"WAIT",IF(F17>=70,"GO",IF(F17>=50,"CONDITIONAL","NO-GO")))'
TESTS = [
    ("original_explicit_no", ["Yes", "Yes", "No", "Yes", "Yes", "Yes"], 75, "WAIT", True),
    ("blank_gate", ["Yes", "Yes", "", "Yes", "Yes", "Yes"], 75, "WAIT", True),
    ("unknown_gate", ["Yes", "Yes", "Unknown", "Yes", "Yes", "Yes"], 90, "WAIT", True),
    ("all_yes", ["Yes"] * 6, 75, "GO", False),
    ("score_49", ["Yes"] * 6, 49, "NO-GO", False),
    ("score_50", ["Yes"] * 6, 50, "CONDITIONAL", False),
    ("score_69", ["Yes"] * 6, 69, "CONDITIONAL", False),
    ("score_70", ["Yes"] * 6, 70, "GO", False),
    ("missing_score", ["Yes"] * 6, None, "WAIT", False),
    ("text_score", ["Yes"] * 6, "70", "WAIT", False),
]
NS = {"x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def source_fingerprint(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def inspect_ooxml(raw: bytes) -> dict:
    if len(raw) > 10_000_000:
        raise ValueError("Workbook exceeds bounded inspection size")
    with zipfile.ZipFile(io.BytesIO(raw), "r") as z:
        parts = z.infolist()
        if len(parts) > 500 or sum(i.file_size for i in parts) > 20_000_000:
            raise ValueError("OOXML archive exceeds safe inspection bounds")
        names = [i.filename for i in parts]
        suspicious = [n for n in names if re.search(r"vbaProject|externalLinks|activeX|embeddings|oleObject", n, re.I)]
        if suspicious or any(i.flag_bits & 1 for i in parts):
            raise ValueError("Encrypted or executable/external-link OOXML parts detected: " + ", ".join(suspicious))
        workbook = ET.fromstring(z.read("xl/workbook.xml"))
        sheets = [(n.get("name"), n.get("state", "visible")) for n in workbook.findall(".//x:sheet", NS)]
        if set(n for n, _ in sheets) != {"Scorecard", "Gates", "Log"}:
            raise ValueError("Unexpected worksheet identities: " + repr(sheets))
        formulas = []
        for name in names:
            if not re.fullmatch(r"xl/worksheets/sheet\d+\.xml", name):
                continue
            root = ET.fromstring(z.read(name))
            for cell in root.findall(".//x:c", NS):
                f = cell.find("x:f", NS)
                if f is not None and f.text:
                    formulas.append({"sheet_file": name, "cell": cell.get("r"), "formula": f.text})
        gate = [f for f in formulas if 'COUNTIF(Gates!C2:C7,"No")>0' in f["formula"]]
        if len(gate) != 1:
            raise ValueError("Expected exactly one source gate formula; found " + str(len(gate)))
        if gate[0]["cell"] != "F18" or "GO — commit the hours" not in gate[0]["formula"]:
            raise ValueError("Original F18 status formatting or source formula changed")
        gates_xml = ET.fromstring(z.read("xl/worksheets/sheet2.xml"))
        validations = [item.get("sqref") for item in gates_xml.findall(".//x:dataValidation", NS)]
        if "B2:B7" not in validations or "C2:C7" in validations:
            raise ValueError("Gate answers are not validated in expected B2:B7: " + repr(validations))
        def gate_text(ref):
            cell = gates_xml.find(f'.//x:c[@r="{ref}"]', NS)
            if cell is None:
                return None
            rich = "".join(t.text or "" for t in cell.findall(".//x:t", NS))
            return rich or (cell.findtext("x:v", namespaces=NS) or "")
        if gate_text("B4") != "No" or "Worked example" not in (gate_text("C4") or ""):
            raise ValueError("Pinned source B4 No / C4 narrative-note example not found")
        return {"sheets": sheets, "formula_count": len(formulas),
                "source_gate_formula": gate[0], "actual_gate_input_range": "B2:B7",
                "wrong_source_formula_range": "C2:C7",
                "source_b4": gate_text("B4"), "source_c4_is_notes": True,
                "macro_external_parts": len(suspicious),
                "hidden_sheets": sum(state != "visible" for _, state in sheets)}


def run_cells(path: Path, located: dict) -> dict:
    book = SpreadsheetFile.import_xlsx(Blob.load(str(path)))
    gates = book.worksheets.get_item("Gates")
    score = book.worksheets.get_item("Scorecard")
    source_cell = located["source_gate_formula"]["cell"]
    # Source F18 reads notes in C; candidate must read validated answers in B.
    # F17 is replaced in memory only to isolate score thresholds.
    score.get_range("H18").formulas = [[RECOMMENDED_FORMULA]]
    results = []
    for title, answers, points, expected, original_must_go in TESTS:
        gates.get_range("B2:B7").values = [[a] for a in answers]
        score.get_range("F17").values = [[points]]
        observed_original = score.get_range(source_cell).values[0][0]
        observed_candidate = score.get_range("H18").values[0][0]
        if observed_candidate != expected:
            raise AssertionError(f"{title}: candidate {observed_candidate!r} vs expected {expected!r}")
        if original_must_go and not (isinstance(observed_original, str) and observed_original.startswith("GO")):
            raise AssertionError(f"{title}: source wrong-column false GO not reproduced: {observed_original!r}")
        results.append({"case": title, "source": observed_original,
                        "candidate": observed_candidate, "expected": expected})
    source_bug = next(x for x in results if x["case"] == "original_explicit_no")["source"].startswith("GO")
    if not source_bug:
        raise AssertionError("Original false-GO defect was not reproduced in imported workbook")
    return {"tests": results, "candidate_passes": len(results), "original_defect_reproduced": source_bug}


def make_fixture(path: Path) -> None:
    """Build a source-shaped *synthetic* workbook, never a source acceptance."""
    book = Workbook.create()
    score = book.worksheets.add("Scorecard")
    gates = book.worksheets.add("Gates")
    book.worksheets.add("Log")
    gates.get_range("B2:B7").values = [["Yes"], ["Yes"], ["No"], ["Yes"], ["Yes"], ["Yes"]]
    gates.get_range("C2:C7").values = [
        ["eligibility evidence"], ["service area evidence"],
        ["Worked example: board approval pending"], ["budget note"],
        ["cost-share note"], ["owner note"]
    ]
    gates.get_range("B2:B7").data_validation = {"rule": {"type": "list", "values": ["Yes", "No"]}}
    score.get_range("F17").values = [[75]]
    score.get_range("F18").formulas = [[SOURCE_FORMULA]]
    SpreadsheetFile.export_xlsx(book).save(str(path))

def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("workbook", nargs="?", type=Path)
    p.add_argument("--fixture-test", action="store_true", help="Test harness on synthetic book; not upstream qualification")
    a = p.parse_args(argv)
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "fixture.xlsx" if a.fixture_test else a.workbook
        if path is None:
            p.error("Supply source XLSX or --fixture-test")
        if a.fixture_test:
            make_fixture(path)
        raw = path.read_bytes()
        digest = source_fingerprint(raw)
        if not a.fixture_test and digest != EXPECTED_SHA:
            raise ValueError(f"Git blob fingerprint mismatch: expected {EXPECTED_SHA}, observed {digest}")
        original = inspect_ooxml(raw)
        formula_test = run_cells(path, original)
        report = {"status": "PASS", "kind": "SYNTHETIC HARNESS SELF-TEST" if a.fixture_test else "PINNED ORIGINAL SOURCE ACCEPTANCE",
                  "git_blob_sha": digest, "expected_source_sha": EXPECTED_SHA, "static": original, "engine": formula_test,
                  "qualifications": ["No original file was modified or exported", "Excel/LibreOffice behavior is not inferred",
                                     "No real grant eligibility or finance acceptance was checked"]}
        print(json.dumps(report, indent=2))
        return report


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}), file=sys.stderr)
        sys.exit(1)
