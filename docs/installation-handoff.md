# Skill Installation Handoff

A bootstrap is not complete when it has merely identified or created good skills.

It is complete when the user knows exactly how to get those skills working on the agent or application they actually use.

This document defines the installation handoff contract for `skill-bootstrap` and other skill-generation workflows.

## The simple rule

At the end of the process, the agent must do one of these three things:

1. **Install it** — if the host lets the agent write or install skills and the user has authorized the change.
2. **Prepare it for upload** — if the host requires the user to upload or enable the skill in a UI.
3. **Explain the blocker** — if the current host cannot use the skill directly.

The user should never be left with a folder of files and the unexplained instruction "install this."

## Installation is part of the deliverable

Every bootstrap result must include an **Installation** section for each target host or surface.

For each target, report:

- host/product name
- surface: desktop app | web app | CLI | IDE | API | local agent | other
- detected installation mode
- whether the agent can perform the installation itself
- files/package produced
- exact destination or UI path when known
- permissions or plan requirements that matter
- installation status
- verification result or verification steps
- the user's next action, if any

## Installation modes

Classify each target as one of:

### DIRECT-WRITE

The agent can write the skill into the host's recognized skill directory or repository.

Examples include local coding agents and CLI hosts where the agent has filesystem access.

Procedure:

1. Identify the host's actual skill location or supported installer.
2. Validate the generated skill before writing it.
3. Show the intended destination and action.
4. Obtain any approval required by the environment.
5. Write/install the skill.
6. Verify that the expected files exist at the target.
7. Run a simple trigger test when possible.
8. Report **INSTALLED + VERIFIED** only if both installation and verification actually occurred.

If the repository's `skill-sync` supports the target, prefer it over inventing another copy mechanism.

### API-INSTALL

The host exposes a supported API for creating or uploading skills and the agent has an authorized connection to that API.

Procedure:

1. Confirm that the current API supports skills.
2. Confirm the required package shape.
3. Validate the skill locally where possible.
4. Ask for authorization if the operation creates or changes remote state.
5. Upload/create the skill.
6. Read back the created skill or version when the API permits.
7. Run or describe a trigger test.
8. Report the resulting identifier/version without exposing credentials.

Never ask the user to paste an API key into chat when a safer authenticated connection is expected.

### UI-UPLOAD

The host requires a human to use its graphical interface.

The agent must make the human part as small as possible.

Procedure:

1. Produce the exact upload artifact the host expects when the environment can create files.
2. Name the artifact clearly.
3. Give numbered click-by-click instructions using the host's current official documentation when web access is available.
4. Put **one action per numbered step**.
5. Avoid unexplained technical terms.
6. Tell the user exactly which file to choose when the file picker opens.
7. Explain what success should look like.
8. Give one tiny test prompt to confirm the skill works.

If the agent cannot create the upload artifact, show the exact folder/archive structure and tell the user how to create it.

### PORTABLE-HANDOFF

The target host does not currently support installable skills, or its supported mechanism cannot be established.

Do not pretend a file upload, custom instruction, project file, or prompt is equivalent to a real installed skill.

Instead:

1. Preserve the skill in the portable Agent Skills / `SKILL.md` form when possible.
2. Explain that this host cannot currently install it as a skill, or that support was not established.
3. Offer the closest supported binding separately, such as project instructions or reference files, only if it preserves the important behavior.
4. Mark that binding as an adapter, not the canonical skill.
5. Keep the portable skill ready for another compatible host.

## Current host examples

These are examples, not eternal truths. Product UIs change because apparently buttons also require a migration strategy.

When web access is available, verify current official instructions before giving click paths.

### Claude web / desktop

As of 2026-08-28, Anthropic documents custom skill upload through **Customize → Skills**. A custom skill is packaged as a ZIP containing the skill folder as the ZIP root. After upload, the skill can be enabled and tested.

Source of truth at installation time: Anthropic Help Center documentation for custom Skills.

### ChatGPT web / desktop

As of 2026-08-28, OpenAI documents Skills in the **Plugins → Skills** area for eligible accounts. Skills can be created or uploaded from the Skills interface. Availability and workspace permissions vary by plan and workspace.

Source of truth at installation time: OpenAI Help Center documentation for Skills in ChatGPT.

Do not substitute GPT knowledge files or Project instructions and call that an installed Skill when the account does not expose Skills.

### Claude Code / local coding agents

Use the host's supported local skill directory or installer. For this repository, `skill-sync` already supports Claude Code user skills plus several markdown-host repository layouts.

The exact filesystem destination must be resolved from the active host rather than assumed from an example path.

### OpenAI API

As of 2026-08-28, the OpenAI API exposes Skills resources that accept a directory upload or a ZIP file. Use the API only through an authorized connection and treat creation/version updates as remote mutations.

## Packaging contract

The installation handoff should produce only what the user needs.

For each selected skill, prefer:

```text
<skill-name>/
  SKILL.md
  references/        # only when needed
  scripts/           # only when needed
  assets/            # only when needed
```

When a host requires ZIP upload, also produce:

```text
<skill-name>.zip
  <skill-name>/
    SKILL.md
    ...
```

If the target host expects a different shape, generate a host adapter while preserving the portable canonical source.

## Beginner-facing instruction rules

Installation instructions are written for a user who may have never opened a terminal or installed an AI skill before.

Required:

- one action per numbered step
- short sentences
- exact button/menu/file names where verified
- no unexplained acronyms
- no optional branches mixed into the main path
- clearly mark anything the user can skip
- show the filename they should see
- state what success looks like
- end with one test prompt

Bad:

> Deploy the portable bundle to your host's skill registry and validate invocation.

Good:

> 1. Open Claude.
> 2. Click **Customize**.
> 3. Click **Skills**.
> 4. Click the button to add a skill.
> 5. Choose `repo-review.zip` from your Downloads folder.
> 6. Turn the new skill on.
> 7. Type: `Review this repository for documentation drift.`

If a current UI label cannot be verified, say that clearly instead of inventing a button name.

## ADHD-friendly handoff

The final handoff must separate **what is already done** from **what the user still has to do**.

Use this structure:

```markdown
## Installation

Status: READY TO UPLOAD
Target: Claude
File: repo-review.zip

### Do this now
1. Open Claude.
2. Open Customize → Skills.
3. Upload `repo-review.zip`.

### Then test it
Type: "Review this repository for documentation drift."

### You are done when
Claude shows the skill as enabled and uses it for the test request.
```

Do not give the user three different installation routes unless the primary route is blocked.

## Multi-host installs

When the user wants the same skill system on several hosts:

1. Keep one canonical portable skill source.
2. Produce a separate installation status for each host.
3. Generate host-specific adapters/packages only where required.
4. Do not assume that installing on one surface installs it everywhere.
5. Verify each host independently.

## Security and authority

- Installation is a mutation.
- Automatic installation requires the authority expected by the host/environment.
- Never silently enable organization-wide sharing.
- Never change workspace permissions merely to make installation easier.
- Never upload secrets, private keys, tokens, cookies, or unrelated private files inside a skill package.
- Review third-party scripts before installing or enabling them.

## Completion states

Use exactly one per target:

- `INSTALLED + VERIFIED`
- `INSTALLED, VERIFICATION PENDING`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

A bootstrap result without an installation state for every selected target host is incomplete.
