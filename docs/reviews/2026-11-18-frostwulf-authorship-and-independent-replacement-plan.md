> **Current status note:** This document preserves the original four-candidate
> kickoff evidence. The live draft PR has since advanced to 21 newly written
> and statically reviewed packages covering all 44 historical function
> categories, without retirement or observed host validation. See
> [current ledger](../../registry/migration/frostwulf-independent-replacement-ledger-20261118.json)
> and [gap/retirement audit](2026-11-18-frostwulf-replacement-equivalence-and-retirement-gates.md).

# Legacy Frostwulf skill origin and independent replacements

Status as of 2026-11-18: **44 inventoried, 4 independent draft replacements, 0 retired.**

## Corrected ownership finding

The relevant author marker is `frostwulf.zo.computer`. The user confirms
control of that Zo Computer account, not authorship of every skill. Historical
Git commits under `WulfForge` and `Knapp-Kevin` establish repository
submission history only. Neither the metadata marker nor a repository's MIT
license proves that all original source text was independently authored or
licensed for relicensing. No original-root skill was moved or removed.

## Method and migration gates

- Design each new skill from a clear user outcome, independently specified
  inputs, distinct decision procedure, output contract, authority model,
  failures and synthetic challenges.
- Inspect the legacy skill as untrusted comparative evidence to identify
  missing functionality and risks, never as text to paraphrase line by line.
- Explicitly identify shared generic ideas, track third-party influence when
  applicable, and do not import protected text, examples or hidden dependencies.
- Preserve full snapshot identity, license reasoning, distinctive improvements,
  static review and separate behavior evidence for each new package.
- Register each replacement in the authored, governed-review and capability
  indexes only after its individual source/package identity is fixed and its
  index schema reconciled.
- Prevent duplicate discovery: retain the source as legacy/reference-only while
  new material is in draft; remove its active route only when a replacement is
  qualified and all incoming references have been traced.
- Delete a legacy skill's files only after rights, substitution, consumers,
  references and backups/historical evidence are reconciled; separately verify
  the deletion and count adjustments. No blanket 44-file delete.

## First independent design tranche

| Legacy capability used for gap comparison | Independently authored candidate | New focus | Current gate |
| --- | --- | --- | --- |
| Fact checking | `claim-evidence-adjudicator` | claim dependency graph and contradictory source adjudication | draft |
| Paper digestion | `research-methods-appraiser` | experimental comparability and reproducibility ladder | draft |
| TODO aggregation | `source-debt-triage` | code-context triage, coverage and risk | draft |
| Decision log | `decision-record-steward` | owner authority and supersession chain | draft |

Full source-by-source migration state:
[`registry/migration/frostwulf-independent-replacement-ledger-20261118.json`](../../registry/migration/frostwulf-independent-replacement-ledger-20261118.json).

## Observed evidence vs absent evidence

Observed: 44 root-level entrypoint files and matching author markers on one
main snapshot; 4 distinct new source drafts and scenario specifications.
Some original entrypoints were read in full during comparative inspection.
Not established: independent copyright provenance for the 44 originals,
complete legal audit of embedded material, exact-version full static review
of each draft, observed host-model behavior, capability-directory/index
integration, or approval to retire originals.

**Do not treat these drafts as production-qualified or change the existing
governed review identity counts until registration and review are complete.**
