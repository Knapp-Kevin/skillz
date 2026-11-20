# Passive model compatibility profiles

**Purpose:** Discover model/host assumptions for an *exactly pinned* skill version without guessing that a model is capable or incompetent, splitting canonical skill identities, or treating prompt advice as observed behavior. This is **maintainer/catalog metadata**, not a dependency for a standalone installed skill. See the repository-wide [capability-adaptive execution standard](capability-adaptive-skill-execution.md). A single downloaded skill package must remain complete offline without this registry.

## Use the browse facet

Start with the task and the [canonical 33-domain capability directory](../registry/capability-directory.json). The [model compatibility capability facet index](../registry/model-compatibility/by-capability.json) has secondary routes to three [exact-version example profiles](../registry/model-compatibility/profiles.json). A key such as `cloud-devops/ci-cd` is the **existing domain/subdomain route**. The same governed skill has exactly one identity regardless of how many capability routes or model/host annotations refer to it. A facet does not establish capability coverage, verification, license clearance, suitability, host installation or permissions. Use the canonical `matched_skill_ids` entries and current companions for those decisions.

Example tranche, **no observed cross-model validation**:

| Governed identity | Exact reviewed package | Existing capability routes | Current observed model/host effectiveness |
| --- | --- | --- | --- |
| `local-skills/ci-guard` | v1.2.0; Git tree `950bf5db6b9740bdd3fa92721ffb5a8a0fb9c258` | `cloud-devops/ci-cd` | `UNKNOWN` |
| `local-skills/claim-evidence-adjudicator` | v1.1.0; tree `4f1576d8c8170e1b14f97e761a2dcfd4a8bcd0c4` | `research/fact-checking` | `UNKNOWN` |
| `local-skills/technology-change-intelligence` | v1.2.5; tree `7aa1d44926dc7eeda91ac71f7ddebd3cf34772b7` | `research/source-discovery`, `research/synthesis` | `UNKNOWN` |

All three annotations pin the original `SKILL.md` blob, complete package tree, verification companion, historical `reviewed_at`, independent `checked_at`, and source snapshot commit `47d0345a1b6fae61b5d1f65448154aba15f36a7d`. They are `STATIC_ASSESSMENT` annotations about source instructions, **not** cross-model observations, model-specific instructions, permission upgrades, or recommendations to execute. Existing review timestamps, rubrics, statuses, first-party copyright and skill contents were not changed.

## Evidence and authority vocabulary

[JSON Schema](../registry/model-compatibility/profile.schema.json) constrains an individual profile. The [collection](../registry/model-compatibility/profiles.json) is intentionally additive rather than a new compulsory field in every existing companion.

- `AUTHOR_CLAIM`: the author says an approach is effective; independent confirmation is not established.
- `THIRD_PARTY_CLAIM`: a commentator or distributor says an approach works; this is a lead, not vendor authority or independently observed performance.
- `STATIC_ASSESSMENT`: an assessor read a pinned source and identified supported instruction/host/context assumptions. **Cannot** demonstrate that a model followed instructions successfully.
- `OBSERVED_TEST`: a documented host run at exact model revision, host, fixture, tool permissions, results and trace. A claim needs a real, retrievable receipt, **not** a simulated answer or hypothetical prompt. Host qualification is limited to the tested configuration.
- `UNKNOWN`: unestablished behavior, unknown model/host, missing sources or untested effectiveness. Unknown is not failed.

A profile's `observed_effectiveness` remains `UNKNOWN` without directly witnessed qualifying evidence. A source reviewer may identify where prompts call for examples, tool access, long context, planning, verification, or mitigation, without guessing whether a named model passes. The claimed model, host, version, context limit and runtime need independent evidence before filling fields. No compatibility profile can grant write authority, private-file reads, external egress, subagent spawning, installations or override host policy.

## Capability-adaptive application

