#!/usr/bin/env python3
"""Deterministic, conservative change-impact classifier for CI Guard.

Optional standalone executable shipped inside the CI Guard skill package.
No network, dependencies, secrets, or arbitrary repository code execution.
GitHub Actions template executes it from a TRUSTED BASE checkout, never from
untrusted PR changes. The workflow must retain independently required checks.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

SHA_RE = re.compile(r"[a-fA-F0-9]{40}(?:[a-fA-F0-9]{24})?\Z")
DOC_SUFFIXES = {".md", ".markdown", ".rst", ".adoc"}
PYTHON_SUFFIXES = {".py", ".pyi"}
SPECIAL_DOCS = {"README", "README.md", "CHANGELOG.md", "CONTRIBUTING.md"}
PROTECTED_NAMES = {
    "CODEOWNERS", "LICENSE", "LICENSE.md", "SECURITY.md",
    "pyproject.toml", "setup.py", "setup.cfg", "tox.ini", "pytest.ini",
    "Pipfile", "Pipfile.lock", "uv.lock", "poetry.lock",
    "Dockerfile", "Makefile", "Justfile", ".gitmodules",
    "package.json", "package-lock.json", "pnpm-lock.yaml",
    "Cargo.toml", "Cargo.lock", "go.mod", "go.sum",
}
PROTECTED_PREFIXES = (
    ".github/workflows/", ".github/actions/", ".github/CODEOWNERS",
    ".github/dependabot", "ci/", "scripts/ci/", "packaging/", "release/",
    "infra/", "infrastructure/", "terraform/", "deploy/", "deployment/",
    "migrations/", "docs/api-contracts/", "docs/generated-contracts/",
)
MAX_FILES = 2000


class ClassificationError(ValueError):
    pass


def git(repo: Path, *args: str) -> bytes:
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo), "-c", "core.hooksPath=/dev/null", *args],
            stderr=subprocess.PIPE, timeout=15)
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise ClassificationError("Git comparison unavailable; refuse to skip checks") from exc


def changed_paths(repo: Path, base: str, head: str) -> list[str]:
    """Compare exact refs, including changed/deleted paths, without rename suppression.

    Renames are deliberately represented as delete+add so both the old and
    new location affect classification; filenames are NUL delimited.
    """
    if not SHA_RE.fullmatch(base) or not SHA_RE.fullmatch(head):
        raise ClassificationError("Base and head must be full commit SHA values")
    for ref in (base, head):
        actual = git(repo, "rev-parse", "--verify", ref + "^{commit}").strip().decode()
        if actual.lower() != ref.lower():
            raise ClassificationError("Unverified commit object: " + ref)
    raw = git(repo, "diff", "--no-ext-diff", "--no-renames",
              "--name-only", "-z", base, head)
    files = [p.decode("utf-8", errors="strict") for p in raw.split(b"\0") if p]
    if len(files) > MAX_FILES:
        return ["__TOO_MANY_CHANGED_FILES__"]
    return files


def is_protected(path: str) -> bool:
    name = Path(path).name
    lower = path.lower()
    if path in PROTECTED_NAMES or name in PROTECTED_NAMES:
        return True
    if name.startswith(("requirements", "Dockerfile", "Containerfile")):
        return True
    if lower.endswith((".lock", ".toml", ".ini", ".cfg", ".yml", ".yaml",
                       ".json", ".sh", ".ps1", ".bat", ".cmd")):
        return True
    return path.startswith(PROTECTED_PREFIXES)


def classify(paths: list[str]) -> dict:
    """Return selected check categories, conservative reason and normalized paths.

    The example supports focused Python and documentation checks. Other code,
    unknown paths and protected config must fall back to FULL. This is NOT a
    source dependency graph and cannot independently exempt required gates.
    """
    if not paths:
        paths = ["__EMPTY_OR_UNVERIFIED_DIFF__"]
    unique = sorted(set(paths))
    if len(unique) > MAX_FILES:
        unique = ["__TOO_MANY_CHANGED_FILES__"]
    invalid = any(
        not path or path.startswith("/") or path.startswith("../")
        or "/../" in path or "\\" in path or any(ord(ch) < 32 for ch in path)
        for path in unique
    )
    categories = set()
    reason = []
    if invalid:
        categories.add("full")
        reason.append("unsafe-filename")
    for path in unique:
        if is_protected(path):
            categories.add("full")
            reason.append("protected-config-or-boundary")
        elif Path(path).suffix.lower() in DOC_SUFFIXES or path in SPECIAL_DOCS:
            categories.add("docs")
        elif Path(path).suffix.lower() in PYTHON_SUFFIXES:
            categories.add("python")
        else:
            categories.add("full")
            reason.append("unknown-or-cross-language-impact")
    if "full" in categories:
        # Include targeted jobs alongside full integration checks: the full
        # suite in real consumers is policy-defined and must not be a no-op.
        selected = ["docs", "python", "full"]
        route = "full"
    elif categories == {"docs"}:
        selected, route = ["docs"], "docs"
    elif categories == {"python"}:
        selected, route = ["python"], "python"
    else:
        selected, route = ["docs", "python"], "mixed"
    return {
        "route": route, "selected": selected,
        "run_docs": "true" if "docs" in selected else "false",
        "run_python": "true" if "python" in selected else "false",
        "run_full": "true" if "full" in selected else "false",
        "reason": ",".join(sorted(set(reason))) or "recognized-paths",
        "changed_count": len(unique),
        "changed_paths": unique,
        "mandatory_floor": "independent required security, policy and trust checks always remain",
    }


def emit(result: dict, output: Path | None) -> None:
    print(json.dumps(result, sort_keys=True))
    if output is not None:
        # Only fixed validated literals reach the GitHub output file.
        rows = {k: result[k] for k in
                ("route", "run_docs", "run_python", "run_full", "reason")}
        with output.open("a", encoding="utf-8") as out:
            for key, value in rows.items():
                out.write(f"{key}={value}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--base", help="trusted PR base commit full SHA")
    parser.add_argument("--head", help="PR head commit full SHA")
    parser.add_argument("--paths-file", type=Path,
                        help="local line-separated path fixture only")
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args()
    if args.paths_file and (args.base or args.head):
        parser.error("choose exact git refs OR a local fixture, not both")
    if args.paths_file:
        paths = args.paths_file.read_text(encoding="utf-8").splitlines()
    else:
        if not args.base or not args.head:
            parser.error("--base and --head are required with git mode")
        paths = changed_paths(args.repo.resolve(), args.base, args.head)
    emit(classify(paths), args.github_output)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ClassificationError, UnicodeError, OSError) as exc:
        # An unavailable comparison is not permission to infer docs-only.
        print(f"CLASSIFICATION_UNVERIFIED: {exc}", file=sys.stderr)
        sys.exit(2)
