# Capability expansion discovery: 2026-10-26

**Status:** bounded discovery and preliminary source vetting only. **Not admission, exact-version semantic verification, package-security approval, or behavioral validation.**

## Baseline and authority

Repository `Knapp-Kevin/skillz`, starting `main` `07a04794c3648ea8aab3b04ed6b621dca7e597e6`. Current Tier-1 governance, `README.md`, `AGENTS.md`, `docs/GOVERNANCE_INDEX.md`, `docs/SYSTEM_STATE.md`, and `CURATION_QUEUE.md` govern. The repository is **entirely passive**; source-owned upstream tooling is reference material, not a `skillz` runtime. No package execution, scanning, or behavioral validation occurred.

The catalog at this HEAD reports 44 first-party user-facing skills, 22 source identities, 12 pinned corpora, and 721 persisted exact-version third-party semantic reviews. The first-party catalog emphasizes monitoring/intelligence (17/44) over software/repository practice (3/44), per issue #406. This distribution is a discovery clue, **not proof of a whole-corpus absence**. Issue #414 already owns memory, cost/observability, accessibility/multilingual, and incident-recovery gap adjudication; coordinate rather than duplicate it. Historical #35 is destination evidence, while #27, #41 and PR #42 are closed historical material.

### Capability-gap macro map

| Capability / differentiated mechanism | Existing exposure / duplication risk | Priority |
| --- | --- | --- |
| Accessibility regressions tied to actual user behavior, and accessible chart/data equivalents | #414 provisional; existing browser-testing/evaluation references require whole-skill comparison | High |
| Threat models as **implicit security contracts** with traceable assumption and trust-surface evidence | Existing `mcp-vetting`, `permissions-review`, and third-party security review overlap but differ in purpose | High |
| Reproducible geospatial analysis with source pins, CRS/geometry correctness, rerun evidence | No named first-party GIS skill in the current 44-skill catalog; whole-source overlap still unproven | High |
| Stable keyed cross-references and bounded worst-case context loading | `session-continuity`, `skill-bootstrap`, Matt Pocock and other context-management prior art overlap | High/medium |
| Formal model checking and proof-backed counterexamples | Existing testing/evaluation skills may cover tests, not TLA+/Lean/Kani proof mechanisms | Medium |
| Context degradation and poisoning diagnosis | Memory and context-management governed sources already exist; must avoid repackaging generic advice | Medium |
| Portable structured notes and interactive knowledge views | Documentation/memory skills overlap, but Obsidian Bases/Canvas formats are specific | Medium |
| Scientific research methods | Broad research skills exist; discovery aggregators are not themselves source-authored skill packages | Medium |
| Privacy-specific RAG permission/deletion audits | #414 and proposed #412 data-lifecycle skill overlap; licensing blocks unchanged adoption for one lead | Medium |

## 14 canonical leads, deduplicated against 22 registered source identities

These 14 GitHub repositories were resolved directly and are **not** among the 22 source identities in the current registry. SHA means the observed source HEAD, not an approved admission pin. License is root evidence and may not cover separately licensed subpackages. All entries have `admitted=0`, `semantic_verified=0`, `security=not-run`, `behavioral_validation=not-run` in this discovery pass.

