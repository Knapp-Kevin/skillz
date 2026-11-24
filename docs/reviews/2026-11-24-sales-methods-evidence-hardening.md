# Sales methodology skill refinement: evidence provenance and paired red-team trial

Date: 2026-11-24
Owner: Skillz first-party authored corpus
Targets: `sandler-conversation-strategist` and
`meddpicc-opportunity-assurance`, both v0.1.0. Starting review and
registry source identity: merged PR #910, commit
`f3e0abc067afe0f6de39a51cb89ee59095f7f180`.
Result: **author-led adversarial refinement**, not agent-host validation.

## Existing outcome and differentiation

Sandler-aligned Conversation Strategist should lead to better
**mutual, buyer-autonomous conversations** without pretending buyer claims
were authenticated by the caller. MEDDPICC Opportunity Assurance should
expose buyer-side evidence gaps and blockers before a seller forecast
or close plan is trusted. Both remain original, independently usable
portable text packages; a conversation is not a completed deal check.

Current public [Sandler seven-stage overview](https://sandler.com/sandler-selling-system/)
and [MEDDPICC public methodology overview](https://meddicc.com/meddpicc-sales-methodology-and-process)
continue to support their intentionally different scopes. No new vendor
course text, copyrighted templates, training scripts or proprietary assets
were copied into this revision. Do not claim official affiliation,
certification or legal adjudication of a framework name.

## Red-team VETO: reproduced static contract gaps

1. **RT-S1, provenance / evidence:** Sandler labeled buyer statements
   as buyer-confirmed while the underlying source might be seller-written
   notes, an uninspected transcript or a pasted quote. Transferring the
   claim to MEDDPICC risked **provenance laundering**.
2. **RT-M1, state contract:** MEDDPICC asked reviewers to mark
   `CONFLICTED` for contradictory buyer evidence, but its enumerated
   states omitted that state. `DISCONFIRMED` also needed separation:
   a current buyer denial does not have the same evidentiary standing
   as the seller's stale optimistic forecast.
3. **RT-R1, dimensional correctness:** The optional Sandler training
   value worksheet defined a period `t` but its benefit formula
   used a generic baseline `B` with unknown units and compared it
   to fee/cost amounts. This could produce fake dollar ROI from leads,
   attendees or hours and double-count adoption.
4. **RT-C1, combined behavior:** Existing independent fictional
   scenarios did not force a common opportunity's evidence state
   to survive a Sandler→MEDDPICC handoff, current buyer denial and
   a later access revocation.

Qortara Logic's hosted verdict parser interpreted the above
**caller-authored** report as VETO, then an independently drafted
repair plan as PASS. This validates verdict text under hosted rules;
the service did **not** inspect these files, run a skill, authenticate
a source or conduct an independent red-team attack. This report is
therefore an author-led static evaluation.

## Repair architecture

- **Sandler:** Add a provenance gate distinguishing
  `SELLER_ASSERTED`, `SOURCE_OBSERVED`, `BUYER_CONFIRMED`,
  `SIMULATED`, `DISCONFIRMED`, `CONFLICTED` and privacy
  `ACCESS_HOLD`. Buyer-confirmed must name an actual currently
  permissioned source/interaction and its narrow claim. CRM field
  or seller-pasted quote never proves buyer acceptance.
- **MEDDPICC:** Define all eight ledger states and explicit
  contradiction precedence: denied permission blocks details;
  conflicting authenticated buyer sources remain CONFLICTED;
  current buyer refutation of a seller-only claim is DISCONFIRMED;
  stale facts are not refreshed by rewriting the CRM; unknown
  and seller-inferred claims stay provisional. No close percentage.
- **Value model:** Require one common period and monetary eligible
  revenue `R_t`, fractional attributable uplift `u`, incremental
  contribution margin `m`, adoption `a` **only when not already
  included**, and same-period fees `F_t` and costs `C_t`.
  `benefit_t = R_t × u × m × a` and
  `net_t = benefit_t - F_t - C_t` are **hypotheses**, not
  realized gains or proof of causality. If a lead or conversion-rate
  percentage point is supplied instead of monetary revenue,
  abstain from a dollar calculation without a compatible model.
- **Both:** Bundle the identical, original
  `CASE-JOINT-01` exercise within each standalone
  `examples/acceptance.md`, so neither package requires its sibling.
  The fixture progresses from seller-only claims (T0), a
  permissioned fictional buyer document (T1), a buyer denial
  versus equally credible buyer-source contradiction (T2a/T2b),
  and current viewer revocation (T3).
  Expected outputs are documented for both skills. A user who
  wants only conversation coaching must not be forced to run
  complex qualification or a spreadsheet.

## Evidence matrix and acceptance

| Case | Sandler expected | MEDDPICC expected |
| --- | --- | --- |
| T0: $500k hypothetical, $65k alleged budget, pasted "buyer said" | Discuss actual pain and mutual agenda, no verified benefit or buying authority | Metrics, economic approval, champion and paper claims unproven; no numeric probability |
| T1: authenticated fictional buyer doc says only exploring, no measured baseline, no funding decision, procurement not started | Explore business problem and priority, preserve the explicit buyer uncertainty | Refute seller funding assumption, with missing baseline and paper process; no automatic champion |
| T2a: buyer finance denies, seller CRM still says funded | Treat seller claim as DISCONFIRMED; permit pause/no-sale | DISCONFIRMED, not CONFLICTED; do not upgrade forecast |
| T2b: two current credible buyer-owned sources conflict | Seek reconciliation, do not select optimistic conclusion | CONFLICTED and readiness hold |
| T3: current authorization revoked | ACCESS_HOLD, no cached private details/counts | ACCESS_HOLD without material factor disclosure or cache replay |

The test in `scripts/qa/test_sales_methodology_contract.py`
checks the shared scenario remains identical in both standalone
packages, source/permission state vocabulary, and period-bound
finance formula. These tests are **deterministic text/fixture checks**,
not observed model responses or real CRM/host actions.

## Release evidence and remaining risks

Both packages retain 4 files and v0.1.0, without a daemon,
connector, CRM access, outbound messages, scheduled tasks or
private user data. Preserve source Git blob SHA and complete-package
tree SHA in all three registry records for each package. Keep
`review_status: needs-re-review`, `verification_status:
needs-re-review` and `behavioral_validation: not-run`
under current repository gates. Prior 19/20 ratings are
**historical author-led static candidates bound to prior source**.
No automatic score increase is warranted from passing text checks.

The next distinct evidence gate, not a requirement for this
bounded static-hardening PR, is an actual independently hosted
consuming-agent trial with recorded exact packages, available
tools, fictional input packets, observed outputs, negative controls
and reviewer signoff. Real-world sales benefit remains unmeasured.

## Qualification before merge

- Full existing authored feedback and the amended sales-method
  offline tests pass at exact PR head.
- Git blob/tree registry companions match both changed packages.
- Review scope and current-head independent GitHub code review
  are recorded, and material reviewer findings resolved.
- PR is actually merged and main source identity verified.

This review does not authorize source reads, vendor use,
training purchases, contact outreach or a new scheduled agent.
