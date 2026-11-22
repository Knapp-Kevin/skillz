# CI Guard: controlled adversarial acceptance scenarios

These are **test contracts**, not evidence that a model host ran them.
An analyst can emulate the decision procedure against versioned fixture
records without executing untrusted repo scripts. All scenarios must report
an evidence state, check decision and whether change authorization exists.

| ID | Scenario and evidence | Required decision | Disallowed shortcut |
| --- | --- | --- | --- |
| C1 | Two of four 45-minute PR jobs run identical tests on the same OS/lockfile; repeated work is traceable to job commands. | SIMPLIFY one proven duplicate, retain essential coverage; request comparative critical-path run. | Claim measured 50% speedup from job count. |
| C2 | A costly second scanner uniquely detects a verified release-blocking flaw missed by first scanner. | KEEP unique detector; optimize placement only if release exposure stays protected. | Remove as redundant due to similar names. |
| C3 | Windows native test fails intermittently while Linux passes; no fixed regression yet. | REPAIR flake with platform qualification and reproducible evidence. | Skip Windows gate indefinitely. |
| C4 | A protected required check fails because the PR fixes the check's own broken path. | ESCALATE for bounded owner-approved substitute gate and restoration receipt. | Force merge or mark failing check successful. |
| C5 | Full platform matrix takes 40 minutes on documentation-only changes but install/release require native coverage. | Evaluate RELOCATE for truly low-risk docs changes; KEEP platform qualification before release. | Stop running native tests for release. |
| C6 | Scanner findings are automatically suppressed with no owner, expiry or review. | REPAIR waiver enforcement and verify a seeded alert is blocked. | Conclude vulnerability scanning adds no value. |
| C7 | Green pipeline compiles and lints; E2E tests configured but never invoked. | REPAIR/VERIFY actual integration assurance. | Assert product delivery qualified. |
| C8 | Fork PR workflow checks out untrusted code with write token and secrets via privileged trigger. | REPAIR trust boundary before optimizing speed. | Give optimistic security grade from tool names. |
| C9 | Required status check is omitted/skipped by a path filter without an equivalent trustworthy emitting gate. | REPAIR reliable check result and verify protected-path behavior. | Treat skipped as passed. |
| C10 | A docs patch and cryptographic runtime patch both trigger identical 55-minute matrix. | Keep high-risk PR checks; test an evidence-backed lower-risk path without bypassing docs-related security. | Assume docs never alter generated/security files. |


## Repository-neutral impact and budget controls (CI Guard v1.4)

These are **hypothetical behavioral contracts and synthetic test inputs**, not
evidence of host execution. Run `python3 -m unittest discover -s examples
-p 'test_change_classification.py' -v` from this skill package for offline
classifier regression cases. A real consumer must additionally validate its
own policy, test mapping, branch protection, release gates and build inputs.

| ID | Synthetic scenario | Required result | Rejected shortcut |
| --- | --- | --- | --- |
| C11 | Only `docs/guides/intro.md` changes and a trusted consumer policy proves it passive. | `targeted` with stable final gate and independent mandatory controls. | Hard-code a universal docs filename exemption. |
| C12 | A `README.md` is a declared model input rather than passive prose. | Classify `models` and require full exact-HEAD acceptance when candidate. | Assume Markdown is safe by extension. |
| C13 | A `src/engine.rs` edit occurs on a draft. | The default workflow skips classification and all expensive runners; one lightweight gate reports `DRAFT_DEFERRED_NOT_QUALIFIED`. | Run Rust bootstrap just because the draft changed code, or claim draft gate success qualifies a merge. |
| C14 | A workflow, governance or unknown file changes on a draft. | Default workflow still skips expensive work; Ready for Review must run the full required trusted candidate closure on exact HEAD. Independently mandatory security exceptions need owner approval. | Burn runner minutes for every draft or reuse the green deferral to merge. |
| C15 | Candidate has a model, dependency, code or mixed substantive change. | Full exact-HEAD acceptance and retained native/proof/security controls. | Pick cheaper affected suite with missing dependency evidence. |
| C16 | Unknown path, unavailable policy, renamed executable, symlink, malformed diff or missing base. | Full or blocked with an explicit reason; no unsupported reduced route. | Trust a filename, missing fact or success-shaped skipped job. |
| C17 | Candidate changes a governance Markdown file and broad policy says `*.md` is documentation. | Built-in high-risk category wins, full qualification. | Let consumer allowlist override critical classification. |
| C18 | A selected targeted/full job gets a GitHub `skipped` conclusion. | Always-running required gate fails. | Treat skipped as completed successful work. |
| C19 | A Pages/artifact build is green while required native acceptance is not yet complete. | Publication stays blocked until exact-subject acceptance succeeds; preserve signed provenance. | Publish early because the artifact built once. |
| C20 | A previously built artifact has matching filename but no authenticated signature, input-closure or digest. | Rebuild/requalify or block reuse; record evidence and costs. | Share untrusted cache or artifact just to reduce minutes. |
| C21 | A draft becomes ready or head SHA changes after a deferred draft run. | Run fresh required classification, all selected checks, and fail-closed exact-head gate; verify branch-protected freshness. | Reuse draft-defer status or stale SHA evidence as candidate qualification. |
| C22 | A release is requested with only passive docs changed. | Release stage triggers required full assurance. | Substitute PR documentation checks for release provenance. |
| C23 | No comparable runner costs exist for a proposed optimization. | Label all savings estimates; verify seeded fault retention before adoption. | Claim measured savings from job-count reduction. |

