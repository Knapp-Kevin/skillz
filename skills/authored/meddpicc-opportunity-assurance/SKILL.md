---
name: meddpicc-opportunity-assurance
description: >-
  Independently authored advanced MEDDPICC-aligned B2B deal evidence review,
  qualification, stakeholder and purchasing-process mapping, disconfirmation,
  forecast honesty and manager coaching. Use to assess complex opportunities
  against eight public factors without inventing win likelihood or CRM access.
metadata:
  author: Skillz Maintainers
  category: Sales & Go-to-Market
  display-name: MEDDPICC Opportunity Assurance
  version: 0.2.0
  license: MIT
---

# MEDDPICC Opportunity Assurance

A portable **independent** evidence-assurance skill for complex B2B buying decisions, informed by the public MEDDPICC methodology. No affiliation, license, endorsement or certification from MEDDICC training vendors, MEDDIC Academy or other trademark claimants is implied. This is **original** field-review guidance, not a copy of anyone's curriculum or proprietary deal template. Public methodology background: https://meddicc.com/meddpicc-sales-methodology-and-process . The source is context, not a runtime dependency.

## Activate only for the appropriate decision

**Use** for MEDDPICC qualification review, enterprise deal-risk audit, opportunity handoff, multi-stakeholder mapping, CRM evidence quality, leadership deal inspection, value-case testing, forecasting assumption challenge, or preparing a buyer-verifiable close plan.

**Do not** replace simple prospecting or conversation coaching with an enterprise qualification checklist; do not infer a purchase from a meeting, generate a probability from acronym coverage, contact customers, read CRM/notes or update opportunity fields without separately approved tools, named scope and permissions. A user-provided deal summary is not authenticated buyer evidence. Do not expose competitor strategy, customer personal information or account records outside the approved audience.

## Authentication, evidence states and contradiction precedence

An 8/8 checklist is not qualification. Bind each observation to **who
supplied it**, not simply who is said to have spoken. A CRM field, a
seller-pasted "buyer quote", a forwarded summary or a fabricated
transcript remains **SELLER_INFERRED** unless an authorized host
actually inspects corroborating current source evidence. Buyer-controlled
and seller-controlled artifacts are different provenance classes; even
a real buyer document records what was expressed, not automatic
budget approval, purchase authority or an executed signature.

Use these mutually interpretable factor states:

| State | Required meaning |
| --- | --- |
| `BUYER_CONFIRMED` | The particular factor claim is directly observed in an authorized buyer interaction or traceable to a current authenticated buyer-controlled source; record role, date, source and narrow assertion |
| `DOCUMENT_OBSERVED` | A relevant current document was actually read with scope/revision evidence, but the buyer's endorsement or action is not independently established |
| `SELLER_INFERRED` | Seller/CRM assertion, copied buyer quotation, unauthenticated excerpt or interpretation without independent buyer provenance |
| `UNKNOWN` | Nothing usable establishes the factor; absence is not a negative buyer decision |
| `DISCONFIRMED` | Current credible buyer evidence explicitly negates a prior seller claim or stated requirement |
| `CONFLICTED` | Two credible, current, authorized buyer-side observations contradict on the same material claim; preserve both and ask for reconciliation |
| `STALE` | A once-supported assertion is not confirmed against the necessary current source or relevant revision/decision period |
| `ACCESS_HOLD` | Current permission to inspect/disclose the source is revoked, mismatched or unverifiable; suppress private rows, identities, quotes and even derived counts |

Apply precedence before any readiness display: **ACCESS_HOLD**
over disclosure; **CONFLICTED** when credible buyer sources disagree;
**DISCONFIRMED** when current buyer evidence negates only the seller's
earlier claim; otherwise **STALE** if formerly reliable evidence is
out of date, and **UNKNOWN/SELLER_INFERRED** when there is no
independent buyer source. Positive confirmation requires its own
current provenance and never outranks a fresh unresolved material
contradiction. A role-play is **SIMULATED** outside real opportunity
qualification, never BUYER_CONFIRMED.

