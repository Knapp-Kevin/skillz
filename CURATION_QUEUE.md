# Skill Curation Queue

This is the living evidence ledger for ongoing `skillz` corpus curation. The repository architecture is core-complete and entirely passive. Curation is performed by the external host agent under explicit repository-maintenance authority.

## Current governed depth

- **43** first-party user-facing skills.
- **43/43** first-party provenance-complete.
- **12** pinned upstream reference corpora under `skills/sources/`.
- **19** unique registered source identities.
- **128** persisted exact-version third-party verification companions.
- Broad **500+** first-party + pinned external reference surface.
- Historical source-level evidence for at least **210 reviewed published/eligible external entry points** across nine completed corpora, plus later AWS and selective-source work.

Historical review evidence and current per-skill companion completeness are different accounting layers. Prior work is evidence to reconcile, not permission to invent missing records or to redo trustworthy work from scratch.

## Curation and admission model

**discovery surface → candidate issue/source → source-vetting → exact-version static evaluation → decisive admission result → repository persistence when justified → user-fit decision**

New third-party discoveries use the issue-first workflow in `docs/candidate-intake.md`. Intentional discovery inputs are documented in `docs/discovery-surfaces.md`, including the connected Creator Technical Resource Catalog. Discovery intelligence never substitutes for canonical upstream provenance, exact identity, license/terms, or individual quality evidence.

Every governed user-facing skill must retain truthful provenance and exact-version evidence appropriate to its relationship. Missing provenance is a corpus-completeness defect.

## Mandatory provenance status

Issue #66 is the corpus-wide provenance-completeness audit.

- First-party denominator: **43**.
- First-party structured semantic reviews: **43/43**.
- First-party standalone provenance companions: **43/43** under `registry/skills/local-skills/`.
- No repository-owned scanner, script, CI gate, or runtime enforces this. The external host agent checks and records the contract during curation.

## Completed historical source-level review evidence

| Source | Historical reviewed denominator | Recorded result/state |
|---|---:|---|
| Anthropic Skills | 17 / 17 | 10 verified, 7 rejected |
| Anthropic Knowledge Work Plugins | 74 / 74 | 36 verified, 38 rejected unchanged |
| Matt Pocock Skills | 29 / 29 | Complete |
| OpenHands Extensions | 1 / 1 | `theme-factory` rejected unchanged |
| Vercel Agent Skills | 9 / 9 | 6 verified, 3 rejected |
| Cloudflare Skills | 13 / 13 | 11 verified, 2 rejected |
| Google Agents CLI | 7 / 7 | All verified |
| Cline Skills | 36 / 36 | 19 verified, 17 rejected unchanged, plus one separately characterized internal/unlisted skill |
| Addy Osmani Agent Skills | 24 / 24 | Complete with decisive exact-version static states |

These **210** published/eligible entry points remain evidence even where the newer one-file companion representation is not yet one-for-one complete. Search and reconcile prior evidence before re-reviewing.

## Active admitted-source curation

### AWS Agent Toolkit

- Registered pin: `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`.
- Eligible denominator: **72** skills, historically recorded as 14 core + 58 specialized.
- Historical inspection: **72/72**.
- Prior full-pass disposition: **70 verified / 2 rejected**.
- Current-standard provenance + verification companion completeness: **28/72**.
- Remaining current-standard gaps: **44**.

Latest sequential batch closed seven genuine companion gaps after confirming each pair was absent:

| Skill | Exact package tree | Current state | Score | Authority | Portability |
|---|---|---|---:|---|---|
| `managing-amazon-msk` | `b16afcc92da29d85d0e610d38a1c49b20e5e32e8` | verified | 16/20 | mutating | low |
| `migrate-to-msk` | `a4e9b51d24f59d5bfc0bbb7bf234a2d096163911` | verified | 17/20 | mutating | low |
| `querying-data-lake` | `a619aa25a608b7efac3d5439b1e9c5a0d303defc` | verified | 18/20 | mutating | low |
| `amazon-aurora-mysql` | `0e3f93d02d0bff4d76ae31f425527441989717e1` | verified | 18/20 | mutating | low |
| `amazon-aurora-postgresql` | `eb9414ad02354efaa482cb24003af763030ec00d` | verified | 18/20 | mutating | low |
| `amazon-documentdb` | `4fc95aee114b9b6911dcdfc1d41a9715c3df4e62` | verified | 16/20 | mutating | low |
| `amazon-elasticache` | `7ab33b79df92988e90fe25e9318fe748c7d15149` | verified | 17/20 | mutating | low |

