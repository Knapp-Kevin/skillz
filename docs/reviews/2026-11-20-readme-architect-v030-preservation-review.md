# Repository README Architect v0.3: non-destructive delivery gates

**Date:** 2026-11-20. **Scope:** exact twelve-file first-party standalone package. **Status:** static maintainer review with executed local method tests; no independent host-agent validation.

## Root cause and source review

Version 0.2 required truthful statements and preserving generated spans, but failed to make *source-document preservation*, *formatter discovery*, *generator ownership* and *exact-HEAD CI status* explicit pre-delivery obligations. The dangerous failure is a cleaner-looking README that deletes legitimate technical limits, examples or provenance while removing template copy.

Two real public repository sources were separately read via GitHub:
- [UOR-Foundation/uor-comms](https://github.com/UOR-Foundation/uor-comms), main `82dae7aa7e15d4609f5cc5d43efb79ed60c14634`: README still contains template-derived paths/front door; PR #35 addresses the README. A preservation-first UPLIFT is appropriate but the actual original-vs-PR side-by-side acceptance was **not performed**.
- [UOR-Foundation/uor-framework](https://github.com/UOR-Foundation/uor-framework), main `51c01382200b0179d6640b07e9c8119364ab69a1`: the README explicitly identifies its generation by `uor-docs` and tells maintainers not to hand-edit the output. Correct action is inspect and change the controlling generator source **when explicitly in scope**, then regenerate and verify, not a direct README write. The generator implementation and output were **not executed**.

These are real source observations, not independent skill-host trials or evidence of completed UOR repairs.

## Actual implementation

1. **Mandatory formatter preflight:** before CREATE/UPLIFT, inspect scoped Prettier/markdownlint/Vale/.editorconfig rules, declared scripts, source workflows and ignore behavior. Use safe check-only local tooling if actually available and authorized; never run arbitrary scripts from README or spend GitHub Actions merely to discover a formatter mismatch.
2. **Loss prevention:** baseline-bound section IDs and SHA-256 normalized body, with one documented disposition per changed substantive section: RETAINED / RELOCATED / SUPERSEDED / OUTDATED / UNVERIFIED. Removed content with missing, stale or UNVERIFIED status blocks a clean delivery. Retention declarations and relocation evidence remain subject to human/source validation. Original generated regions still covered by the existing byte-preservation checker.
3. **Source ownership:** detect HTML and plain-language generation markers even in README footer, ignore fenced examples, and hold direct edits where the README belongs to a generator. Normative contract requires changing the generator/template with separate sufficient authority, then executing/verifying regeneration where possible.
4. **Exact-head CI:** documentation lint and unrelated repository-wide failures get separate attribution, but required checks are never waived or silently marked green. Unknown required-check inventory, stale head, skipped, neutral and pending required checks block merge-readiness claims.

Optional original offline Python helper `scripts/delivery_preflight.py` reads only bounded local source metadata, performs no subprocess/network/file writes and **always** reports `repository_merge_ready: false`. It supplements, not replaces, source-level and human evidence review. The complete mandatory procedure ships inside SKILL.md; no central repository policy or sibling skill is required.

## Local evidence and identity

- Actual Python 3.13.5 execution: `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -q` **101/101 PASS**, 0 failures (57 previously authored checks + 44 new delivery scenarios).
- Exact locally executed new helper Git blob `d11b678c1420eb83ef068654f7a1f337b8a1a78a`; test Git blob `872c1d77daf3a74c167e8c4f19694d6521860a1d`. Both match GitHub uploaded immutable blobs.
- Twelve-file package tree `a0c876e64a4e69ab4e2ea121a25b21d80e2c4d6c`; SKILL entrypoint `a0e2e2afb9d013ebbc7330c87120a0e97381518e`.
- Original v0.2 snapshot tree `aeb51bc194874ad18df1af7fb8d9b137d768da1b` retained as history. Existing 57-test suite and controls not weakened.

## Semantic review

Structured ten-dimension current **maintainer** assessment remains **19/20**, unchanged from v0.2: procedural, authority, failure and preservation hardening improves robustness but **effectiveness** remains 1/2 until independent reader/agent-host evaluations. This is a judgment of exact source text and actual bounded helper tests, **not** a claim of production acceptance or measured improvement.

Not yet verified: every exotic Markdown section, formatter execution on UOR repos, authenticated public branch policy, generator regeneration, independent multi-model or third-party consumer outcomes, production release/install, or external link results. No root README changelog change, unrelated code modification, new GitHub Actions job, CI budget consumption or automatic merge authority is in the helper.

[Machine receipt](../evals/receipts/2026-11-20-readme-architect-v030-preservation-gates.json).
