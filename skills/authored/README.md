# Authored Skills

This is the **canonical home for newly authored first-party skills** produced for this repository: `skills/authored/<skill-name>/`. It distinguishes maintainer-owned original work from the external discovery/reference corpus under `skills/sources/` and historical first-party skills at `skills/<name>/`. "Authored" denotes accountability for source and rights, **not** a claim that a human personally typed every instruction or that AI assistance was absent.

## New skill package requirements

1. Put the complete usable package under `skills/authored/<slug>/`: `SKILL.md` plus only the references, examples, fixtures and optional scripts it actually requires. No copied third-party contents without explicit rights.
2. Register **every package** in [`registry/authored-skills-index.json`](../../registry/authored-skills-index.json) with current source path, SPDX license expression, copyright holder, license evidence path, exact `SKILL.md` Git blob SHA, complete package tree SHA, provenance/verification links, and review/test status.
3. For the original first-party content, the repository root [MIT license](../../LICENSE) is the **current default**. This permits proprietary uses and commercial redistribution subject to required notice retention. It does **not** guarantee free-of-charge availability or that derivatives remain open source.
4. If a new skill should use **GPL-3.0** or **AGPL-3.0**, choose it explicitly *before publication*, include the complete applicable legal text and clear per-package `SPDX-License-Identifier` scope. Do not infer copyleft from author intentions or silently relicense third-party materials. AGPL's network-source clause primarily targets qualifying modified network software, not automatically every remotely used Markdown prompt.
5. Record third-party references separately with exact source pin, original publisher, actual rights and attribution. A root LICENSE file is evidence, but nested and bundled material may carry other restrictions. **Unknown rights => do not import.**
6. Keep static semantic review, external scanner evidence, host behavioral tests, permission/authority, and publication clearance as separate fields. A draft package may be statically reviewed with `behavioral_validation: not-run`.

The existing first-party `skills/<slug>/` entries are not automatically moved or relicensed. Move them only as separate, reviewed maintenance work with compatible index/registry updates.

## Current authored package

[Healthcare Contract Forensics](healthcare-contract-forensics/SKILL.md) | [Package record](../../registry/authored-skills-index.json) | [Review and licensing evidence](../../docs/reviews/2026-11-06-issue714-healthcare-contract-forensics-static-review.md).

This remains **draft/behaviorally unvalidated**; being present in this directory is not an instruction to install or process regulated/private data.
