# Make Your AI Better at Helping You

You do not need to understand skills, write code, clone repositories, or browse hundreds of files.

**Give your AI the GitHub link to this repository. That is enough to start.**

`skillz` is passive. The host agent reads the repository, reasons over legitimately available context, and creates or hands off a fitted skill system using capabilities it already has.

There is no CI, runtime, test harness, or executable proof requirement.

## First visit

If the user provides this repository with no narrower task and has no fitted skill system to review, begin first-visit bootstrap.

Read [`AGENT_START_HERE.md`](AGENT_START_HERE.md), [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md), and [`AGENTS.md`](AGENTS.md).

Then:

1. inspect the minimum relevant accessible evidence needed to identify durable working patterns;
2. translate those patterns into capability requirements before searching by skill name;
3. compare existing user/project skills, the local library, governed third-party records, the pinned 500+ reference corpus when available, and relevant tracked upstream references;
4. inspect both whole-skill fit and reusable components, including required scripts, templates, references, fixtures, or other package material;
5. gate unchanged third-party reuse on exact-version quality, provenance, licensing, dependencies, authority, portability, identity confidence, and user fit;
6. choose explicitly among reuse, refinement, adaptation, supplementation, composition, custom creation, helper/checklist, dynamic handling, or no skill;
7. compose the smallest coherent system;
8. adapt artifacts to the actual host instead of assuming one product's format;
9. adversarially review important instructions for likely misinterpretation, overreach, hidden assumptions, or unnecessary ceremony;
10. install only when capability and authority exist, otherwise provide a complete portable handoff.

## Returning visit

Do not rebuild from zero.

1. inventory the existing fitted system and the jobs its pieces perform;
2. identify only material drift, overlap, conflict, changed need, or missing capability;
3. preserve custom behavior and skill-owned supporting components that still fit;
4. re-evaluate only affected capabilities;
5. make the smallest justified change;
6. review changed instructions semantically again;
7. update the installation/handoff state.

**`NO CHANGE NEEDED` is a correct result.**

## Reference corpus and governed selection

`vendor/` contains pinned upstream reference corpora. Other sources may remain tracked upstream through `registry/sources.yaml`.

Both are prior-art and discovery surfaces. **Availability does not create blanket trust.** A reference can be valuable for comparison, component extraction, or adaptation even when it has not earned unchanged-reuse eligibility.

An unchanged third-party skill is eligible for consideration only when its individual exact-version state is `verified` or `validated` and the remaining provenance, license, dependency, authority, portability, identity, and fit conditions are acceptable.

- `unverified`: reference/design evidence only;
- `trusted-baseline`: legacy characterization only;
- `stale`: do not inherit prior review silently;
- `rejected` / `retired`: exclude from normal unchanged selection.

A blocked whole skill may still contain a useful idea. Component reuse does not bypass the reason the source material was limited or rejected.

## Semantic quality

The quality model is defined in [`docs/skill-verification.md`](docs/skill-verification.md).

- `verified` means the exact skill/package version passed structured semantic review.
- `validated` means the verified material also received representative scenario/adversarial semantic review.

These are best-effort judgments about instruction and package quality. They are not guarantees about the capability or compliance of any particular model.

## Curation state

Core bootstrap functionality is complete. Skill discovery and evaluation continue as ongoing enrichment.

See [`CURATION_QUEUE.md`](CURATION_QUEUE.md) for the living evidence ledger showing completed source-level review depth, current per-skill companions, reconciliation work, admitted sources still under evaluation, and future discovery candidates.

## The result

A good result may adopt an existing skill, refine one, adapt one, supplement one, compose several, create something new, use a smaller helper, keep behavior dynamic, retire something unnecessary, or conclude that no durable skill change is warranted.

The goal is the **smallest dependable skill system that matches the user's actual workflow and environment**.

Finish with complete artifacts or a complete portable package and an explicit handoff state such as `INSTALLED`, `READY TO UPLOAD`, `USER ACTION REQUIRED`, or a specific compatibility blocker.
