# Archie Indian OpenClaw Superpowers: final internal rights disposition (#544)

**Decision (2026-11-04): REFERENCE-ONLY / NOASSERTION / BLOCK REUSE.** This concludes the bounded downstream rights-risk classification. It does **not** repair or certify the upstream copyright license.

## Canonical evidence

- Pinned upstream: `archieindian/openclaw-superpowers` commit `a95a59d221d44b89d4fc27a52934e24fb2060ddb`.
- At that commit and at the upstream current default branch, root `LICENSE` is the **same 259-byte Git blob** `7869c12457fe7aee29e85b93036280bfde5380c2`.
- The document names MIT but stops after its opening permission grant. The notice-preservation condition and standard warranty/liability disclaimer are not present. No complete standard MIT grant is inferred from a heading or GitHub license detection; SPDX stays `NOASSERTION`.
- The 56 source-specific provenance YAML records were enumerated. **56/56** already state `license: NOASSERTION`, `upstream_license_label: MIT`, `license_terms_status: incomplete-upstream-license`, and `relationship: external-reference`. There is no vendored executable package from this source inside skillz.

## Concrete corrective action

- The `registry/sources.yaml` entry now states `import_eligibility: reference-only-license-hold` and `redistribution_and_adaptation: blocked-pending-maintainer-confirmed-terms`.
- 51/56 source-specific records already carried the stricter `reference-only-rejected-unchanged` status. Five individually reviewed records previously used conditional/adaptable eligibility wording. Their `import_eligibility` has now been changed to `reference-only-license-hold`: `brainstorming`, `pull-request-feedback-loop`, `secrets-hygiene`, `skill-effectiveness-auditor`, and `verification-before-completion`.
- No source package SKILL.md, review rubric grade, exact source pin, historical identity, inventory total, or original license text was altered. Discovery/reference value is preserved; safe use is **not** granted.

## What is and is not permitted

- **Allowed:** retaining public repository pointers and attributed, factual, high-level research observations; independently authored general concepts without copying expressive upstream text or code.
- **Blocked:** treating any of the 56 packages as licensed for unchanged import/installation, copying distinctive procedure text or bundled code into products, derivative redistribution, vendoring, and automatic promotion merely because a static source review scored well.
- **Reassessment trigger:** upstream maintainer publishes a corrected/clarified rights document at a verifiable revision, or independently substantiated per-file rights evidence is supplied. Before any changed eligibility, conduct new exact-version license/notice analysis, security checks, authority/privacy evaluation, and user-fit review.
- **Residual uncertainty:** upstream terms remain incomplete. This is not an upstream fix. It is a conservative, durable downstream **no-reuse decision** that removes the immediate ambiguous adoption path. Follow ongoing upstream change discovery under #599; reopen #544 if changed upstream rights create a real requalification task.

## Validation

Verify all 56 per-skill provenance files retain their source identity and `NOASSERTION`; 51 remain reference-only rejected unchanged and the other five are explicit license holds. Verify `registry/sources.yaml` source-level license hold matches; no review/verification files or source package content changed. This classification requires no SkillSpector run because nothing was installed, executed or re-licensed. It does **not** reduce the separate P0 #402 scanner backlog.
