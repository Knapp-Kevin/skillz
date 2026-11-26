# Contract-derived acceptance plans

For a newly generated single, phased or pack skill, reuse its authored
[design dossier](design-contract.md), rather than inventing a second
contract. The optional generator reads the exact completed canonical draft
and compares every member to deterministic rendering of that dossier.
It then checks the selected assessed host and produces a private NOT_RUN plan.

    python3 -B engine/builder/acceptance_plan.py --design /private/design.json \
      --package /private/exact-skill-slug --host claude-apps

The package folder must have its canonical slug and contain every expected
file, with no added or changed members. This route covers builder-generated
original skills. For manually authored or adapted packages, use the reviewed
source route below or the [manual native host protocol](host-acceptance.md).
Do not force them through an unrelated blueprint.

The output binds the plan to the canonical file SHA-256 map, the dossier
digest and the selected host member transformation manifest. Every case
has an explicit expected contract and stage mapping. It preserves the
authored positive, near-non-trigger, missing-input, authority and false-green
probes and adds per-step/per-module output and missing-handoff cases.
Optional pack modules have separate fallback challenges. Host loading and
reset have their own cases. A plan is not a generated executable test suite:
concrete fictional/public fixtures and independent outcome oracles must
be authored and reviewed before any run. The deterministic output cannot
establish semantic coverage, authorization or execution.

For optional comparative research, the [trial matrix](trial-matrix.md) freezes
matched control/baseline/candidate run identities against selected cases.
It is structural bookkeeping, not actual execution or native qualification.

## Handoff to native acceptance

1. Review each case against the actual skill and choose concrete safe input,
   independent observation and pass/fail criteria. Freeze the exact plan
   digest and fixture/oracle identities in private custody before running.
2. Obtain separate authorization for the actual native host and isolation.
   For a release, reconcile the exact source tree and selected archive's
   members/digests against this plan, then use the source-pinned manifest.
   If the package or adapter changed, regenerate and review the plan.
3. Observe each required case. Never derive a PASS from the plan, a missing
   dependency alone, a self-report or a green static check. Record failures,
   timeouts and unknowns separately. Keep evidence and raw prompts private.
4. Use the plan's receipt_stage_requirements as a **conjunctive** checklist:
   only claim a stage pass if every mapped case has independently supported
   successful observations. Missing or failed cases block that stage.
   For generated skills, use the detailed case ledger reconciler below.
   The six-stage [host acceptance checker](host-acceptance.md) alone cannot
   establish this coverage. No automatic evidence promotion is performed.

The CLI prints private design-derived text to stdout. Do not publish its
output, include it in a skill archive, or send it as anonymous feedback.
If Python is unavailable, perform the same bounded design-to-package review
manually and label the tool NOT_RUN.

## Reconcile the detailed case ledger

The optional read-only checker regenerates the plan from the exact design
and canonical package instead of accepting a potentially pruned plan.
It verifies the selected release archive's complete member inventory,
payload digests and CRC readback against the generated host member manifest.
Then it compares every case and derives each stage claim: any failure
wins; all passed means PASS_CLAIMED; all NOT_RUN means NOT_RUN; a mixture
with missing observations is UNKNOWN. The submitted stage receipt must
match these derived states exactly.

    python3 -B engine/builder/acceptance_ledger.py --design /private/design.json \
      --package /private/skill-slug --manifest /private/manifest.json \
      --archive /private/skill.zip --receipt /private/receipt.json \
      --ledger /private/cases.json

The ledger has exactly four top-level fields: schema_version (integer 1),
plan_sha256 (from the generated plan), receipt_sha256 (SHA-256 of the
raw receipt JSON file), and cases (one row for every generated case ID).
Each row has case_id, status, fixture_id, oracle_id and evidence_id.
Statuses are PASS_CLAIMED, FAIL_CLAIMED, NOT_RUN or UNKNOWN. Observed
claims need distinct non-placeholder opaque IDs for the concrete fixture,
independent oracle and evidence. Fixture IDs may be shared for the same
test input; oracle/evidence IDs must not be reused between cases or as
stage-level evidence. Unobserved rows have null evidence_id; fixture and
oracle IDs may both be null or both specified for prepared cases.
No extra case, dropped failure, or altered plan can be silently accepted.

Exit 0 means COMPLETE_CASE_CLAIMS_REVIEW_REQUIRED; exit 2 is HOLD or invalid
input. A match is a consistency check, not authenticated proof of execution,
fixture contents, preregistration timing, or independent consumer acceptance.
Keep the original case plan, private fixtures/oracles and raw observations
outside the distributed package. Do not publish or transmit them by default.

## Existing or manually authored skills

Use the same case-ledger engine without reconstructing a fictitious design
dossier. Read the complete package, obtain its exact inventory, then author
a reviewed source contract with explicit cases and unique verbatim anchors
in its actual normative instructions. The read-only tool can list its
Git blob identities and SHA-256 values:

    python3 -B engine/builder/source_acceptance.py --package /private/skill-slug --inventory
    python3 -B engine/builder/source_acceptance.py --package /private/skill-slug \
      --contract /private/source-contract.json --host claude-apps

