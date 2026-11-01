# OpenAI Game Studio: nine-candidate exact-source vetting (2026-11-01)

## Scope and terminal decision

**9/9 finite candidates resolved: 7 REFERENCE-ONLY / 2 REJECT unchanged; zero admissions.** These are candidate-vetting dispositions, not governed semantic `verified` states. No package was installed, executed, copied or tested.

- Discovery source: [OpenAI Plugins](https://github.com/openai/plugins), registered as `openai-plugins` / `dynamic-discovery` at exact revision `0722921d5542fc593105c27bd52630babd8b8c2a` (commit 2026-10-08T05:21:32Z).
- Plugin: `plugins/game-studio`, tree `b20ed7187bf5633b8b18ee9c7780e69eb68686e4`; manifest `.codex-plugin/plugin.json` blob `5e44d10c60c6415130c5f8442e60577be257979c`, version `0.1.2`, author `OpenAI`.
- Exact denominator: **nine** distinct, direct, front-mattered `skills/<name>/SKILL.md` packages, each with one `agents/openai.yaml`. No nested first-class SKILL.md, alias, symlink or mirror in this plugin tree. **16 shared reference Markdown files, 3 Python helper scripts and 2 assets** are dependencies, not extra eligible skills.
- License: plugin manifest labels itself `MIT`, but no controlling LICENSE/COPYING/NOTICE text exists at the pinned repository root or plugin subtree. **Redistribution: NOASSERTION**. Do not vendor or infer blanket copying permission from the manifest label.
- Skill-specific freshness: all nine SKILL.md paths last changed in pinned path history at `d965fdc57d1f872f52bcdb10c9e1cbf922a8a761`, **2026-03-16T17:03:20Z**. The October source pin does not imply October updates to these skills.
- Scores below are **candidate usefulness/risk estimates**, not governed 20-point semantic verification. All nine remain security `not-run` and behavioral `not-run`.

## Macro-first map

**Coherent strengths:** 2D Phaser-first routing with separate vanilla Three.js and React Three Fiber paths; simulation/render state separation; DOM HUD and camera/pointer-lock boundaries; GLB/glTF asset shipping; screenshot-backed canvas/WebGL QA; sprite-strip shared-anchor normalization. These add game-specific methods beyond generic React/visual-QA references, though they overlap them.

**Dependency/identity structure:** one umbrella route to eight specialists, shared architecture/playtest/asset references, three source-owned Pillow scripts used only by `sprite-pipeline`. Those upstream scripts are *not* repository-owned execution machinery. All nine have distinct exact package trees and manifests; the 16 shared references do not add to the first-class denominator.

**Authority/privacy risk:** ordinary planning is advisory; implementation may mutate a local project; browser automation may hit production or authenticated targets and capture private screenshots; external image generation may disclose protected seed art and incur cost; lossy asset optimization and output overwrites can destroy work. A chosen stack, input file, available tool or user asking for QA does not authorize unrelated disclosure, billing, persistent overwrites or publication.

**Observed implementation defects:** the bundled sprite canvas helper writes a chosen output path, the strip normalizer writes `01.png` and later numbered files into a chosen directory, and the preview helper writes a chosen sheet, all without overwrite refusal. `game-playtest` does not require local/staging target scope, test identity or screenshot handling authorization before booting and capturing. No helper was executed here.

**Licensing, freshness and priority:** absence of controlling license text prevents source admission. The March skill edits and unpinned Phaser/Three/Rapier/Pillow/imagegen dependencies limit freshness and portability confidence. The source remains useful reference/design material but does not displace the higher-priority blocked first-party qualification frontier.

## Exact-package identities and decisions

| Candidate | Package tree SHA | SKILL.md blob SHA | Candidate score | Terminal decision |
|---|---|---|---:|---|
| `game-studio` | `208acc7c2d90dbe137827b0759a477185755070f` | `ba409990d8ff8fa0e04350c18a2c1581c39bd30c` | 17/20 | REFERENCE-ONLY |
| `web-game-foundations` | `f4b156637c3ae3b63d976d2b4bf208b84a7c93a4` | `1fe88e9c7c63c4f0ef9fda4ebd24fa61ae9a44a1` | 17/20 | REFERENCE-ONLY |
| `game-playtest` | `c64a812d177aeaa173a59f8a5368b227ba5af611` | `d74823c9231966b8bc49924932f4b1c7d3a19e0a` | 13/20 | REJECT unchanged |
| `game-ui-frontend` | `f78601e12510452b1801861f18fe6b88552650b1` | `f2681fb955143f96cb04bfa4f1cb09d6839b162a` | 17/20 | REFERENCE-ONLY |
| `phaser-2d-game` | `2baac87633b5ec6d4fc73347c90964ad9e0aa74a` | `8bd4ed6afcb502a0c78cd8b32cbb3163b7187fff` | 16/20 | REFERENCE-ONLY |
| `react-three-fiber-game` | `8f7237a63f0a8f445091a10e718c91ce7a15e12d` | `90fb0657bce2c96ab8aa3ae52534aaf51bbe67b8` | 16/20 | REFERENCE-ONLY |
| `sprite-pipeline` | `0c8eb6ef5d75288bc878eef509e56f5bfa91b314` | `a31ef15cf890426873a805ced1ed9b11f16a1efa` | 10/20 | REJECT unchanged |
| `three-webgl-game` | `c93cb8299830f6388442ee24b3e183e3f3d0a4f2` | `647cbcaddd28d3c3092d28e1b9de6ce56aa39999` | 16/20 | REFERENCE-ONLY |
| `web-3d-asset-pipeline` | `82c3bdc7f235848fa6569dc012e2216275837756` | `d0fde630c0cbae52b52aa22f43c8df9eb7989212` | 15/20 | REFERENCE-ONLY |

### Individual rationale and boundaries

1. **`game-studio` (17/20), REFERENCE-ONLY.** Trigger: Unspecified game or cross-domain stack selection. Non-trigger: Selected engine or QA-only request. Dependencies: Eight specialist skills, eight shared references. Authority `generate-only`, portability `medium`; controlled tag examples: planning / orchestration / modularity. **Rationale:** Differentiated 2D-first routing and 3D React/imperative fork; routing to sprite generation does not grant execution or data-disclosure authority. **Security: not-run; external behavioral/adversarial validation: not-run.**

2. **`web-game-foundations` (17/20), REFERENCE-ONLY.** Trigger: Simulation/render/input/save architecture. Non-trigger: Already settled engine-specific implementation. Dependencies: Six shared architecture/engine/asset references. Authority `generate-only`, portability `high`; controlled tag examples: architecture / modularity / risk-aware. **Rationale:** Simulation outside renderer, stable asset keys and DOM HUD are sound design prior art; engine defaults are not universal evidence. **Security: not-run; external behavioral/adversarial validation: not-run.**

3. **`game-playtest` (13/20), REJECT unchanged.** Trigger: Authorized browser-game boot and visual QA. Non-trigger: Unapproved production or authenticated targets. Dependencies: Playwright or equivalent, SpectorJS, browser profiler, playtest checklist. Authority `external-side-effect`, portability `medium`; controlled tag examples: testing / visual-verification / evidence-first. **Rationale:** Boot/automation/screenshots are prescribed without bounding environment, test identity, production side effects, sensitive capture, retention or disclosure. Preserve screenshot/reproduction checklist only. **Security: not-run; external behavioral/adversarial validation: not-run.**

4. **`game-ui-frontend` (17/20), REFERENCE-ONLY.** Trigger: HUD/menu/overlay design and pointer-lock transitions. Non-trigger: Backend-only or simulation-only work. Dependencies: DOM/CSS and shared frontend, HUD and playtest references. Authority `generate-only`, portability `high`; controlled tag examples: ux / visual-verification / risk-aware. **Rationale:** Strong playfield budget, reduced-motion and camera/input boundary guidance; 20–25% HUD heuristic is not executed UX acceptance. **Security: not-run; external behavioral/adversarial validation: not-run.**

5. **`phaser-2d-game` (16/20), REFERENCE-ONLY.** Trigger: Authorized Phaser 2D TypeScript/Vite implementation. Non-trigger: 3D or explicitly different engine. Dependencies: Phaser, TypeScript, Vite, DOM HUD and shared architecture/sprite refs. Authority `mutating`, portability `medium`; controlled tag examples: implementation / modularity / deterministic. **Rationale:** Thin scene and deterministic system guidance is useful; project writes, installations and testing remain host-scoped, no version pins or executed evidence. **Security: not-run; external behavioral/adversarial validation: not-run.**

6. **`react-three-fiber-game` (16/20), REFERENCE-ONLY.** Trigger: React-hosted 3D with shared UI state. Non-trigger: Plain Three.js or asset-only conversion. Dependencies: React, three, fiber, drei, rapier, postprocessing, optional a11y, starter refs. Authority `mutating`, portability `medium`; controlled tag examples: implementation / modularity / compatibility-aware. **Rationale:** High-frequency simulation versus React state separation and low-chrome UI are useful; dependencies unpinned and no app acceptance. **Security: not-run; external behavioral/adversarial validation: not-run.**

7. **`sprite-pipeline` (10/20), REJECT unchanged.** Trigger: Approved seed frame to generated strip and normalized frames. Non-trigger: 3D assets, unlicensed art, offline-only tasks. Dependencies: Three bundled Python/Pillow helpers, external imagegen service and sprite reference. Authority `external-side-effect`, portability `low`; controlled tag examples: implementation / visual-verification / tool-assisted. **Rationale:** Imagegen seed-frame transfer lacks separate rights/sensitivity/cost authority; helpers save to caller paths and overwrite numbered PNGs without collision gate. Preserve full-strip shared-anchor method. **Security: not-run; external behavioral/adversarial validation: not-run.**

8. **`three-webgl-game` (16/20), REFERENCE-ONLY.** Trigger: Plain TS/Vite imperative Three.js runtime. Non-trigger: React R3F or asset-only work. Dependencies: Three, GLTF/Draco/KTX2 loaders, Rapier, SpectorJS, eight shared refs. Authority `mutating`, portability `medium`; controlled tag examples: implementation / modularity / risk-aware. **Rationale:** Context loss, asset budgets, camera and simulation/render split are useful; no pinned versions or executed GPU/browser evidence. **Security: not-run; external behavioral/adversarial validation: not-run.**

9. **`web-3d-asset-pipeline` (15/20), REFERENCE-ONLY.** Trigger: GLB/glTF export, optimization, LOD and collision preparation. Non-trigger: Scene/camera/runtime engine choice. Dependencies: Blender/DCC, glTF Transform, Draco/Meshopt/KTX2, GLTF loader and shared refs. Authority `mutating`, portability `medium`; controlled tag examples: implementation / risk-aware / evidence-first. **Rationale:** Pivot, compression and texture-budget guidance is useful; lossy edits and shipping require output/backup/rights/release authority. No measured performance proof. **Security: not-run; external behavioral/adversarial validation: not-run.**

## Completion and accounting

Bounded issue [#566](https://github.com/Knapp-Kevin/skillz/issues/566) is resolved by these nine terminal decisions. No source pin, license declaration, upstream file, taxonomy value, first-party package, admitted-source denominator, security state or semantic companion changed. Public counts remain **44 first-party / 995 persisted third-party (874 registered/tracked + 121 candidate-only) / 1,039 matching verification-provenance pairs**, **23 registered sources**, **12 pinned corpora**. **New semantic pairs: 0; admissions: 0; scans: 0; behavioral runs: 0.**

Eight pre-existing issues and five draft PRs (#489/#492/#496/#412/#413) were triaged. No draft had a qualifying review, review thread, status or workflow run; all remain qualification-held. The three first-party repair drafts need complete pinned external SkillSpector v2.12.0 reports/digests and independent executed adversarial acceptance for **36 distinct final changed trees**, plus shared-registry reconciliation. Admission drafts #412/#413 have separate gates; Archie license issue #544 awaits authoritative upstream terms.

**Next highest-priority action:** obtain those 36 exact-tree external security/adversarial receipts, reconcile the shared first-party registry, and merge only qualified repairs. The host agent remains the active system; `skillz` remains passive.
