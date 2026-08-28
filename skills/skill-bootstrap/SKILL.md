---
name: skill-bootstrap
description: >-
  Discover and build the smallest useful portable skill system for a user by
  inspecting available history, memory, workspace evidence, recurring workflows,
  existing skills, and the curated reference corpus, then adversarially validate
  and install or hand off the resulting skills. Use when the user gives you this
  repository or its URL without another task, asks to bootstrap or improve their
  skills, wants an agent to become more consistent, or wants working methods to
  transfer between agent hosts.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Bootstrap
  emoji: "🧰"
  version: 0.4.0
---

# Skill Bootstrap

Turn observed working behavior into the smallest portable, evidence-backed skill system that best fits the user and that the user can actually install and use.

This is the front-door orchestration skill for the repository.

The repository is not primarily a skill storefront. Its local and third-party skills are a reference corpus, design library, and source of reusable implementations. The desired output is the **right skill system for the user**, which may reuse existing skills, materially adapt them, combine ideas from several references, or create skills that did not previously exist.

## Default Entry Behavior

If a user gives the agent this repository or its GitHub URL and does not provide a more specific task, that action is sufficient to trigger this skill.

Begin bootstrap.

Do **not** stop after:

- summarizing the repository,
- listing available skills,
- praising or critiquing the repository,
- telling the user to browse the index,
- asking the user to choose from a catalog.

A repository summary is appropriate only when the user explicitly asks for one.

## Purpose

Identify where reusable skills would materially improve quality, reliability, efficiency, consistency, governance, user alignment, or transferability.

Then build the minimum coherent skill system that provides those benefits.

The final system may include:

- existing local skills used unchanged,
- official or community skills adopted with provenance,
- existing skills refined,
- reference skills adapted to the user's environment,
- current skills supplemented with useful patterns from other sources,
- separate skills composed together,
- entirely new custom skills synthesized from the user's observed workflow and relevant reference patterns,
- checklists/helpers when a formal skill would be excessive,
- deliberately dynamic behavior when formalization would reduce quality.

Then finish the job: validate the result and install the selected/custom skills when the host permits it and authority exists, or produce the exact package and beginner-readable installation steps when human action is required.

The goal is not maximum reuse or maximum skill count.

The goal is **best fit with the smallest useful system**.

## Trigger

Use this skill when:

- the user gives you this repository or repository URL with no more specific task,
- a user wants to bootstrap or improve their personal or organizational agent skill system,
- a user wants working patterns to transfer between agent hosts,
- an agent needs to infer latent skills from repeated behavior,
- a user has recurring corrections or workflows but has never formalized them,
- the user's current agent memory/history appears to contain durable working methods that should become portable,
- an existing skill ecosystem needs a broad consolidation or re-evaluation pass.

## Do Not Trigger

Do not use this skill when:

- the user already named one specific skill and only wants that skill executed,
- the user explicitly asks only for a repository overview or catalog lookup,
- the task is a one-off request with no meaningful reusable pattern,
- repository/project rules prohibit broad profile discovery,
- the available evidence is so narrow that a durable skill architecture would be mostly guesswork and the user did not ask for a provisional analysis.

## Preconditions

At least one evidence source must be available, such as:

- current conversation,
- accessible conversation history,
- persistent memory exposed by the host,
- workspace/project instructions,
- repositories or project artifacts,
- tool invocation history,
- prior agent corrections,
- an existing skill/profile configuration.

Unavailable sources are recorded as unavailable. They are never reconstructed from assumptions.

When installation is part of the outcome, identify the active host/surface if possible. If it cannot be established, skill discovery may proceed, but installation status must be `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED` rather than guessed.

## Evidence Scope and Privacy

Use the minimum evidence needed to identify stable execution patterns.

### Prefer evidence the host already exposes

When available, begin with relevant interaction history and persistent memory before asking the user to restate how they work.

Also use relevant ambient context such as:

