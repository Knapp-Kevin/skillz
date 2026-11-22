# Repository README Architect v0.5.2: Root README history-log advisory

**Date:** 2026-11-22. **Scope:** one original first-party authored package, read-only checker and package-local acceptance. No outside consumer or repository source imported.

## Behavioral defect corrected

The already published README Architect guidance says a root README should be a reader-facing project introduction and navigational front door, **not a running PR/commit changelog**. Its existing read-only link/generated-region checker did not expose that specific quality regression. A dense PR history could therefore pass all existing local checks while losing reader focus.

## Patch-level refinement

- `scripts/check_readme.py` now reports `CHRONOLOGICAL_LOG_ADVISORY` under repeated PR/date bullet entries (three or more) in a heading such as Recent PRs, Progress Log, Latest Updates or Changelog. The heading has to match an explicit log category and the entries must occur in the same section.
- **Advisory only**, not a local blocker, content deletion, editorial grade, or human-readability certification. It does not alter existing link integrity, generated block preservation, safe path, or CLI exit criteria.
- Eight additional negative/positive cases cover dense PR history, actual dated log, sparse PR mention, ordinary quick-start bullets, fenced Markdown example, section isolation, multiple independent sections, and zero exit code for editorial warnings.
- `SKILL.md` instructs editors to review and move history to proper maintained evidence only when authorized; preserving user-relevant current status and factual project content is mandatory.
- One path-scoped, draft-skipping GitHub Actions workflow runs the whole existing README Architect package test suite as a single offline contract job. It does not run unrelated corpus tests or material downstream consumer CI.

## Conservative semantic version decision

Version changes **only from 0.5.1 to 0.5.2**. This fulfills an already documented README front-door requirement with compatible, non-breaking additional diagnostics. No v0.6.0 or v1.x promotion. Future releases should not increment versions merely because a PR merges; major versions require explicit backwards-incompatible contract evidence.

## Acceptance/evidence limits

Source PR exact-head tests and complete package hash reconciliation are mandatory before calling this delivered. Until then, **PENDING**. Automated syntactic inspection does not prove user comprehension, accessible rendered navigation, or real external consumer adoption. Those remain NOT_RUN.