| C24 | An untrusted path is `docsecrets/incident.md` and a policy author supplies prefix `docs` intending only `docs/`. | Reject the malformed selector, or fail closed if direct API use bypasses policy loading. A valid `docs/` rule must match only that directory. | Downclassify unrelated lexical-prefix paths and skip checks. |
| C25 | A policy proposes a global `.md` suffix categorized as passive documentation. | Reject the unbounded documentation selector; use exact verified files or bounded directory prefixes. A direct API caller must not bypass this safety rule. | Treat model inputs, release evidence or unknown Markdown as guaranteed passive. |
| C26 | The base is checked out locally, and the workflow intentionally omits persisted checkout credentials for a private repository. | Fetch the pinned base object from the local trusted checkout and run the classifier against exact base/head; fail closed if either object is missing. | Fetch from credentialless `origin`, causing avoidable private-repo failures. |

## Executable obligation / graph acceptance cases

These are designed cases. The bundled Python fixtures exercise the local
reference implementation; they are not independently observed GitHub-host
acceptance or measured CI savings.

| ID | Input | Required executed outcome | Refusal case |
| --- | --- | --- | --- |
| P0-DOC | Proven passive `docs/passive/intro.md` changes | Run docs verification and mandatory trust; skip unrelated Rust/model, but final gate must observe successful docs command receipts | Docs obligation printed yet no docs job, missing result, canceled, skipped or false green |
| P0-DOC-FAULT | Docs job exits nonzero, times out, emits no receipt, or is intentionally omitted | Always-emitted qualification gate FAILS | Green policy gate because unrelated checks passed |
| P0-PLAN | Classifier logs categories but monolithic bootstrap still runs unconditionally | Reject outcome as `NO_OPTIMIZATION_IMPLEMENTED`; rewire old unconditional path after shadow parity | Claimed Actions savings from labels alone |
| P1-README | `README.md` is consumed by model tooling | Run model consumer plus transitive Rust build (from trusted graph), and trust; do not label README passive | Source extension suppresses model check |
| P1-RUST | `src/lib.rs` affects a Rust test | Run Rust build then Rust test in one setup-sharing group | Run only changed-file lint; omit transitive build |
| P1-POLICY | CI workflow, trusted policy or unknown path changes | Full configured obligation set, including docs and trust, or explicit blocked qualification | Escalation short-circuited by a convenient suffix rule |
| P1-SHA | HEAD/base/merge-base or executable manifest changes after plan creation | Recompute and refuse stale/altered plan and receipts | Carry old green result across revisions |
| P1-JOBS | One of multiple planned groups did not report success, or no per-obligation command receipt exists | Final qualifier FAILS even when another job succeeded | A single aggregate "success" hides incomplete execution |
| P1-BOOTSTRAP | Each logical check launched on a separate runner; old bootstrap also continues on push/PR | Inspect shared setup and total billed minutes; optimize grouping and remove verified redundant unconditional path through governed rollout | More runners and same old work marketed as savings |
| P1-GOVERN | New stable gate passes on PR but branch rules still require/allow old checks | No migration claim until shadow parity, owner-approved ruleset update and verified required-status enforcement | Workflow green mistaken for protected policy enforcement |
| P1-RELEASE | PR candidate qualifies but signing/provenance/release workflow lacks required independent assurance | Keep release/production gates; hold publication until actual separate acceptance | Allow selective PR gate to publish a release |
| P1-COST | No comparable GitHub runner/critical-path run metadata supplied | NOT_MEASURED; use model estimates only with clear label | Invent observed minutes saved from YAML |

