# Skill Pack manifest v1: declarative local component graph

The optional \`pack.json\` is a portable **composition description**, not an
executable plan, authorization token, evaluation score, installation
declaration or SemVer release. \`schema_version: 1\` identifies the
**manifest shape**, not the version of any skill. Single-skill packages
need no manifest. The public engine can discuss packs without a host API.

## Required keys

- \`schema_version\`: integer \`1\`.
- \`pack_id\`: lowercase kebab-case, unique in the local installation context.
- \`capability\`: concrete user-visible outcome.
- \`entrypoint\`: \`SKILL.md\`, with one overall trigger, non-trigger,
  authority statement and truthful result-completion condition.
- \`completion\`: the outcome-level pass criterion, unaffected by
  optional display preferences.
- \`authority\`: \`read-only\` or \`approval-gated\`; the manifest
  **cannot grant** even those permissions without actual host/user authority.
- \`license\`: claimed controlling pack license; independent source
  and rights verification is still necessary.
- \`files\`: explicit relative inventory of mandatory and optional
  package files, including \`SKILL.md\`, \`LICENSE\` and every module path.
  These names must exist *inside* the package without symlink traversal.
  Text may describe additional runtime dependencies not inferable from
  \`pack.json\`; assess the **complete package** separately.
- \`modules\`: two or more coherent units, each with:
  - \`id\`: unique local identifier.
  - \`kind\`: \`phase\`, \`skill\` or \`component\`.
  - \`path\`: relative local Markdown file; independently runnable \`skill\`
    entries end in \`/SKILL.md\`.
  - \`requires\`: IDs of upstream modules. No cycles, self-reference,
    missing IDs or implicit external dependencies.
  - \`required\`: Boolean. A required module cannot require an optional
    module, so a skipped preference cannot erase a mandatory guarantee.
  - \`fallback\`: \`null\` when required, or a nonempty safe handoff
    description when optional.
  - \`authority\`: read-only or approval-gated, never stronger than the
    pack's declared ceiling.
  - \`output\`: actual handoff/result obligation, not just “ran successfully.”
  - \`origin\`: \`original\` or \`authorized-adaptation\`.
  - \`source_identity\`: \`NONE\` for original, exact source identity for an
    adaptation. \`rights_basis\`: \`ORIGINAL\` for original, a nonempty
    specific rights/NOTICE basis for an adaptation. **Neither label
    authenticates the license or legal permission.**
- \`preference_slots\`: optional array of non-sensitive declarative
  **allowlisted keys**, each with \`key\`, \`kind: enum\`, \`choices\`,
  \`default\` and \`scope: user-private-opt-in\`. This defines which
  presentation settings could be applied by a consuming host, **not**
  any stored consumer values. No consumer ID, account, name, email,
  active choice, personalized request, telemetry or profile belongs
  in the manifest.
- \`feedback_policy\`: fixed policy
  \`{"canonical":"maintainer-review","consumer":"private-opt-in",
  "mixed":"split","iteration":"bounded"}\`. A producer cannot use
  this metadata to bypass safety, approve a canonical change or save a
  private overlay.

The example [fictional pack](fictional-evidence-brief/pack.json) has
intake → evidence check → summary skill → optional style. It has one
result-completion condition and a fallback for the last optional phase.
The specific phrasing and identifiers are invented for tests. It is
not a preapproved skill available for installation.

## Safe dependency/handoff behavior

There is one canonical owner for each internal file and module
identifier. A phase only consumes completed outputs from its declared
\`requires\`. A missing required upstream module **HOLDs** the pack.
An optional phase can be skipped with its explicit fallback, and the
pack's truthfulness/completion contract must still hold. A change
to a shared component reopens checks in all downstream modules and any
other packs that lawfully share that component. Never automatically
propagate a write across installed users.

Pack-level tests challenge the **whole outcome** even when each module
has individually passed. Consumer feedback is routed through the
[feedback decision tree](feedback-decision-tree.md) before any change;
it cannot edit upstream source, authorize deployment, invent a receipt
or turn a neutral default into consumer-specific stored data.

## Optional offline structural check

Run from the repository root, using Python 3.9+ standard library:

\`\`\`sh
python3 engine/packs/check_pack.py \
  --root engine/packs/fictional-evidence-brief
\`\`\`

This checks only manifest shape, file containment and module DAG,
safe optional fallbacks, authority ceilings, and the absence of personal
values in the preference declaration. It does not execute a phase,
authenticate rights, verify the completeness of every link in embedded
scripts, prove consumer permission, query the network or persist data.

The result \`PACK_STRUCTURE_VALID_NOT_EXECUTED\` is **not**
\`HOST_OBSERVED\` or \`CONSUMER_ACCEPTED\`. Any failure returns exit 2
with \`PACK_STRUCTURE_HOLD\`. A constrained host can follow the
written checklist without Python, but must not claim to have run it.

## Packaging and release

A real authoring/installation workflow must separately check exact
complete-package identity, all bundled supports, current licenses,
tool requirements, portability and rights, version-compatibility for
user-private overlays and safe uninstall. Publishing a pack does not
automatically create an independent quality state for every subskill.
Likewise, an individually verified subskill does not validate this pack's
handoff graph.

Keep source fingerprints current after each changed byte. Publish
SemVer releases intentionally, not for every example, formatting or
test edit. Do not silently mutate an immutable released package.