See the [Scheduled Work Proof Auditor pilot](examples/scheduled-work-source-contract.json):
three exact source blobs and nine concrete fictional cases. The [MCP Tool
Surface Auditor pilot](examples/mcp-tool-surface-source-contract.json)
adds seven exact source blobs, twelve cases, two script targets, separate
helper-unavailable and maintainer-suite boundaries, and an offline fictional
18-to-12 comparison oracle. Both native plans are NOT_RUN, not native-host
passes. The offline fixture test is separate from actual host activation.
The authority-boundary batch adds [Decision Record Steward](examples/decision-record-steward-source-contract.json),
[Agent Workspace Footprint Assessor](examples/agent-workspace-footprint-assessor-source-contract.json)
and [Connector Capability Risk Review](examples/connector-capability-risk-review-source-contract.json).
Each adds ten source-anchored cases, including independent outcome, authority,
missing capability and false-success challenges. These are plans, not observations. The contract's fields are schema_version, skill,
source_blobs (complete path-to-Git-blob-ID map), and cases. Each case has
id, kind, source (package-relative Markdown path), anchor (unique exact
excerpt), setup and expected. Required kinds are load, positive,
near-non-trigger, outcome, missing-input, false-green, dependency-unavailable,
authority-boundary and cleanup. Each recognized script resource (including
PowerShell and Windows command scripts) must be explicitly covered by both
a resource case and a dependency-unavailable case. These two case kinds
accept a nonempty resource_paths list of exact package-relative members;
other kinds cannot declare that field. A case may cover several related
paths if the concrete fixture and oracle actually check them all. For
resources used only by maintainers or tests, verify presence and the
safe non-invocation boundary rather than requiring a consumer to run them.
The unavailable-capability case must preserve a valid fallback or HOLD;
never execute code just to prove it exists. Plans bind every target's SHA-256.
Nested entrypoints each require an anchored nested-skill case.
These are structural coverage minima, not exhaustive semantic coverage.
Core cases must cite normative instructions, not just test examples.

The tool verifies actual Git blob identities (historical source pins, not
authenticated trust), records SHA-256 of every canonical member and host
transformation, and maps each case into the same six stages. Review all
essential capabilities and add cases as needed. A changed source requires
re-review, not blind repinning. Use the same acceptance_ledger.py command
with --source-contract instead of --design to regenerate the source plan,
verify exact archive member bytes and reconcile case results. Never infer
real execution or approval from a coherent ledger. Keep consumer inputs and
observations private.

The [Effort Allocation Navigator source contract](examples/effort-allocation-navigator-source-contract.json) covers 18 exact files, 18 cases and seven Python resources, including protected priority, bounded choices, focus continuity, snapshot identity, capacity, authority and preference retention. Its separate offline focus oracle is not evidence of native activation or real productivity improvement.

The [File Lifecycle Curator source contract](examples/file-lifecycle-curator-source-contract.json) covers 33 source files, 24 cases and 12 Python resources. It separates read-only curation, private checkpoint writes, stale/revoked evidence, visual progress, and scheduler authorization. Its offline visual fixture checks one receipt-attested relocation out of three planned; native operation and real provider behavior remain NOT_RUN.

The [Repository README Architect source contract](examples/repository-readme-architect-source-contract.json) binds 18 files, 17 cases and seven Python resources. It challenges false Gold acceptance, exact-head drift, generated ownership, substantive preservation, reader success and unauthorized side effects. Its focused offline negative control does not establish actual rendered usability or newcomer acceptance.

The [CI Guard source contract](examples/ci-guard-source-contract.json) binds 55 files, 26 cases and 24 Python resources. It explicitly challenges nested duplication, independent native/release obligations, draft deferral, exact-head receipt integrity, required-check authority and unmeasured savings. The two focused offline overlap controls do not establish actual provider behavior or economic benefit.

The next evidence-boundary batch adds [Privilege Exposure Mapper](examples/privilege-exposure-mapper-source-contract.json), [Research Methods Appraiser](examples/research-methods-appraiser-source-contract.json), [Research Question Dossier](examples/research-question-dossier-source-contract.json) and [Statement Variance Reviewer](examples/statement-variance-reviewer-source-contract.json), ten scenarios each. The shared corpus regression discovers every *-source-contract.json example, verifies exact authored inventory and assessed-host plans, and preserves a minimum reviewed coverage floor so missing contracts or shrinking cases cannot silently disappear. Focused executable oracles remain separate. Existing documented package holds must be explicitly accommodated before extending the matrix to a held package; do not skip arbitrary failures.

The progress and communication batch adds [Work Period Evidence Reporter](examples/work-period-evidence-reporter-source-contract.json), [Personal Operations Control Board](examples/personal-operations-control-board-source-contract.json), [Evidence Narrative Composer](examples/evidence-narrative-composer-source-contract.json) and [Learning Evidence Progression](examples/learning-evidence-progression-source-contract.json). Ten cases each bind actual source instructions to distinct fictional checks for delivery evidence, attribution, bounded priorities, safe drafts, disclosure, demonstrated learning and unavailable host capability. No observed host acceptance is asserted.