- current conversation,
- workspace/project instructions and artifacts,
- existing skill/profile configuration,
- repository or tool history already in the active work context.

The agent should not make the user manually reconstruct information that is already available through the normal host context.

### Do not widen scope casually

Do **not** sweep unrelated connected private accounts merely because a connector exists. Email, private chat, calendar, finance, personal cloud storage, or similar external sources require at least one clear scope basis:

1. the user explicitly asks to include that source,
2. the current project/task already authorizes and requires that source, or
3. relevant material has already been surfaced into the current working context by an authorized workflow.

Access to a connector is capability, not consent to mine it for a profile.

When a smaller evidence set is sufficient, prefer it. Record source categories and availability in the output rather than copying private source content into the profile.

## Procedure

### 1. Bind to the environment

Discover authoritative local instructions first:

1. current explicit user instruction,
2. safety/security restrictions,
3. repository/project governance or instruction files,
4. workspace/operator profile if explicitly available,
5. host capabilities and accessible evidence sources,
6. current agent product and surface when installation is expected.

Record what can and cannot be inspected.

For installation, record whether the current surface appears to be web, desktop, CLI, IDE, API, or another local agent surface. Do not assume two surfaces of the same product share installed skills unless that behavior is established.

Do not ask the user to manually repeat information that is already accessible through the host.

### 2. Mine for latent skills

Review the available in-scope interaction history, memory, recent work, instructions, and tool/skill usage.

Look especially for patterns that the user may already have taught the agent without formalizing them:

- instructions repeated across tasks,
- corrections the user makes repeatedly,
- recurring reasoning patterns,
- repeated tool sequences,
- manual reconstruction of the same procedure,
- governance/security/validation rules repeatedly reintroduced,
- recurring human verification points,
- recurring definitions of "done",
- repeated dissatisfaction caused by the same failure mode,
- workflows where failure is costly,
- existing skills repeatedly used across workflows,
- overlapping or conflicting skills,
- skills that are too generic for the actual workflow,
- implicit procedures that already behave like skills even though nobody named them as such.

Treat a stable repeated procedure living only in memory/history as a **latent skill candidate**.

For every finding, distinguish observed evidence from inference.

### 3. Classify each opportunity

Classify every candidate as one of:

- **SUFFICIENT** — existing skill is adequate.
- **REFINE** — correct abstraction, inadequate implementation, guidance, tests, or governance.
- **ADOPT** — an existing implementation already solves the requirement with good fit.
- **ADAPT** — an existing implementation provides the best base but needs environmental or workflow changes.
- **SUPPLEMENT** — keep the current/custom skill but borrow a specific pattern that strengthens it.
- **COMPOSE** — use separate skills together rather than merging responsibilities.
- **CREATE** — a custom skill is the best fit for a stable reusable workflow.
- **CHECKLIST/HELPER** — formal skill would be excessive.
- **DYNAMIC** — circumstances vary enough that formalization would reduce adaptability.
- **DO NOT CREATE** — rare, trivial, volatile, redundant, or unjustified.

`CREATE` does not mean "no related skill exists."

`CREATE` is also correct when related skills exist but adapting them would preserve the wrong assumptions, UX, authority model, scope, terminology, or workflow shape.

### 4. Score candidate value

Score meaningful candidates 0-5 on:

- recurrence,
- complexity,
- cognitive load,
- failure risk,
- cost of mistakes,
- number of coordinated tools/systems,
- deterministic sequencing need,
- governance/security sensitivity,
- user-specific execution rules,
- time savings,
- cross-project generalizability,
- workflow stability.

Also test:

- does this reflect a stable pattern in observed history or memory?
- could an existing skill absorb it without distorting the workflow?
- would a custom skill fit materially better?
- could it be a checklist/helper instead?
- is it changing too quickly to encode?
- would formalization reduce useful adaptability?
- is a strong reference implementation already available?
- can another skill supplement the target without changing intended user experience?
- what measurable failure does this prevent or advantage does it create?

