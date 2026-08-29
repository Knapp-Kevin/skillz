# Feature Index

Maps current `skillz` capabilities to their passive repository surfaces.

`skillz` itself executes nothing. A capability here means the repository gives an external agent enough instructions/evidence to perform the method using capabilities supplied by its host.

| ID | Capability | Passive surface | Current state |
|---|---|---|---|
| FX01 | Human/agent repository front door | `README.md` | CURRENT |
| FX02 | Explicit passive-agent entry contract | `AGENT_START_HERE.md`, `AGENTS.md` | CURRENT |
| FX03 | First-visit discovery/bootstrap method | `BOOTSTRAP.md`, `engine/skills/skill-bootstrap/SKILL.md` | CURRENT |
| FX04 | Returning-user minimal refinement / no-change method | `BOOTSTRAP.md`, `AGENTS.md` | CURRENT |
| FX05 | Direct library use without forced bootstrap | `README.md`, `AGENTS.md`, `skills/` | CURRENT |
| FX06 | Unified user-facing skill tree | `skills/`, `skills/sources/` | MIGRATION ACTIVE ON PR #42 |
| FX07 | Maintenance instructions excluded from corpus counts | `engine/skills/`, `engine/README.md` | CURRENT |
| FX08 | Human browse-by-purpose categories | `skills/categories/`, `registry/categories.yaml` | CURRENT; continue reconciliation as corpus evolves |
| FX09 | Source identity, role, pin, and license | `registry/sources.yaml` | CURRENT |
| FX10 | Per-skill provenance companions | `registry/skills/`, `docs/companion-metadata.md` | ACTIVE CURATION |
| FX11 | Exact-version static quality state and tags | `registry/verification/`, `registry/taxonomy.yaml` | ACTIVE CURATION |
| FX12 | Source-level visibility/maintenance context | `registry/source-signals.yaml` | ACTIVE; contextual only |
| FX13 | Structured static review method | `docs/skill-verification.md`, `engine/skills/skill-audit/SKILL.md` | CURRENT METHOD; corpus coverage incomplete |
| FX14 | Source/candidate vetting | `engine/skills/source-vetting/SKILL.md` | CURRENT |
| FX15 | Limited ecosystem discovery | `engine/skills/skills-pulse/SKILL.md` | CURRENT; on-demand external research only |
| FX16 | Custom/adapted skill authoring guidance | `engine/skills/skill-forge/SKILL.md` | CURRENT; passive instruction |
| FX17 | Behavioral evaluation guidance | `engine/skills/skill-eval/SKILL.md`, `docs/evaluation-framework.md` | METHOD EXISTS; external evidence only |
| FX18 | Skill transfer/install handoff guidance | `engine/skills/skill-sync/SKILL.md`, `docs/installation-handoff.md` | METHOD EXISTS; external host action only |
| FX19 | Portable fitted-skill profile | `docs/portable-skill-profile.md` | CURRENT |
| FX20 | Human-readable reviewed shelf | `CURATED.md` | ACTIVE RECONCILIATION |
| FX21 | Human/machine catalog snapshots | `INDEX.md`, `index.json` | STALE/RECONCILIATION PENDING; passive snapshots only |
| FX22 | Third-party attribution/license boundary | `THIRD_PARTY_NOTICES.md`, `docs/third-party-provenance.md` | CURRENT; maintain per source/skill |
| FX23 | Source freshness review guidance | `docs/vendor-freshness.md`, registry companions | CURRENT CONCEPT; old filename retained historically |
| FX24 | Wayfinder planning discipline for corpus refinement | GitHub Issue #35 + pinned Wayfinder reference skill | ACTIVE |
| FX25 | Static-completion contract | Wayfinder decision #37 + curation docs | CURRENT |
| FX26 | Companion metadata interpretation contract | Wayfinder decision #36 + `docs/companion-metadata.md` | CURRENT |
| FX27 | Entirely passive repository invariant | README/AGENT_START_HERE/AGENTS/Architecture/Governance | CURRENT; executable scaffolding removed on PR #42 |

## Current proof language

Use evidence-specific language instead of old runtime/test labels:

- **DOCUMENTED**: the passive instruction/policy exists and is current.
- **RECONCILED**: relevant static files and companions agree for the stated scope.
- **VERIFIED**: an exact skill version passed the structured static review standard.
- **VALIDATED**: representative external behavioral evidence exists.
- **INCOMPLETE**: denominator or evidence coverage is not complete.
- **STALE**: prior evidence no longer matches current content/assumptions.

Do not use “runtime pending,” “CI pass,” “preflight pass,” or similar repository-execution states as current `skillz` capability gates.

## Current frontier

The useful work is now corpus work:

1. finish PR #42 passive architecture/path/catalog reconciliation;
2. establish full denominators for partially characterized sources;
3. review untouched registered sources;
4. give every eligible skill decisive static provenance/quality/tag state;
5. reconcile passive catalogs/counts;
6. only after static completion, prioritize consequential skills for external behavioral validation.

Historical feature IDs or proof systems tied to removed scripts/tests/CI remain recoverable in Git history but are not current architecture.