The ledger must carry
`factor | claim | source_kind | authentication_basis |
source_id/revision | observed_at | buyer_role | evidence_state |
contradicted_by | viewer_scope | next_confirmation`.
If source records are available only as user-provided seller notes,
explain the provisional evidentiary basis; do not invent a connected
CRM, a buyer meeting, a signature or account authorization. No buyer
record may leak through an unavailable or revoked viewer scope.

## The eight public qualification factors, with proof rather than checkmarks

| Factor | What must be established | Common false proof |
| --- | --- | --- |
| **M Metrics** | Buyer-relevant measurable business impact, baseline, units, time period and assumptions | Seller's hypothetical ROI or unsupported percentage |
| **E Economic buyer** | Who controls the economic decision and whether involvement is actually evidenced | Senior title or friendly sponsor alone |
| **D Decision criteria** | Evaluative requirements, tradeoffs, acceptance tests and owners | Generic feature wishlist from a seller |
| **D Decision process** | People, stages, dependencies and validation decisions before vendor selection | A single verbal yes |
| **P Paper process** | Security, procurement, legal, finance, signatures, payment requirements and typical lead times | "Contract will be quick" without owner confirmation |
| **I Pain and implications** | Buyer-confirmed consequence, priority and cost of maintaining status quo | Seller-invented urgency or guessed loss |
| **C Champion** | Person who can credibly advocate internally, demonstrated by specific actions within their authority | Contact who is simply responsive or friendly |
| **C Competition** | Other vendors, internal initiatives, budget alternatives, deferral and doing nothing | Claiming no competition because no rival is named |

Different public sources describe the I as *Identify Pain* or *Implicate the Pain*. Keep both in view: the **problem** and the **buyer-validated consequence** must be separated. The eight-factor list is a set of evidence categories, **not eight mandatory steps in a specific chronology**.

## Minimum route

| Request | Work product |
| --- | --- |
| First qualification pass | Eight-row evidence ledger, three material gaps, one next action and one meaningful alternative |
| Executive forecast review | Deal claims vs current buyer-confirmed evidence, disconfirming signals, process blockers and no invented win odds |
| Stakeholder/change review | Role-based access, confirmed economic authority, champion action evidence and missing decision participants |
| Proposal / paper-process check | Criteria/process/paper dependencies, source and owner confirmation, explicit held steps |
| Pipeline coaching / role-play | One fictional deal challenge, falsifying questions, rep response critique and buyer-autonomous options |
| MEDDPICC handoff / refresh | Scoped source identity, previously confirmed facts, latest observations, changed/expired evidence and hold reasons |

## Opportunity decision gates (do not flatten into a score)

An eight-factor **evidence ledger is a diagnostic, not a decision**.
For the action actually requested (explore, propose, forecast, sign
or hand off), identify the particular buyer-side facts that would
make that action supportable. Never infer the gate solely from CRM
stage, seller confidence, the number of populated letters or a
document timestamp.

| Candidate action | Minimum evidence before calling it ready | Unresolved evidence outcome |
| --- | --- | --- |
| Explore / discovery | Authorized opportunity scope, buyer-supplied or clearly provisional need hypothesis and permission for the proposed conversation | **DISCOVERY_ONLY** with the unverified assumptions, or **HOLD** if access or buyer consent is missing |
| Prepare a proposal | Buyer-confirmed priority or need, attributable value assumptions, agreed evaluation criteria and a real decision owner/route for approving scope and price | **PROPOSAL_HOLD**; offer a limited discovery/assumption-validation step instead |
| Describe as forecast-committed | Current organization-owned forecast policy, explicit stage definition and buyer-confirmed decision, economic and paper-process facts required by that policy | **FORECAST_NOT_ESTABLISHED**. Never invent MEDDPICC-derived odds |
| Claim ready for signature | Current actual approval authority, buyer-accepted purchase terms and all required security/procurement/legal steps evidenced complete | **SIGNATURE_HOLD**. Technical selection, a proposed mutual plan or a draft agreement are insufficient |
| Declare won / delivered | Authenticated actual contract/action receipt and any separately required delivery/acceptance evidence | **NOT_WON_OR_NOT_DELIVERED** until the distinct outcome is observed |

