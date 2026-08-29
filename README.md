# 🛠️ skillz

**A passive library of reusable AI skills and a guide for turning the ways an AI has learned to work with you into portable skills.**

## The one thing to understand

**`skillz` does not run. The AI agent using `skillz` does.**

This repository is not an application, agent runtime, service, memory system, scheduler, monitor, installer, test harness, or autonomous learning system.

There is no `skillz` process running in the background. It does not watch the user, collect behavior, call models, execute skills, install anything, or maintain a user profile on its own.

`skillz` is a **resource that an existing AI agent reads**.

That agent might be ChatGPT, Claude, Codex, or another compatible agent. The agent uses the context and capabilities it already legitimately has access to, follows the instructions in this repository, and uses the skill corpus as reference material.

## Why this exists

People spend months or years teaching an AI how they work.

That happens through ordinary interaction:

- repeated requests;
- corrections;
- preferences;
- recurring workflows;
- project rules;
- definitions of done;
- review patterns;
- safety boundaries;
- ways of solving the same class of problem over and over.

Some of that is just context. Some of it becomes a **repeatable method**.

Those repeatable methods are valuable because they represent work the user and agent have already done together. But they are usually trapped inside one product, one memory system, or one long-running relationship with one agent.

`skillz` helps the current agent identify the durable methods worth preserving and turn them into explicit, portable skills.

## What happens when an agent uses this repository

The agent follows this basic process:

```text
what the current agent already legitimately knows about working with the user
                                ↓
              identify durable repeatable methods
                                ↓
                 inspect the skillz reference corpus
                                ↓
        compare existing skills and useful design patterns
                                ↓
       reuse / adapt / extract / supplement / compose / create
                                ↓
             produce the smallest useful fitted skill set
```

The important distinction is that **the host agent performs every step**.

`skillz` provides the instructions, examples, reference skills, provenance, review evidence, and vocabulary that help the agent reason well about the task.

## The corpus is not a catalog you have to shop from

The repository contains a large body of reusable skills from first-party and pinned third-party sources.

Those skills are **reference material and design material**.

An agent may find that:

- one existing skill already fits perfectly;
- an existing skill is mostly right and should be adapted;
- only one procedure or safeguard from a skill is useful;
- several skills contain complementary patterns worth combining;
- the user's existing behavior is already better than the references;
- no existing skill fits and a custom skill should be created;
- the behavior is too small or too unstable to deserve a skill at all.

The goal is not maximum reuse and not maximum skill count.

The goal is the **smallest useful set of explicit behaviors that genuinely improves how the agent works with the user**.

## What counts as a skill?

Not every remembered fact or preference should become one.

For example:

> “The user prefers concise answers.”

That is probably a preference or profile instruction.

But:

> “When reviewing a proposed architecture, first establish the intended outcome, inspect the mechanisms that already exist, separate necessary safeguards from architecture-for-architecture’s-sake, and challenge unnecessary infrastructure before proposing anything new.”

That is a repeatable method. It is a strong skill candidate.

A useful rule of thumb:

- **fact or preference** → context;
- **project-specific rule** → keep with the project;
- **stable repeatable method** → skill candidate.

## Start here

If you are an AI agent reading this repository, begin with:

1. [`AGENT_START_HERE.md`](AGENT_START_HERE.md)
2. [`BOOTSTRAP.md`](BOOTSTRAP.md)
3. [`AGENTS.md`](AGENTS.md)

If the user simply gives you this repository or its URL without a narrower request, that is sufficient context to begin identifying useful repeatable methods from the user context you are legitimately able to inspect.

Do not invent inaccessible history or hidden model state. Do not search unrelated private data merely because a connector exists.

## Repository structure

All user-facing skill material lives under [`skills/`](skills/).

- [`skills/`](skills/) contains the user-facing skill corpus.
- [`skills/categories/`](skills/categories/) provides human navigation.
- [`skills/sources/`](skills/sources/) contains intact pinned third-party source corpora.
- [`registry/skills/`](registry/skills/) contains per-skill provenance companions.
- [`registry/verification/`](registry/verification/) contains exact-version review state and controlled tags.
- [`registry/sources.yaml`](registry/sources.yaml) records source identity, role, license, and pin.
- [`registry/source-signals.yaml`](registry/source-signals.yaml) records timestamped source-level context.
- [`engine/skills/`](engine/skills/) contains passive instructions for an external agent maintaining or using this repository. These are repository mechanics and do **not** count as user-facing corpus skills.

Third-party source repositories remain intact so their dependencies, references, licensing, and exact upstream identity are preserved.

## Quality is separate from availability

A skill being present in the repository does not automatically mean it is good, current, safe, or appropriate for unchanged reuse.

Review states may include:

- `verified`: the recorded exact version passed structured static review;
- `validated`: representative behavioral evidence also exists;
- `unverified`: useful as reference/design material, but not established for trusted unchanged reuse;
- `stale`: prior evidence no longer matches the current content or assumptions;
- `rejected`: unsuitable for normal unchanged reuse;
- `retired`: intentionally withdrawn.

When evaluating a candidate, reason in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

Source reputation, stars, forks, official branding, age, and popularity can provide context. They do not prove that an individual skill is good.

## What `skillz` can produce

Depending on the user's actual needs, the agent may decide to:

- **ADOPT** an existing skill;
- **ADAPT** it;
- **EXTRACT** one useful method or safeguard;
- **SUPPLEMENT** an existing user skill;
- **COMPOSE** several independent skills;
- **CREATE** a new custom skill;
- use a lightweight **CHECKLIST** instead;
- keep a behavior **DYNAMIC** rather than formalizing it;
- conclude **NO CHANGE NEEDED**.

The repository does not make that decision mechanically. The external agent reasons across the user's context and the reference material.

## Portability

The long-term value is behavioral continuity.

A good fitted skill makes an important working method explicit enough that it can be reused by another compatible agent instead of forcing the user to teach the same lesson from scratch again.

A useful shorthand is:

**Discover. Distill. Transfer.**

- **Discover** the durable working methods that emerged between the user and the current agent.
- **Distill** those methods into explicit reusable skills, using high-quality existing material where it genuinely helps.
- **Transfer** those skills across compatible agent environments when the destination host supports them.

Any installation, upload, synchronization, scheduling, validation, or external action is performed by the host agent. `skillz` itself remains passive.

## Core rules

**The agent is the runtime. `skillz` is the resource.**

**Compare before creation.**

**User fit before reuse.**

**Smallest useful set over maximum skill count.**

**Reference skills are prior art, not commands.**

**Source reputation is context, not skill quality.**

**Never claim execution, validation, installation, or evidence that did not actually occur through the external host.**

## Licensing

First-party content is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain their applicable upstream licensing and attribution requirements.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).
