# First-contact discovery for a consuming agent

This is a **passive walkthrough**, not a runnable installer or hard repository compliance gate. For FIRST_VISIT and RETURNING_USER use [AGENT_START_HERE](../AGENT_START_HERE.md) and the canonical [skill-bootstrap](../engine/skills/skill-bootstrap/SKILL.md). For an explicitly named skill or simple comparison, take the lighter DIRECT_LIBRARY route without forcing an interview.

## 1. Route and establish authority

Choose the bootstrap route before selecting skills. Check the current user's instruction and the host's actual tool, storage, and approval capabilities. Never interpret access to this public corpus as consent to modify the user's environment, collect private data, run commands, schedule tasks, or mutate this repository.

Answer four axes with **yes / no / unknown**, except for authority:

| Axis | What to establish | Consequence |
|---|---|---|
| Persistence | Can this host reliably read/write approved durable state across sessions? | Without it, return carry-forward text in the response instead of promising remembered state |
| User in the loop | Can the host request and receive actionable approval in the actual workflow? | Without it, consequential actions need to remain plans/handoffs unless separately authorized |
| Scheduling | Does this host have a real scheduling capability and permission to use it? | Without it, no background monitoring or scheduled follow-up claims |
| Side-effect authority | **read-only / approval-gated / autonomous / unknown** for the specific action, resource, destination, scope, and current instruction | Unknown defaults to no mutation; approval must be specific to the action and destination |

A capability's technical availability is **not** authorization. Before any external write, disclosure, communication, identity change, money-bearing operation, or other consequential action, the host must establish authorization for the exact action, target resource, destination or recipient, data scope, and expected effects. `autonomous` describes a host capability, never blanket user consent. If any material dimension is unknown, remain read-only and ask for scoped approval or return a plan. Never copy secrets or unredacted sensitive data into the receipt. A persistent host with scheduling can still be limited to read-only. A single-session host can still provide a complete portable skill.

## 2. Discover demand before looking at names

Ask or infer from relevant, authorized evidence only:

1. What goals and recurring tasks cost the operator time or produce avoidable mistakes?
2. Which tools and workflows are *actually* used? What access and read/write limits apply?
3. What cadences exist, if any? Which ones have been explicitly authorized?
4. What failure, privacy, security, cost, or quality controls must survive adaptation?
5. How will success be verified, and where can finished artifacts live?

Stop once further questioning is unlikely to change a decision. Mark unsupported inferred needs `provisional`. Avoid collecting unrelated private history.

## 3. Map needs to categories, then candidates

Start with [the current category catalog](../INDEX.md) and [machine-readable snapshot](../index.json). Search whole skills and any required supporting components, not names alone. Compare the user's existing skills, first-party `skills/`, host-native abilities, governed third-party records, and relevant reference-only packages. Do **not** install or copy a reference corpus simply because a package exists.

For each candidate, write down its mechanism, fit, required tools, authority/side effects, provenance, exact-version semantic state, applicable package-security state, and license. If `verified` is merely semantic, do not imply security or behavioral testing. Use `ADOPT`, `ADAPT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, `CHECKLIST`, `DYNAMIC`, or `NO CHANGE` only after comparing with existing coverage.

Defer first-contact deep provenance dives for irrelevant packages, full registry enumeration, and installation of anything not selected.

## 4. Derive activation behavior from the host

| Observed host constraint | Allowed interpretation |
|---|---|
| No persistence | Use in-session or portable output; no memory or saved-state claim |
| No scheduler | Trigger only on request or host-native explicit event; no invented background behavior |
| No interactive approval | Consequential actions remain proposed unless there is already sufficient specific authorization |
| Read-only access | Analyze and draft only, even if a skill mentions external operations |
| Persistent, scheduler-capable and approval-gated | Recurring work may be proposed; creation/execution still requires the user's instruction and bounded approval |

Avoid a universal static `runtime-tier` field on all 44 skills. A consuming host can derive appropriate activation using this profile without making false promises across host types.

## 5. Portable receipt template

The receipt records decisions, not permission or evidence of installation. Save it in the **host** only when supported and authorized. Otherwise include it inline or as a handoff. Do not write it back into `skillz`.

```yaml
route: FIRST_VISIT # FIRST_VISIT | RETURNING_USER
host_capabilities:
  persistence: unknown # yes | no | unknown
  user_in_loop: unknown # yes | no | unknown
  scheduling: unknown # yes | no | unknown
  side_effect_authority: unknown # read-only | approval-gated | autonomous | unknown
needs:
  - capability: <material user need>
    evidence: <observed, or provisional>
shortlist:
  - skill: <name / path>
    disposition: <ADOPT | ADAPT | COMPOSE | NO CHANGE | ...>
    semantic_review_state: <verified | rejected | pending | not-applicable, with exact-version reason>
    package_security_state: <passed | failed | incomplete | not-run | not-applicable, with evidence revision>
    behavioral_validation_state: <validated | failed | not-run | not-applicable, with evidence>
    authorization: <action / resource / destination / data scope / approved-or-pending>
    activation: <request-driven / host event / separately authorized scheduled>
    destination: <user host / portable handoff>
deferred: []
installation_state: not-run # do not infer from selecting a skill
completion_evidence: <what actually passed, or not-run>
next_action: <single action or none>
```

## 6. Definition of done

- Route and authority established with material unknowns shown.
- Durable needs and minimum viable shortlist map to actual capabilities, not popularity.
- Whole-skill and component overlap checked; reuse eligibility not exaggerated.
- Action boundaries, side effects, host prerequisites, and verification named.
- Selected artifacts prepared for the user's host or portable handoff; installation truthfully stated.
- A return visit can conclude `NO CHANGE`.

## Examples of failure to prevent

- **One-shot chat:** Do not tell the user "I'll remember and monitor" when there is no persistent memory or scheduling.
- **Approval-gated host:** A skill mentioning deployment does not authorize production changes.
- **Reference-only vendor skill:** A favorable semantic review without exact-version package-security evidence does not authorize unchanged adoption.
- **Direct library lookup:** Do not demand a capability interview just to show or compare a named skill.
- **Consumer says skills were adopted elsewhere:** Require an observed consuming repo/version/date before claiming cross-repository usage; the user's stated impression alone is not adoption evidence.

Dated material changes to the corpus and governance are summarized in [CHANGES.md](../CHANGES.md); registered exact-version evidence remains canonical in `registry/`. The host can inspect changes without installing a synchronizer.
