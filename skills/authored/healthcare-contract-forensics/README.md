# Healthcare Contract Forensics

**An MIT-licensed, evidence-first AI skill for reviewing employer health-plan and pharmacy benefit manager (PBM) agreements.**

The goal is to turn an opaque contract into **specific clauses to question, transparent calculations, and evidence-backed discussion points** for the team responsible for reviewing or negotiating it. This is contract review support, not an accusation, legal opinion, or savings guarantee.

## What a useful finding looks like

For each significant finding, the skill is instructed to show the **actual wording, source location, financial implication, competing explanation, what to verify, and what to ask in negotiations**.

**Example from the included fictional agreement:**

| Review element | Synthetic demonstration |
|---|---|
| **Original clause** | C-01 §4.1: “$2.00 per settled paid prescription claim” and “excluding reversed or rejected claims” |
| **Why it matters** | Reversed claims should not be included when calculating the fee. A-01 §A1.2 does not change that rate. |
| **Financial impact** | March 2025: 3 settled claims × $2.00 = **$6.00** expected; invoice I-01 line 1 lists **$7.25**, giving a **+$1.25 arithmetic variance**. **Not a proven refund or savings amount.** |
| **Evidence to request** | Actual settled-claim count, adjustments, credit memos and fee calculation detail. |
| **Negotiation question** | Can the PBM provide an auditable per-claim calculation and a contractual credit/true-up process? |

This example is **entirely fictional**. The supplied [worked report](examples/filled-report-synthetic.md) also distinguishes $20 in manufacturer service fees excluded from defined rebates and a $50 allowed sponsor/pharmacy price difference. Neither amount is automatically money owed back.

## How to use this package

1. **Get the whole folder**, not just `SKILL.md`. It includes [the skill instructions](SKILL.md), references, a fictional contract and claim data, a filled report and evaluation scenarios.
2. In an agent host that supports portable skills or project instructions, load this skill and give it **only the exact materials you are authorized to review**. Host permissions and data handling requirements still apply.
3. Request a report with the controlling agreement versions, **short verified clause excerpts linked to their source**, a bounded financial workpaper, counter-readings, evidence requests and negotiation questions.
4. **Start with the synthetic files**: [fictional PBM contract](examples/synthetic-pbm-case.md) and [synthetic claims CSV](examples/claims-synthetic.csv). Compare the output to the [expected case](examples/expected-case-review.md) and [completed example report](examples/filled-report-synthetic.md).

**Suggested prompt for the fictional example:**

> Use Healthcare Contract Forensics to review only the attached fictional PBM agreement and claims CSV. Identify which exact clauses deserve scrutiny, quote only short verified excerpts with document/section citations, explain financial amounts and their limits, and provide specific verification and negotiation questions. Do not claim fraud, unlawful pricing or recoverable savings without supporting evidence.

## What's inside

- [`SKILL.md`](SKILL.md): scope, triggers, privacy/authority rules and audit workflow
- [`references/`](references/): clause analysis, reconciliation method and report requirements
- [`examples/synthetic-pbm-case.md`](examples/synthetic-pbm-case.md) and [claims CSV](examples/claims-synthetic.csv): invented agreement and data
- [`examples/filled-report-synthetic.md`](examples/filled-report-synthetic.md): four quote-backed clause scrutiny cards and a reproducible workpaper
- [`examples/negative-scenarios.md`](examples/negative-scenarios.md): controlled adversarial and missing-evidence cases

## Trust, privacy and status

- **Version:** 1.1.0. **License:** [MIT](../../../LICENSE), for original first-party content.
- **Status:** statically reviewed; **external agent-host behavior and improvement over a one-line prompt have not been validated**. This is reference-only and **not production-qualified** for confidential healthcare documents.
- **Data:** Do not put identifiable member claims, confidential contract material or PHI into an unapproved host. The skill is read-only by default and does not send files or contact vendors.
- **Decision boundary:** A suspicious-looking financial arrangement may be expressly permitted by its signed contract. Observed differences are not necessarily breaches, recoverable overpayments or savings. Significant decisions require qualified legal/plan review.

[Original issue and qualification tracker](https://github.com/Knapp-Kevin/skillz/issues/714) · [Full package static review](../../../docs/reviews/2026-11-06-issue714-healthcare-contract-forensics-static-review.md)
