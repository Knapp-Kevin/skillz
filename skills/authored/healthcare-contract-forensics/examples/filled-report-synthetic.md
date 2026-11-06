# Worked report: fictional PBM contract (HCF-SYN-01)

**DEMONSTRATION ONLY.** Every contract, claimant identifier and figure in this report is fictional. This is a *human-authored worked example* of the intended output, not evidence that an LLM host ran the skill or that actual money can be recovered.

## Review identity, authority and limitations

- **Review date:** 2026-11-06. **Reviewer role:** simulated employer-side plan sponsor.
- **Scope/permission:** only files `synthetic-pbm-case.md` and `claims-synthetic.csv` in this package. No external systems, healthcare records, vendors, private files, tools or accounts accessed.
- **Plan and measurement period:** fictional U.S. self-insured employer plan, Q1 2025 rebates; March 2025 settled claims.
- **Documents:** `C-01` master agreement (signed Dec. 15, 2024, effective Jan. 1, 2025); `S-01` Schedule A (same signing/effective dates); `A-01` signed Feb. 15, 2025, effective Mar. 1, 2025; `I-01` invoice issued Apr. 10, 2025; `R-01` manufacturer ledger delivered May 12, 2025; `D-01` CSV rows 1–4.
- **Completeness:** provided materials are legible and complete for the exercise, but independent bank settlements, full affiliate invoices, credits outside the provided invoice, and claim adjudication evidence are absent.
- **Privacy handling:** invented identifiers only; no real PHI, personal data or confidential contract used. No outbound disclosure.
- **Excluded:** legal conclusions, regulatory compliance verdicts, vendor motives, collection/offset rights, claim-by-claim pharmacy-network guarantees, and actual savings.

## Executive take

The fictional March invoice lists $7.25 in administration fees when the provided contract and three settled claims support an expected $6.00, creating a **+$1.25 arithmetic variance** requiring invoice verification. The PBM reports $20 in manufacturer service fees excluded from the agreement's defined rebates, so the issue is **transparency and negotiation**, not a proven failure to remit defined rebates. The $50 difference between plan charges and pharmacy payments is permitted by the provided agreement, so it is **not a proven overpayment or theft**. The amendment adds access to annual aggregate manufacturer-fee summaries but does not require delivery of raw affiliate invoices. The sponsor should request billing detail, applicable credit memos, independent settlement records and the newly available annual report before deciding on legal or financial action.

## Clause-by-clause scrutiny for negotiation

The following quotes are **short, directly checked excerpts from the fictional input text** in `synthetic-pbm-case.md`. In a real engagement they belong in an authorized private report, not an automatically public post. This is a worked demonstration, not an observed model-host result.

**Open the original fictional evidence:** [contract, amendments, invoice and ledger](synthetic-pbm-case.md) (C-01, S-01, A-01, I-01, R-01) and [claims CSV](claims-synthetic.csv) (D-01). The section and row citations in the cards below point into these two source files.

### HCF-001: Settled-claim administration fee (medium)

- **Original wording:** “$2.00 per settled paid prescription claim” and “excluding reversed or rejected claims” — **C-01 §4.1**, effective 2025-01-01. **S-01 §A.1** confirms $2.00 and **A-01 §A1.2**, effective 2025-03-01, says “No change to the §4.1/S-01 administration-fee rate” **I-01 line 1** shows $7.25.
- **Why scrutinize:** The formula only charges for settled claims. A reversed claim must not enter the denominator, and the later amendment does not change the rate.
- **Financial impact:** **VERIFIED ARITHMETIC on supplied synthetic records, March 2025 USD only.** **3 × $2.00 = $6.00** from **D-01 rows 1–3** (exclude reversed row 4); **$7.25 − $6.00 = +$1.25** invoice variance. **Not established owed back or recoverable** until claims counts, credits and true-ups are verified. No extrapolation or annual savings estimate.
- **Verify:** Sponsor billing analyst requests March settled-claim IDs, credit memos, exclusions and final paid-claim denominator.
- **Negotiation question:** Can the PBM supply an auditable per-claim calculation and a defined credit/true-up process for charges inconsistent with §4.1?

