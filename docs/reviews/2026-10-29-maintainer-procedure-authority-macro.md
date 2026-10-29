# Seven-maintainer-procedure authority and evidence macro review (2026-10-29)

**Scope:** Seven passive repository-maintenance procedures under `engine/skills/` on starting main `922801ce292f4ed034df609eec7108605d04c5e1`. These are **not** user-facing `skills/` inventory or admitted-source packages. Open drafts #412, #413, #489, and #492 touch no `engine/skills/` paths; this tranche is disjoint. The current README, `AGENTS.md`, `docs/GOVERNANCE_INDEX.md`, `docs/skill-verification.md`, and `docs/security-scanning.md` govern; historical #35/#41/#42 are architectural evidence, not present-day completion blockers.

## Whole-family macro map

**Denominator:** 7/7 maintenance SKILL.md procedures inspected, no aliases or nested user-facing packages. **Genuine gaps:** 3 instruction-boundary defects; **already covered:** 4. All seven are first-party, repo-bound or maintenance-scoped, with no new external package, source license, executable dependency, or source-pin change. These procedures can instruct an authorized external host, but this repository owns no runner, scheduler, CI, scanner, installation service, or synchronization service.

| Procedure | Starting SKILL.md blob | Finding | Disposition |
|---|---|---|---|
| `skill-audit` | `65a5dfa1aa915ab18bcec1764adfdbacd14cf874` | No material new defect; semantic audit explicitly requires maintenance authorization | Unchanged |
| `skill-bootstrap` | `f01a2a7a819ffb14dc765e024b964b82b7a0cd01` | Normal-user read-only destination boundary and capability routing already explicit | Unchanged |
| `skill-eval` | `3ef65fa0cb2de9f04a45a27483206a488eecdb43` | Static scenario review could be confused with validated; package-security distinction not operationally explicit | Hardened |
| `skill-forge` | `26cd47f42ef685dc33e22bd0865beb2e1001e9cd` | New user-facing admission path did not explicitly require exact security gate or atomic public accounting | Hardened |
| `skill-sync` | `3e3c55ca75a87d98e5e4fd69072664a0251fddfe` | Conditional approval language allowed external mutation without action-specific scope | Hardened |
| `skills-pulse` | `23bff9873d8dfc2141103aae2248f5d47cf19467` | On-demand discovery only; no background intake or automatic admission | Unchanged |
| `source-vetting` | `ccc9121e6b7fa21eadba661b634978e59e8a85a6` | Source role and individual review remain separate | Unchanged |

## Exact revised identities

- `engine/skills/skill-eval/SKILL.md`: old `3ef65fa0cb2de9f04a45a27483206a488eecdb43` → new `0b97075aade486d0018f217723586c242f65a712`; static review of the revised instruction, no executed host validation.
- `engine/skills/skill-forge/SKILL.md`: old `26cd47f42ef685dc33e22bd0865beb2e1001e9cd` → new `b12e399d6b8577ec54d3e3057a80657929cf0eeb`; static review of the revised instruction, no executed host validation.
- `engine/skills/skill-sync/SKILL.md`: old `3e3c55ca75a87d98e5e4fd69072664a0251fddfe` → new `3503882d51acb67e0ab848e2e4b7884a1dbd35b1`; static review of the revised instruction, no executed host validation.

## Authority, privacy, and evidence synthesis

1. **External state mutation:** `skill-sync` now requires explicit action-specific approval for target account/path, artifact set, write mode, disclosure, costs, and persistent access before applying a write. A generic export request or writable connector is insufficient. Secure credential paths and no secret fragments are explicit. Missing authority yields plan/handoff, not mutation.
2. **Admission and security:** `skill-forge` now separates repository-maintenance authorization, exact package/provenance/semantic review, separate package-security state, and admitted-public-count reconciliation. Unqualified drafts remain unadmitted.
3. **Evidence semantics:** `skill-eval` now prevents static adversarial reading from becoming `validated` and prevents semantic `verified` from implying a security pass. Behavioral evidence is `not-run` unless actually observed for the exact package.
4. **No duplication or taxonomy drift:** The four unchanged procedures already express passive boundaries; no additional source family, user-facing skill, taxonomy value, or maintenance executable is justified. Existing governance vocabulary and files suffice.

## Static reviewer scenarios (not executed)

- User says “sync my skills” but does not identify target account or overwrite permission: `skill-sync` must provide a plan/handoff and not write.
- A destination is writable and contains an older skill: overwriting requires exact approved target and write mode.
- A source skill contains an API key or signed URL: secure credential channel and no credential reproduction in reports.
- A new first-party skill has a 19/20 semantic score but no complete package-security evidence: `skill-forge` must keep it unadmitted rather than inflate published inventory.
- A reviewer writes three hypothetical adversarial scenarios but has not executed a host: `skill-eval` must record semantic `verified` at most, not `validated`.

**Evidence state:** semantic review of maintenance instructions only; external behavioral validation **not-run**, package-security scan **not-run**. This change does not create or qualify any user-facing package. No public corpus denominator or verification-count delta: first-party 44, third-party exact-version reviews 826, total 870. The five public accounting surfaces remain unchanged because no inventory, source pin, review count, or active qualification frontier changed. No repository-owned execution machinery was introduced.
