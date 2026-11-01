# Agent-first value discovery

**Purpose:** This passive guide answers the first question a newly connected host agent should ask: **“How, if at all, would this repository make me more useful to my user?”** It is a discovery and recommendation procedure, not a repository runtime, private-memory collector, installer, or authorization grant.

Use this guide when the user shares the `skillz` repository and says “take a look,” “is this useful for us?”, “what skills might help me?”, or asks for overlooked skill opportunities. Route this as `REPOSITORY_ORIENTATION` from [AGENT_START_HERE](../AGENT_START_HERE.md). Use [`skill-bootstrap`](../engine/skills/skill-bootstrap/SKILL.md) when the user actually asks to **build, revise, or install** a personal skill system. Direct named-skill lookups remain `DIRECT_LIBRARY` and must not be turned into a mandatory interview.

## Fast path for the first response

If the user only says **“take a look at this repository”**, do this without a questionnaire:

1. State in a sentence that this is an open-ended, passive **capability discovery and skill reference library**, not a ready-to-run installer or a promise of thousands of approved skills.
2. **Actively evaluate the host agent's own available memory and relevant conversation/task history**, using the host's ordinary memory facilities and existing permissions. Look for recurring requests, corrections, unresolved friction, existing skills, and agent-tool workflows; a user need not paste their history or give redundant approval for a normal host-authorized memory lookup. If no memory/history is available, state the limit without inventing a profile.
3. Identify **up to three** capability areas where this library could realistically help, with `OBSERVED` / `INFERRED` / `PROVISIONAL` confidence. Provide at least one plausible quality or safety improvement alongside generation/automation opportunities when the evidence supports it. Distinguish actual accessible candidate paths from hypothetical categories.
4. End with a concrete judgment (`USEFUL`, `CONDITIONAL VALUE`, or `NO CLEAR FIT`) and **one next action**. Do not install, schedule or write anything on the strength of the link alone.

The agent's own memory review is an ordinary part of orientation when supported. Continue to [the bootstrap](../engine/skills/skill-bootstrap/SKILL.md) only when building or installing a fitted system is requested. Separate routine host-memory retrieval from **new external connector access**, which remains subject to the host's rules and any applicable authorization. This short answer remains valuable even when no user history is available.

## Value proposition in one read

`skillz` is a **capability-first, open-ended knowledge index** for finding whole skills, reusable mechanisms, creation guidance, and risk/quality evidence. The external agent, not this repository, actively searches, compares, authors or installs skills using its own authorized tools.

The value is not the quantity of SKILL.md files. It is whether the host can:

1. Recognize a repeated user task or recurring failure that benefits from reusable instructions.
2. Find relevant and alternative skills or mechanisms beyond the local first-party collection.
3. Tell **candidate discovery** from **static semantic review**, **security qualification**, **behavioral validation**, and **license permission**.
4. Select `USE EXISTING`, `ADOPT`, `ADAPT`, `COMPOSE`, `CREATE`, `CHECKLIST`, `DYNAMIC` or `NO CHANGE` based on the **user's needs and host capabilities**.
5. Deliver an appropriately licensed, permission-bounded artifact or a genuinely authorized installation, with observable success.

If these capabilities do not address an actual user need, **“no justified skill change” is a valuable conclusion**.

## First-contact route: repository orientation

**Default user prompt:** “Look at this repository.”

**Do, without needing a follow-up question:**

