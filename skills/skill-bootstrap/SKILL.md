---
name: skill-bootstrap
description: >-
  Discover the smallest useful portable skill system for a user by inspecting
  available history, memory, workspace evidence, recurring workflows, existing
  skills, and the curated reference corpus, then adversarially validate and
  install or hand off the proposed skill set. Use when the user asks to
  "bootstrap my skills", "figure out what skills I need", "make my agent more
  consistent", "port how I work to another agent", or when onboarding a user
  who has little or no formal skill configuration.
metadata:
  author: frostwulf.zo.computer
  category: Meta
  display-name: Skill Bootstrap
  emoji: "🧰"
  version: 0.3.0
---

# Skill Bootstrap

Turn observed working behavior into a small, portable, evidence-backed skill layer that the user can actually install and use.

This is the front-door orchestration skill for the repository. It does not assume the user already understands skills, the repository layout, installation paths, packaging, or which capabilities should be formalized.

## Purpose

Identify where reusable skills would materially improve quality, reliability, efficiency, consistency, governance, or user alignment, then select, refine, adapt, compose, or propose the minimum coherent skill set that provides those benefits.

Then finish the job: install the selected skills when the host permits it and authority exists, or produce the exact package and beginner-readable installation steps when human action is required.

The goal is not maximum skill count.

## Trigger

Use this skill when:

- a user wants to bootstrap or improve their personal/organizational agent skill system,
- a user wants working patterns to transfer between agent hosts,
- an agent needs to infer latent skills from repeated behavior,
- a user has many recurring corrections or workflows but has never formalized them,
- an existing skill ecosystem needs a broad consolidation/re-evaluation pass.

## Do Not Trigger

Do not use this skill when:

- the user already named one specific skill and only wants that skill executed,
- the task is a one-off request with no meaningful reusable pattern,
- the user only wants a catalog lookup,
- repository/project rules prohibit broad profile discovery,
- the available evidence is so narrow that a durable skill architecture would be mostly guesswork and the user did not ask for a provisional analysis.

## Preconditions

At least one evidence source must be available, such as:

- current conversation
- accessible conversation history
- persistent memory exposed by the host
- workspace/project instructions
- repositories or project artifacts
- tool invocation history
- prior agent corrections
- an existing skill/profile configuration

Unavailable sources are recorded as unavailable. They are never reconstructed from assumptions.

The active host/surface should also be identified when installation is part of the requested outcome. If the host cannot be established, skill discovery may proceed, but installation status must be `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED` rather than guessed.

## Evidence Scope and Privacy

Use the minimum evidence needed to identify stable execution patterns.

The following ambient working context may be inspected when the host normally exposes it for the current task:

- current conversation and directly relevant conversation history,
- persistent memory already available to the agent for normal assistance,
- current workspace/project instructions and artifacts,
- existing skill/profile configuration,
- repository or tool history already in the active work context.

Do **not** sweep unrelated connected private accounts merely because a connector exists. Email, private chat, calendar, finance, personal cloud storage, or similar external sources require at least one clear scope basis:

1. the user explicitly asks to include that source,
2. the current project/task already authorizes and requires that source, or
3. the relevant material has already been surfaced into the current working context by an authorized workflow.

Access to a connector is capability, not consent to mine it for a profile.

When a smaller evidence set is sufficient, prefer it. Record source categories and availability in the output rather than copying private source content into the profile.

## Procedure

### 1. Bind to the environment

Discover authoritative local instructions first:

1. repository/project governance or instruction files,
2. workspace/operator profile if explicitly available,
3. current user instructions,
4. host capabilities and accessible evidence sources,
5. current agent product and surface when installation is expected.

Record what can and cannot be inspected.

For installation, record whether the current surface appears to be web, desktop, CLI, IDE, API, or another local agent surface. Do not assume two surfaces of the same product share installed skills unless that behavior is established.

Do not ask the user to manually repeat information that is already accessible through the host.

### 2. Build an evidence inventory

Review the available in-scope recent work and tool/skill usage.

Look for:

