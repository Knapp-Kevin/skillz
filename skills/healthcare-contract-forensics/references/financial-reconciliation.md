# Reconciliation and calculation protocol

**Never silently infer amounts, denominator or legal consequence from arithmetic.** Keep source row IDs and the effective pricing formula together. Any example data below is fictional and only illustrates process.

## Admissibility preflight

1. Scope each dataset to the **same** plan, claim service window, adjudication status, currency, claim basis, version and counterparties. Require source provenance and authorized data minimization.
2. Normalize units: \`per paid claim\`, \`per member per month\`, \`gross amount\`, \`ingredient cost\`, \`rebate received\`, \`reversal\`, \`tax\`. Never substitute one for another.
3. Inspect duplicates, reversals, reprocessed/rejected claims, negative amounts, missing timestamps, varying price basis, and adjustments. Record excluded rows and why.
4. Use decimal/currency-safe math when available. Never use LLM mental arithmetic for high-stakes totals. If no reliable calculation capability exists, show an unexecuted formula and mark **NOT CALCULATED**.
5. Reconcile rounding by the **contractual rule** if present, otherwise disclose the rounding assumption without treating pennies as confirmed discrepancies.

## Basic formulas and distinctions

**Fixed administrative fee example:**

\`expected_fee = qualifying_paid_claim_count × contract_fee_per_claim\`

\`arithmetic_variance = invoiced_fee - expected_fee\`

A positive variance is a **candidate billing discrepancy**, not a recoverable amount, until credit memos, exception fees, overrides, plan/period scope and invoicing terms are checked.

**Pricing spread observation:**

\`observed_difference = sponsor_plan_charge - pharmacy_payment\`

Only label it \`observed difference\`. To establish a spread claim, require matching claim basis, netting adjustments, and contract definitions. Do **not** sum observed differences as "money stolen" or savings. When only one side of this equation exists, the spread is unknown.

**Retained manufacturer payment observation:**

\`potentially_retained_manufacturer_compensation = eligible_manufacturer_payment - verified_plan_credit\`

Not every manufacturer payment is a defined \`rebate\`. Eligibility and pass-through obligations must be adjudicated *per agreement term*; otherwise this is an evidence request, not an overpayment.

**Rebate guarantee:**

Use the actual contractual rate/denominator, exclusions, measurement interval and true-up language. Do not apply a rebate percentage to an arbitrary gross drug cost. Missing settlement data -> no verified variance.

**Economic sensitivity**, not recovery:

A scenario \`assumed_fee_delta × eligible_volume\` may be used **only** when both inputs and their basis are explicit; label \`MODELED SCENARIO, NOT SAVINGS\`. Distinguish measured volume from forecast volume. No market rate from memory.

## Working-paper evidence table

| Row | Contract source (section/period) | Financial source (file/row) | Formula and exclusion logic | Expected | Observed | Variance | Status |
|---|---|---|---|---:|---:|---:|---|
| F-01 | C-01 §4.1 / 2025-Q1 | D-02 rows 1–3; I-01 line 1 | 3 paid claims × $2 | $6.00 | $7.25 | +$1.25 | Arithmetic only; credits to check |

The example row above belongs to the synthetic fixture in \`../examples/\`, not real-world evidence. Summaries must reproduce the calculation and cite every input.

## Stop conditions

Stop affected calculations on unverified claim identity alignment, mismatched date/basis, unknown treatment of reversed claims, unresolved units, missing price schedule, unreliable OCR of monetary values, unavailable deterministic arithmetic tools, or sensitive-data authority uncertainty. Continue contractual observations with the correct incomplete status.
