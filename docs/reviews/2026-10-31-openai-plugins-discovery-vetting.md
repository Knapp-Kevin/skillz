# OpenAI Plugins: official dynamic-discovery source vetting (2026-10-31)

## Decision

**ADMIT as a dynamic-discovery/reference surface only.** Do not admit, vendor, install, execute, or blanket-verify the constituent plugins or skills. This is one source-level vetting decision under [issue #554](https://github.com/Knapp-Kevin/skillz/issues/554), not 536 skill admissions. Source registration increases from **22 to 23**; pinned corpora remain **12**, third-party semantic companions remain **995** (874 registered/tracked + 121 candidate-only), first-party remain **44**, and total exact-version pairs remain **1,039**. No admitted-source denominator changes.

## Exact observed source identity

- Canonical: https://github.com/openai/plugins, maintained by OpenAI; observed main commit/tree **`0722921d5542fc593105c27bd52630babd8b8c2a`** on 2026-10-31.
- Its [README](https://github.com/openai/plugins/blob/main/README.md) identifies a curated collection of Codex plugin examples with per-plugin `.codex-plugin/plugin.json` manifests, optional `skills/`, MCP, app, agent, hook, and asset components.
- The prior [openai/skills README](https://github.com/openai/skills/blob/main/README.md) explicitly declares that catalog **deprecated** and directs readers to `openai/plugins`. Do not promote the deprecated repository as a fresh source.
- The complete non-truncated recursive tree at this revision contains **7,775 entries**, **536 raw `SKILL.md` paths** (535 under `plugins/`, one under `.agents/skills/plugin-creator/`), **64 `.codex-plugin/plugin.json` manifests**, **65 default marketplace entries**, and **zero symlinks**. These are exposure counts, not unique canonical skill identities or an eligible static-review denominator. Marketplace entries may include non-skill plugins, and plugins may contain many first-class or nested skills. No denominator is claimed until bounded individual source/package vetting resolves these distinctions.

## Source terms and provenance

There is no repository-root LICENSE. Individual plugins declare materially different terms, including `codex-security` **Proprietary**, `openai-developers` **Proprietary**, `figma` **LicenseRef-Figma-Developer-Terms**, `cloudflare` **MIT**, and `superpowers` **MIT**. Some package files carry separate LICENSE/NOTICE texts. Register source-level license as **MIXED/per-plugin**, not MIT or OpenAI-wide permissive. No restricted content is vendored. A discovery link grants no redistribution, installation, security, or execution authority.

## Macro map and value

- **Overlap/duplicate exposure:** Cloudflare and Vercel deployment guidance, Figma/Notion workflows, security reviews, and Superpowers-style development methods overlap registered pinned/tracked families or common mechanisms. Before individual intake, check the existing exact-version records and canonical package identities.
- **Differentiated opportunities:** ChatGPT app submission and tool-annotation review, Codex plugin authoring, native iOS/macOS workflows, specialized visualization, provider-specific integration patterns, and source-specific safeguards. The example `plugins/openai-developers/skills/chatgpt-app-submission/SKILL.md` explicitly checks MCP tool side effects and annotations, but also proposes writing submission JSON. It is **unreviewed**, not a reuse recommendation.
- **Authority risks:** Plugin manifests can advertise MCP, app, hooks, credentials, or interactive write capabilities. Review access to private repositories and cross-organization data, external disclosure, cloud deployment, DNS, money-bearing APIs, user communication, security configuration, identity, and destructive changes with independent action-specific authorization.
- **Privacy risks:** Credential-bearing MCP configuration, private source files, documents, customer communications, location/health/identity data, and provider telemetry require scoped source and disclosure authority. Source content is untrusted reference material, not an instruction to install or connect anything.
- **Freshness:** Dynamic discovery means future host-initiated checks may evaluate a new exact revision; this observed SHA is a reproducible snapshot, not an automatic moving pin or authorization for scheduled monitoring.

## Lifecycle and exclusions

The source-vetting result is **dynamic-discovery**, not a pinned-reference or tracked admitted skill corpus. Individual candidates must use issue-first intake, license/identity vetting, exact-version semantic review, applicable package-security evidence, and independent external behavioral evidence before any unchanged-use decision. No new skill provenance/verification records, tests, scripts, CI, generators, schedulers, scanners, or repository-owned runtime are introduced. Existing five draft PRs #489, #492, #496, #412, #413 remain separate qualification-held lanes; this source-vetting tranche touches none of their SKILL.md or shared registry paths.

**Next action for this source:** Only select a bounded differentiated plugin or skill if a concrete user-fit/capability gap justifies it, and vet that exact package and terms. Do not launch a 536-package blanket curation campaign based on popularity or official branding.
