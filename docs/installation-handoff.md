# Skill Installation Handoff

`skillz` does not install skills. This document tells an external host agent how to hand off a portable skill truthfully when the user wants to use it elsewhere.

The repository remains passive. Any packaging, upload, filesystem write, API mutation, verification, or trigger test is performed by the external agent using capabilities supplied by its host and only with the authority that host normally requires.

## The simple rule

For each requested target host, the external agent should end in exactly one truthful state:

- `INSTALLED + VERIFIED`
- `INSTALLED, VERIFICATION PENDING`
- `READY TO UPLOAD`
- `USER ACTION REQUIRED`
- `BLOCKED: HOST DOES NOT SUPPORT SKILLS`
- `BLOCKED: INSTALLATION METHOD NOT ESTABLISHED`

Do not claim installation because a skill exists in this repository, because a package was prepared, or because another surface of the same product supports skills.

## Required handoff information

For every requested target, record only what can be established from current evidence:

- host/product and surface;
- selected portable skill artifact;
- installation or upload mechanism, if established;
- whether the external agent can perform the mutation;
- destination/path/UI flow only when verified from the active host or authoritative current documentation;
- permissions or plan constraints that materially affect installation;
- resulting completion state;
- verification evidence already obtained, or the exact remaining verification step;
- one next user action when user action is required.

If a current destination, API, UI path, package shape, or product capability cannot be established, say so rather than inventing it.

## Transfer modes

### DIRECT WRITE

Use when the external host agent can write to a destination recognized by the target environment.

1. Establish the target's actual supported skill location or installer from current evidence.
2. Confirm the selected artifact and any host adaptation required.
3. Preserve portable behavior, provenance, and applicable licensing.
4. Obtain any approval the host normally requires for mutation.
5. Write using the external host's own filesystem or repository capability.
6. Read back or otherwise inspect the destination when possible.
7. Run a representative trigger check when practical.
8. Report `INSTALLED + VERIFIED` only when both installation and verification actually occurred.

### API INSTALL

Use when the target exposes a current supported API and the external agent has an authorized connection.

1. Verify that the current API supports the intended skill operation.
2. Establish the required request/package shape from authoritative current information.
3. Confirm mutation authority.
4. Create or upload the skill through the host-provided connection.
5. Read back the resulting object/version when the API permits.
6. Verify representative behavior when practical.
7. Record the returned identity/version without exposing credentials.

Never ask the user to expose secrets merely to make a transfer convenient.

### UI UPLOAD

Use when the target requires a human UI action.

1. Prepare the exact artifact the current target expects when the external host can create files.
2. Verify current UI guidance from authoritative documentation when possible.
3. Give one action per numbered step.
4. Name the exact artifact the user should choose.
5. State what successful upload/enablement should look like.
6. Give one small representative test.
7. Use `READY TO UPLOAD` or `USER ACTION REQUIRED` until the upload actually occurs.

### PORTABLE HANDOFF

Use when installable-skill support is absent or cannot be established.

1. Preserve the portable skill in its canonical `SKILL.md` form, with only necessary references/assets.
2. State that installation support is unavailable or unestablished for the requested target.
3. If useful, describe a separately labeled host adapter such as project instructions or reference files.
4. Do not call that adapter an installed skill when it is not one.
5. Keep the portable source suitable for another compatible host.

## Portable artifact shape

Prefer the smallest artifact that preserves the behavior:

```text
<skill-name>/
  SKILL.md
  references/        # only when required
  scripts/           # only when the portable skill itself legitimately requires them
  assets/            # only when required
```

Third-party source repositories under `skills/sources/` are reference sources. Do not mutate them in place to create a host-specific installation package. Create a separate adapted artifact when adaptation is required.

## Host-specific information is volatile

Product support, menus, API shapes, package formats, installation locations, and plan restrictions change over time.

Therefore this repository does not encode current product-specific installation claims as permanent truth. At transfer time, the external agent should prefer, in order:

1. capabilities and documentation exposed by the active target host;
2. current authoritative vendor documentation;
3. current verified repository or API documentation;
4. a truthful `INSTALLATION METHOD NOT ESTABLISHED` result when the mechanism cannot be established.

Do not convert an old example into a current assertion merely because it remains in history.

## Human-facing instructions

When user action is required:

- separate what is already complete from what remains;
- use one action per numbered step;
- use exact labels only when verified;
- identify the exact artifact;
- state what success looks like;
- end with one representative test;
- avoid presenting multiple routes unless the primary route is blocked.

Example structure:

```markdown
## Installation

Status: READY TO UPLOAD
Target: <verified target>
File: <artifact>

### Do this now
1. <verified action>
2. <verified action>

### Then test it
<one representative trigger>

### You are done when
<observable success condition>
```

## Multi-host transfer

When the same fitted behavior is requested on several hosts:

1. Keep one canonical portable skill source.
2. Establish support independently for each target surface.
3. Create host adapters only where required.
4. Keep a separate completion state for each target.
5. Never infer that installation on one product surface propagates to another.

## Security and authority

- Installation and upload are mutations.
- The external host's normal authority rules apply.
- Never silently enable organization-wide sharing or broaden workspace permissions.
- Never package secrets, private keys, tokens, cookies, or unrelated private data.
- Review third-party executable content before transferring or enabling it when execution is part of the target skill.
- Recommendations and reference material are not authorization.

## Relationship to `skillz`

`skillz` supplies passive skill artifacts, provenance, verification evidence, source context, and transfer instructions.

It owns no installer, synchronizer, packaging process, filesystem deployment mechanism, API client, trigger runner, or validation service. The external agent performs any requested action and records only evidence that actually exists.