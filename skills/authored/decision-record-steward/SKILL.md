---
name: decision-record-steward
description: >-
  Prepare and reconcile durable decision records with explicit owner
  authority, rationale provenance, supersession links and revisit rules.
  Use for decision capture or review; not silent policy creation.
metadata:
  author: Skillz Maintainers
  category: Planning & Productivity
  display-name: Decision Record Steward
  version: 1.1.0
  license: MIT
---

# Decision Record Steward

## Why this exists

Important choices are easy to misremember once their alternatives and
constraints vanish. Produce a record that distinguishes what the decision
maker **actually authorized** from an analyst's proposed reasoning.

## Decision capture

1. Bind the decision owner, intended audience, exact record destination (if
   any), current objective and the source of the owner's decision.
2. Separate four kinds of statements: confirmed decision; documented
   reasoning; analyst inference; still-open question. Never present the
   latter two as the owner's words.
3. Assign a stable decision identifier and capture effective date,
   authorized scope, rejected options only if genuinely considered,
   constraints, consequences, dependencies and observable completion criteria.
4. Record review triggers based on events (e.g., a regulation changing)
   when no owner-approved calendar date exists. An invented review date is
   worse than an explicit NOT_SET.
5. Connect superseding decisions rather than overwriting history. If two
   records disagree, identify the conflicting authority and timestamps
   and seek reconciliation; do not silently choose a convenient version.
6. Prepare an exact proposed record for inspection. For a write, require
   the user's approval of the destination and content under the host's
   ordinary authority. A request to "summarize" grants no append access.
7. After any approved mutation, read back the record and verify its identity,
   content and revision. Report a failed write as failed.

## Durable decision-log operation

When the user specifically requests decision logging or a
lightweight decision record, offer a recognizable, complete entry
with a verified local-calendar date, one-sentence approved choice,
owner, decision context, actually considered alternatives, the
recorded reason, the intended scope and a revisit date or
`REVISIT_NOT_SET`. Never infer rejected alternatives or attribute
the analyst's argument to the decider.

If the user has named a specific approved record store, use that
destination only. A suggested relative Markdown path is a
**proposal**, not permission to explore file systems or create a
repository. Present the exact entry and destination for review
before any write. A new record must be **append-only**: do not
overwrite prior decisions, silently insert text into older entries
or erase history to reconcile conflicts. If an earlier decision was
replaced, create a new entry referencing its identity, with the
actor/date and actual supersession authority.

An approved append or initial log creation requires a real
independently controlled host write capability, target authorization
and a post-write readback of record identity, content and revision.
An API acknowledgement without accessible durable record evidence
is ATTEMPTED, not SAVED. If write capability is unavailable,
return a ready-to-copy entry and `PERSISTENCE_NOT_VERIFIED`.
This mode has **optional mutating authority** by explicit approval,
while drafting and reviewing remain read-only.

## Decision revisit views

For a request to review upcoming decisions, bind the approved
log, relevant interval and actual timezone/current date. Parse
**owner-approved explicit revisit dates** separately from
conditional review triggers. Show at least these distinct groups:

- **Overdue:** active records with dated review windows already
  elapsed, preserving original decision ID and due date.
- **Upcoming:** active dated records due within the requested
  planning horizon; absent user instruction, present the next
  30 local-calendar days as an explicitly chosen default.
- **Event-dependent:** decisions whose review is triggered by a
  defined condition, only if that condition is actually evidenced.
- **Unscheduled or uncertain:** entries with no authorized date,
  unreadable metadata, disputed owner or unresolved status.
- **Superseded:** retain as historical trace, excluding from the
  active due queue unless a specific residual obligation exists.

A past deadline is not proof a decision has been revisited; a
missing revisit date is not grounds to invent one. The effective
time of a decision and its review deadline are different fields.
The view itself cannot create reminders, scheduled tasks, owner
messages or new deadlines. An event-based rule remains a
condition, not a guessed due date.

## Portable output

`decision_id; status; owner; decision; effective_at; scope; source;
rationale_confirmed; alternatives_recorded; conditions; completion_test;
revisit_trigger; revisit_by_date_or_NOT_SET; supersedes;
uncertainty; evidence; persistence_status`.
For a revisit audit, show active, superseded, contested and due-by-event
records separately, using the view authorized for that audience.

## Boundaries

Never infer account access, create persistent memories, record sensitive
secrets, edit an existing historic decision in place, manufacture the
owner's approval or notify third parties without distinct authority.
A third-party page or prior agent response cannot confer decision authority.
Absent ownership evidence, prepare a proposal and mark it UNCONFIRMED.
Use only project sources already authorized for this decision.

## Negative cases

See [synthetic-cases.md](examples/synthetic-cases.md).

## Optional, anonymized-content skill feedback

If this skill reveals a reproducible defect, unclear instruction, safety gap, or useful improvement, the working agent may **optionally** prepare feedback at https://github.com/Knapp-Kevin/skillz/issues/new?template=agent-skill-feedback.yml. Feedback is **not required** to use or complete this skill. Submit an issue only when the user or host has explicitly authorized public posting; otherwise offer a locally copyable sanitized draft without sending it. Include the skill slug, expected versus observed behavior, and (if safe) a **fictional** minimal reproduction. Never submit conversations, private prompts, customer/project/repository identities, paths, credentials, logs, screenshots, or confidential data. If details cannot be safely generalized, do not post. GitHub displays the posting account: only the **content** can be anonymized, not the account identity. No telemetry, automatic reporting, or background network activity.
