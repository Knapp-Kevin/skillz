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
    source, state = public_source(sour