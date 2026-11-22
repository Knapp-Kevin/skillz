# Governed recursive skill improvement
## Umbrella architecture strategy, revision 0.4 (2026-11-22)

**Status:** Proposed, architecture validation and staged implementation authorized for issue planning. **Not implemented.**  
**Scope:** Skillz's **passive authored skill instructions, in-package optional components and maintainer-only QA**. Actual capture, replay and policy selection are invoked by an **authorized external consuming host**, never as repository-owned consumer infrastructure. The standalone Evidence-Driven Refinement Loop package remains independently usable.  
**Source:** [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858) and the [published Google Research reference](https://github.com/google-research/dream-rsi). Mechanisms are adapted, not copied or claimed to be experimentally reproduced.  
**Existing baseline:** Evidence-Driven Refinement Loop v0.3.4 in [draft PR #826](https://github.com/Knapp-Kevin/skillz/pull/826), not yet the merged canonical runtime. [Phase-0 contract PR #836](https://github.com/Knapp-Kevin/skillz/pull/836) is now merged on `main` at `96024878db5961121ec5988432a9842033ab101c`. This is **maintainer QA code**, not a repository-owned consumer runner.

## 1. Decision in one paragraph

Adopt a **bounded, evidence-driven meta-refinement program**. The existing loop fixes a real artifact: OBSERVE → EXPLAIN → CHANGE → CHALLENGE → DECIDE. Add an **optional, separately governed exploration policy** that chooses which falsifiable hypothesis or adversarial test to pursue next, under a fixed evaluator, budget, and authority contract. Collect **minimal, verified discovery traces** from real authorized attempts; replay only observed outcomes to compare exploration strategies cheaply; challenge proposed policy improvements against unseen adverse cases and actual execution before promotion. Never promote local user preferences into canonical policy, treat same-model agreement as external proof, or let an exploration policy change its evaluator or grant itself mutation authority.

**This is recursive improvement of the search strategy and skill implementation, not automatic LLM weight training, general self-modification, or permission to run unsupervised jobs.**

## 1.1. Hard architecture boundary: passive library and external execution

The current [AGENTS.md](../../AGENTS.md) and [Governance Index](../GOVERNANCE_INDEX.md) make Skillz a **passive skill library**, not a consumer runtime, evaluator, replay service, CI platform or policy-runner host. An external consuming agent/environment owns execution, local state, privacy controls, authorized evaluation and user-specific preferences. Skills may bundle **self-contained optional scripts and fixtures**, which the consuming host may execute under its own authority. Maintainer-only checks in `scripts/qa/` may validate repository sources on explicitly authorized maintenance requests; they must not grow into a consumer execution service.

Accordingly, this strategy **does not create a repository-owned learner, daemon, test harness service, policy lab, auto-refiner, scheduled task or automatic CI trigger**. P0's merged `contract.py` is an offline **maintenance-only structural checker**, with synthetic fixtures; it is not the future P1/P2/P3 runtime. The optional replay/capture functionality, if justified by the pilot, is packaged **inside a portable authored skill** for explicit use by the external host, or provided as a host-owned adapter. No consumer installation depends on `scripts/qa/` or on the Skillz monorepo.

Changing this boundary would require an **explicitly authorized Tier-1 architecture revision**, not an incidental issue or PR that happens to introduce executable code.

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
- **Policy:** initially a versioned, non-executable declarative decision table with bounded choices, not free-form Python supplied by a model. A **consuming host**, explicitly authorized by its user, may evaluate it with a self-contained bundled helper and allowlisted parser. The Skillz repository must never launch, host or schedule policy execution. Arbitrary executable policies are **out of scope** until host sandbox/threat review justifies them.
- **Executor:** current skill/source editing only under current owner authority; permitted outputs include `HOLD`, `NO_ACTION`, and unchanged artifacts. Replay never writes source files.
- **Replay store:** an optional, **host-owned** private or ephemeral workspace controlled by the consuming user/host; no automatic repository capture, telemetry, upload or persistent store. A portable skill must work with no store and must never write anything on activation. Only sanitized, permission-cleared synthetic/public fixtures may be deliberately contributed to repository maintenance. Raw personal/confidential/license-restricted recordings stay outside this repository.
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
  "workspace_state_digest": "sha256:<64-hex>",
  "evaluation_context_id": "fixed-context-001",
  "evaluator_id": "schema-validator-v1",
  "policy_id": "incumbent-v1",
  "outcome": "OBSERVED_FAIL",
  "outcome_receipt_digest": "sha256:<64-hex>",
  "measured": {"test_invocations": 1, "wall_ms": 110},
  "privacy_class": "public-synthetic"
}
```

This JSON is illustrative, not schema-valid: the placeholder digests must be replaced with real fingerprints. Validation must reject missing parents, cycles, duplicate IDs, illegal transitions, invalid/missing receipts, evaluator/source mismatch, implausible timestamps, unsupported task families and unknown outcomes. Events never contain raw user requests, preference file paths, personal IDs, credentials, full tool logs or secret-bearing diffs. The workspace-state digest is a **privacy-safe content fingerprint of authorized synthetic/public test state**, not a raw dump of file contents; unavailable or unshareable state yields `UNKNOWN_STATE` and is not eligible for exact replay. A digest proves correspondence to a claimed snapshot only when its evidence source is actually verified, not authorship or consent.

**Discovered hypotheses** and **executed outcomes** are different entities. A candidate may exist without an outcome; it cannot be silently counted as a successful attempt. A `SKIPPED`/unobserved branch has no replay reward.

### 5.2 Policy decision surface

Input: task-family tags, established evidence, allowed branch frontier, remaining **bounded** budget, evaluator version and risk constraints. Output: choose among **observed/allowlisted actions** (`inspect`, `adversarial-probe`, `run-targeted-verification`, `preservation-check`, `hold`, `stop-no-change`); optional priority and maximum attempts. Never output an arbitrary tool command, file path from untrusted text, remote URL, workflow dispatch, authority grant or new evaluator definition. Validate all decisions against trusted host constraints before executing.

### 5.3 Replay and policy promotion

Given a frozen replay-world collection and fixed evaluator:

1. Evaluate the incumbent first; retain its measured result and exact identity.
2. For each proposed policy, step only across **previously observed** choices and outcomes whose **preconditions and state provenance match** the target replay step; an unseen transition is `UNKNOWN_BRANCH`, and a different underlying workspace/environment state is `UNKNOWN_STATE`. Never infer a result solely because a similar command ran elsewhere. Mark state-changing/order-sensitive operations **non-replayable** absent matching isolated branch snapshots. Neither unknown status receives a guessed reward or an `OBSERVED_PASS` label.
3. Maintain separate development and **held-out** fixtures by task family and time cohort. No leaked holdout scores during candidate tuning. No duplicate evidence masquerading as independent worlds.
4. Compare on non-negotiable correctness and safety gates **before** utility/cost. A single material authority/security failure vetoes promotion. Measure test calls, elapsed time, stalled branches, false skips, and preservation regressions, using identical accounting rules.
5. Prefer incumbent on ties, too-small samples, missing provenance, disagreement, excessive overhead, unsupported transfers, or changed evaluator. Improvement is a **hypothesis**, not a shipped fact, until a bounded **live** adversarial pilot confirms it.
6. Proposals never self-merge, rewrite `SKILL.md` or the evaluator, or change user memory/persistent preferences.

**Invalid shortcut:** Offline replay can answer only “how would this policy have navigated the observed, **state-compatible** subset?” It cannot answer “what result would an unexplored branch have produced?” or “what would this mutation do if earlier edits were different?” A winning score on replay is not a guarantee of generalization.

**State-equivalence gate:** In code/skill refinement, earlier branch edits may change tests, dependencies, file state, available authority or downstream prompts. Replay must bind each outcome to a verified isolated source/workspace snapshot and evaluator/tool context (or a demonstrably invariant read-only operation). Ordering and parallelism can only be varied if they cannot change that outcome. If equivalence cannot be proved, replay reports `UNKNOWN_STATE`; the policy comparison cannot count it as a successful hypothetical execution.

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
| Mutations make recorded outcomes order-dependent | Bind outcomes to isolated workspace snapshots and evaluator context; never reorder non-commuting effects | Candidate changes prior edit or environment: return UNKNOWN_STATE, not reused reward |
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

The first conceptual design pass (not separately committed or executed) contemplated storing every attempt and selecting the highest replay score. That fails for sparse histories, polluted history, false claims of permission and evaluator drift. Revision 0.2 made recording optional, added provenance, fixed the evaluator, held the incumbent on ties and restricted replay to observed nodes. A **second adversarial challenge** found a further defect: even an *observed* node's outcome may depend on prior mutable workspace state, so changing branch order can invalidate reuse. Revision 0.3 adds state/context fingerprints, non-replayable classifications and an explicit `UNKNOWN_STATE` gate. Both are **design-level improvements**, not executed implementation proof.

### Adversarial revision v0.4: ownership and governance

Codex review of [strategy PR #835](https://github.com/Knapp-Kevin/skillz/pull/835) revealed a **P1 architecture conflict**: the previous version assigned trace capture, replay and policy-lab execution to a repository-owned engine under `scripts/qa/`, contradicting current Tier-1 passive-library governance. Revision 0.4 moves these execution responsibilities to **authorized external consuming hosts**, using optional self-contained skill components, and limits repository scripts to explicit maintenance-only QA. The earlier design's automatic consumer-infrastructure plan is **rejected**, not silently grandfathered in by an issue or by P0's passing tests. This is an adversarial design correction; executing host behavior remains to be tested in later phases.

## 8. Phased delivery and stop gates

Each phase is a **useful completed behavior**, not a completed planning note. A phase may end `NO_GO` when evidence contradicts its value. This strategy is tracked by [umbrella #828](https://github.com/Knapp-Kevin/skillz/issues/828). No bulk rollout until the pilot works.

| Phase | Executable deliverable | Exit evidence | Dependency |
| --- | --- | --- | --- |
| [0. Architecture proof (#829)](https://github.com/Knapp-Kevin/skillz/issues/829) | Frozen contract & attack matrix tested against a minimal demonstration fixture | Red/green planted failures for unknown branches, **state mismatch**, evaluator tamper and private data | None |
| [1. Evidence intake (#830)](https://github.com/Knapp-Kevin/skillz/issues/830) | Self-contained optional **skill-bundled / external-host** event recorder/importer; no repo-owned collector | CLI/API fixture tests, no raw personal overlay/secret capture, exact digest/readback, package closure | 0 |
| [2. Offline replay (#831)](https://github.com/Knapp-Kevin/skillz/issues/831) | Portable host-invoked deterministic traversal with UNKNOWN_BRANCH / UNKNOWN_STATE and budget accounting | Reproducible paired replay, state-swap negatives, seeded isolated snapshots, exact evaluator pins | 1 |
| [3. Policy laboratory (#832)](https://github.com/Knapp-Kevin/skillz/issues/832) | Host-executed **optional skill component** for declarative policy comparison with fixed evaluator, hard vetoes and heldouts | Candidate that cheats is rejected; on tied/small samples incumbent retained | 2 |
| [4. Adversarial live pilot (#833)](https://github.com/Knapp-Kevin/skillz/issues/833) | Bounded, user-approved **external-host** real tasks across two skill families; matched budgets | Real red/green outcomes, preserved acceptance gates, measured cost, decision to ship or stop | 3 |
| [5. Consumer integration (#834)](https://github.com/Knapp-Kevin/skillz/issues/834) | Optional explorer embedded inside a portable authored skill and/or consuming-host adapter; **no repository engine runtime** | Standalone/no-network/no-store export tests, no regression in v0.3.4 local preference behavior | 4 |

No hidden background task or recurring automation. GitHub Actions minutes may be used for bounded deterministic QA. Later corpus-wide rollout, third-party replication, or agent-host trials are **optional follow-on work**, not prerequisites to finish the first vertical slice.

## 9. Ownership and interfaces

- **Skillz maintainers:** own passive authored skill packages, source/provenance records, architecture documents, optional synthetic fixtures, and explicitly invoked **maintenance-only QA**. No owned consumer runtime, benchmark harness service, scheduler or evaluator. Source approval remains normal maintainer governance.
- **External consuming host:** owns execution of optional portable skill components, test/evaluator setup, private/ephemeral trace storage, real user consent, experiment budgets and any side effects. It must establish actual authorization; skill text or receipt flags are not grants.
- **Self-contained authored skill:** retains all mandatory usage rules, schemas, dependencies and fallback behavior **inside the downloaded package**. Optional trace/replay helpers must be package-local and host-invoked, never call back to repository-owned scripts or infer permanent user storage.
- **Repository QA:** [merged P0 #836](https://github.com/Knapp-Kevin/skillz/pull/836) supplies an offline structural checker under `scripts/qa/recursive-improvement/` and synthetic negative fixtures. That checker is for **explicit repository maintenance**, not the owner of future experiment replay/policy engines. Do not expand it into the consuming user's runner.
- **Data boundaries:** no public preference profiles, raw user prompts, full private code, tenant IDs or portable auto-telemetry. Only explicitly sanitized synthetic/public evidence can be committed to source. Real user traces remain host-local unless the user separately authorizes a governed contribution.
- **Existing PR #826:** baseline reference; avoid mixing policy laboratory work into its unrelated skill-version review. Strategy PR and implementation issues may land independently.

## 10. Architecture decisions to validate before implementation

1. **Event format:** JSONL+schema vs single JSON manifest. Default JSONL immutable events plus content-addressed fixture receipts, if an executable minimal proof supports it.
2. **Policy format:** declarative rule table vs sandboxed executable policies. Default declarative and pure until actual evidence demonstrates an essential expressiveness gap.
3. **Replayer boundary:** only observed child transitions; stop or return UNKNOWN on missing child, never interpolate guessed outcomes.
4. **Retention:** per-run opt-in ephemeral/sanitized evidence; explicit maximum size; content-addressed references to source-controlled public fixtures, with no private text retained.
5. **Evaluator versions:** stable IDs pinned for fair comparison; schema upgrades require version migration tests and no cross-version claims by default.
6. **Rollout:** start with one small vertical slice and planted failures, not automatic conversion of every authored skill.

**Next concrete action:** Phase 0 [#829](https://github.com/Knapp-Kevin/skillz/issues/829) is merged and complete (39 tests on Python 3.9/3.11/3.13, [CI run 44988171113](https://github.com/Knapp-Kevin/skillz/actions/runs/44988171113)). Phase 1 [#830](https://github.com/Knapp-Kevin/skillz/issues/830) must deliver a **standalone, host-invoked component** with no repository-owned runtime and real privacy/consent negative tests. If real authorized traces are unavailable, halt rather than invent a “dreaming” simulator.

## Research links

- Tong Zheng et al., [Dream-RSI: Recursive Self-Improvement through Evolving Worlds](https://arxiv.org/abs/2609.14858), arXiv 2609.14858, submitted September 2026 and revised October 2026.
- [Google Research reference implementation](https://github.com/google-research/dream-rsi). The published repository explicitly holds the agent/evaluator/task fixed during policy evolution.
- [DREAM-RSI project explanation](https://dream-rsi.com/). Important limit: the replay world only knows branches that were actually explored.

The proposal is an original Skillz design; no external implementation has been copied, installed, or executed.