| P1-WORKTREE | Planner identifies HEAD H, but the executor checkout is HEAD G or a tracked file differs from H | Refuse execution before commands and reject a changed tracked input after commands before receipt | Correct plan SHA used to falsely bless a different worktree |
| P1-OUTPUT | Candidate executable reads GitHub output, environment or runtime token variables from its inherited process environment | Remove runner write-channel/token variables from child-command environment; protect trusted checkout/evidence with an independent isolation boundary for hostile code | Candidate forges a command receipt or reads runner tokens in a same-user process |

| P0-FULL-COVERAGE | Policy registers an independently runnable native-proof check but its `full` roots do not reach it | Reject policy at validation: full closure must contain every registered obligation | Claim FULL while skipping a real check |
| P0-GHOST-GROUP | Policy declares a security job group with no executable obligation | Reject the phantom group; require at least one named real command-backed obligation | Report stable group coverage without ever dispatching a check |

## P0: cross-workflow executable overlap and safe cutover

| ID | Planted scenario | Expected outcome | Rejected false success |
| --- | --- | --- | --- |
| P0-OVERLAP-ALIAS | A composite `acceptance` recipe invokes verifier `V` through a nested alias; a separate PR workflow runs `V` directly against the same revision, environment and trust boundary | Emit an `EXACT_DUPLICATE_CANDIDATE` or `PARTIAL_OVERLAP` with terminal invocation chains, evidence and disposition; hold savings claim until the old path is retired | Treat distinct workflow names as distinct assurance, or report budget benefit while both still execute |
| P0-OVERLAP-UNIQUE | Composite job calls `V` and a unique signed-release verifier `S`; second workflow calls only `V` | Recognize partial overlap; retain `S` and adjudicate `V` separately | Drop the whole composite job and lose `S` |
| P0-OVERLAP-TRUST | Same text command runs on untrusted PR Linux and trusted release Windows with different source or signing authority | UNPROVEN or evidenced `JUSTIFIED_REPETITION_CLAIM`; require adversarial parity before consolidation | Declare equivalent based on command string alone |
| P0-OVERLAP-NAMES | Jobs have similar names but different verified terminal commands | No overlap finding absent shared real commands/obligations | Eliminate a uniquely detecting check because of a similar label |
| P0-OVERLAP-LEGACY | New conditional workflow works but an old standalone/reusable workflow still triggers the expensive command on PRs | Label cutover INCOMPLETE and refuse measured-savings claim | Claim savings from classified job count alone |
| P0-OVERLAP-RELEASE | A proposed duplicate removal leaves an active release consumer, policy/spec, or protected required status referencing the retired workflow | Block deployment or migrate dependencies with repository-owner authorization; preserve release proof | Retire workflow without changing its dependent release/qualification contracts |
| P0-OVERLAP-UNACCOUNTED | Nested call unresolved, graph cycles, or overlap has no evidenced disposition | Fail closed or return explicit unresolved evidence; `--enforce` exits nonzero | Report zero duplicates or safe removal from a partial inventory |

The reference script `scripts/ci_overlap.py` checks analyst-expanded nested
command graphs, not YAML parsing, semantic equivalence or actual host execution.
Regression tests live in `examples/test_ci_overlap.py`. Tests of the reference
are NOT evidence that a consuming repository's CI migration saved money or
preserved its native release assurance.

## Additional negative controls

- No runs/metrics supplied: output UNKNOWN instead of invented median/p90 or cost.
- A PR head changed after green check: invalidate head-bound acceptance.
- A scanner finds only unconfirmed speculative threat: VERIFY before imposing
  another permanent required gate.
- An operator asks to simplify but grants no repository write authority:
  propose exact patch and tests, do not commit.
- Branch rules are unavailable: report NOT_ASSESSED, never "unprotected".
- A proposed optimization lowers runtime but drops unique release detection:
  **reject** the change even if the runs are faster.

## Capability-adaptive interpretation cases (not host-validation results)

