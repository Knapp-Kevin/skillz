# OpenAI Build iOS Apps: nine exact-pin candidate decisions

**Date:** 2026-11-01. **Source:** [openai/plugins](https://github.com/openai/plugins/tree/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/build-ios-apps) at `0722921d5542fc593105c27bd52630babd8b8c2a`, registered as **dynamic discovery**, not admitted. **Issue:** [#580](https://github.com/Knapp-Kevin/skillz/issues/580). **Plugin version:** `0.1.2`; plugin tree `f9a0d9e756f52a8a6764e823dc7760b64b6ec2f1`; manifest blob `cea374fe5d45bf09a93826d21cce102208152fa7`; skills tree `6c3f05cd4d55a65278bb2f15effb193c743be23e`.

## Macro-first denominator, provenance and terms

The pinned Git tree contains **nine distinct direct front-mattered `plugins/build-ios-apps/skills/*/SKILL.md` packages** and the pinned plugin README names those same nine. No nested first-class SKILL.md, symlink alias, mirrored exposure or independently front-mattered reference was found in this plugin subtree. The nine package trees and nine manifest blobs below are unique; 76 plugin-tree blobs include supporting materials, not 76 skills. The plugin bundles its own Node/Python/shell helpers, Swift templates, 43 reference Markdown files, MCP configuration and metadata. They remain **upstream source-owned evidence**; nothing here becomes `skillz` runtime or is executed.

The manifest identifies **OpenAI** as plugin publisher and labels the plugin **MIT**, but the pinned root and plugin trees do not contain controlling LICENSE text; no child grant was established. **Redistribution: NOASSERTION**. Source access and official branding do not authorize copying, installation, publication or unchanged use. All exact identities below are from Git tree/blob objects at the registered pin, not from the latest upstream branch. Eight SKILL.md paths last changed in commit `11b5af688423fb5ba8bdae1c04ea666596c1ff59` on **2026-05-27 14:26 UTC**; `ios-simulator-browser` last changed in `a47b2656a41d9279ae68745cd4f0b192dce0f6ea` on **2026-06-03 16:49 UTC**. These are path freshness facts, not runtime compatibility proof.

## Individual exact-version identity and decisions

The two hashes in each row are the **complete skill package tree / SKILL.md Git blob**. Scores are **static candidate assessments out of 20**, not admitted semantic-verification records or external test results. Both REFERENCE-ONLY and REJECT unchanged exclude unchanged adoption.

| First-class skill | Package tree / SKILL.md blob | Last SKILL change | Terminal decision | Authority / portability |
|---|---|---|---|---|
| `ios-app-intents` | `db74d90bc1f0045f9d40e67797c831f47cb5a528` / `098e520f93a4618f00b07975b8692e070f362d44` | May 27 2026 | **REFERENCE-ONLY 16/20** | mutating / potential external disclosure; medium |
| `ios-debugger-agent` | `add88139fbe34878f821f80bed52d3ac8c35d062` / `092e79abdff23ba94f95f37c584395aac6a51491` | May 27 2026 | **REJECT unchanged 14/20** | external-side-effect; low |
| `ios-ettrace-performance` | `22e0f71cf0b14d06b670422fb2de75c5e7b74024` / `a2538d4d81584596ba265de639b39e99fbebe403` | May 27 2026 | **REJECT unchanged 12/20** | mutating / external-side-effect; low |
| `ios-memgraph-leaks` | `72ee0ce5b5787a594632c464f45a85eeee0ded68` / `bddac5965753192bf4000f6a62a3faf54d1bab08` | May 27 2026 | **REJECT unchanged 13/20** | external-side-effect / sensitive data; low |
| `ios-simulator-browser` | `887409ee5db17fe78a4964e3d349b997737da733` / `d5f0dd1e88f77f52eac99515673987bbf76e9caa` | June 3 2026 | **REJECT unchanged 11/20** | external-side-effect / private screen disclosure; low |
| `swiftui-liquid-glass` | `f56543b8aa78f16b021f90ca4b2f180dc62aa3c7` / `9a0fb205669c695db6430a32304eb49dfcce4a1c` | May 27 2026 | **REFERENCE-ONLY 17/20** | mutating when implementing; medium |
| `swiftui-performance-audit` | `3a1507d5a38c6b8818ff5a6efa0eae4a0410e053` / `db22c9dfb7afa5038243669756e1cb235450ca91` | May 27 2026 | **REFERENCE-ONLY 17/20** | read-only intake; mutating remediation; high as checklist |
| `swiftui-ui-patterns` | `a0844abb6c63dd78f8093aa1f96e102fd3e743ec` / `bb1c733651c178514d3a60e88793a539094cbfbf` | May 27 2026 | **REFERENCE-ONLY 16/20** | mutating; medium |
| `swiftui-view-refactor` | `724dc11249a00d2bc8f40dee31d4840b6df8995c` / `5617e31f0fc4980dadfb5276cb102a337d845e36` | May 27 2026 | **REJECT unchanged 14/20** | mutating; medium |

## Individual boundaries and reusable evidence

### `ios-app-intents`

- **Purpose/trigger and exclusion:** Design a scoped Siri/Shortcuts/Spotlight/widget action surface; not automatic publication or exposure of private entities.
- **Bundled/shared dependencies:** 4 references (intent checklist, code templates, examples, system surfaces), Apple App Intents APIs; Xcode.
- **Controlled tags:** `implementation, ux | design, implementation | modularity, compatibility-aware | mutating` (use case | lifecycle | characteristics | authority); portability medium.
- **Decision and rationale:** **REFERENCE-ONLY 16/20.** Useful narrow entity/intent routing and OS-surface checklist, but steps prescribe implementation, shortcuts exposure and build without independent source-edit and sensitive-entity disclosure approval.
- **Exact-version behavioral validation:** `not-run`; package security: `not-run`; no scan or execution claim.

### `ios-debugger-agent`

- **Purpose/trigger and exclusion:** Explicitly scoped simulator app build/debug session; not unattended launches, log streaming or private-screen capture.
- **Bundled/shared dependencies:** XcodeBuildMCP, plugin `.mcp.json` with `npx -y xcodebuildmcp@latest`, simulator and log/screenshot APIs.
- **Controlled tags:** `debugging, testing | verification | tool-routing, visual-verification | external-side-effect` (use case | lifecycle | characteristics | authority); portability low.
- **Decision and rationale:** **REJECT unchanged 14/20.** Boot restraint and UI proof are good, but auto-selected project/session defaults, build/launch and optional relaunch/log capture lack action-specific app/data scope and dependency pinning.
- **Exact-version behavioral validation:** `not-run`; package security: `not-run`; no scan or execution claim.

### `ios-ettrace-performance`

- **Purpose/trigger and exclusion:** Authorized targeted simulator profile; not automatic dependency installation, app instrumentation or deletion.
- **Bundled/shared dependencies:** 2 source-owned scripts, ETTrace CLI/xcframework, EmergeTools Git source, Homebrew, Xcode/dSYMs, simulator.
- **Controlled tags:** `observability, debugging | verification | instrumentation, evidence-first | external-side-effect` (use case | lifecycle | characteristics | authority); portability low.
- **Decision and rationale:** **REJECT unchanged 12/20.** Excellent UUID-matched dSYM and processed-flamegraph proof, but `brew install`, `git clone`, app-target wiring, `rm -rf` and trace capture are not separately authorized; profiling artifacts may be sensitive.
- **Exact-version behavioral validation:** `not-run`; package security: `not-run`; no scan or execution claim.

### `ios-memgraph-leaks`

- **Purpose/trigger and exclusion:** Scoped memory-leak reproduction and artifact handling; not unapproved memory snapshot or automatic patch.
- **Bundled/shared dependencies:** 2 source-owned scripts, `xcrun simctl`, `leaks`, live simulator process, memgraph output.
- **Controlled tags:** `debugging, memory | verification | evidence-first, traceable | external-side-effect` (use case | lifecycle | characteristics | authority); portability low.
- **Decision and rationale:** **REJECT unchanged 13/20.** Strong ownership-path before/after discipline, but memgraphs can include credentials, account content and other in-process data; capture, persistence, reporting and root-cause source edits lack separate authorization and retention limits.
- **Exact-version behavioral validation:** `not-run`; package security: `not-run`; no scan or execution claim.

### `ios-simulator-browser`

- **Purpose/trigger and exclusion:** Explicit preview session on named simulator with approved data exposure; not automatic mirror/server or hot-reload service.
- **Bundled/shared dependencies:** `serve-sim@latest` via `npx --yes`, source-owned Node preview launcher/lib/templates, Xcode/simulator, long-lived local browser mirror.
- **Controlled tags:** `browser-testing, prototyping | verification | visual-verification, tool-assisted | external-side-effect` (use case | lifecycle | characteristics | authority); portability low.
- **Decision and rationale:** **REJECT unchanged 11/20.** Scoped UDID and screenshot proof are useful; dynamic latest-package install, stale-helper kill, generated host install, watch service and private simulator-frame streaming have no independent dependency, process or disclosure boundary.
- **Exact-version behavioral validation:** `not-run`; package security: `not-run`; no scan or execution claim.

### `swiftui-liquid-glass`

- **Purpose/trigger and exclusion:** Review iOS 26+ glass effects and fallbacks; not automatic project styling changes.
- **Bundled/shared dependencies:** 1 Liquid Glass reference; SwiftUI iOS 26+ and Apple platform guidance.
- **Controlled tags:** `ux, implementation | design | compatibility-aware, visual-verification | mutating` (use case | lifecycle | characteristics | authority); portability medium.
- **Decision and rationale:** **REFERENCE-ONLY 17/20.** Differentiated availability/fallback, modifier-order, container and interactivity checklist; implementation/refactor paths still need source-edit approval and live SDK compatibility checking.
- **Exact-version behavioral validation:** `not-run`; package security: `not-run`; no scan or execution claim.

### `swiftui-performance-audit`

- **Purpose/trigger and exclusion:** Code-first audit or authorized trace review; not automatic app edits or uploading unredacted captures.
- **Bundled/shared dependencies:** 7 reference guides (smells, profiling intake, report, WWDC/Apple summaries), optional Instruments evidence.
- **Controlled tags:** `observability, evaluation | verification | metric-driven, evidence-first | mutating` (use case | lifecycle | characteristics | authority); portability high as checklist.
- **Decision and rationale:** **REFERENCE-ONLY 17/20.** Useful suspicion-versus-trace discipline and before/after metrics; `Apply targeted fixes` has no separate edit approval, and requested traces/screenshots require privacy minimization.
- **Exact-version behavioral validation:** `not-run`; package security: `not-run`; no scan or execution claim.

### `swiftui-ui-patterns`

- **Purpose/trigger and exclusion:** Design/compare SwiftUI composition and state ownership; not unapproved scaffolding or compilation.
- **Bundled/shared dependencies:** 30 SwiftUI component/navigation/state references, Xcode build/previews, OS-specific Observation APIs.
- **Controlled tags:** `ux, architecture | design, implementation | modularity, compatibility-aware | mutating` (use case | lifecycle | characteristics | authority); portability medium.
- **Decision and rationale:** **REFERENCE-ONLY 16/20.** Broad practical reference index and iOS 16/17 compatibility routing, but mandates project scaffolding, component creation, builds and previews without separate mutation/side-effect scope.
- **Exact-version behavioral validation:** `not-run`; package security: `not-run`; no scan or execution claim.

### `swiftui-view-refactor`

- **Purpose/trigger and exclusion:** Scoped view-structure proposal; not automatic multi-file refactoring or model rewrites.
- **Bundled/shared dependencies:** 1 MV-pattern reference, SwiftUI/Observation iOS 16/17+ and project source.
- **Controlled tags:** `refactoring, implementation | implementation | behavior-preserving, maintainability | mutating` (use case | lifecycle | characteristics | authority); portability medium.
- **Decision and rationale:** **REJECT unchanged 14/20.** Small-view/Observation guidance is useful, but the workflow directly orders source reordering, extracting subviews and replacing view-model ownership with no scoped diff approval or executed behavior-regression proof.
- **Exact-version behavioral validation:** `not-run`; package security: `not-run`; no scan or execution claim.

## Cross-package findings and synthesis

1. **High-authority simulator operations:** `ios-debugger-agent`, ETTrace and memgraph procedures can build, launch, profile or snapshot app processes and write output. A named simulator UDID, bundle ID or successful tool invocation is **target identification**, not independent authorization for install, logging, memory capture, source edits or retention. Simulator UI screenshots, console output and memory graphs can include private account or credential data; require explicit target, data, storage, sharing and deletion boundaries before any external host execution.
2. **Unpinned and potentially persistent execution:** plugin-local `.mcp.json` invokes `npx -y xcodebuildmcp@latest mcp`. `ios-simulator-browser` invokes `npx --yes serve-sim@latest`, runs a long-lived local mirror and bundled preview generator/watch process. Its explicit per-UDID cleanup is better than unscoped kill, but does not establish install, process-control or browser-frame disclosure authority. ETTrace recommends `brew install`, `git clone`, temporary framework wiring and `rm -rf`; `collect_ios_dsyms.sh` also removes a destination path before replacing it. These are **upstream** helpers, not `skillz` code.
3. **Strong differentiated reference methods:** App Intents action/entity minimization; iOS 26+ glass availability and fallback checks; code-first SwiftUI invalidation analysis; before/after trace evidence; UUID-matched dSYM symbolication; ownership-path leak proof; Observation and component state ownership. These may support host-side ADAPT, EXTRACT, CHECKLIST or COMPOSE decisions after user-fit and authorization assessment, without importing the source's implicit action permissions.
4. **Overlap and freshness:** This family conceptually overlaps the separately vetted Build macOS Apps SwiftUI, Liquid Glass and refactoring procedures. Their names, platform scopes, package trees and evidence are distinct; no approval is inherited. May/June source-path freshness does not establish compatibility with future Xcode, Apple OS or dynamically installed `@latest` tools. There is **no omission** within the nine README-listed direct manifests; the large nested references are dependencies, not separate first-class packages.
5. **Source-family priority:** Retain the official plugin as a **discovery/reference** surface. No unchanged admission or source pin promotion is justified by static review. Focus future vetting on differentiated methods and explicit action/data boundaries, not a near-duplicate iOS/macOS prompt wrapper.

## Accounting and lifecycle disposition

**9/9 terminal candidate decisions: 4 REFERENCE-ONLY / 5 REJECT unchanged / 0 ADMIT.** No exact-version governed provenance or semantic verification companions were created because this is **pre-admission** source vetting. All nine have **security `not-run` / behavioral `not-run`**, not `verified` or `validated`. No tool, app, helper, simulator, scanner, installer or code from this upstream family was executed or copied.

Official-plugin finite intake **106/106 (14 families) → 115/115 (15 families)**, cumulative **46 REFERENCE-ONLY / 69 REJECT unchanged**. Admitted-source denominator delta **0**; governed inventory **44 first-party / 995 third-party / 1,039 total provenance/verification pairs**, **23** registered sources, **12** pinned corpora unchanged. README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json are reconciled in the same documentation tranche. Existing first-party repair drafts #489, #492, #496 remain externally qualification-held for **36** changed package trees; draft admissions #412 and #413 retain separate gates. Archie source terms issue #544 remains externally dependent. Next priority: complete the pinned SkillSpector v2.12.0 reports and independent adversarial acceptance for those 36 exact first-party repairs, then reconcile their shared verification registry before merge.
