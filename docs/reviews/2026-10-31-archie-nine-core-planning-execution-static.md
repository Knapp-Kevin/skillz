# Archie Indian Superpowers: nine core planning/execution exact-pin reviews (2026-10-31)

## Whole-family macro map and denominator

Registered tracked reference pin `a95a59d221d44b89d4fc27a52934e24fb2060ddb`; recursive upstream tree has **56** distinct first-class manifests: 17 core, 38 OpenClaw-native, one community, with no duplicate manifest blobs. The two exact-version companion directories previously contained **9** matching records (eight core, one native). Nine remaining core paths were confirmed genuine gaps. Core **8/17 → 17/17**; tracked family **9/56 → 18/56**, gaps **47 → 38** (37 native and one community). No source admission, pin movement, vendoring or denominator change.

## Individual exact-version decisions

| Package | SKILL.md blob | Package tree | Last package change | Static decision |
|---|---|---|---|---|
| `brainstorming` | `3fe96151e6c9b88f7e2e49975452b1e513b5ee29` | `f5799d818bfcaedc0c0d2b44eecab649459fb87e` | 2026-03-14 | VERIFIED semantic only 17/20 |
| `create-skill` | `6bbd507a278fb4db995f3b860660d258f1f63389` | `8e888605052bbbac056d30b1a6879157b238c6c4` | 2026-03-15 | REJECT unchanged 13/20 |
| `executing-plans` | `e254e14ec6693c7a0243876c63cea4426912c563` | `c85b2817eb186e34fa87b6220dce8cfa36c25839` | 2026-03-14 | REJECT unchanged 14/20 |
| `project-onboarding` | `e06ce4040bcfb9022b144056368117a72dc9cef7` | `155e3ef30d3a5f9f2e3e5aec24ce97d180b86a4b` | 2026-03-15 | REJECT unchanged 12/20 |
| `pull-request-feedback-loop` | `a0deae2ab6adabe6c9c055a3e22fd48f9f55210e` | `ede45efc5621c11e83d5f828b3f05c338f08e6a8` | 2026-04-17 | VERIFIED semantic only 17/20 |
| `subagent-driven-development` | `21f0ef38c492e6c678e0d69110daa597e9929c97` | `45655661646e2c5847930aff74bfa7d36bbe9a12` | 2026-03-14 | REJECT unchanged 10/20 |
| `test-driven-development` | `e0c0df52242a9e2ab86304f70807aceb91ccd471` | `a5f8bc721245984cc630d0e10d4fca9f925950a6` | 2026-03-14 | REJECT unchanged 15/20 |
| `using-superpowers` | `5262a935dbff9ff68ba675d353f3195e6fc61bb8` | `58cb6c8c88abfde4f1bbd2ae16f6287b3278f83d` | 2026-03-14 | REJECT unchanged 13/20 |
| `writing-plans` | `bfe88131e0a7d477e2e66fc80c9fe728928c6a1d` | `3785f4552e341ec45ee3ddcd906490ba838f6014` | 2026-03-14 | REJECT unchanged 15/20 |

Each new provenance/verification pair binds the registered pin, manifest Git blob, full package-tree Git SHA, skill-specific upstream revision/date, source path, dependency context, controlled tags, authority/portability, individual rubric and explicit security/behavioral `not-run`. Bundled `create-skill/TEMPLATE.md` and `project-onboarding/onboard.py`, `STATE_SCHEMA.yaml`, `example-state.yaml` were statically read as upstream-owned material. No scripts were executed.

## Synthesis and hard boundaries

**2 VERIFIED semantic only:** `brainstorming` is advisory option/risk comparison. `pull-request-feedback-loop` is scoped to a user-requested PR, groups review findings, verifies local changes and prepares but does not automatically send replies; force push, branch deletion and review dismissal are explicitly gated. Neither static approval authorizes a remote push, side-effecting tests or unrelated private reads.

**7 REJECT unchanged:** `create-skill` assumes persistent skill writes, install symlinks and cron registration; `executing-plans` blindly follows plan steps and writes memory; `project-onboarding` crawls private code and writes durable PROJECT.md/state with auto-load/monthly refresh; `subagent-driven-development` mandates `--permission-mode bypassPermissions` and external/background delegation; `test-driven-development` lacks test environment and external-fixture authorization; `using-superpowers` treats a 1% heuristic as permission to follow unreviewed skills exactly; `writing-plans` persists private memory checkpoints without approval. The bundled onboarding Python helper also reports registration when missing PyYAML prevents state persistence. Preserve valuable planning, TDD, PR feedback and decomposition patterns as ADAPT/EXTRACT/CHECKLIST where appropriate.

**Shared structure:** brainstorming → writing-plans → executing-plans → subagent-driven-development is a coupled pipeline, not independent trust evidence. Creator/onboarding procedures share OpenClaw persistence assumptions. No security scan or representative external behavioral/adversarial validation was executed.

**License omission:** pinned root `LICENSE` blob `7869c12457fe7aee29e85b93036280bfde5380c2` is 259 bytes, declares MIT but omits standard notice/disclaimer text. The source registry incorrectly asserted standard MIT despite GitHub NOASSERTION; its rationale was corrected. External clarification is tracked in [#544](https://github.com/Knapp-Kevin/skillz/issues/544). No redistribution or unchanged-use license clearance is inferred.

## Lifecycle and accounting

Starting main `5c195e2707b11a6c34cbd5862a6aefdfa77eb92e`: independently enumerated **992 verification YAML / 992 matching provenance YAML**, zero unmatched, including 9 Archie pairs. This tranche adds 9/9 companions; expected post-merge **1001/1001**, 44 first-party / 957 third-party (836 registered/tracked + 121 candidate-only). Five public accounting surfaces updated atomically, including stale live 984 totals in INDEX and SYSTEM_STATE snapshot. All seven pre-existing issues and five existing draft PRs were triaged: #489/#492/#496 need pinned SkillSpector v2.12.0 complete reports and independent executed adversarial acceptance for 36 changed first-party package trees plus shared registry reconciliation; #412/#413 retain admission gates. All five drafts mergeable but unqualified, with no reviews, review threads, statuses or workflow runs. Issue #544 opened for exact license terms; no existing issue qualified for closure. No repository-owned runtime, scripts, tests, CI, schedulers, scanners or generators introduced.

Next priority: external qualification of 36 first-party repairs; continue 37 Archie OpenClaw-native gaps in a disjoint lane.
