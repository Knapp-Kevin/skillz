# First-contact discovery for a consuming agent

This is a **passive walkthrough**, not a runnable installer or hard repository compliance gate. For a generic “look at this repository” request take the lightweight [REPOSITORY_ORIENTATION / value-discovery route](agent-value-discovery.md) **before** attempting a full fitted-system build. For explicit FIRST_VISIT and RETURNING_USER skill-system requests use [AGENT_START_HERE](../AGENT_START_HERE.md) and the canonical [skill-bootstrap](../engine/skills/skill-bootstrap/SKILL.md). For an explicitly named skill or simple comparison, take DIRECT_LIBRARY without forcing an interview.

## 1. Route and establish authority

Choose the route before selecting skills. A public repository link alone is **REPOSITORY_ORIENTATION**: the consuming agent should **evaluate its available host-native memories and relevant task/conversation history** to understand the user's patterns, while separately assessing the public corpus. This is host-side analysis with existing permissions; no separate `skillz` consent gate applies. A link does not authorize installing anything, altering the environment, collecting unrelated connected-account data, scheduling tasks, or mutating the repository. For requested fitted systems, also check the host's actual tools, storage and approval capabilities.

Answer four axes with **yes / no / unknown**, except for authority:

| Axis | What to establish | Consequence |
|---|---|---|
| Persistence | Can this host reliably read/write approved durable state across sessions? | Without it, return carry-forward text in the response instead of promising remembered state |
| User in the loop | Can the host request and receive actionable approval in the actual workflow? | Without it, consequential actions need to remain plans/handoffs unless separately authorized |
| Scheduling | Does this host have a real scheduling capability and permission to use it? | Without it, no background monitoring or scheduled follow-up claims |
| Side-effect authority | **read-only / approval-gated / autonomous / unknown** for the specific action and current instruction | Unknown defaults to no mutation; approval must be specific to the action and destination |

A capability's technical availability is **not** authorization. A persistent host with scheduling can still be limited to read-only. A single-session host can still provide a complete portable skill.

## 2. Discover demand before looking at names

Ask or infer from relevant, authorized evidence only:

1. What goals and recurring tasks cost the operator time or produce avoidable mistakes?
2. Which tools and workflows are *actually* used? What access and read/write limits apply?
3. What cadences exist, if any? Which ones have been explicitly authorized?
4. What failure, privacy, security, cost, or quality controls must survive adaptation?
5. How will success be verified, and where can finished artifacts live?
6. When external material may be installed or adapted, what use is intended (private, organizational, commercial, public redistribution), and do any host/organization license policies or approval requirements apply? Ask only if those distinctions can change the selected path.

Stop once further questioning is unlikely to change a decision. Distinguish `OBSERVED` repeated workflows from `INFERRED` quality/adjacent gaps and `PROVISIONAL` ideas. **Review host-native memory and relevant prior interactions without making the user restate them.** Memory summaries are not complete histories, and a single topic mention is not a recurring need. Access to unrelated external services remains a separate question; do not transmit user task histories to the public library or skill authors. Prioritize quality improvements and important safeguards as well as frequent tasks.

## 3. Map needs to categories, then candidates

Start with [the populated capability quickstart](capability-quickstart.md) for real examples, then [the capability directory](../registry/capability-directory.json) (domain → subdomain → specific capability) and [all governed review companion names](../registry/governed-review-name-index.json) for wider discovery. **The directory's name-only leads are uninspected lexical hits, not approved or verified capability matches.** An empty list or unassessed entry means unknown coverage and triggers capability-keyword fallback across other accessible sources. Use [the current catalog](../INDEX.md), [machine-readable snapshot](../index.json), and [source registry](../registry/sources.yaml) as **complementary evidence/accounting surfaces**, not first-party ranking or complete enumeration. Search by capabilities and inspect whole skills plus relevant components. Compare the user's existing skills and host-native abilities against **all capability-matched indexed resources together**, including governed third-party records, pinned/tracked upstream references, reference-only packages, and first-party `skills/`. Never prioritize a source merely because its metadata is simpler to access. Disclose missing external-source access rather than silently narrowing the search to first-party records. Do **not** install or copy a reference corpus simply because a package exists.