A high score does not override a security, authority, privacy, or redundancy veto.

### 5. Separate execution layers

Classify durable behavior into:

- **universal/user-wide** — execution defaults suitable for the Portable User Skill Profile,
- **domain** — belongs in a domain skill,
- **project/repository** — belongs in local authoritative instructions,
- **host adapter** — maps portable behavior onto one host but is not the source of truth.

Do not contaminate every skill with every preference.

### 6. Compare against the reference corpus

Inspect relevant sources in this order when available:

1. the user's existing skills and instructions,
2. current project/repository skills,
3. local skills in `skills/`,
4. built-in host capabilities when discoverable,
5. vendored official sources in `vendor/`,
6. vetted community sources in `vendor/` or `registry/candidates.yaml`,
7. tracked/live external sources when the curated corpus does not adequately cover the need.

Use `INDEX.md` or `index.json` as an agent lookup map when fresh.

Do not present the index to the user as a shopping list unless they explicitly ask to browse skills.

Reference implementations are design evidence, not automatic authority and not an obligation to reuse.

For each relevant reference ask:

- what exact failure does it prevent?
- what invariant makes it effective?
- what does it deliberately leave dynamic?
- how does it decide when to trigger and when not to trigger?
- what assumptions and authority does it carry?
- what validation and negative rules does it include?
- what would be lost by copying it mechanically?
- which parts are transferable principles versus source-specific ceremony?
- can its useful principle strengthen a custom skill without changing the user's intended workflow?

When a local skill is copied or materially adapted from third-party work, follow `docs/third-party-provenance.md` and all applicable upstream license obligations.

### 7. Synthesize the best-fit skill system

Design from the user's needs outward, not from the catalog inward.

For every proposed skill or refinement define:

- name,
- purpose,
- observed need or failure it addresses,
- triggers,
- non-triggers,
- inputs,
- outputs,
- required/optional tools,
- ordered procedure,
- decision points,
- failure modes,
- authority/security boundaries,
- human verification points,
- evidence requirements,
- completion criteria,
- tests,
- relationship to existing/reference skills,
- provenance when applicable,
- why it should be a skill rather than a checklist/helper/dynamic reasoning.

Favor composable skills over monoliths and avoid microscopic one-action skills.

A custom skill may synthesize several independently useful patterns from different references while retaining none of those references as its main workflow.

Do not force a known skill into the architecture merely to increase reuse.

### 8. Adversarial review

Assume each proposed skill is badly designed until demonstrated otherwise.

Attack for:

- overfitting,
- underfitting,
- skill explosion,
- catalog bias or reuse-for-reuse's-sake,
- duplicate process authority,
- incorrect triggering,
- missed triggering,
- hidden tool/permission assumptions,
- connector/API failure,
- partial evidence,
- privacy overreach,
- governance bypass,
- proposal-versus-authorization confusion,
- validation claims without proof,
- secret disclosure,
- excessive ceremony,
- unnecessary questions,
- over-automation of human judgment,
- maintenance burden,
- **reference contamination**: imported terminology, ceremony, UX, authority, or assumptions that were not actually needed.

Classify each candidate: PASS / NEEDS REVISION / MERGE / SPLIT / DELETE.

Then test cross-skill conflicts and precedence.

### 9. Produce the Portable User Skill Profile

Use `docs/portable-skill-profile.md`.

The profile contains durable execution methods and selected/custom skills, not biography.

Every profile claim derived from incomplete evidence must be marked as inference or provisional.

Include installation targets for known hosts/surfaces so a future agent can distinguish "this skill belongs here" from "this skill is actually installed here."

### 10. Create or refine the actual skill artifacts

Where the current environment permits file creation, produce the actual skill files rather than stopping at recommendations.

Use existing lifecycle capabilities when useful:

- `skill-forge` for convention-clean custom skill scaffolding,
- `skill-audit` for structural and semantic-risk validation,
- direct adaptation with provenance when an upstream skill is the correct base.

