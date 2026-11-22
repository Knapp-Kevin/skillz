"""Adversarial, fictional execution-graph cases for CI Guard v1.6.

These test the offline method, not a real consumer, provider or Actions budget.
"""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("overlap", ROOT / "scripts" / "audit_execution_overlap.py")
overlap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(overlap)
SHA = "0123456789abcdef0123456789abcdef01234567"


def node(id, kind, invokes=(), **attrs):
    return {"id": id, "kind": kind, "invokes": list(invokes), **attrs}


def terminal(id, obligation, *, command="check", platform="ubuntu-24.04",
             trust="pr-unprivileged", assurance="", receipt_id=""):
    return node(id, "terminal", obligation=obligation, command=command, sha=SHA,
                inputs=["lockfile:v1", "source:HEAD"], platform=platform,
                environment="CI=true; stable-locale", toolchain="rust:1.84.1",
                trust=trust, failure_boundary=f"detect:{obligation}",
                equivalence_proven=True, independent_assurance=assurance,
                assurance_receipt=receipt_id,
                cost_class="cheap" if obligation in {"freshness", "draft-deferred"} else "expensive",
                receipt="success")


def fixture():
    nodes = [
        node("acceptance", "workflow", ["accept-job"], stages=["candidate", "release"], entrypoint=True),
        node("accept-job", "job", ["accept-recipe"], stages=["candidate", "release"],
             needs=[], matrix_expanded=True),
        node("accept-recipe", "recipe", ["accept-script"]),
        node("accept-script", "script", ["accept-repro", "model", "freshness"]),
        terminal("accept-repro", "repro", command="cargo xtask check-reproducibility"),
        terminal("model", "model", command="model-validator"),
        terminal("freshness", "freshness", command="generator-freshness"),
        node("standalone-repro", "workflow", ["repro-job"], stages=["candidate", "release"], entrypoint=True),
        node("repro-job", "job", ["just-repro"], stages=["candidate", "release"], needs=[], matrix_expanded=True),
        node("just-repro", "recipe", ["call-repro-script"]),
        node("call-repro-script", "script", ["other-repro"]),
        terminal("other-repro", "repro", command="cargo xtask check-reproducibility"),
        node("release", "workflow", ["sign-job"], stages=["release"], entrypoint=True),
        node("sign-job", "job", ["sign"], stages=["release"], needs=[], matrix_expanded=True),
        terminal("sign", "sign", command="signature-verifier"),
        node("draft", "workflow", ["draft-job"], stages=["draft"], entrypoint=True),
        node("draft-job", "job", ["draft-deferred"], stages=["draft"], needs=[], matrix_expanded=True),
        terminal("draft-deferred", "draft-deferred", command="status-only"),
    ]
    required = {"draft": [], "candidate": ["repro", "model", "freshness"],
                "release": ["repro", "model", "freshness", "sign"]}
    return {"schema_version": 1, "revision": SHA, "phase": "baseline",
            "inventory_complete": True, "unresolved_invocations": [],
            "nodes": nodes, "required": required,
            "qualification": {stage: {"required": list(required[stage]), "exact_revision": True,
                              "reject_non_success": True, "trusted": True,
                              **({"draft_marker": "DRAFT_DEFERRED_NOT_QUALIFIED"} if stage == "draft" else {})}
                              for stage in required},
            "dispositions": [{"stage": stage, "obligation": "repro",
                              "decision": "CONSOLIDATE", "reason": "Both wrappers resolve to identical verified work"}
                             for stage in ("candidate", "release")]}


def byid(doc, id):
    return next(n for n in doc["nodes"] if n["id"] == id)


def consolidated(doc):
    d = copy.deepcopy(doc)
    d["phase"] = "candidate"
    d["nodes"] = [n for n in d["nodes"] if n["id"] not in
                  {"standalone-repro", "repro-job", "just-repro", "call-repro-script", "other-repro"}]
    d["dispositions"] = []
    return d


