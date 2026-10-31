# Cloudflare Skills: telemetry and staging deployment authority macro review

**Date:** 2026-10-30  
**Registered source:** `cloudflare/skills` at `f96bff754e428838818017f75817f0f9428acd48` (Apache-2.0).  
**Scope:** 13 first-class pinned packages, 13 existing verification/provenance pairs, zero missing static identities. Risk-map all 13; deep-inspect two previously verified procedures and the Workers bundled rules/review references. Static-only: no package mutation, execution, scanner, behavioral acceptance, source pin movement or new admission.

## Exact family map

The pinned `skills/` source tree exposes **13 first-class directories**, each with its own `SKILL.md`. There are no separately counted nested first-class skills, aliases or mirrored duplicates in this family. Bundled `references/` and source-owned scripts are dependencies, not additional skill identities or repository-owned runtime.

| Risk cluster | Canonical packages | Current disposition |
|---|---|---|
| Agent and broad platform routing | `agents-sdk`, `cloudflare` | VERIFIED semantic only, retained |
| Stateful application design | `durable-objects` | VERIFIED semantic only, retained |
| Sandbox SDK version lines | `sandbox-next`, `sandbox-stable` | VERIFIED semantic only, retained |
| Guarded Turnstile setup | `turnstile-spin` | VERIFIED semantic only, retained; explicit user waits for consequential actions |
| Workers code review and logging | `workers-best-practices` | **VERIFIED 18/20 → REJECT unchanged 14/20** |
| Stable-to-preview deployment | `sandbox-migrate-to-next` | **VERIFIED 20/20 → REJECT unchanged 16/20** |
| Email and account/domain effects | `cloudflare-email-service` | REJECT unchanged, retained |
| Identity/network policy migration | `cloudflare-one-migrations`, `cloudflare-one` | REJECT unchanged, retained |
| Browser/telemetry tool bootstrap | `web-perf` | REJECT unchanged, retained |
| General cloud CLI mutations | `wrangler` | REJECT unchanged, retained |

**Before:** 8 VERIFIED semantic only / 5 REJECT unchanged. **After:** 6 VERIFIED semantic only / 7 REJECT unchanged. Static coverage **13/13**, zero gaps, denominator delta **0**.

## Exact-version escalations

**`workers-best-practices`.** Package tree `7dd384e79c76d3e388dfe53e12e93642679ff1fd`; SKILL.md Git blob `bebd018cdcae1771eacdee30cfb96af3ad3bd936`; bundled `references/rules.md` blob `2ac2df70f696ae585063b305adfe582b220f6011`, `references/review.md` blob `24c70e02ea9d4c718ae276a9f796afe74fb6b33a`. The parent quick-reference says to enable `observability`; the bundled rules specifically instruct enabling Workers Logs and Traces before production, sample logs at `head_sampling_rate: 1`, and illustrate logging request method/path. The parent review workflow checks observability configuration. There is no action-specific gate for telemetry activation, sensitive fields, sampling, cost, retention, or the exact target account/environment. Reviewing Worker code or requesting a code fix does not authorize sending additional production request data into a logging service. Secret-setting guidance similarly needs an independent credential/configuration mutation boundary. Preserve source retrieval, streaming, type safety, crypto, anti-patterns and review methods for scoped adaptation.

**`sandbox-migrate-to-next`.** Package tree `6653491197cd99b53582df12eca6b51dcf1e60a1`; SKILL.md blob `745bcc5655dec3b690d6df4c31141a2b46a6d4c3`. The runbook commendably stops for a user decision before production cutover and accurately warns that immediate rollout interrupts in-flight work. But the `Deploy cutover` phase says staging/branch first without separately authorizing staging environment, account or deployment; the validation checklist includes `Production used --containers-rollout=immediate` even for a code-only port. A production-cutover question cannot authorize an independent staging deployment, and permission to port code does not imply permission to deploy. Preserve package/image parity, API migration, process lifecycle, secrets, anti-invention and smoke-validation methods for adapted use. A scoped adaptation must distinguish code-only, staging and production, obtaining separate approval for each external effect.

## Macro synthesis

The family has high-value retrieval-first product-specific guidance, and the narrower Sandbox stable/preview and Turnstile procedures include meaningful safeguards. The recurring defect is **operational escalation hidden in otherwise excellent technical guidance**: enabling telemetry is a privacy/retention/cost decision, and staging deployments are external persistent effects, not merely a harmless validation step. Strong implementation quality or even a 20/20 historical rubric score cannot override an authorization hard fail.

Do not convert source-owned Cloudflare scripts, examples or reference files into `skillz` runtime. Neither correction changes upstream bytes or retroactively changes package-security/behavioral evidence. Both corrected packages remain useful for ADAPT/EXTRACT/CHECKLIST rather than unchanged adoption.

## Lifecycle and accounting

Two existing exact-version verification records and two provenance records refreshed. **0** new skill identities, **0** source admissions, **0** denominator delta, **0** security scans, **0** executed behavioral tests. Both corrected validation states remain `not-run`. Public totals remain **44 first-party / 867 third-party / 911 total**. All five public surfaces are reconciled in the same tranche. The 36 changed first-party package trees in draft PRs #489/#492/#496 remain separately blocked on pinned external SkillSpector v2.12.0 full reports and independent adversarial acceptance; admission drafts #412/#413 remain on hold. No existing open issue or draft PR was eligible for closure/merge from this static source-family recheck.
