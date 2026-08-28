# 🛠️ skillz

[![CI](https://github.com/Knapp-Kevin/skillz/actions/workflows/ci.yml/badge.svg)](https://github.com/Knapp-Kevin/skillz/actions/workflows/ci.yml)
![Skills](https://img.shields.io/badge/first--party_skills-49-blue)
![Sources](https://img.shields.io/badge/reference_sources-7-8A2BE2)
![Runtime](https://img.shields.io/badge/runtime-Bun_%7C_Node_22.18%2B-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

**Give this repository to your AI. It helps build the right skill set for you.**

`skillz` is a portable skill discovery, design, evaluation, installation, and transfer system for AI agents.

It is **not** primarily a catalog of skills for a person to browse and choose from.

The repository gives an AI enough process, reference material, validation tools, and installation guidance to study how a person actually works and build the smallest skill system that fits them.

## If you are an AI agent reading this

If a user gave you this repository or its GitHub URL and did not give you a more specific task, **begin the bootstrap process now**.

Do not stop at a repository summary, feature list, or "this looks useful" response unless the user explicitly asked for an overview.

1. Read [`BOOTSTRAP.md`](BOOTSTRAP.md).
2. Read [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md).
3. Use the relevant history, memory, instructions, workspace context, existing skills, and recurring corrections your current host can legitimately access.
4. Identify durable working methods that should become reusable skills.
5. Compare those needs against this repository's local and third-party references.
6. Build the skill system that best fits the user.
7. Validate it.
8. Install it when you safely can, or prepare the correct files and simple installation steps when the user must act.

For agents that automatically read repository instruction files, [`AGENTS.md`](AGENTS.md) defines the same entry contract.

## For humans: what happens when I give my AI this link?

You do not need to know how skills work.

You do not need to know how to code.

You do not need to pick skills from a giant list.

Your AI should start by looking at the useful information it already has about how you work.

That can include things such as:

- instructions you keep repeating,
- mistakes you keep correcting,
- jobs you do again and again,
- steps you almost always follow,
- tools you regularly use together,
- rules you do not want forgotten,
- ways you decide when work is actually finished,
- existing skills or instructions that already work well.

If your AI can see useful memory or prior interactions, it should use them instead of making you explain everything again.

If it cannot see old conversations or memory, it should say so and work with the evidence it actually has. It must not pretend it knows things it cannot see.

## The goal is your skill system, not our skill list

The skills already in this repository are **ingredients and reference material**.

They show useful ways to solve problems, write triggers, structure procedures, validate work, handle failure, protect authority boundaries, and make behavior more dependable.

They are not a menu you are expected to shop from.

For each need, the bootstrap may decide to:

- **KEEP** an existing skill that already fits,
- **REFINE** a skill that has the right purpose but needs stronger behavior,
- **ADOPT** a strong existing skill,
- **ADAPT** a useful reference to the user's real environment,
- **SUPPLEMENT** a current skill with one strong idea from another source,
- **COMPOSE** several skills that work better separately,
- **CREATE** a completely new custom skill,
- use a smaller **CHECKLIST/HELPER** instead,
- leave something **DYNAMIC** when formalizing it would make it worse,
- or **DO NOT CREATE** anything when a skill would add no real value.

A related skill already existing in the repository does **not** mean the agent should force the user's workflow to fit it.

If a custom skill better represents the person's real day-to-day work, the correct result is to build that custom skill and use existing skills only as design references where they help.

## Memory can contain skills that have never been written down

People often teach an AI a workflow without ever calling it a skill.

For example, a user may repeatedly tell an agent to:

1. research the current state first,
2. distinguish evidence from assumptions,
3. make a recommendation,
4. adversarially challenge it,
5. implement only after the approach survives review,
6. verify the result before claiming completion.

If that pattern appears repeatedly in accessible history or memory, the bootstrap should recognize that the user has already developed a **latent skill**.

The job is to extract the durable method, improve it where useful, test it, and save it outside the memory of one AI product.

That is how behavior learned through months of interaction can become portable instead of disappearing when the user changes agents.

## What this repository provides to the agent

The repository supplies the machinery needed to do that work:

- **Discover** recurring workflows, corrections, safeguards, and latent skills.
- **Compare** those needs against strong first-party, official, and vetted community references.
- **Synthesize** useful patterns from multiple references without inheriting unnecessary ceremony or assumptions.
- **Create** custom skills when existing implementations do not fit.
- **Evaluate** whether a skill actually improves behavior.
- **Audit** structure, risk, authority boundaries, missing-evidence handling, and unsafe assumptions.
- **Install** directly when the active agent has the capability and authority.
- **Hand off** exact packages and beginner-readable steps when installation requires human action.
- **Transfer** durable working methods between compatible AI systems instead of trapping them inside one provider's memory.

The goal is the **smallest useful skill system that makes the agent more dependable for the person it serves**.

## Compare before creation. User-fit before reuse.

The agent should always inspect relevant existing implementations before inventing a solved mechanism from scratch.

But reuse is not the objective.

**User fit is the objective.**

Existing skills are valuable because they may contain tested ideas, safeguards, abstractions, failure handling, validation methods, or useful vocabulary. Those pieces can strengthen a custom skill even when the existing skill itself should not be adopted.

The bootstrap should therefore ask:

> What is the best skill for this person's actual workflow, given everything we can learn from the reference corpus?

Not:

> Which skill in this repository can we make the user live with?

Humanity has endured enough software designed around the second question.

## Installation is part of the result

A bootstrap is not finished when it produces some Markdown files and abandons the user beside them.

For each target AI system or surface, the result must end in a clear state such as:

- `INSTALLED + VERIFIED`
- `INSTALLED, VERIFICATION PENDING`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

When the active agent can install skills through a filesystem, repository, supported API, or installer and has the required authority, it should do so and verify the result.

When a web or desktop interface requires the human to upload something, the agent should prepare the correct artifact when possible and give one-action-per-step instructions with the exact filename and one small test.

See [`docs/installation-handoff.md`](docs/installation-handoff.md).

## Portable by design

The canonical skill should remain separate from any one product's private memory or UI.

Host-specific installation is an adapter layer. A portable skill may be installed differently on a local coding agent, web assistant, IDE agent, API-driven agent, or another compatible system.

The Portable User Skill Profile records durable execution defaults, selected/custom skills, validation state, and installation state without making one provider's memory format the source of truth.

See [`docs/portable-skill-profile.md`](docs/portable-skill-profile.md).

## Where reference material comes from

The repository can use several kinds of evidence:

1. **First-party skills and tooling** created and maintained here.
2. **Official reference sources** from platform and tooling vendors.
3. **Vetted community references** that provide useful patterns or comparative value.
4. **Tracked external sources** that may be consulted when the curated corpus does not adequately cover a need.

Third-party material retains its upstream attribution and licensing requirements. Inclusion makes a source available for comparison; it does not grant blanket trust or authority.

See:

- [`registry/sources.yaml`](registry/sources.yaml) for source identity, trust class, path, and provenance metadata,
- [`docs/third-party-provenance.md`](docs/third-party-provenance.md) for attribution and adaptation rules,
- [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) for licensing boundaries,
- [`registry/candidates.yaml`](registry/candidates.yaml) for individual candidate decisions.

## Reference corpus, not storefront

[`INDEX.md`](INDEX.md) and [`index.json`](index.json) are machine- and human-readable maps of the reference corpus.

They primarily exist so **agents can search and compare efficiently**.

A beginner should not need to open the index, understand source repositories, or select skills manually.

When the curated corpus has no strong match, that is not a failure. It is evidence that the agent may need to synthesize a new skill using the repository's design and evaluation methods.

## Repository layout

```text
README.md                     # human + agent entry point
AGENTS.md                     # self-starting agent entry contract
BOOTSTRAP.md                  # simple bootstrap explanation and procedure
INDEX.md / index.json         # generated reference map
skills/
  skill-bootstrap/            # discover + design the fitted skill system
  skill-eval/                 # behavioral before/after evaluation
  skill-forge/                # custom skill creation
  skill-audit/                # structural + semantic-risk validation
  skill-sync/                 # supported local deployment
  ...                         # reusable first-party capabilities
registry/
  candidates.yaml             # per-skill intake decisions
  sources.yaml                # reference-source trust + provenance
vendor/                       # pinned official + community-vetted references
scripts/                      # deterministic repository tooling
tests/                        # behavior and contract tests
docs/
  portable-skill-profile.md   # cross-host execution profile
  installation-handoff.md     # install / upload / verification contract
  third-party-provenance.md   # attribution + adaptation rules
  evaluation-framework.md     # adoption and evaluation rules
```

## Design rules

1. **The repository URL is an invocation.** When a user points an agent here without another task, bootstrap should begin.
2. **Do not make the user shop for skills.** The agent performs discovery and comparison.
3. **Compare before creation.** Learn from existing solutions before designing another one.
4. **User-fit before reuse.** Never preserve reuse at the expense of a better custom skill.
5. **The corpus is design evidence.** Borrow useful invariants without inheriting unnecessary workflow ceremony.
6. **Behavior over aesthetics.** A polished skill that does not improve outcomes is not an improvement.
7. **Portable core, replaceable adapters.** Keep durable behavior independent from host-specific installation details.
8. **Read-only discovery by default.** Installation and other mutations require the authority expected by the target environment.
9. **Minimum necessary evidence.** Access to a private connector is not permission to mine it for profile data.
10. **Explicit provenance.** Materially copied or adapted third-party work keeps its required attribution and license obligations.
11. **Smallest useful system.** More skills are not automatically better.
12. **Installation is part of done.** The result must either work on the target or tell the user exactly what remains.

## Validation

Repository tooling enforces structural and semantic-risk validation, and behavior tests run alongside both layers.

Passing those checks proves that a skill satisfies repository contracts. It does not by itself prove the skill helps the user.

High-value skill changes should also receive controlled behavioral evaluation against representative tasks. See [`skills/skill-eval/SKILL.md`](skills/skill-eval/SKILL.md).

## Licensing

First-party content in this repository is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain their own upstream license obligations. The root MIT license does not relicense vendored or otherwise identified third-party material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).

## For advanced users and agents

The beginner experience intentionally hides most of the machinery. Advanced users and agents can work directly with:

- [`skills/skill-bootstrap/SKILL.md`](skills/skill-bootstrap/SKILL.md)
- [`skills/skill-eval/SKILL.md`](skills/skill-eval/SKILL.md)
- [`skills/skill-forge/SKILL.md`](skills/skill-forge/SKILL.md)
- [`skills/skill-audit/SKILL.md`](skills/skill-audit/SKILL.md)
- [`skills/skill-sync/SKILL.md`](skills/skill-sync/SKILL.md)
- [`docs/evaluation-framework.md`](docs/evaluation-framework.md)
- [`docs/portable-skill-profile.md`](docs/portable-skill-profile.md)
- [`docs/installation-handoff.md`](docs/installation-handoff.md)

Specific products and hosts belong in installation adapters and verified host instructions, not in the repository's core identity.

## Development status

The bootstrap architecture is being developed through Issue #7 and PR #8.

Before promotion to protected `main`, the branch still requires generated index refresh/idempotency proof, behavioral bootstrap evaluation, and the repository's governed substantiation process.