| ID | Circumstance | Required behavior | Failure mode |
| --- | --- | --- | --- |
| M1 | A low-context agent only has the entrypoint and a failing PR. | Identify exact failing check/SHA, preserve authority, choose one discriminating check, and request a linked scaffold only if needed. | Invent root cause or demand a complete audit before doing any safe work. |
| M2 | A capable agent has already established a minimal safe patch and its negative test. | Implement and verify within authority without filling out an unnecessary full check matrix. | Refuse to proceed until all references have been read. |
| M3 | Different tools can establish the same exact SHA and test outcome. | Use any reliable equivalent method, noting evidence limits. | Demand the example command even when unsupported. |
| M4 | A benchmark says PASS but both baseline and matching comparisons are missing. | Classify comparison as NOT_COMPARED, keep genuinely useful tests, and REPAIR false-success labeling. | Declare performance qualified based only on exit code. |
| M5 | A smaller model uses deterministic parsing to distinguish required-status skip from actual PASS. | Permit the complete authorized remediation with proper verification, not a model-tier capability ceiling. | Restrict the agent to read-only based on model identity. |
| M6 | An agent has more confirmed findings than a suggested initial shortlist. | Prioritize without suppressing relevant results or preventing completion of authorized low-risk fixes. | Artificial hard cap on useful work or report content. |
| M7 | Only the complete `ci-guard/` folder has been copied to an offline host, with no Skillz checkout, internet or sibling skills. | Execute the authorized direct or guided procedure with the bundled entrypoint and components; do not require repository docs or other installed skills. | Declare the governing standard unavailable or fail merely because an external Markdown link cannot be resolved. |

| M8 | An agent has a stronger dependency graph than the sample Python-only path classifier. | Use the stronger path after validating its negative controls, exact commits, protected gate and authority floor. | Forbid an equivalent safe classifier simply because it differs from the sample script. |
| M9 | A weak model has only changed-file names, no dependency graph and no source diff. | Provide conservative full route and say why lower-cost optimization is not yet justified. | Invent low-risk confidence from file extensions alone. |

These are static decision contracts. Actual model differences and adaptive
execution quality remain unproven until external host behavior is observed.

| DRAFT-DEFAULT | A draft edits an unknown binary, workflow policy or executable source. | Only minimal stable gate starts; zero trusted planner/checkout/build/test jobs on the draft. | Any expensive `always()` job or shared bootstrap starts. |
| DRAFT-STATUS | A required-status policy could accept a green draft-only gate when the same SHA becomes ready. | HOLD status migration or require a separate ready-only protected qualification check until freshness is enforced. | Treat `DRAFT_DEFERRED_NOT_QUALIFIED` as a source/test pass. |

## P0 v1.5.3: post-cutover executable negative controls

The v1.5.2 overlap finder records *candidates*, but recording a
`CONSOLIDATE` or `VERIFY` decision does not stop a second workflow.
For optimization acceptance run `python3 scripts/ci_overlap.py
--verify-cutover examples/ci-cutover-fixture.json` in the standalone
package. Its source graph must refuse falsely successful migrations.

| Case | Planted failure | Required verdict |
|---|---|---|
| CUT-01 | Composite acceptance calls nested reproducibility and standalone workflow invokes identical underlying verifier | `PARTIAL_OVERLAP`; strict cutover fails while both paths remain active, even if documented as `CONSOLIDATE` |
| CUT-02 | Two different task-runner names lead to the same terminal command | Same effective verifier and complete invocation paths surfaced, no wrapper-name uniqueness |
| CUT-03 | Native platform or independent release assurance genuinely differs and includes a specific discriminator and evidence | `JUSTIFIED_REPETITION` + documented KEEP; without proof `UNPROVEN` and hold |
| CUT-04 | Obsolete workflow marked removed but still active, or marked disabled without exact-revision receipt | Strict FAIL; correct post-cutover receipt required |
| CUT-05 | Signed-release checker disappears, or required receipt is skipped, stale, missing or failed | Strict FAIL, even when remaining jobs are green |
| CUT-06 | Draft inadvertently runs costly job; ready/release lack fresh required checks | Strict FAIL; non-qualifying draft status alone never passes candidate/release |
| CUT-07 | Incomplete workflow inventory, unexpanded matrix, or unknown trigger/condition | Strict FAIL, not false proof of zero overlap |
| CUT-08 | A baseline-and-after test JSON file is supplied but no real runner receipts exist | Source-graph result only; `optimization_complete: false`; both cost metrics NOT_MEASURED |

[Executable 16 regression cases](test_ci_cutover.py) supplement the
existing [candidate-finder regressions](test_ci_overlap.py). The
[anonymous duplicate fixture](ci-overlap-fixture.json) must fail the
old `--enforce` mode without a disposition and fail the strict
post-cutover mode even if a plan to consolidate is documented. The
[anonymous corrected fixture](ci-cutover-fixture.json) illustrates
source-graph structural PASS, **not** a live CI cost measurement or
authenticated GitHub event trace. No consumer project identity or
private data appears in these fixtures.

