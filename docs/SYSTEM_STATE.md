# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-29 |
| **Active work** | PR #42 passive-repository reconciliation, followed by corpus curation, provenance/verification completion, organization, and documentation reconciliation |
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

The unified-tree branch has reconciled characterized companion records and established these current source states:

- Vercel Agent Skills: exact pinned denominator 9/9; all provenance + verification companions reconciled; 6 verified / 3 rejected;
- Cloudflare Skills: exact pinned denominator 13/13; all companions reconciled; 11 verified / 2 rejected;
- Google Agents CLI: exact pinned denominator 7/7; all companions reconciled; all 7 verified;
- OpenHands Extensions: exact pinned denominator 1/1; companion fingerprint matches the pinned skill; rejected unchanged;
- Anthropic Skills: exact pinned denominator 17/17; all companions reconciled; 10 verified / 7 rejected;
- Matt Pocock Skills: exact eligible denominator 29/29; all companions reconciled;
- Cline Skills: pinned README publishes 36 first-class skills; all 36 have provenance + exact-version review companions and decisive static states: 19 verified / 17 rejected unchanged, plus one additional unlisted/internal `cline-session-history` skill characterized separately;
- Addy Osmani Agent Skills: exact pinned denominator 24/24; all 24 have provenance + exact-version review companions, controlled tags, dependency/authority/portability characterization, and decisive static states. Final closure tranche: four verified and four rejected unchanged.

These figures distinguish complete source denominators from partial review coverage. A reconciled characterized subset is not the same thing as a statically complete source.

## Remaining corpus frontier

PR #42 remains the active structural frontier until its passive-repository reconciliation is complete and merged. Within that constraint, primary work remains static corpus curation rather than architecture expansion:

1. finish the remaining current first-party maintenance/documentation sweep for stale execution and legacy physical-path assumptions;
2. reconcile `INDEX.md` and `index.json` as passive static snapshots once the underlying paths and companion metadata are internally consistent;
3. reconcile remaining public counts/status wording to live curated truth;
4. establish exact denominators and complete static review for the remaining registered source families: Anthropic Knowledge Work, AWS, Microsoft, and Azure;
5. ensure every eligible skill has decisive provenance, exact-version review state, controlled tags, and dependency/authority/portability characterization;
6. keep source-level reputation/context separate from individual skill quality;
7. only after static corpus completion, prioritize consequential skills for external behavioral validation.

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

Advance PR #42 with the smallest remaining reconciliation unit while continuing non-conflicting corpus work:

1. finish the passive first-party maintenance/documentation sweep;
2. reconcile the passive catalog snapshots only after path and companion consistency is established;
3. reconcile remaining public status/count surfaces;
4. review the final PR diff for accidental loss of passive reference/history material;
5. merge PR #42 when those gates are satisfied;
6. continue source-by-source static curation with Anthropic Knowledge Work, then the remaining AWS/Microsoft/Azure families unless evidence establishes a better ordering.

Wayfinder Issue #35 remains the destination/scope map. External reviewer feedback remains evidence to evaluate, not an instruction to implement.
