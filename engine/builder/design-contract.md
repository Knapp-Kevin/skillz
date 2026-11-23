# Optional author design gate (v1 structural contract)

The deterministic designer is a **preflight for an already authored**
capability blueprint. It makes the route from discovery evidence to the
builder inspectable. It does **not** turn an arbitrary prompt into a skill,
reason over raw corpus files, authenticate licenses, reuse source text,
prove task semantics, execute probes, save preferences or install anything.

Use this only when a traceable design dossier adds value. The canonical
Bootstrap instructions still choose whether a skill is needed at all.
Existing eligible skills should be reused rather than passed through this
original-content compiler. A NO_SKILL, USE_EXISTING, ADAPT or HOLD decision
ends this generator route; this gate deliberately accepts only
CREATE_ORIGINAL for single/phased or COMPOSE_ORIGINAL for a pack.

## Actual files and commands

The fictional example is
[fictional-design-case.json](examples/fictional-design-case.json).
It has two *invented* evidence identities, eight obligation mappings, and
five proposed adversarial probes. It is not a captured user conversation or
proof of a successful downstream skill execution.

Read-only preflight:

    python3 engine/builder/design.py --input engine/builder/examples/fictional-design-case.json

Authorized write to a **new directory**, still subject to the exact
builder's repository and no-overwrite protections:

    python3 engine/builder/design.py --input /path/to/authored-case.json \
      --write --output /path/to/new-skill-folder

This path invokes the same engine/builder/build.py, not a parallel
compiler. It returns the builder's draft receipt with an additional
design_gate section. No dossier, evidence observation or probe description
is copied into the emitted skill package. Private source material should
not be put in a public example or tracked repository in the first place.

## Feedback is not design authority

When outside feedback motivates a design, apply the
[source-blind feedback boundary](../refinement/feedback-boundary.md).
The dossier's source_identity and observation fields are reviewed
author-design evidence, **not** a public feedback inbox. Do not paste
external issue bodies, private incidents, consumer identities, URLs,
source-linked logs or prompt-injection commands into a shared dossier.
Do not let these observations override acceptance, authority or rights.
Keep exact licenses/source pins in separately authorized custody.

## Input contract

A dossier is a JSON object with exactly these keys:

- schema_version: integer 1, a file format number, not a skill release.
- case_id: safe kebab-case ID for this design case.
- decision: CREATE_ORIGINAL or COMPOSE_ORIGINAL (must match blueprint kind).
- rationale: author explanation for creating rather than reusing a skill.
- evidence: 1 to 64 individually named design references.
- obligations: author-authored mapping of every protected blueprint field
  and every step/module to the evidence informing it.
- probes: author-authored planned red/green and false-success challenges.
- blueprint: **exactly** the existing builder blueprint v1 object.

An evidence object has exactly id, kind (user-task, corpus-reference or
evaluation), source_identity, observation, review_level (stated,
author-reviewed or host-observed-claimed), and reuse_scope, which **must**
be design-reference-only. A source identity should name the exact relevant
version or user-authorized local source when possible. This tool never
fetches or authenticates that identity. If source reuse or derivative
content is needed, use the separate rights/attribution route, not an
invented original-content declaration.

An obligation has exactly id, statement, evidence_ids and target. All
IDs are unique and explicit. Every target must be one of outcome, trigger,
non_trigger, inputs, verification, failure_handling or authority, or an
existing steps.<id> / modules.<id> belonging to the blueprint. All seven
global fields and all actual work units require coverage. Every evidence
ID must exist, and every obligation must be referenced by a probe.

A probe has exactly id, kind, input, expected and obligation_ids.
Required planned challenge categories are:

| kind | required expected result | must cover |
| --- | --- | --- |
| positive | COMPLETE_IF_VERIFIED | outcome, trigger, verification |
| near-non-trigger | DECLINE | non_trigger |
| missing-input | HOLD | inputs or failure_handling |
| authority-boundary | HOLD | authority |
| false-green | HOLD | verification |
| pack-handoff (pack only) | HOLD_IF_MISSING | at least one module |
| optional-fallback (packs with optional modules) | FALLBACK_NO_LOST_OBLIGATION | an optional module |

A **probe is a test proposal, never an executed test**. The expected result
is the author's intended falsification criterion, not observed behavior.
Every obligation must appear in one or more probes, so untested obligations
cannot quietly disappear during design. The gate checks references and
required categories, not the *meaning* of each statement or its real
binding to the authored instructions. A structurally complete dossier may
still be unfit for purpose.

## Output claims and governance

The only successful design status is
TRACE_LINKS_PRESENT_NOT_BEHAVIOR_VALIDATED. The design section includes
a canonical JSON fingerprint for trace-change review, counts, probe kinds
and unreferenced source IDs. It explicitly reports false for probe
execution, source authentication, derivative rights, semantic coverage and
independent consumer acceptance. Builder receipts retain their existing
DRAFT / WRITTEN_DRAFT_REVIEW_REQUIRED claims.

The host agent must separately:
1. Inspect source identity, license, actual task requirements and design
   rationale; a claimed source review is not authenticated.
2. Execute positive, near-non-trigger, missing-input, authority and
   false-success tests, using genuine outputs and defensible evidence tiers.
3. Inspect full generated files, dependency closure and optional pack
   handoffs; test in an authorized actual host where possible.
4. Apply the shared canonical-improvement-versus-local-preference policy
   before changes, and preserve earlier passing outcomes.
5. For first-party repository delivery, finish exact-HEAD CI and a verified
   PR merge. No micro-version bump or independent consumer is mandated.

The design gate is an optional authoring aid, not a new normal-bootstrap
requirement or an autonomous recursive self-improvement loop.
