# Authored Skills

This is the **canonical home for newly authored first-party skills** produced for this repository: `skills/authored/<skill-name>/`. It distinguishes maintainer-owned original work from the external discovery/reference corpus under `skills/sources/` and historical first-party skills at `skills/<name>/`. "Authored" denotes accountability for source and rights, **not** a claim that a human personally typed every instruction or that AI assistance was absent.

## New skill package requirements

**Required capability indexing:** A new first-party authored package is not complete merely because its files live under `skills/authored/<slug>/`. It must be indexed in `registry/authored-skills-index.json`, `registry/governed-review-name-index.json`, and the canonical `registry/capability-directory.json` under its evidence-backed domain/subdomain routes. The latter must include one canonical `skill_records` identity and `matched_skill_ids` links for every applicable domain; update browse previews and derived counts without counting cross-links as extra skills. Run `node scripts/qa/check-authored-capability-links.mjs` during authorized local repository maintenance. [November 8 example and exact evidence](../../registry/discovery/authored-capability-routing-20261108.json). This is discovery, not host permission or proof of behavioral validation.

1. Put the complete usable package under `skills/authored/<slug>/`: `SKILL.md` plus only the references, examples, fixtures and optional scripts it actually requires. No copied third-party contents without explicit rights.
2. Register **every package** in [`registry/authored-skills-index.json`](../../registry/authored-skills-index.json) with current source path, SPDX license expression, copyright holder, license evidence path, exact `SKILL.md` Git blob SHA, complete package tree SHA, provenance/verification links, and review/test status.
3. For the original first-party content, the repository root [MIT license](../../LICENSE) is the **current default**. This permits proprietary uses and commercial redistribution subject to required notice retention. It does **not** guarantee free-of-charge availability or that derivatives remain open source.
4. If a new skill should use **GPL-3.0** or **AGPL-3.0**, choose it explicitly *before publication*, include the complete applicable legal text and clear per-package `SPDX-License-Identifier` scope. Do not infer copyleft from author intentions or silently relicense third-party materials. AGPL's network-source clause primarily targets qualifying modified network software, not automatically every remotely used Markdown prompt.
5. Record third-party references separately with exact source pin, original publisher, actual rights and attribution. A root LICENSE file is evidence, but nested and bundled material may carry other restrictions. **Unknown rights => do not import.**
6. Keep static semantic review, external scanner evidence, host behavioral tests, permission/authority, and publication clearance as separate fields. A draft package may be statically reviewed with `behavioral_validation: not-run`.

The existing first-party `skills/<slug>/` entries are not automatically moved or relicensed. Move them only as separate, reviewed maintenance work with compatible index/registry updates.

## Current authored packages

[Healthcare Contract Forensics](healthcare-contract-forensics/SKILL.md) | [Package record](../../registry/authored-skills-index.json) | [Review and licensing evidence](../../docs/reviews/2026-11-06-issue714-healthcare-contract-forensics-static-review.md).

[Narrative Scene Gap Audit](narrative-scene-gap-audit/SKILL.md) | [Synthetic acceptance cases](narrative-scene-gap-audit/examples/acceptance-cases.md) | [Exact-source review](../../docs/reviews/2026-11-08-writer-story-tools-original-skills-static-review.md).

[Character Motivation Interview](character-motivation-interview/SKILL.md) | [Synthetic acceptance cases](character-motivation-interview/examples/acceptance-cases.md) | [Exact-source review](../../docs/reviews/2026-11-08-writer-story-tools-original-skills-static-review.md).

**November 8, 2026:** Three original MIT-authored packages are indexed in this collection. All three have bounded static reviews and no executed agent-host behavioral validation. The writing workflows are not copies of [Writer Story Tools](https://writer-story-tools.mdlafilms.workers.dev/), whose external applications remain all-rights-reserved; see [source and rights findings](../../docs/discovery/2026-11-08-writer-story-tools-reference.md). Repository presence is not an installation or external-account authorization.
