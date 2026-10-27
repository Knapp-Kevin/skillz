# Governed discovery: Google ADK Recipes plugin skills (2026-10-27)

**State:** DISCOVERY / SELECTIVE SOURCE VET ONLY. This document does not register or admit a source, assert an eligible package denominator, approve installation, or claim package security/behavioral validation. Discovery was conducted by the external host, not by repository-owned automation.

## Discovery funnel for this cycle

Three public surface families were queried on 2026-10-27: (1) recent GitHub agent-skill/SKILL.md repositories and release coverage; (2) skills.sh / marketplace coverage; (3) Hugging Face skill coverage. The latter two mainly surfaced previously known general marketplace descriptions, security commentary, and unrelated tutorials, with **zero distinct eligible new candidate packages promoted from those results**. Recent Google coverage yielded the concrete [ADK Recipes announcement (2026-10-15)](https://developers.googleblog.com/three-layers-one-repo-a-tour-of-googleadk-recipes/), followed by independent live GitHub inspection. Do not count search results or marketing claims as verified skill candidates.

- **Distinct new canonical source leads promoted for tracking:** **1** (`google/adk-recipes`).
- **Actual first-class SKILL.md files inspected:** **3**, but only **2** are externally oriented retail plugin skills; the third is repository-maintenance guidance, not a user-facing skill candidate for `skillz`.
- **New source registrations / admitted skills / exact-version governed verification companions / package-security passes / behavioral validations:** **0 / 0 / 0 / 0 / 0**.
- A default-branch `skillz` code search for `google/adk-recipes` returned no matches. This is **preliminary name-based deduplication**, not a proof of absence under aliases or across all historical ledgers. Compare with registered Google Agents CLI and other Google/retail/RAG sources before issue-first intake.

## Canonical source evidence

- **Repository:** https://github.com/google/adk-recipes
- **Observed HEAD:** `45a6999ec8e391a75266ae9507e0e7ca2285ce8e` (2026-10-27 inspection).
- **License:** root Apache-2.0 LICENSE text independently read; plugin manifests also declare Apache-2.0. Per-package dependency and Google Cloud service terms still require review.
- **Source roles:** `core/` contains executable ADK examples; `contrib/` contains runnable/deployable agent examples; `plugins/` contains installable domain plugins with `SKILL.md` and evaluation artifacts; `.agents/skills/` contains source-maintainer procedures. These are distinct exposure classes. Upstream scripts, tests, deployment scaffolding and CI are **source-owned reference evidence**, never `skillz` runtime.
- **Denominator:** **UNRESOLVED.** README and code search exposed the following three manifests, but no complete exact Git tree enumeration, aliases/symlink review, or plugin package dependency closure was performed. Do not infer three eligible user-facing skills from three search hits.

### Three exact manifest spot checks

| Source path | Observed Git blob SHA-1 | Role and value | Risk / preliminary decision |
|---|---|---|---|
| [`plugins/retail/skills/product-search/SKILL.md`](https://github.com/google/adk-recipes/blob/45a6999ec8e391a75266ae9507e0e7ca2285ce8e/plugins/retail/skills/product-search/SKILL.md) | `6bd001eba757502d43ee252386018a70305c6255` | Retail semantic product search with catalog ingestion, BigQuery, vector search, ADK and deployment | **SELECTIVE VET / ADAPT**: billable Google Cloud resource provisioning, catalog data export, persistent vector storage, deployment and credential scopes require operation-specific authorization; source-owned setup script is not automatically runnable. |
| [`plugins/retail/skills/virtual-tryon/SKILL.md`](https://github.com/google/adk-recipes/blob/45a6999ec8e391a75266ae9507e0e7ca2285ce8e/plugins/retail/skills/virtual-tryon/SKILL.md) | `0155f498353e7b711568d7aed0c0c62f5035fa76` | Retail image/video virtual try-on using Gemini/Veo and cloud storage | **SELECTIVE VET / ADAPT**: personal photos, consent, possible minors, off-device image/video processing, retention, external generation cost, cloud storage and publication require explicit data and operation scope. No image uploaded or generated in this review. |
| [`.agents/skills/repo-oracle/SKILL.md`](https://github.com/google/adk-recipes/blob/45a6999ec8e391a75266ae9507e0e7ca2285ce8e/.agents/skills/repo-oracle/SKILL.md) | `72e4d2dd7f79161e2273c4fa39bbb374365f548a` | Repository-specific read-only policy/CI/governance explainer with file:line evidence discipline | **REFERENCE-ONLY**: tightly coupled to the ADK Recipes repository; useful evidence/citation method, not a general user-facing imported skill. Its mentions of CI and policy scripts describe **upstream** facilities, not a request for `skillz` execution infrastructure. |

## Macro judgment and next source decision

The distinctive value is not another generic “build a RAG agent” prompt; it is **domain-specific scaffolding coupled to concrete Google Cloud data, identity, cost and deployment paths**. That same coupling creates a high-authority admission risk. Source-level Apache-2.0 licensing does not authorize access to customer catalog data, personal photos, credentials, or billable services. Source popularity and Google branding confer no automatic trust.

**Decision:** TRACK this source as discovery evidence, **do not admit or vendor**. Next source-vetting pass should enumerate the exact `plugins/*/skills/**/SKILL.md` denominator and separate repo-maintenance skills and runnable recipe examples; inspect plugin.json, referenced scripts/templates, license/terms and overlaps. If a differentiated candidate remains, open a bounded issue-first evaluation and terminate it with ADMIT, ADAPT, EXTRACT, REFERENCE-ONLY or REJECT. Do not open an issue for the repository-maintenance oracle as though it were a general-purpose skill.

**Accounting:** no source registry or five public catalog surface change; no repository-owned crawler, script, scheduler, CI, runtime or installation path added.
