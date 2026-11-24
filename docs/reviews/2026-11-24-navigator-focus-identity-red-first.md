# Effort Allocation Navigator: adversarial focus and identity refinement

Date: 2026-11-24
Target: `skills/authored/effort-allocation-navigator/`
Previous merged version: v0.2.0, PR #914 merge `1946d2d4b52496a269e976c4dacabcada1afcf39`
Candidate version: **v0.3.0**, original first-party MIT, portable.
Review scope: *local source-method behavior and safety of task evidence*,
not independently observed ADHD or human performance.

## Decision and rationale

The current task helper already offers a five-minute voluntary start,
one recommendation plus a credible alternative, mandatory safety and
deadline precedence, and a read-only two-snapshot comparator. However,
two repeat-use failure modes matter to people who find context
switching and re-entry demanding:

**F1, false continuity:** The comparator previously equated matching
task IDs with the same underlying work. A reused ID with different
label or action/milestone type could be reported as `completed`,
`newly_ready` or `resume_candidate` despite missing identity evidence.
A benign rename and genuine ID reuse are indistinguishable from
labels alone; the safe response is lightweight **IDENTITY_REVIEW**,
not an automatic claim of either.

**F2, unnecessary switching:** Even after a user deliberately chose
a viable action, the next planner run could replace it with a nearly
identical higher-ranking task because no explicit chosen-focus input
was modeled. This undermines the ADHD-supportive task-initiation
and re-entry procedure, although a legitimate newly urgent obligation
must still be able to override an older choice.

## Red before repair (independent GitHub Actions evidence)

The 18 original synthetic cases in
`tests/test_focus_identity_adversarial.py` were committed before
production script edits. [PR #915's first offline run
#45445942389](https://github.com/Knapp-Kevin/skillz/actions/runs/45445942389)
ran 148 tests and ended **4 FAIL, 12 ERROR** in the new test module.
The original 130 tests remained preserved. These are *observed
local source-method failures*, not observed user-task failures.

After the bounded script correction, interim
[offline run #45446142605](https://github.com/Knapp-Kevin/skillz/actions/runs/45446142605)
passed **148/148**. The authored source/registry integrity job
at that interim commit failed because the modified package had
not yet been repinned. That failure is a required provenance
gate, not a reason to skip or weaken it. Final exact-HEAD QA
must establish both code behavior and package identity.

## Source repair and challenge matrix

1. **Explicit focus preservation:** Optional `focus_task_id` is
   a current-run, caller-declared selected task. Only an eligible
   action with supported value/effort, no missing predecessors
   or external hold, and score at least 85% of the best candidate
   **in the same protected priority lane** can move to primary.
   This threshold is a provisional heuristic, not calibrated
   user utility or medical guidance. Without focus input the
   legacy decision order is unchanged.
2. **Defensible redirects:** Safety or owner-confirmed imminent
   deadlines outrank lower-lane focus. A blocked, completed,
   missing, unscored or materially poorer-scored chosen task
   returns a categorical `focus_resolution`, never an
   implicit task switch, fabricated completed task or
   silent host write. The *user* retains the decision,
   subject to actual authority restrictions.
3. **Identity review:** When the same ID has a different label
   or type across snapshots, return `identity_review_ids`.
   Exclude affected rows from asserted completion, reopening,
   newly-ready, newly-blocked and resume lists, and separately
   mark state changes as `state_transition_review_ids`.
   A rename is a **possible benign edit**, not proof of
   task recycling. The authorized host can resolve the
   identity with one small clarification, without dumping
   a full backlog or printing private labels.
4. **Keep the existing portable fallback:** Python 3.9+
   standard library, local read-only, original
   `--input` route unchanged, optional separate source
   `--previous` unchanged and still requiring matching
   caller-declared scope IDs plus independent permissions.

| Adversarial challenge | Required safe result | Evidence |
| --- | --- | --- |
| Explicit viable second task, equal score | Preserve chosen focus as primary | Synthetic local test |
| No explicit focus supplied | Same legacy ranking | Synthetic local test |
| New safety obligation / confirmed deadline | Higher priority lane wins | Synthetic local test |
| Blocked, done, missing or unscored focus | Never auto-execute or invent a score | Synthetic local test |
| Explicit but far worse focus | Honest material priority difference | Synthetic local test |
| Recycled ID with new label and claimed DONE | Hold completion under identity review | Synthetic local test |
| Same label but action becomes milestone | Hold cross-snapshot progress | Synthetic local test |
| Legitimate label-only edit | Flag review; do not accuse user or count progress | Synthetic local test |
| Stable unchanged identity | Allow `CALLER_ASSERTED` transitions only | Synthetic local test |
| Private label containing account name | Return ID tokens, never original labels | Synthetic local test |
| User requests an unrelated third choice | Default remains one primary and one alternative | Preserved 130 cases |
| Opted-out buyer action from optional sales handoff | No outreach permission, task writes or sends | Preserved first-party contracts |

## Existing Skillz engine used, not replaced

- `engine/refinement/README.md` red-first baseline, bounded
  repair, near-negative, false-green, preservation and
  integration evidence.
- `engine/skills/skill-eval/SKILL.md` and
  `engine/skills/skill-audit/SKILL.md` for full-package
  quality, security/authority boundaries, missing proof and
  exact source fingerprint.
- `engine/skills/skill-forge/SKILL.md`, existing authored
  skills registry QA and offline planner CI for **real
  first-party source maintenance**, not generated scaffolds.
- `engine/packs/feedback-decision-tree.md`: canonical
  protections against false completion and unwarranted task
  switching are distinct from local user preferences for
  brevity, start duration and alternative explanations.
- `engine/builder/acceptance.md` requires a useful
  task outcome, controlled choices, true stop conditions
  and negative paths. Builder CREATE/COMPOSE is not invoked
  for this existing 17-file standalone package.
- The existing `engine/refinement/check_case.py` validates
  the separate fictional source-bound maintainer receipt
  `docs/reviews/fixtures/2026-11-24-navigator-focus-identity-refinement-case.json`.
  This **structural** check does not verify actual model behavior.

## Version and release gate

A new optional input with visible decision semantics is a
**minor capability release**: `0.2.0 → 0.3.0`, not a
mechanical patch increment per PR. Version `0.3.0` remains
pre-1.0; it makes no stable-host interop or measured outcome
claim. Preserve v0.2.0 source identities in history.

Package is expected to contain **17 original files**:
prior 15 plus an adversarial test module and fictional focus
input example. No personal task snapshots, diagnosis,
persistent memory, telemetry, external API, scheduler, CRM
write or automatic task actions are introduced.

**Stop/merge gates:** final complete tree and entrypoint
Git fingerprints in all three registry records, 148/148
synthetic planner tests and existing authoring checks,
the original engine receipt validation plus the new case,
clean independent exact-head review and actual PR merge
read back from `main`. Do not promote
`needs-re-review` or `behavioral_validation: not-run`
because source tests pass. Host-based multi-turn consumer
trials and actual task outcomes remain **NOT_RUN**.