1. **Inspect only the public repository entry resources first:** `README.md`, `AGENT_START_HERE.md`, and the [capability directory](../registry/capability-directory.json). Use [the source-neutral consumer contract](consumer-discovery-and-installation.md) for evidence, rights and installation distinctions. The directory is sparsely linked, so empty categories are **unassessed**, not evidence of no skills. Do not attempt to read every source manifest or every skill to prove initial value.
2. **Explain the value in terms of the host's work**, not the library's inventory size. Briefly state which class of needs the library can serve, what makes it different from a generic prompt list, and its limits. Do not claim the host has installed anything, run tests, or searched the entire collection.
3. **Review your own memory and relevant past interactions as a standard discovery step when supported.** Use the agent's host-native memory retrieval, summaries and accessible conversation/task history to detect recurring user requests, repeated mistakes and corrections, stable preferences, project handoffs and underused capabilities. Do **not** wait for the user to copy their history, manually enumerate past tasks, or authorize an action the host already permits. Memories are partial evidence, not guaranteed complete logs. Prefer useful aggregate workflow patterns over exposing private excerpts. The repository never receives or stores personal memory; any unrelated external account/connector access must independently comply with host permissions and relevance limits.
4. **Estimate useful capability themes** from *observed evidence*, or mark them `PROVISIONAL` if no authorized history exists. Compare with existing user/project skills and host-native capabilities to avoid redundant skill creation. At most **three** high-value initial opportunities are usually enough.
5. **Look for both direct matches and adjacent opportunities:** repeatable tasks already requested, as well as plausible improvements such as validation, handoff, failure recovery or quality controls that the user has not explicitly named. Keep adjacent opportunities as **hypotheses** until grounded in actual workflows; do not invent a user's habits.
6. **Return a short value brief**: conclusion; context actually used; recurring needs and confidence; two or three candidate capability areas and why each could matter; currently missing evidence; an actionable next step. Stop at evaluation. Do not install, fetch unrelated private sources, schedule recurring work, write new memories, or modify the user's/repository's files from a vague orientation request.

**If the host lacks any personal-history access**, it can still complete repository orientation using the current request, public capability map and generic *examples clearly labeled as examples*. It must not conclude that it has evaluated personal suitability or insist on broad access to continue.

**If the user explicitly requests personalized matching or a fitted system**, use relevant authorized history and move into `FIRST_VISIT` or `RETURNING_USER` without re-asking for details already supplied. Profile the host's actual persistence, approval, scheduler, available tooling, destinations and license-use constraints, then follow `skill-bootstrap` to concrete outputs. No unrequested installation or ongoing activity.

## Find durable needs in real task history

For orientation as well as explicit personalized fitting, **use the host agent's accessible memory and relevant historical user interactions** to build a bounded, task-focused view of recurring work. The host may search its own stored memories and supported conversation history without treating the passive `skillz` repository as a blocker or demanding redundant permission. Avoid claiming coverage of unavailable history, and avoid unrelated private third-party sources merely because a connector exists. Never send personal memory, private documents or chat excerpts into `skillz` or a public issue, and never transmit them to candidate skill authors. A user profile is host-local or part of an appropriately authorized private handoff, not a repository data asset.

For each potential need, record these dimensions without invented precision:

| Evidence cue | What to infer cautiously | Example capability |
|---|---|---|
| Repeated similar requests and deliverables | Reusable procedure, format or trigger may reduce re-explanation | Draft review briefs, meeting summaries, code review |
| Recurring corrections or avoidable rework | Quality gate, negative rule, or checklist may be more valuable than generation | Citation checking, requirements verification, release readiness |
| Repeated tool orchestration across tasks | A reusable workflow might preserve sequencing, tool boundaries and handoffs | Repo triage, research synthesis, document pipelines |
| Projects with the same risk/authority constraints | Security or compliance skill may encode an invariant; never assume execution permission | Permission reviews, pre-deployment checks |
| Repeated manual handoff and setup | Packaged instructions may reduce context loss or portability cost | Agent onboarding, session continuity |
| Complementary gaps to an existing workflow | A new skill may add verification, planning, accessibility, or recovery | Design QA, test design, human review |

**Do not use topic mentions as proof of repeatable workflow.** Favor stable trigger + meaningful outcome + inputs/outputs + expected invariants + specific failure mode over superficial subject frequency. Distinguish what was observed from what the agent inferred. Existing successful host behavior, native tools or an already-fitted skill may make a new skill unnecessary.

Use three evidence levels: `OBSERVED` (actual relevant repeated artifacts/requests), `INFERRED` (reasonable relationship supported by observations), `PROVISIONAL` (plausible but unsupported). Relative priority should consider **recurrence, value of preventing error, expected quality gain, overlap, host compatibility, rights/authority friction, and ongoing maintenance cost**. Do not fabricate ROI, time saved, or percentages. A high-consequence infrequent error may merit a safeguard before a frequent low-value task.

