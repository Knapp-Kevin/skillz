# Cloudflare pinned authority and privacy reclassification (2026-10-29)

## Scope and exact-version macro map

- Registered source: `cloudflare/skills`, Apache-2.0, pinned at `f96bff754e428838818017f75817f0f9428acd48` under `skills/sources/cloudflare-skills/`.
- Recomputed eligible denominator: **13 distinct first-class pinned `skills/*/SKILL.md` entry points**, with 13 provenance and 13 verification companions. All 13 recorded manifest Git-blob SHA-1 identities matched the upstream pinned Git tree; no missing current-standard companion or duplicate exposure path was found in this bounded family.
- Pre-tranche: **11 VERIFIED semantic only / 2 REJECT unchanged**. Post-tranche: **8 VERIFIED semantic only / 5 REJECT unchanged**, 13/13 current-standard complete, zero static gaps.
- High-authority cluster: Cloudflare One security/identity/routing policies, migrations, and Email Service configuration/communications. Other clusters: three Sandbox stable/next/migration references, Turnstile setup, Wrangler CLI, browser performance telemetry, and Cloudflare/Agents/Workers/Durable Objects engineering guidance. Shared dependencies are the pinned Cloudflare reference tree, current Cloudflare docs and APIs, and host-provided account/toolchain authority.
- Three consequential packages were deeply re-reviewed; ten unchanged decisions were screened for this specific family-level authority pattern, **not** revalidated or freshly security-scanned. The source package content, source pin, licensing, source-owned scripts and reference dependencies remain intact.

## Three exact pinned decisions

| Package | SKILL.md Git blob | Previous | Current | Static score |
|---|---|---|---|---|
| `cloudflare-email-service` | `fb3565111a2ce94761e5ad6642d20d02e7707946` | VERIFIED | **REJECT unchanged** | 15/20 |
| `cloudflare-one` | `753ab60c176e82f11097caa958cd4646ecd67078` | VERIFIED | **REJECT unchanged** | 16/20 |
| `cloudflare-one-migrations` | `53c770fb2cad0339cccffbc85b68b2b9810dbcb4` | VERIFIED | **REJECT unchanged** | 16/20 |

**Email Service.** The prerequisite step says that if a domain is not onboarded, run `wrangler email sending enable`; the same procedure routes to live sending, inbound routing and address creation. An email-development request, a domain selection, or an available token does not authorize enabling account services, modifying routes, or sending communications to particular recipients with particular content. It also recommends real addresses for testing, increasing the need for an explicit communication boundary. Preserve the binding-versus-REST guidance, retrieval sources, deliverability, transactional-only scope, and credential hygiene.

**Cloudflare One.** The workflow says to inspect Access policies, identity providers, groups, Gateway, DNS, tunnels, DLP and device posture **if account access is available**, without first binding the private read to an authorized account, resources, fields and purpose. It then stages risky policies disabled or in pilots, with approval only for *wider* rollout. A pilot or disabled policy is still a persistent security/routing mutation. Preserve its current-doc retrieval, network topology, policy-order and rollback guidance as proposal-only material pending independent read/write authority.

**Cloudflare One Migrations.** The workflow requests identity, traffic, firewall, TLS and DLP exports/logs without explicit scoped data-access and disclosure approval. Steps 5-6 then direct creation of SCIM/connectors, routes/DNS, Access/Gateway and DLP resources and pilot/audit rules. Source-to-target mapping and a later decommissioning decision do not authorize those initial security, identity and network writes. Preserve source-rule accounting, explicit unmapped/partial dispositions, mapping heuristics, pilot design, rollback and validation gates for governed adaptation.

## Macro synthesis, omissions and boundaries

- **Systemic defect:** platform expertise, retrieval freshness, staging discipline and technical rollback are repeatedly treated as substitutes for **action-specific authority**. They are not. Security/identity configuration, persistent account resources, private inspection and user communications each require separately scoped host authorization.
- **Sensitive-data pattern:** source exports, logs, identity/group data, Gateway/DLP telemetry and email contents can expose private or regulated material. Host access alone does not authorize reading, storing, sharing or transmitting them. Use minimum necessary fields, secure external credential handling, redaction, bounded retention and no secret values in chat.
- **Source-family value:** these three are high-value design/reference packages despite the unchanged-use rejection. Prefer ADAPT, EXTRACT or CHECKLIST with explicit account, target, action, disclosure, rollback, cost, delivery and expiry boundaries. Do not copy their automatic side effects unchanged.
- **Existing rejects retained:** `wrangler` (installation/deploy/delete authority) and `web-perf` (Chrome DevTools MCP browser-data/telemetry disclosure). **Other eight verified decisions retained:** `agents-sdk`, `cloudflare`, `durable-objects`, `sandbox-migrate-to-next`, `sandbox-next`, `sandbox-stable`, `turnstile-spin`, `workers-best-practices`. In particular, `turnstile-spin` contains upstream-owned helper scripts and user confirmation gates; those scripts are not repository-owned runtime. Future targeted review may examine optional observability settings and package installation in other packages, but no unproven reclassification is asserted here.
- No source admission, pin promotion, new source-family denominator, taxonomy tag or package content change. Exact package-tree security scanning and executed adversarial behavior were **not** performed; `validation_status: not-run` remains truthful.

## Atomic public accounting

The five public surfaces (`README.md`, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md`, `index.json`) record Cloudflare **13/13, 8 VERIFIED semantic only, 5 REJECT unchanged, 0 static gaps**. Published inventory stays **44 first-party, 826 third-party exact-version reviews, 870 total verification records**. This is a safety correction to three existing exact-version semantic decisions, not a security pass or behavioral validation.
