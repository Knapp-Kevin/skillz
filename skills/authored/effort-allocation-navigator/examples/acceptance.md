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