For each candidate, write down its mechanism, fit, required tools, authority/side effects, provenance, exact-version semantic state, applicable package-security state, and controlling package license/NOTICE requirements. Determine whether the user's intended action is mere reading/linking, copying, adapting, combining, redistribution, or installation: each requires its own rights check. If rights are unresolved, do not assume root MIT applies or install/copy unchanged. See [consumer lifecycle contract](consumer-discovery-and-installation.md). If `verified` is merely semantic, do not imply security or behavioral testing. Use `ADOPT`, `ADAPT`, `SUPPLEMENT`, `COMPOSE`, `CREATE`, `CHECKLIST`, `DYNAMIC`, or `NO CHANGE` only after comparing with existing coverage.

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
  license_use_policy: unknown # e.g. internal-only, commercial, public redistribution, restricted licenses; ask only if material
needs:
  - capability: <material user need>
    evidence: <OBSERVED | INFERRED | PROVISIONAL; concise supporting workflow evidence>
    opportunity_kind: <recurring-need | adjacent-hypothesis>
    existing_host_coverage: <covered | partial | unknown>
    likely_value: <specific quality/effort/risk improvement; no fabricated metrics>
shortlist:
  - skill: <name / path>
    disposition: <ADOPT | ADAPT | COMPOSE | NO CHANGE | ...>
    identity_and_security: <exact pin, semantic state and independent security state or unresolved>
    rights_and_notices: <package-specific licensing, requested use and unresolved obligations>
    activation: <request-driven / host event / separately authorized scheduled>
    destination: <user host / portable handoff>
deferred: []
installation_state: not-run # do not infer from selecting a skill
completion_evidence: <what actually passed, or not-run; not a claim of behavioral validation>
search_limitations: <inaccessible family, sparse directory, unknown coverage>
context_access: <only relevant already-available sources examined; unavailable or out of scope noted>
untapped_opportunity: <one evidence-labeled adjacent idea or none>
next_action: <single action or none>
```

## 6. Definition of done

For `REPOSITORY_ORIENTATION` (a link plus “take a look”), use the separate [value-brief definition of done](agent-value-discovery.md): clear public value proposition, honest limitations, up to three capability opportunities ranked by specific benefit and evidence, and one next action. **Do not use the full installation receipt or require a personal interview** for a vague first look.


- Route and authority established with material unknowns shown.
- Durable needs and minimum viable shortlist map to actual capabilities, not popularity.
- Whole-skill and component overlap checked; reuse eligibility not exaggerated.
- Action boundaries, side effects, host prerequisites, and verification named.
- Selected artifacts prepared for the user's host or portable handoff; licensing/notice obligations preserved for protected source material; installation truthfully stated and post-install observations distinguished from semantic desk-check.
- A return visit can conclude `NO CHANGE`.

## Examples of failure to prevent

- **One-shot chat:** Do not tell the user "I'll remember and monitor" when there is no persistent memory or scheduling.
- **Approval-gated host:** A skill mentioning deployment does not authorize production changes.
- **Reference-only vendor skill:** A favorable semantic review without exact-version package-security evidence does not authorize unchanged adoption.
- **Direct library lookup:** Do not demand a capability interview just to show or compare a named skill.
- **Consumer says skills were adopted elsewhere:** Require an observed consuming repo/version/date before claiming cross-repository usage; the user's stated impression alone is not adoption evidence.

Dated material changes to the corpus and governance are summarized in [CHANGES.md](../CHANGES.md); registered exact-version evidence remains canonical in `registry/`. The host can inspect changes without installing a synchronizer.
