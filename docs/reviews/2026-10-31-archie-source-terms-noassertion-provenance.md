# Archie Indian pinned source terms and 56-companion provenance correction (2026-10-31)

## Decision and authority

The registered tracked source `archieindian-superpowers` points to `archieindian/openclaw-superpowers` at exact revision `a95a59d221d44b89d4fc27a52934e24fb2060ddb`. The pinned upstream `LICENSE` blob is `7869c12457fe7aee29e85b93036280bfde5380c2`, 259 bytes. The current upstream `LICENSE` is the same blob. It begins with the label `MIT License` and an opening permission grant, but lacks the standard MIT notice-preservation condition and warranty/liability disclaimer. A label is not a verified complete SPDX grant; terms remain unresolved in issue #544.

The registry and all **56** individual pinned provenance companions previously had `license: MIT`, even though their rationales noted the truncated license. This was an inconsistent structured license assertion. This tranche changes the machine-readable license field to `NOASSERTION`, preserves the upstream claim as `upstream_license_label: MIT`, and records `license_terms_status: incomplete-upstream-license`. It does **not** replace, supplement, or silently relicense the upstream text.

## Exact scope and invariant checks

- Source family: **56/56** first-class exact-pin static provenance/verification pairs; 17 core, 38 OpenClaw-native, 1 community. No genuine static gap, denominator delta **0**.
- Changed: 56 `registry/skills/archieindian-superpowers/*.yaml` provenance companions and `registry/sources.yaml`. No `registry/verification/` record, score, static disposition, source pin, source package, source-owned tooling, package fingerprint, revision, or tag changed.
- Preserved: all existing individual authority/privacy findings and explicit `not-run` package-security and external behavioral states. This correction is source-terms provenance, **not** a new static semantic review, scanner result, behavioral acceptance, admission, or redistribution permission.
- Tracked external-reference use remains permitted as a reference to observed upstream material; vendoring, material copying/adaptation and unchanged-use approval are held pending authoritative complete terms and separate security/authority/user-fit gates.
- The five public accounting surfaces were inspected against current main. Counts remain **44 first-party / 995 persisted third-party / 1039 total matching verification/provenance pairs**, with **874 registered/tracked + 121 candidate-only** third-party records. No count changes are warranted by a license-field correction.

## Macro finding and follow-up

The source-family review accurately detected the incomplete license, but a free-text rationale was not enough while structured `license: MIT` continued to imply clearance. Future license ambiguities must be represented in structured provenance, preserving the exact upstream claim separately from the verified terms.

**Issue #544 remains OPEN**. Closure requires maintainer-controlled upstream correction/clarification tied to an exact revision and a fresh license/redistribution decision. This review does not create a new issue or invent a legal conclusion.
