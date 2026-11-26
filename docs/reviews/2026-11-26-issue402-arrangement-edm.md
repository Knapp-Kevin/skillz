# Issue #402: arrangement and EDM exact-source review

Date: 2026-11-26. Scope: complete owned source of two historically INCOMPLETE packages at `jtydhr88/music-composition-skills@e283141babb8806f2798d5fd2d9e833e75c1bd26`. Default branch compares identical to that pin. Three owned files and both Git trees reconciled: sorted regular-file entries with their returned blob IDs reproduce the exact historical Git tree SHA-1. Root LICENSE and NOTICE read; sibling schema/reference existence checked (not a complete sibling-package audit). No source commands, DAW actions, model calls, audio, scanners or consumer agents executed.

| Package | Pinned tree | Owned files | Static rubric /20 | Historical scan |
| --- | --- | ---: | ---: | --- |
| [mc-arrangement-arch](https://github.com/jtydhr88/music-composition-skills/tree/e283141babb8806f2798d5fd2d9e833e75c1bd26/plugins/music-composition/skills/mc-arrangement-arch) | `f372d0e4348f02b9fb51cf7d39d91c05b0bb3fe8` | 2 | 13 | INCOMPLETE |
| [mc-style-edm](https://github.com/jtydhr88/music-composition-skills/tree/e283141babb8806f2798d5fd2d9e833e75c1bd26/plugins/music-composition/skills/mc-style-edm) | `803834c1b9360986a7d90e738e4fffb515628640` | 1 | 13 | INCOMPLETE |

## Findings

### mc-arrangement-arch

- **inconsistent-reported-denominator** (reference.md §3; SKILL.md §3.3): The reference equates 36/62 with 70%; the fraction is approximately 58.1%. The source does not establish which numerator or percentage is correct. Do not use the published 70% as verified or silently repair the underlying observation.
- **inconsistent-lint-identity** (SKILL.md §10; reference.md §4): Energy decline is assigned lint #5 in the entrypoint and #1 in the reference; the reference calls #3 a multiples-of-four constraint while the entrypoint calls it multiples-of-eight. A consumer cannot treat these conflicting identifiers as the same executable check.
- **sample-to-universal-generalization** (SKILL.md §§2.2, 4.2, 5.1, 7, 11; reference.md §3): Finite corpus observations and unverified segmentation do not establish universal arrangement or AI-origin detection rules. The entrypoint itself recognizes minimal, short and repetitive exceptions; its compulsory checklist can still invite forced alterations. No listening or source-classification outcome was independently measured.
- **project-mutation-and-rights-boundary** (SKILL.md §§3.1, 4.1; root NOTICE): The proposed fill/delete and reference-audio import/remove workflow is useful as a method but does not authorize actual DAW edits, deletion, acquisition or copying of third-party audio. The assertion about structural borrowing is not a legal clearance. Book quotations and translations are explicitly outside root MIT.

Positive safeguards: Explicit source uncertainty and a distinction between sampled tendencies and techniques, including contradictory peak-detection evidence. Role boundaries and intentional-exception guidance for solo, loop-based and short forms.

Remediation: Reconcile numerator/denominator against original measurements, align lint identifiers with an independently verified schema, constrain assertions to the studied population, require authorized disposable project edits and preserve separate third-party rights.

### mc-style-edm

- **style-exception-versus-hard-check** (SKILL.md §§3.3, 4.2, 6.1, 10): The entrypoint describes sustained-density dub techno and intentional all-grid production, but the final checklist calls for build/drop contrast, low-frequency removal and a new drop element. These checks need conditional applicability for tracks without drops; otherwise a valid style is treated as failed.
- **unverified-sample-and-aesthetic-claim** (SKILL.md §§4.2, 6, 8): Cross-genre numerical comparisons rely on ten examples per named genre and unverified upstream measurements. A finite set of examples does not prove grid alignment identifies AI, or that a proposed drop works on a dance floor. The source acknowledges beat-tracking errors; no actual audio or listener test was performed.
- **sibling-reference-not-standalone** (SKILL.md §§7, 9; scanner incomplete locations 215, 285): The one-file export points to the neighboring sound-design reference and shared ARR-SPEC fields. The named reference and schema exist at the immutable upstream pin, outside this package. The recorded missing-reference count is not evidence of two missing owned files; no scanner rerun or executable lint pass is claimed.
- **third-party-reference-and-project-authority** (SKILL.md §§5.1a, 7; root NOTICE): Book-derived recipes and attributed technique descriptions are not a blanket MIT grant over the underlying published text. Suggested synthesis, sampling and render changes do not authorize backend calls, paid usage, external assets or DAW modifications.

Positive safeguards: Separates listening context and subgenre, provides transfer limitations and explicitly allows justified quantization exemptions. Reports uncertain BPM measurement rather than presenting detected tempo as ground truth.

Remediation: Make drop-specific checks conditional, preserve exemption semantics, verify companion resources and output applicability, measure actual listening outcomes, and review rights and destination authority independently.


The upstream root MIT grant applies to original expression only; NOTICE excludes separately protected publications and translations. No upstream expression copied, no rights or unchanged-use approval granted. The scanner's incomplete Chinese-language coverage is not itself evidence of intentional obfuscation. The EDM sibling reference exists at the pin but is not owned by the single-file package. Neither observation is a scanner PASS.

## Accounting

[Exact machine ledger](../../registry/security/q8-two-incomplete-arrangement-edm-static-dispositions-20261126.json). Direct static review frontier advances **30/40 to 32/40**, including **7/7 historical FAIL + 25/33 historical INCOMPLETE**. Eight incomplete packages remain. Historical scanner states remain 10 PASS / 7 FAIL / 33 INCOMPLETE. No new scan, behavioral pass, unchanged-use approval or corpus discovery credit. #402 remains open.