class ExecutionOverlapTest(unittest.TestCase):
    def test_composite_and_standalone_invoke_same_terminal_check(self):
        result = overlap.audit(fixture())
        self.assertEqual(result["structural_assessment"], "HOLD")
        self.assertEqual({x["stage"] for x in result["overlaps"]}, {"candidate", "release"})
        self.assertTrue(all(x["classification"] == "PARTIAL_OVERLAP" for x in result["overlaps"]))
        self.assertTrue(any("just-repro > call-repro-script" in p for x in result["overlaps"]
                            for p in x["invocation_paths"]))

    def test_different_wrapper_names_same_execution(self):
        d = fixture()
        byid(d, "other-repro")["command"] = "just repro (resolved to cargo xtask check-reproducibility)"
        result = overlap.audit(d)
        self.assertEqual(result["overlaps"][0]["classification"], "PARTIAL_OVERLAP")
        self.assertEqual(result["structural_assessment"], "HOLD")

    def test_composite_only_repro_has_exact_duplicate_not_partial(self):
        d = fixture()
        byid(d, "accept-script")["invokes"] = ["accept-repro"]
        d["nodes"] = [x for x in d["nodes"] if x["id"] not in {"model", "freshness"}]
        d["required"]["candidate"] = ["repro"]
        d["required"]["release"] = ["repro", "sign"]
        d["qualification"]["candidate"]["required"] = ["repro"]
        d["qualification"]["release"]["required"] = ["repro", "sign"]
        result = overlap.audit(d)
        self.assertEqual(result["overlaps"][0]["classification"], "EXACT_DUPLICATE")

    def test_different_platforms_protect_distinct_assurance(self):
        d = fixture()
        byid(d, "other-repro")["platform"] = "windows-2025"
        byid(d, "other-repro")["independent_assurance"] = "Windows ABI and native path behavior"
        byid(d, "other-repro")["assurance_receipt"] = "synthetic:windows-negative"
        byid(d, "accept-repro")["independent_assurance"] = "Linux POSIX reproducibility"
        byid(d, "accept-repro")["assurance_receipt"] = "synthetic:linux-negative"
        for x in d["dispositions"]:
            x["decision"] = "KEEP"
        r = overlap.audit(d)
        self.assertTrue(all(x["classification"] == "JUSTIFIED_REPETITION" for x in r["overlaps"]))
        self.assertEqual(r["structural_assessment"], "PASS")

    def test_changed_toolchain_alone_does_not_prove_independent_detection(self):
        d = fixture()
        byid(d, "other-repro")["toolchain"] = "rust:1.86"
        r = overlap.audit(d)
        self.assertTrue(all(x["classification"] == "UNPROVEN" for x in r["overlaps"]))
        self.assertEqual(r["structural_assessment"], "HOLD")

    def test_old_standalone_remains_after_claimed_cutover(self):
        d = fixture()
        d["phase"] = "candidate"
        self.assertEqual(overlap.audit(d)["structural_assessment"], "HOLD")
        self.assertTrue(any("duplicated effective execution still present" in x
                            for x in overlap.audit(d)["violations"]))

    def test_remove_only_candidate_duplication_leaves_release_duplication(self):
        d = fixture()
        byid(d, "standalone-repro")["stages"] = ["release"]
        byid(d, "repro-job")["stages"] = ["release"]
        d["dispositions"] = [x for x in d["dispositions"] if x["stage"] == "release"]
        r = overlap.audit(d)
        self.assertEqual([x["stage"] for x in r["overlaps"]], ["release"])
        self.assertEqual(r["structural_assessment"], "HOLD")

    def test_removing_duplication_preserves_required_candidate_and_release_coverage(self):
        r = overlap.audit(consolidated(fixture()))
        self.assertEqual(r["structural_assessment"], "PASS")
        self.assertFalse(r["overlaps"])
        self.assertFalse(r["optimization_complete"])
        self.assertEqual(r["observed_runner_minutes_delta"], "NOT_MEASURED")
        self.assertEqual(r["observed_critical_path_delta"], "NOT_MEASURED")

    def test_release_signing_lost_during_deduplication_is_blocked(self):
        d = consolidated(fixture())
        byid(d, "release")["invokes"] = ["accept-job"]
        r = overlap.audit(d)
        self.assertEqual(r["structural_assessment"], "HOLD")
        self.assertTrue(any("release: required verification absent: sign" in x for x in r["violations"]))

    def test_gate_missing_repro_is_schema_failure(self):
        d = consolidated(fixture())
        d["qualification"]["release"]["required"] = ["model", "freshness", "sign"]
        with self.assertRaises(overlap.InvalidInput):
            overlap.audit(d)

    def test_authoritative_verification_skipped_does_not_qualify(self):
        d = consolidated(fixture())
        byid(d, "accept-repro")["receipt"] = "skipped"
        r = overlap.audit(d)
        self.assertEqual(r["structural_assessment"], "HOLD")
        self.assertTrue(any("skipped does not qualify" in x for x in r["violations"]))

    def test_stale_verification_refused(self):
        d = consolidated(fixture())
        byid(d, "accept-repro")["sha"] = "old-revision"
        with self.assertRaises(overlap.InvalidInput):
            overlap.audit(d)

    def test_draft_skips_expensive_while_ready_release_still_verify(self):
        r = overlap.audit(consolidated(fixture()))
        self.assertEqual(r["structural_assessment"], "PASS")
        self.assertEqual({x["obligation"] for x in r["execution_inventory"] if x["stage"] == "draft"},
                         {"draft-deferred"})
        self.assertEqual({x["obligation"] for x in r["execution_inventory"] if x["stage"] == "release"},
                         {"repro", "model", "freshness", "sign"})
        d = consolidated(fixture())
        byid(d, "acceptance")["stages"].append("draft")
        byid(d, "accept-job")["stages"].append("draft")
        self.assertEqual(overlap.audit(d)["structural_assessment"], "HOLD")

    def test_draft_requires_a_real_deferral_job_in_graph(self):
        d = consolidated(fixture())
        byid(d, "draft")["stages"] = ["candidate"]
        r = overlap.audit(d)
        self.assertEqual(r["structural_assessment"], "HOLD")
        self.assertIn("draft: required cheap deferral status not emitted", r["violations"])

    def test_distinct_platform_without_justification_is_unproven(self):
        d = fixture()
        byid(d, "other-repro")["platform"] = "windows-2025"
        r = overlap.audit(d)
        self.assertTrue(all(x["classification"] == "UNPROVEN" for x in r["overlaps"]))
        self.assertEqual(r["structural_assessment"], "HOLD")

    def test_unknown_script_path_blocks_optimization(self):
        d = consolidated(fixture())
        d["inventory_complete"] = False
        d["unresolved_invocations"] = ["workflow:dynamic-template"]
        self.assertEqual(overlap.audit(d)["structural_assessment"], "HOLD")

    def test_disposition_required_for_every_overlap(self):
        d = fixture()
        d["dispositions"] = []
        self.assertTrue(any("lacks documented disposition" in x
                            for x in overlap.audit(d)["violations"]))

    def test_disposition_cannot_keep_known_duplicate(self):
        d = fixture()
        for row in d["dispositions"]:
            row["decision"] = "KEEP"
        self.assertTrue(any("cannot be kept" in x for x in overlap.audit(d)["violations"]))

    def test_matrix_expansion_is_required(self):
        d = consolidated(fixture())
        byid(d, "accept-job")["matrix_expanded"] = False
        with self.assertRaises(overlap.InvalidInput):
            overlap.audit(d)

    def test_nested_reusable_workflow_supported(self):
        d = consolidated(fixture())
        byid(d, "accept-job")["invokes"] = ["reusable-workflow"]
        d["nodes"].append(node("reusable-workflow", "workflow", ["accept-recipe"],
                                stages=["candidate", "release"], entrypoint=False))
        r = overlap.audit(d)
        self.assertEqual(r["structural_assessment"], "PASS")
        self.assertTrue(any("reusable-workflow" in x["path"]
                            for x in r["execution_inventory"]))

    def test_input_duplicate_keys_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "bad.json"
            path.write_text('{"schema_version":1,"schema_version":1}', encoding="utf-8")
            p = subprocess.run([sys.executable, "-B", str(ROOT / "scripts" / "audit_execution_overlap.py"),
                                "--input", str(path)], capture_output=True, text=True)
            self.assertEqual(p.returncode, 2)
            self.assertIn("duplicate JSON key", p.stderr)

    def test_cli_exit_codes_and_no_writes(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "graph.json"
            path.write_text(json.dumps(fixture()), encoding="utf-8")
            before = set(Path(temp).iterdir())
            cmd = [sys.executable, "-B", str(ROOT / "scripts" / "audit_execution_overlap.py"),
                   "--input", str(path)]
            p = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(p.returncode, 3, p.stderr)
            self.assertEqual(json.loads(p.stdout)["structural_assessment"], "HOLD")
            path.write_text(json.dumps(consolidated(fixture())), encoding="utf-8")
            q = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(q.returncode, 0, q.stderr)
            self.assertEqual(json.loads(q.stdout)["structural_assessment"], "PASS")
            self.assertEqual(before, set(Path(temp).iterdir()))

    def test_symlinked_json_input_rejected_before_read(self):
        with tempfile.TemporaryDirectory() as temp:
            src = Path(temp) / "private.json"
            src.write_text(json.dumps(fixture()), encoding="utf-8")
            alias = Path(temp) / "alias.json"
            alias.symlink_to(src)
            p = subprocess.run([sys.executable, "-B", str(ROOT / "scripts" / "audit_execution_overlap.py"),
                                "--input", str(alias)], capture_output=True, text=True)
            self.assertEqual(p.returncode, 2)
            self.assertFalse(p.stdout)


if __name__ == "__main__":
    unittest.main()