### HCF-002: What “100%” rebate pass-through actually includes (medium)

- **Original wording:** “100% of Rebates” — **C-01 §2.1**; but “Rebates exclude separate administrative, data, consulting and service fees paid to PBM or affiliates” — **C-01 §1.1**, both effective 2025-01-01. **A-01 §A1.2** retains those definitions. **R-01 lines 1–3** report the credits and fees.
- **Why scrutinize:** The broad-sounding percentage is narrowed by a defined-term exclusion. The arrangement may align with the contract but leaves a commercial incentive and disclosure question.
- **Financial impact:** **NOT QUANTIFIED as economic harm.** R-01 and D-01 report **$50 defined rebates credited** and **$20 separate manufacturer administration/service fees** for the illustrative Q1 2025 period. The $20 is an **observed category**, not a contractual rebate shortfall or a proven $20 recovery.
- **Verify:** Benefits lead seeks remittance evidence, manufacturer fee classifications, all applicable amendments and the annual aggregate report permitted under A-01 §A1.1.
- **Negotiation question:** Could the rebate definition or reporting obligation expressly cover all manufacturer-related compensation, including affiliate service/data fees, with exceptions disclosed and priced?

### HCF-003: Sponsor charges versus pharmacy reimbursements (low)

- **Original wording:** “the PBM may retain the difference” — **C-01 §3.2**, effective 2025-01-01, referring to differences between sponsor charges and amounts paid to pharmacies.
- **Why scrutinize:** The two amounts need not be identical under this agreement. Understanding how those prices are calculated can matter in negotiations even without a breach.
- **Financial impact:** **VERIFIED ARITHMETIC of a difference, NOT QUANTIFIED as loss.** D-01 rows 1–3 show **$360 sponsor charges − $310 pharmacy payments = $50** in March 2025 USD. The contract expressly allows a difference; **$50 is neither verified overpayment nor recoverable savings**.
- **Verify:** Benefits procurement requests matched claim-level price components, applicable guarantees, netting adjustments and true-up evidence.
- **Negotiation question:** Would a transparent pricing schedule with separately disclosed PBM compensation and an independently auditable claim reconciliation be acceptable?

### HCF-004: Limits on manufacturer-fee audit access (medium)

- **Original wording:** “Raw affiliate manufacturer-service invoices are not expressly provided under this section.” — **C-01 §5.3**, effective 2025-01-01. **A-01 §A1.1**, effective 2025-03-01, adds “annual aggregate summaries” of certain manufacturer payments, not the underlying invoices.
- **Why scrutinize:** Annual summaries provide some visibility, but the records available may not let the sponsor independently test all related-party remuneration. The amendment improves access; it must not be overlooked.
- **Financial impact:** **NOT QUANTIFIED.** No reliable amount of avoidable cost follows from this access limitation alone. The known $20 manufacturer-fee category is not automatically an audit loss.
- **Verify:** Sponsor fiduciary and counsel request the available annual summary, data definitions and a specific description of the records omitted from audit access.
- **Negotiation question:** Can the parties agree on independent third-party verification of affiliate compensation and a defined process to resolve discrepancies without unnecessary disclosure of other clients' data?

## Findings register

