# Effort Allocation Navigator: adversarial ADHD-supportive release review

Date: 2026-11-24
Authority: owner-requested bounded Skillz repository maintenance
Baseline: Skillz main `03a5591999a09c47f1a734b2222c58a8d2166877`
Primary target: first-party `effort-allocation-navigator`
Release candidate: **v0.2.0** (15 files, original MIT)
Adjacent safeguarded interfaces: first-party Sandler and MEDDPICC
remain **v0.2.0**, five files each, with updated exact fingerprints.

## Why this is a material improvement

The merged 0.1.0 task skill already provided an unusually careful
dependency-aware bounded choice, mandatory safety and deadlines,
two genuinely useful actions, private opt-in preferences, and a
Python-standard-library read-only graph helper. Its prior synthetic
qualification was 101/101 pass; no independent host, user-task
completion or ADHD-related clinical outcome was verified.

The next user-visible gap was *activation*, not merely ranking.
A recommendation to spend 25 minutes on a large task can remain
difficult to begin; an unchanged snapshot can be misconstrued as
a personal failure; a lost conversation can force the user to
re-plan instead of resuming. The helper also lacked a way to
compare separately supplied snapshots. This release adds a
bounded, source-safe repeat-use comparator AND micro-start
support. These are new capabilities, not editorial patch edits.

## Public context and evidence limitation

