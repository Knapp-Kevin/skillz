# Per-source retirement eligibility for historical Skillz entrypoints

Date: 2026-11-18 (owner local). Scope: the 44 rights-uncertain historical entrypoints mapped into 21 independently authored replacements under [issue #738](https://github.com/Knapp-Kevin/skillz/issues/738). This document is a **conservative maintainer release procedure**, not an instruction to delete anything.

## Owner decision and current hold

The owner permits removing previous `skills/` entrypoints **once the replacement is demonstrably successful and the owner is comfortable with the evidence**. This conditional direction is not a present assertion that any of the 44 historical sources has qualified. Every source remains RETIREMENT_HOLD in the [per-source ledger](../../registry/evaluation/frostwulf-paired-host-status-20261118.json), including the proposed pilot in PR #737. A successful GitHub merge, static 18/20 review, low textual overlap or a 1.1.0 label is insufficient to lift the hold.

**Not every consolidation yields equivalent source modes.** The 17 former topic-pulse skills must each be accepted under their own profile. A passing `github-discovery` profile does not validate `openai-developer`, `mcp-protocol` or any other profile. A combined source can be retired piecemeal only when the exact original's functionality, trigger and negative behavior were separately covered.

## Owner-approved controlled-emulation exception, November 18, 2026

The owner has explicitly revised the acceptance method: independently observable
external model-host execution is **preferred but not mandatory** when unavailable.
A specific source may be retired after a documented, source-bound **controlled
emulation and/or real procedure test** demonstrates essential outputs and safety
requirements sufficiently for an owner's informed decision. The report must
distinguish actual commands executed, deterministic source/fixture checks,
analyst-emulated outputs, and independent model executions. Do not invent a
model-run ID or treat any emulation as proof of an observed model-host A/B pair.

This is a narrow **owner risk-acceptance path**, not permission to silently
waive every safety and integrity requirement for the remaining 44-source
migration. For a proposed retirement:

- Pin the exact old entrypoint and all actually known supporting files;
  preserve immutable Git history and rights notices. If the full original
  directory cannot be enumerated, **only remove the exact inspected active
  entrypoint**. Do not sweep unknown siblings or claim package completeness.
- Execute representative synthetic tasks wherever an authorized safe
  environment exists, with real local operations for data collection when
  feasible; independently document essential outcomes, adversarial refusals,
  unknowns and any critical loss. Emulation counts as controlled acceptance
  only in the specific scope its tests actually covered.
- Reconcile the **known** canonical name index, capabilities, local
  verification, category navigation and active README references before
  removal. If exhaustive source-tree/code-search coverage is unavailable,
  record the **consumer audit as partial** and obtain specific informed
  owner risk acceptance; retain immutable source links for rollback. Never
  describe a partial scan as complete.
- Require no known active broken route, no unwaived critical safety
  regression, and explicit owner authorization to take the narrowly
  scoped irreversible Git-tree deletion step. Retention in Git history
  makes this reversibly deployable by a new commit, not a legal license grant.
- Preserve behavioral state as NOT_RUN when there were no independent
  host/model executions. Mark procedural/emulated qualification in a
  *separate receipt*. Mark 1.5× improvement NOT_PROVEN unless measured
  with the governed comparable scoring method.
- Record any exception as `OWNER_ACCEPTED_CONTROLLED_EMULATION` and
  identify unresolved original-package and consumer-coverage limits.
  Scope the exception per historical entrypoint; it is **not**
  a blanket qualification for all remaining sources.

The initial exception covers `skills/todo-harvester/SKILL.md` only,
supported by [five controlled checks](../evals/receipts/2026-11-18-todo-harvester-controlled-procedure.json)
and [independently pinned source/active-navigation review](../reviews/2026-11-18-todo-controlled-procedure-retirement.md).
A future stricter host-observed parity result may supersede this limited
acceptance but must not be invented retroactively.

## Non-compensatory retirement checklist

All of the following must be recorded **for the exact historical entrypoint**, not merely its replacement package:

1. **Complete original package fingerprint.** Resolve its full directory content from a pinned commit using an authorized read-only Git tree enumeration. Verify the real Git object identities for SKILL.md **and every dependency** including `sources.json`, references, examples, media, license notices, templates, scripts, nested directories, symlinks and submodules. Record executable support files as data and never run them during source audit. If source-tree enumeration is truncated, lacks an expected referenced file or returns conflicting identities, mark PACKAGE_INCOMPLETE and stop.
2. **Independent authored package integrity.** Verify the replacement's exact blob and full package tree against the governed authored index and companions. Confirm names, capability routes, all referenced files, rights and authority classification. A source-content update invalidates materially affected prior behavioral results.
3. **Function-by-function outcome acceptance.** Cover the historical trigger, non-trigger, expected artifact and recipient workflow; complete the five preregistered nominal/challenging/missing-evidence/adversarial/integration paired tests at minimum. Any material historical feature that cannot be tested must be explicitly classified as an intentional, safety-based restriction or an unresolved regression, never silently dismissed. Critical capability loss blocks retirement unless the owner deliberately accepts the narrower successor with its lost function documented.
4. **Host observation and adjudication.** Obtain independently executed, isolated original/replacement host-agent runs with genuinely equal constraints, capture observed outputs and effects, have a separate adversarial reviewer adjudicate them, and keep both PASS and FAIL evidence. A deterministic schema check or source-level interpretation is **not** a host pass.
5. **Safety and permitted authority.** Zero unwaived unauthorized writes, external sends, secret exposure, cross-account reads, uncontained source-code execution, new schedules or false completion. Existing owner's permission to maintain Skillz is not authority to use customer accounts or run risky historical commands. Abort unsafe live scenarios or use synthetic controlled environments.
6. **Quality target disposition.** Report the user-requested >=1.5× improvement target with actual comparable case-level scores, resource costs, sample limitations and confidence. If not measurable, below target or mathematically impossible on the bounded quality score, mark NOT_PROVEN / BELOW_TARGET / CEILING_UNATTAINABLE respectively, with actual historical baseline and attainable maximum. Request an explicit owner choice whether to retain the original despite functional equivalence; never say the improvement target passed. A score ceiling is not proof of parity, and a parity pass is not proof of measured superiority. Improvement cannot compensate for missing a critical outcome.
7. **Historical rights and preservation.** Historical authorship/copyright remains unresolved merely because old files were stored in an owner-controlled account. Preserve exact commit IDs, original file paths, package tree, attribution, known notices and prior review records. Confirm that removing the active tree does not destroy required attribution/history or relicense the historical expression. If a copyright/license uncertainty affects redistribution, preserve the evidence and resolve it separately; deletion is not proof of originality.
8. **Consumer/reference graph.** With an exhaustive **untruncated** repository tree and a bounded, authorized native search, inspect all active README, skill index, capability mapping, routing, registry, source/verification companions, templates, examples, source manifests and internal links. For each incoming reference, either retarget to a validated source, retain an explicit historical evidence link or classify a documented unresolved consumer. A GitHub code-search zero-result response is **not** a complete repository scan.
9. **Owner acceptance and atomic retire.** Present a named source-retirement receipt: `exact old package | new package profile | five scenarios | observed negative gates | quality target | rights | complete consumer resolution | rollback commit`. Only after an explicit owner acceptance of the observed evidence may a narrowly scoped PR remove the original's active entrypoint and exclusively owned supporting files, while preserving immutable historical references. Never delete shared assets or sweep other historical skills.
10. **Exact-head verification.** Before merge, re-run available safe maintainer reference and routing checks at the *actual* prospective commit head, verify branch/conflict and index/README/graphic counts, and confirm that active selection routes point to qualified replacements. After merge, read live `main` for absence of the old active package, preserved history, correct links and consistent counts. If any test fails, keep HOLD and restore the consumer path.

## Safe package enumeration guidance for an independent maintainer host

Prefer a scope-limited GitHub Git Trees API read of the pinned commit:
`GET /repos/{owner}/{repo}/git/trees/{commit_sha}?recursive=1`.
The external host must require the returned tree to be `truncated == false`, select entries under **exact original directory prefixes**, compare SHA and mode/type for every entry, and separately detect submodules (160000), symlinks (120000), nested references and unexpected paths. This is a **suggested read-only API operation** to be implemented in an authorized independent host, not a command that Skillz itself runs. For very large repositories, use paginated or recursive subtree-specific listing backed by full coverage receipts and compare each subtree SHA; never infer completeness from a partial API response. Any target whose nested assets cannot be enumerated remains blocked.

No local Git command is assumed safe merely because it is read-only: system/global/repository configuration, pagers, fsmonitor and hooks can execute code, and user-controlled paths can escape a naive workspace boundary. A maintainer may use local Git only in a separately contained, explicitly authorized environment with those execution surfaces controlled. Do not run historical scripts, package installers, commands embedded in old skill text or external evaluator tools during passive source inventory.

## Earliest retirement pilot

The old `skills/todo-harvester/` pilot [PR #737](https://github.com/Knapp-Kevin/skillz/pull/737) was a stale HOLD based on the earlier, strict independent-host-only policy. A newer, controlled-emulation evaluation has been performed and separately documented under the owner-approved exception above. This qualifies **only the exact active SKILL.md for a narrowly scoped retirement** after canonical route checks; full old package enumeration and exhaustive consumer scan are not established, and no claim of model-host parity or 1.5× gain follows. Other historical entries remain held pending their own evaluations.

## State semantics

`NOT_DESIGNED` means no preregistered paired case; `DESIGNED` means a fixture only; `NOT_RUN` means no observed model-host run; `PAIR_COMPLETE` means two observations exist without necessarily passing; `PARITY_PASS` means all critical required functions/safety conditions are met for a specific original; `RETIREMENT_QUALIFIED` requires every gate above plus owner evidence acceptance. `RETIRED_ON_MAIN` is reserved for a subsequently verified merge, never for an approved plan or a draft PR.

Reviewers must also inspect the [paired protocol](frostwulf-paired-evaluation-protocol.md), [issue #738](https://github.com/Knapp-Kevin/skillz/issues/738), and governing [static review/freshness policy](../static-review-and-freshness.md). No change here authorizes a scheduled task, source install, agent execution, customer account access, or source deletion.

## Second source-bound controlled acceptance, November 19, 2026

Historical `skills/agent-postmortem/SKILL.md` has a verified untruncated one-file Git directory tree (`cceb115c92467cd3be2a997484ef6756a47b6f58`), historical blob `dde789e87da090b92021b3e55304299244f62ac2`, and an exact unchanged authored replacement package tree `426391a3bea7e75f364fe86da8845dee2718f8a5` (v1.1.0). [Five single-analyst synthetic incident reports](../evals/receipts/2026-11-19-agent-postmortem-controlled-report-evaluation.json) passed bounded report-oracle checks. This is not a paired independent host test and did not establish measured superiority, real user-outcome verification or exhaustive consumer resolution. The owner-authorized controlled-emulation risk exception applies **only** to this exact second source; all other originals remain on HOLD. The [specific review](../reviews/2026-11-19-agent-postmortem-controlled-retirement.md) records known route reconciliation and rollback identity.

## Two further controlled evaluations, November 19, 2026

The historical single-file entrypoints `automation-receipts` (directory tree `39a8e08f7037fca28665b33edcc9d93314059c2d`) and `decision-log` (`ca790304801fd1717841a8fab98bb4ebeed4c9bf`) were fully inventoried at original pinned source and current main. Their independent successors have full package trees `bd9254ce997d807b1bfe91c820b820fd51ae9cfc` and `56b32d80412fbae75f05914e992156f081d8ce05`. [Ten tested synthetic scenarios](../evals/receipts/2026-11-19-automation-decision-controlled-procedures.json) passed (five per mode), including a separate synthetic write/readback. These are deterministic procedural emulations, **not** model-agent A/B evidence, full consumer coverage, or a measured 1.5× gain. Owner risk acceptance applies only to these exact source-bound retirements. See their [automation review](../reviews/2026-11-19-automation-receipts-controlled-retirement.md) and [decision review](../reviews/2026-11-19-decision-log-controlled-retirement.md).

## Fifth bounded controlled review, November 19, 2026

Historical `permissions-review` blob `18f46840032829963715ec23894f7826dbbfcb77`, complete single-file tree `e942297c3e343ad5af388b23604987a9bb49322d`, compared with separately authored `privilege-exposure-mapper` full package tree `0bcb42382d152636c4b9f7c6c70367eb52633740`. [Five synthetic security/control cases](../evals/receipts/2026-11-19-permissions-review-controlled-security.json) passed under ephemeral Python graph traversal and deterministic simulation; no private source read, real permission edit or external send occurred. This is **not** an independent original-versus-new host-agent A/B or proven 1.5× improvement, and exhaustive consumer reference coverage remains unverified. Rights/attribution remain historically preserved. Narrow owner risk acceptance applies to this exact source, not remaining originals; [individual source review](../reviews/2026-11-19-permissions-review-controlled-retirement.md).

## Sixth controlled source exception, November 19, 2026

`mcp-vetting` original blob `37a13d7296c7d3d87dc360988bc6aca1f873c4db`, full single-file directory tree `a8824fff4a3d0ed5b7a82603b48f1aefbccb9666`, matches immutable historical source and pre-retirement main. Authored `connector-capability-risk-review` v1.2 has exact tree `26b1fa68302ce1fb088748edd98d9702b85de23d` and adds explicit as-of reporting and non-routine trigger boundary to prevent lost legacy outcomes. [Five controlled synthetic cases](../evals/receipts/2026-11-19-mcp-vetting-controlled-execution.json) exercised an actual offline Python JSON evaluator, not any installed MCP server, original or replacement skill through an independent model host. Source rights not established; no 1.5× improvement claimed, complete repo-wide consumer scan remains incomplete. [Specific retirement review](../reviews/2026-11-19-mcp-vetting-controlled-retirement.md).

## Seventh source-bound controlled procedure acceptance, November 19, 2026

Historical `agent-home-doctor` Git blob `3415f1f4bb72afc44266706be649c3950f809337`, full single-file tree `7e78ed3047b66c67c492eae1191853d6d7ce095e`; independent `agent-workspace-footprint-assessor` v1.2 full tree `0dbad84eadc96648879fdf2f279b07137d28d76c`. [Nine controlled synthetic filesystem procedures](../evals/receipts/2026-11-19-agent-home-controlled-filesystem.json) passed; seven static source assertions passed. Critical historical context-cost reporting and pre-mutation identity verification were corrected, and max authority now accurately mutating. These checks are **not** independent model-host A/B, real owner-data cleanup or a measured 1.5x improvement. Historical rights unresolved; complete consumer reference scan not established. This exception is narrowly source-bound. [Individual review](../reviews/2026-11-19-agent-home-controlled-retirement.md).
