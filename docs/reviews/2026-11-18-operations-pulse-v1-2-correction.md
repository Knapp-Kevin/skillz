# Functional regression correction: daily briefing, inbox triage and repository pulse

Reviewed: November 18, 2026 (owner-local), issue #738.

## Correction to earlier source assessment

The merged v1.1 source reviews improved `personal-operations-control-board`
and `repository-delivery-assessor`, but their earlier static verdicts
were **not sufficient to establish full source-level functional parity**
for every historical entrypoint. The current audit found specific
missing *output requirements*:

- `skills/daily-briefing/SKILL.md`: a one-screen action-first
  briefing with **Today's Shape / Act On max 5 / Loose Ends Carried Over /
  FYI**, using individually scoped calendar, unread mail and yesterday's
  approved records.
- `skills/inbox-triage/SKILL.md`: user-visible
  **Act / Delegate / Read Later / Archive** piles, one-line reason per
  message, priority flags, and a complete safe reply draft for every
  Act message requiring a response when enough evidence is available.
- `skills/repo-pulse/SKILL.md`: action-first
  **Needs You / Per-Repo Notes / Quiet Repos** multi-repository
  output, correctly bounded review requests, red CI, recent activity,
  stale branches and authorized local state.

The prior package had generalized task/message categories or portfolio
analysis but no mandatory compatible deliverables for these triggers.
This is a **confirmed source-level gap** and therefore the older
static score must remain historical rather than support a new
parity claim.

## Independently authored v1.2 remediation

**Personal Operations Control Board v1.2** now requires the specific
one-screen morning output, strict action cap, appropriate missing-source
disclosure, four distinct human-facing inbox piles, per-item reasons,
priority-contact verification, drafts and DRAFT_BLOCKED status.
It retains privacy and no-send/no-archive defaults. Explicitly
separately approved task/repository creation or status writes remain
available but are categorized by *maximum* host authority
**MUTATING**, with **read-only as default**, rather than the inaccurate
former index label.

**Repository Delivery Assessor v1.2** now explicitly requires
action-oriented multi-repo pulse, evidence-limited user-review requests,
source-bound check/ref history, quiet repository coverage and
LOCAL_STATE_NOT_ASSESSED when the checkout is not safely inspectable.
No new write, Git shell execution or recurring scheduler is authorized.

Sixteen additional **original synthetic expected-outcome** cases
(eight per revised package) test the missing output modes and negative
authority boundaries. They are specifications, not observed host runs.

## Historical reference identity and rights

| Historical comparator | Git blob SHA-1 |
| --- | --- |
| `skills/daily-briefing/SKILL.md` | `95e18a42978ef7ef5e6a1a8f4d60012c98c73da9` |
| `skills/inbox-triage/SKILL.md` | `9326d7a691e40ff30a07a71738b13a04117206d6` |
| `skills/task-surface/SKILL.md` | `27f1a5ffe56f7653ec68c6ac998a4a03c0137085` |
| `skills/repo-doctor/SKILL.md` | `fed90fa0a664611e560bbc3ded630eb9e72253e1` |
| `skills/repo-pulse/SKILL.md` | `9e6938b29e4c0748e4098bc53a96498f42784423` |

The historical skills remain rights-uncertain source comparators;
account ownership does not establish original authorship. No original
text/assets were copied into the v1.2 source and no legacy
entrypoints were retired or relicensed.

## Exact three-file package identities

Each package has `SKILL.md`, `LICENSE` (unchanged MIT Git blob
`023abdb34298b27580d1d303084aca942050585e`), and
`examples/acceptance.md`. Both v1.1 package tree IDs were
independently reconstructed from their previous component Git
blobs before v1.2 trees were calculated.

| Package | SKILL blob | Cases blob | Complete Git tree |
| --- | --- | --- | --- |
| Personal Operations v1.1 (historical) | `6ec82d3e34e2bd5adea16838d9ba49955106b893` | `1d909279525f353d7d5a9204207b3a1fcb4f6a14` | `9ab584fac422cbaaea81d12fdc832945c9661bf4` |
| Personal Operations v1.2 | `485eec5425782c0310413de3a355a844ff856a25` | `3e7a4dd2b63bbc0b1f322e326a3a73e2614d879c` | `8a2036ee370e1918da0964b7dbeff91b0edf8a07` |
| Repository Delivery v1.1 (historical) | `8f142859fac2420657377453f5b531d80c31dbb4` | `2fd511c67a50f730adfd945353c332f6b1ee2189` | `d77f373e2825c2eee23cfe60937afc83a547e778` |
| Repository Delivery v1.2 | `9261eadd5df37e4265f8913c538c0a379cf2f8f4` | `937042e7d59dcba2681aecc32f6ff17d50a8b113` | `a0d217f8f48399acb95d3a8f263f26fb87eda4f1` |

## Current source-only assessment

Read each exact v1.2 package and the five relevant historical
SKILL entrypoints. Reviewed trigger specificity, concrete procedure,
consent/permission boundaries, failure behavior, source evidence,
dependency safety, portability, usefulness, adversarial cases and
effectiveness design. Dimension scores
`2,2,2,2,2,2,1,2,2,1` = **18/20** for each *new source version*.
No current source hard-fail was identified; portability remains
host-connector-dependent and effectiveness remains design-only.

**No host-agent A/B trial was executed**, including against any of
the five historical modes; no observed customer or operator outcome
was established. The earlier 18/20 v1.1 reviews are superseded for
the changed exact package identities, and must not be carried forward
as if they reviewed v1.2. Preserve their historic records.

## Dependent acceptance pins and retirement

The paired-host ledger contains mappings from
`daily-briefing`, `inbox-triage`, `task-surface`,
`repo-doctor` and `repo-pulse`. All five records must be
re-pinned to the **current v1.2 authored tree**; existing phase-two
cases for `task-surface` and `repo-doctor` must also be
re-pinned. The tests remain `NOT_RUN`, and prior source-level
static reviews prove neither source-to-host behavior nor 1.5×
improvement. No original is eligible for retirement.