If the environment cannot create files, output the complete skill artifacts in a form the user can save or upload.

Do not claim an artifact exists unless it was actually created.

### 11. Validate behavior

Where the host and evidence permit, use `skill-eval` for controlled baseline/treatment testing.

For important custom or adapted skills:

1. define representative tasks and success checks before treatment,
2. observe baseline behavior without the skill when feasible,
3. run the same task with the skill,
4. compare behavioral improvement, failure rate, evidence quality, trigger accuracy, intervention burden, and relevant cost/context overhead,
5. revise when the skill adds ceremony without measurable benefit.

Do not claim validation occurred unless it actually ran.

### 12. Install or produce the installation handoff

Follow `docs/installation-handoff.md`.

For each target host/surface:

1. Identify the host and surface.
2. Determine the installation mode:
   - **DIRECT-WRITE**
   - **API-INSTALL**
   - **UI-UPLOAD**
   - **PORTABLE-HANDOFF**
3. Determine whether this agent can perform the installation itself.
4. Verify the host's current packaging/install mechanism from authoritative local docs or current official documentation when available.
5. Validate/package the selected skill files for that host.
6. If installation is possible and authorized, perform it and verify the result.
7. If human UI action is required, produce the exact upload artifact when file creation is available and give one-action-per-step instructions that name the actual file.
8. Give one small trigger test and state what success looks like.
9. Record one installation completion state for the target:
   - `INSTALLED + VERIFIED`
   - `INSTALLED, VERIFICATION PENDING`
   - `READY TO UPLOAD`
   - `USER ACTION REQUIRED`
   - `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
   - `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

Do not end with a vague "install these skills" instruction.

Do not force the user to understand repository layout, ZIP structure, filesystem conventions, or host configuration when the agent can prepare those details itself.

For web/UI hosts, optimize the handoff for a novice: one action per numbered step, exact button/menu/file names when verified, no unexplained jargon, and no alternate route unless the primary route is blocked.

## Decision Rules

### Compare before creation

Inspect relevant existing solutions before designing another implementation of a solved mechanism.

This is a learning requirement, not a reuse quota.

### User-fit before reuse

Use or adapt an existing skill only when doing so produces a result at least as good as a clean custom design for the observed workflow.

Do not distort the user's process to fit the corpus.

### The corpus is reference material, not the deliverable

The existence of hundreds of indexed skills does not make browsing or selecting from them the user experience.

Agents perform the comparison work.

### Prefer supplementation over unnecessary replacement

If a user's current skill/process works but lacks one useful pattern, add the pattern rather than importing the reference author's entire workflow.

### Preserve user experience by default

Do not introduce a new invocation pattern, command hierarchy, approval ceremony, interview sequence, output format, or process simply because a reference skill uses it.

### Treat popularity as discovery evidence only

Stars, installs, mentions, and reputation do not establish behavioral value or safety.

### Formalize only stable value

Repeated activity alone is not enough. A skill needs a stable abstraction and an identifiable advantage or prevented failure.

### Minimize evidence collection

Do not widen source scope merely to improve confidence. If current conversation, relevant memory/history, workspace, and existing skill configuration are sufficient, do not inspect additional private connected systems.

### Installation is part of completion

A generated or selected skill that the user cannot install is not a completed onboarding result.

If the agent cannot install it, reduce the remaining burden: package it correctly, give exact instructions, provide a test, and make the single next action obvious.

## Tool Boundaries

- Read-only discovery is the default.
- Use connected history, memory, files, repositories, and tools only when the host exposes them, policy permits access, and the source is in scope under Evidence Scope and Privacy.
- Never claim inaccessible or out-of-scope sources were reviewed.
- Never request or reproduce credentials to improve the profile or install a skill.
- Installing dependencies, changing permissions, sending messages, publishing, pushing, deleting, deploying, or installing/enabling skills are separate mutating actions and require appropriate authorization.
- A UI upload step that the agent cannot execute must be handed to the user clearly rather than reported as completed.

