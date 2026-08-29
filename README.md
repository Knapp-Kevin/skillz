# 🛠️ skillz

![Library Corpus](https://img.shields.io/badge/indexed_library-500%2B-blue)
![Registered Sources](https://img.shields.io/badge/registered_sources-14-8A2BE2)
![Passive Repository](https://img.shields.io/badge/repository-passive-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)

**A governed skill corpus and agent-guided discovery protocol for preserving repeatable user workflows across AI systems.**

`skillz` executes nothing.

It is not an application, runtime, service, autonomous agent, memory system, or background process. The AI agent reading this repository is the active system. `skillz` gives that agent instructions, reusable skills, provenance, verification evidence, and reference material so it can identify durable ways of working and turn them into a small portable skill set fitted to the user.

> **AI agent?** Start with [`AGENT_START_HERE.md`](AGENT_START_HERE.md), then [`BOOTSTRAP.md`](BOOTSTRAP.md) and [`AGENTS.md`](AGENTS.md).
>
> Use only context and capabilities the host legitimately exposes. Do not invent inaccessible history, hidden model state, or unavailable evidence.

## What this repository does

A user may spend months teaching an AI how they work through corrections, repeated instructions, recurring workflows, preferences, and definitions of done. Much of that collaboration is easy to lose when the user changes models, products, or agent hosts.

`skillz` helps the current agent make the durable parts explicit and portable.

The basic flow is:

```text
current agent experience
        ↓
review legitimately available user context
        ↓
identify durable repeatable methods
        ↓
compare against the governed skill corpus
        ↓
reuse / adapt / extract / compose / create
        ↓
produce the smallest useful portable skill set
```

The repository itself does not observe the user, execute skills, install anything, schedule anything, validate anything in the background, or call tools. Those actions, when appropriate, are performed by the external host agent using its own capabilities and authority.

## Start here

### First visit

If a user gives an agent this repository or its URL without a narrower request, the agent should begin discovery rather than merely summarize the repository.

1. Read [`AGENT_START_HERE.md`](AGENT_START_HERE.md), [`BOOTSTRAP.md`](BOOTSTRAP.md), and [`AGENTS.md`](AGENTS.md).
2. Inspect only relevant history, memory, instructions, corrections, workflows, existing skills, and project context the host legitimately exposes.
3. Identify repeatable methods worth preserving. Do not confuse simple preferences or one-off facts with skills.
4. Compare those methods against the corpus under [`skills/`](skills/).
5. Use provenance and verification companions under [`registry/`](registry/) to understand origin, freshness, quality, dependencies, authority, portability, and source context.
6. Reuse an existing skill when it genuinely fits. Adapt, extract, or compose useful patterns when that produces a better result. Create a new skill when existing material would preserve the wrong workflow or assumptions.
7. Return the smallest useful fitted set, with uncertainty and provenance made explicit.
8. If installation or external action is requested and the host supports it, the host agent may perform that action under its normal authority rules. That execution is outside `skillz`.

### Returning visit

When a user already has a fitted skill set:

1. inventory the current set and intended jobs;
2. compare it with current working patterns and accessible evidence;
3. identify meaningful drift, overlap, gaps, or stale dependencies;
4. preserve custom behavior that still works;
5. refine, replace, supplement, compose, add, or retire only where evidence supports a change;
6. allow **NO CHANGE NEEDED** as a correct result.

The goal is not to keep adding skills. The goal is to preserve the **smallest dependable set** that matches how the user actually works.

## Browse the corpus

All user-facing skill material lives under [`skills/`](skills/).

- Locally maintained skills live directly under `skills/`.
- Human category navigation lives under [`skills/categories/`](skills/categories/).
- Intact pinned third-party source corpora live under [`skills/sources/`](skills/sources/).

For reviewed third-party material, use:

- [`CURATED.md`](CURATED.md) for the human-readable reviewed shelf;
- [`registry/skills/`](registry/skills/) for provenance companions;
- [`registry/verification/`](registry/verification/) for exact-version quality state and tags;
- [`registry/sources.yaml`](registry/sources.yaml) for source identity, role, license, and pinned revision;
- [`registry/source-signals.yaml`](registry/source-signals.yaml) for timestamped source-level context such as visibility and maintenance signals.

`INDEX.md` and `index.json` are passive catalog snapshots. They may help navigation, but live skill files and registry companions control when the snapshots disagree.

## What belongs in `skills/`?

Anything intended to help an external agent perform a reusable user-facing capability belongs in the user-facing skill tree.

Third-party source repositories remain intact rather than being flattened into copied `SKILL.md` files. This preserves their dependencies, references, licensing, and exact upstream identity.

Repository-maintenance instructions may remain separately identified because they describe how an agent should curate this repository, but they are still passive instructions. They do not execute and do not count toward the user-facing corpus.

## Quality is separate from availability

A skill being present in the corpus does not automatically make it good, current, safe, or appropriate for unchanged reuse.

Quality states include:

- `verified`: the recorded exact version passed structured static review;
- `validated`: representative behavioral evidence also exists;
- `unverified`: useful as reference or design evidence, but not established for trusted unchanged reuse;
- `stale`: prior evidence no longer matches current content or assumptions;
- `rejected`: unsuitable for normal unchanged reuse;
- `retired`: intentionally withdrawn.

Verification records bind their conclusions to an exact skill fingerprint. A changed skill must be reconsidered before an old decision is treated as current.

For selection reasoning, use this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

Popularity, stars, official branding, forks, or repository age are context. They are not proof that an individual skill is good.

## Companion metadata

A useful source skill should be accompanied by enough evidence for an agent to understand what it is looking at without pretending source reputation is quality.

Companion material may include:

- source repository and canonical path;
- license and relationship to local material;
- exact source revision and skill fingerprint;
- purpose and use cases;
- skill-specific freshness and earliest-known history when establishable;
- dependency, authority, and portability context;
- structured review status and controlled tags;
- behavioral evidence when it actually exists;
- timestamped source reputation/adoption observations such as stars, forks, activity, or archive state;
- direct usage/reception evidence only when it can actually be established.

See [`docs/companion-metadata.md`](docs/companion-metadata.md) and [`docs/curation-policy.md`](docs/curation-policy.md).

## Agent interpretation rules

When using this repository, an agent should:

1. establish the user's real need before searching for a skill;
2. distinguish stable repeatable methods from simple preferences, facts, or project-local rules;
3. inspect relevant existing skills before creating another one;
4. treat each source skill as reference evidence, not a mandate to reuse it;
5. preserve useful patterns without importing unnecessary terminology, ceremony, authority, or UX;
6. prefer minimal adaptation over wholesale replacement when a current method already works;
7. create custom material when it fits materially better;
8. keep external side effects subject to the host agent's normal authorization rules;
9. never claim validation, installation, execution, or evidence that did not actually occur.

**Compare before creation. User fit before reuse. Smallest useful set over maximum skill count.**

## Repository map

| Area | Purpose |
|---|---|
| [`AGENT_START_HERE.md`](AGENT_START_HERE.md) | Entry instructions for an agent reading the repository |
| [`BOOTSTRAP.md`](BOOTSTRAP.md) | First-visit and returning-user discovery/refinement method |
| [`AGENTS.md`](AGENTS.md) | Repository operating boundaries for external agents |
| [`skills/`](skills/) | Complete user-facing skill tree |
| [`skills/categories/`](skills/categories/) | Human browse-by-purpose navigation |
| [`skills/sources/`](skills/sources/) | Pinned third-party reference corpora |
| [`CURATED.md`](CURATED.md) | Human-readable reviewed third-party shelf |
| [`registry/sources.yaml`](registry/sources.yaml) | Source identity, role, pin, and license |
| [`registry/skills/`](registry/skills/) | Per-skill provenance companions |
| [`registry/verification/`](registry/verification/) | Fingerprint-bound quality state and tags |
| [`registry/source-signals.yaml`](registry/source-signals.yaml) | Timestamped source-level context |
| [`docs/`](docs/) | Curation, verification, portability, and historical documentation |

## Licensing and attribution

First-party content is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain their applicable upstream obligations. The root MIT license does not relicense third-party material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).
