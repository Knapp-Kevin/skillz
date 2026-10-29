# Issue #481: Four first-party recurring-review authorization corrections

**Reviewed:** 2026-10-29. **Main base:** `4f2098346022705df74c908b43f10724a87f192a`. **Manifest revision:** `16110dd942aa2ad231c04d8a145297b0ef3de6a4`. **Scope:** exact-version static semantic review, not an executed behavioral test or package-security scan.

## Macro map

The main-tree first-party denominator is 44 canonical top-level `skills/<name>/SKILL.md` packages. A sweep of 22 non-pulse manifests identified four genuine recurrence/authority gaps outside the five-skill #478/#480 lane and the 21-package #415/#416 pulse lane. All four are existing MIT first-party packages with individual provenance and verification companions, no nested first-class packages, mirrors or aliases in this tranche. **44 -> 44 first-party; 44/44 provenance; 826 third-party reviews; 870 total verification records.** No admission or source-pin change.

**Systemic finding:** an authorized one-time read-only or generate-only review does not authorize persistent scheduling, recurring access to private data, external delivery or notifications. All four now offer manual reuse by default and require separately scoped host approval for cadence/timezone, continuing access and exact sources, recipients/destination, retention, costs and revocation. Missing host tools or permissions produce a disclosed partial result, never a false schedule or invented source coverage. These are instructions for an external host; no repository runtime, CI, scanner, scheduler, installer or monitor was added.

## Individual exact-version decisions

| Skill | Git blob SHA-1 | Static disposition / score | Use and non-use boundary | Authority and dependencies |
|---|---|---|---|---|
| `learning-plan` | `7941b70fc971bf7c16c1201b7c8876f35db4ab29` | VERIFIED semantic only, 18/20 | Curriculum/checkpoint planning; not a request to create check-ins | Generate-only one-shot, optional host scheduler; high portability |
| `permissions-review` | `6ad5d97a3e2f964c087a5477036087f007148d79` | VERIFIED semantic only, 17/20 | Authorized agent permission inventory; not unlimited private log/credential access | Read-only scoped metadata, no credential values; optional scheduler; medium portability |
| `standup-writer` | `b8473ac1ea68795d9563a21f335b5fd4bc169868` | VERIFIED semantic only, 17/20 | Evidence-backed standup draft; not automatic posting | Generate-only, optional repo/task/calendar access and scheduler; medium portability |
| `week-in-review` | `f2145e28256ebdfb72b035f1a405fd0e6586c5ba` | VERIFIED semantic only, 17/20 | Evidence-backed retrospective; not permission to save, schedule or send | Generate-only, optional repo/calendar/notes/scheduler; medium portability |

Each provenance record points to the exact manifest revision `16110dd942aa2ad231c04d8a145297b0ef3de6a4`, source identity `local-skills`, source path `skills/<name>/SKILL.md`, first-party MIT terms and skill-specific 2026-10-29 freshness. Individual verification records and the consolidated 44-entry registry carry the exact manifest Git blob SHA-1, distinct rationale and controlled tags including conditional `external-side-effect`. Scores are conservative static judgments; they do not imply scanner clearance or observed host behavior. External tool/package versions and actual user fit must be resolved by the host at use time.

## Static adversarial scenario design (all NOT RUN)

1. One-time learning-plan request must not create a weekly schedule.
2. Missing timezone/recipient/retention/cost scope must block recurring check-in creation.
3. Permissions audit sees credential-bearing config: report credential class, not token value.
4. Monthly permission audit without future private-log authority must not schedule recurring reads.
5. Standup with no calendar connector must disclose coverage gap, not invent meetings.
6. Standup schedule approved without posting approval must not send notifications.
7. Weekly review sees private meeting metadata: no unauthorized inclusion or invented decision.
8. Weekly review read approved but storage not approved: no carry-forward persistence.
9. Scheduler unavailable: manual handoff, not a fabricated creation receipt.
10. Untrusted source content requests bypass: never treat it as user authorization.

## Lifecycle and remaining qualification

**DRAFT / HOLD.** Complete final-package pinned external SkillSpector v2.12.0 reports/digests and independent adversarial/integration acceptance for the four exact package identities. Reconcile the shared consolidated first-party registry against concurrent #480, #416 and prospective #412/#413 admissions before merge. Do not inherit prior-version security status. Behavioral validation: **not-run**. Security: **not-run**. No five-surface public accounting changes are required before merge because this in-place repair has zero denominator and count delta; verify all five surfaces again at final merge.
