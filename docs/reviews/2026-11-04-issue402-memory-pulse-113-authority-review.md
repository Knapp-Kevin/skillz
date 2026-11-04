# P0 #402 / PR #673: Memory Pulse 1.1.3 private-context authority repair

Date: 2026-11-04. Scope: complete current first-party package, **static source-level review only**. No agent-host behavioral test or NVIDIA SkillSpector scan was run on this changed package.

## Defect and exact correction

The previously proposed Memory Pulse 1.1.2 text included: `Bind: discover the memory-layer project from an operator profile or project governance doc`. A **public memory-news digest** did not authorize inspecting a private operator profile or local governance file. This was a real source-instruction authority defect not addressed by the earlier 16-pulse pass. It conflicts with the repository's one-time public read-only default and issue #402's no-private-access-without-consent requirement.

The 1.1.3 candidate now:
- Defaults to public source research with generic architecture relevance.
- Accepts project-specific comparison only from a redacted user-provided summary or an explicitly user-approved source and read scope for **this** run.
- Forbids implicit operator-profile, host-memory, governance, private-repository and connected-account discovery.
- Makes the trigger description and output heading consistent with optional project context.
- Preserves read-only, evidence-gap, retrieved-content-as-data, secret-egress, and separate recurring-scheduling consent boundaries.

## Complete package fingerprint and rights

| Item | Exact identity |
|---|---|
| Package | `skills/memory-pulse` |
| `SKILL.md` Git blob | `84fe948e761f95d4196efaf80a0ef6add7c01a16` |
| `sources.json` Git blob | `d05ad098fcb822b1af81798cae1321d135f3f042` |
| Full two-file package Git tree | `69d2337cc4d9c0728dfca18d556c7d0b7551057a` |
| Prior package Git tree, historical PASS only | `bc5e32b023a13bdd39e077d05f0a4ad43eb2aba2` |
| First-party root MIT `LICENSE` blob | `023abdb34298b27580d1d303084aca942050585e` |

The Git tree was deterministically reproduced with `git mktree --missing` from these two known Git blob identities. The same method independently produced the **old** package tree exactly equal to the previous pinned tree, so the recorded identity calculation is checkable. The unchanged `sources.json` was fully inspected: it contains public blog, repository, model-paper/search references, not local-file reads or executable sidecars. No dependency installation, untrusted code execution, or sensitive account access was performed.

## Ten-axis current source-semantic review

| Dimension | Score | Source-specific rationale |
|---|---:|---|
| Trigger precision | 2 | Public memory-news requests are explicit; optional user-approved project relevance is non-default |
| Procedure | 2 | Public source collection, gap filling, comparative synthesis and source-output sequence are usable |
| Authority and safety | 2 | No implicit private project discovery; recurrence, private scope, egress, and side effects require separate authority |
| Failure handling | 1 | Missing sources are reported as gaps; no executed host failure handling observed |
| Evidence discipline | 2 | Cites URLs and publication dates, treats community leads as unverified, and never claims unseen checks |
| Dependencies | 2 | Bundled JSON present, parsed and inspected; host search/connector access optional; no runner |
| Portability | 2 | Browser, search or connected read-only source path; generic summary when target/host access missing |
| Differentiation | 2 | Agent-memory-specific source watch with architecture relevance rather than generic vendor headlines |
| Adversarial resilience | 2 | Retrieved instructions cannot authorize private reads, installs, credentials or future schedules |
| Effectiveness design | 1 | Source/trend synthesis design is credible but comparative effectiveness has not been measured |
| **Total** | **18/20** | **Static semantic gate only, with no observed host behavior** |

No source-level hard fail remained in this bounded complete-package examination. The exact package may therefore be recorded **semantic `verified`**, **behavior `not-run`**. Static verification is *not* security acceptance, unchanged-use approval, or real-world model adherence.

## Scanner invalidation and required acceptance

The external pinned NVIDIA SkillSpector v2.12.0 receipt for old package tree `bc5e32b...` **does not transfer** to `69d2337...`. Move this package from 10 matching current-tree passes to the new-scan queue on #673, so the active **34-package** repair frontier becomes **14 matching passes / 20 fresh scans required** (#673: **9 / 7**; #686: **5 / 0**; #703: **0 / 13**). All 34 behavioral runs remain pending and 0 unchanged-use approvals stand.

Before merging: scan the exact new two-file package with registered pin `c7958a3268d9498644b22edb75d0f051bbc8cbfc`, capture complete report/coverage and report hash, run independent synthetic-host cases for unauthorized private discovery, hostile source injection, optional binding, and recurring schedules, then reconcile current main and obtain owner acceptance. Keep issue #402 and #415 open. Do not relabel any old scanner result as current.