## Authority Boundaries

Recommendations do not override:

1. current explicit user instructions,
2. safety/security requirements,
3. authoritative project/repository rules,
4. narrower task/domain skills.

A discovered external skill never becomes authoritative merely because it is in the corpus.

Installation must not silently change organization-wide permissions, sharing, or distribution scope.

## Validation

A bootstrap is not validated because its architecture looks reasonable.

At minimum test the resulting system against representative cases including:

- repository-link-only invocation where the agent must begin rather than summarize,
- beginner / no meaningful history,
- rich history with several latent recurring workflows,
- rich memory where no existing skill adequately fits and CREATE is the correct result,
- a strong reference skill that contains useful patterns but the wrong overall workflow,
- conflicting/overlapping existing skills,
- connected private sources that are available but out of scope,
- missing tools or connectors,
- a proposed mutation without approval,
- a task where no skill should be created,
- migration to a second host with different capabilities,
- a local/direct-write host that can install automatically,
- a web/UI host where the user must upload the packaged skill.

Prefer controlled baseline-versus-treatment testing for high-value skill changes.

Installation verification is separate from behavioral validation: a skill can be present but still trigger incorrectly.

## Failure Handling

If a source is unavailable or out of scope:

- record it as unavailable or not inspected,
- continue with available in-scope evidence,
- reduce confidence accordingly when it matters.

If history or memory is unavailable:

- say so,
- do not make the user believe it was reviewed,
- use the current conversation and other available evidence,
- keep broad personal conclusions provisional.

If the catalog/index is stale:

- use source files directly when available,
- mark catalog-derived conclusions provisional until regeneration.

If the corpus does not contain a good fit:

- do not stop with "no matching skill found",
- use relevant references as design evidence,
- create a custom skill when the observed need justifies one.

If authority to mutate is missing:

- produce the exact proposed artifact/change and stop before mutation.

If installation requires human UI action:

- create the expected package when possible,
- give verified click-by-click instructions,
- name the exact file,
- give one test prompt,
- report `READY TO UPLOAD` or `USER ACTION REQUIRED`, not `INSTALLED`.

If the target does not support skills:

- preserve the canonical portable skill,
- clearly report the limitation,
- describe any supported adapter separately without mislabeling it as a real skill installation.

If the installation mechanism cannot be established:

- do not guess UI labels or filesystem locations,
- report `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`,
- preserve the ready skill package and the exact missing fact.

If evidence does not justify a durable skill:

- return `DO NOT CREATE`, `DYNAMIC`, or `CHECKLIST/HELPER` rather than filling the architecture with speculative skills.

## Negative rules

- Never fabricate usage evidence, recurrence, user preferences, test results, token counts, success rates, host capabilities, installation paths, UI labels, or installation status.
- Never reproduce secret-shaped strings. Refer only by type and a short non-sensitive prefix when necessary, and recommend rotation if exposure may have occurred.
- Required sections may be explicitly empty. Missing evidence is a finding, not a blank that needs invented content.
- Mark inference as inference.
- Never encode incidental sensitive/personal facts into the portable profile.
- Never inspect unrelated connected private accounts solely because they are technically accessible.
- Never treat a proposal as authorization to install, push, send, publish, deploy, change permissions, or mutate an external system.
- Never report a UI-required upload as completed unless the host actually confirms it.
- Never silently enable workspace/org-wide sharing when installing a personal skill.
- Never import a third-party procedure without preserving required provenance and license obligations.
- Never force the user to select from the catalog when the agent can perform the comparison itself.
- Never reject a justified custom skill merely because a vaguely related skill already exists.

## Completion Criteria

Bootstrap may claim completion only when:

