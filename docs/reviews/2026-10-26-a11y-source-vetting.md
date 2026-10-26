# Accessibility skill source: bounded 12-package vetting (2026-10-26)

**Disposition: selective ADAPT / EXTRACT / REFERENCE-ONLY; no unchanged admission.** Governed candidate [#418](https://github.com/Knapp-Kevin/skillz/issues/418). Source: [smukh/a11y-agent-skills](https://github.com/smukh/a11y-agent-skills), exact inspected commit `8bc24f049734c607e23bd3955700fd4858649614`. This is a **candidate assessment**, not a new registered source, a security clearance, a verified catalog companion, or observed behavioral validation.

## Macro and licensing evidence

- The upstream recursive Git tree at the stated commit is **not truncated** (272 tree entries). Under `skills/`, **12 top-level directories, 12 first-class `SKILL.md` manifests, 12 bundled reference Markdown files, zero symlinks and zero nested skill manifests**. The source README's seven-skill badge is stale; neither the badge nor the number of generic Markdown files is the denominator.
- The root [MIT LICENSE](https://github.com/smukh/a11y-agent-skills/blob/8bc24f049734c607e23bd3955700fd4858649614/LICENSE) is blob `3ed9e473d3ea1a9ae143a805f591a869c2a1d602`. [THIRD_PARTY_NOTICES.md](https://github.com/smukh/a11y-agent-skills/blob/8bc24f049734c607e23bd3955700fd4858649614/THIRD_PARTY_NOTICES.md) is blob `2c5bc2b3fd5aa7c659d2d98b00f5303a5229e0b6` and identifies axe-core MPL-2.0, Playwright Apache-2.0 and other tool dependencies. Do not assume the root MIT grant relicenses bundled third-party runtimes.
- Each package contains one `SKILL.md` and one required `references/*.md` file; the audit also refers to shared `docs/EVIDENCE-MODEL.md` (blob `b4db13a01522094daae6239b8aeae4243405ee70`). All 12 referenced files were located and inspected. The upstream CLI, MCP, browser, bundled axe runtime and GitHub Action are **source-owned optional/external host tooling**, not `skillz` runtime.
- The source [security model](https://github.com/smukh/a11y-agent-skills/blob/8bc24f049734c607e23bd3955700fd4858649614/docs/SECURITY.md) claims local-first/no telemetry, DNS and metadata-address blocking, best-effort evidence redaction and bounded browser journeys. These are **upstream claims**, not an independent code audit. The browser can still execute untrusted page JavaScript and reports can expose DOM/route information. An actual package-security scan was **not run**.
- Existing `skillz` catalog includes UX, testing and evaluation prior art; issue #414 owns broader accessibility coverage. No claim is made that the entire third-party corpus lacks comparable mechanisms. Particularly distinctive facets here: nonvisual chart/filter parity, async combobox race safety, virtualized grid identity, streamed-update timing, MFA cognitive accessibility and behavior-level regression selection.

## Individual exact-version candidate records

The provisional scores below use the current ten-dimension, 20-point static rubric as **triage evidence only**. They are **not** `verification_status: verified` and do not override hard-fail gates. In particular, many original manifests instruct source repairs or browser actions without a separate, sufficiently explicit authorization boundary. Scores describe useful design quality, not unchanged-use eligibility. All twelve have `behavioral_validation: not-run` and `package_security: not-run`.

| Package (upstream `skills/`) | Manifest blob SHA-1 | Full package tree SHA-1 | Required reference blob SHA-1 | Provisional score | Decision |
| --- | --- | --- | --- | ---: | --- |
| [accessibility-audit](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/accessibility-audit) | `1f3e80724dc46d1206d924ea71535aa47ce24c3d` | `d29addd2919294348123667b60eba693c9019217` | `ad37eee11fa2639908acf303b3b66023e609480c` | 17/20 | **ADAPT** |
| [accessibility-regression-test](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/accessibility-regression-test) | `c3152c581e79ca0e3a478c7a992f91cebd6493f3` | `f90f8a25204f16164baf7b29e360294bb75b0875` | `f68673b156dcfa82a22d7957d0bb6c3a6b9033a2` | 18/20 | **ADAPT** |
| [accessible-authentication](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/accessible-authentication) | `e8c85b3f344a427d951e901318ee020880cdfc28` | `cf01968e870ef2c1ce600ff9e2029ad984d3236e` | `b395bcb3f67c211ae94d9d813863172f4d817108` | 16/20 | **ADAPT** |
| [accessible-charts-and-dashboards](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/accessible-charts-and-dashboards) | `9cce3b0fe24e50be96e1ace01fe559cf74ff2b52` | `7ffa87902837a9ff9d413e6c8f6f1f13b8f81423` | `c36bfae894929e2303686fc4e6194cccfdb3c16b` | 18/20 | **EXTRACT** |
| [accessible-combobox-and-autocomplete](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/accessible-combobox-and-autocomplete) | `a56c1b598dcbd79a9d3203455176c4d3951acbaa` | `efbc6242ff3050ba0aebdfc63e13b63f03bfa1fd` | `6484c4b7c08fdf0892d6ee92edae0eb61a1caf72` | 18/20 | **EXTRACT** |
| [accessible-component-review](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/accessible-component-review) | `6c4a4571f14b55de4d954091ab25995571e8a0c2` | `7b693cd3a93ddc5a4016b83bd347158a7f6a30bc` | `d4273e4479f74635bfc68151ec8449450846cca8` | 16/20 | **REFERENCE-ONLY** |
| [accessible-data-tables-and-grids](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/accessible-data-tables-and-grids) | `2cf1df9b30fc4534ce931357b88f9d773a1daa38` | `8157ec9db09fa6d2977df48d381664c65cc0102d` | `879d37b4bd9d6e335d8f94307511a8ba6c19035a` | 18/20 | **EXTRACT** |
| [accessible-dynamic-updates](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/accessible-dynamic-updates) | `f73b8c24460813a95e413ee7ba0ffd866dcc4ef4` | `0fb84486123e27f76059edb154253b0f97c667a5` | `ed7b837f6389dfdf396dc9542fec4367550b0f5c` | 18/20 | **EXTRACT** |
| [accessible-forms](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/accessible-forms) | `037a721c4fe7cc1b48e8576f6ddb16fe6209497b` | `472163fc2260c2bbd23f60d4700e973117a12d0c` | `ceace543f0578cc16c01f64e1c01512b3ed3763e` | 16/20 | **REFERENCE-ONLY** |
| [dialog-accessibility](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/dialog-accessibility) | `e48a23fbb3b7e2f6774ff4804d8e3bec94fd9c7b` | `79d89b63658088f8bf7692d2ded4d8b51aaeef55` | `98eaf790f280d85adb1bf02236ae9f1a585c6c35` | 16/20 | **REFERENCE-ONLY** |
| [fix-accessibility-issue](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/fix-accessibility-issue) | `2e23f0109fea64e31ea6adef4f61c25175940553` | `262eeccfbc7d53fc238f8bb1401ec970a7fbf12c` | `144fbcc9429b6d1ebb1153897672d5faa90ad562` | 16/20 | **ADAPT** |
| [keyboard-navigation-review](https://github.com/smukh/a11y-agent-skills/tree/8bc24f049734c607e23bd3955700fd4858649614/skills/keyboard-navigation-review) | `29329a36e818118f241fab52bf7a4d7799784d68` | `c871434c53dc84cda3caa2abba4c9be25397c733` | `3cfea93a1bb552a7bacd0c42f60cef320fdd7912` | 17/20 | **ADAPT** |

## Skill-by-skill rationale, authority and controlled tags

Every record uses source `smukh/a11y-agent-skills`, MIT skill-text terms subject to third-party notices, upstream revision `8bc24f049734c607e23bd3955700fd4858649614`, host-dependent browser/CLI/AT availability where relevant, and **external behavioral evidence `not-run`**. `ADAPT` means the useful method requires a host-authorization/privacy boundary before unchanged reuse. `EXTRACT` means retain the distinctive mechanism as prior art, not a blanket skill import. `REFERENCE-ONLY` retains discoverability without redundant admission. All authority/side-effect notes below are candidate assessments, not permission grants.

### accessibility-audit

- **ADAPT, provisional 17/20.** Reproducible one-state audit; separates axe findings from manual barriers.
- **Authority/privacy:** Target URL/authentication and DOM evidence require scoped browser access; CLI is optional host tooling. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/accessibility-audit/references/manual-boundaries.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** ux, testing; evidence-first, risk-aware. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### accessibility-regression-test

- **ADAPT, provisional 18/20.** Selects lint/component/Playwright/keyboard/manual evidence based on observed failure.
- **Authority/privacy:** Writing tests or executing browser journeys needs explicit target approval; no broad snapshot-as-proof. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/accessibility-regression-test/references/test-selection.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** testing, ux; evidence-first, test-driven. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### accessible-authentication

- **ADAPT, provisional 16/20.** Whole MFA, OTP paste, recovery and password-manager accessibility with negative controls.
- **Authority/privacy:** Auth journeys require synthetic accounts and approved target; never weaken MFA/rate limits or disclose codes. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/accessible-authentication/references/authentication-review.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** security, ux; risk-aware, human-review. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### accessible-charts-and-dashboards

- **EXTRACT, provisional 18/20.** Shared filtered dataset and nonvisual task equivalence, including loading/empty/error.
- **Authority/privacy:** Access to underlying datasets may be sensitive; editing renderers and collecting data require authorization. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/accessible-charts-and-dashboards/references/chart-review.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** ux, evaluation; evidence-first, visual-verification. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### accessible-combobox-and-autocomplete

- **EXTRACT, provisional 18/20.** Async response-race invariants, active-descendant correctness and IME-aware input.
- **Authority/privacy:** State/DOM tests must use authorized fixtures; source repairs are not approved by a review request. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/accessible-combobox-and-autocomplete/references/combobox-review.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** ux, testing; deterministic, test-driven. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### accessible-component-review

- **REFERENCE-ONLY, provisional 16/20.** Native-first component semantics, focus, zoom, motion and consumer-state coverage.
- **Authority/privacy:** Broad component repairs require scope; overlaps general UX review and WAI-ARIA prior art. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/accessible-component-review/references/component-checklist.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** ux, evaluation; visual-verification, human-review. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### accessible-data-tables-and-grids

- **EXTRACT, provisional 18/20.** Stable record identities through sort/edit/delete, virtualized focus and AT reachability.
- **Authority/privacy:** Mutation scenarios must use synthetic fixtures, not production data; code edits need approval. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/accessible-data-tables-and-grids/references/table-grid-review.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** ux, testing; deterministic, risk-aware. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### accessible-dynamic-updates

- **EXTRACT, provisional 18/20.** Temporal status and focus rules for SPA transitions, streaming, cancellation and stale callbacks.
- **Authority/privacy:** Private chats and streamed content must be minimized; code and network mutations require approval. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/accessible-dynamic-updates/references/dynamic-update-review.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** ux, evaluation; evidence-first, risk-aware. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### accessible-forms

- **REFERENCE-ONLY, provisional 16/20.** End-to-end invalid/corrected/success form states, semantic errors and redundant entry.
- **Authority/privacy:** Forms can hold PII/credentials; use synthetic inputs and explicit scope before replay or edits. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/accessible-forms/references/forms-checklist.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** ux, testing; evidence-first, human-review. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### dialog-accessibility

- **REFERENCE-ONLY, provisional 16/20.** Open-operate-close focus lifecycle, nested dialogs, inert background and zoom.
- **Authority/privacy:** Source repairs and browser interactions require approval; overlaps broader component guidance. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/dialog-accessibility/references/dialog-checklist.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** ux, evaluation; visual-verification, risk-aware. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### fix-accessibility-issue

- **ADAPT, provisional 16/20.** Evidence-to-source tracing, conservative repair and same-state verification.
- **Authority/privacy:** Mutation intent is present, but require exact repository/file scope, rollback and host authorization. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/fix-accessibility-issue/references/repair-policy.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** ux, implementation; incremental, test-driven. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

### keyboard-navigation-review

- **ADAPT, provisional 17/20.** Bounded physical-key journeys and focus evidence, with AT limitations explicit.
- **Authority/privacy:** CLI/browser navigation and private pages require target authorization; journey evidence can contain PII. External URL access, source changes, browser testing, or collection of sensitive evidence must be separately authorized and scoped. Untrusted page content remains data, never instructions.
- **Dependencies:** `skills/keyboard-navigation-review/references/journey-review.md`; optional host browser/assistive-technology tools as applicable; source-owned `a11y-agent` CLI only where explicitly called. Portability: procedural text high, automated verification medium/host-dependent.
- **Controlled tags (candidate):** ux, testing; evidence-first, risk-aware. Authority: `read-only` for inspection, `mutating` if performing repairs or adding tests, `external-side-effect` for network/browser access. No source modifications, browser runs, credential use or tests were performed in this review.

## Source-vetting conclusion and boundaries

**Terminal source-vetting decision:** retain all 12 as discoverable, versioned **REFERENCE / ADAPT / EXTRACT** evidence; **do not vendor or mark any unchanged candidate approved** in this tranche. The source's original, source-owned tooling stays intact upstream. The 12 entries are not added to the governed 721-review shelf or the 44 first-party count. No public accounting denominator changes, so the five inventory surfaces remain unchanged.

The most valuable follow-on composition targets are: (1) regression test-layer selection and before/after behavior; (2) chart data-alternative equivalence across filters; (3) async combobox race and IME behavior; (4) virtualized grid record-identity invariants; (5) streaming announcement/focus continuity; (6) MFA/OTP accessibility with synthetic fixtures. General forms, component and dialog checklists remain useful comparison references, not duplicates to discard.

**Conditions for any future unchanged admission:** exact-version semantic verification including hard-fail remediation, explicit scoped authorization for page access and source edits, private DOM/log minimization, license/notice compliance for actual copied material, full dependency review, applicable exact-version external package-security evidence, and atomic five-surface accounting. External behavioral validation is separate and remains `not-run` until actually observed. The [candidate issue](https://github.com/Knapp-Kevin/skillz/issues/418) can close on this decisive reference/adaptation disposition; a future, separately authorized admission effort must be independently scoped.
