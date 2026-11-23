# Private local preference boundary

This **public** directory contains only a shareable JSON schema and
neutral rules. Do not place personal overlay values, real task logs,
individual health information, account identifiers or source identity
here. This package does not create, discover, read or mutate a
preference store.

## Current-run settings

The standalone CLI optionally accepts:
- choice_count: **2 by default**; permitted 1, 2 or 3. Showing three
  requires a clear user preference; never force more choices.
- pace: balanced by default; short-sprints may favor eligible tasks
  taking at most 30 minutes but **cannot** change the hard safety or
  owner-confirmed imminent-deadline lane.

An agent may additionally adapt written explanation length or suggested
first-slice duration **within safe, authorized task acceptance** in the
current conversation. These are preferences, not objectively better
canonical algorithms. A different user may choose differently.

## Optional future storage (not implemented here)

Only after genuine user opt-in and a host with user-private, revocable,
version-scoped storage may an agent propose an overlay conforming to
[schema.json](schema.json). There is **no active persistence or
background learning mechanism**. The sample schema carries no
identity, history, prompts, source paths, risk bypass, script, network
destination or authorization change. A profile missing or invalid
must fall back to the neutral defaults; no private store should be
created as a side effect of merely using the skill.

Always give a user a way to change or revoke a stored preference when
storage actually exists, without needing to delete public source.
Current direct user instructions override older compatible local
preferences; canonical correctness, security and approval gates are
not adjustable.

**Split feedback:** a reproducible universal scoring/graph defect may
be proposed for maintainer-reviewed canonical correction with
source-blind sanitized evidence; an individual's preference remains
private and optional. Neither complaint frequency nor the reporter's
identity grants technical authority or qualifies a regression.