| ID | Priority | Status | Exact source(s) and observation | Counter-reading / evidence against | Monetary value status | Confidence in bounded finding | Verification owner |
|---|---|---|---|---|---|---|---|
| HCF-001 | Medium | **CONFIRMED ARITHMETIC VARIANCE** | `C-01 §4.1`, `S-01 §A.1` and `A-01 §A1.2` set $2.00 per settled paid claim; `D-01` rows 1–3 settled, row 4 reversed; `I-01` line 1 bills $7.25 | Off-invoice credits or authoritative later counts could change interpretation | **$1.25 calculated variance**, **not** established recoverable amount | High for arithmetic only | Sponsor billing analyst |
| HCF-002 | Medium | **POTENTIAL ECONOMIC RISK** | `C-01 §§1.1, 2.1`, `R-01` lines 1–4: $50 defined rebates credited; $20 manufacturer service/admin fees excluded and not credited | The written defined rebate term explicitly excludes those fees; no shown violation of 100% **defined** rebate credits | **$20 observed as separate category**, **NOT quantified as owed or savings** | High for definition, low for total economic loss | Benefits lead + counsel |
| HCF-003 | Low | **POTENTIAL ECONOMIC RISK** | `C-01 §3.2`; `D-01` rows 1–3: sponsor charge $360 vs pharmacy reimbursement $310 | Contract expressly permits different amounts; no contract guarantee breached by difference alone | **$50 observed difference**, **NOT quantified as overpayment** | High for arithmetic, low for avoidable cost | Benefits procurement |
| HCF-004 | Medium | **POTENTIAL ECONOMIC RISK** | `C-01 §§5.3, 7.1`, `A-01 §A1.1`: annual aggregate reporting added; raw affiliate manufacturer invoices remain outside express access | Amendment improves access relative to master, so “no report available” would be inaccurate | Not quantified | High for stated contractual access, uncertain for other legal rights | Sponsor fiduciary + counsel |
| HCF-005 | Medium | **DOCUMENT GAP** | `R-01` final note, `I-01` line 2: no independent settlement record, raw affiliate invoices or external credits provided | Absence from supplied documents is not proof records do not exist | Not quantified | High that materials are missing from this review | Sponsor data custodian |

## Reconciliation workpaper (fictional USD)

| Workpaper | Governing formula and version | Included / excluded data | Expected | Observed | Difference | Scope limit |
|---|---|---|---:|---:|---:|---|
| F-01 administration | `C-01 §4.1` and `S-01 §A.1`, unchanged by `A-01 §A1.2`: **3 × $2.00** | `D-01` rows 1–3 counted; row 4 **REVERSED** excluded | $6.00 | `I-01` line 1 $7.25 | **+$1.25** | Billing variance only, pending all credits and authoritative settled-count check |
| F-02 price difference | `C-01 §3.2`: not a pass-through guarantee | `D-01` rows 1–3: ($120+$200+$40) - ($96+$176+$38) | $360.00 sponsor charges | $310.00 pharmacy payments | **$50.00 observed difference** | Explicitly permitted by supplied master; not a recoverable amount |
| F-03 defined rebates | `C-01 §§1.1–2.1`: 100% of **defined** Rebates | `D-01` rows 1–3: $20+$30+$0 | $50.00 defined rebates | `R-01` $50.00 reported credit | **$0.00 observed undercredit** | Ledger not independently bank-verified; $20 service fees excluded by definition |

## Priority evidence requests

1. A March paid-claim settlement count with duplicate, reversal and reprocessing reconciliation, plus the invoice detail and any credit memos or cross-period true-ups.
2. Rebate remittance evidence for the reported $50 credit, manufacturer payment classification and the `A-01 §A1.1` annual aggregate service/admin-fee summary.
3. Confirmation of reporting and audit access for affiliated entities, the precise included versus excluded compensation categories, and contract precedence for future amendments.

## Negotiation questions for counsel/vendor discussion

- Would the sponsor prefer a broader pass-through definition covering manufacturer service and administrative remuneration, with exceptions explicitly priced?
- Can audit rights extend to independently test aggregate fees and related-party compensation without exposing unrelated third-party confidential records?
- Can pricing transparency and fully matched sponsor-versus-pharmacy charges be provided at a mutually acceptable level without publishing PHI?

## Completion receipt

**PARTIALLY REVIEWED.** Source-linked descriptive analysis and arithmetic are complete for the synthetic example. Real payments, rights to a refund, full source documents, legal compliance and any production/agent-host behavior remain **not verified**. No private content was accessed and no external tool, message or claim was sent.
