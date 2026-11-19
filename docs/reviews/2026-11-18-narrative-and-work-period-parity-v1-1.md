# Narrative and work-period replacements: functional outcome review

Review date: 2026-11-18. Audit issue: #738.
Review method: manually inspected the four retained historic SKILL.md
entrypoints, two replacement skill entrypoints, existing MIT licenses
and revised original synthetic acceptance files. No host-agent
execution or secret/private account reading took place.

## Exact evidence and rights boundaries

| Historical input | Exact Git blob |
| --- | --- |
| skills/deck-outline/SKILL.md | `63c943992417148d010551238a15259d4968cb55` |
| skills/devlog-draft/SKILL.md | `d74ff133f69c8908c4acf296fb93313069082114` |
| skills/standup-writer/SKILL.md | `21c216fbc46f516fecc0a562afbe652fbd436b95` |
| skills/week-in-review/SKILL.md | `5fa0b34372aa28067f41ab19afacbe4430a31b4e` |

The historical account/author strings do not establish copyright
origin. Only *functional requirements* from historical skills were
used for newly composed instructions. Do not copy their wording or
claim MIT permission over uncertain legacy content. The historical
files and prior review records remain intact; removal is not
authorized by this static assessment.

## Functional outcome comparison

| Deliverable | Source-level gap in authored v1.0 | Independently written v1.1 response |
| --- | --- | --- |
| Deck planning | Narrative beats not bounded; no headline-only coherence check | Default 10–14-step causal spine and claim-level slide progression |
| Slide detail | General visual instruction; no explicit per-slide audience inference or source gap | Claim, evidence, visual treatment, transition, and missing-source flag |
| Build handoff | No direct capability-resolution gate | Requires editorial approval unless waived, qualified host tool and actual file verification |
| Devlog | General narrative with no guaranteed title options, single story or receipt-state ladder | Three title candidates, one evidence-bound thread, status-specific claims and publication review |
| Daily standup | General daily progress without contractually stable structure | Did, Doing, Blocked, Needs confirmation, with bounded date window and provenance |
| Weekly review | General retrospective without explicit starting-list artifact | Shipped, Stalled, Decisions and prioritized portable Carry-forward |
| Local repository inspection | No named repository-controlled Git command hazard | Rejects unsafe local helpers and uncontained Git use; API-first |
| Publication/storage | Permission safeguard already existed | Preserved and clarified independent permission and post-write verification |

## Complete package fingerprints

Each replacement comprises SKILL.md, LICENSE, and
examples/acceptance.md. Prior tree reconstruction was reproduced
exactly using the Git object model.

| Package | SKILL blob | Cases blob | LICENSE blob | Tree SHA |
| --- | --- | --- | --- | --- |
| evidence-narrative-composer v1.0 (historical) | `d67e8824ab340014f5379f32fc8e02df3220d18a` | `d509edb0ebc9d51f48446c6713ff5d6d5b276a52` | `023abdb34298b27580d1d303084aca942050585e` | `6e356d294bab2483fd4a938c24fd5e5b0b2ad34a` |
| evidence-narrative-composer v1.1 | `1e8cb987017c06dd12b995ed22055dc6b3367b45` | `37da3e6ea9b5575f6d5a93985e0e5c156df6b4c6` | `023abdb34298b27580d1d303084aca942050585e` | `2b1a5f2885c4d60bf7446ed1eeb0691ea7a8b12f` |
| work-period-evidence-reporter v1.0 (historical) | `bbd1317876ddbcdee2f25d5ffb9530685a9fb3e6` | `7d0ccea01ff82dcd8120a50ed79161351c9d6f97` | `023abdb34298b27580d1d303084aca942050585e` | `75a2ef507564aa4c4a827b7f15a6e3b21cbd5697` |
| work-period-evidence-reporter v1.1 | `dd0bc7714997c7deb0c66dbc1dc9714514082dee` | `8ca3ed2c5379ab013e9fe67c678cd71167592a32` | `023abdb34298b27580d1d303084aca942050585e` | `d9da08e777e8c5ad23f4c91f5def189b4ca29bc2` |

## Current source review (not behavioral acceptance)

Rubric order: trigger precision, procedural clarity, authority/safety,
failure behavior, evidence discipline, dependency coherence,
portability, differentiated usefulness, adversarial resilience and
effectiveness design. Reviewed exact three-file packages with no
scripts, installations, external sends or implicit persistence.

| Exact version | Dimension scores | Total | Static disposition |
| --- | --- | --- | --- |
| evidence-narrative-composer v1.1 | 2,2,2,2,2,2,1,2,2,1 | **18/20** | VERIFIED_STATIC |
| work-period-evidence-reporter v1.1 | 2,2,2,2,2,2,1,2,2,1 | **18/20** | VERIFIED_STATIC |

Portability still depends on actual host artifact and authorized
source capabilities. Effectiveness remains an unobserved design
hypothesis. No static hard-fail finding was identified. Source
materials (including git messages, calendars and vendor content)
remain untrusted data, never instructions to act.

## Unproven and follow-up

- All sixteen newly specified cases are **expected behaviors only**,
  not executed output evidence.
- No presentation file was generated or visually inspected; no
  publication, account reads, local Git execution or task writes.
- Legacy-host functional parity and the target **1.5x improvement**
  have not been measured and remain **NOT_PROVEN**.
- Exact-head consumer/index freshness and merge state require final
  recheck. Historical originals may not be retired.
- The full 44-to-21 audit remains open under #738.
