# Inclusive discovery expansion: environment, civic, physical systems, arts and accessibility

**Snapshot 2026-11-01.** This is the third source-intake tranche for the passive `skillz` reference corpus. See [initial 15-source inventory](INDEX.md), [second 14-source expansion](DOMAIN_GAP_EXPANSION.md) and [SHA audit](audit/README.md). The newest additions **do not grant unchanged-use eligibility**.

## Collection receipt

**17 new original GitHub repositories, 17 source-pinned static CSV inventories, 440 additional exact SKILL.md path identities.** Each row has an immutable source revision, Git blob fingerprint, package-directory Git tree fingerprint, supporting-blobs count, and `DISCOVERED_UNGRADED` status. All 17 source tree responses reported `truncated=false`. This is *source enumeration*, not copying, executing, installing, approving or behavioral grading.

| Discipline / source perspective | Immutable source | SKILL.md paths | Original identity inventory | Observed license context |
|---|---|---:|---|---|
| climate weather datasets | [`jinwx/weather-data-skills`](https://github.com/jinwx/weather-data-skills/tree/263437cf110d64c20f3eed8e9429240e7c976973) | 1 | [`climate-weather.csv`](climate-weather.csv) | MIT |
| scientific research workflows | [`dgilford/ai-science-toolkit`](https://github.com/dgilford/ai-science-toolkit/tree/c88bb438241339067fbb6fc0504155c082d837da) | 24 | [`climate-science-toolkit.csv`](climate-science-toolkit.csv) | MIT |
| GIS data and ArcGIS workflows | [`danmaps/gis-agent-skills`](https://github.com/danmaps/gis-agent-skills/tree/7b53423036342d917392dd9d7bd350e33ecd3f59) | 21 | [`gis-operations.csv`](gis-operations.csv) | NOASSERTION (no root LICENSE observed) |
| geostatistics and geospatial AI | [`muend/geoai-skills`](https://github.com/muend/geoai-skills/tree/19937ce14c7d60d764732cc2688c6a3dd92f6d0e) | 18 | [`geoai.csv`](geoai.csv) | MIT |
| government and civic service navigation | [`skills-il/government-services`](https://github.com/skills-il/government-services/tree/55c2d6ce9161307dfc0c161dd7d2230abf742863) | 31 | [`government-services.csv`](government-services.csv) | MIT |
| civic notices and public problem analysis | [`AI-Lab-for-Cities-at-Harvard/civic-skill-exchange`](https://github.com/AI-Lab-for-Cities-at-Harvard/civic-skill-exchange/tree/5ab9eece30fe5229add5b4155677c5ac9588716f) | 9 | [`civic-exchange.csv`](civic-exchange.csv) | Root MIT, individual skills separately licensed |
| pet-health education (brand-affiliated) | [`Glumoo-ai/glumoo-pet-health-skill`](https://github.com/Glumoo-ai/glumoo-pet-health-skill/tree/62fbf378a1476cb1ddce87787c98c7ddebeb5e21) | 1 | [`veterinary-pet-health.csv`](veterinary-pet-health.csv) | MIT |
| industrial quality and logistics | [`ai-evos/agent-skills`](https://github.com/ai-evos/agent-skills/tree/1eda1feb184cfde82175d4ffa5feccf6501a4394) | 8 | [`industrial-supply-chain.csv`](industrial-supply-chain.csv) | Apache-2.0 |
| factory/manufacturing specialization | [`AirsupHQ/factory-skill`](https://github.com/AirsupHQ/factory-skill/tree/9fde7554e6a30e77ea1008dec08f2ba8d8d37f27) | 1 | [`manufacturing-factory.csv`](manufacturing-factory.csv) | MIT (third-party vendor notices) |
| PCB fabrication and KiCad ecosystem | [`aklofas/kicad-happy`](https://github.com/aklofas/kicad-happy/tree/2fd9aa0fe2d620f36627d9221e8b1393987ae38e) | 11 | [`electronics-kicad.csv`](electronics-kicad.csv) | MIT |
| circuit design and SKiDL | [`nickkraakman/skidl-skills`](https://github.com/nickkraakman/skidl-skills/tree/1b33fb9151b69c5f9c3009f50b0ec3868f3da038) | 4 | [`electronics-skidl.csv`](electronics-skidl.csv) | MIT-form license text |
| logistics documents and product workflows | [`orbit-logistics/orbit-skills`](https://github.com/orbit-logistics/orbit-skills/tree/57333e8a8e64db85fd7a8377841ea6325b894dda) | 2 | [`logistics-orbit.csv`](logistics-orbit.csv) | Apache-2.0 |
| humanities research and writing | [`tizzy916/humanities-writing-companion`](https://github.com/tizzy916/humanities-writing-companion/tree/e097ff629f6575af1b2ec129afa7b23f30d2a39c) | 1 | [`humanities-writing.csv`](humanities-writing.csv) | CC BY-NC 4.0; noncommercial restriction |
| historical research | [`Travishistory/history-research-agent`](https://github.com/Travishistory/history-research-agent/tree/515ab776f4906f35e13e6142cde738388813c519) | 1 | [`history-research.csv`](history-research.csv) | MIT |
| cognitive/digital accessibility | [`Owl-Listener/inclusive-design-skills`](https://github.com/Owl-Listener/inclusive-design-skills/tree/6e0740f04b2130af60bc57abe3401b91e460e70d) | 58 | [`inclusive-design.csv`](inclusive-design.csv) | MIT |
| audio, visual and media production | [`calesthio/generative-media-skills`](https://github.com/calesthio/generative-media-skills/tree/8c85352d5d75d4dcbe58480bd138e37b9742bab1) | 153 | [`generative-media.csv`](generative-media.csv) | MIT |
| writing craft across host integrations | [`haowjy/creative-writing-skills`](https://github.com/haowjy/creative-writing-skills/tree/1cb520f9c61e79ce2b1c56dba18601b2d6873433) | 96 | [`creative-writing.csv`](creative-writing.csv) | Apache-2.0 |

**License precision:** License types above were determined by fetching the actual original root license text at the named revision, except for GIS operations (no root license observed); they are **source-level hints**, not per-package redistribution grants. Harvard's civic repository states explicitly that each skill can carry its own license; an example notice-rewriter skill has `license: CC0-1.0` in frontmatter. The humanities writing source uses `CC BY-NC 4.0`; retain for reference and analysis, **not unchanged commercial reuse** absent separate rights. `AirsupHQ/factory-skill` discloses third-party `three.js` vendor licensing. Root licensing does not clear embedded datasets, design media, trademark, tools or supporting scripts.

## Genuine capability expansion, not just more filenames

- **Climate and Earth observation:** climate/weather dataset intake adds a source; GIS, remote sensing, geospatial processing and map publication gain two independent publishers. Need weather science, water, biodiversity, field measurements and map-validation evidence.
- **Public sector:** government navigation and civic service notices give complementary citizen-service and public-information use cases; they **do not** prove statutory correctness, official endorsement or any authority to send notices or submit government forms.
- **Veterinary and animal welfare:** an initial cat/dog health education candidate is recorded. It is brand-affiliated and *not* a comprehensive veterinary corpus. Medical advice, emergency triage and product conflicts demand qualified external review.
- **Electronics and manufacturing:** KiCad, SKiDL, quality nonconformance, factory processes, logistics and supply-chain workflows are now represented. Electrical safety, fabrication QA and regulated manufacturing tests remain unqualified.
- **Accessibility and inclusion:** a dedicated cognitive/digital accessibility collection adds 58 paths, richer than generic web accessibility alone. Observe multimodal, physical, educational, cultural, language and nonvisual accessibility gaps.
- **Media and writing:** 153 audio/video/generative-media entrypoints and 96 creative-writing paths create more comparison opportunities; large package numbers and host-specific clones can overstate independent methods. Verify final audio/video artifacts, rights, caption/accessibility and professional workflow behavior.
- **History, humanities and archives:** sources appear for historical methodology and humanities prose, but provenance ethics, archival citation, preservation and disciplinary alternatives remain sparse.

## Current archive accounting

| Measure | Result |
|---|---:|
| Earlier repositories / paths | 29 / 3,743 |
| New repositories / paths | 17 / 440 |
| **All collected repositories / source-file paths** | **46 / 4,183** |
| Unique byte-identical `SKILL.md` file hashes | **4,155** |
| Duplicate occurrences / exact-blob groups | **28 / 28** |
| Cross-repository exact-blob matches found | **0** |
| New skills admitted into governed inventory | **0** |
| Actual behavioral evaluation runs in this tranche | **0** |

Byte-level comparison of [SHA batches 01–06](audit/README.md) is **not** semantic deduplication. The 28 duplicate groups include FreeCAD host paths, a GIS agent-configuration path, numerous creative-writing cross-host copies and an accessibility pair with matching content. Crucially, **byte-distinct files do not prove distinct methodologies**.

## Intake priorities, by emerging deficit

1. **Source breadth first** across all category/subdomain checklists. Do not close the discovery door after finding one plausible candidate; preserve competing methods and implementation ecosystems.
2. Next, *method-level* identity graph and qualified coverage scoring by subdomain, preserving source originality, derivation, language variants, host variants, dependencies and license restrictions.
3. Then task-level baseline-vs-skill evaluation, security/authority, license, portability, freshness and specialist review. Publish component grades and direct receipts, not ungrounded overall stars.
4. If repeated search plus measured evaluation demonstrates a real unsatisfied user task, draft a narrowly scoped **first-party gap-fill skill** through maintainer governance, with positive/negative examples, risk boundary and test suite. Keep such a draft unadmitted until independently reviewed. **Do not generate a filler skill merely because the catalog count or a category column looks thin.**

All findings are reference-only, source-pinned and outside the canonical admitted corpus. No local scripts, CI workflows, scanners or autonomous repository automation were added.
