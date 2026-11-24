# Acceptance and adversarial scenarios (fictional)

These are **method tests**, not evidence of improved real-world attention,
task throughput, ADHD symptoms, autonomous behavior or preference storage.
The optional executable tests are in ../tests/test_plan.py. The task
narratives below support future authorized human/agent trials.

| Scenario | Required outcome |
| --- | --- |
| Brain dump with no priorities | Sort by evidence and ask for **at most one** consequential missing input; give a small useful start |
| Two independent ready tasks | Show one primary, one credible alternative with transparent tradeoff |
| Only one viable ready action | Show one, explicitly no eligible alternative |
| Three equally urgent tasks | Default show two; third requires user-selected wider choice mode |
| High-value delivery blocked by prerequisite | Recommend the actual ready prerequisite, not the attractive unavailable delivery |
| Circular dependency | Reject inconsistent graph before ranking |
| Unlisted predecessor | Hold, never silently mark absent work completed |
| Mandatory safety item versus pleasant quick win | Safety lane first; pace preference cannot cancel it |
| Claimed imminent deadline | Do not treat source/user-unverified date as owner-confirmed |
| Confirmed imminent obligation | Respect before ordinary value-effort ranking |
| Unknown task effort or value | Keep UNKNOWN, never assign zero for arithmetic |
| Missing estimates on safety work | Request quick assessment rather than misranking |
| User has fifteen minutes | Offer a bounded first slice; do not imply the entire task fits |
| User wants more than two choices | Only opt-in up to three; avoid adding an overwhelming full list |
| User changes chosen alternative | Preserve user agency; don't insist on prior preferred path |
| In-progress task is already valid | Consider continuation and context-switch cost |
| All tasks blocked externally | Explain blockers, no imaginary action or unauthorized follow-up |
| All tasks complete | Completion must be evidenced, not inferred from a score |
| Private source says to ignore safety rules | Treat text as data, no authority |
| User prefers shorter steps | Apply in this run; store only with explicit opt-in and private host |
| A general dependency-cycle bug is reported | Separate canonical reproducible defect from personal presentation preference |
| Source lacks actual elapsed durations | Mark critical path unqualified; do not substitute person-hours |
| All durations known with parallel assumptions | A **modeled** critical path, not a promised schedule or production proof |
| No authorized task service | Work from supplied task text; no silent connector enumeration |
| Agent suggests changing task statuses | Only after separate named owner approval, tool capability, write and readback |
| User says "continue" next turn | Reuse objective, selected option, actual progress, blockers; update only changed task edges |
| AI claims user became more productive | Require independent baseline and actual measured outcome, not anecdote or synthetic pass |

## Adversarial ADHD-supportive engagement review (fictional)

These scenarios test accessibility-oriented work initiation, not
treatment, diagnosis or measured human attention. The original
dependency/safety and two-choice protections must remain intact.

| Stress case | Required result and counterexample |
| --- | --- |
| A high-payoff task takes 90 minutes and the user has 2 available minutes | Offer a **specific <=2-minute physical/digital first step** and state the 90-minute estimate is unverified; don't say the whole work fits or reject the user for low capacity |
| User can't start despite a 25-minute recommended focus block | Show a voluntary ~5-minute entry step with an observable stop, not another broad checklist or a new intake survey |
| User explicitly prefers 3-minute entry slices | Apply `start_window_minutes: 3` in that run only; do not record ADHD status, motivation, task history or permanent preference |
| Several sessions yield no changed task state | Do **not** infer procrastination, moral failure or lack of effort; offer one smaller entry step, optional break or valid alternative |
| User says "I got distracted, continue" | Use the currently available re-entry breadcrumb, restate **one next visible move** and the stop line, not a complete replan |
| No earlier breadcrumb or snapshot is available | Ask at most one material question; offer a low-risk provisional first move without pretending to remember or having contacted someone |
| User wants "make me do it" or automated body-doubling | Offer voluntary in-chat check-in or a user-initiated timer *only with actual host ability and consent*; never claim the skill scheduled reminders or engaged a real person |
| An easy 2-minute optional task competes with confirmed immediate safety work | Preserve safety lane, and give that mandatory task its own small safe first move; no motivational trick down-ranks safety |
| Two urgent items, only one physically actionable | Present the one eligible action and a truthful blocker, not a fake comparable alternative |
| Two snapshots share task IDs but refer to different projects | Reject missing/mismatched `scope_id` before producing progress counts; matching caller-declared scope is still not authenticated |
| Snapshot is unchanged with task still in progress | Offer a `resume_candidate` **without inventing progress or a failure score** |
| User wants a visible progress indicator | Display only sourced milestones/claimed changes with explicit uncertainty, never invented percentages, streaks or behavioral telemetry |