- repository-link-only invocation, when applicable, actually progressed into discovery rather than ending in summary,
- accessible, in-scope, out-of-scope, and unavailable evidence sources are identified where relevant,
- relevant accessible memory/history was inspected when available or explicitly reported unavailable,
- major recurring and latent patterns are inventoried,
- candidates are classified and redundancy-checked,
- relevant repository/reference skills were compared before final design,
- the final architecture is optimized for user fit rather than reuse count,
- justified custom skills were created when the corpus did not fit,
- surviving candidates passed an adversarial design review or unresolved failures are explicitly reported,
- actual skill artifacts were produced where the environment permits,
- a Portable User Skill Profile was produced or a concrete reason it should not yet be produced was documented,
- validation status is explicit for every adopted, adapted, supplemented, composed, or custom recommendation,
- every known target host/surface has an explicit installation state,
- any required upload/install artifact is identified by exact filename/path or the inability to create it is stated,
- any remaining user action is expressed as simple numbered steps with one clear next action,
- every installed skill has either been verified or is explicitly marked verification pending,
- no external mutation is implied unless it actually occurred.

A bootstrap that ends with a skill shopping list, useful skill files with no installation path, or a repository summary instead of beginning discovery is incomplete.

## Output Format

```markdown
# Skill Bootstrap Result

## Evidence coverage
- Available and inspected: ...
- Available but out of scope / not inspected: ...
- Partial: ...
- Unavailable: ...

## Latent working patterns found
...

## Skill decisions
| Need | Evidence | Best-fit design | References used | Decision | Validation |
|------|----------|-----------------|-----------------|----------|------------|

## Existing skills retained or refined
...

## Custom skills created
...

## Reference patterns borrowed
...

## Do not create / keep dynamic
...

## Adversarial findings
...

## Final skill architecture
...

## Portable User Skill Profile
<YAML or linked artifact following docs/portable-skill-profile.md>

## Validation results / plan
...

## Installation
| Target | Surface | Mode | Package | Status | Verification | Next action |
|--------|---------|------|---------|--------|--------------|-------------|

### Do this now
1. <single first action, or "Nothing — installation is complete.">

### Then test it
<one small trigger prompt or automated verification result>

### You are done when
<plain-language success condition>

## Remaining material risks
...

## Review triggers
...
```

## Examples

### Repository-link-only case

The user sends only the `skillz` GitHub URL. The agent reads this repository, recognizes the URL as bootstrap invocation, inspects relevant accessible history/memory, and begins identifying latent workflows. It does not respond with a repository review or ask the user which skill they want.

### Custom-skill case

Accessible history shows that the user repeatedly performs a specialized daily workflow combining several tools, evidence rules, approval boundaries, and a particular completion test. No indexed skill fits the workflow. Several references contain strong individual patterns. Bootstrap uses those patterns as design evidence, creates a new custom skill around the user's actual workflow, records provenance where required, evaluates it, and installs or packages it.

### Existing-skill case

A user's observed workflow maps cleanly onto an existing skill with no material compromise. Bootstrap adopts the existing skill rather than recreating it, validates host compatibility, and installs or packages it.

### Web/UI installation case

A user is working in a web application that supports skill upload but the agent cannot click the user's account UI. Bootstrap creates the required upload package, reports `READY TO UPLOAD`, gives the shortest current official UI path in numbered steps, names the exact file to select, and provides one test prompt. It does not call the skill installed until the upload actually occurs.

### No-history edge case

A new user provides only the repository link and one short conversation. Bootstrap reports that broader history/memory are unavailable, uses the current conversation as provisional evidence, avoids inventing a broad personal skill architecture, and creates or recommends only what the evidence supports.

### Privacy edge case

A host has email and calendar connectors, but the user only supplied the repository link. Bootstrap does not inspect email or calendar merely because they are connected. It uses normal ambient history/memory/workspace context and records the other sources as out of scope.

### Do not activate

The user asks, "Run the fact-check skill on this article." A specific skill is already named; execute that skill rather than running a whole ecosystem bootstrap.