- existing skills repeatedly used across workflows,
- repeated reasoning patterns,
- repeated tool sequences,
- manual reconstruction of the same procedure,
- governance/security/validation rules repeatedly reintroduced,
- recurring human verification points,
- repeated corrections or dissatisfaction,
- workflows where failure is costly,
- overlapping or conflicting skills,
- skills that are too generic for the actual workflow,
- implicit procedures that behave like skills even though nobody named them as such.

For every finding, distinguish observed evidence from inference.

### 3. Classify each opportunity

Classify every candidate as one of:

- **SUFFICIENT** — existing skill is adequate.
- **REFINE** — correct abstraction, inadequate implementation/guidance/tests/governance.
- **ADOPT** — a repository/reference skill already solves the requirement.
- **ADAPT** — an existing implementation should be customized for the environment.
- **SUPPLEMENT** — keep the current skill but borrow a specific pattern that strengthens it.
- **COMPOSE** — use separate skills together rather than merging responsibilities.
- **CREATE** — a stable reusable workflow has no adequate existing implementation.
- **CHECKLIST/HELPER** — formal skill would be excessive.
- **DYNAMIC** — circumstances vary enough that formalization would reduce adaptability.
- **DO NOT CREATE** — rare, trivial, volatile, redundant, or unjustified.

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

- could an existing skill absorb it?
- could it be a checklist/helper instead?
- is it changing too quickly to encode?
- would formalization reduce useful adaptability?
- is a strong reference implementation already available?
- can another skill supplement the current one without changing user experience?
- what measurable failure does this prevent or advantage does it create?

A high score does not override a security, authority, privacy, or redundancy veto.

### 5. Separate execution layers

Classify durable behavior into:

- **universal/user-wide** — execution defaults suitable for the Portable User Skill Profile,
- **domain** — belongs in a domain skill,
- **project/repository** — belongs in local authoritative instructions,
- **host adapter** — maps portable behavior onto one host but is not the source of truth.

Do not contaminate every skill with every preference.

### 6. Compare against the repository corpus

Inspect in order:

1. local skills in `skills/`,
2. current project/repository skills,
3. built-in host capabilities when discoverable,
4. vendored official sources in `vendor/`,
5. vetted community sources in `vendor/` or `registry/candidates.yaml`,
6. tracked external sources only when the earlier layers do not cover the need.

Use `INDEX.md` or `index.json` as the primary catalog when fresh.

Reference implementations are design evidence, not automatic authority.

For each relevant reference ask:

- what exact failure does it prevent?
- what invariant makes it effective?
- what does it deliberately leave dynamic?
- what assumptions and authority does it carry?
- what validation and negative rules does it include?
- what would be lost by copying it mechanically?
- can its useful principle be incorporated without changing the target workflow?

When a local skill is copied or materially adapted from third-party work, follow `docs/third-party-provenance.md`.

### 7. Design the minimum skill architecture

For every proposed skill or refinement define:

- name,
- purpose,
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
- why it should be a skill rather than a checklist/helper/dynamic reasoning.

Favor composable skills over monoliths and avoid microscopic one-action skills.

### 8. Adversarial review

Assume each proposed skill is badly designed until demonstrated otherwise.

Attack for:

- overfitting,
- underfitting,
- skill explosion,
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

The profile contains durable execution methods and selected skills, not biography.

Every profile claim derived from incomplete evidence must be marked as inference or provisional.

Include installation targets for known hosts/surfaces so a future agent can distinguish "this skill belongs here" from "this skill is actually installed here."

### 10. Plan or execute validation

Where the host and permissions allow, use existing lifecycle skills:

- `skill-eval` for controlled baseline/treatment testing,
- `skill-forge` for convention-clean local skill scaffolding,
- `skill-audit` for structural and semantic-risk validation,
- `skill-sync` for supported local host deployment.

Do not claim those steps occurred unless they actually ran.

Mutating repository state, installing skills, or deploying to hosts requires the authority expected by the target environment.

### 11. Install or produce the installation handoff

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

### Prefer reuse over creation

Do not create a new skill when an existing skill meets the requirement without material compromise.

### Prefer supplementation over replacement

If a user's current skill/process works but lacks one useful pattern, add the pattern rather than importing the reference author's entire workflow.

