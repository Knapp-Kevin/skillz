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
   A README can be a language/model build input; a security heading,
   release note, executable document, generated interface contract,
   workflow policy or Markdown symlink can be consequential. **Neither
   filename nor extension alone proves documentation-only impact.** A mixed change inherits
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

The bundled [offline classifier](../scripts/classify_change.py) is
**repository-neutral**: it recognizes universal danger categories without
assuming a project's primary language, repository name, model format or
documentation semantics. The [anonymous policy fixture](../examples/impact-policy.json)
illustrates inert JSON rules. A real consumer MUST author its own trusted
impact policy by auditing exact build, model, governance, dependency and
release inputs. An absent policy means FULL, including for Markdown.
The generic classifier is not a dependency graph. It cannot independently
prove that `README.md` is passive or that a suite may be skipped.

Policy schema: a JSON object with `"schema_version": 1` and `"rules"`
array. Each rule has exactly `match` (`exact`, `prefix` or `suffix`),
`pattern` (a path or extension) and `category` (`documentation`,
`executable-code`, `models`, `dependencies`, `governance`,
`workflows`, `release-assets`). Multiple matching rules union their
categories, and built-in critical classes cannot be overridden.
Only explicitly verified passive paths should use `documentation`.
A **prefix selector must end in `/` and designate a directory**;
`{"match":"prefix","pattern":"docs"}` is invalid, because it also
matches `docsecrets/` and `docs-private/`. Use `docs/` only after
inspecting all relevant descendant inputs. **Documentation cannot be
assigned by a global suffix rule** such as `{"match":"suffix",
"pattern":".md","category":"documentation"}`: a Markdown file may
be model input, generated build material, executable documentation,
governance or release evidence. Use bounded exact file or directory
prefix rules for established passive content. Other suffix categories
remain permitted when they select conservatively.
An unlisted path is `unknown` and FULL. Structural validation refuses
unsafe/unsupported selectors. The JSON must be copied to and run from the
**trusted base revision**, not the candidate PR revision.

The [GitHub Actions reference](../examples/classified-github-pr.yml)
uses the unprivileged PR event, exact trusted-base policy and classifier,
a draft/candidate impact decision, mutually exclusive target/full jobs, and
an always-emitted final gate. Consumer `ci/targeted-qualification.sh`
and `ci/full-qualification.sh` are **required actual scripts**: the
example fails if missing, not a success-shaped placeholder. Existing
branch-protection checks and provider-specific release assurance remain
independent until their replacements are explicitly qualified. Pin third-party
actions. Never execute or install generated workflows without authorization.

**Stage and evidence requirements:** A draft with known executable/model/
dependency impact may run targeted feedback only, with full acceptance still
due when ready. Workflows, trust/governance, release inputs and unknown impact
always require full verification. Final consequential candidates and releases
must pass the complete applicable suites on their exact commit, including
negative controls, platform-specific tests, proof/model verification, signed
input identity and immutable SDK boundaries where relevant. Ordinary
hand-authored documentation receives reduced work only after the consumer
explicitly proves it is not an input to those contracts.

**Pages, deployment and build reuse:** Before removing any repeated build,
verify that producing/consuming jobs use identical content-addressed input
closure, exact source SHA, toolchain/SDK pins, platform assumptions, artifact
digest and provenance. The consumer must authenticate signatures and release
eligibility, not trust a cache key, filename, self-reported fingerprint or an
untrusted artifact from a fork. Sequence publication after all required
acceptance has succeeded on the exact subject revision. Reuse the qualified
artifact only where it preserves both content and assurance. Otherwise,
retain a separate build and investigate future safe composition. Measure
wall time and billed minutes from comparable real runs, never from YAML
job counts alone.

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
toolchain, OS and trust boundary in key), content-addressed build outputs and
signed provenance. Track both the **bytes** and the **acceptance verdict**
that qualified those bytes. A consumer of a CI/Pages/release artifact must
validate its producer, immutable input closure, digest, trust domain and
exact-revision required-gate success. Never accept untrusted fork caches or
artifacts into signing/release without explicit isolation and verification.
A cache hit alone is not a security or correctness pass.

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
