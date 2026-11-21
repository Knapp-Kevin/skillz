#!/usr/bin/env python3
"""Standalone, repository-neutral, fail-closed PR impact classifier.

Requires a trusted-base policy for any reduced route. Does not run repository
code, authenticate event data or authorize a merge. Python 3.9+ and Git only.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Optional

SHA_RE = re.compile(r"[a-fA-F0-9]{40}(?:[a-fA-F0-9]{24})?\Z")
MAX_FILES = 2000
MAX_RULES = 256
CATEGORIES = frozenset({
    "documentation", "executable-code", "models", "dependencies",
    "governance", "workflows", "release-assets", "unknown"
})
MATCHES = frozenset({"exact", "prefix", "suffix"})
DEPENDENCY_NAMES = frozenset({
    "Cargo.toml", "Cargo.lock", "go.mod", "go.sum",
    "package.json", "package-lock.json", "pnpm-lock.yaml", "yarn.lock",
    "pyproject.toml", "poetry.lock", "uv.lock", "Pipfile", "Pipfile.lock",
    "requirements.txt", "Gemfile", "Gemfile.lock", "composer.json",
    "composer.lock", "pom.xml", "gradle.lockfile", "build.gradle",
    "build.gradle.kts", "settings.gradle", "settings.gradle.kts"
})
GOVERNANCE_NAMES = frozenset({
    "AGENTS.md", "CLAUDE.md", "CODEOWNERS", "SECURITY.md",
    "GOVERNANCE.md", "POLICY.md", "POLICIES.md"
})
MODEL_EXT = frozenset({
    ".onnx", ".gguf", ".safetensors", ".tflite", ".pte", ".pt",
    ".pth", ".h5", ".hdf5", ".pb", ".ckpt", ".mlmodel"
})
CODE_EXT = frozenset({
    ".py", ".pyi", ".rs", ".go", ".js", ".jsx", ".mjs", ".cjs",
    ".ts", ".tsx", ".java", ".kt", ".swift", ".c", ".h", ".cc",
    ".cpp", ".hpp", ".cs", ".rb", ".php", ".scala", ".sh",
    ".ps1", ".bat", ".cmd", ".lua", ".sql", ".wasm"
})
RELEASE_EXT = frozenset({
    ".whl", ".exe", ".msi", ".msix", ".dmg", ".apk", ".aab",
    ".ipa", ".vsix", ".deb", ".rpm", ".jar", ".nupkg"
})
RELEASE_NAMES = frozenset({"CHANGELOG.md", "RELEASE_NOTES.md", "RELEASE.md"})
POLICY_NAMES = frozenset({"impact-policy.json", "classify_change.py"})
ALWAYS_FULL = frozenset({"unknown", "governance", "workflows", "release-assets"})
CANDIDATE_FULL = frozenset({"executable-code", "models", "dependencies"})


class ClassificationError(ValueError):
    pass


def git(repo: Path, *args: str) -> bytes:
    try:
        return subprocess.check_output(
            ["git", "-C", str(repo), "-c", "core.hooksPath=/dev/null", *args],
            stderr=subprocess.PIPE, timeout=15
        )
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
              "--raw", "-z", base, head)
    # Raw --no-renames format: :oldmode newmode oldoid newoid status NUL path NUL.
    # Both sides of a rename are evaluated. A symlink, submodule, executable
    # bit or unknown file mode must never be misclassified as docs-only.
    chunks = raw.split(b"\0")
    if chunks and chunks[-1] == b"":
        chunks.pop()
    if len(chunks) % 2:
        raise ClassificationError("Malformed raw diff; refuse reduced checks")
    files = []
    nonregular = False
    for i in range(0, len(chunks), 2):
        header, path = chunks[i], chunks[i + 1]
        meta = header.decode("ascii", errors="strict").split()
        if len(meta) != 5 or not meta[0].startswith(":"):
            raise ClassificationError("Malformed raw change record")
        before_mode, after_mode, status = meta[0][1:], meta[1], meta[4]
        if status not in {"A", "M", "D", "T"}:
            nonregular = True
        if any(mode not in {"000000", "100644"} for mode in (before_mode, after_mode)):
            nonregular = True
        files.append(path.decode("utf-8", errors="strict"))
    if len(files) > MAX_FILES:
        return ["__TOO_MANY_CHANGED_FILES__"]
    if nonregular:
        files.append("__NONREGULAR_FILE_OR_MODE__")
    return files



def _safe_path(path: str) -> bool:
    return (isinstance(path, str) and bool(path) and not path.startswith("/")
            and not path.startswith("./") and not path.startswith("../")
            and not any(part in (".", "..", "") for part in path.split("/"))
            and "\\" not in path and not any(ord(ch) < 32 for ch in path))


def _no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ClassificationError("duplicate impact policy key")
        result[key] = value
    return result


def load_policy(path: Path) -> list[dict]:
    """Parse only trusted-base JSON; pattern matching never runs code."""
    try:
        if path.is_symlink() or path.stat().st_size > 131072:
            raise ClassificationError("unsafe impact policy input")
        raw = json.loads(path.read_text(encoding="utf-8"),
                         object_pairs_hook=_no_duplicate_keys)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ClassificationError("impact policy unavailable or invalid") from exc
    if not isinstance(raw, dict) or set(raw) != {"schema_version", "rules"}:
        raise ClassificationError("unexpected impact policy schema")
    if type(raw["schema_version"]) is not int or raw["schema_version"] != 1:
        raise ClassificationError("unsupported impact policy version")
    rules = raw["rules"]
    if not isinstance(rules, list) or len(rules) > MAX_RULES:
        raise ClassificationError("impact rules absent or excessive")
    normalized = []
    for rule in rules:
        if not isinstance(rule, dict) or set(rule) != {"match", "pattern", "category"}:
            raise ClassificationError("unknown impact rule property")
        match, pattern, category = rule["match"], rule["pattern"], rule["category"]
        if (not isinstance(match, str) or match not in MATCHES or
                not isinstance(category, str) or
                category not in CATEGORIES - {"unknown"}):
            raise ClassificationError("unsupported impact selector/category")
        if not isinstance(pattern, str) or len(pattern) > 255 or not pattern:
            raise ClassificationError("invalid impact pattern")
        if match == "suffix":
            if not pattern.startswith(".") or "/" in pattern or "\\" in pattern:
                raise ClassificationError("invalid suffix selector")
            # A global filename extension cannot establish that *every*
            # matching artifact is passive documentation. Some Markdown is
            # executable, generated input, governance or release evidence.
            if category == "documentation":
                raise ClassificationError(
                    "documentation rules require an exact path or directory prefix")
        elif match == "prefix":
            # Require a real directory boundary: "docs" also matches
            # "docsecrets/", "docs-private/" and similar unrelated paths.
            if not pattern.endswith("/") or not _safe_path(pattern[:-1]):
                raise ClassificationError(
                    "prefix selectors must name a directory ending in /")
        elif not _safe_path(pattern):
            raise ClassificationError("unsafe impact selector")
        normalized.append(rule)
    return normalized


def _built_in(path: str) -> set[str]:
    """Recognize universal danger boundaries without granting docs-only."""
    name = path.rsplit("/", 1)[-1]
    parts = path.lower().split("/")
    lowered = name.lower()
    cats = set()
    if name in GOVERNANCE_NAMES or lowered in ("agents.md", "claude.md"):
        cats.add("governance")
    if path.startswith((".github/workflows/", ".github/actions/")):
        cats.add("workflows")
    if name in POLICY_NAMES or path.startswith(("ci/", "scripts/ci/")):
        cats.add("workflows")
    if name in DEPENDENCY_NAMES or lowered.startswith(("requirements-", "dockerfile", "containerfile")):
        cats.add("dependencies")
    if lowered.endswith((".lock", ".lockb")):
        cats.add("dependencies")
    if parts[0] in ("release", "releases", "packaging", "dist"):
        cats.add("release-assets")
    if name in RELEASE_NAMES or Path(name).suffix.lower() in RELEASE_EXT:
        cats.add("release-assets")
    if Path(name).suffix.lower() in MODEL_EXT:
        cats.add("models")
    if Path(name).suffix.lower() in CODE_EXT:
        cats.add("executable-code")
    # Governance and generated interfaces are not merely their file extensions.
    if path.startswith(("docs/api-contracts/", "docs/generated-contracts/", "docs/governance/")):
        cats.add("governance")
    if path.startswith((".github/", "infra/", "infrastructure/", "deploy/", "deployment/")):
        cats.add("workflows")
    return cats


def _matches(path: str, rule: dict) -> bool:
    pattern = rule["pattern"]
    if rule["match"] == "exact":
        return path == pattern
    if rule["match"] == "prefix":
        # An already-validated rule has a trailing separator. Keep the
        # boundary check here as defense if a caller supplies direct rules.
        return pattern.endswith("/") and path.startswith(pattern)
    return path.endswith(pattern)


def classify(paths: list[str], policy: Optional[list[dict]] = None,
             stage: str = "candidate") -> dict:
    """Select generic targeted/full work, never authorize a merge.

    Absent trusted policy always means FULL. A draft may defer full work for
    *known* executable/model/dependency changes, but readiness, unknown or
    mandatory safety categories require full acceptance.
    """
    if stage not in ("draft", "candidate", "release"):
        raise ClassificationError("unknown development stage; no reduced route")
    unique = sorted(set(paths)) if paths else []
    invalid = (not unique or len(unique) > MAX_FILES
               or any(not _safe_path(x) for x in unique))
    categories = set()
    reasons = []
    if invalid:
        categories.add("unknown")
        reasons.append("missing-overlarge-or-unsafe-diff")
    for path in unique if not invalid else []:
        path_cats = _built_in(path)
        if policy is not None:
            path_cats.update(rule["category"] for rule in policy if _matches(path, rule))
        if not path_cats:
            path_cats.add("unknown")
            reasons.append("unmapped-impact")
        categories.update(path_cats)
    if policy is None:
        categories.add("unknown")
        reasons.append("trusted-policy-unavailable")
    full = bool(categories & ALWAYS_FULL) or stage == "release"
    if stage == "candidate" and categories & CANDIDATE_FULL:
        full = True
    target = not full
    return {
        "route": "full" if full else "targeted",
        "stage": stage,
        "categories": sorted(categories),
        "changed_count": len(unique),
        "changed_paths": unique[:MAX_FILES],
        "run_targeted": "true" if target else "false",
        "run_full": "true" if full else "false",
        "requires_exact_final_acceptance": bool(categories - {"documentation"}),
        "deferred_full_acceptance": bool(
            stage == "draft" and target and categories & CANDIDATE_FULL),
        "merge_qualified": False,
        "reason": ",".join(sorted(set(reasons))) or "trusted-identified-impact",
        "mandatory_floor": "independent required security, policy and trust checks always remain",
    }


def emit(result: dict, output: Optional[Path]) -> None:
    print(json.dumps(result, sort_keys=True))
    if output:
        with output.open("a", encoding="utf-8") as stream:
            # No PR-derived paths, rule text or arbitrary values go into GITHUB_OUTPUT.
            for key in ("route", "run_targeted", "run_full"):
                stream.write(f"{key}={result[key]}\n")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, default=Path("."))
    ap.add_argument("--base", help="exact base commit SHA")
    ap.add_argument("--head", help="exact head commit SHA")
    ap.add_argument("--stage", choices=("draft", "candidate", "release"), default="candidate")
    ap.add_argument("--policy", type=Path, help="trusted-base policy file; absent means full")
    ap.add_argument("--paths-file", type=Path, help="local fixture only, not a PR input")
    ap.add_argument("--github-output", type=Path)
    args = ap.parse_args()
    if args.paths_file:
        if args.base or args.head:
            ap.error("fixture and Git refs are mutually exclusive")
        paths = args.paths_file.read_text(encoding="utf-8").splitlines()
    else:
        if not args.base or not args.head:
            ap.error("both exact base and head commits are required")
        paths = changed_paths(args.repo.resolve(), args.base, args.head)
    policy = load_policy(args.policy) if args.policy else None
    emit(classify(paths, policy, args.stage), args.github_output)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ClassificationError, UnicodeError, OSError) as exc:
        print(f"CLASSIFICATION_UNVERIFIED: {exc}", file=sys.stderr)
        sys.exit(2)
