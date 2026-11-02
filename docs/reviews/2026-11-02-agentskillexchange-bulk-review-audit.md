# Independent audit of the AgentSkillExchange bulk static review (2026-11-02)

**Scope:** the 3,199 AgentSkillExchange source-vetting records published in #632 and #634–#638, plus the identity segmentation and capability index.
**Auditor:** an independent read-only reviewer that did not produce the original reviews.
**Verdict:** **PASS-WITH-DEFECTS**. No defect changed any package's eligibility, and no record was promoted toward adoption.

## Sample and agreement

The sample was **95 records**, stratified and deterministically chosen:
- 15 description-only stubs;
- 30 authored procedures, including every REFERENCE-ONLY scoring 17 or more, every override and both license-conflict records;
- 40 install pointers across all five pointer ledgers;
- all 6 duplicate-pair members;
- all 3 DEFER records;
- the excluded template.

| Check | Agreement |
|---|---:|
| Exact blob and tree identity against the pin | 95/95 |
| Package file inventory | 94/95 |
| Total score within 2 points | 94/94 (88 exact; none off by 3 or more) |
| Authority dimension | 93/95 |
| Hard-fail flags | 91/95 |
| Disposition | 93/95 |

Beyond the sample, the auditor checked population-level facts:
- **Identity:** all 3,199 records match their pinned blob and tree, and decision totals reconcile to 3,125 REJECT, 71 REFERENCE-ONLY and 3 DEFER.
- **Deferrals:** all 3 DEFER blockers are files genuinely absent from the pinned package.
- **Reporting:** no README, accounting surface or directory statement presents these decisions as governed review, verification, admission or approved use.

The auditor would have scored `openhook` and `darkmoon-pentest-mcp` at 1/2 on authority rather than 0/2. Both integration overrides are more conservative, not unsafe, so they are kept and the disagreement is recorded here.

## Defects and repairs

| # | Defect | Affected | Repair |
|---|---|---|---|
| 1 | Nested DocsBot records listed only their SKILL.md | 3 | `package_owned_files` now lists the full nested subtree |
| 2 | darkmoon finding text contradicted the override | 1 | Adjudicated finding written; the reviewer's text is kept in `reviewer_original_authority_finding` |
| 3 | Hard-fail flag missing on ungated active attack tools and autonomous issue creation (authority already 0/2) | 6 | `unauthorized-consequential-action` added. All were already REJECT; no decision change |
| 4 | DEFER basis stated inconsistently | 5 | DEFER rule recorded in the authored-procedures ledger, and the macro wording corrected. No relabel: the 3 DEFER records meet the rule, and the 2 REFERENCE-ONLY cards carry substantive procedure of their own |
| 5 | Exact duplicate twin graded 5 vs 6 | 1 pair | The `-2` twin is regraded identically to its canonical twin, with the original scores kept. `duplicate_basis` wording corrected for all 3 pairs |
| 6 | Rationale text rotated across three dimensions in one reviewer batch | 24 (the whole affected cluster: developer-tools batch 1) | Rationales re-derived from each pinned card; originals kept under `audit_repair_20261102.original_rationale` |
| 7 | Template rationale phrases contradicting the card | 41 | Re-derived from the cards, in the same pass as #6 |
| 8 | Prefix and denominator formatting (`1: 1/2:`, `/1`, `(max 1)`) | 395 rationale strings | Normalized to `n/2:`. The pointer-card cap is documented in each pointer ledger's `rubric_calibration_note`; scores unchanged |
| 9 | Stale "545 … 55 REFERENCE-ONLY" sentence in the capability directory | 1 | Corrected to 3,196 terminal (3,125 / 71) plus 3 DEFER |
| — | "Fully dispositioned" wording overstated, because 3 DEFER remain | 4 surfaces | Reworded to name the 3 DEFER and the excluded template |

The repair pass (#6–#7) rewrote 175 dimension rationales and changed **5 scores**, each from 1 to 0 and each justified from the card:
- `jujutsu-jj-git-compatible-vcs` and `uptime-robot-status-page-webhook-alerter`: usefulness/differentiation;
- `rspack-rust-based-javascript-bundler`, `sage-wordpress-starter-theme-laravel-blade` and `schedule-and-inspect-dotnet-agent-jobs-with-tickerq`: adversarial resilience.

No changed record crossed a disposition boundary. The progress ledger's `grade_20` and the capability index were updated to match.

## Process changes adopted for later tranches

- **Second-pass sweep:** REFERENCE-ONLY records whose notes mention ungated actions, privacy or rights now go through an independent adjudication before publication. This was first used on the 313-package Awesome Copilot tranche.
- **Threshold signal:** the integration owner computes the static threshold signal and does not take it from reviewers.
- **Batch spot checks:** each reviewer batch output is spot-checked for dimension/rationale alignment before integration.
