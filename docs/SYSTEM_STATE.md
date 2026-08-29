# System State

## Snapshot

| Attribute | Value |
|---|---|
| **Last updated** | 2026-08-29 |
| **Active work** | PR #42 passive-repository reconciliation, admitted-source static completion, governed discovery/source-vetting, and documentation/catalog reconciliation |
| **Architecture** | Entirely passive repository; external agent is the active system |
| **Purpose** | Accumulate reusable skill knowledge so the viewing agent can construct the smallest useful custom skill set for the user |
| **Wayfinder map** | GitHub Issue #35 |
| **Source queue** | GitHub Issue #27 |
| **Active structure work** | GitHub Issue #41 / PR #42 |

## Repository model

```text
skillz/
├── README.md                         human + agent front door
├── AGENT_START_HERE.md               passive agent entry instructions
├── BOOTSTRAP.md                      first-visit + returning-user method
├── AGENTS.md                         agent operating boundaries
├── skills/                           complete admitted user-facing skill tree
│   ├── categories/                   human navigation
│   └── sources/                      pinned third-party reference corpora
├── engine/skills/                    passive repository-curation/use instructions
├── registry/
│   ├── sources.yaml                  admitted/reference/discovery source identity + role
│   ├── source-signals.yaml           timestamped source-level context
│   ├── categories.yaml               local category assignments
│   ├── skills/                       per-skill provenance companions
│   ├── verification/                 exact-version quality state + tags
│   └── taxonomy.yaml                 controlled characterization vocabulary
├── docs/                             curation, provenance, validation, portability, history
└── INDEX.md / index.json             passive catalog snapshots
```

There is no repository runtime, CI workflow, test runner, preflight process, executable helper layer, scheduler, monitor, crawler, installer, or background service.

Any active behavior is performed by the external agent reading the repository using capabilities supplied by its host.

## Knowledge and source model

`skillz` is not merely an installable-skill shelf. It accumulates complete skills, procedures, safeguards, anti-patterns, rejected examples, creator methods, standards, source-specific knowledge, provenance, exact-version quality evidence, and portability/freshness context.

The host agent combines that accumulated knowledge with relevant user context and may adopt, adapt, extract, supplement, compose, create, use a checklist, keep behavior dynamic, or make no change.

The source lifecycle is:

**discovery surface → candidate source → admitted corpus/reference → exact-version skill review → user-fit decision**

Discovery/source-vetting may proceed in parallel with admitted-source curation. Discovery does not establish individual quality, trust, or installation authority.

## Inventory boundaries

- User-facing admitted skills belong under `skills/`.
- Pinned third-party repositories under `skills/sources/` are user-facing reference corpus material.
- Passive maintenance/use instructions under `engine/skills/` do not count toward user-facing corpus totals.
- Tracked discovery surfaces and standards may live only in the source registry and issue queue without being vendored or counted as admitted skill inventory.
- Registry and documentation files are evidence/instruction surfaces, not executable product logic.

Current public corpus counts should be treated as provisional when older catalog snapshots disagree with the live tree. Exact denominators and static companion records control.

## Quality and provenance model

- Discovery is not admission.
- Admission is not verification.
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

## Current admitted-source curation progress

Statically complete:

- Vercel Agent Skills: 9/9; 6 verified / 3 rejected;
- Cloudflare Skills: 13/13; 11 verified / 2 rejected;
- Google Agents CLI: 7/7; all verified;
- OpenHands Extensions: 1/1; rejected unchanged;
- Anthropic Skills: 17/17; 10 verified / 7 rejected;
- Anthropic Knowledge Work Plugins: 74/74; 36 verified / 38 rejected unchanged;
- Matt Pocock Skills: 29/29;
- Cline Skills: 36/36 published first-class skills; 19 verified / 17 rejected unchanged, plus one separately characterized internal/unlisted skill;
- Addy Osmani Agent Skills: 24/24 with decisive exact-version states.

In progress:

- AWS Agent Toolkit: exact pinned denominator **72** (14 core + 58 specialized). All 72 canonical skill entry points have been inspected against pin `ff1481a7bc1a04ee00ebf63d3a8a149aa6a2c546`, with source-level static disposition **70 verified / 2 rejected unchanged**. Exact per-skill provenance and verification companion pairs currently exist for **6/72** skills (`amazon-bedrock`, `aws-billing-and-cost-management`, `aws-blocks`, `aws-cdk`, `aws-sdk-swift-usage`, and `aws-transform`); **66/72** still require companion population before the source can be called statically complete. Package fingerprints use canonical skill-package Git tree SHA-1 identity, including bundled references/assets/scripts. The two rejected unchanged skills are `aws-sdk-swift-usage` and `aws-transform`.
- Microsoft Skills: pending full denominator/static review.
- Microsoft Azure Skills: pending full denominator/static review.

## Active discovery/source-vetting

- Hugging Face Skills is now a tracked official candidate source at reviewed snapshot `cead19e10754e773bad24fecef83cb64be24094e`; root Apache-2.0; selective deeper intake accepted. Individual skills remain unverified until reviewed.
- GitHub Awesome Copilot remains a registered dynamic-discovery surface, not a trusted wholesale corpus.
- Agent Skills Specification remains a registered normative portability/format reference.
- Creator/source candidates tracked in Issue #27 include Cole Medin, David Ondrej, Nate B. Jones, Andrej Karpathy-derived methodology, Sabrina Ramonov, Sean Kochel/upstream recommendations, and Chase AI+ restricted-reference material.

Discovery is performed intentionally by the external host agent. No automated monitoring/intake service exists or is desired.

## Remaining frontier

1. finish AWS exact-version companion closure (6/72 populated; 66 remaining);
2. complete Microsoft Skills;
3. complete Microsoft Azure Skills;
4. continue governed discovery/source-vetting in parallel, admitting sources only when identity, licensing, source role, and relevance justify it;
5. reconcile first-party user-facing skill denominator and any residual registered-source gaps;
6. finish current first-party maintenance/documentation sweep for stale execution and legacy physical-path assumptions;
7. reconcile `INDEX.md` and `index.json` as passive static snapshots;
8. reconcile README/governance/public count surfaces to live truth;
9. review PR #42 final diff and merge when the passive tree is internally consistent;
10. only after static corpus completion, prioritize consequential/high-use skills for external behavioral validation.

## Passive-repository invariant

Current first-party files must not instruct `skillz` itself to:

- run code;
- start a process;
- schedule work;
- monitor or crawl a source;
- execute tests;
- install or synchronize skills;
- fetch network data autonomously;
- validate itself through a runtime;
- depend on CI or a local command.

A skill may instruct the **external host agent** to use tools or perform actions when the user's request and authority permit. That activity belongs to the host, not to this repository.

Wayfinder Issue #35 remains the destination/scope map. External reviewer feedback remains evidence to evaluate, not an instruction to implement.
