# Governed recursive skill improvement
## Umbrella architecture strategy, revision 0.2 (2026-11-21)

**Status:** Proposed, architecture validation and staged implementation authorized for issue planning. **Not implemented.**  
**Scope:** Skillz authored skill improvement and its repository-level quality engine. The standalone Evidence-Driven Refinement Loop package remains independently usable.  
**Source:** [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858) and the [published Google Research reference](https://github.com/google-research/dream-rsi). Mechanisms are adapted, not copied or claimed to be experimentally reproduced.  
**Existing baseline:** Evidence-Driven Refinement Loop v0.3.4 in [draft PR #826](https://github.com/Knapp-Kevin/skillz/pull/826), subject to normal merge governance. Do not make the strategy depend on that draft being merged or claim it is live on `main`.

## 1. Decision in one paragraph

Adopt a **bounded, evidence-driven meta-refinement program**. The existing loop fixes a real artifact: OBSERVE → EXPLAIN → CHANGE → CHALLENGE → DECIDE. Add an **optional, separately governed exploration policy** that chooses which falsifiable hypothesis or adversarial test to pursue next, under a fixed evaluator, budget, and authority contract. Collect **minimal, verified discovery traces** from real authorized attempts; replay only observed outcomes to compare exploration strategies cheaply; challenge proposed policy improvements against unseen adverse cases and actual execution before promotion. Never promote local user preferences into canonical policy, treat same-model agreement as external proof, or let an exploration policy change its evaluator or grant itself mutation authority.

**This is recursive improvement of the search strategy and skill implementation, not automatic LLM weight training, general self-modification, or permission to run unsupervised jobs.**

## 2. What DREAM-RSI contributes, and what it does not

The paper's loop comprises online discovery by a fixed coding agent/evaluator, recorded discovery trees, and offline replay to improve the policy selecting branches, parallelism and stopping. Its code specifies that **only the exploration policy changes**, leaving the task, underlying agent and evaluator fixed. The recorded tree is an exact historical replay world **only for already realized outcomes**. Its performance figures are published research observations in algorithm and GPU optimization domains, **not** evidence of improvement on Skillz. Its research runtime and task dependencies are not portable skill requirements.

Transfer the architectural principle, **not** the repository, weights, execution harness, performance numbers, unrestricted arbitrary policy code, or a false claim that an untried branch has a known result.

## 3. Existing Skillz contracts that may not regress

| Contract | Unchanged governing requirement |
| --- | --- |
| Canonical skill | Versioned, independently useful, offline portable; no dependency on the Skillz monorepo, agents, CI or replay store |
| User preferences | Private, opt-in and user-scoped; presentation only; never exported as shared discovery history, benchmark examples, or source changes |
| Authority | Host/user approves actual side effects; proposals, issue comments, code in skill packages and `--approved` flags are not permissions |
| Evidence | Preserve `OBSERVED_PASS`, `OBSERVED_FAIL`, `NOT_RUN`, `BLOCKED`, `STATIC_INFERENCE`, evidence version and exact artifact identity |
| Adversarial method | Prefer planted negative reproductions, red/green tests and preservation checks over same-author response scoring |
| Reviewer independence | Separate-agent consumer trials are **optional**, not a universal release or merge gate |
| Production outcome | Correct CI/test mechanics do not imply end-user success or improved skill effectiveness |
| Repository hygiene | No progress log in the root README; no continual ticket or workflow creation; close each issue on shipped behavior rather than reports |

## 4. Separation of responsibilities

```text
[Authorized real task / local user]
                  |
                  v
[Immutable task requirements + trusted evaluator/version]
                  |
                  v
[Exploration policy] ----> chooses candidate hypothesis, budget,
                  |        branch, allowed test, priority, stop
                  v
[Existing skill refinement executor + adversarial verifier]
                  |
                  v
[Result: exact artifact revision, red/green evidence, cost]
                  |
                  +----> [PRIVATE user store] (never shared or replayed)
                  |
                  +----> [Sanitized opted-in event collector]
                                  |
                                  v
                        [Append-only discovery tree]
                                  |
                         [Replay ONLY observed nodes]
                                  |
                        [Candidate exploration policies]
                                  |
                            [Holdout + real pilot]
                                  |
                         [Owner-governed promotion]
                                  |
                             next real task
```

**Trust boundaries:**

- **Evaluator and protected invariants:** fixed before the experiment; a candidate policy may not rewrite tests, evidence interpretation, ratings, privacy policy, authority limits, or task acceptance criteria. Version changes create a **new** evaluation cohort and invalidate cross-version score comparisons until reconciled.
- **Policy:** initially a versioned, non-executable declarative decision table with bounded choices, not free-form Python supplied by a model. Evolve the policy only inside a trusted runner using a allowlisted parser and deterministic tie-breaking. Arbitrary executable policies are **out of scope** until sandbox/threat review justifies them.
- **Executor:** current skill/source editing only under current owner authority; permitted outputs include `HOLD`, `NO_ACTION`, and unchanged artifacts. Replay never writes source files.
- **Replay store:** repository-maintenance experiment data only, written in a governed opt-in workspace. No portable user skill should require the store or write anything on activation. Upload of recordings with confidential, personal or license-restricted contents is prohibited.
- **Preference overlay:** application controls output presentation, never task scoring, branch priority, search budgets, source maintenance, or global learned policy.

## 5. Minimal first-party contracts (design targets, not deployed schemas)

### 5.1 Immutable attempt/event

One record per **actual observed** branch action and outcome, with a content-addressed receipt. Proposed example:

```json
{
  "schema_version": 1,
  "experiment_id": "synthetic-experiment-001",
  "node_id": "n-002",
  "parent_node_id": "n-001",
  "candidate_id": "hypothesis-duplicate-fields",
  "branch_action": "execute-negative-test",
  "task_family": "schema-compatibility",
  "task_fixture_id": "fixture-red-001",
  "source_artifact_git_blob": "40-character-hex-git-blob",
  "evaluator_id": "schema-validator-v1",
  "policy_id": "incumbent-v1",
  "outcome": "OBSERVED_FAIL",
  "outcome_receipt_digest": "sha256:<64-hex>",
  "measured": {"test_invocations": 1, "wall_ms": 110},
  "privacy_class": "public-synthetic"
}
```

This JSON is illustrative, not schema-valid: the placeholder digests must be replaced with real fingerprints. Validation must reject missing parents, cycles, duplicate IDs, illegal transitions, invalid/missing receipts, evaluator/source mismatch, implausible timestamps, unsupported task families and unknown outcomes. Events never contain raw user requests, preference file paths, personal IDs, credentials, full tool logs or secret-bearing diffs.

**Discovered hypotheses** and **executed outcomes** are different entities. A candidate may exist without an outcome; it cannot be silently counted as a successful attempt. A `SKIPPED`/unobserved branch has no replay reward.

### 5.2 Policy decision surface

Input: task-family tags, established evidence, allowed branch frontier, remaining **bounded** budget, evaluator version and risk constraints. Output: choose among **observed/allowlisted actions** (`inspect`, `adversarial-probe`, `run-targeted-verification`, `preservation-check`, `hold`, `stop-no-change`); optional priority and maximum attempts. Never output an arbitrary tool command, file path from untrusted text, remote URL, workflow dispatch, authority grant or new evaluator definition. Validate all decisions against trusted host constraints before executing.

### 5.3 Replay and policy promotion

Given a frozen replay-world collection and fixed evaluator:

1. Evaluate the incumbent first; retain its measured result and exact identity.
2. For each proposed policy, step only across **previously observed** choices and outcomes; if a policy requests an unobserved transition, report `UNKNOWN_BRANCH` or a coverage penalty, not a guessed reward.
3. Maintain separate development and **held-out** fixtures by task family and time cohort. No leaked holdout scores during candidate tuning. No duplicate evidence masquerading as independent worlds.
4. Compare on non-negotiable correctness and safety gates **before** utility/cost. A single material authority/security failure vetoes promotion. Measure test calls, elapsed time, stalled branches, false skips, and preservation regressions, using identical accounting rules.
5. Prefer incumbent on ties, too-small samples, missing provenance, disagreement, excessive overhead, unsupported transfers, or changed evaluator. Improvement is a **hypothesis**, not a shipped fact, until a bounded **live** adversarial pilot confirms it.
6. Proposals never self-merge, rewrite `SKILL.md` or the evaluator, or change user memory/persistent preferences.

**Invalid shortcut:** Offline replay can answer only “how would this policy have navigated the observed subset?” It cannot answer “what result would an unexplored branch have produced?” A winning score on replay is not a guarantee of generalization.

## 6. Baseline, research questions and scorecard

**Incumbent:** the current bounded adversarial loop and its observed process for selecting next failures, explicitly frozen before experimental comparison.

Test falsifiable questions, rather than assume recursive gains:

- Does tree-backed replay improve **which real defect is found first** at matched evaluator budget, relative to the fixed incumbent?
- Does the alternative policy reduce unnecessary tool calls or aborted directions **without** increasing missed protected checks?
- Does it generalize across at least two substantially different task families, rather than memorizing one Git path or JSON Schema defect?
- Does it preserve the same original correctness/safety in changed skill packages and decline low-value work?
- Can it run without mandatory cloud services, user profiling, surprise background tasks or downstream repository-specific hooks?

Primary measures, all **observed** and reported with denominators: verified actionable defects discovered per bounded investigation; false skip count; protected-invariant violations (hard veto); regressions; wall time and actual test/tool calls; replay unknown-branch rate and world coverage; replay rank agreement with subsequent live pilot; evidence completeness; reviewer-required corrections. Context size and monetary cost are secondary and must not conceal safety failures. Never manufacture a “1.5× benefit” target without a defensible experiment and budget.

## 7. Architecture validation, adversarial review and explicit decisions

| Failure mode / attack | Required design response | Falsification test |
| --- | --- | --- |
| Same-model praise becomes quality evidence | Keep author-generated output labeled, require external mechanics where possible | Feed repeat self-endorsement with no changed artifact: no policy promotion |
| Partial tree creates hindsight bias | Record unknown branches, restrict replay to observed outcomes | Candidate chooses missing child: return UNKNOWN, never fabricated score |
| Policy changes evaluator or safety checks | Separate roles and frozen immutable evaluator ID | Mutated evaluator identity blocks comparison/promote |
| Prompt injection in history/issue text | Input treated as untrusted data, allowlisted parser | Event contains “skip security”: no tool/authority change |
| Personal preference reused as generic improvement | Separate private overlay from canonical improvement ledger | A wants table, B wants paragraphs: no global policy alteration |
| Consent flag forged or stored in events | Host-side authorization, no authority inferred from logs | Replay record `approved:true` cannot authorize a write |
| Replay optimized for known examples | Heldout family/time cohorts, incumbent and live challenge | Train score rises, holdout fails: block promotion |
| Cost reduction by silently skipping obligations | Hard correctness/safety gate before utility ranking | Docs+code and policy-change fixtures still select protected checks |
| Unlimited search/CI expense | Frozen max calls/duration; optional bounded execution only | Budget exhausted: stop/hold, no recursive dispatcher |
| Tampered evidence/double-counting | Exact artifact/evaluator receipts, deterministic duplicate checks | Forged digest or reused event: fail closed |
| Canonical package depends on monorepo | Standalone closure and offline tests remain valid | Export source package without repo, run without replay service |
| Replayed “counterfactual” presented as observed | Distinct status and provenance | Unexecuted branch may not receive `OBSERVED_PASS` |

Architecture acceptance requires **actual planted negative tests** for each high-risk mechanism, not just this table. Where a test is not run, mark `NOT_RUN`, never silently waive the failure.

### Adversarial revision from v0.1 to v0.2

The first architectural draft contemplated storing every attempt and selecting the highest replay score. That fails for sparse histories, polluted history, false claims of permission, and evaluator drift. Revision 0.2 therefore makes recording **optional and privacy-filtered**, distinguishes hypotheses from executed nodes, constrains replay to supported transitions, holds evaluator identity fixed, retains the incumbent on ties, adds unseen cases and live pilots, and makes the policy **declarative** by default. This is a design critique, **not an executed proof**.

## 8. Phased delivery and stop gates

Each phase is a **useful completed behavior**, not a completed planning note. A phase may end `NO_GO` when evidence contradicts its value. Issue links are tracked by the umbrella issue; no bulk rollout until the pilot works.

| Phase | Executable deliverable | Exit evidence | Dependency |
| --- | --- | --- | --- |
| 0. Architecture proof | Frozen contract & attack matrix tested against a minimal demonstration fixture | Written decision plus red/green planted failures for replay unknowns, evaluator tamper and private data | None |
| 1. Evidence intake | Minimal standalone-optional event recorder/importer; reject unauthorized/invalid records | CLI/API fixture tests, no raw personal overlay/secret capture, exact digest/readback, package closure | 0 |
| 2. Offline replay | Deterministic traversal of observed tree with explicit UNKNOWN_BRANCH and budget accounting | Reproducible paired replay, mutation negatives, seeded fixtures, exact evaluator pins | 1 |
| 3. Policy laboratory | Declarative baseline plus candidate comparison, fixed evaluator, hard-veto safety checks and heldouts | Candidate that cheats is rejected; on tied/small samples incumbent retained | 2 |
| 4. Adversarial live pilot | Bounded real tasks across two skill families; baseline and candidate use equal budgets | Real red/green outcomes, preserved acceptance gates, measured cost, decision to ship or stop | 3 |
| 5. Consumer integration | Optional explorer embedded through portable in-package instructions and/or repository engine; versioned opt-in | Standalone/no-network/no-store export tests, no regression in v0.3.4 local preference behavior | 4 |

No hidden background task or recurring automation. GitHub Actions minutes may be used for bounded deterministic QA. Later corpus-wide rollout, third-party replication, or agent-host trials are **optional follow-on work**, not prerequisites to finish the first vertical slice.

## 9. Ownership and interfaces

- **Canonical owners:** Skillz maintainers control skill versions, registry pins, evaluator and release decisions. No auto-merge or implied owner approval.
- **Repository engine:** owns optional experiment capture, replay and policy-lab code. Initial likely location `scripts/qa/recursive-improvement/`, with versioned fixtures under `tests/recursive-improvement/`. Exact paths require Phase-0 validation against current repo layout.
- **Authored portable skill:** retains all mandatory references **inside its package** and an accessible static adversarial path. Optional replay component only if it materially improves consumer outcomes and ships self-contained. Do not make repo tools a hard runtime dependency.
- **Data stores:** no public user preference data, memory files, raw user prompts, full private code, or tenant IDs. Synthetic/public sanitized fixtures only in source; ephemeral workspace for real governed experiments.
- **Existing PR #826:** baseline reference; avoid mixing experimental replay code into its unrelated versioning/review gate. Strategy PR and issues may land independently.

## 10. Architecture decisions to validate before implementation

1. **Event format:** JSONL+schema vs single JSON manifest. Default JSONL immutable events plus content-addressed fixture receipts, if an executable minimal proof supports it.
2. **Policy format:** declarative rule table vs sandboxed executable policies. Default declarative and pure until actual evidence demonstrates an essential expressiveness gap.
3. **Replayer boundary:** only observed child transitions; stop or return UNKNOWN on missing child, never interpolate guessed outcomes.
4. **Retention:** per-run opt-in ephemeral/sanitized evidence; explicit maximum size; content-addressed references to source-controlled public fixtures, with no private text retained.
5. **Evaluator versions:** stable IDs pinned for fair comparison; schema upgrades require version migration tests and no cross-version claims by default.
6. **Rollout:** start with one small vertical slice and planted failures, not automatic conversion of every authored skill.

**Next concrete action:** Phase-0 issue produces a minimal validated event/decision fixture and failing tests; Phase-1 turns it into real trace capture. If these do not reveal usable branch structure or trustworthy evidence, halt before building a “dreaming” simulator that mostly simulates paperwork.

## Research links

- Tong Zheng et al., [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858), arXiv 2609.14858, submitted September 2026 and revised October 2026.
- [Google Research reference implementation](https://github.com/google-research/dream-rsi). The published repository explicitly holds the agent/evaluator/task fixed during policy evolution.
- [DREAM-RSI project explanation](https://dream-rsi.com/). Important limit: the replay world only knows branches that were actually explored.

The proposal is an original Skillz design; no external implementation has been copied, installed, or executed.
