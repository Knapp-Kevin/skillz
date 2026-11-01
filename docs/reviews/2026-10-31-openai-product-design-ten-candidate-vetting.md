# OpenAI Product Design: ten-skill bounded source vetting (2026-10-31)

## Scope and decisive result

[Bounded issue #560](https://github.com/Knapp-Kevin/skillz/issues/560) reconciles **10/10** distinct front-mattered first-class `SKILL.md` packages under [`plugins/product-design/skills/`](https://github.com/openai/plugins/tree/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/product-design/skills) at exact registered official discovery revision `0722921d5542fc593105c27bd52630babd8b8c2a`. **2 REFERENCE-ONLY / 8 REJECT unchanged**, 0 admitted packages, 0 new semantic verification/provenance companions, 0 source pin changes, 0 package scans, 0 behavioral executions. The 10 are the denominator of this *finite candidate slice*, not a newly admitted-source denominator. Each directory has its own `agents/openai.yaml`; `audit` and `design-qa` include rubric references, and `user-context` contains two source-owned Python helpers and template/onboarding references. No nested independent `SKILL.md`, symlinks, aliases or mirror exposures were found in this slice. Shared plugin references, JavaScript bootstrap scripts, mobile/web starter templates, Playwright tests and worker files are dependencies, not independent first-class skills or repository-owned machinery.

Source plugin manifest `plugins/product-design/.codex-plugin/plugin.json`: Git blob `93370dd2ca2f823ae45721c03ba4ffc06322d84c`, version **0.1.52**, `license: Proprietary`. No controlling open-source license was observed for the plugin subtree; **no copying or redistribution is cleared**. Exact tree: [`openai/plugins@0722921d5542fc593105c27bd52630babd8b8c2a`](https://github.com/openai/plugins/tree/0722921d5542fc593105c27bd52630babd8b8c2a). Upstream source code and templates were **read as evidence only**, not executed, installed, vendored or modified. Host-agent permission and tool availability never substitute for action authorization.

## Macro-first map

- **Identity/dependency:** 10 distinct first-class skills, 26 skill-subtree files in total (3+3+2+2+2+2+2+2+2+6). Shared router `index`, `critical-overrides`, `user-context` preflight, local prototype bootstrap, Vite/mobile runtime, Sites/Browser/ImageGen/Figma integration. The shared code is plugin-owned upstream reference material.
- **Authority clusters:** browser navigation and live interactions; private source/connector reads; screenshot and design-context disclosure; source-asset copying; npm installs and local project mutation; persistent user-context writes; public deployment and billable/persistent hosting.
- **Privacy patterns:** every normal design workflow is instructed to load saved context and run preflight when shell is available. The preflight reads `user-context.md` up to **2,000,000 bytes** and prints parsed URLs, paths and notes as JSON. `ideate` then instructs attaching saved design context to image generation. A private reference's presence is not consent to send it to another service.
- **Evidence strengths:** `audit` requires actual screenshot inspection and limits accessibility claims; `design-qa` demands same-state comparisons and explicit blocked/passed receipts; `image-to-code` distinguishes server health from browser verification. These methods are useful as extracted checklists, not evidence that the source was executed or validated here.
- **Capability overlap:** existing `skillz` first-party design, research, review, and release-evidence procedures already cover much of the planning/checklist layer. The strongest differentiated prior art is visual identity binding and iterative source-versus-rendered QA, not the bundled runtime or automatic deployment workflow.

## Individual exact-version source decisions

Candidate utility is a **qualitative source-vetting 0–5 scale**, not the corpus's 20-point semantic score or a security/behavioral pass: 0 no value, 1 generic, 2 limited, 3 useful, 4 differentiated, 5 especially strong reusable method. All rows have **behavioral validation: not-run; security scan: not-run**. The SHA columns are Git blob and complete per-package tree identities at the pinned source revision.

| Candidate | `SKILL.md` blob | Package tree | Files | Decision | Utility |
|---|---|---|---:|---|---|
| `audit` | `16f32b81979d4db19980a26e6efe86a70906b207` | `a030d85a39b842778716cc31e4d6dbb2ef663ea6` | 3 | **REJECT unchanged** | 4/5 |
| `design-qa` | `9b904098f7ca9a4bed798afbc1b5ccea66fc7506` | `fe123959ba5fc800dd65462a478b73645e24e7ca` | 3 | **REFERENCE-ONLY** | 5/5 |
| `get-context` | `be27d4a61721693ad1de3c15ae7a80e1ba523e3c` | `ff71bf7be6f21ed8003399b8309685611c652eb1` | 2 | **REJECT unchanged** | 3/5 |
| `ideate` | `e16f57cf4dcbdbc610a266d14a4b69270f6938c7` | `0d5d8061ddef6d8a631407f3a4f90c642dc8a105` | 2 | **REJECT unchanged** | 4/5 |
| `image-to-code` | `84dd7069d8e03469a8172a487d663abf1c7b1af1` | `20172b060474c3273d4b0be94015ff1dcc53ad6c` | 2 | **REJECT unchanged** | 4/5 |
| `index` | `32b04b0d9cc476144a391e89e6ad7e88284ecfe2` | `48798e6ed094087f408d0712f29b178e5d1e538d` | 2 | **REFERENCE-ONLY** | 3/5 |
| `research` | `a904833cea9775c2a40d2f76a4fe0316520713e7` | `279e5cba8f696fd472357a9cee19309c015c8fc9` | 2 | **REJECT unchanged** | 3/5 |
| `share` | `66d0eb37877c02500e22c658c6e4b8577d401668` | `318c970d06ef51944ce58902a4301a0f3cb8faa6` | 2 | **REJECT unchanged** | 3/5 |
| `url-to-code` | `b0fade2f245aec5582b29eeb6ed5dc9cadc2592c` | `6a819342eb09279d5e0818f4c5f283bdfe1101c4` | 2 | **REJECT unchanged** | 4/5 |
| `user-context` | `0faf6430432696d80de1d54c490de954d3fff6eb` | `72794eabb714b0ccfa61abb641523e9c0e223760` | 6 | **REJECT unchanged** | 3/5 |

### `audit` — REJECT unchanged (4/5 candidate utility)

**Purpose/fit:** Screenshot-backed UX/accessibility step evidence and explicit screenshot limits are differentiated. **Authority, privacy, dependency and portability:** Mandatory private saved-context preflight, browser interaction/capture and workspace screenshots lack bounded authorization for authenticated/private flows; Figma upload requires separately scoped disclosure. Browser, Figma, shared overrides; no behavior run. Trigger/non-trigger follows the upstream frontmatter and focused router; reference-only or rejected material is **not** cleared for unchanged use. Exact package: `plugins/product-design/skills/audit/` at `0722921d5542fc593105c27bd52630babd8b8c2a`.

### `design-qa` — REFERENCE-ONLY (5/5 candidate utility)

**Purpose/fit:** Source-versus-rendered same-state visual comparison, P0/P1/P2 fix loop and blocked evidence receipts are valuable QA prior art. **Authority, privacy, dependency and portability:** Unchanged workflow prescribes npm runtime checks, browser captures and project-root report writes; those require host-authorized project/workspace scope. Mobile runtime and rubric are plugin-specific; no behavior run. Trigger/non-trigger follows the upstream frontmatter and focused router; reference-only or rejected material is **not** cleared for unchanged use. Exact package: `plugins/product-design/skills/design-qa/` at `0722921d5542fc593105c27bd52630babd8b8c2a`.

### `get-context` — REJECT unchanged (3/5 candidate utility)

**Purpose/fit:** Minimal target/outcome brief gate avoids premature implementation. **Authority, privacy, dependency and portability:** Mandatory saved-context load and Python preflight before ordinary design requests is not scoped to authorized private context. Host may extract brief-playback checklist only; no behavior run. Trigger/non-trigger follows the upstream frontmatter and focused router; reference-only or rejected material is **not** cleared for unchanged use. Exact package: `plugins/product-design/skills/get-context/` at `0722921d5542fc593105c27bd52630babd8b8c2a`.

### `ideate` — REJECT unchanged (4/5 candidate utility)

**Purpose/fit:** Three independent visual directions, explicit selected-image identity and viewport consistency reduce wrong-option builds. **Authority, privacy, dependency and portability:** Instructs automatic attachment of saved screenshots, product/codebase references and potentially sensitive design context to external image generation without a separate source/disclosure gate. ImageGen/host specific; no behavior run. Trigger/non-trigger follows the upstream frontmatter and focused router; reference-only or rejected material is **not** cleared for unchanged use. Exact package: `plugins/product-design/skills/ideate/` at `0722921d5542fc593105c27bd52630babd8b8c2a`.

### `image-to-code` — REJECT unchanged (4/5 candidate utility)

**Purpose/fit:** Selected-image binding and rendered-browser/console/interaction QA are strong design fidelity methods. **Authority, privacy, dependency and portability:** Automatic template bootstrapping, npm installation, file mutation, image generation and preview actions are not independently bounded to authorized destination, dependencies or spend; plugin-owned mobile/runtime and Sites dependencies; no behavior run. Trigger/non-trigger follows the upstream frontmatter and focused router; reference-only or rejected material is **not** cleared for unchanged use. Exact package: `plugins/product-design/skills/image-to-code/` at `0722921d5542fc593105c27bd52630babd8b8c2a`.

### `index` — REFERENCE-ONLY (3/5 candidate utility)

**Purpose/fit:** Useful design-intent routing and explicit audit-versus-design-QA distinction; no direct source write in router. **Authority, privacy, dependency and portability:** Tightly bound to ChatGPT Work/Sites/Browser capabilities, refers to downstream skills that may perform unauthorized private reads or writes. Routing is not authorization; no behavior run. Trigger/non-trigger follows the upstream frontmatter and focused router; reference-only or rejected material is **not** cleared for unchanged use. Exact package: `plugins/product-design/skills/index/` at `0722921d5542fc593105c27bd52630babd8b8c2a`.

### `research` — REJECT unchanged (3/5 candidate utility)

**Purpose/fit:** Severity/frequency/confidence source map and opportunity clustering are useful research structure. **Authority, privacy, dependency and portability:** Internal Slack/Gong/Drive/CRM/GitHub reads are suggested when connectors are available and request 'allows it', without explicit workspace/record/field scope, privacy minimization or retention/egress approval; no behavior run. Trigger/non-trigger follows the upstream frontmatter and focused router; reference-only or rejected material is **not** cleared for unchanged use. Exact package: `plugins/product-design/skills/research/` at `0722921d5542fc593105c27bd52630babd8b8c2a`.

### `share` — REJECT unchanged (3/5 candidate utility)

**Purpose/fit:** Keeps the existing prototype intact and requires selected hosting target. **Authority, privacy, dependency and portability:** Selecting Sites/Vercel is not sufficient authorization for exact deployment project, public/private visibility, content disclosure, domains, traffic, billing and persistent resources. Runs builds and deployment; no behavior run. Trigger/non-trigger follows the upstream frontmatter and focused router; reference-only or rejected material is **not** cleared for unchanged use. Exact package: `plugins/product-design/skills/share/` at `0722921d5542fc593105c27bd52630babd8b8c2a`.

### `url-to-code` — REJECT unchanged (4/5 candidate utility)

**Purpose/fit:** Source-first desktop/mobile capture, interaction inventory and browser-rendered QA are valuable cloning discipline. **Authority, privacy, dependency and portability:** Says any asset loaded by page is available to copy; terms warning does not grant copying rights. Interactive testing can mutate live authenticated site state; automatic source extraction, install and local writes need authorization. No behavior run. Trigger/non-trigger follows the upstream frontmatter and focused router; reference-only or rejected material is **not** cleared for unchanged use. Exact package: `plugins/product-design/skills/url-to-code/` at `0722921d5542fc593105c27bd52630babd8b8c2a`.

### `user-context` — REJECT unchanged (3/5 candidate utility)

**Purpose/fit:** Curated saved references and explicit no-secrets note are useful context hygiene. **Authority, privacy, dependency and portability:** Automatic preflight reads and prints up to 2 MB of durable context as JSON, including URLs, file paths and notes, with no per-task read/egress boundary. Init script creates persistent directories and can overwrite context with --overwrite; no separate retention/deletion scope. No behavior run. Trigger/non-trigger follows the upstream frontmatter and focused router; reference-only or rejected material is **not** cleared for unchanged use. Exact package: `plugins/product-design/skills/user-context/` at `0722921d5542fc593105c27bd52630babd8b8c2a`.

## Macro findings and omissions

1. **Systemic authorization failure:** automatic persistent-context preflight is imposed on otherwise unrelated design tasks. A user's request for an audit, ideation or prototype is not blanket authorization to read historical private project context, inspect connectors, upload screenshots, or persist new context. Secure alternative: per-task minimum source selection, explicit read/disclosure scope, redaction, and proposal-only when absent.
2. **Copyright/terms and live-state exposure:** `url-to-code` equates browser asset availability with copying rights, despite its generic terms warning; interactive source testing can cause real authenticated changes. Require a rights/authorization boundary and non-mutating inspection by default.
3. **Deployment is a consequential operation:** `share` chooses a hosting provider but does not separately bind project/account, exact content, visibility, domain/traffic, cost, and durable-resource authorization. Do not infer deployment approval from tool availability or a target label alone.
4. **Strong reusable method:** same-state screenshot comparison, evidence-first UX audit, selected-image identity, browser-rendered interaction checks and blocked QA receipts. Preserve as conceptual adaptation/checklist material; avoid importing the source-owned Vite/Playwright/Sites toolchain into `skillz`.
5. **No freshness/quality laundering:** the registered observed commit and plugin version are exact historical source evidence, not proof of current upstream behavior, legal clearance, scan pass, test pass or representative user fit. Future promotion requires a separate governed intake and package-specific review at a newly chosen exact identity.

## Lifecycle and accounting

Issue #560 is the bounded evidence workspace. At this decision point the candidate slice is **10/10 terminal**, no external dependency is needed to close the *vetting* issue. Source license is Proprietary, so no vendoring was attempted. No additional issue is needed merely to repeat the standing license boundary. Existing first-party repair PRs #489/#492/#496 (36 changed package trees) and admissions #412/#413 remain qualification-held; none is made ready by this review. The three repair drafts have no qualifying exact-package external SkillSpector v2.12.0 full reports/digests or independently executed adversarial acceptance; the admission drafts have their own security/acceptance gates.

Public surfaces remain **44 first-party / 995 third-party / 1,039 verification-provenance pairs**, of which 874 third-party records are registered/tracked and 121 are candidate-only. Registered sources **23**, pinned corpora **12**, admitted denominator delta **0**. No changes to `skills/`, `engine/skills/`, `registry/skills/`, `registry/verification/`, `registry/sources.yaml`, source pins, or runtime/executable machinery.
