# Sales methods v0.2.0: release-significance correction and bounded capability qualification

Date: 2026-11-24
Repository: `Knapp-Kevin/skillz`
Scope: first-party `sandler-conversation-strategist` and
`meddpicc-opportunity-assurance`, both independent MIT packages.
Baseline: merged [PR #912](https://github.com/Knapp-Kevin/skillz/pull/912),
merge `501d2b5025db2302111c65bc5a58e11a93ee703c`.
Qualification at authoring: **candidate source and maintenance review**, not
real consuming-agent behavior.

## The decision: a minor bump is warranted

The [repository version discipline](../skill-template.md) explicitly says
a package version is a **deliberate release identity**, not a counter of
each PR, paragraph, test or registry note. It also says significance is
determined by **user-visible behavior, compatibility, safety and actual
distribution needs**, and that source fingerprints change separately.

The initial `0.1.0` packages were separately authored and merged in PR
#910. PRs #911 and #912 then merged **material behavior** on `main`:
- Buyer-controlled conversation routing, explicit opt-out stop and
  proposal/no-fit branches in Sandler.
- Claim-specific buyer provenance, cross-method state translation,
  contradictory source and access-revocation safeguards.
- Separate MEDDPICC evidence dossier reviewability from commercial
  proposal, forecast, signature, delivery readiness decisions.
- A period/unit-safe illustrative training-services value model.

These were more than harmless prose edits. **Continuing to describe the
main-branch consumer-facing capability as unchanged `0.1.0` obscured
actual capability growth.** That was an overly conservative decision,
not an immutable repository mandate. We intentionally consolidate the
accumulated capability expansion **once** as `0.2.0` for each package,
not as a series of automatic patch increments.

**Why not `0.1.1`?** The first-party skills expose newly useful
procedures/decision outputs; they are not solely corrections of an
implementation bug or typo. **Why not `1.0.0`?** Stable independent
host behavior, installation compatibility, cross-agent interpretation
and customer value have not been verified. There is no evidence that
these packages are ready for a mature stable-major compatibility claim.

**This is a repository-hosted source release only.** No separate npm,
PyPI, marketplace, hosted course, official vendor certification or
production agent installation is asserted. The earlier `0.1.0`
source revisions remain reachable via Git commits and reviews;
the new `CHANGELOG.md` files document that their content evolved
while retaining an unchanged declared release number.

## Engine-first diagnosis and additional substantive changes

Existing components actually applied, not replaced:
- [Forge](../../engine/skills/skill-forge/SKILL.md) for authorized first-party
  edits, whole-package portability and provenance closure.
- [Eval](../../engine/skills/skill-eval/SKILL.md) and
  [Audit](../../engine/skills/skill-audit/SKILL.md) for exact-source
  semantic review and frozen successful outcomes.
- [Shared refinement lifecycle](../../engine/refinement/README.md) for
  original failure hypothesis, adjacent negative, preservation and
  false-green checks; retain `STATIC_RISK` rather than fabricating
  an independently reproduced model failure.
- [Builder acceptance](../../engine/builder/acceptance.md) and
  [version policy](../skill-template.md) for meaningful artifact
  completion and defensible release identity. The builder's
  CREATE/COMPOSE generator is **not** required to revise either
  already complete standalone skill.

### Sandler: fictional turn-taking as an actual practice protocol

**Finding S-PLAY (high use-value):** Existing role-play guidance only
said to simulate a buyer and score the rep. It did not specify
the interaction boundary between an *agent-invented buyer utterance*
and a *real user-written rep reply*. That could yield a long fabricated
two-sided dialogue and unearned coaching scores while looking complete.

**Repair:** Distinguish explicit full-dialogue fictional DEMONSTRATION from INTERACTIVE_REHEARSAL, then add the SETUP → PLAY → OBSERVE → COACH → CONTINUE/CLOSE
procedure: one fictional buyer utterance, **stop for rep input**,
separate `SIMULATED` buyer and `ROLE_PLAY_OBSERVED` rep evidence,
one behavior-linked coaching improvement and a meaningful alternative.
A stop instruction stops practice; a no-contact response is not an
objection to overcome. A user who never supplies a rep turn gets
`NOT_OBSERVED_REP_BEHAVIOR`, not a fabricated grade.
This works in text-only offline host environments with no connected
CRM, audio or external course. Cases S15–S18 cover positive, false-green,
zero-turn and no-recording situations.

### MEDDPICC: recovery from a justified action hold

**Finding M-RECOVER (high operational value):** The previous
`PROPOSAL_HOLD`, `FORECAST_NOT_ESTABLISHED`,
`SIGNATURE_HOLD` and delivery boundaries were good safety
checks, but the instructions could leave an agent permanently
saying HOLD after new authoritative evidence arrived.

**Repair:** Add source-gated re-evaluation of a **specific requested
commercial action** and conditional advisory outcomes:
`PROPOSAL_INPUTS_SUPPORTED`,
`FORECAST_POLICY_CHECK_READY`,
`SIGNATURE_PREREQUISITES_OBSERVED`, and
`CONTRACT_EXECUTION_OBSERVED`. Every previously required buyer
obligation is rechecked; a new security approval does not
automatically clear missing budget or legal acceptance. A later
buyer-controlled approval may supersede a dated denial without
destroying its history. Cross-account source reuse, CRM status
promotion and current-access revocation remain hard stops.

The new statuses are **evidence assertions**, never send/sign,
outreach, forecast, CRM-write, or scheduling authorization. Cases
M18–M21 and an original T0–T4 reference progression cover partially
cleared, fully supported, unauthorized-source and historic-denial
counterexamples.

## Explicit unchanging boundaries

Both skills remain standalone, no compulsory sibling package,
text-first and offline usable. Keep the original rights, independent
vendor non-affiliation, zero default CRM/outreach permission,
privacy-on-revocation, and customer autonomy. The common fictional
`CASE-JOINT-01` is unmodified and the prior 15 sales-method
contract tests must continue passing.

No user preferences are committed as canonical policy, no new
automated skill engine or third-party content is introduced,
and no GitHub issues or external tasks are created as a surrogate
for changing and merging the actual skills.

## Qualification plan and evidence levels

| Check | Evidence type | Limit |
| --- | --- | --- |
| Existing authored skill package test group | LOCAL_TEST if CI executes | Version and source identity consistency, not consumer semantics |
| Existing and new sales skill tests | LOCAL_TEST if CI executes | Structural, static fixture and 0.2.0 contract coverage |
| Complete package Git fingerprints | Deterministic source identity | New bytes are not proof of effectiveness |
| Exact final-head GitHub code review | Independent code review | Does not establish seller/buyer model-host performance |
| Actual independent consuming agent using fictional S15/M18 cases | NOT_RUN unless genuinely performed | Requires explicit recorded inputs/outputs and host capability |
| End user outcome and sales effectiveness | NOT_RUN | No observed actual win-rate, consent, or ROI impact |

The version release is **not** a formal review promotion. Both must
retain `review_status: needs-re-review`, `verification_status:
needs-re-review`, and `behavioral_validation: not-run` per current
repo-wide quality gates. A clean code review cannot certify
Sandler training or MEDDPICC commercial forecasting.

Proposed source identities, bound to the final five-file packages:

| Package | SKILL.md Git blob | Complete Git tree |
| --- | --- | --- |
| Sandler `0.2.0` | `adf3fb41ba362b484a6f1caa307c1de773da4752` | `4418e608782c4a3811c6ec12f409e8404f51126d` |
| MEDDPICC `0.2.0` | `c2d59e2102430c6b4845130dd39cd8ee4b7983a0` | `8c25620e8a9394ce87cf9d88a0bc8d5ba034943e` |

**Release completion:** exact-head authored CI, full-package review,
any material findings corrected, actual PR squash merge and
`main` readback. A PR left unmerged is not delivered.