Public CHADD practical task-management material discusses smaller
behaviorally actionable chunks, external planning cues and
alternative ways to recover focus:
- [CHADD: Evidence-Based Coaching for Adult ADHD](https://chadd.org/adhd-news/adhd-news-adults/attention-monthly-evidence-based-coaching-for-adult-adhd/)
- [CHADD: Time Management and ADHD](https://chadd.org/for-adults/time-management-and-adhd-to-do-lists/)
- [CHADD: Workplace strategies](https://chadd.org/for-adults/succeeding-in-the-workplace/)
- [NHS inform: work and education](https://www.nhsinform.scot/illnesses-and-conditions/adhd/managing-adhd-symptoms-in-work-and-education)

The ideas motivate **accessible interface hypotheses**,
not diagnoses, medical treatment, precise personal effectiveness
estimates, proof of symptom improvement, or a requirement to
disclose any health condition. The task skill does not treat
ADHD or prescribe medical interventions. The actual behavioral
effect for any user remains NOT_OBSERVED.

## Existing Skillz components actually reused

- `engine/refinement/README.md`:
  BASELINE → diagnosis → narrow modification → adversarial
  false-green/negative/preservation → decision → actual merge
- `engine/skills/skill-forge/SKILL.md`: complete original package,
  conservative versioning and first-party maintainer authority
- `engine/skills/skill-eval/SKILL.md` and
  `engine/skills/skill-audit/SKILL.md`: source and authority review,
  independent from human outcome claims
- `engine/packs/feedback-decision-tree.md`:
  canonical safe activation/identity fixes are separate from
  individual start-length, layout or motivational preferences
- `engine/builder/acceptance.md`: actual usable first action,
  source refusal, protected successful paths and false-green cases
- `engine/refinement/check_case.py`: the existing structural
  validator of the source-bound fictional adversarial maintenance
  case in `docs/reviews/fixtures/`. It does **not** independently
  inspect GitHub source or assert model/medical efficacy.

No new always-on agent, skill engine, scheduled reminder, CRM,
clinical intake, source-observation service, task database, or
cross-user profile is introduced.

## Independent red-first findings

**A1 (activation, high use value):** The prior helper offered
up to a 25-minute slice, with no deterministic five-minute start
cue. An eligible 90-minute task could be dismissed by a
two-minute user even though a tiny safe first move was feasible.

**A2 (re-entry, high use value):** Repeated unchanged task state
had no explicit voluntary resume marker. The skill must not
interpret a stalled-looking external list as diagnosis, blame,
low motivation or a failed streak.

**A3 (source scope, high trust risk):** Two separately supplied
snapshots with coincidentally identical task IDs could be
compared even when they represented different projects. This
could yield false completion, reopening and blocker statistics.

**A4 (authority false green):** Proposing a sales follow-up or
marking a readiness gate as conditionally supported cannot
authorize external customer contact, a proposal send, task
mutation, signature or reminder.

### Red evidence, then implementation

The new `tests/test_engagement_adversarial.py` was committed
**before** the implementation. [Actions run
#45440239015](https://github.com/Knapp-Kevin/skillz/actions/runs/45440239015)
failed with **9 errors in the new cases**, while previously
existing tests remained protected. These were actual local
Python source-method errors, not observed human task failures.

Corrections:
- `plan()` now conservatively decorates eligible choices with
  `first_microstep_minutes`, `TIMEBOX_NOT_COMPLETION`
  and a `PICK_NEXT_VISIBLE_ACTION` re-entry cue.
  Default five-minute start, bounded by actual capacity,
  declared task effort and an optional current-run
  `start_window_minutes` 2–10. These are estimates or
  suggested windows, never enforced timers or task completion.
- A concise user-visible contract asks for a task-specific
  verb, object, observable endpoint, at most one useful
  alternative and one-line re-entry breadcrumb. No diagnosis
  or guilt-based push messages.
- The optional `compare_snapshots()` requires both snapshots
  declare **the same non-sensitive scope_id**, and otherwise
  refuses the comparison. Matching scope is a *caller assertion*,
  not an authenticated viewer or source identity.
- Unchanged `doing` state can emit a provisional
  `resume_candidate_ids` marker, never blame or fake
  progress. A removed task stays `REMOVED_UNRECONCILED`;
  a `done` state is a caller claim.
- All features remain read-only; old snapshot access must be
  authorized separately by the host before invocation.

After the source repair, [Actions run
#45440863551](https://github.com/Knapp-Kevin/skillz/actions/runs/45440863551)
ran **130/130 synthetic planner tests PASS** (101 historical
tests plus 15 initial continuity and 14 new engagement cases).
The same head's authored registry integrity run failed for a
**known stale source fingerprint**, which is not a waiver:
the package, index and provenance pins must be reconciled
and the final exact-head run repeated.

## Preservation and acceptance matrix

| Case | Required conclusion | Evidence tier |
| --- | --- | --- |
| Two independent legitimate tasks | One recommended, one different useful alternative | Offline synthetic |
| Low-capacity 2-minute day, large required task | Two-minute first step, not false full-task fit | Offline synthetic |
| User selects 3-minute starting window | Local preference applies this run; default unchanged on next | Offline synthetic |
| ADHD is not disclosed | Same accessible default, no diagnosis or health data collected | Source contract |
| Priority safety obligation vs tiny optional task | Safety lane preserved; short first step may apply to safety task | Offline synthetic |
| Identical day-after-day task state | No fabricated productivity or moral conclusion; optional resume cue | Offline synthetic |
| Earlier snapshot from other namespace | Refuse cross-scope change history | Offline synthetic |
| Snapshot missing old permission | Host must HOLD without disclosing cached IDs or counts | Source contract |
| Removed task vs claimed DONE | Removal is unreconciled, not completed | Offline synthetic |
| Sandler/MEDDPICC propose external action | Task remains permission BLOCKED, not implicitly authorized | Static interface scenarios |
| Multiple turns and user interrupts | Re-entry breadcrumb from actual context; no imagined previous step | Source contract |

Both actual source and test runner remain Python 3.9+ stdlib
and no network/storage/write operations. There is no independent
agent-host run using real task context; no personal ADHD
outcome measurement, productivity metric or actual preference
persistence is claimed.

## Release and QA obligations

The navigator's `0.2.0` is a **single deliberate minor
capability release** relative to its first-party `0.1.0`;
the new comparator and activation flow materially expand
user-visible behavior. Existing Sandler and MEDDPICC
v0.2.0 packages only receive consent-boundary clarification,
so they do not receive arbitrary patch increments.
Changed source fingerprints remain mandatory even without
new SemVer identities.

Package fingerprints, **subject to final exact-head QA**:

| Package | Changed entrypoint Git SHA | Complete package tree | Count |
| --- | --- | --- | --- |
| Navigator v0.2.0 | `bc3710ae61508e24860e83d8023e66aab2438050` | `1de24c983592388706d89361ae2cf0706b789624` | 15 |
| Sandler v0.2.0 | `5d844ac0e8d4f733f904cafa63966dd33ff4a032` | `770c367d10cd7bb52e0fb0fb1b24ed95a57a7b25` | 5 |
| MEDDPICC v0.2.0 | `e0b293b96459b01db4535adc0a917225ce2cabb9` | `6980f6e74f8a519e7d93347618f04311d60ef026` | 5 |

**Completion standard:** both existing authored QA and
navigator's offline source+fixture+engine receipt checks
PASS at exact current PR head; no unresolved material
independent reviewer findings; PR actually merged and
the three source versions/trees reverified on main.

Both published first-party packages and candidate still
retain `needs-re-review` and `behavioral_validation:
not-run` until separately proven. A static QA result
is not real world user engagement.
