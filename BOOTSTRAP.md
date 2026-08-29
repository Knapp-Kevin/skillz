# Make Your AI Better at Helping You

Give your AI the GitHub link to this repository. That is enough to start.

`skillz` is passive. It does not run bootstrap, select candidates, execute validation, or install anything. The AI agent reading these instructions performs the work using context and capabilities supplied by its own host.

## First visit

If the user supplied this repository or its URL without a narrower task and does not already have a fitted skill set, begin discovery rather than merely summarizing the repository.

Read [`AGENT_START_HERE.md`](AGENT_START_HERE.md), [`AGENTS.md`](AGENTS.md), and [`engine/skills/skill-bootstrap/SKILL.md`](engine/skills/skill-bootstrap/SKILL.md).

### 1. Inspect relevant existing evidence

Use only context the host legitimately exposes and that is relevant to the user's working methods, such as:

- current conversation;
- accessible interaction history or persistent memory;
- recurring corrections;
- workspace/project instructions;
- existing skills;
- repeated workflows or tool combinations;
- definitions of done.

Do not ask the user to reconstruct information already accessible. Do not invent inaccessible history. Do not mine unrelated private connectors merely because they are connected.

### 2. Identify durable working methods

Look for repeated procedures, reasoning patterns, safeguards, review sequences, failure-prevention rules, and human-verification points.

Separate:

- simple preferences/profile facts;
- project-local rules;
- stable reusable methods that merit a skill.

### 3. Compare against the corpus

Inspect relevant user-facing material under [`skills/`](skills/), including pinned reference sources under [`skills/sources/`](skills/sources/).

Use passive companion evidence where available:

- [`registry/skills/`](registry/skills/) for provenance;
- [`registry/verification/`](registry/verification/) for exact-version review state and tags;
- [`registry/sources.yaml`](registry/sources.yaml) for source role, license, and pin;
- [`registry/source-signals.yaml`](registry/source-signals.yaml) for source-level context.

When exact content identity can be established through the host, compare it with the recorded fingerprint before making an exact-version claim. When it cannot, lower confidence rather than inventing a match.

### 4. Choose the right relationship

For each need, choose among:

- **SUFFICIENT**: no change needed;
- **ADOPT**: reuse an existing skill unchanged;
- **ADAPT**: use an existing skill as the base but change it;
- **EXTRACT**: take a useful pattern without adopting the source workflow;
- **SUPPLEMENT**: strengthen an existing skill;
- **COMPOSE**: use separate skills together;
- **CREATE**: build a custom skill because it fits materially better;
- **CHECKLIST**: formal skill would be excessive;
- **DYNAMIC**: keep the behavior flexible;
- **DO NOT CREATE**: evidence or value is insufficient.

The corpus is design material, not a reuse quota.

### 5. Build the smallest useful set

For every retained skill define:

- purpose;
- triggers and non-triggers;
- ordered procedure;
- evidence requirements;
- decision points;
- authority/privacy boundaries;
- failure handling;
- completion criteria;
- relationship to source/reference material;
- provenance when applicable.

Avoid both giant monolithic skills and microscopic one-action skills.

### 6. Adversarially review

Challenge the fitted set for:

- overfitting;
- unnecessary skill creation;
- duplicated authority;
- poor triggering;
- hidden capability assumptions;
- privacy overreach;
- unsupported certainty;
- copied ceremony or terminology that does not help the user;
- unnecessary maintenance burden.

Revise, merge, split, or delete as needed.

### 7. Create static artifacts

When the external host can write files and the user has authorized repository changes, create or refine the actual Markdown skill artifacts and passive companion metadata.

When direct file creation is unavailable, provide complete portable artifacts for saving or handoff.

`skillz` itself does not perform the write.

### 8. Evaluate or install only through the host

If behavioral evaluation, installation, upload, scheduling, or another external action is useful and authorized, the external host agent performs it with its own tools.

Never describe that action as something `skillz` executed.

## Returning visit

Do not restart from zero.

1. Inventory the current fitted skills and intended jobs.
2. Compare them with current user behavior and accessible evidence.
3. Identify meaningful drift, overlap, stale assumptions, or missing capabilities.
4. Preserve custom behavior that still works.
5. Search the corpus only where a real improvement opportunity exists.
6. Make the smallest justified change.
7. Permit **NO CHANGE NEEDED** as a successful outcome.

## How to use quality metadata

For selection reasoning, use:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**

- `verified`: structured static review passed for the recorded version;
- `validated`: representative behavioral evidence also exists;
- `unverified`: design/reference evidence by default;
- `stale`, `rejected`, `retired`: exclude from normal unchanged reuse.

Popularity, source reputation, stars, forks, or official branding are useful context only. They do not establish individual skill quality.

## Completion

The user should be able to tell:

- which durable methods were identified;
- which skills were reused, adapted, extracted from, composed, created, or left unchanged;
- what evidence supports those decisions;
- what remains uncertain;
- what static artifacts now exist;
- whether any external installation/action was actually performed by the host or remains a separate handoff.

**Compare before creation. User fit before reuse. Smallest useful set over maximum skill count.**
