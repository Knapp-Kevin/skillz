# Capability expansion discovery, wave 2: 2026-10-26

**State:** discovery and preliminary source vetting. **No new admission, exact-version semantic verification, package-security pass, or behavioral validation.**

## Baseline and scope

Repository: `Knapp-Kevin/skillz`. Starting `main` `f11c13eb9ba1fed883d91958846a3d550db4b367`. Current README, AGENTS, governance index, system state, queue, taxonomy and source registry were inspected before discovery. Current catalog: **44 first-party skills, 22 source identities, 12 pinned reference corpora, 721 persisted third-party exact-version reviews**. These numbers are unchanged by discovery. Prior [wave 1](capability-discovery-2026-10-26.md) already identified 14 leads; this wave intentionally excludes those 14 and the 22 registered source identities. #418 owns accessibility evaluation of smukh; #414 owns provisional capability gaps.

The repository is **entirely passive**. Source-authored scripts and tooling remain upstream evidence, never skillz-owned execution. This cycle did not execute source packages, use credentials, inspect private project data, install tools, run scanners, or conduct behavioral validation.

## Macro gap map

| Differentiated capability | Current overlap / uncertainty | Priority |
| --- | --- | --- |
| Precision-oriented combined CWE/GDPR source-code review with detector/validator suppression | Existing security reviews and #412 trust/data lifecycle proposals; exact detector/validator methodology is distinct | High |
| Game-engine-specific headless tests, exports, resource lifecycle, multiplayer and shaders | Existing generic code/testing/release skills, but no named game-engine first-party skill | High |
| Hardware-board pin/PSRAM/camera constraints and firmware recovery | Generic implementation skills do not provide board-specific physical constraints | High, elevated physical side-effect risk |
| Translation key drift, provider cost and locale review handoff | Existing writing/communication skills do not establish i18n file/provider mechanics | High, external provider privacy/cost |
| Reproducible computational biology and scientific-paper reproduction | General research/evaluation coverage; specialized scientific tools and data privacy need deep review | Medium/high |
| Incident log-to-trace diagnosis, cost and query-language migration | Existing monitoring and agent-cost #414 overlap; vendor-specific live production access raises authority burden | Medium |
| Jurisdiction-specific legal contract evidence | General document review overlaps; jurisdiction/freshness and sensitive personal data are critical | Medium |
| Behavioral accessibility evidence | Already actively owned by #418; compare, do not duplicate candidate admission | Reference-only this cycle |

## Twelve *new* canonical source leads

Observed revision is a **source HEAD**, not an approved admission pin. `Root terms` are observed GitHub metadata unless explicitly marked as LICENSE-body inspected. The source owner is the GitHub repository owner. Every entry: `admitted=0`, `semantic_verified=0`, `security=not-run`, `behavioral_validation=not-run`.

