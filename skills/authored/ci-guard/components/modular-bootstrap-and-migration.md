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

## Early-failure ordering before expensive setup

Review the **actual event trace** for cheap correctness failures that occur
only after downloading a large container/toolchain or performing heavy
bootstrap. A deterministic format, metadata, whitespace or policy check
may be suitable as a preflight *if* its tool/version/environment semantics
are proven equivalent to the canonical gate. Its success is only an early
screen; the trusted final acceptance still checks the authoritative form.

- Prefer a lightweight preflight before expensive runner/container setup
  **when the expected saved cost outweighs another runner startup**. A
  separate GitHub job is not automatically the cheapest architecture.
- Where exact toolchain reproducibility is required, run the cheap check in
  the existing trusted environment before the expensive operation, or prove
  an equivalent pinned tool; never create a second loose formatter whose
  inconsistent results weaken acceptance.
- Fail fast on an actual negative result; retain full downstream checks on
  a preflight pass. A proposed reordering is not measured savings.
- Distinguish queue, checkout, image transfer, build and test latency using
  timestamps and billed job minutes from actual runs. One run that failed
  early does not establish a counterfactual median, p90 or net cost benefit.

**Observed failure pattern informing the design:** A repository bootstrap
downloaded its large locked SDK, then immediately failed a deterministic
Rust formatting check for one extraneous blank line. That confirms a
costly *ordering opportunity* worth evaluating, not that an alternate
preflight would have passed governance, been cheaper on average or
preserved unique acceptance. Validate those properties in shadow mode.

## Measurements: separate budget from critical path

For each comparable actual baseline and new-run pair, record:
`scenario | repo/source HEAD | run ID/attempt | runner OS/size |
cache state | check group | start/end timestamps | status |
billed runner minutes | approval/protected status | fault-detection verdict`.

- **Billed runner minutes:** sum recorded job-level billed minutes, including
  cache/set-up duplication. Some billing plans round to whole minutes;
  don't infer costs from YAML or a single wall-clock delta.
- **Critical path:** derive the longest *actual* required-job dependency
  chain from observed per-job starts/ends and explicitly supplied `needs`
  edges. Report the separate qualification wall-time envelope from first
  required start to final required completion. Missing cross-workflow
  dependency records, incomplete job lists or cycles mean UNKNOWN; the
  sum of billed runner minutes is not critical-path latency.
- **Comparable cohorts:** docs-only, README/model input, Rust-only, mixed,
  policy/trust and release separately. Annotate environment and cache
  differences, retries, cancellation and unrelated infrastructure changes.
- **Independent acceptance:** observe end-to-end selected work and real gate
  conclusions in at least one external consumer repo after owner approval.
  Offline scripts and synthetic fixtures prove only the local mechanism.

The optional [offline run comparator](../scripts/compare_ci_runs.py)
accepts explicitly supplied *actual* baseline/new GitHub job receipts with
same exact HEAD, case, runner profile and cache cohort. Each job requires its
measured billed runner minutes, start/end UTC, observed success and dependency
`needs`. It outputs billable minute deltas, DAG critical-path deltas and the
separate observed elapsed-time envelope. It refuses missing source identity,
failed protected status, incomparable pairs and incomplete multi-workflow
dependency edges. The tool **does not authenticate API data** or manufacture
measured savings from synthetic inputs. Synthetic examples test math only.

**Decision:** qualify optimization only when required check detection and
protected-status behavior are preserved, the old expensive path really
stops, and comparative observed runner cost or critical path improves.
If evidence is missing, the appropriate status is `IMPLEMENTED_NOT_ADOPTED`.
