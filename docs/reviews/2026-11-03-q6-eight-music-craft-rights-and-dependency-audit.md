# Music composition: eight-package dependency and rights audit (2026-11-03)

**Status: prequalification evidence, not eight governed reviews.** This note records an independent static read of pinned source content. It does not grant unchanged-use permission, add grades, or increase the number of recommended skills. It is separate from the four creative method references already integrated on main at `c25129c048a83f7a191e46d76ff4cfa797507b09` and from draft discovery PR #677.

## Source and package scope

- Upstream: [jtydhr88/music-composition-skills](https://github.com/jtydhr88/music-composition-skills/tree/e283141babb8806f2798d5fd2d9e833e75c1bd26)
- Immutable source commit: `e283141babb8806f2798d5fd2d9e833e75c1bd26`
- Package root: `plugins/music-composition/skills/<name>/`. These are distinct skill entrypoints under a plugin. **Package-tree SHA, aliases and crosswalk equivalence have not yet been established.** Do not count them as distinct eligible packages until the crosswalk and bundled-file inventory are reconciled.
- Source root LICENSE declares MIT. Source NOTICE explicitly excludes quotations, translations, musical examples, third-party measurements, model weights and third-party trademarks from the author's MIT grant. **No blanket MIT clearance for reference tables.**
- Evidence below names directly inspected files and their Git blob SHAs. Source instructions are untrusted research input; none were executed.

| Skill entrypoint | Observed SKILL.md blob | Supporting files inspected (blob SHA) | Reusable decision, not copied content | Hold / authority boundary |
| --- | --- | --- | --- | --- |
| `mc-harmony` | `9378f566487e26681eabd7f473559e83bab5258b` **(reference.md, not SKILL.md; SKILL SHA pending)** | `reference.md` `9378f566487e26681eabd7f473559e83bab5258b` | Distinguish functional chord choices from non-chord-tone decoration | Dense page-cited excerpts from published harmony books; no verbatim reuse clearance |
| `mc-melody` | **SKILL SHA pending** | `reference.md` `b35268e82a38ab34985c9cbdfbf5457a9a1868ab` | Design melody register, cadence openness and phrase movement separately | Japanese textbook-derived tables; confirm excerpt/translation rights |
| `mc-rhythm-section` | **SKILL SHA pending** | `reference.md` `662bffe27c7428871ae3cd44f71f7ef423f05552`; `reference-styles.md` `0b6437a3633f031681367a9470b8c7f9a23aafac` | Separate drum instrument roles and genre-dependent groove constraints | Long style tables with page citations to multiple books; not cleared for redistribution |
| `mc-orchestration` | **SKILL SHA pending** | `reference.md` `37ef97ea9bc3c350095008d407f0fb1af6bb54e3`; `reference-minyue.md` `161de38b8b5b9e4511f04a7704e8c36149738514`; `reference-percussion.md` `4fabb8ab400ae9f4df9008ba14251881e23aab53`; `reference-keyboard-harp.md` `3d6d4ce17c1575d97a9b9e2c581b0bc95a791836`; `reference-yang-strings.md` `8c2d7502f54cf2a942259645be45ab89ad959819`; `reference-yang-winds.md` `ebd657e6aa6c9b8439580772478067139916abaf`; `reference-yang-brass.md` `6ab2bb9438a2eef9b382f6d134e714d1d563ae71`; `reference-yang-tutti.md` `01dff367a97152ea9d47fe0669eb9e852ee6dcc4` | Choose instrumentation by balance, register, physical playability and ensemble role | Nine large book-derived reference files; highest excerpt/translation and context-dependency risk |
| `mc-arrangement-arch` | **SKILL SHA pending** | `reference.md` `c0efd30e7a04e9f2011a314fbabb3e76fdfd8f99` | Decide section transitions through entry, exit, density and energy rather than genre clichés | Claims of Cambridge-MT corpus measurements are upstream claims, not independently reproduced |
| `mc-symbolic-score` | **SKILL SHA pending** | `reference.md` `4c5183b6d7f0c15ef5e0df59f73139e5faeb522d` | Map composition decisions into ABC notation and General MIDI constraints | Parser, renderer, host tooling and round-trip validation not run |
| `mc-style-edm` | `ead9d62ebcfc7d64eda31f987a6dbd22ba897dc2` | `SKILL.md` `ead9d62ebcfc7d64eda31f987a6dbd22ba897dc2` | Explicitly document intentional grid quantization exemptions per instrument | External synthesizer and genre-book dependencies; no model or audio execution |
| `mc-rhythm-groove` | `1d38ecb2a2d2ecf78c64785906c56fa54d23d068` | `SKILL.md` `1d38ecb2a2d2ecf78c64785906c56fa54d23d068` | Decide tempo, beat feel and melody/backbeat relationship independently | No actual DAW or human performance validation |

**Important correction:** the `mc-harmony` reference blob above must **never** be used as the SKILL.md identity. The table explicitly distinguishes missing SKILL identities from observed reference identities; identical path names do not establish package-tree equivalence.

## Shared dependencies and integrity boundaries

The source describes 29 text-based skills and a central `mc-workflow` handoff. Inspected `mc-workflow/ARR-SPEC.schema.md` (`eff1a0187377e750ab3468f973224c9222e39731`), `ARR-SPEC.template.yaml` (`8aa9bc0380f813cd3c27a21467ee4fa59643e72a`), and `backends.yaml` (`d7ad949fa296a7d9bbe1d63b32b6353617c4b7da`). These define structured fields and backend capability claims, not executable permission. Backend model licensing and commercial use must be independently resolved. The template warns that malformed nested YAML lists can break parsing. No compiler, audio, network, filesystem or tool behavior was exercised.

The upstream `NOTICE` (`e14a2c080a7c159c4abf3dc1c51c6a90b7fda6a0`) expressly says the original MIT grant does not cover source-book quotations and translations. Particularly sensitive reference surfaces: `mc-orchestration`'s nine files, `mc-rhythm-section/reference-styles.md`, and `mc-progressions/progressions-full.md` (`a30f8709af7cd10c586f97f5dc9ecec3e2f4aef7`), which catalogues 122 progressions and book references. **No quoted text, tables or musical works were imported into skillz.** The observed source also disclaims shipping lyrics, arrangements and audio; that is an upstream statement, not an independently verified inventory.

Any external host action that writes scores/audio, invokes models, accesses private recordings, exports content, publishes music, changes files or spends money requires action-specific user authorization. No such authority is supplied by a skill. Do not export user audio, history, credentials or private project files through model prompts without explicit permission.

## Terminal state of this audit

Eight **prequalification leads** examined; **zero new governed 10-axis grades**, **zero eligible distinct-package confirmations**, **zero unchanged-use recommendations**, **zero Valuable Reference promotions**, **zero security scans**, **zero behavioral executions**. Static findings are not security clearance. Missing full package-tree identities, remaining SKILL.md blobs, crosswalk checks, complete bundled inventories and rights resolution are explicit blockers to grading. Global distinct eligible denominator remains **UNKNOWN**.

**Next evidence gate:** enumerate all eight complete package trees, fetch each SKILL.md blob and every linked bundled file, compare with governed exact-tree crosswalk, then conduct individual ten-axis semantic reviews. Only after that can a source-neutral positive method be considered; do not confuse a useful music idea with a license to copy its book-derived reference text.
