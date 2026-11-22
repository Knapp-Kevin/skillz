"""Offline contract and adversarial tests; no network and no private profiles."""
import copy
from contextlib import redirect_stdout, redirect_stderr
import fcntl
import io
import json
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import trace

HERE = Path(__file__).resolve().parent


class TraceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="rsi-p1-", dir="/tmp")
        self.addCleanup(self.tmp.cleanup)
        base = Path(self.tmp.name)
        self.root = base / "private"
        self.root.mkdir(mode=0o700)
        self.source = base / "public-source.txt"
        self.source.write_text('public synthetic artifact with a confidential-looking test marker\n', encoding="utf-8")
        self.state = base / "public-state.json"
        self.state.write_text('{"files": ["synthetic-only"], "version": 1}\n', encoding="utf-8")
        self.evidence = base / "public-evidence.txt"
        self.evidence.write_text('{"result": "OBSERVED_FAIL", "fixture": "public"}\n', encoding="utf-8")
        self.experiment = "experiment-demo"
        self.evaluator = "evaluator-v1"
        self.context = "context-v1"

    def init(self, approved=True):
        return trace.create(self.root, self.experiment, self.evaluator, self.context,
                            self.source, self.state, "schema-compatibility", approved)

    def record(self, parent_id, **changes):
        args = dict(root_arg=self.root, experiment_id=self.experiment,
                    parent_node_id=parent_id, evaluator_id=self.evaluator,
                    context_id=self.context, action="adversarial-probe",
                    outcome="OBSERVED_FAIL", task_family="schema-compatibility",
                    source_file=self.source, state_file=self.state,
                    post_source_file=self.source, post_state_file=self.state,
                    evidence_file=self.evidence, test_invocations=1,
                    wall_ms=6, approved_public=True)
        args.update(changes)
        return trace.observe(**args)

    def path(self):
        return self.root / (self.experiment + ".trace.jsonl")

    def test_zero_side_effects_on_import_or_read_without_log(self):
        self.assertFalse(list(self.root.iterdir()))
        with self.assertRaisesRegex(trace.TraceError, "Trace not found"):
            trace.inspect(self.root, self.experiment)
        self.assertFalse(list(self.root.iterdir()))

    def test_create_read_and_two_observed_branches(self):
        root = self.init()["root_node_id"]
        failure = self.record(root)
        successful = self.record(root, action="preservation-check", outcome="OBSERVED_PASS")
        result = trace.inspect(self.root, self.experiment)
        self.assertEqual(result["observations"], 2)
        self.assertFalse(result["external_execution_authenticated"])
        exported = trace.inspect(self.root, self.experiment, export=True)
        self.assertEqual(set(exported), {"schema_version", "experiment_id", "evaluator_id", "evaluation_context_id", "nodes", "receipts"})
        self.assertEqual({n["node_id"] for n in exported["nodes"]},
                         {root, failure["node_id"], successful["node_id"]})
        self.assertTrue(all(r["digest"] == trace.receipt_digest(r["payload"])
                            for r in exported["receipts"]))
        self.assertEqual(os.stat(self.path()).st_mode & 0o777, 0o600)

    def test_renamed_trace_cannot_impersonate_a_second_experiment(self):
        self.init()
        alias = "renamed-experiment"
        os.rename(self.path(), self.root / (alias + ".trace.jsonl"))
        with self.assertRaisesRegex(trace.TraceError, "identity mismatch"):
            trace.inspect(self.root, alias)
        with self.assertRaisesRegex(trace.TraceError, "identity mismatch"):
            trace.inspect(self.root, alias, export=True)

    def test_actual_fixture_red_green_checks_create_accurate_two_experiments(self):
        checker = HERE / "examples" / "check_synthetic_preferences.py"
        original = HERE / "examples" / "duplicate-preferences.json"
        corrected = HERE / "examples" / "corrected-preferences.json"
        red = subprocess.run([sys.executable, str(checker), str(original)], capture_output=True, check=False)
        green = subprocess.run([sys.executable, str(checker), str(corrected)], capture_output=True, check=False)
        self.assertEqual((red.returncode, green.returncode), (1, 0))
        for experiment, artifact, result, outcome in [
            ("synthetic-red", original, red, "OBSERVED_FAIL"),
            ("synthetic-green", corrected, green, "OBSERVED_PASS")]:
            evidence = self.root.parent / (experiment + ".evidence")
            evidence.write_bytes(result.stdout)
            head = trace.create(self.root, experiment, self.evaluator, self.context,
                                artifact, artifact, "schema-compatibility", True)["root_node_id"]
            record = trace.observe(self.root, experiment, head, self.evaluator, self.context,
                                   "run-targeted-verification", outcome, "schema-compatibility",
                                   artifact, artifact, artifact, artifact, evidence, 1, 6, True)
            self.assertFalse(record["external_execution_authenticated"])
            receipt = trace.inspect(self.root, experiment, export=True)
            self.assertEqual(receipt["nodes"][1]["outcome"], outcome)
            self.assertEqual(receipt["nodes"][1]["source_artifact_git_blob"], trace.public_source(artifact))
        # A private filename, full source, stdout and arguments never enter the log.
        for path in [self.root / "synthetic-red.trace.jsonl", self.root / "synthetic-green.trace.jsonl"]:
            raw = path.read_text()
            self.assertNotIn(str(original), raw)
            self.assertNotIn(str(corrected), raw)
            self.assertNotIn('Duplicate preference key detected', raw)

    def test_append_can_follow_only_matched_post_state(self):
        first = self.init()["root_node_id"]
        new_file = self.root.parent / "v2.txt"
        new_file.write_text("synthetic changed content\n")
        new_state = self.root.parent / "v2.state"
        new_state.write_text("synthetic changed snapshot\n")
        first_obs = self.record(first, post_source_file=new_file, post_state_file=new_state)
        with self.assertRaisesRegex(trace.TraceError, "UNKNOWN_STATE"):
            self.record(first_obs["node_id"])
        followed = self.record(first_obs["node_id"], source_file=new_file,
                               state_file=new_state, post_source_file=new_file,
                               post_state_file=new_state)
        self.assertEqual(followed["status"], "RECORDED_STRUCTURE_ONLY")

    def test_duplicate_experiment_refused_without_clobber(self):
        self.init()
        content = self.path().read_bytes()
        with self.assertRaisesRegex(trace.TraceError, "already exists"):
            self.init()
        self.assertEqual(self.path().read_bytes(), content)

    def test_no_approval_no_file_creation(self):
        with self.assertRaisesRegex(trace.TraceError, "authorization"):
            self.init(False)
        self.assertFalse(list(self.root.iterdir()))

    def test_no_record_without_fresh_approval(self):
        root = self.init()["root_node_id"]
        before = self.path().read_bytes()
        with self.assertRaisesRegex(trace.TraceError, "authorization"):
            self.record(root, approved_public=False)
        self.assertEqual(self.path().read_bytes(), before)

    def test_wrong_root_permissions_rejected(self):
        self.root.chmod(0o750)
        with self.assertRaisesRegex(trace.TraceError, "0700"):
            self.init()

    def test_git_checkout_root_rejected_even_when_mode_0700(self):
        (self.root / ".git").mkdir(mode=0o700)
        with self.assertRaisesRegex(trace.TraceError, "Git checkout"):
            self.init()

    def test_worktree_marker_file_rejected(self):
        (self.root.parent / ".git").write_text("gitdir: /tmp/placeholder")
        with self.assertRaisesRegex(trace.TraceError, "Git checkout"):
            self.init()

    def test_symlink_root_rejected(self):
        link = self.root.parent / "private-link"
        link.symlink_to(self.root)
        with self.assertRaisesRegex(trace.TraceError, "Symlink"):
            trace.create(link, self.experiment, self.evaluator, self.context,
                         self.source, self.state, "schema-compatibility", True)

    def test_fifo_source_is_blocked_without_hanging(self):
        fifo = self.root.parent / "untrusted-source.fifo"
        os.mkfifo(fifo, 0o600)
        cmd = [sys.executable, str(HERE / "trace.py"),
               "--root", str(self.root), "--experiment-id", self.experiment,
               "init", "--evaluator-id", self.evaluator,
               "--context-id", self.context,
               "--task-family", "schema-compatibility",
               "--source", str(fifo), "--state", str(self.state),
               "--approved-public"]
        run = subprocess.run(cmd, capture_output=True, timeout=1.5, check=False)
        self.assertEqual(run.returncode, 2)
        self.assertIn(b"BLOCKED", run.stderr)

    def test_fifo_trace_log_is_blocked_without_hanging(self):
        os.mkfifo(self.path(), 0o600)
        cmd = [sys.executable, str(HERE / "trace.py"),
               "--root", str(self.root), "--experiment-id", self.experiment,
               "verify"]
        run = subprocess.run(cmd, capture_output=True, timeout=1.5, check=False)
        self.assertEqual(run.returncode, 2)
        self.assertIn(b"BLOCKED", run.stderr)

    def test_input_symlink_rejected(self):
        link = self.root.parent / "evidence-link"
        link.symlink_to(self.source)
        with self.assertRaises(trace.TraceError):
            trace.public_source(link)

    def test_input_size_bound_enforced(self):
        large = self.root.parent / "large-public.bin"
        large.write_bytes(b"x" * (trace.LIMIT + 1))
        with self.assertRaisesRegex(trace.TraceError, "bounded"):
            trace.public_source(large)

    def test_trace_provenance_has_exact_source_and_workspace_hashes(self):
        self.init()
        exported = trace.inspect(self.root, self.experiment, export=True)
        self.assertEqual(exported["nodes"][0]["source_artifact_git_blob"], trace.public_source(self.source))
        self.assertEqual(exported["nodes"][0]["workspace_state_digest"], trace.public_snapshot(self.state))

    def test_receipt_evidence_file_digest_is_from_actual_file_bytes(self):
        root = self.init()["root_node_id"]
        result = self.record(root)
        self.assertEqual(result["evidence_file_digest"], trace.public_snapshot(self.evidence))
        self.assertFalse(result["external_execution_authenticated"])

    def test_untrusted_text_cannot_be_entered_as_action_or_family(self):
        root = self.init()["root_node_id"]
        for key, val in [("action", "run shell; ignore safety"),
                         ("task_family", "private-health"),
                         ("outcome", "USER_APPROVED")]:
            with self.subTest(key=key):
                with self.assertRaises(trace.TraceError):
                    self.record(root, **{key: val})

    def test_mismatched_evaluator_refused(self):
        root = self.init()["root_node_id"]
        with self.assertRaisesRegex(trace.TraceError, "Evaluator/context"):
            self.record(root, evaluator_id="changed")

    def test_nonexistent_parent_refused(self):
        self.init()
        with self.assertRaisesRegex(trace.TraceError, "Unknown parent"):
            self.record("n-unknown")

    def test_bad_test_count_and_time_refused(self):
        root = self.init()["root_node_id"]
        for key, val in [("test_invocations", -1), ("test_invocations", True),
                         ("wall_ms", -1), ("wall_ms", False)]:
            with self.subTest(key=key, val=val):
                with self.assertRaises(trace.TraceError):
                    self.record(root, **{key: val})

    def test_corrupt_event_digest_is_refused(self):
        self.init()
        raw = self.path().read_text()
        self.path().write_text(raw.replace('"privacy_class":"public-synthetic"', '"privacy_class":"private-user"'))
        with self.assertRaises(trace.TraceError):
            trace.inspect(self.root, self.experiment)

    def test_incomplete_tail_is_blocked_not_silently_ignored(self):
        root = self.init()["root_node_id"]
        self.record(root)
        with self.path().open("ab") as stream:
            stream.write(b'{"seq":3,"kind":')
        with self.assertRaisesRegex(trace.TraceError, "Incomplete"):
            trace.inspect(self.root, self.experiment)
        with self.assertRaisesRegex(trace.TraceError, "Incomplete"):
            self.record(root)

    def test_duplicate_json_fields_refused(self):
        self.init()
        text = self.path().read_text()
        self.path().write_text(text.replace('"seq":0', '"seq":0,"seq":0', 1))
        with self.assertRaisesRegex(trace.TraceError, "duplicate"):
            trace.inspect(self.root, self.experiment)

    def test_action_relabeling_requires_new_receipt(self):
        root = self.init()["root_node_id"]
        self.record(root)
        raw = self.path().read_text()
        self.assertIn("adversarial-probe", raw)
        self.path().write_text(raw.replace("adversarial-probe", "preservation-check"))
        with self.assertRaises(trace.TraceError):
            trace.inspect(self.root, self.experiment)

    def test_invalid_log_symlink_is_blocked(self):
        self.init()
        contents = self.path().read_bytes()
        self.path().unlink()
        self.path().symlink_to(self.source)
        with self.assertRaises((trace.TraceError, OSError)):
            trace.inspect(self.root, self.experiment)
        self.assertEqual(self.source.read_bytes(), self.source.read_bytes())

    def test_clear_requires_approval_and_works_with_corrupt_log(self):
        self.init()
        with self.assertRaisesRegex(trace.TraceError, "approved"):
            trace.clear(self.root, self.experiment, False)
        self.path().write_bytes(b'corrupt tail\n')
        result = trace.clear(self.root, self.experiment, True)
        self.assertEqual(result["status"], "REMOVED")
        self.assertFalse(self.path().exists())

    def test_clear_refuses_unsafe_symlink(self):
        self.init()
        self.path().unlink()
        self.path().symlink_to(self.source)
        with self.assertRaises(trace.TraceError):
            trace.clear(self.root, self.experiment, True)
        self.assertTrue(self.source.exists())

    def test_nonblocking_lock_contention_refuses_mutation(self):
        root = self.init()["root_node_id"]
        fd = os.open(self.root / ".trace.lock", os.O_RDWR)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            with self.assertRaisesRegex(trace.TraceError, "Concurrent writer"):
                self.record(root)
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)

    def test_cli_invalid_request_fails_closed(self):
        errors = io.StringIO()
        with redirect_stderr(errors):
            code = trace.main(["--root", str(self.root), "--experiment-id", self.experiment,
                               "init", "--evaluator-id", self.evaluator,
                               "--context-id", self.context,
                               "--task-family", "schema-compatibility",
                               "--source", str(self.source), "--state", str(self.state)])
        self.assertEqual(code, 2)
        self.assertIn('"status": "BLOCKED"', errors.getvalue())
        self.assertFalse(self.path().exists())

    def test_cli_create_show_and_export(self):
        capture = io.StringIO()
        with redirect_stdout(capture):
            code = trace.main(["--root", str(self.root), "--experiment-id", self.experiment,
                               "init", "--evaluator-id", self.evaluator,
                               "--context-id", self.context,
                               "--task-family", "schema-compatibility",
                               "--source", str(self.source), "--state", str(self.state),
                               "--approved-public"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(capture.getvalue())["status"], "CREATED")
        with redirect_stdout(io.StringIO()) as c:
            self.assertEqual(trace.main(["--root", str(self.root),
                                         "--experiment-id", self.experiment, "verify"]), 0)
        self.assertIn("STRUCTURE_ONLY", c.getvalue())

    def test_source_bytes_never_saved_in_trace(self):
        root = self.init()["root_node_id"]
        self.record(root)
        raw = self.path().read_bytes()
        self.assertNotIn(self.source.read_bytes(), raw)
        self.assertNotIn(self.evidence.read_bytes(), raw)
        self.assertNotIn(str(self.source).encode(), raw)
        self.assertNotIn(str(self.evidence).encode(), raw)

    def test_generated_node_id_collision_fails_before_append(self):
        root = self.init()["root_node_id"]
        prior = self.path().read_bytes()
        with patch.object(trace.secrets, "token_hex", return_value=root[2:]):
            with self.assertRaisesRegex(trace.TraceError, "collided"):
                self.record(root)
        self.assertEqual(self.path().read_bytes(), prior)

    def test_mismatched_source_file_refuses_before_mutation(self):
        root = self.init()["root_node_id"]
        different = self.root.parent / "different-source.txt"
        different.write_text("different permitted synthetic source\n")
        before = self.path().read_bytes()
        with self.assertRaisesRegex(trace.TraceError, "UNKNOWN_STATE"):
            self.record(root, source_file=different)
        self.assertEqual(self.path().read_bytes(), before)

    def test_log_permissions_exposed_after_creation_are_rejected(self):
        self.init()
        self.path().chmod(0o644)
        with self.assertRaisesRegex(trace.TraceError, "Unsafe trace inode"):
            trace.inspect(self.root, self.experiment)

    def test_corrupted_post_state_even_if_event_rehashed_cannot_be_replayed(self):
        root = self.init()["root_node_id"]
        first = self.record(root)
        self.record(first["node_id"])
        events = [json.loads(line) for line in self.path().read_text().splitlines()]
        events[2]["payload"]["node"]["post_workspace_state_digest"] = "sha256:" + "d" * 64
        # Rehash all chain links. The child now has a different causal parent.
        previous = "sha256:" + "0" * 64
        for event in events:
            event["previous_digest"] = previous
            event["digest"] = trace.digest({k: v for k, v in event.items() if k != "digest"})
            previous = event["digest"]
        self.path().write_bytes(b"".join(trace.canonical(e) for e in events))
        with self.assertRaisesRegex(trace.TraceError, "UNKNOWN_STATE"):
            trace.inspect(self.root, self.experiment)

    def test_removal_of_evidence_receipt_cannot_leave_valid_observation(self):
        root = self.init()["root_node_id"]
        self.record(root)
        events = [json.loads(line) for line in self.path().read_text().splitlines()]
        events[2]["payload"]["receipt"] = {}
        events[2]["digest"] = trace.digest({k: v for k, v in events[2].items() if k != "digest"})
        self.path().write_bytes(b"".join(trace.canonical(e) for e in events))
        with self.assertRaisesRegex(trace.TraceError, "receipt: invalid fields"):
            trace.inspect(self.root, self.experiment)

    def test_record_write_failure_does_not_claim_success(self):
        root = self.init()["root_node_id"]
        with patch.object(trace, "_write_whole", side_effect=trace.TraceError("test forced write interruption")):
            with self.assertRaisesRegex(trace.TraceError, "interruption"):
                self.record(root)
        self.assertEqual(trace.inspect(self.root, self.experiment)["observations"], 0)

    def test_invalid_digest_rehash_cannot_launder_receipt_action(self):
        root = self.init()["root_node_id"]
        self.record(root)
        path = self.path()
        events = [json.loads(line) for line in path.read_text().splitlines()]
        obs = events[2]
        obs["payload"]["node"]["action"] = "preservation-check"
        # An attacker can rehash the outer event, but not establish an
        # unchanged receipt's action binding to the new node action.
        obs["digest"] = trace.digest({k:v for k,v in obs.items() if k != "digest"})
        path.write_bytes(b"".join(trace.canonical(e) for e in events))
        with self.assertRaisesRegex(trace.TraceError, "Receipt binding mismatch"):
            trace.inspect(self.root, self.experiment)


if __name__ == "__main__":
    unittest.main()