| Rank | Canonical source / observed HEAD | Root terms | Unique value and preliminary decision | Dependencies, authority/privacy and overlap |
| --- | --- | --- | --- | --- |
| 1 | [facebookresearch/secpriv-skill](https://github.com/facebookresearch/secpriv-skill) `70e1269a988cb401ac838164b3db9434ffa9f4ea` | **MIT LICENSE body inspected** | **SELECTIVE VET**: one root SKILL.md combines CWE and GDPR code-flow review with detector/validator suppression and explicit confidence thresholds. Benchmark claimed, not executed. | Source-code and personal-data-flow inspection require scoped access; no automatic legal certification. Overlaps security/data-lifecycle review but differentiates cross-domain suppression. |
| 2 | [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) `184b72be02884f782a0058f2eeae2ce4277453e4` | **Apache-2.0 LICENSE body inspected**, NOTICE present | **SELECTIVE VET** (#420): source claims 74 engine-specific skills; exact first-class denominator not yet established. Godot headless testing and export mechanisms inspected. | Godot 4.7 and other engine/tool versions; project writes, installs, builds and publishing require explicit authority. Stronger specificity than generic testing/release. |
| 3 | [alexex1993/mcu-skills](https://github.com/alexex1993/mcu-skills) `48b56f8756a21c6e566bd3edd6a1f942b4ef2738` | MIT metadata | **SELECTIVE VET**: MCU family subtrees for ESP32, STM32, RP2, nRF, AVR, etc.; inspected ESP32-S3 camera board constraints. | Board-specific toolchains, pin maps, flashing and physical hardware changes. Elevated irreversible/device safety risk. Never flash without device-scoped approval. |
| 4 | [verbatra/skills](https://github.com/verbatra/skills) `d772c10ffe53263c777bcd07a9841b67aacdf1d1` | MIT metadata | **ADAPT/SELECTIVE VET**: three provider-specific CLI/MCP/Studio skill directories; locale-key drift, translation costs and human review. | Vendor CLI/MCP, paid translation providers and private source strings. No provider send or money-bearing action without approval. |
| 5 | [ssinder/bioinformatics-agent-skills](https://github.com/ssinder/bioinformatics-agent-skills) `0b337a346f0c5d50b12c4f1ae2d82855da98615e` | MIT metadata | **SELECTIVE VET**: 17 observed top-level skill directories; scRNA-seq, protein structure, docking and scientific figures. | Python/Scanpy or alternative pipeline; health/genetic data can be sensitive. Algorithmic equivalence claims need independent evidence. |
| 6 | [onescience-ai/OneSkills](https://github.com/onescience-ai/OneSkills) `e4da8dd75961ae448dfb8978906052d211156d83` | MIT metadata | **EXTRACT/SELECTIVE VET**: structured paper reproduction specifications and evidence handoff, separate from code execution. | Orchestrator and file handoff dependencies; other skills submit compute jobs and publish externally. Paper-to-code output is not reproducibility proof. |
| 7 | [jxtse/scientific-research-skills](https://github.com/jxtse/scientific-research-skills) `68098d5565f423ffcfce1c9936de77ae230843aa` | MIT metadata | **ADAPT/OVERLAP REVIEW**: seven research directories including three-depth paper reading, literature search and Zotero. | External scholarly sources, PDF access, citation verification and Zotero/private library permissions. Generic paper summary overlaps existing research. |
| 8 | [axiomhq/skills](https://github.com/axiomhq/skills) `e5d68f9362719a7ab0c80567626cb6c9c473c165` | MIT metadata | **EXTRACT/SELECTIVE VET**: APL query, SRE trace investigation, Splunk translation and telemetry-cost diagnosis. | Live production logs, sensitive traces, dashboards and alerts. `axiom-controlling-costs` asks for parameters but does **not thereby authorize** monitor/dashboard writes. #414 overlap. |
| 9 | [donrami/employment-contract-review](https://github.com/donrami/employment-contract-review) `0c70d4b70f5a557eb815990aad18e373979c68a1` | MIT metadata | **REFERENCE-ONLY/SELECTIVE VET**: German/EU clause-by-clause contract risk review with explicit jurisdiction and law-as-of 2026-08-22. | Sensitive identity/employment details; jurisdiction-specific law, external citation verification, no legal outcome guarantees. |
| 10 | [fastfold-ai/skills](https://github.com/fastfold-ai/skills) `c8f441633c77bb918bc4bdc9d59d5e293239a1f2` | **Unclear**: no root LICENSE in inspected root | **REFERENCE-ONLY, NO VENDOR**: Boltz API protein design, molecular dynamics and structure analysis. | Vendor API credentials, paid cloud jobs, potential proprietary biological data. Do not promote without exact package terms. |
| 11 | [mgifford/accessibility-skills](https://github.com/mgifford/accessibility-skills) `ada839399f053c55e1a776a98c02f8904d70dd32` | AGPL-3.0 metadata | **REFERENCE-ONLY/COMPARATIVE**: behavioral accessibility outcomes distinguish indicators, cannot-tell and confirmed failures. | Browser automation, private-page evidence, strong redistribution terms; overlaps #418 and existing wave-1 accessibility sources. |
| 12 | [sinzin91/awesome-sre-skills](https://github.com/sinzin91/awesome-sre-skills) `962f6a2149d0688a8c32d9e12948c5102cc9d184` | CC0-1.0 metadata for list | **DISCOVERY SURFACE / REFERENCE-ONLY**: 86 claimed SRE pointers; no first-class skills in inspected root. | Each linked upstream has separate owner/license/revision. No inherited trust or double-counting from aggregator. |

## Exact-version samples inspected, not semantic verification

- SecPriv `SKILL.md` blob `852c54b9a9fe131f29200359274724b70d43f6cb`, MIT `LICENSE` blob `b93be90515ccd0b9daedaa589e42bf5929693f1f`. Its structured findings include category, confidence, file/line, remediation, CWE or regulatory basis.
- Game development `skills/godot/godot-gdscript-headless-testing/SKILL.md` blob `c8eea6a301309564c95f028a92f6ee651341b1b6`; `skills/godot/godot-export/SKILL.md` blob `7f8962080187ac87376a3cea966500ce4243c3b5`. Apache-2.0 `LICENSE` blob `c7fc0c6d59cb8129a0e30fe13f5a6118f3933c44`. Distinguish source-owned CI guidance from prohibited skillz CI.
- MCU ESP32-S3 camera `SKILL.md` blob `a04a97563ff4771b21974cc48d4f119e5ded51ee`, physical pin and PSRAM conflict mechanisms.
- Verbatra CLI `SKILL.md` blob `c10598425084900e83f387205da4dcb76f79b2d0`, explicit cost/credential guidance but requires action-specific authorization.
- Single-cell RNA-seq `SKILL.md` blob `135944c305f9284b0b12ed8639fa0c3177349883`, alternative backend claims unvalidated.
- OneScience paper reproduction `SKILL.md` blob `702221645b6037b82058167c8ce529184f4446aa`, handoff-based specification only.
- Scientific paper reading `SKILL.md` blob `77a6d34c6daf39a4f978debfa5353be9df8f342f`.
- Axiom cost control `SKILL.md` blob `4aa071a66b03957dc6d798b1a5a19d518fff4f77`.
- German employment contract review `SKILL.md` blob `51f62c147b04114182a072fc8179d30348dc549f`.
- Fastfold Boltz `SKILL.md` blob `9149a1d6623731e1b086d168ec8156db89660703`.
- Behavioral accessibility `SKILL.md` blob `1731e9652b89cba5623f76d4063751a90f455884`.
- SRE aggregator `README.md` blob `feb3f155ba1c5020480d17708c07c3602c6c3a92`.

## Macro findings and decision gates

1. **Highest new coverage value:** security/privacy precision review, game-engine-specific validation, embedded hardware constraints, localization provider controls, and computational biology. These are distinct from generic coding/monitoring prompts.
2. **Highest authority risk:** firmware flashing, paid translation and bioinformatics services, production telemetry, compute-job submission, credential-bearing files and private employment/genetic records. Tool availability, input confirmation or warning text is not authorization.
3. **License gate:** fastfold cannot be vendored with unclear root terms; AGPL accessibility source needs redistribution obligations assessed. Root aggregator license does not cover linked repositories.
4. **No fake quality evidence:** source HEADs, Git blobs, LICENSE and sampled procedures are discovery evidence only. The source's benchmark or test suite has **not** been executed. Semantic `verified`, package security `passed`, and behavioral `validated` are all **zero new**.
5. **No accounting inflation:** twelve new leads and one bounded candidate issue (#420) create **zero** new admitted sources, **zero** new user-facing skills, and **zero** new persisted verification companions. The five public accounting surfaces therefore remain unchanged.

**Flow:** 12 newly identified source leads; 12 source identities and exact HEADs inspected; 13 sampled skill/document blobs inspected; 2 LICENSE bodies inspected; 1 bounded issue opened (#420); 0 admissions, 0 new static verifications, 0 package scans, 0 behavioral validations.

**Next highest-priority action:** complete #420's bounded Godot-first source-vetting and selective exact-version semantic review, then issue decisive per-skill dispositions with the appropriate package-security gate. Keep #418's accessibility work separate.
