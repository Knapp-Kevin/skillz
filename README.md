# 🛠️ skillz

![Library Corpus](https://img.shields.io/badge/indexed_library-500%2B-blue)
![Engine Skills](https://img.shields.io/badge/engine_skills-7-lightgrey)
![Registered Sources](https://img.shields.io/badge/registered_sources-17-8A2BE2)
![Maintenance Runtime](https://img.shields.io/badge/maintenance_runtime-Bun_%7C_Node_22.18%2B-brightgreen)
![Agent Use](https://img.shields.io/badge/agent_use-no_local_runtime_required-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**A large reusable AI-skill library, plus an engine that can help you discover, build, install, review, and improve the skill set that fits the way you actually work.**

You do not need to understand how agent skills work. You do not need to read hundreds of files. You can hand this repository to an AI and let it do the comparison work for you.

> **AI agent?** Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md), then use [If you are an AI agent reading this](#if-you-are-an-ai-agent-reading-this). For the operating contract, read [`AGENTS.md`](AGENTS.md). For first-visit and returning-user workflows, read [`BOOTSTRAP.md`](BOOTSTRAP.md).
>
> **No shell, clone, Node, or local filesystem? That is supported.** If the agent can read this repository through GitHub, a connector, API, browser, or equivalent tool, it should use the connector-native path in [`AGENT_START_HERE.md`](AGENT_START_HERE.md) rather than stopping.

## Start here

### First visit: build your skill set

If this is your first time here, the easiest path is simple:

1. Give your AI the URL to this repository.
2. Ask it to help build the skills that would make it more useful and dependable for you, or simply provide the repository with no more specific task.
3. The bootstrap process should inspect only the relevant history, memory, instructions, existing skills, recurring corrections, and workflows the current host legitimately exposes.
4. It should compare your needs against this library, reuse good existing skills when they genuinely fit, and create custom skills when they do not.
5. It should evaluate the fitted set and install it when the host supports installation, or give you the shortest correct handoff when it does not.

Start with [`BOOTSTRAP.md`](BOOTSTRAP.md) if you want to see exactly what the AI is being asked to do.

### Returning visit: review, refine, and improve

If you already have skills from an earlier visit, come back with the repository URL and your current skill set or accessible installed-skill context.

A returning review should:

1. identify the skills you already have and the jobs they are meant to perform;
2. detect stale, overlapping, weak, unused, or missing capabilities;
3. check whether better or newer library skills now exist;
4. compare current skill fingerprints and upstream freshness where available;
5. refine, replace, supplement, or retire skills only when there is a concrete reason;
6. preserve custom behavior that still matches how you work;
7. re-evaluate changed skills and update installation state.

The goal is not to keep adding skills forever. The goal is to keep the **smallest useful set** current, reliable, and fitted to you.

## Browse the library yourself

You can also use `skillz` as a normal skill library without running bootstrap.

### Browse local skills by purpose

| Category | Examples |
|---|---|
| [Planning & Productivity](skills/categories/planning-productivity/) | brief daily work, decisions, task coordination, learning, weekly review |
| [Writing & Communication](skills/categories/writing-communication/) | briefs, deck outlines, handoffs, standups, devlogs |
| [Research & Analysis](skills/categories/research-analysis/) | comparisons, deep research, fact checking, paper review |
| [Software & Repositories](skills/categories/software-repositories/) | repository health, repo monitoring, TODO maintenance |
| [Agent Operations & Security](skills/categories/agent-operations-security/) | agent environment health, postmortems, MCP vetting, permissions |
| [Monitoring & Intelligence](skills/categories/monitoring-intelligence/) | model, platform, protocol, governance, and ecosystem scans |
| [Business & Career](skills/categories/business-career/) | career scanning, finance review, small-business operations |

See [`skills/categories/`](skills/categories/) for the full categorized local browse surface.

For the complete indexed library, including approved third-party source corpora, use:

- [`INDEX.md`](INDEX.md) for the generated human-readable catalog;
- [`index.json`](index.json) for machine-readable lookup;
- [`CURATED.md`](CURATED.md) for individually characterized and reviewed third-party skills;
- [`registry/verification/`](registry/verification/) for quality state, fingerprints, and tags;
- [`registry/skills/`](registry/skills/) for provenance and attribution.

The generated index covers local/imported skills and approved vendored corpora. Individually characterized tracked external sources extend the governed selection surface through their exact registry companions without being falsely counted as vendored/indexed inventory.

## What counts as a library skill?

### Local and directly imported skills

[`skills/`](skills/) contains user-facing skills maintained or deliberately imported in this repository. They count.

The categorized folders under [`skills/categories/`](skills/categories/) are currently a human navigation layer while recursive category-aware discovery is integrated into the repository tooling. Canonical skill paths remain stable during that compatibility transition.

### Indexed third-party library

[`vendor/`](vendor/) contains pinned upstream source repositories. Approved indexed user-facing skills in those sources are part of the available library corpus and count.

The repository historically recorded 524 vendor-indexed skills alongside 48 local skills. Current work has added sources rather than removed the historical corpus, so the library still contains **500+ available skills**. The exact current deduplicated total will be produced by the next deterministic index refresh rather than maintained by hand.

### Governed tracked external sources

[`registry/sources.yaml`](registry/sources.yaml) may also register external corpora that are intentionally tracked at exact snapshots rather than vendored wholesale. Source admission alone does **not** make every upstream skill trusted inventory.

A tracked external skill becomes a governed unchanged-selection candidate only when it has:

- exact provenance under [`registry/skills/`](registry/skills/);
- a fingerprint-bound quality companion under [`registry/verification/`](registry/verification/);
- a current `verified` or `validated` state; and
- a fingerprint that can be matched to the recorded canonical upstream content.

Connector/API/web-capable hosts can fetch that exact upstream file when relevant. This lets `skillz` use valuable external material without copying whole repositories into `vendor/` merely to make them discoverable.

### Engine machinery does not count

[`engine/skills/`](engine/skills/) contains bootstrap, forge, evaluation, audit, synchronization, ecosystem scanning, and source-vetting procedures used to operate `skillz` itself. These do **not** count as library inventory.

The boundary test is straightforward: would this capability make sense for someone to install independently of maintaining this repository? If yes, it can be library material. If its purpose is operating `skillz`, it is engine machinery.

## Quality is separate from availability

A skill being present in the library does not automatically mean it has been verified for quality.

The current quality lifecycle is:

```text
available/indexed -> characterized -> unverified -> verified -> validated
                                      \-> stale | rejected | retired
```

The rules are version-specific:

- `verified` means an exact skill version passed the current individual structured quality and effectiveness rubric in [`docs/skill-verification.md`](docs/skill-verification.md).
- `validated` is stronger. It requires representative behavioral evidence showing the skill improves outcomes.
- `unverified` means the skill may be useful as reference or design evidence but has not earned trusted unchanged selection.
- `trusted-baseline` is retained only as a legacy characterization/schema state. It is **not eligible for current unchanged selection** until replaced by an individual structured review.
- `stale` means the canonical skill changed after characterization or the supporting evidence no longer matches.
- `rejected` and `retired` are excluded from normal selection.

Each individually characterized third-party skill has provenance under [`registry/skills/`](registry/skills/) and quality metadata under [`registry/verification/`](registry/verification/). Verification records bind to the exact canonical `SKILL.md` Git blob SHA. A hash change makes the previous characterization stale until it is reviewed again.

Tags come from [`registry/taxonomy.yaml`](registry/taxonomy.yaml) and describe use case, lifecycle phase, workflow characteristics, authority level, and portability. Those tags are intended to help both humans and bootstrap choose by capability rather than by filename alone.

## Current curation state

There are currently **17 registered sources**:

- 12 pinned vendored corpora;
- 3 tracked external corpora admitted for selective exact-version curation: Cole Medin Skills, David Ondrej Skills, and Bhushan Modi Agent Skills;
- 1 normative specification source, the Agent Skills specification;
- 1 tracked dynamic-discovery source, GitHub Awesome Copilot.

The individually characterized shelf contains exact-version records with decisive `verified` and `rejected` results alongside legacy records still awaiting migration to the current individual-review standard. No record claims local behavioral validation unless actual evaluation evidence exists.

See [`CURATED.md`](CURATED.md), [`docs/curation-policy.md`](docs/curation-policy.md), [`docs/skill-verification.md`](docs/skill-verification.md), and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## If you are an AI agent reading this

Humans come first in this README. Your operating contract starts here.

**Read [`AGENT_START_HERE.md`](AGENT_START_HERE.md) first.** It defines repository-native, connector/API/web, and minimal read-only paths. Do not treat missing local execution as a bootstrap blocker.

### First-visit mode

If the user supplied this repository or its GitHub URL without a more specific task, begin bootstrap.

1. Read [`AGENT_START_HERE.md`](AGENT_START_HERE.md).
2. Read [`BOOTSTRAP.md`](BOOTSTRAP.md).
3. Read [`AGENTS.md`](AGENTS.md).
4. Read [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md) when accessible.
5. Use only relevant history, memory, workspace context, and instructions the host legitimately exposes.
6. Identify durable or latent working methods.
7. Search the complete governed surface: the indexed user-facing library plus individually characterized tracked external sources when they add relevant coverage.
8. Consult provenance, verification state, tags, authority, portability, and freshness before unchanged reuse.
9. Use the governed candidate selector when local execution and a current generated catalog are available; otherwise inspect the relevant registry/provenance records and exact pinned upstream files directly.
10. Reuse, refine, adapt, supplement, or compose when that genuinely fits.
11. Create a custom skill when the user's real workflow is not adequately represented.
12. Evaluate the fitted set and install it when authorized, or produce the shortest correct installation handoff.

### Returning-user mode

If the user already has an installed or previously generated skill set and asks to review, update, refine, improve, audit, or revisit it:

1. inventory the current skill set and its intended jobs;
2. compare current fingerprints, versions, provenance, and available evidence where accessible;
3. identify stale, duplicated, conflicting, underperforming, or missing capabilities;
4. search the current governed surface for materially better fits;
5. preserve still-valid custom behavior instead of resetting to generic defaults;
6. refine the smallest necessary set;
7. re-run appropriate verification or behavioral evaluation for changed skills;
8. update installation or portable-handoff state.

For direct browse, search, compare, or install requests, use library mode rather than forcing bootstrap.

## Selection safety

For third-party unchanged reuse:

- prefer individually characterized records whose current fingerprint matches and whose status is `verified` or `validated`;
- treat `unverified` and legacy `trusted-baseline` skills as design evidence until a current individual structured review is completed;
- exclude `stale`, `rejected`, and `retired` records from default selection;
- require a locally or connector-established matching fingerprint before treating a candidate as fully governed for unchanged selection;
- if exact fingerprint verification is unavailable on the current host, lower confidence and adapt/create rather than fabricating the match.

A high-quality skill can still be the wrong fit. **Compare before creation. User-fit before reuse.**

## Installation is part of completion

A fitted skill system should finish with an explicit host-level state such as:

- `INSTALLED + VERIFIED`
- `INSTALLED, VERIFICATION PENDING`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

See [`docs/installation-handoff.md`](docs/installation-handoff.md).

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Zero-runtime capability routing for AI agents |
| [`skills/`](skills/) | Local and directly imported user-facing skills |
| [`skills/categories/`](skills/categories/) | Human browse-by-purpose navigation |
| [`vendor/`](vendor/) | Pinned indexed third-party source corpora |
| [`CURATED.md`](CURATED.md) | Characterized third-party shelf |
| [`registry/sources.yaml`](registry/sources.yaml) | Source identity, role, pin, and license |
| [`registry/skills/`](registry/skills/) | Per-skill provenance and attribution |
| [`registry/verification/`](registry/verification/) | Hash-bound quality state, tags, and evidence |
| [`engine/skills/`](engine/skills/) | Repository machinery, excluded from library counts |
| [`docs/README.md`](docs/README.md) | Documentation map, architecture, curation, evaluation, installation, and alpha criteria |
| [`tests/`](tests/) | Behavior and contract tests |

## Alpha status

Alpha is **not locked yet**. Governed selection and recursive category-aware discovery are implemented. Connector-native agent use is a supported path; local runtime is reserved for deterministic maintenance proof. The remaining alpha-critical work is to regenerate the catalog from a fully materialized repository, prove deterministic/idempotent output and exact counts, execute a connector-native portability smoke in a constrained host, and execute the five representative blind first-visit/returning-user journey evaluations.

See [`docs/initial-implementation.md`](docs/initial-implementation.md) for the intended finish line, [`docs/alpha-lock.md`](docs/alpha-lock.md) for the live checklist, and [`docs/evals/initial-alpha-matrix.md`](docs/evals/initial-alpha-matrix.md) for the proof matrix. Broad skill acquisition and deeper corpus curation are post-alpha enrichment rather than blockers for the initial implementation.

## Validation and GitHub Actions

Structural audits and risk checks prove repository conformance. They do not prove behavioral effectiveness.

**Runtime requirements apply to maintenance tooling, not normal agent use.** An agent with repository read access must not stop solely because Node, Bun, Git, a shell, or initialized submodules are unavailable.

Automatic GitHub Actions are currently disabled to protect the Actions budget. The workflow is manual-dispatch only. Do not treat an intentionally absent CI run as evidence of failure or success.

## Licensing and attribution

First-party content is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain their applicable upstream license obligations. The root MIT license does not relicense vendored or otherwise identified third-party material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).