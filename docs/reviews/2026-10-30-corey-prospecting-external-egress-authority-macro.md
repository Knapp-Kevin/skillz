# Corey Haines prospecting external-egress authority macro (2026-10-30)

## Exact source and scope

Registered tracked corpus: `corey-haines-marketing-skills`, MIT, Corey Haines, pin `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`. Independent directory readback returned **50** top-level first-class `skills/<name>/SKILL.md` packages, with **50** existing exact-version verification companions and no genuine static gaps. No source pin or package was changed. Nested references and `tools/` integrations are dependencies, not independent skill denominator entries.

A risk-screen of **16** current pinned packages covered `cold-email`, `emails`, `directory-submissions`, `events`, `influencer-marketing`, `co-marketing`, `community-marketing`, `referrals`, `launch`, `public-relations`, `prospecting`, `paywalls`, `seo-audit`, `sales-enablement`, `schema`, and `site-architecture`. Eleven initial records were inspected for communication/data-use risks, and five additional previously VERIFIED advisory/SEO/design records were screened for overlap. **One** was escalated for deep package/reference review and corrected. **Fifteen** prior dispositions remain unchanged (ten rejected, five verified); these were a risk screen, not a claim of fresh full-depth semantic re-verification for every retained package.

## Decisive exact-version correction

`prospecting`: **VERIFIED semantic only 17/20 → REJECT unchanged 14/20**.

- Manifest: `skills/prospecting/SKILL.md`, Git blob `472435c76bb7c0e03d620b9412994ec016615e42`.
- Exact package tree: `90018c683343a850a78defd09387b6035228098f`, independently read back with the manifest, `references/`, and `evals/` trees. Source revision: `5b2c0007766c6a1cf1d53fd8fc73e979e0821022`.
- Phase 3 says to **always verify deliverability** before including B2B/SaaS contacts; `references/data-sources.md` prescribes Truelist or similar validation and paid providers. The upstream `tools/integrations/truelist.md` documents inline and bulk API requests, CSV uploads, and a pay-per-email model. It sends identity-bearing email addresses to an external service, including an inline endpoint with `email=` in the URL query. Neither selecting a provider nor possessing an API credential establishes approval for the particular data disclosure, recipient, cost, retention, or sensitive-log exposure.
- The optional Truelist account endpoint can return API keys; this is a potential secret-output surface, not evidence of actual exposure. Provider enrichment, stargazer-to-company identity mapping, and CSV lead-sheet persistence likewise require scoped data handling and retention decisions.
- Existing protections remain meaningful: public business channels, no bulk platform scraping, no bypass, no sensitive-trait targeting, provenance/recency and confidence labels, no automatic outreach in the demand-signal branch, and a separate `cold-email` handoff. Preserve as ADAPT/EXTRACT/CHECKLIST material rather than discarding the package.
- Exact manifest/package identities and source-owned tools remain unchanged. **Behavioral validation: not-run.** No new scanner report, external API request, upload, credential read, or behavioral execution is claimed.

## Macro synthesis

The source is stronger as strategy, research, and reusable checklist material than as an autonomous operational mandate. The main systemic hazard is **advisory-to-action escalation through bundled tool references**: a seemingly read-only research procedure can require paid third-party verification, transmit contact data, or persist a prospect list. Existing rejected communication/event/launch packages already reflect separate send, publication, and spend boundaries. The five retained VERIFIED design/SEO/advisory records were not reclassified on this evidence; their context-file read assumptions should be revisited if an independently demonstrated private-scope or disclosure defect emerges.

Source family **50/50 static-reviewed, zero gaps → 50/50, zero gaps**; one existing record corrected, no denominator delta, no new admissions or discovery decisions. Public inventory **44 first-party / 848 third-party exact-version reviews / 892 total verification** remains unchanged. The five public accounting surfaces were reconciled as one tranche.

## Lifecycle and next action

The existing draft PRs #489 (29 changed first-party trees), #492 (5), #496 (2), #412 and #413 remain outside this disjoint third-party lane. None has a qualifying new pinned SkillSpector v2.12.0 complete final-tree report and independent executed adversarial acceptance. No merge or issue closure is justified solely by technical mergeability. Next priority: obtain authorized external qualification for the 36 changed first-party trees, reconcile their shared registry, and merge qualifying repairs.

No repository-owned scripts, tests, CI, scheduler, scanner, runtime, or automation were added.
