# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-07 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 43 |
| **First-party provenance complete** | 43 / 43 |
| **Persisted third-party review companions** | 402 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Skills current-standard gaps** | 0 |
| **Microsoft Azure Skills current-standard companions** | 34 / 34 |
| **Microsoft Azure Skills current-standard gaps** | 0 |
| **Cole Medin Skills current-standard companions** | 13 / 33 |
| **Cole Medin Skills current-standard gaps** | 20 |
| **Microsoft .NET direct-package companions** | 29 / 29 |
| **Microsoft Java direct-package companions** | 26 / 26 |
| **Microsoft Python direct-package companions** | 40 / 40 |
| **Microsoft Rust direct-package companions** | 9 / 9 |
| **Microsoft TypeScript direct-package companions** | 25 / 25 |
| **Evaluation model** | Static semantic review first; optional later external behavioral evidence |
| **Repository runtime/CI requirement** | None |

## Current architecture

The canonical boundary is stable: user-facing material lives under `skills/`; intact pinned upstream corpora live under `skills/sources/<source-id>/`; passive repository-use/curation procedures live under `engine/skills/` and are excluded from user-facing counts; provenance and exact-version evidence live under `registry/`.

`skillz` owns no runtime, scripts layer, tests gate, CI workflow, scheduler, monitor, crawler, installer, synchronizer, preflight process, generator, background service, vector database, autonomous observer, or personalization service. Tooling inside pinned third-party repositories remains upstream package material.

## Inventory boundaries

- First-party: **43/43 provenance-complete** with structured semantic review evidence.
- AWS Agent Toolkit: **72/72** current-standard companion-complete.
- Microsoft Skills: **186/186** companion-complete, **0 gaps**.
- Microsoft Azure Skills: exact registered-pin denominator **34**, **34/34** companion-complete, **0 gaps** at pin `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Cole Medin Skills: exact registered-pin denominator **33**, **13/33** companion-complete, **20 gaps** at pin `fb2e876f057c5356d6603ba0c52d6b4418d893ba`.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Microsoft Azure Skills denominator reconciliation

The exact pin exposes 28 canonical plugin skill roots. Recursive package-tree review establishes one additional first-class nested `SKILL.md` under `azure-kubernetes/azure-kubernetes-automatic-readiness` and five additional nested first-class `SKILL.md` packages under `microsoft-foundry` beyond the Foundry root: `finetuning`, `models/deploy-model`, and its `capacity`, `customize`, and `preset` children. That yields an eligible denominator of **34**, exactly matching the 34 current provenance and verification companion pairs.

The prior **131** denominator counted ordinary workflow, procedure, reference, example, SDK, or other Markdown as independent skills. Current governance explicitly excludes ordinary reference Markdown that is not independently first-class skill content. The same distinction previously corrected the Microsoft Skills denominator from 189 to 186. Microsoft Azure Skills is therefore current-standard complete at **34/34**, not 34/131.

The latest package-level Azure reconciliation remains `python-appservice-deploy`, rejected unchanged **12/20**, bound to exact tree `6e11dad529e50b7fbc37191de665788d0427ccad`, `SKILL.md` blob `ac25db692762945d0e3e9ed2016dcfa29fbfa610`, and canonical Azure plugin-path freshness revision `82492494405b948c8422766ddae390714bbd78ed` on 2026-06-15. Behavioral validation remains `not-run`.

## Cole Medin Skills frontier

The registered pin contains **33** first-class `.claude/skills/*/SKILL.md` entries. Thirteen now have current companion pairs: `ablate-ai-layer`, `rules-check-drift`, `second-brain-audit`, `agent-browser`, `ast-grep`, `build-dark-factory`, `hooks-create`, `opportunity-scan`, `piv-commit`, `piv-create-pr`, `piv-fix-review-findings`, `piv-implement-issue`, and `piv-implement`.

`piv-implement` is bound to exact package tree `f441f4997c7656134a4081b261a36031bca15efe`, `SKILL.md` blob `4af15c77bd319df84630363a9ab4f29494ea31fa`, and skill-path freshness revision `1c46cd18bc6100d358082c06357d649f7a4cf8c6` on 2026-08-09. It is rejected unchanged **14/20** with behavioral validation `not-run`. Preserve its full-plan reading, ordered task execution, per-task `VALIDATE` gating, full validation reruns, final verification, and structured implementation/deviation reporting. Unchanged operational use fails the authority hard rule because it may create a feature branch and mutate source, tests, documentation, and repository report files without mandatory action-specific authorization immediately before those consequential mutations. Plan-supplied validation commands are also executed exactly as written without an explicit hostile-instruction or command-safety boundary.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue Cole Medin Skills exact-version curation from the registered 33-skill denominator, checking existing companions and prior evidence before every unit.
2. Reconcile historically completed external corpora from compatible prior evidence before fresh re-review.
3. Continue governed discovery/source-vetting and omission recovery.
4. Resolve bounded candidate issues when evidence supports a decisive outcome.
5. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