Behavioral evidence is `not-run` for this static batch. Upstream scripts, assets, references, and templates remain intact package dependencies rather than `skillz` execution machinery.

**AWS continuation rule:** work sequentially and repeatedly until 72/72 current-standard completeness. Before every unit, check both companion paths and recoverable historical evidence. Create or refresh records only for a genuine current-standard gap or identity/evidence delta.

### Microsoft Skills

- Pin: `32cad4ee689c95c309e61aeefcbc6af356f1e6a7`.
- Full source review remains pending after AWS current-standard closure.
- Favor differentiated Microsoft/M365/Foundry/developer-platform mechanisms rather than official-brand duplication.

### Microsoft Azure Skills

- Pin: `8f8c72bb9e22aee4366e07aadfd5766ef9add8f4`.
- Full source review remains pending after Microsoft Skills.
- Distinguish planning/read-only guidance from deployment, RBAC, cost, identity, and other higher-authority operations.

### Other admitted/tracked sources

- **Cole Medin Skills**: pin `fb2e876f057c5356d6603ba0c52d6b4418d893ba`; denominator 33; selective reviews include `second-brain-audit`, `rules-check-drift`, `ablate-ai-layer`.
- **David Ondrej Skills**: public pin `7d0ef87dad1f638cab58995eead9e0e6e3fae237`; current evidence describes 44 canonical `SKILL.md` files while a historical tracker recorded 55. Reconcile denominator before completion claims.
- **OpenClaw Agent Skills**: pin `6cd3366b10e2a8c5608265f692acf9f5da2b2448`; denominator 8; selective `handoff` review exists.
- **Archie Indian OpenClaw Superpowers**: pin `a95a59d221d44b89d4fc27a52934e24fb2060ddb`; denominator 56; selective `secrets-hygiene` review exists.
- **Sabrina Ramonov Learn Claude Code Skills**: historical denominator 2, but canonical source identity/pin/license must be recovered before further work.

## Evidence-reconciliation lane after AWS

Historically completed corpora with broader prior review evidence than their current one-file companion shelf should be reconciled without automatic re-review. High-value targets include Anthropic Knowledge Work Plugins, Cline, Addy Osmani, and any completed Vercel/Cloudflare/Google/Matt records not represented one-for-one today.

## Discovery/source-vetting frontier

Discovery proceeds in parallel but does not interrupt admitted-source completion merely to increase issue counts.

Current useful surfaces/candidates include:

- Hugging Face Skills, previously source-vetted for selective intake at recorded snapshot `cead19e10754e773bad24fecef83cb64be24094e`;
- Selamy Labs Agent Skills;
- Hypergiant Agent Skills;
- BCGov Agent Skills;
- GitHub Awesome Copilot as registered dynamic discovery;
- Agent Skills Specification as normative format/portability reference;
- Creator Technical Resource Catalog in connected Google Drive as internal governed discovery intelligence;
- candidate evaluation issues #62 through #65.

New discoveries are queued as issues before admission. Restricted or unclear-license material remains reference-only unless terms later support a different relationship.

## Working rules

1. **Finish the admitted corpus.** Sequential curation is the default until current-standard gaps are closed.
2. **Do not lower the bar for throughput.** Every unit still gets duplication checking, exact identity, provenance, license/terms, package/dependency context, authority, portability, freshness, controlled tags, decisive static state, and explicit behavioral-evidence status.
3. **Search before re-reviewing.** Recover compatible prior evidence first.
4. **Do not erase negative evidence.** Rejection and retirement reasons prevent repeated mistakes.
5. **Preserve complete packages.** Upstream scripts/references/assets/templates remain package context, not repository runtime.
6. **Keep discovery separate from admission.** Popularity and catalog reputation are context, never proof.
7. **Keep `skillz` passive.** No repository-owned runtime, scripts, tests, CI, scheduler, monitor, crawler, installer, synchronizer, preflight, generator, background service, vector database, or autonomous observer.
8. **Keep public accounting synchronized.** README, System State, this ledger, `INDEX.md`, and `index.json` must agree after each material batch.

## Current posture

**Core:** complete and passive.

**First-party:** 43/43 provenance-complete.

**AWS:** 72/72 historically inspected; 28/72 current-standard companion-complete; 44 gaps remain.

**Next:** continue the AWS database-family gap scan and curation sequentially, then proceed through the remaining AWS specialized families until current-standard AWS closure is 72/72.
