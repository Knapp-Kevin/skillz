#!/usr/bin/env python3
"""Optional host-invoked, offline public/synthetic discovery-trace recorder.

No work occurs on import. A user/host must establish actual permission and
public/synthetic clearance independently: --approved-public is not proof.
The recorded hashes prove internal integrity, not a test's authenticity.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import secrets
import stat
import sys

try:
    import fcntl
except ImportError:
    fcntl = None

FORMAT = 1
LIMIT = 1_048_576
MAX_NODES = 1000
ID = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
SHA1 = re.compile(r"^[0-9a-f]{40}$")
TASKS = frozenset({"schema-compatibility", "path-isolation", "ci-classification"})
ACTIONS = frozenset({"inspect", "adversarial-probe", "run-targeted-verification", "preservation-check"})
OUTCOMES = frozenset({"OBSERVED_PASS", "OBSERVED_FAIL", "BLOCKED"})
NODE_BASE = frozenset({"node_id", "parent_node_id", "record_type", "candidate_id", "task_family", "action", "source_artifact_git_blob", "workspace_state_digest", "evaluator_id", "evaluation_context_id"})
NODE_OBS = NODE_BASE | frozenset({"outcome", "receipt_digest", "post_workspace_state_digest", "post_source_artifact_git_blob"})
RECEIPT = frozenset({"node_id", "outcome", "action", "source_artifact_git_blob", "workspace_state_digest", "evaluator_id", "evaluation_context_id", "test_invocations", "wall_ms"})
EVENT = frozenset({"seq", "previous_digest", "kind", "payload", "digest"})
HEADER = frozenset({"schema_version", "experiment_id", "evaluator_id", "evaluation_context_id", "privacy_class"})
OBS_WRAPPER = frozenset({"node", "receipt", "evidence_file_digest", "evidence_basis"})


class TraceError(ValueError):
    """Invalid trace, unsafe operation or unverifiable local precondition."""


def require(ok, reason):
    if not ok:
        raise TraceError(reason)


def exact(obj, fields, what):
    require(type(obj) is dict and set(obj) == fields, what + ": invalid fields")


def identity(value, what):
    require(type(value) is str and ID.fullmatch(value) is not None, what + ": invalid identifier")


def fingerprint(value, pattern, what):
    require(type(value) is str and pattern.fullmatch(value) is not None, what + ": invalid digest")


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False) + "\n").encode("ascii")


def digest(value):
    return "sha256:" + hashlib.sha256(canonical(value)).hexdigest()


def json_pairs(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "JSON duplicate field")
        result[key] = value
    return result


def invalid_constant(value):
    raise TraceError("JSON non-finite value refused")


def load_json(raw):
    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=json_pairs, parse_constant=invalid_constant)
    except TraceError:
        raise
    except (ValueError, UnicodeError) as exc:
        raise TraceError("Invalid JSON or encoding") from exc


def receipt_digest(payload):
    """Match the frozen P0 receipt representation (no trailing newline)."""
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=True, allow_nan=False).encode("ascii")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _read_regular_file(path):
    path = Path(path)
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC)
        with os.fdopen(fd, "rb") as stream:
            info = os.fstat(stream.fileno())
            require(stat.S_ISREG(info.st_mode) and info.st_size <= LIMIT, "Input must be a bounded regular file")
            raw = stream.read(LIMIT + 1)
    except OSError as exc:
        raise TraceError("Cannot read authorized regular input") from exc
    require(len(raw) <= LIMIT, "Input size limit exceeded")
    return raw


def public_source(path):
    raw = _read_regular_file(path)
    return hashlib.sha1(b"blob " + str(len(raw)).encode("ascii") + b"\x00" + raw).hexdigest()


def public_snapshot(path):
    return "sha256:" + hashlib.sha256(_read_regular_file(path)).hexdigest()


def checked_root(root_arg):
    require(os.name == "posix" and fcntl is not None and hasattr(os, "O_NOFOLLOW"), "Private POSIX storage required; use a host-owned secure adapter")
    root = Path(root_arg).expanduser()
    require(root.is_absolute(), "Host must supply an absolute existing private directory")
    for parent in (root, *root.parents):
        try:
            info = parent.lstat()
        except OSError as exc:
            raise TraceError("Private root or ancestor missing") from exc
        require(stat.S_ISDIR(info.st_mode), "Symlink or non-directory root ancestor refused")
        if parent == root:
            require(info.st_uid == os.getuid() and not stat.S_IMODE(info.st_mode) & 0o077, "Root must be user-owned mode 0700")
        else:
            require(not (info.st_mode & 0o022 and not info.st_mode & stat.S_ISVTX), "Unsafe replaceable ancestor")
        require(parent.name != ".git" and not (parent / ".git").exists() and not (parent / ".git").is_symlink(), "Trace storage inside a Git checkout refused")
    return root


@contextmanager
def writer_lock(root):
    lock = root / ".trace.lock"
    fd = os.open(lock, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW | os.O_CLOEXEC, 0o600)
    try:
        st = os.fstat(fd)
        require(stat.S_ISREG(st.st_mode) and st.st_uid == os.getuid() and not stat.S_IMODE(st.st_mode) & 0o077 and st.st_nlink == 1, "Unsafe lock inode")
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise TraceError("Concurrent writer busy; retry") from exc
        yield
    finally:
        try:
            fcntl.flock(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)


def _log_path(root, experiment_id):
    identity(experiment_id, "experiment")
    return root / (experiment_id + ".trace.jsonl")


def _validate_node(node, header, observed):
    exact(node, NODE_OBS if observed else NODE_BASE, "node")
    for field in ("node_id", "candidate_id", "evaluator_id", "evaluation_context_id"):
        identity(node[field], field)
    require(type(node["task_family"]) is str and node["task_family"] in TASKS, "Unsupported task family")
    require(type(node["action"]) is str and node["action"] in ACTIONS, "Unsupported action")
    require(node["evaluator_id"] == header["evaluator_id"] and node["evaluation_context_id"] == header["evaluation_context_id"], "Evaluator/context drift")
    fingerprint(node["source_artifact_git_blob"], SHA1, "source")
    fingerprint(node["workspace_state_digest"], SHA256, "state")
    parent = node["parent_node_id"]
    require(parent is None or type(parent) is str and ID.fullmatch(parent) is not None, "Invalid parent")
    require(node["record_type"] == ("observation" if observed else "proposal"), "Wrong record type")
    if observed:
        require(type(node["outcome"]) is str and node["outcome"] in OUTCOMES, "Unobserved outcome")
        fingerprint(node["receipt_digest"], SHA256, "receipt")
        fingerprint(node["post_workspace_state_digest"], SHA256, "post state")
        fingerprint(node["post_source_artifact_git_blob"], SHA1, "post source")


def _check_log(raw):
    require(raw and len(raw) <= LIMIT and raw.endswith(b"\n"), "Incomplete or oversized trace; no silent tail recovery")
    lines = raw.splitlines()
    require(2 <= len(lines) <= MAX_NODES + 1, "Invalid trace length")
    events = []
    prev = "sha256:" + "0" * 64
    for seq, line in enumerate(lines):
        require(len(line) <= 8192, "Event too large")
        event = load_json(line)
        exact(event, EVENT, "event")
        require(type(event["seq"]) is int and event["seq"] == seq and event["previous_digest"] == prev, "Sequence/chain failure")
        fingerprint(event["digest"], SHA256, "event digest")
        value = {key: event[key] for key in EVENT if key != "digest"}
        require(digest(value) == event["digest"], "Tampered event digest")
        prev = event["digest"]
        events.append(event)
    require(events[0]["kind"] == "header" and events[1]["kind"] == "proposal", "Missing trace header/root")
    header = events[0]["payload"]
    exact(header, HEADER, "header")
    require(type(header["schema_version"]) is int and header["schema_version"] == FORMAT, "Unsupported trace version")
    identity(header["experiment_id"], "experiment")
    identity(header["evaluator_id"], "evaluator")
    identity(header["evaluation_context_id"], "context")
    require(header["privacy_class"] == "public-synthetic", "Unsupported privacy class")
    root = events[1]["payload"]
    _validate_node(root, header, observed=False)
    require(root["parent_node_id"] is None and root["action"] == "inspect", "Invalid proposal root")
    nodes = {root["node_id"]: root}
    receipts = []
    for event in events[2:]:
        require(event["kind"] == "observation", "Unexpected event kind")
        wrapper = event["payload"]
        exact(wrapper, OBS_WRAPPER, "observation wrapper")
        require(wrapper["evidence_basis"] == "host-supplied-file-unattested", "Unsupported evidence basis")
        fingerprint(wrapper["evidence_file_digest"], SHA256, "evidence input")
        node, receipt = wrapper["node"], wrapper["receipt"]
        _validate_node(node, header, observed=True)
        require(node["node_id"] not in nodes, "Duplicate node")
        parent = nodes.get(node["parent_node_id"])
        require(parent is not None, "Unobserved parent or cycle")
        before_source = parent["post_source_artifact_git_blob"] if parent["record_type"] == "observation" else parent["source_artifact_git_blob"]
        before_state = parent["post_workspace_state_digest"] if parent["record_type"] == "observation" else parent["workspace_state_digest"]
        require(node["source_artifact_git_blob"] == before_source and node["workspace_state_digest"] == before_state, "UNKNOWN_STATE: parent snapshot mismatch")
        exact(receipt, {"digest", "payload"}, "receipt")
        exact(receipt["payload"], RECEIPT, "receipt payload")
        rp = receipt["payload"]
        for key in ("node_id", "outcome", "action", "source_artifact_git_blob", "workspace_state_digest", "evaluator_id", "evaluation_context_id"):
            require(rp[key] == node[key], "Receipt binding mismatch")
        require(type(rp["test_invocations"]) is int and 1 <= rp["test_invocations"] <= 1000, "Invalid test count")
        require(type(rp["wall_ms"]) is int and 0 <= rp["wall_ms"] <= 86_400_000, "Invalid elapsed time")
        require(receipt_digest(rp) == receipt["digest"] == node["receipt_digest"], "Invalid receipt digest")
        require(receipt["digest"] not in {x["digest"] for x in receipts}, "Duplicate receipt")
        receipts.append(receipt)
        nodes[node["node_id"]] = node
    return {"header": header, "nodes": nodes, "events": events, "receipts": receipts, "last_digest": prev}


def _read_log(path):
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_CLOEXEC)
        with os.fdopen(fd, "rb") as stream:
            st = os.fstat(stream.fileno())
            require(stat.S_ISREG(st.st_mode) and st.st_uid == os.getuid() and not stat.S_IMODE(st.st_mode) & 0o077 and st.st_nlink == 1, "Unsafe trace inode")
            raw = stream.read(LIMIT + 1)
    except FileNotFoundError as exc:
        raise TraceError("Trace not found") from exc
    except OSError as exc:
        raise TraceError("Cannot open safe private trace") from exc
    require(len(raw) <= LIMIT, "Trace exceeds size bound")
    return _check_log(raw)


def _event(seq, prev, kind, payload):
    value = {"seq": seq, "previous_digest": prev, "kind": kind, "payload": payload}
    value["digest"] = digest(value)
    raw = canonical(value)
    require(len(raw) <= 8192, "Event exceeds size limit")
    return raw, value["digest"]


def _sync_dir(path):
    fd = os.open(path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def _write_whole(fd, data):
    # A single O_APPEND write per event. An interrupted/partial write is
    # explicitly BLOCKED and makes the log unreadable until manual recovery.
    written = os.write(fd, data)
    require(written == len(data), "Partial write: trace must be reviewed before reuse")
    os.fsync(fd)


def create(root_arg, experiment_id, evaluator_id, context_id, source_file, state_file, task_family, approved_public):
    require(approved_public, "Explicit authorization and public/synthetic clearance required")
    for val, field in ((evaluator_id, "evaluator"), (context_id, "context")):
        identity(val, field)
    require(task_family in TASKS if type(task_family) is str else False, "Unsupported task family")
    source, state = public_source(source_file), public_snapshot(state_file)
    root = checked_root(root_arg)
    path = _log_path(root, experiment_id)
    header = {"schema_version": FORMAT, "experiment_id": experiment_id, "evaluator_id": evaluator_id,
              "evaluation_context_id": context_id, "privacy_class": "public-synthetic"}
    root_id = "n-" + secrets.token_hex(12)
    proposal = {"node_id": root_id, "parent_node_id": None, "record_type": "proposal",
                "candidate_id": "root", "task_family": task_family, "action": "inspect",
                "source_artifact_git_blob": source, "workspace_state_digest": state,
                "evaluator_id": evaluator_id, "evaluation_context_id": context_id}
    first, first_hash = _event(0, "sha256:" + "0" * 64, "header", header)
    second, _ = _event(1, first_hash, "proposal", proposal)
    with writer_lock(root):
        try:
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC, 0o600)
        except FileExistsError as exc:
            raise TraceError("Trace already exists; append or choose a new experiment") from exc
        with os.fdopen(fd, "wb", buffering=0) as stream:
            _write_whole(stream.fileno(), first)
            _write_whole(stream.fileno(), second)
        _sync_dir(root)
        verified = _read_log(path)
        require(len(verified["nodes"]) == 1, "Post-write verification failed")
    return {"status": "CREATED", "experiment_id": experiment_id, "root_node_id": root_id}


def observe(root_arg, experiment_id, parent_node_id, evaluator_id, context_id,
            action, outcome, task_family, source_file, state_file, post_source_file,
            post_state_file, evidence_file, test_invocations, wall_ms, approved_public):
    require(approved_public, "Explicit authorization and public/synthetic clearance required")
    identity(parent_node_id, "parent node")
    identity(evaluator_id, "evaluator")
    identity(context_id, "context")
    require(type(action) is str and action in ACTIONS, "Disallowed action")
    require(type(task_family) is str and task_family in TASKS, "Unsupported task family")
    require(type(outcome) is str and outcome in OUTCOMES, "Disallowed outcome")
    require(type(test_invocations) is int and 1 <= test_invocations <= 1000, "Invalid test invocation count")
    require(type(wall_ms) is int and 0 <= wall_ms <= 86_400_000, "Invalid elapsed time")
    source, state = public_source(source_file), public_snapshot(state_file)
    post_source, post_state = public_source(post_source_file), public_snapshot(post_state_file)
    evidence = public_snapshot(evidence_file)
    root = checked_root(root_arg)
    path = _log_path(root, experiment_id)
    with writer_lock(root):
        trace = _read_log(path)
        header = trace["header"]
        require(header["experiment_id"] == experiment_id, "Trace identity changed")
        require(evaluator_id == header["evaluator_id"] and context_id == header["evaluation_context_id"], "Evaluator/context mismatch")
        parent = trace["nodes"].get(parent_node_id)
        require(parent is not None, "Unknown parent")
        require(len(trace["nodes"]) < MAX_NODES, "Node budget exhausted")
        expected_source = parent["post_source_artifact_git_blob"] if parent["record_type"] == "observation" else parent["source_artifact_git_blob"]
        expected_state = parent["post_workspace_state_digest"] if parent["record_type"] == "observation" else parent["workspace_state_digest"]
        require(source == expected_source and state == expected_state, "UNKNOWN_STATE: cannot reuse different parent snapshot")
        node_id = "n-" + secrets.token_hex(12)
        require(node_id not in trace["nodes"], "Generated node identity collided; retry without altering trace")
        payload = {"node_id": node_id, "outcome": outcome, "action": action,
                   "source_artifact_git_blob": source, "workspace_state_digest": state,
                   "evaluator_id": evaluator_id, "evaluation_context_id": context_id,
                   "test_invocations": test_invocations, "wall_ms": wall_ms}
        proof = {"digest": receipt_digest(payload), "payload": payload}
        node = {"node_id": node_id, "parent_node_id": parent_node_id, "record_type": "observation",
                "candidate_id": node_id, "task_family": task_family, "action": action,
                "source_artifact_git_blob": source, "workspace_state_digest": state,
                "evaluator_id": evaluator_id, "evaluation_context_id": context_id,
                "outcome": outcome, "receipt_digest": proof["digest"],
                "post_source_artifact_git_blob": post_source,
                "post_workspace_state_digest": post_state}
        wrapper = {"node": node, "receipt": proof, "evidence_file_digest": evidence,
                   "evidence_basis": "host-supplied-file-unattested"}
        raw, event_hash = _event(len(trace["events"]), trace["last_digest"], "observation", wrapper)
        require(path.stat().st_size + len(raw) <= LIMIT, "Trace size limit exhausted")
        fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_NOFOLLOW | os.O_CLOEXEC)
        try:
            st, current = os.fstat(fd), path.lstat()
            require(stat.S_ISREG(st.st_mode) and st.st_uid == os.getuid() and
                    not stat.S_IMODE(st.st_mode) & 0o077 and st.st_nlink == 1 and
                    (st.st_dev, st.st_ino) == (current.st_dev, current.st_ino), "Trace changed during append")
            _write_whole(fd, raw)
        finally:
            os.close(fd)
        checked = _read_log(path)
        require(checked["last_digest"] == event_hash and node_id in checked["nodes"], "Post-append integrity check failed")
    return {"status": "RECORDED_STRUCTURE_ONLY", "node_id": node_id,
            "outcome": outcome, "evidence_file_digest": evidence,
            "external_execution_authenticated": False}


def inspect(root_arg, experiment_id, export=False):
    root = checked_root(root_arg)
    trace = _read_log(_log_path(root, experiment_id))
    require(trace["header"]["experiment_id"] == experiment_id,
            "Trace experiment identity mismatch")
    if export:
        # Export exactly the Phase-0 closed-world trace contract, without a
        # runtime envelope or leaking any original file/path content.
        return {"schema_version": FORMAT,
                "experiment_id": experiment_id, "evaluator_id": trace["header"]["evaluator_id"],
                "evaluation_context_id": trace["header"]["evaluation_context_id"],
                "nodes": list(trace["nodes"].values()), "receipts": trace["receipts"]}
    return {"status": "STRUCTURE_ONLY", "experiment_id": experiment_id,
            "observations": len(trace["receipts"]), "nodes": len(trace["nodes"]),
            "last_digest": trace["last_digest"],
            "external_execution_authenticated": False}


def clear(root_arg, experiment_id, approved):
    require(approved, "Explicit approved revocation required")
    root = checked_root(root_arg)
    path = _log_path(root, experiment_id)
    with writer_lock(root):
        try:
            info = path.lstat()
        except FileNotFoundError:
            return {"status": "NOT_FOUND"}
        require(stat.S_ISREG(info.st_mode) and info.st_uid == os.getuid() and
                not stat.S_IMODE(info.st_mode) & 0o077 and info.st_nlink == 1, "Unsafe trace cannot be removed by helper")
        path.unlink()
        _sync_dir(root)
        require(not path.exists() and not path.is_symlink(), "Revocation verification failed")
    return {"status": "REMOVED"}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", required=True, help="Existing mode-0700 host-owned private directory")
    p.add_argument("--experiment-id", required=True)
    subs = p.add_subparsers(dest="command", required=True)
    ini = subs.add_parser("init")
    ini.add_argument("--evaluator-id", required=True)
    ini.add_argument("--context-id", required=True)
    ini.add_argument("--task-family", required=True, choices=sorted(TASKS))
    ini.add_argument("--source", required=True)
    ini.add_argument("--state", required=True)
    ini.add_argument("--approved-public", action="store_true")
    obs = subs.add_parser("observe")
    for flag in ("parent-node-id", "evaluator-id", "context-id", "source", "state",
                 "post-source", "post-state", "evidence"):
        obs.add_argument("--" + flag, required=True)
    obs.add_argument("--task-family", required=True, choices=sorted(TASKS))
    obs.add_argument("--action", required=True, choices=sorted(ACTIONS))
    obs.add_argument("--outcome", required=True, choices=sorted(OUTCOMES))
    obs.add_argument("--test-invocations", required=True, type=int)
    obs.add_argument("--wall-ms", required=True, type=int)
    obs.add_argument("--approved-public", action="store_true")
    subs.add_parser("verify")
    subs.add_parser("export")
    rem = subs.add_parser("clear")
    rem.add_argument("--approved", action="store_true")
    args = p.parse_args(argv)
    try:
        if args.command == "init":
            result = create(args.root, args.experiment_id, args.evaluator_id, args.context_id,
                            args.source, args.state, args.task_family, args.approved_public)
        elif args.command == "observe":
            result = observe(args.root, args.experiment_id, args.parent_node_id, args.evaluator_id,
                             args.context_id, args.action, args.outcome, args.task_family,
                             args.source, args.state, args.post_source, args.post_state,
                             args.evidence, args.test_invocations, args.wall_ms, args.approved_public)
        elif args.command == "clear":
            result = clear(args.root, args.experiment_id, args.approved)
        else:
            result = inspect(args.root, args.experiment_id, export=args.command == "export")
        print(json.dumps(result, sort_keys=True))
        return 0
    except (TraceError, OSError, UnicodeError, TypeError, ValueError) as exc:
        print(json.dumps({"status": "BLOCKED", "reason": str(exc)}, sort_keys=True), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