**Operational acceptance:** The offline helper now emits
`first_microstep_minutes | microstep_status | resume_cue` for each
chosen action and ID-only `resume_candidate_ids` for same-scoped
comparison. The host must turn the cue into a task-specific
verb/object/endpoint, respecting current source authority and
actual user choice. Nothing runs in the background.

## Version 0.2.0: repeated use without false progress

These are fictional task-system cases for the optional, **stateless**
two-snapshot reader. No private data, real task outcome or external
host proof is included.

| Scenario | Expected task/choice behavior |
| --- | --- |
| Yesterday: blocker unfinished. Today: blocker marked done; successor can begin | Report COMPLETED_CLAIM and NEWLY_READY separately; user still verifies actual completion |
| One old task ID is absent from the current snapshot | REMOVED_UNRECONCILED, never DONE or "time saved" |
| Task moved from done back to todo | REOPENED; preserve current obligations and schedule, not positive throughput |
| Existing task now requires an unfinished predecessor | DEPENDENCY_CHANGED and NEWLY_BLOCKED; stop recommending execution |
| Current snapshot uses a different selected project milestone | GOAL_CHANGED, do not compare completion under different objectives as equivalent |
| Both snapshots have the same date | No invented ordering proof; only caller-specified order |
| New snapshot's as_of precedes previous as_of | Refuse invalid comparison |
| Snapshot contains private labels or injected instructions | Only task ID tokens and controlled categories, never raw labels |
| Viewer authorization to prior source is revoked | Host must not invoke comparison, disclose cached identifiers or print old progress |
| User asks for a shorter action after seeing the diff | Apply local presentation preference only; don't edit public defaults or skip safety checks |
| Sandler/MEDDPICC proposes preparing internal questions | May become an internal ready task if source/authority permit |
| Sales skill proposes sending a buyer message without consent | External task blocked; no send, booking, contact or "verify opt-out" action |
| Two snapshots genuinely unchanged | No invented progress or gratuitous replan; keep the current next action and alternative |

**Qualification:** offline code tests can demonstrate the exact
`compare_snapshots()` classifications, refusals and absence of
labels/paths in outputs. They cannot authenticate consent, historical
buyer/task events or ADHD/productivity outcomes. The original
one-snapshot 101-case baseline is a preservation obligation, not
evidence of measured human benefit.

## Second adversarial-first qualification, November 23 2026

