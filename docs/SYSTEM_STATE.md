# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-10 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 44 |
| **First-party provenance complete** | 44 / 44 |
| **Persisted third-party review companions** | 466 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 19 |
| **Anthropic Skills current-standard companions** | 17 / 17 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Azure Skills current-standard companions** | 34 / 34 |
| **Cole Medin Skills current-standard companions** | 33 / 33 |
| **Matt Pocock Skills current-standard companions** | 29 / 29 |
| **Cloudflare Skills current-standard companions** | 13 / 13 |
| **Addy Osmani Agent Skills current-standard companions** | 24 / 24 |
| **Vercel Agent Skills current-standard companions** | 9 / 9 |
| **Google Agents CLI current-standard companions** | 7 / 7 |
| **Google Agents CLI current-standard gaps** | 0 |
| **Cline Skills published current-standard companions** | 36 / 36 |
| **Cline Skills published current-standard gaps** | 0 |
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

- First-party: **44/44 provenance-complete** with structured semantic review evidence.
- Anthropic Skills: **17/17**, gaps **0**, historical distribution **10 verified / 7 rejected unchanged**.
- AWS Agent Toolkit: **72/72**, gaps **0**.
- Microsoft Skills: **186/186**, gaps **0**.
- Microsoft Azure Skills: **34/34**, gaps **0**.
- Cole Medin Skills: **33/33**, gaps **0**.
- Matt Pocock Skills: **29/29**, gaps **0** after excluding `deprecated` and `in-progress` per source policy.
- Cloudflare Skills: **13/13**, gaps **0**, **11 verified / 2 rejected unchanged**.
- Addy Osmani Agent Skills: **24/24**, gaps **0**.
- Vercel Agent Skills: **9/9**, gaps **0**, **6 verified / 3 rejected unchanged**.
- Google Agents CLI: exact registered-pin denominator **7**, **7/7** provenance/verification companion pairs, gaps **0**, all seven verified at pin `ef7808f33fc3038112b69d4ad488ce33b72699b1`.
- Cline Skills: exact published denominator **36**, **36/36** provenance/verification companion pairs, published gaps **0**, at pin `26378461e978f2b4e2e6d67b57121b86b2a79ba5`; the internal/unlisted `review-team` record remains separate from the published denominator.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## Cline Skills reconciliation

Source queue #27 records the finite public Cline corpus as **36/36 published skills reviewed**, plus a separate internal/unlisted `review-team` record. The source registry pins Cline Skills at `26378461e978f2b4e2e6d67b57121b86b2a79ba5`.

After the passive-tree migration, current `main` retained only six published companion pairs plus `review-team`. Superseded PR #42 preserved exact package-level provenance and verification evidence for all 37 records under canonical `skills/sources/cline-skills/...` paths. The 30 genuinely missing published pairs have been recovered while the seven records already modernized on `main` were left untouched. This yields **36/36 published current-standard companion completeness** without counting the internal record in the published denominator or inventing behavioral evidence.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue the corpus-wide provenance audit in issue #66 by testing the Anthropic Knowledge Work Plugins per-package historical-mapping blocker against current evidence; if still blocked, select the next admitted family with a truthful current-standard gap.
2. Continue governed discovery/source-vetting and omission recovery.
3. Resolve bounded candidate issues when evidence supports a decisive outcome.
4. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.