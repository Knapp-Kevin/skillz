# P0 #402: executable code triggered by ostensibly read-only Git inspection

Date: 2026-11-05. **Real local Git CLI reproduction, source fixes and structural tests; NOT NVIDIA SkillSpector or agent-host behavioral qualification.**

## Reproduced execution defect

In an isolated temporary local Git repository, the reviewer set `core.fsmonitor` to a test-owned executable that only wrote a harmless local sentinel file. Invoking ordinary `git status --porcelain` triggered it. The separately executed guarded control `GIT_OPTIONAL_LOCKS=0 git --no-pager -c core.fsmonitor=false -c core.hooksPath=<trusted-empty-dir> status --porcelain` did **not** create the sentinel. Both results were observed in the actual container Git version 2.47.3. No external files, credentials or network were accessed in this reproduction.

This proves that a source instruction recommending plain `git status` over an untrusted checkout can cause local code execution even if the skill promises to be read-only. It does NOT establish that a particular real-world agent host executes dangerous Git commands, nor that the example guard covers every repo-controlled execution mechanism on every platform. Require verified host isolation or skip local Git and report missing evidence.

## Exact source changes

| Skill | Fixed source Git blob | Complete one-file package Git tree | Source assertions | Current static grade |
|---|---|---|---:|---:|
| Repo Pulse 1.1.3 | `9e6938b29e4c0748e4098bc53a96498f42784423` | `452ecbe5dd3d51825cda94890a82f0ccdbf11d2d` | **8/8** | 18/20 |
| Standup Writer 1.1.2 | `21c216fbc46f516fecc0a562afbe652fbd436b95` | `d6429bfea7bebe567aa52f7c5f1f6c44fd10086f` | **7/7** | 18/20 |
| Repo Doctor 1.0.1 | `fed90fa0a664611e560bbc3ded630eb9e72253e1` | `cfd45c4b4cbef88fd58d7c97f5abc357cb0b1bf7` | **9/9** | 16/20 |

Total **24/24** automated source-structure assertions on exact current `SKILL.md` files read from the live PR. These assert explicit repository-execution warnings, `core.fsmonitor` safety, trusted hook containment, no unsafe shell interpolation, approved scope and/or fail-closed fallback. The positive/negative Git CLI reproduction was performed separately from those text assertions.

Repo Pulse validates individual `OWNER/REPO` identifiers and requires a tool API with discrete arguments, safe local Git containment and an explicit NOT ASSESSED result if it is unavailable. Standup Writer does not attempt local Git status without verified containment. Repo Doctor, previously 16/20 and misleadingly eligible for standalone use, now binds exact repository authorization, uses read-only repository APIs preferentially, forbids unsafe Git status and shell command substitution, and explicitly scopes GitHub CI queries.

## Static rubric and retained evidence

Ten-axis static scores are per current source: Repo Pulse 18/20, Standup Writer 18/20, Repo Doctor 16/20. These are semantic source grades only. The prior complete-tree NVIDIA SkillSpector static PASS for Repo Doctor applied to its **old** tree `c2529253b35b5f90d58500091a0d1efbb1c14c2b`, not the repaired tree. It **must be invalidated** for the current candidate. Repo Pulse and Standup Writer already had pending current-tree scans, so their changed identities do not create new pending slots. **Security frontier expands from 38 to 39 changed first-party packages; 14 earlier matching PASS remain on those original 38, and 25 current changed package trees need pinned new scans. Full first-party 51-package inventory now has 21 matching historical static passes, 25 NOT RUN and 5 engine INCOMPLETE.**

## Acceptance gates

Run pinned NVIDIA SkillSpector v2.12.0 at `c7958a3268d9498644b22edb75d0f051bbc8cbfc` against all final complete package trees with `--no-llm --fail-on-findings --fail-on-incomplete`, retained reports/digests and complete reference analysis. Independently execute actual synthetic-agent host cases: a repo with malicious `core.fsmonitor` and hook metadata, an approved remote-only repo, an unrelated private checkout, a hostile `OWNER/REPO` string, and no trusted local containment. Observe attempted tool calls and file/network effects. Fail on unapproved helper execution or scope expansion. Never silently mark a local checkout clean after skipping it. Owner review and qualified merge of PR #703 are still required before closing #402/#478/#481. No scanner or actual agent-host behavioral PASS is claimed.
