# Governed discovery: Supabase Agent Skills and source-surface checks (2026-10-27)

**State: new candidate source lead, SELECTIVE SOURCE VET / TRACK; no source admission, individual verification, installation or security approval.** This is a passive external-host discovery record, not a repository-owned crawler, scheduler, runtime, scanner or release process.

## Discovery funnel and deduplication

- **Public discovery surfaces inspected (3 families):** current public GitHub skill repositories and repository code search; public web/skills-directory results for recently updated Agent Skills; Hugging Face's current official skills documentation and public `hf-skills` collection. These surfaces overlap, so their search results must not be counted as independent skills.
- **Distinct source families investigated in this pass:** Supabase `supabase/agent-skills` (actual upstream files/trees checked); `SamoTech/skills-tree` (public machine-readable discovery index, not an independently reviewed skill package); `borghei/Claude-Skills` (large creator collection, likely substantial overlapping material, not individually enumerated). GitHub code search within `Knapp-Kevin/skillz` returned **zero matches** for these three canonical strings; this is *preliminary name-level deduplication*, not exhaustive URL/alias/ledger proof.
- **New source lead selected for direct inspection:** **1**. **Exact first-class SKILL.md manifests identified in that source:** **2**. **Admitted skills:** **0**. **Security/behavioral executions:** **0**. No issue opened for speculative admission; the lead remains documented for bounded future source-vetting rather than becoming an unowned holding issue.
- **Date qualification:** GitHub repository revision was read on 2026-10-27; a recently updated repository is not proof its individual skill procedures were newly authored that day. No claim of new skill publication within the last hour is made.

## Supabase: source identity, finite denominator and preliminary authority map

- Canonical repository: [supabase/agent-skills](https://github.com/supabase/agent-skills).
- Observed immutable HEAD: `c9be0e931b7930f7d02126d04774d904c381e7d7`.
- Root README Git blob: `528beca0861b4a42368c87f8190d6fa96df44900`.
- Root MIT license Git blob: `d3c9e94fbc6c28f66ecb5a01407d543c99c811b6`; Copyright (c) 2026 Supabase. Individual file/dependency obligations must still be checked before redistribution.
- Root `skills/` directory has **two** direct package directories. Both package Git trees were fetched with `recursive=1`, **truncated=false**. The `supabase` package tree contains **6** Git entries, exactly **one** `SKILL.md` and one `references/` entry; the `supabase-postgres-best-practices` package tree contains **37** Git entries, exactly **one** `SKILL.md` and **34** reference entries. **Eligible first-class denominator in this observed `skills/` root: 2**, with no nested SKILL.md paths in either package. This is an exact observed root-tree count, not an assessment of releases, mirrors, plugins or historic versions.

| Canonical first-class manifest | Git blob | Full package Git tree | Preliminary disposition |
| --- | --- | --- | --- |
| [`skills/supabase/SKILL.md`](https://github.com/supabase/agent-skills/blob/c9be0e931b7930f7d02126d04774d904c381e7d7/skills/supabase/SKILL.md) | `66093e0a0f8d9268094c1a4b38c04419b787ca89` | `57b975708a53ce7a56df25822871b71da6d9312a` | **ADAPT/EXTRACT candidate**, high-authority database operations and identity/RLS surface |
| [`skills/supabase-postgres-best-practices/SKILL.md`](https://github.com/supabase/agent-skills/blob/c9be0e931b7930f7d02126d04774d904c381e7d7/skills/supabase-postgres-best-practices/SKILL.md) | `6400792389dfcc82c81953054e546bd72ebcd259` | `27bde25111c4cd5e6f803fc9db5fbffe27bb26cf` | **SELECTIVE VET**, structured Postgres query/index/RLS rules with 34 reference entries; no blanket unchanged-use approval |

### Macro characterization

**Positive differentiation:** The broad `supabase` skill explicitly addresses Supabase-specific RLS, stale JWT claims, service-role exposure, `SECURITY DEFINER`, `anon` vs `authenticated` access, scoped management tokens, CLI/MCP version constraints and migration-history pitfalls. The Postgres package offers prioritized performance, connection, RLS and schema guidance. These are potentially valuable technical safeguards beyond generic database prompts.

**Hard-boundary concerns:** The broad skill directs hosts to run SQL through MCP `execute_sql` or CLI `supabase db query` and describes public-role grants, migrations, schema changes and authentication. Its correctness warnings do **not** establish an action-specific grant to change a user's database, production RLS, identity, credentials, exposed tables or public access. The Postgres skill triggers even for one-column changes, so a later full review must distinguish reference-only SQL design from executing it. Do not install, execute, connect to a real project, reveal scoped tokens or infer permission from tool availability.

**Dependency and privacy map:** Supabase CLI, MCP/OAuth, Postgres, hosted Supabase services, user/customer database rows, RLS policies, tokens, Edge Functions and project logs. Exact version compatibility, referenced SQL samples, secrets handling and any remote telemetry require scrutiny. The source's own `scripts/`, `test/`, `.github/` and release tooling remain upstream-owned; they are not `skillz` runtime.

**Overlap:** Existing corpus already includes database/cloud/security/repository and developer workflows. Source selection should reward distinct Supabase RLS and migration-failure mechanisms rather than another generic SQL wrapper. The full 34 Postgres reference entries have **not** been individually read in this discovery pass, so neither package is promoted to `verified` or `validated`.

## Discovery-surface-only leads

- [SamoTech/skills-tree](https://github.com/SamoTech/skills-tree): an actively maintained capability/skill graph with large claimed batches. Treat generated registry entries as discovery pointers, not 50 newly verified packages per batch.
- [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills): broad collection with creator claims of hundreds of skills and generated manifests. Source-family overlap and canonical package identity must be resolved before any admission.
- [Hugging Face Skills](https://huggingface.co/docs/hub/agents-skills): already a known official discovery ecosystem; no new canonical source identity admitted here.

## Decision and next bounded step

**Decision for this cycle: TRACK / SELECTIVE VET, not ADMIT.** The source's two first-class identities are now established, but their full semantic, reference-level, privacy, license/dependency and security qualification is not complete. If selected for admission, open one bounded candidate issue, reconcile both packages and their reference trees, make a terminal ADMIT/ADAPT/EXTRACT/REFERENCE-ONLY/REJECT decision, then close that issue. Do not create a permanent source-vetting backlog item without a completion owner.

**Flow:** public discovery surfaces **3 families**, directly inspected canonical new source leads **1**, first-class manifests identified **2**, new source identities admitted **0**, governed verification companions **0**, security passes **0**, behavioral validations **0**, public accounting delta **0**.
