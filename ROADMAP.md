# Roadmap

`skillz` is an entirely passive skill corpus and agent-guided discovery protocol. The external agent is the active system.

The roadmap is therefore about **corpus quality, evidence, organization, portability, and usefulness**, not building software to operate the repository.

## Current milestone: production-ready corpus foundation

Status: **ACTIVE CURATION**

The immediate goal is to make the existing corpus coherent, fully attributable, decisively reviewed, well tagged, and easy for an external agent to reason over.

### 1. Complete the unified user-facing tree

- keep every user-facing skill under `skills/`;
- keep pinned third-party repositories intact under `skills/sources/`;
- keep passive repository-maintenance instructions separate from user-facing corpus counts;
- remove stale references to the old top-level `vendor/` layout;
- preserve exact pins, licensing, and source identity.

### 2. Finish static corpus curation

Work source by source rather than expanding architecture.

For every registered source:

1. establish the full eligible denominator;
2. identify every eligible `SKILL.md` or equivalent skill entry;
3. create/maintain provenance companions;
4. bind exact-version conclusions to the skill content identity when establishable;
5. record dependency, authority, portability, and freshness context;
6. apply controlled tags;
7. assign a decisive current static disposition;
8. record rejection/retirement reasons rather than silently omitting unsuitable material.

A source is not complete because some of its skills were sampled.

### 3. Complete companion metadata

Per-skill provenance should support reasoning about:

- source repository and canonical path;
- license and relationship;
- source pin/revision;
- skill-specific freshness and earliest-known history where establishable;
- dependencies and shared references;
- authority/side-effect assumptions;
- portability;
- intended use;
- rationale for inclusion or rejection.

Exact-version verification companions should carry:

- content identity/fingerprint where establishable;
- structured review state;
- controlled tags;
- evidence/rationale;
- behavioral-validation state.

Volatile source-level context belongs separately in `registry/source-signals.yaml`, with observation timestamps. Stars, forks, activity, reputation, and official status are context, not proof of individual skill quality.

### 4. Make agent interpretation unambiguous

Current documentation and passive maintenance skills must consistently teach:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

Agents should understand that they may:

- adopt;
- adapt;
- extract;
- supplement;
- compose;
- create;
- use a checklist;
- keep behavior dynamic;
- make no change.

The corpus is prior art and design material, not a mandate to maximize reuse.

### 5. Reconcile passive navigation surfaces

`CURATED.md`, `INDEX.md`, `index.json`, category pages, registry records, and public documentation should agree with the live corpus.

These are passive static artifacts. An external curating agent updates them when needed. Do not introduce a repository-owned generator or runtime merely to maintain them.

### 6. Behavioral validation after static completion

Once the static corpus is complete, prioritize consequential/high-use skills for representative behavioral validation.

Validation is performed externally by an agent/evaluation environment. `skillz` may store the evidence but does not execute the evaluation.

Prioritize skills where poor behavior has meaningful cost, authority, security, or workflow consequences rather than attempting to behaviorally test every reference skill indiscriminately.

### 7. Ongoing limited discovery

Discovery remains useful, but it should not outrun curation.

- inspect new sources when they fill a demonstrated gap;
- re-check existing source freshness when a decision depends on it;
- avoid speculative source accumulation;
- compare before adding;
- preserve source role, license, pin, and provenance from intake onward.

## Returning-user and portability refinement

After the corpus foundation is healthy:

- improve passive guidance for identifying drift and overlap in fitted sets;
- improve composition/adaptation guidance from real use;
- refine portable skill profile documentation;
- document host-specific packaging only when a real host surface requires it;
- keep installation/external actions explicitly outside the repository and under the host agent's authority.

## Human browsing

Continue improving direct readability without turning `skillz` into an application:

- clearer category navigation;
- better static indexes and source summaries;
- visible provenance and quality state;
- clear distinction between source reputation and skill quality;
- concise companion explanations that help both humans and agents.

## Durable rules

1. **`skillz` is passive. The host agent is active.**
2. **Compare before creation. User fit before reuse.**
3. **Smallest useful set over maximum skill count.**
4. **Availability is not verification.**
5. **Exact-version evidence matters.**
6. **Attribution travels with third-party material.**
7. **Source popularity is context, not competence proof.**
8. **User-facing skills live under `skills/`.**
9. **Maintenance instructions do not count as user-facing inventory.**
10. **Returning users are refined, not reset.**
11. **No-change is a valid outcome.**
12. **No repository-owned scripts, CI, runtime, scheduler, monitor, installer, or preflight system.**

## Historical material

Older runtime-oriented plans, alpha preflight work, CI/test artifacts, Qor-era records, and execution-harness documents are historical evidence only. They do not define the current architecture or roadmap.

Current truth is controlled by `README.md`, `AGENT_START_HERE.md`, `AGENTS.md`, `BOOTSTRAP.md`, `docs/CONCEPT.md`, `docs/ARCHITECTURE_PLAN.md`, `docs/SYSTEM_STATE.md`, and the active Wayfinder map.
