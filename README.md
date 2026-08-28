# 🛠️ skillz

![Library Corpus](https://img.shields.io/badge/indexed_library-500%2B-blue)
![Engine Skills](https://img.shields.io/badge/engine_skills-7-lightgrey)
![Registered Sources](https://img.shields.io/badge/registered_sources-14-8A2BE2)
![Runtime](https://img.shields.io/badge/runtime-Bun_%7C_Node_22.18%2B-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

**A large reusable AI-skill library, plus an engine that can discover, build, evaluate, and install a fitted skill set for a particular person.**

`skillz` has two equally valid entry paths.

## 1. Use it as a skill library

Browse, search, compare, install, adapt, or reuse skills through [`INDEX.md`](INDEX.md), [`index.json`](index.json), the locally maintained skills under [`skills/`](skills/), and the approved indexed source corpus under [`vendor/`](vendor/).

**The library is the whole indexed user-facing corpus, not merely the directories under `skills/`.**

The repository historically recorded 524 vendor-indexed skills alongside 48 local skills. Current work has added sources rather than removed the historical corpus, so the repository still contains **500+ available library skills**. The exact current deduplicated count is intentionally deferred to the next generated-index refresh rather than maintained by hand.

## 2. Give the repository to your AI

If you do not know which skills you need, give your AI this repository URL. With no more specific task, that is the bootstrap invocation.

The engine can use relevant history, memory, instructions, recurring corrections, workspace context, and existing skills that the current host legitimately exposes; infer durable working methods; compare those needs against the library; create new skills when necessary; evaluate the result; and install or package the fitted skill system.

You do not need to know how skills work, know how to code, or choose from hundreds of files.

The library is the asset. Bootstrap is the accessibility and synthesis layer built on top of it.

## What counts, and what does not

### Local/imported library: `skills/`

[`skills/`](skills/) contains user-facing skills maintained or deliberately imported directly in this repository. They count.

### Indexed reference library: `vendor/`

[`vendor/`](vendor/) contains pinned upstream source repositories. Approved indexed user-facing skills in these sources are part of the available library corpus and count.

Availability does **not** mean quality verification. A skill may be present and searchable while still being unverified.

### Engine machinery: `engine/skills/`

[`engine/skills/`](engine/skills/) contains bootstrap, forge, evaluation, audit, sync, ecosystem scanning, and source-vetting procedures used to operate `skillz`. These do **not** count as library inventory.

The boundary test is simple: would the capability make sense to install independently of maintaining `skillz`? If yes, it can be library material. If its purpose is operating this repository, it is engine machinery.

## Quality is not inherited from a logo

Source reputation and individual skill quality are separate facts.

The quality lifecycle is:

```text
available/indexed -> characterized -> unverified | trusted-baseline | verified -> validated
                                             \-> stale | rejected | retired
```

Current policy:

- **Matt Pocock** is the sole `trusted-baseline` source. Matt skills do not need to prove baseline quality from scratch, but individual skills still need fingerprints and characterization tags before they are treated as fully characterized selection candidates.
- **Every other skill-bearing source starts `unverified`**, including official vendor repositories.
- `verified` means an exact skill version passed the structured quality/effectiveness rubric in [`docs/skill-verification.md`](docs/skill-verification.md).
- `validated` is stronger. It requires representative behavioral evidence showing the skill improves outcomes.
- `stale` means the canonical skill changed after characterization or the supporting evidence no longer matches.

### Hash-bound characterization

Each individually characterized third-party skill has:

1. provenance under [`registry/skills/`](registry/skills/), and
2. quality/tags under [`registry/verification/`](registry/verification/).

Verification records bind to the exact canonical `SKILL.md` Git blob SHA. A hash change invalidates the old characterization for operational selection until it is reviewed again.

Run the zero-network integrity check deliberately with:

```bash
node engine/skills/source-vetting/scripts/verify-characterization-integrity.ts
```

Tags come from [`registry/taxonomy.yaml`](registry/taxonomy.yaml) and describe use case, lifecycle phase, workflow characteristics, authority level, and portability. Those dimensions are intended to improve bootstrap matching instead of treating skill names as the entire selection algorithm.

## Current curation state

There are currently **14 registered sources**:

- 12 pinned vendored corpora;
- 1 normative specification source, the Agent Skills specification;
- 1 tracked dynamic-discovery source, GitHub Awesome Copilot.

The current individually characterized sample contains:

- 3 Matt Pocock skills marked `trusted-baseline` and fingerprinted;
- 3 non-Matt skills that passed structured verification: Cline `review-team`, Cloudflare `agents-sdk`, and Google `google-agents-cli-eval`;
- 10 Addy Osmani skills characterized and fingerprinted but intentionally reset to `unverified` under the new policy.

None of those records claims local behavioral validation unless actual eval evidence exists.

See [`CURATED.md`](CURATED.md), [`docs/curation-policy.md`](docs/curation-policy.md), [`docs/skill-verification.md`](docs/skill-verification.md), and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## If you are an AI agent reading this

If the user supplied this repository or its GitHub URL without a more specific task, **begin bootstrap now**.

1. Read [`BOOTSTRAP.md`](BOOTSTRAP.md).
2. Read [`AGENTS.md`](AGENTS.md).
3. Read [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md).
4. Use only relevant history, memory, workspace context, and instructions the host legitimately exposes.
5. Identify durable or latent working methods.
6. Search the entire indexed user-facing library, including approved vendor sources.
7. Consult provenance, verification state, tags, authority, portability, and freshness before unchanged reuse.
8. Reuse, refine, adapt, supplement, or compose when that genuinely fits.
9. Create a custom skill when the user's real workflow is not adequately represented.
10. Evaluate the fitted set and install it when authorized, or produce the shortest correct installation handoff.

For direct browse/search/install requests, use library mode rather than forcing bootstrap.

## Selection safety

For third-party unchanged reuse:

- prefer individually characterized records whose current fingerprint matches and whose status is `trusted-baseline`, `verified`, or `validated`;
- treat `unverified` skills as design evidence until verified on demand;
- exclude `stale`, `rejected`, and `retired` records from default selection;
- a Matt skill without an individual characterization record may inherit source-quality confidence, but it still lacks a locally bound fingerprint/tag profile and should be characterized before being treated as a fully governed selection candidate.

A high-quality skill can still be the wrong fit. **Compare before creation. User-fit before reuse.**

## Memory can contain unwritten skills

Repeated instructions, recurring corrections, stable task sequences, approval boundaries, tool combinations, and completion standards can be evidence of a latent skill candidate.

When accessible history or memory contains a stable useful pattern, bootstrap should preserve the durable method rather than forcing the user to reconstruct it. Do not invent inaccessible history or mine unrelated private connectors merely because they exist.

## Installation is part of completion

A fitted skill system should finish with an explicit host-level state such as:

- `INSTALLED + VERIFIED`
- `INSTALLED, VERIFICATION PENDING`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

See [`docs/installation-handoff.md`](docs/installation-handoff.md).

## Repository layout

```text
README.md / AGENTS.md / BOOTSTRAP.md
INDEX.md / index.json             # generated library map

skills/                           # local/imported user-facing library
engine/skills/                    # repository machinery, excluded from count

registry/
  sources.yaml                    # source identity, role, default quality state
  taxonomy.yaml                   # controlled characterization vocabulary
  skills/                         # provenance companions
  verification/                   # hash-bound quality/tags/evidence

vendor/                           # pinned indexed upstream corpora
scripts/                          # deterministic repository tooling
tests/                            # behavior and contract tests
docs/                             # architecture, curation, eval, install docs
```

## Alpha status

Alpha is **not locked yet**. The foundational governance is now in place, but bootstrap selection still needs to consume verification/tags directly, the generated index needs a current deterministic refresh, and representative end-to-end fitted-set evals still need to demonstrate reuse, rejection, custom creation, and installation/handoff behavior.

See [`docs/alpha-lock.md`](docs/alpha-lock.md) for the exact remaining gate list.

## Validation and Actions

Structural audits and risk checks prove repository conformance. They do not prove behavioral effectiveness.

Automatic GitHub Actions are currently disabled to protect the Actions budget. The workflow is manual-dispatch only. Do not treat an intentionally absent CI run as evidence of failure or success.

## Licensing

First-party content is licensed under the [MIT License](LICENSE).

Third-party repositories and materially derived content retain their applicable upstream license obligations. The root MIT license does not relicense vendored or otherwise identified third-party material.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/third-party-provenance.md`](docs/third-party-provenance.md).
