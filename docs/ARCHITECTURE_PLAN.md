# Architecture

## Objective

Keep `skillz` as an entirely passive repository that helps an external AI agent discover, evaluate, adapt, compose, create, curate, and transfer reusable skills.

The repository must keep four things distinct:

1. **user-facing skill material**;
2. **passive repository-curation instructions**;
3. **source/provenance metadata**;
4. **quality and behavioral evidence**.

There is no execution layer inside the repository.

## Repository shape

```text
skillz/
├── README.md
├── AGENT_START_HERE.md
├── BOOTSTRAP.md
├── AGENTS.md
├── skills/
│   ├── <local user-facing skills>/
│   ├── categories/
│   └── sources/                      intact pinned third-party corpora
├── engine/skills/                    passive curation/bootstrap instructions
├── registry/
│   ├── sources.yaml
│   ├── source-signals.yaml
│   ├── categories.yaml
│   ├── skills/                       provenance companions
│   ├── verification/                 exact-version quality/tags/evidence
│   └── taxonomy.yaml
├── docs/
├── CURATED.md
├── INDEX.md                          passive catalog snapshot
└── index.json                        passive machine-readable snapshot
```

## Inventory boundaries

### `skills/`

The complete user-facing skill tree. These are the capabilities a user or external agent may reuse, adapt, extract from, compose, or learn from.

### `skills/sources/`

Pinned third-party repositories retained intact so their shared references, dependencies, licensing, and exact upstream identity remain honest.

Presence here establishes availability/reference value, not individual quality.

### `engine/skills/`

Passive instructions describing how an external agent should bootstrap, audit, evaluate, curate, transfer, or research skills and this repository.

These files do not execute and do not count toward the user-facing corpus.

### `registry/`

Passive evidence and classification data.

- `sources.yaml`: source identity, role, pin, and license;
- `source-signals.yaml`: timestamped source-level context;
- `categories.yaml`: local browse/category assignments;
- `skills/`: per-skill provenance companions;
- `verification/`: exact-version quality status, tags, and evidence;
- `taxonomy.yaml`: controlled characterization vocabulary.

## Load-bearing rules

1. **The repository is passive.** Any active behavior belongs to the external host agent.
2. **User-facing and maintenance skill populations stay distinct.** Maintenance instructions never inflate corpus counts.
3. **All user-facing skill material lives under `skills/`.**
4. **Third-party sources remain intact when flattening would lose dependencies, identity, or licensing context.**
5. **Availability is not verification.**
6. **Quality evidence is version-specific.** Exact-version conclusions apply only to the recorded skill/fingerprint and supporting assumptions.
7. **Attribution travels with third-party material.**
8. **Compare before creation. User fit before reuse.**
9. **Source popularity is context, not proof.**
10. **Returning users are refined, not reset.**
11. **Private access is scoped.** Connector capability is not blanket permission to mine unrelated data.
12. **No repository-owned runtime, scripts, CI, test runner, scheduler, monitor, installer, or preflight process.**

## Discovery and selection

Discovery and selection are reasoning tasks performed by the external agent.

The repository supplies:

- user-facing skill text;
- categories and tags;
- provenance;
- exact-version review state;
- freshness evidence;
- dependency/authority/portability context;
- source reputation/adoption context where established.

The external agent uses those materials in this order:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

The agent may choose `ADOPT`, `ADAPT`, `EXTRACT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, `CHECKLIST`, `DYNAMIC`, or `NO CHANGE`.

No deterministic selector inside this repository is required or desired.

## Catalogs

`INDEX.md` and `index.json` are passive navigation snapshots, not executable/generated truth that requires a repository runtime.

When they drift from the live tree or registry, the external curating agent should reconcile them as ordinary static artifacts or rely on the live source/registry records until reconciliation is complete.

Do not introduce a generator merely to maintain the catalog.

## Static review

Static curation is performed by an external reviewing agent using the instructions under `engine/skills/` and the evidence it can legitimately inspect.

A source is statically complete when every eligible skill in the established denominator has adequate provenance/characterization and a decisive current review state under the repository's curation policy.

Static review may consider:

- structure and trigger quality;
- scope and redundancy;
- dependencies;
- authority and privacy boundaries;
- portability;
- source freshness;
- licensing;
- exact content identity when establishable;
- controlled tags;
- safety and failure handling.

## Behavioral validation

Behavioral validation is separate from static review and is performed outside the repository by an external agent or evaluation environment.

The repository may store resulting evidence, but it does not execute the evaluation.

Consequential/high-use skills should be prioritized after static corpus completion rather than attempting to behaviorally test every reference skill indiscriminately.

## First-visit and returning-user use

The repository URL is sufficient invocation context for first-visit discovery when no more specific task is given.

The external agent:

1. inspects legitimately available user context;
2. identifies durable repeatable methods;
3. compares them against the corpus;
4. creates the smallest fitted skill set;
5. adversarially reviews important changes;
6. optionally performs external installation or validation only when its host supports and authorizes it.

Returning refinement begins with the existing fitted set and makes only justified changes. `NO CHANGE NEEDED` is valid.

## Mutation boundary

Reading, comparing, characterizing, and designing are read-only by default.

Repository writes, installation, publishing, sending, permissions changes, or other external side effects require the authority expected by the host/destination. Those actions are performed by the external agent, never by `skillz` itself.

## Historical material

Older Qor-era gates, runtime-oriented plans, CI references, preflight records, and execution-oriented evaluation artifacts may remain as historical evidence where useful, but they are not current architecture and must not override the passive-repository contract in:

- `README.md`;
- `AGENT_START_HERE.md`;
- `AGENTS.md`;
- `BOOTSTRAP.md`;
- `docs/CONCEPT.md`;
- `docs/SYSTEM_STATE.md`;
- this document.
