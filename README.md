# 🛠️ skillz

**A governed, entirely passive skill corpus and agent-guided discovery protocol.**

`skillz` executes nothing. The AI agent reading this repository is the active system.

This repository contains skills, instructions, provenance, verification evidence, tags, source context, and reference material. It is not an application, service, runtime, autonomous agent, memory system, scheduler, validator, installer, or background process.

Any reasoning, browsing, editing, validation, installation, automation, scheduling, or external action is performed by the host agent using capabilities and authority supplied outside this repository.

## Start here

Agents should read [`AGENT_START_HERE.md`](AGENT_START_HERE.md), [`BOOTSTRAP.md`](BOOTSTRAP.md), and [`AGENTS.md`](AGENTS.md).

The core flow is:

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

## Corpus

All user-facing skill material lives under [`skills/`](skills/).

- Locally maintained skills live directly under `skills/`.
- Human category navigation lives under [`skills/categories/`](skills/categories/).
- Intact pinned third-party source corpora live under [`skills/sources/`](skills/sources/).

Reviewed third-party material is described by passive companion records:

- [`CURATED.md`](CURATED.md): reviewed shelf;
- [`registry/skills/`](registry/skills/): provenance companions;
- [`registry/verification/`](registry/verification/): exact-version quality state and tags;
- [`registry/sources.yaml`](registry/sources.yaml): source identity, role, license, and pin;
- [`registry/source-signals.yaml`](registry/source-signals.yaml): timestamped source-level context.

`INDEX.md` and `index.json` are passive catalog snapshots. They may aid navigation, but live skill files and registry companions control when snapshots disagree.

## How agents should use the corpus

1. Establish the user's actual need before searching for a skill.
2. Distinguish a stable repeatable method from a simple preference, fact, or project-local rule.
3. Inspect relevant existing skills and companion evidence.
4. Treat reference skills as prior art, not instructions to reuse them wholesale.
5. Reuse an exact skill when it genuinely fits.
6. Adapt, extract, supplement, or compose useful patterns when that fits better.
7. Create a custom skill when existing material preserves the wrong workflow, assumptions, authority, terminology, or user experience.
8. Preserve provenance and licensing when third-party material materially contributes.
9. Keep external side effects subject to the host agent's normal authority rules.
10. Never claim execution, validation, installation, or evidence that did not actually occur outside this repository.

## Quality is separate from availability

A skill being present does not make it good, current, safe, or appropriate for unchanged reuse.

Verification companions may record states such as:

- `verified`: the recorded exact version passed structured static review;
- `validated`: representative behavioral evidence also exists;
- `unverified`: useful reference/design evidence without trusted unchanged status;
- `stale`: prior evidence no longer matches current content or assumptions;
- `rejected`: unsuitable for normal unchanged reuse;
- `retired`: intentionally withdrawn.

For selection reasoning use:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

Popularity, stars, forks, official branding, or repository age are context. They are not proof that an individual skill is good.

## Companion metadata

Useful source skills should carry enough passive evidence for a reviewing agent to understand:

- source repository and canonical path;
- license and relationship;
- exact source revision and skill fingerprint;
- purpose and use cases;
- skill-specific freshness/history when establishable;
- dependency, authority, and portability context;
- structured review status and controlled tags;
- behavioral evidence only when it actually exists;
- timestamped source visibility/maintenance signals;
- direct usage or reception evidence only when genuinely supported.

See [`docs/companion-metadata.md`](docs/companion-metadata.md) and [`docs/curation-policy.md`](docs/curation-policy.md).

## Repository boundary

`skillz` owns no execution layer.

Repository-maintenance skills may describe how an external agent should curate, review, organize, or update this repository. They remain passive instructions and do not count toward the user-facing skill corpus.

Third-party sources remain intact so their dependencies, references, licensing, and exact upstream identity are preserved.

## Core rules

**Compare before creation.**

**User fit before reuse.**

**Smallest useful set over maximum skill count.**

**Source reputation is context, not skill quality.**

**Any active behavior belongs to the external agent, never to `skillz`.**

## Licensing

First-party content is licensed under the [MIT License](LICENSE). Third-party repositories and materially derived content retain their upstream obligations.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).