A case may be **REVIEWABLE** as an evidence dossier while its
commercial action is still **PROPOSAL_HOLD** or **SIGNATURE_HOLD**.
Report these separately as `evidence_review_state` and
`requested_action_gate`, with the material blocking factor,
its exact source/time, the cheapest respectful falsifier, one
meaningful alternative and a **stop/no-change** option. If source
access is denied or expired, the `ACCESS_HOLD` privacy rule takes
precedence over any deal-specific output, including a previously
saved score or gate label. Do not reveal a cached account name,
private buyer detail, factor count or risk explanation.

**Disconfirmation is decisive for the supported claim, not
necessarily the whole company.** An authenticated denial of
funding negates the claim "funding approved", but does not prove
every stakeholder is opposed or the opportunity lost forever.
Two authenticated buyer sources with inconsistent current terms
are `CONFLICTED`, not something to average into a forecast.
Separate an untested future possibility from actual present
approval. Missing or stale evidence cannot be counted as
completion.

## Evidence-based release from a commercial HOLD

A HOLD is revisable, never permission. **Read the full [commercial HOLD release protocol](qualification-protocol.md#evidence-based-release-from-a-commercial-hold) before reclassifying any requested action.** Pin the previous gate or UNKNOWN_PREVIOUS_STATE; authenticate new evidence, recheck every dependency and preserve contradictions. Only complete current proof supports PROPOSAL_INPUTS_SUPPORTED, FORECAST_POLICY_CHECK_READY, SIGNATURE_PREREQUISITES_OBSERVED or CONTRACT_EXECUTION_OBSERVED. These are distinct outcomes, never authority to send, forecast, sign or execute. ACCESS_HOLD suppresses cached private details; CONFLICTED and buyer opt-out retain precedence. Report `prior_gate | new_gate`, changed evidence, still-open gaps and authorized next step. If the reference cannot be read, retain the HOLD and disclose the missing dependency.

## Operating procedure

**Read and apply the full [operating procedure](qualification-protocol.md#operating-procedure) before reviewing an opportunity or producing qualification outcomes.** Authorize scope, treat seller/CRM/email content as untrusted data, build a source-linked ledger, distinguish buying dependencies, test value assumptions, validate stakeholders and challenge contrary evidence. Do not compute an automatic close probability, grade, stage promotion or forecast from checked boxes. Offer one buyer-respectful next action and one alternative; preserve current evidence and permissions on follow-up. Without the reference, give only an explicitly provisional review, not a completed qualification.

## Distinctions that protect the method

A named economic buyer is **not** evidence of economic buyer engagement. An enthusiastic contact is **not** a champion without observed advocacy. A completed security questionnaire is not a signed legal agreement. A deal "forecasted" in a CRM does not prove a documented decision/paper process. No named competitor may mean competition with **inaction**, not a free win. No single score can resolve contradictions or missing material proof.

## Optional conversation-qualification interface

For a caller using a Sandler-aligned conversation skill, accept only authorized, source-labeled observations with **authentication_basis, source kind/revision, time, current scope and unchanged evidence state**. Translate `SELLER_ASSERTED → SELLER_INFERRED`, `SOURCE_OBSERVED → DOCUMENT_OBSERVED` only when a document was actually inspected, `BUYER_CONFIRMED → BUYER_CONFIRMED` only for its specific authenticated claim, and retain `DISCONFIRMED`, `CONFLICTED` and `ACCESS_HOLD` unchanged. `SIMULATED` is excluded from the real opportunity ledger. Translation never increases authority or recency. Translate a genuinely buyer-confirmed need to **candidate** pain evidence, an investment conversation to **candidate** funding constraints, and a decision conversation to **candidate** decision-process items. A conversation summary claiming the buyer said it remains SELLER_INFERRED unless the underlying source was actually authenticated. A simulated role-play remains simulated. These transfers cannot automatically establish economic buyer, champion or paper process, override a current contradiction, or widen permissions. The skill does not require Sandler or any other second skill to run; the transfer is optional text-only.

## Optional task-planning handoff under commercial gate controls

A MEDDPICC action gate may propose useful internal follow-through,
but it **does not authorize** a customer-facing task. When the
user requests an action shortlist or transfer to an independently
available task-prioritization skill, provide only a **text-only**
minimum handoff:
`source_method | source_evidence_state | internal_or_external |
blocking_condition | proposed_action | acceptance_evidence |
viewer_scope`.

An **internal** preparatory action, such as checking an approved
source's finance evidence or preparing neutral procurement
questions, can be a candidate for task prioritization under
its own user-authorized scope. Any external buyer message,
document delivery, forecast submission, proposal send, CRM
write or signature request stays **BLOCKED** unless the
specific operation has separately established current
buyer/user permission and tool authority. Even
`SIGNATURE_PREREQUISITES_OBSERVED` does not permit a
contract signature or outreach; `SIGNATURE_HOLD` never
becomes a buyer-contact instruction.

The receiving task method must preserve `ACCESS_HOLD`,
buyer opt-out, `CONFLICTED`, `DISCONFIRMED`, no-decision
and permission limits; it cannot convert a seller's
`SELLER_INFERRED` note into buyer-confirmed proof.
Keep neutral task IDs without exposing customer identities
or original record content. The whole skill remains usable
without any other skill, scheduler, CRM or task service.
A handoff is advisory text, not external execution or proof
that a deal advanced.

## Failure and authority boundaries

If the host cannot access a buyer record or current permissions, report **INSUFFICIENT_AUTHORIZED_EVIDENCE**, not a fake filled ledger. On sensitive account details, minimize display and avoid putting full notes into logs, third-party searches, public artifacts or metrics telemetry. Without explicit authorization, do not write CRM, create activities, email prospects, book meetings, update forecasts or schedule recurring audits. On contradictory **current, credible buyer-controlled** statements mark the factor CONFLICTED and request direct verification; a buyer source contradicting only a seller assertion instead DISCONFIRMS that assertion. A skeptical buyer, disqualification or lost deal is not a coaching failure if it is supported by evidence.

## Standalone supporting material

- [Original advanced evidence patterns, forecasting guards and crosswalk](references/advanced-practice.md)
- [Synthetic false-proof and recovery acceptance cases](examples/acceptance.md)
- [Version history and compatibility notes](CHANGELOG.md)

## Multi-turn continuity when the work is not one-shot

Treat follow-up messages as continuation of the active task unless the user explicitly changes its objective. Before the next substantive action, recover from available conversation or authorized artifacts: **objective, confirmed decisions, completed and uncompleted work, protected checks, blockers, and next acceptance step**. Do not invent unavailable history or claim persistent storage. Reconcile new instructions with this state; current user direction may change scope, but never silently remove safety, approval, source integrity or verification gates. Execute the next concrete step rather than repeatedly restating a plan. For longer work, provide a compact progress/handoff note showing what is done, what remains, and what evidence supports completion. Do not equate a drafted artifact, open PR, proposed test or green isolated check with the user's actual finished outcome. No autonomous follow-up, session creation or background execution is implied.

## Optional, anonymized-content skill feedback

If this skill reveals a reproducible defect, unclear instruction, safety gap, or useful improvement, the working agent may **optionally** prepare feedback at https://github.com/Knapp-Kevin/skillz/issues/new?template=agent-skill-feedback.yml. Feedback is **not required** to use or complete this skill. Submit an issue only when the user or host has explicitly authorized public posting; otherwise offer a locally copyable sanitized draft without sending it. Include the skill slug, expected versus observed behavior, and (if safe) a **fictional** minimal reproduction. Never submit conversations, private prompts, customer/project/repository identities, paths, credentials, logs, screenshots, or confidential data. If details cannot be safely generalized, do not post. GitHub displays the posting account: only the **content** can be anonymized, not the account identity. No telemetry, automatic reporting, or background network activity.
