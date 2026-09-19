# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-09-19 |
| **Milestone** | Core passive architecture complete |
| **State** | Governed curation mode |
| **Repository type** | Passive skill knowledge resource |
| **Reference surface** | 500+ first-party + pinned external skill/reference artifacts |
| **First-party skills** | 44 |
| **First-party provenance complete** | 44 / 44 |
| **Persisted third-party review companions** | 586 |
| **Pinned external corpora** | 12 |
| **Registered source identities** | 20 |
| **Anthropic Skills current-standard companions** | 17 / 17 |
| **Anthropic Knowledge Work Plugins current-standard companions** | 74 / 74 |
| **Anthropic Knowledge Work Plugins current-standard gaps** | 0 |
| **AWS current-standard companion complete** | 72 / 72 |
| **Microsoft Skills current-standard companions** | 186 / 186 |
| **Microsoft Azure Skills current-standard companions** | 34 / 34 |
| **Cole Medin Skills current-standard companions** | 33 / 33 |
| **David Ondrej Skills current-standard companions** | 49 / 55 |
| **David Ondrej Skills current-standard gaps** | 6 |
| **Corey Haines Marketing Skills tracked denominator** | 50 |
| **Corey Haines Marketing Skills current-standard companions** | 0 / 50 |
| **Matt Pocock Skills current-standard companions** | 29 / 29 |
| **Cloudflare Skills current-standard companions** | 13 / 13 |
| **Addy Osmani Agent Skills current-standard companions** | 24 / 24 |
| **Vercel Agent Skills current-standard companions** | 9 / 9 |
| **OpenHands Extensions current-standard companions** | 1 / 1 |
| **Google Agents CLI current-standard companions** | 7 / 7 |
| **Cline Skills published current-standard companions** | 36 / 36 |
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

- First-party: **44/44 provenance-complete**.
- Anthropic Skills: **17/17**, gaps **0**, **10 verified / 7 rejected unchanged**.
- Anthropic Knowledge Work Plugins: **74/74**, gaps **0**, historical states **36 verified / 38 rejected unchanged**.
- AWS Agent Toolkit: **72/72**, gaps **0**.
- Microsoft Skills: **186/186**, gaps **0**.
- Microsoft Azure Skills: **34/34**, gaps **0**.
- Cole Medin Skills: **33/33**, gaps **0**.
- David Ondrej Skills: exact registered-pin denominator **55**, **49/55** provenance/verification companion complete, gaps **6**; current decisive states **18 verified / 31 rejected unchanged**. Skill authoring is **4/4** complete; agent orchestration is **17/17** complete; ops-and-setup is **11/11** complete; research-and-web is **10/10** current-standard complete; thinking-and-docs is **7/13** reviewed.
- Corey Haines Marketing Skills: tracked at exact snapshot `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`; exact eligible denominator **50** top-level first-class `skills/<name>/SKILL.md` packages; **0/50** individually current-standard reviewed. Root license is MIT. Partner/integration guides, source-owned CLI/tooling, generated partner surfaces, and ordinary reference Markdown do not count toward the skill denominator.
- Matt Pocock Skills: **29/29**, gaps **0** after source-policy exclusions.
- Cloudflare Skills: **13/13**, gaps **0**, **11 verified / 2 rejected unchanged**.
- Addy Osmani Agent Skills: **24/24**, gaps **0**.
- Vercel Agent Skills: **9/9**, gaps **0**, **6 verified / 3 rejected unchanged**.
- OpenHands Extensions: **1/1**, gaps **0**; `theme-factory` remains **rejected unchanged 14/20**.
- Google Agents CLI: **7/7**, gaps **0**, all seven verified.
- Cline Skills: **36/36 published**, gaps **0**; internal/unlisted `review-team` remains outside the denominator.
- Microsoft direct `.NET`: **29/29**; Java: **26/26**; Python: **40/40**; Rust: **9/9**; TypeScript: **25/25**.

Completion means decisive current evidence for every eligible package, not universal approval. Rejected/retired material remains useful bounded prior art.

## David Ondrej denominator reconciliation

The registered public snapshot is `7d0ef87dad1f638cab58995eead9e0e6e3fae237`. Direct inspection establishes five category folders with **17 + 11 + 10 + 4 + 13 = 55** first-class skill packages. Current repository evidence contains forty-nine exact-version companion pairs. Skill authoring is **4/4** current-standard complete, agent orchestration is **17/17** current-standard complete, ops-and-setup is **11/11** current-standard complete, research-and-web is **10/10** current-standard complete, and thinking-and-docs is **7/13** reviewed.

Existing detailed package-level findings remain authoritative in their exact-version verification companions. The current thinking-and-docs frontier includes `ask-then-build`, `before-building`, `brain-to-docs`, `decisions`, `level-up`, `next-decision`, and `prompt-me`.

`prompt-me` is **rejected unchanged 11/20**. It is explicitly draft and contains a useful seed for interviewing the user about remaining work, avoided work, importance, and non-importance, but it does not yet provide a production-usable interview procedure, adaptive question-selection logic, stopping rule, evidence discipline, prioritization synthesis, output contract, or failure behavior. No authority-boundary defect is asserted for this package. Behavioral validation is `not-run`.

Together the David Ondrej family is **49/55**, with **6** gaps and **18 verified / 31 rejected unchanged**.

## Corey Haines source admission

Issue #297 established the exact source identity `coreyhaines31/marketingskills` and admitted it as a **tracked corpus**, not as a blanket trusted or pinned-reference corpus. The registered snapshot is `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` (upstream v2.11.1 state). Direct tree inspection shows **50** top-level skill directories under `skills/`, and source guidance defines each `skills/<name>/SKILL.md` as the required first-class skill entry point. Root terms are MIT. Commercial partner/integration material and source-maintained tooling remain source context and are excluded from the 50-skill denominator. Individual unchanged reuse still requires exact-version review.

## Source lifecycle

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

Discovery is intelligence only. Popularity, branding, creator reputation, and source-level signals never prove individual skill quality.

## Quality model

Every governed user-facing skill must retain truthful provenance and applicable exact-version evidence before being called companion-complete. `verified` means exact material passed structured static semantic review. `validated` additionally requires representative external behavioral/adversarial evidence. `stale`, `rejected`, and `retired` are excluded from normal unchanged reuse while remaining useful evidence where appropriate.

Interpret candidate material in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation priority

1. Continue corpus-wide provenance audit #66. David Ondrej Skills is now **49/55**, with **6** exact-version companion gaps; skill authoring, agent orchestration, ops-and-setup, and research-and-web are complete at **4/4**, **17/17**, **11/11**, and **10/10**.
2. Continue David Ondrej thinking-and-docs, now **7/13**, checking current companions and recoverable history before fresh review of each genuine gap.
3. Begin selective exact-version curation of the newly admitted Corey Haines Marketing Skills **50-skill** tracked corpus after higher-priority admitted-source gaps, starting with high-differentiation user-fit candidates rather than wholesale approval.
4. Continue recomputing remaining admitted and tracked families for genuine provenance, fingerprint, exact-pin, or canonical-path gaps.
5. Continue governed discovery/source-vetting and omission recovery.
6. Resolve bounded candidate issues when evidence supports a decisive outcome.
7. Keep README, this file, `CURATION_QUEUE.md`, `INDEX.md`, and `index.json` aligned with live evidence.

The living work surface is `CURATION_QUEUE.md` plus applicable open evaluation/provenance issues. Historical closed Wayfinder/issues/PRs remain evidence, not active execution plans.
