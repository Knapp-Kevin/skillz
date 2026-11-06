# Healthcare Contract Forensics: LinkedIn commenter acceptance audit

**2026-11-06 | Package v1.1.0 | Scope: original MIT-authored passive skill and fictional fixture only.**

## Requirement being tested

A commenter wanted the AI to **identify exact clauses that deserve scrutiny**, **explain their financial impact**, **point back to the original wording**, and give a team evidence to check and raise in negotiations. The skill was already strong on numerical caution and source IDs, but the v1.0.0 report contract did not require the *actual clause text* alongside each finding, and its worked report paraphrased instead of showing it. That was a real presentation/traceability gap.

This update is a **source/package implementation and static acceptance review**, not a claim that an agent host successfully followed the instructions. No real healthcare agreements, protected records, vendor systems, or PHI were accessed.

## Acceptance evidence

| Requirement | Implemented v1.1.0 source behavior | Static check result |
|---|---|---|
| Which clauses to question? | `SKILL.md` step 7 requires source ID, document name/effective version, precise page/section/row and top-priority clause scrutiny cards | **PASS:** Four worked cards, HCF-001 through HCF-004, match the cited fictional agreement sections |
| Show original wording and take reader back? | Each card quotes short **verbatim** text, separates that text from the reviewer's interpretation and requests an access-controlled original file/page link when available | **PASS:** **8/8** quoted excerpts in the four cards match the actual fictional agreement after normalizing Markdown emphasis. The worked report links to `synthetic-pbm-case.md` and `claims-synthetic.csv` for direct inspection |
| Explain the financial consequence? | Each card states bounded unit, period, formula/data rows or `NOT QUANTIFIED`, with an explicit distinction between observed amounts and legally recoverable money | **PASS:** Three settled claims × $2.00 = **$6.00** vs $7.25 invoice = **+$1.25** arithmetic; $360 plan charges minus $310 pharmacy payments = **$50 observed difference**; $50 defined rebates credited; $20 manufacturer service fees excluded from the defined rebate term. **None is represented as proven recoverable savings** |
| Concrete negotiation preparation? | Each card requires an **explanation**, **counter-reading**, **specific evidence request and owner**, plus **one non-accusatory negotiation question** | **PASS:** 4/4 populated cards include all requested fields |
| Safe handling of incomplete originals? | `QUOTE UNVERIFIED` required for unreadable, missing or unverified source wording, and the affected numerical result is bounded or blocked | **PASS as written instructions only.** Execution of missing-source and OCR scenarios by an independent model host is still **NOT RUN** |
| Useful shared GitHub folder? | A new root-of-package `README.md` explains the value, shows the clause-to-financial-impact example, links all parts and makes trial use with synthetic data possible | **PASS as content**, not evaluated on external users |

### Exact source and numerical test receipt

- Exact current `SKILL.md` Git blob: `5a304a552678ad88f4fa239abf28fe52b20bbab6`.
- Complete **10-file** standalone package Git tree: `587d29e9a1275efcb8f20437bbc5479d36d1f5b3`.
- Four quote-backed worked cards, **3 + 2 + 1 + 2 = 8 exact excerpts**. One mismatched terminal period in an original draft excerpt was detected and corrected **before** this version was pinned; no unmatched excerpts remain in the static inspection.
- Source quote inspection strips Markdown styling markers (`*` and backticks) but does **not** paraphrase or substitute text; exact underlying words match the fictional master and amendment.
- Financial calculation uses exact cents on three `SETTLED` rows, excludes one `REVERSED` row; no annual extrapolation or unsupported recoverable-amount claim.
- Source access is read-only. `examples/synthetic-pbm-case.md` includes a malicious quoted note; no instructions from that note are adopted in the package.
- The changed output contract is versioned **1.1.0** for the new report capability. The retained `19/20` score is only a static ten-axis semantic review, **not** a measured end-to-end score or independent user evaluation.

## Explicit qualification boundary

**Static acceptance: PASS for implementing the commenter-facing requirements in the package instructions, worked example and shareable README.**

**Real-model acceptance: NOT TESTED.** It remains unknown whether a particular model/host will reliably quote exact terms, navigate original files, follow effective amendments, do decimal arithmetic, refuse document injections or avoid overstating savings. An authorized controlled run should record host/model/version, exact file pins, full synthetic input/output, source-quote exact-match rate, source-location precision, calculation correctness, verification-question coverage, forbidden actions, and matched baseline comparison.

**Production use: NOT QUALIFIED.** Confidential agreement processing, PHI/privacy handling, legal interpretations and any negotiation decisions require separate authority and human checks. This follow-up does not close issue #714's independent behavioral, legal-source or corpus-dashboard workstreams.

[Package](../../skills/authored/healthcare-contract-forensics/) · [Updated exact-package review](2026-11-06-issue714-healthcare-contract-forensics-static-review.md) · [Open qualification tracker #714](https://github.com/Knapp-Kevin/skillz/issues/714).