For **any host/model**, including local smaller models and strong hosted models, preserve the same requested outcome, permission floor, threat checks and completion evidence. Choose a *direct* route when the work is within capability and authority; a *guided* route when a concrete ambiguity benefits from a packaged example or deterministic calculation; a *bounded fallback* when evidence, tools or permissions are unavailable. Do not use vendor/family names or token limits as static permission to skip safeguards or impose arbitrary task ceilings. Never require the consumer to fetch this registry, contact the network or install companion runtimes. Only selected, **bundled** references are needed for standalone skill execution.

## Freshness and discovery workflow

1. **Source/package pin:** a change to `SKILL.md` or any *material bundled support file* changes the complete package tree and yields `NEEDS-RE-REVIEW` for the current tracked version. Preserve the previous review and profile as historical evidence, inspect the changed package, then issue a new exact-version review/profile. Updating `checked_at` for a matching tree **never** changes historical `reviewed_at`. An upstream update to an intentionally unchanged pin is `UPSTREAM-UPDATE-AVAILABLE`, not silent staleness.
2. **Model/host revision drift:** a new model/version, changed host behavior, shifted context window, tools or effort semantics flags a specifically **model-bound compatibility claim** as `RECHECK_MODEL_CLAIM`. It **does not stale an unchanged pinned skill** or turn an unrelated claim into failure. Until a witnessed run is available, effectiveness remains `UNKNOWN`. No provider monitoring, scheduled checks or version freshness scan is implied.
3. **Exact discovery leads (#599):** collect model/prompt guidance as **source-pinned read-only leads**. Record canonical publisher and artifact identity, source revision, terms/attribution, model/host/version as actually stated, separate source publication and assessment dates, duplicates/mirrors and unsupported generalizations. Route discovery to existing capability taxonomy (#588). When a source changes, queue the new exact version for review; do not overwrite the previous row or promote a second source mention as independent confirmation. These leads are not new governed identities until reviewed under normal governance.
4. **Static content rubric (#402):** characterize instruction hierarchy assumptions, model-brand gating, unsupported mandatory delegation/long context, loss-of-context behavior, missing tool fallbacks, external reference dependence and claims that test or finish occurred without evidence. Record findings on the **source** separately from the exact-host success of a **model**. A model effectiveness claim has no static PASS merely because the skill looks sensible.
5. **Derivative prompt variants:** if a specialized edition is truly necessary, make a new **separately pinned derivative package** with original source/revision/rights, exact changed source diff, permissions, test conditions and new static/behavioral qualification. Never silently rewrite, relay or relicense the canonical skill.

The [ten unverified presenter guidance leads](../registry/model-compatibility/unverified-presenter-guidance.json) from issue #722 preserve the owner-provided source summary's literal model name `Fable 5.2` without pretending it is verified Anthropic documentation, a real model identity, a known host configuration, a capability floor, or execution evidence. They are deliberately **not** attached to a governed skill as verified instructions. Any subsequent model-specific transformed variant requires its own review and separately witnessed tests.

## Offline integrity, without CI or model calls

From a checkout with Git metadata and Python 3 standard library:

```sh
python3 scripts/qa/check-model-compatibility-profiles.py --self-test
python3 scripts/qa/check-model-compatibility-profiles.py
```

The checker compares the checked-in JSON schema, compatibility collection, capability facets and actual canonical domain matched IDs; verifies original source commit/complete tree/SKILL.md blob against Git; compares unchanged verification companion's version/fingerprint/`reviewed_at`; and checks cited in-skill section anchors. It refuses stale package trees, fake observed tests, mismatched capability routes, missing section pointers, authority escalation and fabricated profile counts. Its self-test contains independent negative mutations plus separate source-drift and model-drift semantics. It reads only local files and Git objects. **No CI workflow, crawler, scheduled job, external network, paid model call, installer or runtime behavior measurement is created by this work.**

No public skill-count/corpus accounting is changed: README, canonical index, systems state and curation queue remain undisturbed rather than being converted into an activity diary.