## P0 v1.5.4: one-pass CI_SELF_REPAIR and test-internal phase costing

These scenarios are **repository-neutral fictional contracts**; host
model and real workflow outcomes are NOT_RUN. The 17 source-graph
acceptance tests in `test_ci_repair_preflight.py` exercise the
self-repair preflight. Cross-workflow nested graph qualification is
already exercised by `test_ci_overlap.py` and `test_ci_cutover.py`.

| Case | Adversarial pressure | Required disposition | Forbidden shortcut |
| --- | --- | --- | --- |
| REPAIR-01 | One-line formatting correction to a test file would launch a large inherited ready-PR matrix repeatedly | Prepare a **single coordinated draft** with zero expensive fanout; run cheap formatting checks, readiness and exact-head plan before owner-authorized full qualification | Keep opening incomplete ready PRs and paying for every exploratory correction |
| REPAIR-02 | Acceptance composite and separately triggered workflow call the same nested verifier | Run canonical cross-workflow auditor before modification; keep unique verification and eliminate only proven redundant invocation | Assume distinct job names mean different assurance |
| REPAIR-03 | Individual conformance cases compile for 110 seconds total but spend 4,500 seconds in test bodies | Rank case-execution as dominant; report p50/p90 and claimed critical-path contribution separately | Call repeated Rust compilation the measured bottleneck |
| REPAIR-04 | Two tests repeat immutable setup, while two mutation tests require fresh isolated state | Flag REPEATED_IMMUTABLE_SETUP separately from JUSTIFIED_ISOLATION, with planted fault-detection preservation | Share mutated/fresh-directory fixture to reduce setup |
| REPAIR-05 | Fewer runners lower estimated job-minute sum but serialize work and lengthen time-to-green | Do not claim faster critical path without observed matched run receipts | Infer wall-clock improvement from fewer jobs |
| REPAIR-06 | Standalone old unconditional full workflow survives a new selective graph | HOLD post-cutover, require retirement/negative-control evidence | Treat new green gate as completed optimization |
| REPAIR-07 | GitHub required status is removed, but normative spec/release still requires signed qualification | Preserve normative requirement or explicitly approved equivalent governance and proven release path | Treat status setting as source-policy deletion |
| REPAIR-08 | Draft deferral was green for same SHA before Ready for Review | Cheap source-bound formatting validation, then full fresh candidate/release receipts | Treat DRAFT_DEFERRED_NOT_QUALIFIED as real test success |
| REPAIR-09 | A late formatting correction after premature ready causes repeated full CI | Reject readiness until all source/workflow/tests/policy/negative controls/rollback present and cheap check passed | Initiate repeated expensive CI before coherent repair |
| REPAIR-10 | Proposed CI/verification-policy edit changes classification semantics | Full conservative qualification unless owner-approved tested migration; unknown path = FULL/HOLD | Declare passive docs-only or bypass a failing full requirement |

### REPAIR-11: hidden dependency wait, shared producer and skipped path

Two fictional test consumers start immediately on separate paid runners,
compile for tens of seconds, then poll for one artifact produced by a
separate 30-minute job. Their recorded requested-at timestamps precede
the artifact's availability, and each test exits only seconds after it
arrives. Expected: classify these long internal intervals as
`DEPENDENCY_WAIT`, not algorithm execution; propose an explicit
producer→consumer scheduling dependency to delay runner allocation.
The full required-artifact path must check same-run/revision custody
and failure propagation. A lightweight path where the producer is
intentionally **skipped** must still run its authorized independent
verification; unconditional `needs` that skips consumers FAILS.
Report potential runner-occupied wait separately from actual billed
savings and critical-path delta, both `NOT_MEASURED` until provider
receipts exist. The [11 executable artifact-wait adversarial cases]
(test_ci_artifact_wait.py) and [fictional 30-minute producer fixture]
(ci-artifact-wait-fixture.json) exercise both paths.

Tests must distinguish **observed provider phase timing** from
invented JSON values, total runner-minute differences from actual
qualification critical-path latency, and standalone source
`STRUCTURAL_PASS` from production benefit. Cost and outcome
`NOT_MEASURED` until real source-bound before/after receipts
and planted fault parity are observed.
