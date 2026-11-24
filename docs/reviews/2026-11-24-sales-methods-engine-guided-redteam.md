# Sales methods: engine-guided adversarial review and bounded refinement

Date: 2026-11-24
Repository: `Knapp-Kevin/skillz`
Route: explicit `REPOSITORY_MAINTENANCE`
Baseline: merged PR #911, `0891972aae8d3d0a1574d208005175373316ff46`
Targets: `skills/authored/sandler-conversation-strategist/` and
`skills/authored/meddpicc-opportunity-assurance/`, both v0.1.0.
Status of this record at authoring: **candidate review, pre-merge**.

## Existing skill-engine components actually used

This is **not** a new skill compiler, additional Skill Pack or runtime.
The existing procedural contracts were read and applied to these two
complete four-file authored packages:

| Engine component | Actual application |
| --- | --- |
| [Refinement lifecycle](../../engine/refinement/README.md) | Freeze original task result; diagnose consequence; isolate minimal change; challenge adjacent negative and false-green; decide based on evidence; deliver actual merged package |
| [Skill Eval](../../engine/skills/skill-eval/SKILL.md) | Exact original package identity, full source/reference/example/license inspection; static 10-dimension rubric; separate deterministic tests, host behavior, consumer result and security |
| [Skill Audit](../../engine/skills/skill-audit/SKILL.md) | Cross-check independent offline closure, safety/authority/privacy, metadata and registry provenance, stale claims and non-required engine paths |
| [Skill Forge](../../engine/skills/skill-forge/SKILL.md) | Maintainer-authorized edits in existing `skills/authored/<slug>/`, not a new skill or forced builder template; no version bump for internal compatible corrections |
| [Feedback decision tree](../../engine/packs/feedback-decision-tree.md) and [source-blind boundary](../../engine/refinement/feedback-boundary.md) | Both findings target canonical correctness, not seller style or company-level private preferences; no customer data, user preference, external issue text or source identity used to justify changes |
| [Builder acceptance](../../engine/builder/acceptance.md) | Review standalone package closure, positive, non-trigger, missing evidence, authority and false-green; optional design gate/blueprint compiler is **CREATE/COMPOSE-only**, deliberately not applied to an existing refinement |
| [Refinement case checker](../../engine/refinement/check_case.py) | Two **fictional** per-skill JSON receipts are packaged in `docs/reviews/fixtures/` and validated in the existing authored QA job. Structural receipt completion is not a proof of an incident or host behavior |

This respects the passive repository: no independently installed
engine dependency, new service, automatic feedback intake, telemetry,
customer CRM access, scheduler or runtime executor. Consumer preferences
such as shorter agenda wording stay private, never canonicalized.

## Sandler: independent red-team

**Frozen result:** Offer a useful buyer-centered meeting action and
a safe exit, without implying consent or changing the buyer's decision.

**S1 critical source-risk, STATIC_RISK:** The original entrypoint
described ethical conversations and no-fit, but did not provide an
actionable transition from an explicit buyer opt-out to a true
no-contact stop. A seller could frame "please stop contacting us" as
an objection to revisit. It also lacked a precautionary hold for a
seller-recorded opt-out where authentication was temporarily impossible.

**S2 medium procedure gap, STATIC_RISK:** A first meeting and a requested
proposal did not have clear branches for sparse buyer evidence,
unconfirmed value/authority, or mutually agreed follow-up. The
original public seven-stage alignment could still be read as
run-the-entire-framework advice.

**S3 high handoff contract, STATIC_RISK:** The original Sandler
`SELLER_ASSERTED` and `SOURCE_OBSERVED` were not deterministically
translatable to MEDDPICC's `SELLER_INFERRED` and
`DOCUMENT_OBSERVED`, while the instruction said never to promote
evidence. A bare caution was insufficient as an exchange contract.

**Repair:** Add `## Buyer-controlled decision branches` with
`STOP_NO_CONTACT`, `PAUSE_OR_NO_FIT`, `DISCOVER`,
`PROPOSAL_HOLD`, `PROPOSE` and specific stop lines; a usable
short micro-agenda; a conservative do-not-contact hold even
for seller-reported opt-outs; and an explicit source-state
translation table. Put original walkthrough and S11–S14
adversarial cases inside the standalone package.

**Falsifiers:** Opt-out vs a seller quota (no outreach even to verify);
an approved meeting request with no known pain (three directions,
no long script); request for proposal without purchasing authority
(proposal hold); seller-quoted customer note handed to qualification
(never buyer-confirmed); unrelated task (non-trigger); offline
host without CRM (no invented access).

## MEDDPICC: independent red-team

**Frozen result:** Expose complex-deal evidence and the specific
commercial decision a buyer is ready for, without inferring
commitment from sales CRM stage or completed qualification fields.

**M1 high false-green risk, STATIC_RISK:** The existing eight-row
ledger and `REVIEWABLE` classification did not explicitly
differentiate *evidence dossier reviewability* from readiness to
propose, forecast, sign or declare won. A rep could have eight
sourced observations but unresolved legal/security paper process
while presenting the deal as ready to sign.

