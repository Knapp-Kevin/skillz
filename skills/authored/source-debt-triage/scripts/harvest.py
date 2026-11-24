#!/usr/bin/env python3
"""Offline, read-only comment-context maintenance marker inventory.

Stdlib only. No git commands, network, execution, writes or source mutation.
Python comments: tokenize. C-like languages: conservative lexical scanner.
"""
from __future__ import annotations

import argparse
import io
import json
import os
from pathlib import Path
import re
import sys
import stat
import token
import tokenize

MARKER = re.compile(r"\b(TODO|FIXME|HACK|XXX)\b", re.IGNORECASE)
PYTHON = {".py", ".pyi"}
C_STYLE = {".c", ".h", ".cc", ".cpp", ".hpp", ".java", ".go", ".rs", ".js", ".jsx", ".ts", ".tsx"}
APPROXIMATE = {".js", ".jsx", ".ts", ".tsx"}
SKIP_DIRS = frozenset({".git", "node_modules", "vendor", "dist", "build", ".venv", "__pycache__"})
MAX_FILE_BYTES = 1_500_000
MAX_FILES = 4000


def python_comments(text: str) -> tuple[list[tuple[int, str]], str]:
    found = []
    try:
        incomplete = False
        for part in tokenize.generate_tokens(io.StringIO(text).readline):
            if part.type == token.COMMENT:
                found.append((part.start[0], part.string))
            elif part.type == token.ERRORTOKEN and part.string.strip():
                # Unclosed single-line strings can surface as ERRORTOKEN,
                # without tokenize raising TokenError.
                incomplete = True
        return found, "PARSE_INCOMPLETE" if incomplete else "EXACT_COMMENT_TOKENIZATION"
    except (tokenize.TokenError, IndentationError, SyntaxError, UnicodeError):
        return found, "PARSE_INCOMPLETE"


def c_comments(text: str, ext: str) -> tuple[list[tuple[int, str]], str]:
    """Find comments while excluding quoted strings and Rust raw strings.

    JS regex and template interpolation are not fully parsed; label as
    approximation. Rust nested comments and raw hashes are considered.
    """
    comments = []
    n, i, line = len(text), 0, 1
    approximate = ext in APPROXIMATE
    while i < n:
        ch = text[i]
        if ch == "\n":
            line += 1
            i += 1
            continue
        if ext == ".rs" and ch == "r":
            m = re.match(r'r(#{0,32})"', text[i:])
            if m:
                end = '"' + m.group(1)
                start = i + len(m.group(0))
                stop = text.find(end, start)
                if stop < 0:
                    return comments, "PARSE_INCOMPLETE"
                line += text.count("\n", i, stop + len(end))
                i = stop + len(end)
                continue
        if ch in "'\"\x60":
            quote = ch
            pos = i + 1
            closed = False
            while pos < n:
                if text[pos] == "\n":
                    line += 1
                if text[pos] == "\\" and quote != "\x60":
                    pos += 2
                    continue
                if text[pos] == quote:
                    pos += 1
                    closed = True
                    break
                if quote == "\x60" and ext in APPROXIMATE and text.startswith("$" + "{", pos):
                    approximate = True
                pos += 1
            if not closed:
                return comments, "PARSE_INCOMPLETE"
            i = pos
            continue
        if text.startswith("//", i):
            end = text.find("\n", i)
            if end < 0:
                end = n
            comments.append((line, text[i:end]))
            i = end
            continue
        if text.startswith("/*", i):
            startline, start = line, i
            depth = 1
            i += 2
            while i < n and depth:
                if ext == ".rs" and text.startswith("/*", i):
                    depth += 1
                    i += 2
                elif text.startswith("*/", i):
                    depth -= 1
                    i += 2
                else:
                    if text[i] == "\n":
                        line += 1
                    i += 1
            if depth:
                return comments, "PARSE_INCOMPLETE"
            comments.append((startline, text[start:i]))
            continue
        i += 1
    state = "LEXICAL_REVIEW_REQUIRED" if approximate else "C_STYLE_LEXICAL"
    return comments, state