### Preserve user experience by default

Do not introduce a new invocation pattern, command hierarchy, approval ceremony, interview sequence, output format, or process simply because a reference skill uses it.

### Treat popularity as discovery evidence only

Stars, installs, mentions, and reputation do not establish behavioral value or safety.

### Formalize only stable value

Repeated activity alone is not enough. A skill needs a stable abstraction and an identifiable advantage or prevented failure.

### Minimize evidence collection

Do not widen source scope merely to improve confidence. If the current conversation, memory, workspace, and existing skill configuration are sufficient, do not inspect additional private connected systems.

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

- beginner / no meaningful history,
- rich history with several latent recurring workflows,
- conflicting/overlapping existing skills,
- connected private sources that are available but out of scope,
- missing tools or connectors,
- a proposed mutation without approval,
- a task where no skill should be created,
- migration to a second host with different capabilities,
- a local/direct-write host that can install automatically,
- a web/UI host where the user must upload the packaged skill.

Prefer controlled baseline-versus-treatment testing for high-value skill changes.

Installation verification is separate from behavioral validation: the skill can be present but still trigger incorrectly.

## Failure Handling

If a source is unavailable or out of scope:

- record it as unavailable or not inspected,
- continue with available in-scope evidence,
- reduce confidence accordingly when it matters.

If the catalog/index is stale:

- use source files directly when available,
- mark catalog-derived conclusions provisional until regeneration.

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

## Completion Criteria

Bootstrap may claim completion only when:

- accessible, in-scope, out-of-scope, and unavailable evidence sources are identified where relevant,
- major recurring patterns are inventoried,
- candidates are classified and redundancy-checked,
- relevant repository/reference skills were compared before new creation was recommended,
- surviving candidates passed an adversarial design review or unresolved failures are explicitly reported,
- a Portable User Skill Profile was produced or a concrete reason it should not yet be produced was documented,
- validation status is explicit for every adopted/adapted/custom recommendation,
- every known target host/surface has an explicit installation state,
- any required upload/install artifact is identified by exact filename/path or the inability to create it is stated,
- any remaining user action is expressed as simple numbered steps with one clear next action,
- every installed skill has either been verified or is explicitly marked verification pending,
- no external mutation is implied unless it actually occurred.

A bootstrap that ends with useful skill files but no usable installation path is incomplete.

## Output Format

```markdown
# Skill Bootstrap Result

## Evidence coverage
- Available and inspected: ...
- Available but out of scope / not inspected: ...
- Partial: ...
- Unavailable: ...

## Usage findings
...

## Skill decisions
| Need | Current state | Reference | Decision | Benefit | Validation |
|------|---------------|-----------|----------|---------|------------|

## Existing skills to refine
...

## New skills justified
...

## Do not create
...

## Comparative reference findings
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

### Normal case

A user has months of accessible work showing repeated repository reviews, evidence-based issue creation, and recurring corrections about authority boundaries. Bootstrap identifies a stable repo-review skill, finds partial coverage in the existing corpus, recommends SUPPLEMENT rather than replacement, produces a profile carrying the evidence/approval defaults across hosts, then installs it directly on a local host or packages it for the user's actual target.

### Web/UI installation case

A user is working in a web application that supports skill upload but the agent cannot click the user's account UI. Bootstrap creates the required upload package, reports `READY TO UPLOAD`, gives the shortest current official UI path in numbered steps, names the exact file to select, and provides one test prompt. It does not call the skill installed until the upload actually occurs.

### Edge case

A new user provides only one short conversation. Bootstrap inventories the current task, reports that history/memory are unavailable, suggests a small provisional set of catalog skills, and declines to infer a broad personal skill architecture until more evidence exists. Any selected skill still receives a concrete installation handoff for the known target host.

### Privacy edge case

A host has email and calendar connectors, but the user only asks the agent to learn from their current workspace and interaction history. Bootstrap does not inspect email or calendar. It records those sources as available but out of scope and proceeds with the smaller evidence set.

### Do not activate

The user asks, "Run the fact-check skill on this article." A specific skill is already named; execute that skill rather than running a whole ecosystem bootstrap.