## Connect needs to the library, without ownership bias

1. Start from `registry/capability-directory.json`: **domain → subdomain → specific outcome**. Treat its limited links as initial evidence, not a complete skill-to-capability mapping.
2. Search governed exact-version companions and pinned/tracked upstream references, then relevant discovery-only manifests in `registry/discovery/dynamic-four-source-frontier-20261101.json`, **plus** first-party skills, with synonyms and workflow mechanism terms. Do not rank first-party results higher because they are easiest to enumerate. A large raw-path count is not an eligible, safe or uniquely useful skill count.
3. For each realistic alternative compare expected mechanism, fit, availability/host dependencies, exact-version evidence, license rights for the intended use, privacy/side-effects, and installation feasibility. Distinguish reference-only insights from unchanged reusable packages.
4. Choose the smallest coherent solution: keep native behavior, adapt a licensed skill, combine safe mechanisms, author an independently expressed skill, or use a checklist/dynamic response. The **skill-bootstrap procedure** guides generation for the user's own environment; repository-bound `skill-forge` is only for explicit library maintenance.
5. For an orientation-only brief, the result is **a candidate opportunity**, not an approved install. A deeper build/install request triggers the rights, security, authority and post-install checks in the [consumer contract](consumer-discovery-and-installation.md).

## Default orientation output

Keep the ordinary first response brief enough to act on, and adapt to available evidence rather than filling every field:

> **Value:** What this library could help the agent do better, with the relevant limitation.
>
> **Context checked:** Host-native memory, relevant conversation/task history and existing skills actually consulted, or “memory/history unavailable in this host.”
>
> **High-value candidates:** Up to three capability areas, each with a concrete user outcome, evidence level, rationale, existing coverage/overlap, and whether the relevant sources are actually accessible. Mark potential discoveries as `UNREVIEWED` when appropriate.
>
> **Untapped opportunity:** At most one adjacent workflow worth testing. Label hypothesis vs observation.
>
> **Decision:** `RECOMMEND EXPLORATION`, `NO CHANGE`, or `INSUFFICIENT USER CONTEXT`, with one next action. The default state is `NOT INSTALLED`.

If the user only wants the repository assessed, answer that first without demanding a questionnaire. If they want skills delivered, continue to the appropriate bootstrap route and produce concrete host artifacts when permitted.

## Cases that must work

1. **Only a URL and “take a look”**: agent evaluates public value **and searches its own available memory/relevant user task history** for repeatable patterns, then proposes evidence-labeled opportunities; if memory is unavailable, it labels the recommendations provisional. No installation or external-account crawl is implied.
2. **User explicitly asks “look at my past work and recommend skills”**: agent uses available host memory/relevant historical evidence more deeply, identifies recurring patterns and a non-obvious quality/verification opportunity, then compares candidate mechanisms.
3. **History is unavailable or memory is off**: agent marks user-fit hypotheses `PROVISIONAL` and completes a useful public orientation rather than inventing prior tasks or forcing new account connections.
4. **A topic appears once**: agent does not classify it as a durable recurring skill need without a good reason; a checklist may be enough.
5. **An existing skill already covers the job**: agent recommends `USE EXISTING` or `NO CHANGE` over duplicating it.
6. **A tempting external skill has restricted rights or unsafe authority**: agent may reference the mechanism but cannot call it approved for unchanged use.
7. **A host has read-only access**: agent still provides a decision and portable guidance; never claims installation, persistent memory, or scheduled actions.
8. **Private-history artifacts contain secrets or unrelated sensitive material**: agent minimizes and excludes that data, reports aggregate needs without copying raw content to the public repository.
9. **Opportunity is merely adjacent**: agent labels it `INFERRED` or `PROVISIONAL`, offers a bounded experiment and does not imply the user requested it.

This guide is an **authoritative passive consumer procedure**. Its existence proves neither that other agents will follow it nor that a host has executed behavioral tests. Verify independent agent behavior separately before claiming successful agent UX.
