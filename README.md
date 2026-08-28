# 🛠️ skillz

[![CI](https://github.com/Knapp-Kevin/skillz/actions/workflows/ci.yml/badge.svg)](https://github.com/Knapp-Kevin/skillz/actions/workflows/ci.yml)
![Library Skills](https://img.shields.io/badge/library_skills-42-blue)
![Engine Skills](https://img.shields.io/badge/engine_skills-7-lightgrey)
![Sources](https://img.shields.io/badge/reference_sources-8-8A2BE2)
![Runtime](https://img.shields.io/badge/runtime-Bun_%7C_Node_22.18%2B-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

**A growing library of reusable AI skills, plus an engine that can discover, build, evaluate, and install the right skill set for a particular person.**

`skillz` has two equally valid ways to use it.

## 1. Use it as a skill library

Browse, search, compare, install, adapt, or reuse skills directly.

The public library lives in [`skills/`](skills/). **Only actual library skills count toward the skill total.** Repository machinery is deliberately separated under [`engine/skills/`](engine/skills/) and does not count.

The goal is for `skills/` to grow into a large, curated collection containing hundreds of useful capabilities across first-party and properly attributed third-party material.

## 2. Give the repository to your AI

If you do not know which skills you need, give your AI the GitHub link to this repository.

That is the bootstrap invocation.

The engine can inspect relevant history, memory, instructions, recurring corrections, workspace context, and existing skills that the current host legitimately exposes; infer durable working methods; compare those needs against the library and reference corpus; create new skills when necessary; validate the result; and install or package the final skill system.

You do not need to know how skills work.
You do not need to know how to code.
You do not need to choose from hundreds of files.

The library remains a first-class product. Bootstrap is an accessibility and synthesis layer on top of it.

---

## Library skills versus engine skills

This distinction is fundamental.

### `skills/` = library inventory

A skill belongs in [`skills/`](skills/) when it makes sense for a user or agent to install and use independently of maintaining this repository.

Examples include research, writing, review, debugging, planning, monitoring, operations, and domain workflows.

If somebody asks, **"How many skills are in skillz?"**, the first-party/imported library count comes from this directory.

### `engine/skills/` = repository machinery

The engine uses skill-shaped procedures because skills are a useful way to make agent behavior explicit and composable. Those procedures are not catalog inventory.

Current engine skills include:

- `skill-bootstrap`
- `skill-forge`
- `skill-eval`
- `skill-audit`
- `skill-sync`
- `skills-pulse`
- `source-vetting`

These operate the repository's discovery, authoring, curation, validation, deployment, and maintenance processes. They **do not count** toward the library total.

The boundary test is:

> Would this capability make sense for a user to install independently of maintaining `skillz`?

If yes, it may belong in `skills/` even if this repository also uses it internally. Internal use alone does not make something engine machinery.

### `vendor/` = reference/source corpus

Pinned upstream repositories under [`vendor/`](vendor/) provide comparison material, upstream source integrity, and update/provenance anchors.

A `SKILL.md` existing inside a submodule does **not** automatically become a `skillz` library skill or inflate the library count. Skills must be deliberately curated/promoted or imported into the library according to licensing, provenance, dependency, and review rules.

---

## If you are an AI agent reading this

If a user gave you this repository or its GitHub URL and did not give you a more specific task, **begin bootstrap now**.

Do not stop at a repository summary, feature list, or "this looks useful" response unless the user explicitly asked for an overview.

1. Read [`BOOTSTRAP.md`](BOOTSTRAP.md).
2. Read [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md).
3. Use the relevant history, memory, instructions, workspace context, existing skills, and recurring corrections your current host can legitimately access.
4. Identify durable working methods that should become reusable skills.
5. Search and compare the actual library in `skills/` and approved reference sources.
6. Reuse, refine, adapt, supplement, or compose existing skills when they genuinely fit.
7. Create new custom skills when a better fit does not already exist.
8. Evaluate and adversarially review the resulting skill system.
9. Install it when you safely can, or prepare the correct files and simple installation steps when the user must act.

For agents that automatically read repository instruction files, [`AGENTS.md`](AGENTS.md) defines the same entry contract.

If the user explicitly asks to browse, search, compare, or install a known skill, do that directly instead of running a full bootstrap.

## The library is real. Bootstrap is extra.

An experienced user may browse the library, install a specific skill, compare implementations, or use the repository as a reference without ever running bootstrap.

Bootstrap exists for users who do not know which skills they need or whose most valuable workflows have never been written as skills at all.

For each observed need, bootstrap may decide to:

- **KEEP** an existing skill that already fits,
- **REFINE** a skill that has the right purpose but needs stronger behavior,
- **ADOPT** a strong existing skill,
- **ADAPT** a useful reference to the user's environment,
- **SUPPLEMENT** a current skill with a useful pattern,
- **COMPOSE** several skills,
- **CREATE** a completely new custom skill,
- use a smaller **CHECKLIST/HELPER** instead,
- leave something **DYNAMIC** when formalization would make it worse,
- or **DO NOT CREATE** anything when a skill would add no real value.

A related skill already existing does not mean the agent should force the user's workflow to fit it.

**Compare before creation. User-fit before reuse.**

## Memory can contain unwritten skills

People often teach an AI a workflow without ever naming it as a skill.

Repeated instructions, recurring corrections, stable task sequences, approval boundaries, tool combinations, and completion standards can be evidence of a **latent skill candidate**.

When accessible memory or history contains a stable useful pattern, bootstrap should be able to extract the durable method, improve it where useful, evaluate it, and preserve it outside one product's memory.

Do not invent inaccessible history. Access to a private connector is capability, not permission to mine it for a profile.

## Installation is part of the result

Bootstrap is not finished when it produces Markdown and leaves the user to figure out the rest.

For each target host or surface, completion should be explicit:

- `INSTALLED + VERIFIED`
- `INSTALLED, VERIFICATION PENDING`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

See [`docs/installation-handoff.md`](docs/installation-handoff.md).

## Curation and provenance

`skillz` is intended to become large, but it is not intended to become a dump.

Third-party skills should have an auditable companion record under [`registry/skills/`](registry/skills/) containing source repository/path, upstream license, source pin, skill-specific last-update revision/date, curation/check dates, dependencies, portability, permission tier, review status, and rationale.

The library distinguishes:

- **available source material** — present in an approved source corpus,
- **curated skills** — individually reviewed and documented,
- **validated skills** — curated skills with additional behavioral evidence here.

Those states are not interchangeable.

See [`CURATED.md`](CURATED.md), [`docs/curation-policy.md`](docs/curation-policy.md), [`registry/sources.yaml`](registry/sources.yaml), and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).

## Repository layout

```text
README.md                     # human + agent entry point
AGENTS.md                     # self-starting agent entry contract
BOOTSTRAP.md                  # beginner-facing bootstrap procedure
INDEX.md / index.json         # generated library/reference index

skills/                       # ACTUAL USER-FACING LIBRARY; these count
  README.md                   # library boundary and counting rule
  fact-check/
  brief-writer/
  repo-doctor/
  ...

engine/                       # repository machinery; does not count
  README.md
  skills/
    skill-bootstrap/
    skill-forge/
    skill-eval/
    skill-audit/
    skill-sync/
    skills-pulse/
    source-vetting/

registry/
  candidates.yaml             # intake decisions
  sources.yaml                # source trust/provenance
  skills/                     # per-skill provenance companions

vendor/                       # pinned upstream reference/source repos
scripts/                      # deterministic repository tooling
tests/                        # behavior and contract tests
docs/                         # architecture, curation, eval, install docs
```

## Design rules

1. **`skills/` is the library.** Engine machinery and submodule contents do not inflate its count.
2. **Maintain a useful library.** Accumulate high-value skills without turning the repository into an uncurated dump.
3. **Support direct use.** Experienced users and agents can browse, search, compare, and install specific skills without bootstrap.
4. **The repository URL is a bootstrap invocation when no other task is given.**
5. **Do not make bootstrap users shop for skills.** The agent performs discovery and comparison for them.
6. **Compare before creation.** Learn from existing solutions before inventing another one.
7. **User-fit before reuse.** Never preserve reuse at the expense of a better custom skill.
8. **Behavior over aesthetics.** A polished skill that does not improve outcomes is not an improvement.
9. **Portable core, replaceable adapters.** Keep durable behavior independent from host-specific installation details.
10. **Read-only discovery by default.** Installation and other mutations require the expected authority.
11. **Minimum necessary evidence.** Do not mine unrelated private data merely because it is accessible.
12. **Explicit provenance.** Materially copied or adapted third-party work keeps its required attribution and license obligations.
13. **Installation is part of bootstrap completion.**

## Validation

Repository machinery under `engine/` validates the actual library under `skills/`.

Structural or risk checks prove conformance to repository rules. They do not by themselves prove that a skill improves outcomes. High-value changes should also receive controlled behavioral evaluation.

See [`engine/skills/skill-eval/SKILL.md`](engine/skills/skill-eval/SKILL.md).

## Licensing

First-party content is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain their applicable upstream license obligations. The root MIT license does not relicense vendored or otherwise identified third-party material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).

## Advanced engine entry points

- [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md)
- [`engine/skills/skill-forge/SKILL.md`](engine/skills/skill-forge/SKILL.md)
- [`engine/skills/skill-eval/SKILL.md`](engine/skills/skill-eval/SKILL.md)
- [`engine/skills/skill-audit/SKILL.md`](engine/skills/skill-audit/SKILL.md)
- [`engine/skills/skill-sync/SKILL.md`](engine/skills/skill-sync/SKILL.md)
- [`engine/skills/skills-pulse/SKILL.md`](engine/skills/skills-pulse/SKILL.md)
- [`engine/skills/source-vetting/SKILL.md`](engine/skills/source-vetting/SKILL.md)

The point of those engine components is to make the library easier to discover, grow, validate, and personalize. They are not the library itself.