**M2 high trust gap, STATIC_RISK:** The source-state handoff
was described as preserving provenance, but the two first-party
frameworks used different state names without a concrete translation.
A buyer-controlled document about technical evaluation could
accidentally become funding or signature proof.

**M3 medium decision-procedure gap, STATIC_RISK:** The prior method
listed missing budget/procurement paths but lacked explicit
action-specific HOLD decisions with the **one next buyer-side
confirmation** and credible alternative, preserving the
no-decision option.

**Repair:** Add independently usable action-gate routing for
`DISCOVERY_ONLY`, `PROPOSAL_HOLD`,
`FORECAST_NOT_ESTABLISHED`, `SIGNATURE_HOLD` and
`NOT_WON_OR_NOT_DELIVERED`. Separate
`evidence_review_state` from `requested_action_gate`.
Inherit the existing `ACCESS_HOLD` disclosure precedence,
`CONFLICTED` and `DISCONFIRMED` meanings; translate
only source and claim-specific states from Sandler.
Add an original false-green walkthrough and M13–M17 cases.

**Falsifiers:** Eight green factor boxes but incomplete security
(CONTRACT/SIGNATURE_HOLD); technical approval only (not
buyer economic/paper approval); seller CRM "approved" vs
authenticated finance denial (DISCONFIRMED, not two credible
sources in CONFLICTED); a readable dossier without calibrated
forecast policy (no invented odds); revoked current access
(no cached detail or counts).

## Baseline static red and candidate static green

A direct exact-blob text comparison at the stated merged baseline
found the five new protected decision/mapping anchors for **each**
skill absent. The same anchors were present on the candidate
branch when checked, without upgrading that observation into
a real model-run success. The source-level red/green is
`STATIC_REVIEW`; proposed unit checks are
`LOCAL_TEST` only after executed CI.

The existing fictional shared CASE-JOINT-01 stays unchanged, so
cross-method evidence provenance and revoked-access cases must not
regress. Each package keeps its own S11–S14 or M13–M17
cases *before* that shared case; an existing local test requires
the shared cases remain text-identical between packages.
Neither sibling is a required runtime dependency.

## Bounded acceptance matrix

| Probe | Sandler | MEDDPICC | Evidence class |
| --- | --- | --- | --- |
| Positive | Open, useful meeting prep with buyer agency | Qualified evidence review with requested action specified | Static cases; local text test |
| Near-negative | Buyer asks no contact: STOP, no consent inference | Buyer technical evaluation: not paper process | Static cases; local text test |
| Missing input | No authenticated buyer source: provisional only | No calibrated forecast policy: FORECAST_NOT_ESTABLISHED | Static cases |
| Authority / privacy | No contacted lead, no CRM write, no opt-out verification via outreach | No source leak on ACCESS_HOLD or false customer forecast | Static source review |
| False-green | Pretty talk track that continues after opt-out is wrong | Eight checked boxes while contract cannot sign is wrong | Static source review |
| Preservation | Seven public stages, original wording, Sandler non-affiliation, separate ROI baseline | Eight factors, explicit conflict precedence, no auto probability | Existing QA + static source review |
| Interoperability | SELLER_ASSERTED → SELLER_INFERRED, claim-scoped BUYER_CONFIRMED | Identical mapping, no source promotion or replay | Source-text contract, not runtime |

The receipts at
`fixtures/2026-11-24-sandler-conversation-strategist-refinement-case.json`
and
`fixtures/2026-11-24-meddpicc-opportunity-assurance-refinement-case.json`
carry `STATIC_RISK` and pre-merge `ITERATE/UNMERGED`
truthfully. They are **fictional, first-party source-bound maintainer
case receipts**, *not* source-blind consumer feedback signals or actual
buyer incident reports. Their public first-party skill slugs and
repository source pins are allowed **only in this maintainer evidence
plane**; they carry no private consumer identity, raw report,
sales interaction or user preference. The separate source-blind
`engine/refinement/feedback_intake.py` route is NOT invoked or
replaced. The common checker cannot prove source authenticity,
severity, licensing or outcome.

## Rubric and qualification boundaries

Both skills were previously assigned a **historical author-led
19/20 static candidate** on their prior package trees.
These content changes require fresh source identity and review;
do not inherit that rating or promote it to formal `verified`.
The repo-wide authored QA currently enforces
`needs-re-review` for both packages. Independent host
validation, customer outcomes, prospective sales uplift and
security scanning are separate and remain `NOT_RUN`
unless separately evidenced.

Target: no substantive regression on the existing skill-specific
checks, newly differentiated adversarial and false-green source
checks, both engine refinement-case structural validations, exact
two-package blob/tree provenance, clean GitHub exact-HEAD reviewer
feedback, and an **actually merged** PR. A clean source review
does not certify Sandler licensing/training or mathematical deal odds.

**Stop rule:** After the targeted defects are repaired and no
new decision-changing flaw is found, stop rather than inventing
an orchestration pack, a third skill or a SemVer increment.
