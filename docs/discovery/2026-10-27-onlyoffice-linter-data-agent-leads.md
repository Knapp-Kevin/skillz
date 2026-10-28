# Governed discovery: ONLYOFFICE, agent-skills-lint and data-agent field tests (2026-10-27)

**Outcome:** 3 previously unrecorded canonical source leads inspected, **4 public first-class skill candidates** identified across two repositories, one link-only index classified separately, **0 admitted**, **0 executed**. The source names returned zero default-branch `skillz` code-search matches, a preliminary name-level deduplication only. No issue is opened for unqualified individual packages; issue-first intake remains required before any admission.

## Discovery funnel

- **GitHub recent repositories:** three different query families, `agent skills created:>2026-10-24 pushed:>2026-10-26`, `SKILL.md agent created:>2026-10-24`, and `agent skills security pushed:>2026-10-25`; 30 rows per query, **90 raw result rows**. The search filters are not proof that the exact skill manifest was published in the last 24 hours.
- **Hugging Face skills/news discovery:** current search checked, but no newly evidenced distinct canonical source was promoted.
- **Skills.sh/public skill directory:** current search checked, but no newly evidenced distinct canonical source was promoted.
- **New source leads recorded:** 3; **new independently first-class candidates identified:** 4 (three ONLYOFFICE public skills, one linter skill). Two linter `SKILL.md` files are test fixtures and three ONLYOFFICE `.claude/skills/` files are repository-internal maintainer procedures. These do **not** inflate the four public-candidate count.
- **New admitted source identities:** 0; **exact-version semantic verification companions:** 0; **package-security passes:** 0; **behavioral tests:** 0; **last successful new source discovery:** 2026-10-27.

## 1. ONLYOFFICE Agent Skills: three SDK-focused public packages

- **Canonical source:** https://github.com/ONLYOFFICE/agent-skills
- **Observed exact HEAD:** `919536661a41eb04c589b9c069dd957674d377f6`
- **Root license:** Apache-2.0, blob `59910f053f34f68fc31f3ab98108df8d72c4a7e5`; all three inspected public manifests explicitly declare Apache-2.0. Check supporting asset/tool licensing before redistribution.
- **Full Git tree:** six physical `SKILL.md` paths. The README presents **three public SDK skills**; the other three under `.claude/skills/` are repository-maintainer sync/docs procedures, not public SDK capability inventory.
- **Exact public manifest identities:**
  - `skills/embed-sdk/SKILL.md`, blob `f79cf37d4bc81217f7076cd95d604ad901f1b5f3`: iframe/postMessage embedding, portal SDK v2.2.0, OAuth/token flows, CSP and 401 debugging.
  - `skills/plugin-sdk/SKILL.md`, blob `d58e5f0215823b0eb50654005ed962ba90a72fca`: SDK v3.0.0 portal plugin creation, scopes, UI actions, build and upload debugging.
  - `skills/ui-kit/SKILL.md`, blob `10499b51b6d4659a341d7fd4202b0d12f5f980b6`: React 19 UI-kit v4.0.1, providers, component prop contracts and visual correctness.
- **Differentiated value:** highly concrete SDK-version and UI behavior guidance, including authentication and component-property failure modes absent from generic frontend prompts.
- **Authority/privacy risks:** portal credentials, OAuth tokens, private documents, embedded frame message origins, plugin installation/upload, repository writes and UI rendering. Source-owned scripts are package dependencies, not `skillz` execution infrastructure.
- **Disposition:** **SELECTIVE SOURCE-VET / ADAPT candidates**, not unchanged admission. Next gate: exact public package trees, reference/script inventory, token-handling, origin and upload authorization, overlap with existing frontend/document sources, and external package-security evidence.

## 2. agent-skills-lint: one skill and two deliberately risky fixtures

- **Canonical source:** https://github.com/shriramkv/agent-skills-lint
- **Observed exact HEAD:** `3c741b4fc0e91ba42264c66c8dba15b6e82373be`
- **Root license:** MIT, blob `1d1e5c0beecdb66d0e61f64f435b24cb4d5151eb`.
- **Full Git tree:** three physical `SKILL.md` paths, but only `skills/agent-skills-lint/SKILL.md` is a public tool-routing skill, blob `0d5ddb5cd56683c17f0911c433ed88571023c9fe`. `agent_skills_lint/samples/good/pdf-table-extractor/SKILL.md` and `agent_skills_lint/samples/risky/risky-helper/SKILL.md` are test fixtures, **not** two additional admitted candidates.
- **Distinctive value:** combines frontmatter, reference integrity, trigger quality and risk checks with line-specific findings and severity grading.
- **Limits and risks:** Python 3.9+ and locally installed linter/checkout, command execution and possible private repository inspection. Its README advertises CI gates; those belong solely to the upstream tool and are **not** a `skillz` architecture recommendation. A static linter score does not replace the pinned SkillSpector exact-package gate or independent semantic/adversarial assessment.
- **Disposition:** **EXTRACT / REFERENCE-ONLY**, pending tool-quality comparison and source-specific false-positive/false-negative evidence. Do not install or invoke in this curation cycle.

## 3. Data-agent skills field-test directory: discovery surface, not a corpus

- **Canonical source:** https://github.com/tartini-ai/awesome-data-agent-skills
- **Observed exact HEAD:** `7f118ae5b7ac3ee0e6af6c0bae4b92a6dc043c87`
- **Full Git tree:** **zero** `SKILL.md` files. The README links to other authors' skills, with install commands and field-test narratives; no root LICENSE found in this bounded inspection.
- **Distinctive value:** small, potentially useful comparison of skills against actual data-quality/schema work, including recorded findings. Those field tests are the source's claims and have not been reproduced independently.
- **Disposition:** **DISCOVERY SURFACE / REFERENCE-ONLY**. Follow original author repositories, canonical skill path and terms for any future candidate. Do not count index entries as source-owned first-class skills or infer validation from field-test claims.

## Macro synthesis and lifecycle

The three sources illustrate **three distinct units of accounting**: SDK skill packages, a tool with adversarial sample fixtures, and a link-only index. Counting every `SKILL.md` or every README link as a new trusted capability would produce inflated and misleading discovery throughput.

The highest-value selective vetting target is the **ONLYOFFICE three-skill SDK family** because of version-specific embedding, plugin and UI-kit procedures. Its auth/document-data and plugin-upload boundaries require a deep review. The linter is useful methodological prior art but cannot silently replace the existing pinned security gate. The data directory is discovery context, not a package source.

This documentation-only lane does not create a new registry source identity, skill admission, verified/validated claim, scanner receipt, CI workflow, script, runner, scheduler, or public accounting change. No separate issue is warranted until a bounded candidate intake with complete exact package/terms and overlap evidence can be resolved. Continue active Microsoft admitted-source reconciliation in parallel.
