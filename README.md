# 🛠️ skillz

[![CI](https://github.com/Knapp-Kevin/skillz/actions/workflows/ci.yml/badge.svg)](https://github.com/Knapp-Kevin/skillz/actions/workflows/ci.yml)
![Skills](https://img.shields.io/badge/first--party_skills-49-blue)
![Sources](https://img.shields.io/badge/reference_sources-7-8A2BE2)
![Runtime](https://img.shields.io/badge/runtime-Bun_%7C_Node_22.18%2B-brightgreen)
![Install](https://img.shields.io/badge/install-zero-success)

**A portable skill discovery, creation, evaluation, and installation system for AI agents.**

`skillz` helps an AI learn how you work, find reusable skills that already solve your problems, improve or combine them when useful, create only what is missing, and carry those working methods between compatible AI systems.

It is designed for people who know exactly what they need and for people who have never heard the phrase "AI skill" before.

## New here? Start here.

You do not need to know what an AI skill is.

You do not need to choose from hundreds of files.

You do not need to be a programmer.

Give your AI access to this repository and point it to **[BOOTSTRAP.md](BOOTSTRAP.md)**.

The bootstrap process helps your AI:

1. look at the relevant work, history, memory, files, tools, and instructions it can actually access,
2. notice things you do again and again,
3. find skills in this repository that already help with those things,
4. improve or combine existing skills when that is better than starting over,
5. create a new skill only when something useful is truly missing,
6. test whether those skills actually make the AI more dependable,
7. save important working rules in a portable form that another compatible system can use, and
8. **install the skills when it safely can, or give you the exact file and simple steps needed to install them yourself.**

In plain language: **teach an AI how you work once, turn the useful lessons into reusable skills, and make those skills portable instead of trapping them inside one product's memory.**

> **Beginner path:** [BOOTSTRAP.md](BOOTSTRAP.md)
>
> **Already know which skill you need?** Use [INDEX.md](INDEX.md) or [index.json](index.json).

---

## What this repository does

`skillz` is more than a folder of prompts.

It provides a complete lifecycle for reusable agent behavior:

- **Discover** — identify repeated workflows, corrections, safeguards, and execution patterns that may deserve a skill.
- **Compare** — check existing first-party, official, and vetted community skills before inventing another one.
- **Adapt** — borrow useful patterns without silently replacing the user's process or experience.
- **Create** — build a custom skill only when the existing corpus leaves a real gap.
- **Evaluate** — test whether a skill actually improves behavior rather than merely looking sophisticated.
- **Audit** — check structure, risk, authority boundaries, missing evidence handling, and unsafe assumptions.
- **Install** — deploy automatically when the active agent has the capability and authority, or prepare the correct package plus simple human instructions when it does not.
- **Transfer** — keep durable working methods outside any one provider's private memory so compatible agent systems can reuse them.

The goal is not to collect the most skills. The goal is to find the **smallest useful set that makes the agent more dependable for the person or system it serves**.

## One-command-style starting instruction

Give the connected AI this instruction:

```text
Read BOOTSTRAP.md and help me figure out which skills would make you better at helping me. When they are ready, either install them if you can safely do that, or give me the exact files and simple steps I need to install them in the AI system I am using.
```

The user should not need to understand the repository layout, package format, filesystem paths, or installation mechanics before getting useful results.

## How the bootstrap decides what to do

For each potential capability, the bootstrap can decide to:

- **KEEP** an existing skill that already works,
- **REFINE** a good skill that needs stronger instructions, tests, or safeguards,
- **ADOPT** a strong existing skill,
- **ADAPT** a strong reference to the user's environment,
- **SUPPLEMENT** a current skill with one useful pattern from another source,
- **COMPOSE** separate skills that should remain separate,
- **CREATE** a new skill when there is a stable, justified gap,
- use a **CHECKLIST/HELPER** instead when a full skill would be excessive,
- leave a workflow **DYNAMIC** when formalizing it would make it worse, or
- **DO NOT CREATE** anything when the value is not there.

Presence in the repository is not automatic trust. A popular or official skill can still be wrong for the target workflow.

## Installation is part of the result

A bootstrap is not finished when it produces a folder and leaves the user staring at it like an archaeological artifact.

For each target agent or surface, the result must end in a clear state such as:

- `INSTALLED + VERIFIED`
- `INSTALLED, VERIFICATION PENDING`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

When the active agent has a supported filesystem, API, repository, or installer and the required authority, it can perform installation directly.

When a web or desktop interface requires a human upload, the agent should prepare the correct artifact when possible and give short, current, click-by-click instructions that identify the exact file and end with one small test.

See [`docs/installation-handoff.md`](docs/installation-handoff.md).

## Portable by design

The canonical skill remains separate from any one host's private memory or UI.

Host-specific installation is treated as an adapter layer. The same portable skill may be installed differently on a local coding agent, a web assistant, an IDE agent, an API-driven agent, or another compatible system.

The repository does **not** assume that one product, vendor, runtime, or interface is the permanent center of the user's workflow.

The Portable User Skill Profile records durable execution defaults, selected skills, validation state, and installation state separately for each known host/surface. See [`docs/portable-skill-profile.md`](docs/portable-skill-profile.md).

## Where the skills come from

The repository contains:

1. **First-party skills** created and maintained here.
2. **Official reference sources** from platform and tooling vendors.
3. **Selected community references** included because they provide useful patterns for comparison, adaptation, supplementation, composition, or benchmarking.

Third-party work keeps its attribution and license information. Inclusion makes a source available for evaluation; it does not grant blanket authority or trust.

See:

- [`registry/sources.yaml`](registry/sources.yaml) — source identity, trust class, path, and provenance metadata
- [`docs/third-party-provenance.md`](docs/third-party-provenance.md) — attribution and adaptation rules
- [`registry/candidates.yaml`](registry/candidates.yaml) — individual candidate decisions

## Skill series

49 first-party skills across seven series:

| Series | Skills | Purpose |
|--------|--------|---------|
| **Pulse** | vendor and topic monitoring skills driven by a shared collector | recurring ecosystem awareness |
| **Research** | `deep-dive`, `compare`, `fact-check`, `paper-digest`, `source-vetting` | structured evidence-based inquiry |
| **Agent-ops** | `skill-eval`, `mcp-vetting`, `agent-postmortem`, `handoff-writer`, `permissions-review` | operating and improving agent systems |
| **Daily-ops** | `daily-briefing`, `inbox-triage`, `standup-writer`, `week-in-review`, `task-surface` | recurring operational work |
| **Comms & life** | `brief-writer`, `decision-log`, `devlog-draft`, `deck-outline`, `finance-review`, `smallbiz-ops`, `career-radar`, `learning-plan` | reusable communication and planning workflows |
| **Repo hygiene** | `repo-pulse`, `repo-doctor`, `todo-harvester` | repository inspection and maintenance |
| **Meta** | `skill-bootstrap`, `skills-pulse`, `skill-audit`, `skill-sync`, `skill-forge`, `agent-home-doctor` | discover, build, validate, install, and maintain skills |

## Skill index

[INDEX.md](INDEX.md) and [index.json](index.json) are the generated catalog of local skills and allowed reference sources.

Agents should resolve skills through the index rather than scanning the repository blindly.

After adding or changing a skill or reference source:

```text
node scripts/build-index.ts
```

The index is generated and should not be edited by hand.

## Repository layout

```text
BOOTSTRAP.md                 # beginner + agent onboarding entry point
INDEX.md / index.json        # generated skill catalog
skills/                      # first-party skills
  skill-bootstrap/           # discovery, architecture, validation + install handoff
  skill-eval/                # controlled skill evaluation
  skill-forge/               # skill creation
  skill-audit/               # structural + semantic-risk validation
  skill-sync/                # supported local deployment
  ...
registry/
  candidates.yaml            # per-skill intake decisions
  sources.yaml               # reference source trust + provenance
vendor/                      # pinned official + community-vetted references
scripts/                     # shared deterministic tooling
tests/                       # behavior and contract tests
docs/
  portable-skill-profile.md  # portable execution + installation profile
  installation-handoff.md    # direct install / upload / verification contract
  third-party-provenance.md  # attribution + adaptation rules
  evaluation-framework.md    # adoption and evaluation rules
  skill-template.md          # local authoring scaffold
ROADMAP.md                   # architecture and development status
```

## Validation

Repository tooling uses two enforced validation layers:

1. **Structural validation** checks skill shape, metadata, scripts, registry values, and generated-index freshness.
2. **Semantic-risk validation** checks for dangerous or misleading behavior such as secret handling failures, fabricated evidence, unsafe mutations, missing approval boundaries, and portability assumptions.

Behavior tests run alongside both layers.

Passing structural checks is not proof that a skill is useful. High-value changes should also receive behavioral evaluation against representative tasks.

## Design rules

The repository stays useful instead of becoming an enormous prompt junk drawer by following a few rules:

1. **Reuse before creation.** Search the existing corpus before making another skill.
2. **Behavior over aesthetics.** A beautifully written skill that does not improve outcomes is not an improvement.
3. **Portable core, replaceable adapters.** Keep durable behavior independent from host-specific installation details.
4. **Read-only discovery by default.** Installation, publishing, permission changes, and other mutations require the authority expected by the target environment.
5. **Minimum necessary evidence.** Access to a connected private source is not permission to mine it for profile data.
6. **Explicit provenance.** Materially copied or adapted third-party work keeps required attribution and licensing information.
7. **Smallest useful system.** More skills are not automatically better.
8. **Installation is part of done.** The result must either work on the target or tell the user exactly what remains.

## Vendored reference sources

The current reference corpus includes official sources from Anthropic, Vercel, Microsoft, Azure, and AWS, plus a community-vetted skill collection from Matt Pocock.

The complete source registry, classifications, resolved paths, and provenance metadata live in [`registry/sources.yaml`](registry/sources.yaml).

Pins are refreshed deliberately rather than silently. Third-party source updates remain subject to review and evaluation.

## For advanced users and agents

The beginner entry point intentionally hides most of the machinery. Advanced users and agents can work directly with:

- [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md)
- [`skills/skill-eval/SKILL.md`](skills/skill-eval/SKILL.md)
- [`skills/skill-forge/SKILL.md`](skills/skill-forge/SKILL.md)
- [`skills/skill-audit/SKILL.md`](skills/skill-audit/SKILL.md)
- [`skills/skill-sync/SKILL.md`](skills/skill-sync/SKILL.md)
- [`docs/evaluation-framework.md`](docs/evaluation-framework.md)
- [`docs/portable-skill-profile.md`](docs/portable-skill-profile.md)
- [`docs/installation-handoff.md`](docs/installation-handoff.md)

Specific products and hosts belong in their installation adapters and verified host instructions, not in the repository's core identity.

## Development status

The next-generation bootstrap/onboarding architecture is being developed through Issue #7 and PR #8.

Before promotion to `main`, the branch still requires:

- generated `INDEX.md` / `index.json` refresh and idempotency proof,
- behavioral bootstrap evaluation, including direct-install and human-upload cases,
- final governed substantiation required by the repository's development process.

The public repository may be browsed now, but the bootstrap changes described above are not on `main` until PR #8 is merged.
