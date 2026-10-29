# Project Concept

## Purpose

Make reusable AI-agent skills easy to discover, compare, and adapt without forcing people to become skill-library experts. Help an **external host agent** build or refine the smallest useful skill system for a user from legitimate context and governed reference evidence.

`skillz` is **an entirely passive knowledge resource**, not an application, agent runtime, or installer. It stores first-party skills, pinned upstream corpora, source context, standards, procedures, safeguards, rejected examples, provenance, exact-version review evidence, controlled tags, and static catalog snapshots. The host performs every active operation using its own authorized capabilities.

## Two ways to use the resource

1. **Direct library:** A person or agent browses, searches, compares, or inspects a named skill or capability. No bootstrap interview is required.
2. **Host-guided first visit or return:** The host follows [AGENT_START_HERE](../AGENT_START_HERE.md) and the passive [skill-bootstrap procedure](../engine/skills/skill-bootstrap/SKILL.md) to compare available knowledge against user needs, then creates or hands off a fitted result **outside this repository**.

A returning visit may correctly conclude `NO CHANGE NEEDED`. No persistent memory, scheduling, installation, or connector access is implied by reading the corpus.

## Destination and authority boundary

Normal use routes `DIRECT_LIBRARY`, `FIRST_VISIT`, and `RETURNING_USER` to **read-only repository access**. Skills created, adapted, composed, refined, or installed for a user belong in the user's authorized host environment or a portable handoff, not in `skillz`.

Only an explicit `REPOSITORY_MAINTENANCE` instruction authorizes governed changes to this repository. Access to a writable tool is not consent. Private-context reads, credential access, external communications, scheduling, persistent state changes, production operations, and other consequential side effects require their own appropriate action-specific authority.

The repository owns **no runtime, scripts, tests, CI workflows, schedulers, monitors, crawlers, installers, synchronizers, preflight processes, generators, background services, vector databases, autonomous observers, or personalization services**. Authorized external hosts may perform reviews, package-security assessments, and behavioral exercises and deposit truthful exact-version evidence. Source-authored tools bundled inside pinned upstream packages remain intact reference material, not repository-owned machinery.

## Physical and evidence surfaces

- `skills/`: maintained first-party user-facing skill knowledge, **not** a normal destination for host-generated user skills.
- `skills/sources/<source-id>/`: intact pinned third-party reference corpora, with upstream dependencies and attribution preserved.
- `engine/skills/`: passive bootstrap and repository-maintenance instructions, excluded from user-facing inventory.
- `registry/sources.yaml` and `registry/skills/`: source identity, license/terms, exact pins, and per-skill provenance.
- `registry/verification/` and `registry/local-verification.json`: individual exact-version semantic-review evidence.
- `registry/security/` and `docs/security-scanning.md`: separate package-security state and host-executed assessment evidence.
- `INDEX.md` and `index.json`: **hand-maintained static catalog snapshots**, not generated outputs or execution prerequisites.

See [README](../README.md), [GOVERNANCE_INDEX](GOVERNANCE_INDEX.md), [SYSTEM_STATE](SYSTEM_STATE.md), and [CURATION_QUEUE](../CURATION_QUEUE.md) for current authority and accounting. Historical execution-era artifacts are not active architecture.

## Selection and quality principles

**Compare before creation. User fit before reuse. Smallest coherent system over maximum skill count.**

Evaluate user fit, exact-version quality, operational fit, skill freshness, and provenance/source context in that order. Possible host decisions include ADOPT, ADAPT, EXTRACT, SUPPLEMENT, COMPOSE, CREATE, CHECKLIST, DYNAMIC behavior, and NO CHANGE. A rejected or reference-only package may still provide bounded useful design evidence, without inheriting approval for unchanged use.

Availability, creator reputation, and source admission do not establish individual quality. `verified` means structured exact-version semantic review; `validated` additionally requires **actually executed representative external behavioral/adversarial evidence** bound to the exact package. Applicable unchanged third-party reuse also requires acceptable **separate** package-security evidence, provenance, licensing, dependencies, authority, portability, and actual user fit. No static scenario plan or green status is a behavioral or security pass.

## Success criteria

A useful `skillz` experience means:

1. A host can find relevant knowledge with no repository runtime or installation prerequisite.
2. The host can distinguish governed exact-version evidence from broad unverified reference material.
3. The host can select, adapt, compose, create, or decline a skill based on actual user needs.
4. User-derived artifacts go to the authorized user environment or a complete portable handoff.
5. Side effects and sensitive-data access remain separately authorized, with missing capabilities disclosed.
6. A returning user can preserve a working system without needless changes.
7. Source identity, licensing, freshness, static semantics, security state, and observed behavior remain separately auditable.
8. Repository maintainers can curate sources and close lifecycle debt without adding active machinery to `skillz`.

Current source-family progress and blockers are recorded in [CURATION_QUEUE](../CURATION_QUEUE.md), not inferred from the age of this concept document.