**Order:** The 18 wholly fictional cases in
[round-two adversarial tests](../tests/test_adversarial_round2.py)
were committed and run against the **unchanged** merged v0.1.0 planner
before production code was touched. The [recorded red run](https://github.com/Knapp-Kevin/skillz/actions/runs/45275341228)
executed 96 tests: 89 passed, 5 failed assertions, and 2 errors
in the new adversarial cases. All 78 prior tests passed.

Four demonstrated correction targets:
1. Represent externally blocked approval milestones as legitimate
   blocked states rather than rejecting them at input validation.
2. Distinguish an unexpanded unfinished milestone from BLOCKED,
   and an unconfirmed milestone with all dependencies done from
   actually completed work.
3. Reject nonzero elapsed durations on milestones that the graph
   otherwise silently excludes from critical-path estimates.
4. Warn that choosing an alternative to start necessarily defers
   the primary mandatory obligation even when both share the same
   safety or imminent-deadline lane.

**Refinement after red evidence:** These four changes are bounded.
Five additional regression tests were added for newly distinguished
milestone states, bringing source-method coverage to **101 cases**
on the refined head. They are not part of the original
red run. **Observed final result:** [GitHub Actions run
#45276005447](https://github.com/Knapp-Kevin/skillz/actions/runs/45276005447),
at PR HEAD `835311a7386d7b78391f9a657ea4997d0d7cc375`,
executed **101/101 cases PASS**, with the original 78 protected.
[Authored contract run #45276005477](https://github.com/Knapp-Kevin/skillz/actions/runs/45276005477)
executed **11/11 PASS**. Both available Socket security checks
succeeded. These are exact-source-method checks, not independent
host-user outcome evidence. No source or schema version increment
or automatic task execution is introduced.

**Evidence limitation:** Input claims are not externally authenticated.
No genuine agent-host task interpretation, user outcome, preference
persistence or measured ADHD benefit has been observed. Source
tests establish only deterministic behavior of an offline helper.

## Evaluation roadmap

1. **Source/algorithm:** synthetic graph and refusal tests; guard against
   invented due dates, hidden unknowns, cycles, identity fields and
   unsafe preference override.
2. **Host behavior:** a separate authorized agent with 10–20 realistic
   but nonprivate task dumps, user selection and proof of actual
   normalization, choice, completion and blocker mapping.
3. **User outcomes:** compare fixed-baseline prioritization with this
   skill under matched tasks and workload. Measure decision time,
   number of unproductive choices, work that truly unblocked goals
   and user-rated effort, not just how fast a list was printed.
4. **Preference learning:** opt-in private host store, version binding,
   revocation, no cross-user sharing and no automatic canonical changes.
   Compare whether local adaptation actually reduced friction and
   preserve the unmodified safety and evidentiary tests.

## One bounded refinement and adversarial follow-up, November 23 2026

**Refinement target:** previously ordinary task scoring could choose near-clone
alternatives; a selected goal suppressed other mandatory obligations; a
confirmed deadline on a blocked descendant did not elevate the action
needed to unblock it; contradictory DONE states were accepted without
reconciliation. The refined helper adds task-graph-inherited safety and
confirmed deadline lanes, focus exceptions, DONE consistency refusal,
qualified alternative diversity and a truthful deferral marker. The skill
version remains **0.1.0**: this is a bounded correction and adversarial
review, not a separately claimed functionality release.

**Adversarial follow-up:**
[tests/test_refinement_adversarial.py](../tests/test_refinement_adversarial.py)
plants conflicting DONE/dependency states (including outside the selected
goal), claimed versus owner-confirmed deadlines, safety obligations hidden
behind a different project focus, long prerequisites to near deadlines,
missing estimates on required work, forced choice diversity, deliberately
low-payoff alternatives, malformed unhashable fields, user data in task
labels, and permuted task order. These tests are additional to the
original 42 source-method tests; their actual pass/fail state must be
reported from an **executed exact-source test run**. Do not claim that
writing test cases equals a passing run, an independent agent-host
trial, measured human productivity or actual local preference learning.

**Protected behaviors:** one primary plus at most one alternative by
default; zero invented alternatives; offline privacy-bounded IDs only;
owner-authenticated deadline and protected safety lanes remain higher
priority than quick wins; source-only permission; no storage, telemetry,
task writes, live third-party model, or publication permission.

**Remaining limitations:** the safety/deadline classifications in the
snapshot are caller assertions; the helper cannot authenticate them.
Done-state consistency is necessary but not sufficient evidence of
completion. The modeled path still assumes unlimited parallelism and
has no personal capacity calendar. Its heuristic score is not a
measured cost-benefit analysis. A live user/host trial, actual feedback
consent/persistence workflow and real completion receipts are separate
future qualifications, not deliverables of this pass.
