# Modular bootstrap, CI cost measurement, and governed migration

**Use when:** an expensive monolithic bootstrap continues running after change
classification is introduced, or an optimized path would change protected
CI obligations. A classifier added next to an unchanged expensive workflow
saves **zero** minutes by itself. Avoid celebrating labels as optimization.

## Inventory before decomposition

Inspect the actual workflow YAML, referenced reusable workflows, scripts,
job conditions, provider trust boundary, required status names, release gates,
runner costs, caches and observed critical path. Record each constituent
check as `id | actual command | shared setup | inputs | prerequisites |
unique failure detection | required status | runner/minutes | scope`.
For a complex repository, inspect transitive source-to-build, build-to-test,
model-to-input, generated-artifact, packaging, trust and publication edges.

Identify **what actually takes time**: runner startup, compiler/toolchain
install, dependency resolution, build, model load, test, package/sign, cache,
release or deployment. A logically separated check is not necessarily a
separate GitHub job. Group checks when they share large setup, keep output
subject identity and trust boundaries clear, and parallelize only where the
critical path improves without increasing billed runner time materially.

## Group based on measurements and dependencies

Design one trusted plan and a small number of execution groups. The example
uses docs, Rust build/test, model consumer and mandatory policy/trust. Rust
build+test run on one runner to avoid repeated setup. Model validation waits
for Rust build if the model consumer requires it; in a real consumer, either
pass authenticated build artifacts with hashes or repeat the exact build
inside the consumer command. A `needs` edge alone **does not transfer bytes**.

Every source-to-obligation mapping is backed by the repository's actual
build/test generator and affected outputs. A doc can be model input. Unknown
files/ambiguous graph extensions => broad verification. Do not suppress a
native OS check, provenance/signature, security gate or branch-required
status just because the candidate looks cheap.

**Important adoption test:** after adding classification, find and address
**all unconditional old bootstrap paths**. A parallel standalone bootstrap
workflow can still run at unchanged cost. Classify *both* GitHub workflow
selection and the commands inside selected jobs, including reusable
`workflow_call` or release dependencies. Rewire eligible expensive work
behind the plan only after shadow comparison and policy approval. Preserve
required always-run security/qualification, release and production gates.

## Governed transition, not a one-step rename

1. **Baseline:** capture full-run acceptance, job-level actual duration,
   billed runner minutes, critical path, error detection, required statuses,
   branch protection and release/production governance at exact revisions.
2. **Shadow:** run new source-to-obligation plan and execute bounded selected
   jobs while the original full acceptance is still authoritative. In a
   no-Actions-budget situation, validate fixtures locally but do NOT claim
   the shadow trial or runner savings occurred. Include seeded faults for
   omitted docs, changed model README, Rust transitive build/test, missing
   commands, canceled jobs and stale SHA/merge base.
3. **Parity:** compare results against real full acceptance for comparable
   revisions, with unique failure detection and positive/negative controls.
   Missing visibility means UNKNOWN, not PASS. Correct graph or command
   omissions and re-run bounded comparisons. Ensure a stable always-emitted
   final status fails on missing, skipped or bad selected work.
4. **Policy migration:** require repository-owner authorization; inspect and
   edit required-status/ruleset settings, `AGENTS.md`/`CLAUDE.md` and any
   local required check lists. Test the new required status on a fresh PR
   before retiring old required names. A passing workflow is not evidence
   branch protection enforces it. Keep reversion instructions and old
   runner available until the new path is proven.
5. **Cutover and proof:** disable or scope the *old unconditional expensive*
   bootstrap so it no longer runs on selective changes. Verify no additional
   `push`, `workflow_call`, default/reusable or deployment trigger silently
   recreates the cost. Reconfirm exact gated HEAD, complete detected failures
   and actual runner-minute and latency savings on comparative runs.
6. **Post-cutover:** monitor false skips, required-status reliability, costs,
   changes to dependency graph and the upstream toolchain. New unknowns
   revert to full/hold rather than losing assurance. Release/production
   signing/approval and other independent trust controls remain intact.

Do **not** remove old checks merely because a new workflow has green CI.
Do not rename a protected status without migrating rulesets/branch protection.
Do not deploy or modify repository governance without authorization.

## Measurements: separate budget from critical path

For each comparable actual baseline and new-run pair, record:
`scenario | repo/source HEAD | run ID/attempt | runner OS/size |
cache state | check group | start/end timestamps | status |
billed runner minutes | approval/protected status | fault-detection verdict`.

- **Billed runner minutes:** sum recorded job-level billed minutes, including
  cache/set-up duplication. Some billing plans round to whole minutes;
  don't infer costs from YAML or a single wall-clock delta.
- **Critical path:** elapsed time from start of required PR qualification
  to actual required final-gate success, excluding/including queue time
  consistently. The sum of runner minutes is *not* critical-path latency.
- **Comparable cohorts:** docs-only, README/model input, Rust-only, mixed,
  policy/trust and release separately. Annotate environment and cache
  differences, retries, cancellation and unrelated infrastructure changes.
- **Independent acceptance:** observe end-to-end selected work and real gate
  conclusions in at least one external consumer repo after owner approval.
  Offline scripts and synthetic fixtures prove only the local mechanism.

**Decision:** qualify optimization only when required check detection and
protected-status behavior are preserved, the old expensive path really
stops, and comparative observed runner cost or critical path improves.
If evidence is missing, the appropriate status is `IMPLEMENTED_NOT_ADOPTED`.
