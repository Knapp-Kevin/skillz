# Q1–Q5 source-vetting reconciliation (2026-11-03)

**Result:** 5,508 terminal static candidate decisions in two *disjoint reported source-vetting frontiers*. Of these, 1,609 are `REFERENCE-ONLY` and 3,899 are `REJECT` for unchanged use. **None of these are automatic positive endorsements or governed approvals.**

This corrects a previously published Q5 arithmetic error: the 150 Q5 ledger records are **92 reference-only, 57 rejected, one deferred**, rather than 96/53/1. The detailed original [Q5 report](2026-11-03-q5-six-new-source-families-static.md) and all six per-family macro counts already agree with 92/57/1; the [Q5 invariant audit](2026-11-02-q5-150-exact-tree-invariant-audit.md) had a mistaken total row. No individual grade or disposition was changed.

| Frontier | Review records | Terminal static decisions | Reference only | Rejected | Deferred |
|---|---:|---:|---:|---:|---:|
| Four original pinned sources | 4,813 raw paths | 4,809 | 1,205 | 3,604 | 3 (plus one excluded non-skill template) |
| Q1–Q4, 19 new source families | 550 | 550 | 312 | 238 | 0 |
| Q5, six more source families | 150 | 149 | 92 | 57 | 1 |
| **Combined terminal decisions** | **5,513 path/record occurrences** | **5,508** | **1,609** | **3,899** | **4 deferred across both frontiers (plus excluded template)** |

The combined raw count is not a distinct-package count. Four-source has 4,813 observed raw paths, including 4 without terminal decisions; Q1–Q5 adds 700 individually reviewed records, of which one is deferred.

## Checked evidence

- Reparsed **all 150 Q5 records** across six pinned ledgers: each has ten numeric rubric grades totaling `score_20`, ten keyed rationales, 40-character skill/blob and package/tree SHA values, and explicit security and behavioral `not-run` states. **Zero failures** under these checks.
- Reparsed all four Q1–Q4 capability-routing files: **113 + 127 + 151 + 159 = 550** records (312 reference-only / 238 rejected) from **19** canonical source repo/pin identities.
- Compared source repo/pin identities and recorded package-tree SHA sets: Q5 brings **six other source families** with no source/pin or recorded package-tree overlaps with Q1–Q4. In those **25 Q1–Q5 families alone**, 700 path decisions map to **694 different recorded package-tree SHA values**. Q5 contributes six extra path exposures in three City-Syntax collision groups, retained as independent context/provenance.
- The four-source frontiers are separately reported by source and not summed into a unique eligible skill count. We **did not** check package-tree equivalence between every four-source path, Q1–Q5, and 1,039 governed review companions; the global denominator remains **unknown**.

**Rights and safety:** Several Q5 packages have license-attribution ambiguity, credentials/egress, automatic consequential writes or unreviewed dependencies. No package was executed; security/behavioral `not-run`; no authorizations assumed. Source rights remain bound to their original package files.

**Consumer catalog:** The number of *Recommended for Use* and genuinely *Valuable Reference* skills is still **unknown**. A static `REFERENCE-ONLY` outcome is research material, not a promotion. Consumer-facing positive recommendations require a separate, individual-value judgment and accurate license, safety, and behavior disclosures.

**Machine-readable source/identity receipts:** [Q1–Q5 reconciliation](../../registry/discovery/q1-q5-terminal-decision-reconciliation-20261103.json), [Q5 recorded tree audit](2026-11-02-q5-150-exact-tree-invariant-audit.md), [Q5 full record summary](2026-11-03-q5-six-new-source-families-static.md).

**Publication:** This reconciliation is a review/accounting update, not a new source admission. The five public surfaces must be updated together using these exact counts. Previous Q4 counters remain accessible as dated historical evidence.