def inspect(root: Path, max_rows: int = 100) -> dict:
    # Do not let Path.resolve() silently follow a caller-selected
    # symlinked root or parent before the authorized boundary is checked.
    # This is a lexical preflight, not a TOCTOU-proof filesystem sandbox:
    # a hostile concurrently mutating filesystem needs a stronger host.
    root = root.absolute()
    if any(part.is_symlink() for part in (root, *root.parents)):
        raise ValueError("Symlinked root or ancestor not allowed")
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Root must be a directory")
    markers = []
    counts = {kind: 0 for kind in ("TODO", "FIXME", "HACK", "XXX")}
    states, skipped = {}, []
    unsupported = scanned = omitted = 0
    stopped_at_limit = False
    def traversal_error(_error):
        # Do not echo the OS error or a possibly private absolute path.
        skipped.append({"path": "(withheld)", "reason": "directory-enumeration-failed"})
    for folder, dirs, files in os.walk(root, topdown=True, onerror=traversal_error, followlinks=False):
        kept = []
        for d in sorted(dirs):
            p = Path(folder) / d
            if d == ".git":
                # Repository object database is metadata, not source coverage.
                continue
            if d in SKIP_DIRS or p.is_symlink():
                skipped.append({"path": p.relative_to(root).as_posix(), "reason": "excluded-directory-or-symlink"})
            else:
                kept.append(d)
        dirs[:] = kept
        for filename in sorted(files):
            p = Path(folder) / filename
            rel = p.relative_to(root).as_posix()
            if p.is_symlink():
                skipped.append({"path": rel, "reason": "symlink"})
                continue
            ext = p.suffix.lower()
            if ext not in PYTHON | C_STYLE:
                unsupported += 1
                continue
            if scanned >= MAX_FILES:
                stopped_at_limit = True
                omitted += 1
                continue
            try:
                info = p.lstat()
                if not stat.S_ISREG(info.st_mode):
                    skipped.append({"path": rel, "reason": "nonregular-file"})
                    continue
                if info.st_size > MAX_FILE_BYTES:
                    skipped.append({"path": rel, "reason": "file-too-large"})
                    continue
                with p.open("rb") as stream:
                    raw = stream.read(MAX_FILE_BYTES + 1)
                if len(raw) > MAX_FILE_BYTES:
                    skipped.append({"path": rel, "reason": "file-too-large"})
                    continue
                content = raw.decode("utf-8")
            except (OSError, UnicodeError):
                skipped.append({"path": rel, "reason": "unreadable-or-not-utf8"})
                continue
            scanned += 1
            found, state = python_comments(content) if ext in PYTHON else c_comments(content, ext)
            states[state] = states.get(state, 0) + 1
            for startline, comment in found:
                for m in MARKER.finditer(comment):
                    kind = m.group(1).upper()
                    position = startline + comment.count("\n", 0, m.start())
                    counts[kind] += 1
                    if len(markers) < max_rows:
                        markers.append({
                            "file": rel, "line": position, "kind": kind,
                            "subsystem": rel.split("/", 1)[0] if "/" in rel else "(root)",
                            "triage": "UNREVIEWED", "age": "AGE_UNKNOWN",
                            "tokenization": state,
                        })
    total = sum(counts.values())
    partial = bool(stopped_at_limit or skipped or states.get("PARSE_INCOMPLETE", 0)
                   or states.get("LEXICAL_REVIEW_REQUIRED", 0))
    return {
        "schema_version": "source-debt-comment-harvest/1",
        "scope": root.name,
        "revision": "UNVERIFIED_CALLER_WORKTREE",
        "scan_status": "PARTIAL" if partial else "COMPLETE_FOR_SUPPORTED_LEXICAL_PARSERS",
        "counts": counts, "markers_detected": total,
        "markers_reported": len(markers), "markers_not_shown": total - len(markers),
        "source_files_scanned": scanned, "non_source_files_not_assessed": unsupported,
        "skipped": skipped, "skipped_count": len(skipped),
        "files_beyond_scan_limit": omitted, "tokenization_states": states,
        "markers": markers,
        "limitations": [
            "No age, issue status, root cause or triage disposition established",
            "Python comment tokens exact for parsable input; C-like lexical scan is not compiler parsing",
            "JS/TS regex, template interpolation and conditional preprocessors need review",
            "Generated/vendor directories excluded by declared scope, not confirmed provenance",
            "Untracked/worktree changes possible; caller must pin revision and review diff",
            "Marker text intentionally not printed to prevent source-secret leakage",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--max-rows", type=int, default=100)
    args = parser.parse_args()
    if not 0 <= args.max_rows <= 10000:
        parser.error("--max-rows must be in 0..10000")
    result = inspect(args.root, args.max_rows)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0 if result["scan_status"] == "COMPLETE_FOR_SUPPORTED_LEXICAL_PARSERS" else 3


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, RecursionError):
        print("HARVEST_UNAVAILABLE: invalid or unreadable approved root", file=sys.stderr)
        sys.exit(2)
