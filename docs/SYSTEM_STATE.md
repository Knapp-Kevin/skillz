# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-29 |
| **Active work** | Corpus curation, provenance/verification completion, organization, and documentation reconciliation |
| **Architecture** | Entirely passive repository; external agent is the active system |
| **Wayfinder map** | GitHub Issue #35 |
| **Active structure work** | GitHub Issue #41 / PR #42 |

## Repository model

```text
skillz/
├── README.md                         human + agent front door
├── AGENT_START_HERE.md               passive agent entry instructions
├── BOOTSTRAP.md                      first-visit + returning-user method
├── AGENTS.md                         agent operating boundaries
├── skills/                           complete user-facing skill tree
│   ├── categories/                   human navigation
│   └── sources/                      pinned third-party reference corpora
├── engine/skills/                    passive repository-curation instructions
├── registry/
│   ├── sources.yaml                  source identity, role, pin, license
│   ├── source-signals.yaml           timestamped source-level context
│   ├── categories.yaml               local category assignments
│   ├── skills/                       per-skill provenance companions
│   ├── verification/                 exact-version quality state + tags
│   └── taxonomy.yaml                 controlled characterization vocabulary
├── docs/                             curation, provenance, validation, portability, history
└── INDEX.md / index.json             passive catalog snapshots
```

There is no repository runtime, CI workflow, test runner, preflight process, executable helper layer, scheduler, monitor, installer, or background service.

Any active behavior is performed by the external agent reading the repository using capabilities supplied by its host.

## Inventory boundaries

- User-facing skills belong under `skills/`.
- Pinned third-party repositories under `skills/sources/` are user-facing reference corpus material.
- Passive maintenance instructions under `engine/skills/` explain how an external agent should curate `skillz`; they do not count toward user-facing corpus totals.
- Registry and documentation files are evidence/instruction surfaces, not executable product logic.

Current public corpus counts should be treated as provisional when older catalog snapshots disagree with the live tree. The curation effort should reconcile exact denominators and static companion records source by source rather than relying on a generator or runtime proof.

## Quality and provenance model

- Source identity and individual skill quality are separate.
- Missing individual quality evidence does not become trusted merely because a source is reputable.
- Verification conclusions apply to the exact recorded skill version/fingerprint.
- `verified` means structured static review passed.
- `validated` additionally requires actual representative behavioral evidence produced by an external evaluating agent.
- `unverified` is design/reference evidence by default.
- `stale`, `rejected`, and `retired` material is excluded from normal unchanged reuse.
- Source visibility/activity signals are contextual only.

For selection use:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

## Current curation progress

The unified-tree branch has reconciled characterized companion records for:

- Vercel Agent Skills: 9/9;
- Cloudflare Skills: 13/13;
- Google Agents CLI: 7/7;
- OpenHands characterized subset: 1/1;
- Cline characterized subset: 7/7;
- Addy Osmani characterized subset: 10/10;
- Anthropic Skills: 17/17;
- Matt Pocock Skills: 29/29.

These figures describe the characterized/reconciled subset discussed in the active curation work. They do not imply that every registered source has had its full eligible denominator completed.

## Remaining corpus frontier

Primary work remains static corpus curation, not architecture expansion:

1. reconcile denominators for partially characterized sources such as Addy, Cline, and OpenHands where the full pinned-tree denominator has not yet been established;
2. review untouched/unfinished registered sources such as AWS, Microsoft, Azure, and Anthropic Knowledge Work;
3. ensure every eligible skill has decisive provenance, exact-version review state, controlled tags, and dependency/authority/portability characterization;
4. keep source-level reputation/context separate from individual skill quality;
5. reconcile passive catalog/documentation snapshots with live curated truth;
6. only after static corpus completion, prioritize consequential skills for external behavioral validation.

## Passive-repository invariant

Current first-party files must not instruct `skillz` itself to:

- run code;
- start a process;
- schedule work;
- monitor a source;
- execute tests;
- install or synchronize skills;
- fetch network data;
- validate itself through a runtime;
- depend on CI or a local command.

A skill may instruct the **external host agent** to use tools or perform actions when the user's request and authority permit. That activity belongs to the host, not to this repository.

## Current next action

Continue the curation pass using the external agent:

1. finish passive documentation reconciliation;
2. reconcile the next incomplete source denominator;
3. review its eligible skills one by one;
4. record provenance, exact-version quality state, tags, and relevant context;
5. make the smallest justified static repository changes;
6. repeat source by source.

Wayfinder Issue #35 remains the destination/scope map. External reviewer feedback remains evidence to evaluate, not an instruction to implement.
