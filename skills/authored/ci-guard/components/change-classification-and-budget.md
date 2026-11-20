# Component: change classification and budget-aware CI generation

**Use when:** generating or materially redesigning a CI workflow, selecting
relevant suites, addressing runner cost, or reducing waste from unrelated
checks. The main [CI Guard entrypoint](../SKILL.md) carries the mandatory
contract; this file is bundled technical guidance, not a central dependency.

## Non-negotiable design gate for GENERATED workflows

**Classify the actual changed artifacts before selecting expensive CI work.**
This must be an explicit decision step in generated workflows, whether a
trusted deterministic classifier, proven dependency graph or an equivalent
provider-native mechanism. Do not confuse job-name labels or post-failure
triage with change classification. A generated workflow without any
pre-dispatch impact classification needs a documented exceptional reason:
e.g., every change has verified identical mandatory checks and a classifier
would add cost without reducing work. Do not silently omit it.

1. **Resolve change set:** compare the exact trusted base and proposed head
   revision. Include deleted/renamed paths, source-generated files, shared
   packages, manifests, migrations, security/identity controls, workflows
   themselves, build tooling and release assets. Check the actual dependency
   graph when available. Missing refs, incomplete diff, unsupported path
   semantics or unknown dependency propagation -> **FULL / BLOCK** according
   to the site's existing policy, never `docs-only` by assumption.
2. **Classify impact, not suffix alone:** identify documentation-only,
   isolated code or tests, shared-library/lockfile, workflow/policy, release,
   security, build infrastructure, generated output and cross-component risk.
   `README.md` is usually low risk; `SECURITY.md`, release notes used as
   signed release inputs, executable docs, generated API schemas, a Markdown
   workflow policy, or an `*.md` symlink may not be. A mixed change inherits
   **the union of required checks**. Disclose uncertain impact.
3. **Bind to the required assurance floor:** classify which **additional**
   checks are safely conditional. Keep the actual branch-protected required
   signals, trust-boundary/security checks, signature/provenance requirements
   and any mandatory policy checks independent of workload class. A
   `docs-only` decision cannot suppress a control it has not proved
   irrelevant. Record the reason a check may be skipped and its substitute
   assurance if any.
4. **Dispatch selectively:** doc/link/format checks on docs changes;
   focused affected-suite checks for verified code dependency boundaries;
   broader integration, native OS, package, release and security checks where
   needed. Revalidate classification if a PR head changes. For unmodeled
   languages or monorepo packages, choose FULL until an impact graph is proven.
5. **Use a dependable required gate:** a short, always-emitted aggregation job
   must fail when classification fails, any **selected** job fails, or a
   selected job was unexpectedly skipped. GitHub's skipped job can report
   SUCCESS, while path-skipped required *workflows* can remain pending.
   Keep the required workflow trigger broad and condition *jobs*, not the
   workflow itself, where branch protection depends on a stable status.
   Never rename an existing protected status without updating its protection.
6. **Keep privileged logic trusted:** an untrusted PR is **data**. Run dispatch
   policy/classifier from a trusted base commit, with read-only permissions and
   no secrets. For GitHub Actions prefer `pull_request`, not privileged
   `pull_request_target` that executes fork code. Path input and job outputs
   cannot be treated as commands. The final gate is independent of PR-edited
   policy. A changed classifier/policy itself triggers the full suite.

The bundled original [offline classifier](../scripts/classify_change.py)
implements a **conservative example** for Python/docs/unknown paths. It is
not a complete dependency graph or a universally safe file whitelist;
repositories must adapt high-risk paths to their own build/deployment
contracts. [GitHub Actions reference](../examples/classified-github-pr.yml)
shows an unprivileged PR event, trusted-base classifier, conditional jobs and
an always-present final gate. Copy/adapt both into the consumer repository
and pin any third-party actions. The example fails closed when its full
qualification implementation is absent, rather than emitting a fake pass.
Do not execute or install generated workflows without user authorization.

## Other high-value, independent budget levers

**A. Affected-test selection with evidence.** Build a mapping from changed
modules to tests and reverse dependencies. Recompute mapping on build-graph,
fixture, compiler flags, generated code, package manager, shared library or
test infrastructure changes. Missing mapping -> broader testing. Keep a
scheduled/release full regression route when the product actually requires it,
not as a substitute for necessary pre-merge failures.

**B. Fast feedback first.** Run cheap format/syntax/static checks early;
parallelize independent, consequential checks only when the cost/latency
tradeoff justifies it. If the early gate fails, avoid launching expensive
downstream jobs unnecessarily. Never serialize unrelated checks merely to
create a more elaborate plan.

**C. Reuse computation safely.** Prefer reproducible caches (lockfile,
toolchain, OS and trust boundary in key) and content-addressed build
artifacts. Do not allow untrusted fork caches or artifacts to poison release,
signing or privileged workflows. Verify artifact origin/digest where it
matters. A cache hit alone is not a security or correctness pass.

**D. Matrix and environment coverage.** Drop redundant combinations only
with evidence they exercise the same behavior. Keep platform-specific/native
qualification for affected code. Where release-specific coverage can move
later, check whether the failure would already be irreversible at merge.
Do not reduce native Windows/macOS/security checks just because Linux is
cheaper.

**E. Cancel stale work.** Use safe per-PR concurrency cancellation for
superseded revisions, but avoid canceling a production deploy, release,
required audit, or the only evidence-generating job on which delivery
depends. Distinguish aborted from failed/passed runs.

**F. Retry discipline.** Treat a reproducibly flaky step as a defect to
repair; use scoped retries only for transient infrastructure errors with
bounded retry budget and a visible failure record. Do not relabel a
consistently failing assertion as intermittent.

**G. Lower overhead where it actually pays.** Compare runner-image startup,
container pull time, dependency install, fanout overhead, artifact transfer
and true critical path. Share setup artifacts only when freshness/security
invariants survive. Beware a cheap classifier that adds 90 seconds to every
8-second docs PR; measure its fixed overhead too.

## Before/after experiment

Report *observed* baseline and candidate, on comparable revision classes:
`change class | sample count | selected/skipped jobs | seeded fault detection |
p50/p90 latency | runner minutes | retries | cost rate and cache assumptions |
required-status outcome | savings confidence | rollback`.

Candidate value must include the classifier, trusted checkout, setup, final
gate, and any reruns caused by false low-risk decisions. Count action
executions only when observed; modeled savings are ESTIMATES. Keep **false
negative risk** explicit: suppressing a check that would have blocked a real
regression is unacceptable regardless of the runner-minute savings.

**Completion:** The generated workflow shows a verified classification
decision, truthful selected/skipped results, a reliable required status, and
an authorized negative control proving a sensitive change is not routed to
docs-only. Deliver a bounded patch and outcome evidence. Do not mistake a
successful YAML parse or simulated check plan for a real CI run.
