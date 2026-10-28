# Governed discovery: WordPress, MicrosoftDocs and Remotion skill sources (2026-10-27)

**State: 3 new source leads, 3 exact representative manifests inspected, 0 source admissions, 0 unchanged-use approvals.** This is source-level discovery intelligence, not a complete candidate issue, an exact eligible denominator, or a security/behavioral scan. None of the three canonical source identities matched current default-branch `skillz` code-search results for its exact repository string; that is **preliminary deduplication**, not a proof that no aliases or historical references exist.

## Search funnel

- **Three GitHub discovery queries:** `agent-skills pushed:>2026-10-25 stars:>2`, `SKILL.md pushed:>2026-10-25 stars:>1`, and `skills agent instructions created:>2026-10-20`. The first 30 results from each produced **90 repository rows / 89 distinct repository identities**. Recency is a search filter, **not** proof that an individual skill was newly published or improved.
- **Additional public surfaces checked:** recent public agent-skills coverage, Hugging Face-related skill searches, and the skills.sh ecosystem/security discovery surface. Search results were predominantly older source guides or already known catalogs; no additional exact-package candidate was promoted from them.
- **Newly recorded source leads:** 3 canonical repositories with exact observed HEAD, README and representative SKILL.md blob. **New candidate issues:** 0, because these are still bounded source-vetting leads rather than individually admitted candidate packages. **Qualified exact-version reviews:** 0. **Last successful discovery in this run:** 2026-10-27.

## Lead 1: WordPress contributor skills

- **Canonical source:** https://github.com/WordPress/agent-skills
- **Observed HEAD:** `eff3785fc28c4380d172094518c66a6a997c95d4`
- **Root README blob:** `1fe8b76b3e624361a160eb82dc1141e52040deca`
- **Root LICENSE blob:** `d3fc07ba4bd24a1f5c2d9f3a39f9e0ed4442dba3`; GPL-family text, **not MIT**. Exact license version and compatibility with reuse/vendor policies must be checked before any copying.
- **Exact representative manifest:** [`skills/wp-abilities-verify/SKILL.md`](https://github.com/WordPress/agent-skills/blob/eff3785fc28c4380d172094518c66a6a997c95d4/skills/wp-abilities-verify/SKILL.md), blob `96bbc6207f4d7a0c0fbe2bd396f26a5e7c6852a7`.
- **Distinctive mechanism:** Adversarially verifies that a WordPress Abilities API declaration of `readonly: true` does not conceal actual writes. Separates static heuristic checks from runtime permission/idempotency checks and explicitly says static PASS is not proof of write-freedom.
- **Risks:** PHP/WordPress runtime, Docker/wp-env and Node/shell dependencies, execution of plugin callbacks, database mutations and possible private site content. Root README discloses AI-assisted authorship and contributor review; neither is automatic trust. **Disposition: SELECTIVE SOURCE VET / EXTRACT candidate**. Prioritize static read-only annotation-correctness mechanism, not runtime invocation without scoped authorization.

## Lead 2: MicrosoftDocs generated Azure skills

- **Canonical source:** https://github.com/MicrosoftDocs/Agent-Skills
- **Observed HEAD:** `95544200a6621ee7481b253beb115ac0be701689`
- **Root README blob:** `ffbdb19d8ca095776752500f6c0eb8a058afd2d8`
- **Root LICENSE blob:** `e056e7c3ec54533985dfb3a4c6ef70dab8ca2e42`; begins CC BY 4.0 legal text. README also advertises MIT, so **license is mixed/unclear at package granularity**; do not blanket-vendor.
- **Exact representative manifest:** [`skills/azure-monitor/SKILL.md`](https://github.com/MicrosoftDocs/Agent-Skills/blob/95544200a6621ee7481b253beb115ac0be701689/skills/azure-monitor/SKILL.md), blob `c7fdf29cc30373e04b3831e8241154ae92f86eb5`.
- **Distinctive mechanism:** Generated service-specific reference navigation, source freshness metadata (`generated_at: 2026-10-25`) and Microsoft Learn retrieval through host tools. README advertises **193+** skills, **not** an independently enumerated eligible denominator.
- **Risks:** Generated prose can be stale or incomplete; network fetching can carry private context and untrusted content; overlap with already admitted Microsoft Skills and Azure Skills is high. **Disposition: REFERENCE-ONLY / selective novelty audit**, not a new pinned corpus or automatic verification.

## Lead 3: Remotion creative video skills

- **Canonical source:** https://github.com/remotion-dev/skills
- **Observed HEAD:** `30d4553ecd46fbc5212fd0ff006ae43af522158b`
- **Root README blob:** `ed8881a733427ddc5628db9a614de88cf2ddc394`
- **Root LICENSE:** not found at `LICENSE` in this bounded pass; package-specific terms and possible other license paths **unresolved**.
- **Exact representative manifest:** [`skills/remotion-markup/SKILL.md`](https://github.com/remotion-dev/skills/blob/30d4553ecd46fbc5212fd0ff006ae43af522158b/skills/remotion-markup/SKILL.md), blob `46f66b5b581e56d129a7da949d8e9be116fb8a68`.
- **Distinctive mechanism:** Remotion frame/fps-aware React composition guidance, editable timing and interactive component patterns, source-change preservation. README describes multiple skill entry points and a generated README; **no exact first-class package denominator** was established.
- **Risks:** Render/runtime dependencies, filesystem changes, asset licensing, video/audio and potentially personal media, unqualified source license. Source-owned README generation/scripts do not authorize adding a generator to `skillz`. **Disposition: TRACK / REFERENCE-ONLY pending license and package-tree audit**.

## Macro decision and next action

WordPress's *annotation claim versus actual effect* verification offers the clearest differentiated security method; Remotion's timeline/editability discipline offers a different creative capability; MicrosoftDocs is a high-overlap documentation retrieval surface. None is admitted or installed. Resolve source licenses, canonical first-class denominators, package dependencies and overlap before opening bounded issue-first candidate tranches. Do not create one issue per index entry.

This discovery lane is separate from the Microsoft Skills admitted-source freshness evidence and from draft PRs #412, #413 and #416. It changes **zero** source identities, pins, first-party counts, governed verification companions, package-security passes, behavioral validations or public accounting totals. The passive architecture is unchanged.
