# Component: placement and bounded CI experiment

**Trigger:** A slow, repeated, flaky or inaccessible workflow is preventing
effective delivery, or a team proposes moving verification to another gate.

Use a risk matrix instead of universal gate rules:

- Local/developer: actionable fastest feedback, focused tests.
- Draft pull request: default to no expensive CI; one cheap required
  status may report `DRAFT_DEFERRED_NOT_QUALIFIED` with no checkout
  or verification. Separately authorized mandatory draft security checks
  are explicit exceptions, not assumptions.
- Ready pull request: run change-relevant tests and critical trust,
  security and correctness controls against the current exact HEAD;
  reject stale or draft-only evidence and preserve merge protection.
- Protected main: meaningful broader integration where the PR gate need not
  repeat it, with an explicit recovery plan for post-merge failure.
- Release candidate: cross-platform, full matrix, signed packaging,
  supply-chain and release-specific checks where justified.
- Staging: real service wiring, migrations, rollback and E2E.
- Production: canary/health acceptance and rollback readiness.
- Periodic: long fuzzing, ecosystem audits and wider performance comparisons
  that need not block unrelated commits.

For every proposed relocation ask whether a vulnerability can become
irreversible *before* the next gate. If so, keep or replace its PR control.

**Experimental contract**
1. Freeze baseline workflow and comparison change classes; collect measured
   runs and note selection bias (queue time, cache, runner, retries).
2. Separate p50/p90 critical path from summed billed runner minutes.
3. Specify a *risk-equivalent* proposed pipeline and counterexample changes.
4. Preserve known positive and negative controls, especially the injected
   failing test and required-status reporting for skipped paths.
5. Run both comparable paths when feasible in an authorized test repository
   or sandbox. Otherwise record an explicit fixture-backed emulation.
6. Report actual measurements separately from modeled estimates. Failure
   rate requires sufficient observed denominators; flaky classification
   requires repetition or corroborated historical evidence.
7. Accept only if meaningful delivery friction improves *and* unique
   detection, protected revision binding, reviewer authority, and release
   acceptance are maintained. Otherwise REVERT or VERIFY.
8. Record the exact rollback patch/ref, rollback owner and the observation
   that triggers restoration. End optimization once acceptance is met.

**Self-blocked CI:** Do not mark a failing repair PR green by bypassing
protection. Identify a narrowly scoped owner-approved substitute verification
or temporary check repair, restore normal gates immediately afterwards,
and preserve the exception receipt.