| Rank | Source and observed HEAD | Root terms | Differentiation and provisional disposition | Authority, privacy, portability, overlap |
| --- | --- | --- | --- | --- |
| 1 | [smukh/a11y-agent-skills](https://github.com/smukh/a11y-agent-skills) `8bc24f049734c607e23bd3955700fd4858649614` | MIT confirmed from LICENSE | **SOURCE-VET SELECTIVE**. 12 skill directories; behavior-level accessibility regression and nonvisual charts stand out. Intake #418. | Browser/Playwright/axe and source edits optional; scoped test-target approval and private DOM minimization. Medium/high portability of static guidance. #414 overlap. |
| 2 | [alpha-omega-security/threat-model](https://github.com/alpha-omega-security/threat-model) `192fd60cd0afe8851128ce4c68ed68c174c11948` | MIT confirmed | **SOURCE-VET SELECTIVE**. Eight first-class threat-model specialists/orchestrators, security contract distinct from vulnerability hunting. | Repository inspection and three artifact writes require target authorization; no security guarantees from a static model. Medium portability. Security review overlap. |
| 3 | [jaakla/openmapstack-skills](https://github.com/jaakla/openmapstack-skills) `a3df1cb8126d5222fbb27e3f1dba49aca01b6302` | MIT confirmed | **SOURCE-VET SELECTIVE**. Four skills for geospatial discovery, reproducible GIS projects, spatial SQL and open mapping. | CLI, DuckDB/PostGIS/QGIS, external geodata and source corrections may have cost/privacy/write effects; consent and immutable pins required. Medium portability. |
| 4 | [serradura/okf](https://github.com/serradura/okf) `cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c` | Apache-2.0 confirmed | **EXTRACT / SELECTIVE VET**. `okf-principles` specifies keyed identity, index-first, permissive reading, kind-over-location and no-tooling-required text. | Principles are high-portability read-only design material; wider OKF stack has optional runtime dependencies and memory/privacy boundaries. Overlaps context-management corpus. |
| 5 | [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) `9ff0c99108b36d3b886defd825d8ac1f47dba374` | MIT (GitHub metadata) | **ADAPT / OVERLAP REVIEW**. 18 subskills include context degradation, compression, harness engineering, advanced evaluation, and multi-agent patterns. | Host/tool assumptions vary; some operational claims require independent evidence. High overlap with existing memory/agent sources. |
| 6 | [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) `3ccff5338ea700537839b21900aa5358a0402c98` | MIT (GitHub metadata) | **ADAPT / SELECTIVE VET**. Six skills cover Obsidian Bases, JSON Canvas, Markdown and CLI. | Writes to user vault require authorization; privacy of notes and host-specific CLI. Format instructions portable, CLI operations less so. |
| 7 | [michael-denyer/agent-formal-verify](https://github.com/michael-denyer/agent-formal-verify) `5bbc2eb852e39160f7b6d4e50cf738ac2f954b3e` | GPL-3.0 | **REFERENCE-ONLY / TERMS REVIEW**. Two skills with TLA+/TLC, Lean 4 and Kani mechanisms. | High tool dependencies, code/model changes and CI guidance belong to external host/project, never `skillz`. No copying until license obligations assessed. |
| 8 | [obra/superpowers](https://github.com/obra/superpowers) `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` | MIT (GitHub metadata) | **EXTRACT / DUPLICATION REVIEW**. Fifteen software-methodology skills, notably verification-before-completion, debugging and worktree discipline. | Strong overlap with existing SDLC/agent sources; upstream hooks/scripts remain upstream. Host changes require scoped authority. |
| 9 | [zivtech/accessibility-skills](https://github.com/zivtech/accessibility-skills) `3ffc2cca364456d09e4daca31f54623b02fe9d93` | GPL-3.0 | **REFERENCE-ONLY / COMPARATIVE**. WCAG 2.2 role-based audit planning, screen-reader reviews and ACR drafting. | High overlap with #1, scripts and browser tooling, private-page privacy; GPL compliance needed before redistribution. |
| 10 | [Stachacl/privacy-skills](https://github.com/Stachacl/privacy-skills) `ea8eb4242b778b5044b72d686ed8b46ed7a76c56` | **Unclear**: root LICENSE exists but is **zero bytes**, GitHub NOASSERTION | **REFERENCE-ONLY, NO VENDOR**. 41 topical privacy skills including RAG document permission scoping, logging PII and deletion propagation. | High sensitive-data and access-control impact. Strong #414/#412 overlap; cannot infer redistribution rights. |
| 11 | [aipoch/open-science](https://github.com/aipoch/open-science) `bca63c44af08616044101e0f0c93bcdcb5ddf78f` | Apache-2.0 (GitHub metadata) | **REFERENCE-ONLY AS APPLICATION**. Research workbench, literature and reproducibility components, not an established first-class SKILL.md denominator. | Desktop app, connectors, Python/R execution, file access and scientific-data privacy. Extract concepts only with independent source terms. |
| 12 | [InternScience/Awesome-Scientific-Skills](https://github.com/InternScience/Awesome-Scientific-Skills) `e67760e2081508773a59398f72bf808f3ac3217c` | MIT (aggregator root) | **DISCOVERY SURFACE / REFERENCE-ONLY**. `skills/` entries are submodule pointers to independently licensed repositories, not first-class reviewed skills. | Resolve each actual upstream owner/license/pin; avoid double counting Anthropic, Corey Haines and Agent Skills spec already in `skillz`. |
| 13 | [myclaude-sh/sql-query-optimizer](https://github.com/myclaude-sh/sql-query-optimizer) `ad60347b79fbf04df4a73633330376b5d44e5a0b` | MIT | **REJECT UNCHANGED**. The sole `SKILL.md` is a short marketplace/install description, claiming scripts/references/templates that are absent from the observed repository root. | No trustworthy bundled optimizer procedure or benchmark evidence. SQL optimization is useful, but this is not the source to admit unchanged. |
| 14 | [mutagent-io/skills](https://github.com/mutagent-io/skills) `195c6b6d550845e04fede3f707dabe87820328da` | MIT | **REFERENCE-ONLY / EXTRACT**. One CLI skill for a vendor's login, install, evaluator and diagnostics tools. | Global package installation, login, quotas and feedback sends are consequential external actions. Overlap with existing agent evaluation and observability; not portable unchanged. |

## Exact-version evidence inspected, not verified

- `smukh/a11y-agent-skills/skills/accessibility-regression-test/SKILL.md` at its observed SHA: Git blob `c3152c581e79ca0e3a478c7a992f91cebd6493f3`. `references/test-selection.md` blob `f68673b156dcfa82a22d7957d0bb6c3a6b9033a2`. It distinguishes lint, component, Playwright, keyboard journey and manual evidence, and refuses to claim full accessibility certification from a scoped regression.
- `smukh/a11y-agent-skills/skills/accessible-charts-and-dashboards/SKILL.md`: blob `9cce3b0fe24e50be96e1ace01fe559cf74ff2b52`. It preserves data equivalence through filters and dynamic states and requires human judgment for unresolved meaning.
- `alpha-omega-security/threat-model/skills/threat-model/SKILL.md`: blob `e6462250f8dfabbafff908d825e8405878dbc9e0`. Explicit trigger/non-trigger distinction: implicit security contract versus audit/CVE hunting.
- `jaakla/openmapstack-skills/skills/reproducible-gis-project/SKILL.md`: blob `7efab9ecc2d8926e4e22fb7278b0c9a631c5095f`. Immutable geospatial sources, explicit corrections, chosen stack and clean rerun evidence.
- `serradura/okf/skills/okf-principles/SKILL.md`: blob `210cefa986848a03733fea71a1c024a76e040ee3`. Static, tool-optional context-structure principles.
- The `smukh` README has an obsolete badge claiming **7 skills**, while its prose and inspected `skills/` directory show **12**. Recompute canonical denominator from pinned source tree, not README claims.

The named blob identities above were re-read at their respective exact observed commit revisions. Other candidates have source-level evidence only, not exact package reviews.

## Macro synthesis and next actions

**Strength:** Strongest novel mechanisms are accessibility regression with actual user behavior, geospatial reproducibility and security contract threat modeling. Context compression, skill authoring and general coding workflows have substantial existing coverage and require stricter duplication scrutiny.

**Risks:** Browser/CLI installs and external service calls must not be treated as authorization; private DOM/notes/research files require explicit scoped access; geospatial data changes must be reversible and provenance-preserving. GPL and missing-license sources cannot be silently vendored. Scientific aggregator entries are source pointers, not independent skill units.

**Discovery flow:** 14 new source leads, 14 source identity/HEAD inspections, 5 pinned individual manifest reads, 0 admitted, 0 semantically verified, 0 package-security scans, 0 behaviorally validated. One bounded source-vetting issue opened: #418. Existing #414 owns accessibility capability fit. No new corpus count or five-surface accounting change is justified by discovery alone.

**Single next priority:** Finish #418's twelve-package macro reconciliation, with deep exact-version static review of the accessibility regression and chart-equivalence packages, then decide selective admission versus adaptation with applicable external package-security evidence.