The business, taxonomy and creative batch adds [business-presence-observatory](examples/business-presence-observatory-source-contract.json), [professional-market-evidence-scout](examples/professional-market-evidence-scout-source-contract.json), [develop-melodic-motif](examples/develop-melodic-motif-source-contract.json), [metadata-taxonomy-steward](examples/metadata-taxonomy-steward-source-contract.json), [narrative-scene-gap-audit](examples/narrative-scene-gap-audit-source-contract.json), [character-motivation-interview](examples/character-motivation-interview-source-contract.json). Ten scenarios each bind exact source bytes to fictional acceptance expectations, including audience boundaries, actual evidence, creative ownership and unavailable capability. No native host acceptance is asserted.

The evidence adjudication batch adds [claim-evidence-adjudicator](examples/claim-evidence-adjudicator-source-contract.json), [agent-failure-boundary-analysis](examples/agent-failure-boundary-analysis-source-contract.json), [source-debt-triage](examples/source-debt-triage-source-contract.json), [decision-tradeoff-workbench](examples/decision-tradeoff-workbench-source-contract.json). Thirteen cases per package distinguish mechanical evidence checks, safe unavailable-capability fallbacks, maintainer resources, source authority and actual outcome claims. No native host acceptance is asserted.

The refinement and trial-evidence batch adds [recursive-refinement-trace](examples/recursive-refinement-trace-source-contract.json), [evidence-driven-refinement-loop](examples/evidence-driven-refinement-loop-source-contract.json), [skill-trial-evidence-auditor](examples/skill-trial-evidence-auditor-source-contract.json). Cases protect observed-only trace semantics, held-out isolation, frozen acceptance, canonical versus local preference routing, independent evidence, non-trigger controls and truthful effect claims. Script and maintainer resources have explicit unavailable-capability cases. No native trial or improvement is asserted.

The continuity and delivery batch adds [context-continuation-contract](examples/context-continuation-contract-source-contract.json), [first-run-experience-validator](examples/first-run-experience-validator-source-contract.json), [repository-delivery-assessor](examples/repository-delivery-assessor-source-contract.json), [release-evidence-reconciler](examples/release-evidence-reconciler-source-contract.json), [pr-integration-surgeon](examples/pr-integration-surgeon-source-contract.json). These cases preserve current authority, intermediate handoff safeguards, fresh-host first value, exact-head checks, release channel coverage and independent outcome evidence. No native behavioral acceptance is asserted.

The federation, reference and technology intelligence batch adds [federated-source-catalog](examples/federated-source-catalog-source-contract.json), [reference-integrity-auditor](examples/reference-integrity-auditor-source-contract.json), [technology-change-intelligence](examples/technology-change-intelligence-source-contract.json). These cases challenge typed identities, incomplete enumeration, viewer confidentiality, source-bound handoffs, link absence proof, scoped graph impact, interest scope, source-lane coverage and dated change evidence. No native behavioral acceptance is asserted.

The final authored batch adds [healthcare-contract-forensics](examples/healthcare-contract-forensics-source-contract.json), [sandler-conversation-strategist](examples/sandler-conversation-strategist-source-contract.json), [meddpicc-opportunity-assurance](examples/meddpicc-opportunity-assurance-source-contract.json), [offline-hyperv-qual-vm](examples/offline-hyperv-qual-vm-source-contract.json). Corpus qualification now requires exact equality between registered authored skills and reviewed contracts. The four documented Hyper-V package holds require the exact listed unsupported PowerShell resource blockers and a failed plan attempt (HOST_PACKAGE_HOLD); they are not successful plans. All other assessed pairs require normal source-bound NOT_RUN plans. Native behavior and consumer outcomes remain unobserved.

## Bind a reviewed source contract to locally built/downloaded bytes

Use the read-only release handoff after an approved release manifest and exact host asset are available:

```sh
python3 -B engine/builder/release_handoff.py --contract engine/builder/examples/scheduled-work-source-contract.json --package skills/authored/scheduled-work-proof-auditor --manifest /approved/authored-download-manifest.json --archive /approved/scheduled-work-proof-auditor-gemini.zip --host gemini-apps
```

This regenerates the source plan, hashes the actual manifest and asset, verifies every adapted archive member and reconciles a deliberately unexecuted receipt and complete case ledger. The returned `receipt_json` and `ledger_json` are exact UTF-8 payload strings; if the authorized host saves them, write the strings as-is without appending a newline or changing JSON formatting. A successful handoff is **DESIGNED_NOT_RUN**; it does not authenticate publication, permissions, the host or any observations. It performs no writes. Use independently verified publication/source provenance and separate execution authority before a trial. Held/unassessed profiles fail closed.

The existing authored-download qualification job consumes its actual builder output (no second archive build) and exercises every registered assessed pair, every documented hold, unassessed hosts, wrong archive routing and a deliberately rehashed altered member. Local build integration is not evidence of public delivery, attestation or native installation.
