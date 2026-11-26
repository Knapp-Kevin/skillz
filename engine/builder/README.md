# Skillz Builder: complete skill and pack drafting

The builder turns **a fully authored capability blueprint** into an actual,
portable skill or Skill Pack layout. This closes the gap between planning and
producing the files. The normal route still begins with
[Skill Bootstrap](../skills/skill-bootstrap/SKILL.md), relevant
[corpus discovery](../../docs/consumer-discovery-and-installation.md),
licensing, and the outcome decision.

The builder is an **optional standard-library compiler**, not an LLM, a
semantic skill generator, a hosted execution engine, an installer or an
automatic publication pipeline. It does not invent instructions that the
author failed to supply. A generated package is a **draft for review**.
It is never called \`validated\`, \`installed\` or consumer accepted on the
strength of scaffolding alone.

## Choose the smallest shape

| Outcome architecture | \`kind\` | Emitted files |
| --- | --- | --- |
| One coherent procedure | \`single\` | One \`SKILL.md\`, original-only MIT \`LICENSE\` |
| One skill with separate checkpoints but one owner | \`phased\` | One \`SKILL.md\` with ordered, explicit step outputs; no pack manifest |
| Multiple independently meaningful subskills, phases or components | \`pack\` | One entrypoint, \`pack.json\`, owned module files, license, optional preference declaration |

The [pack manifest contract](../packs/manifest-contract.md) is
validated by the **existing** \`engine/packs/check_pack.py\`. Builder
does not implement a second graph or permission validator. A self-contained
single or phased skill does not require a pack.

## Optional evidence-linked design preflight

For consequential or multi-source designs, use the
[author design gate](design-contract.md) to connect source identities,
explicit capability obligations, authored blueprint targets, and
planned adversarial checks. It routes only original CREATE or COMPOSE
decisions into this same compiler. A source reference is not a permission
to copy code, and linked probes are not executed consumer evidence.

The ordinary complete-blueprint route below remains supported. No
new service, external agent, mandatory file or release is required.

## Optional session-derived authoring intake

For reviewed, minimized session evidence, use the [session design intake](session-design.md). It binds current requirements, correction history and observation claims to the existing design dossier before the same draft preflight. It does not accept raw native transcripts or automatically derive instructions, write packages, or authenticate success.

## Step-by-step generation

1. **Define the user outcome and limits.** Preserve the user's explicit
   trigger, non-trigger, inputs, observable completion, failure behavior and
   authority ceiling. First ask whether an existing eligible skill is
   sufficient, a checklist would be better, or the task is too dynamic to
   warrant a skill.
2. **Search and evaluate candidate mechanisms.** Inspect relevant entire
   first-party, governed and accessible third-party packages; record
   missing discovery coverage, exact source identities and rights. Never
   infer blanket permission from the Skillz root license.
3. **Author a complete blueprint.** Use the
   [single](examples/single-blueprint.json),
   [phased](examples/phased-blueprint.json) or
   [composed pack](examples/pack-blueprint.json) fictional model.
   Replace the invented user-task instructions with real, task-specific
   steps and verifiable outputs. The blueprint must state
   \`rights_declaration: caller-asserts-original-content\`. This
   **assertion is not a license determination**: blocked, copied, adapted or
   third-party material requires separate legally permitted handling and
   should not be laundered through this original-only generator.
4. **Preflight without writing anything:**

   \`\`\`sh
   python3 engine/builder/build.py \
     --input engine/builder/examples/pack-blueprint.json
   \`\`\`

   The JSON report lists the proposed files, stable content SHA-256
   fingerprints, module sequence, structural status and evidence limits.
   This uses a transient temporary directory for structural checks;
   it does **not** create the user skill at a destination, install it or
   call external tools.
5. **Create the actual files only when specifically authorized:**

   \`\`\`sh
   python3 engine/builder/build.py \
     --input /path/to/authorized-blueprint.json \
     --output /path/to/new-skill-directory \
     --write
   \`\`\`

   The target directory's **parent must exist**; the target itself
   **must not exist**, even if empty. No force or overwrite mode exists.
   The default writer also refuses destinations inside the Skillz
   checkout. Maintainer-authorized repository writes additionally
   require \`--repository-maintenance\`, but that flag itself is **not
   approval** to modify a repository. If an output write fails halfway,
   a partial directory may remain; the tool reports HOLD rather than
   completion. Inspect and remove that partial candidate manually before
   retrying.
6. **Review the finished artifact, not the manifest.** Read every emitted
   \`SKILL.md\`, support file and dependency. Test the original positive
   trigger, a near non-trigger, missing-tool or offline fallback,
   adversarial authority/rights issues, and the *false-success case*
   where generated files exist but the requested task still cannot be
   completed. Use \`STATIC_REVIEW\`, \`LOCAL_TEST\`, \`HOST_OBSERVED\`,
   \`CONSUMER_ACCEPTED\` or \`NOT_TESTED\` precisely.
7. **Only after actual qualification**: hand off a complete portable
   package, or install in the user's authorized host; separately verify
   actual destination, identity and execution. For first-party
   Skillz maintenance, complete provenance, security, exact package
   fingerprint, licensing and PR merge gates before saying delivered.

## Blueprint v1 contract

The whole blueprint has these required keys and **no hidden extras** (a subskill module may additionally declare `discovery_description`):

| Key | Role |
| --- | --- |
| \`schema_version: 1\` | Blueprint *format*, not SemVer release |
| \`kind\` | \`single\`, \`phased\` or \`pack\` |
| \`name\` | Safe kebab-case name |
| \`description\`, \`outcome\`, \`trigger\`, \`non_trigger\` | Meaningful use and avoid-use contract |
| \`inputs\`, \`verification\`, \`failure_handling\` | Required task evidence and safe outcome checking |
| \`authority\` | \`read-only\` or \`approval-gated\` maximum, never a permission grant |
| \`copyright_holder\` and \`rights_declaration\` | Author-provided *original* copyright and provenance assertion, subject to independent review |
| \`steps\` | Ordered \`id\`, \`title\`, \`instructions\`, \`output\` entries for \`single\` or \`phased\` |
| \`modules\` | For \`pack\` only: \`id\`, \`kind\`, \`requires\`, \`required\`, \`fallback\`, \`authority\`, \`output\`, \`instructions\`; optional \`discovery_description\` for independently discoverable subskills |
| \`preference_slots\` | Only optional, public allowlisted enum *definitions*; never a saved consumer selection |

All array and object fields are explicit. Unknown input fields, missing
required data, placeholder text such as TODO, unsafe slugs, cycles,
missing required support files, permission escalation, and non-declared
preferences HOLD. A pack's module files are generated **inside** the
same package, even for separately triggerable subskills. The pack's
metadata and file inventory are derived from the actual generated
modules, not manually trusted from a caller.

The current optional builder is **original-content only**. To incorporate
third-party adapted material, first complete its attribution, source
pin, license/NOTICE and derivative-rights review through the existing
engine procedures. Do not simply claim \`original\` in the blueprint.
The builder only checks that the original-content declaration was
provided; it **cannot know whether it is true**.

A preference declaration describes *possible* neutral settings. It
never grants storage permission, supplies an actual user's choice,
overrides canonical safety, or becomes public personal data. Optional
private preference persistence remains a **separate host-controlled
consent, secure storage, revocation and compatibility workflow**. The
[canonical-versus-preference tree](../packs/feedback-decision-tree.md)
still governs whether feedback belongs in the shared skill.

## Required cross-host compatibility guard

Use [Getting started with Skillz](../../docs/getting-started-with-skills.md)
for destination, authority, upload and verification decisions. The optional
`host_compat.py` is a **part of this existing builder**, not a new engine:

```sh
python3 engine/builder/host_compat.py --all
python3 engine/builder/host_compat.py --skill effort-allocation-navigator --host m365-agent-builder
```

Both `build.py` and `design.py` automatically run this same static gate
against the complete staged package before any destination write, including
dry runs. Repeat `--host` for each established target, for example:

```sh
python3 engine/builder/build.py --input /path/to/blueprint.json --host claude-code --host github-copilot
python3 engine/builder/design.py --input /path/to/design.json --host m365-agent-builder
python3 engine/builder/host_compat.py --package /approved/custom-skill --host m365-agent-builder
```

With no target option, the compiler checks all currently assessed profiles (ten as of 2026-11-25);
this does not establish the actual user's host. A hard blocker on any
selected profile returns HOLD before creating the destination. No bypass
or automatic instruction truncation is provided. Keep the canonical
name as the final installed directory name; an arbitrarily named draft
destination is not an installed skill. The receipt includes per-profile
results, warnings, explicit unknown host/runtime evidence and the required
next verification. Unsupported hosts use manual current official rules
and a portable handoff until qualified. Never mistake model identity for
host functionality. Before implementation, identify actual permissions,
tool dependencies, bundled reference loading, runtime and persistence;
provide safe fallback or HOLD if any required capability is unavailable.
Manual authoring uses the same guard without requiring Python.

### Author for portability before drafting

Read the current machine-readable packaging constraints before choosing the
package architecture:

```sh
python3 engine/builder/host_compat.py --profiles
```

This read-only inventory is generated from the same profiles used for
preflight; `portable_authoring_envelope` calculates the strictest numeric
bounds and shared extension set, with separate profile rows for exact
exceptions. It is not live host capability discovery. The common name,
folder and description rules follow the [Agent Skills specification](https://agentskills.io/specification). The standard-library checker recognizes a conservative required-field subset, not arbitrary YAML validation. Recheck official rules
and use the manual guide when shell/Python is unavailable.

For general-purpose skills, author a clear discovery description of at most
200 characters; put the full activation/non-trigger contract in the body.
Keep each independently discoverable entrypoint compact (target fewer than
20,000 characters), use supported text/data/resource types and a shallow
package tree. The current broad-portability targets include at most 100 files,
three nested directory levels and at most 10 MiB of uncompressed content;
consult the current profile inventory for host-specific limits. Avoid hidden or
cache files, extensionless resources other than the handled license, and
unsupported executable formats. Prefer portable standard-library or
instruction-only methods. Keep all needed resources, rights notices and safety constraints. For packs,
each nested `SKILL.md` must also have valid metadata, a matching parent
folder name, and host-compliant discovery text. The builder uses a qualified
`<pack>-<module>` name and matching folder (maximum 64 characters); provide
an authored `discovery_description` if the full output contract is too long
for discovery. Full output stays in the body. Avoid case-insensitive or
Unicode-normalized path collisions, reserved Windows names and archive
basenames that collide with another skill's host variants.
The strictest assessed profile is a design target, not a reason to remove
essential functionality. Check the actual profile constraints in
`host_compat.py` and current official host guidance; do not infer tools,
script runtimes, network, persistence or permissions from ZIP acceptance.

**Repository admission is all assessed profiles, not a chosen subset.**
`build.py` and `design.py` reject narrowed `--host` scope in repository
maintenance. Manually authored or modified packages must run:

```sh
python3 engine/builder/host_compat.py --skill <slug> --require-authored-ready
python3 engine/builder/host_compat.py --all --require-authored-ready
```

The existing engine CI and release builder enforce the same all-profile
admission policy. Any unexpected static HOLD blocks admission/publication.
The only current narrow exception is the named PowerShell files of
`offline-hyperv-qual-vm` on four restricted upload profiles; those pairs
remain HOLD, not PACKAGE_READY. An additional exception requires explicit
maintainer review of essential functionality, exact skill/host/blockers,
and a safe fallback. Do not use extension disguises, automatic truncation,
resource deletion, weakened verification or a reduced target list to pass.

Builder receipts separately list assessed-but-not-selected profiles and
unassessed routes (currently ChatGPT and unidentified OpenClaude/other).
An unknown host is an explicit HOLD requiring current official documentation
and actual host testing. Adding a new assessed profile expands the default
admission matrix; no universal native execution claim follows.

This checks authored or explicitly supplied custom SKILL.md structure, local reference closure, file
extensions and selected documented host package limits, and can generate
a ZIP with an explicit `--zip-output` or a directory handoff using
`--directory-output`, each at a *new* path outside the Skillz repository. It never
executes scripts, makes network calls, or installs a skill. Its corpus report
is a list of **known blockers and untested execution capabilities**, not an
assertion of universal consumer acceptance. Unknown hosts require review,
not guessed compatibility. Add host adapters only after official method
verification, and preserve one canonical portable package.

## Contract-derived acceptance planning (optional)

For a builder-generated skill, use [acceptance_plan.py and its protocol](acceptance-plan.md)
to derive NOT_RUN cases from the validated design dossier and exact completed
package. The selected host transformation manifest and each required case
are bound to the plan. Prepare concrete fixtures and independent oracles
before an authorized native trial; a plan is not an observed result.
After the trial, use the same protocol's read-only acceptance_ledger.py to
regenerate the plan, verify all archive member bytes and reconcile each
case claim to its stage receipt. It does not authenticate observations. For existing manually authored skills,
use the same protocol's source_acceptance.py with a reviewed exact-source
contract; the included Scheduled Work Proof Auditor pilot exercises that
route without claiming any native execution.

## Native host evidence (optional)

Use the [native host acceptance protocol](host-acceptance.md) after static
preflight for actual bounded host trials. The read-only `host_acceptance.py`
checks exact manifest/archive identity and consistency of recorded stage
claims, without authenticating or executing them. It cannot promote a skill
to validated. No live trial is required for static source admission.

## Evaluation and bounded refinement

Run:

\`\`\`sh
python3 -B scripts/qa/test-engine-builder.py
\`\`\`

The synthetic tests exercise three generated shapes, fresh output creation,
stable hashes, complete links, no-overwrite, repository mutation guard,
missing permissions, unsafe preferences, cycles and false completion
claims. These are **local deterministic mechanics**, not external agent
acceptance. The [authoring acceptance rubric](acceptance.md) defines the
separate semantic and consumer gates.

After material feedback, use the
[engine refinement handoff](../refinement/README.md). Preserve the
baseline and previously successful cases. Promote a general correction
only with evidence and maintainer authority; honor an individual
presentation preference only locally and persist it only with explicit
consent in actual private storage. Stop when no consequential new finding
changes the decision. **Do not increment versions for each micro-edit.**

The acting agent is free to produce the same complete package directly
if it lacks Python or filesystem access. The builder is useful when an
explicit structured blueprint, deterministic formatting and a reproducible
file inventory materially improve results, not a mandatory user
prerequisite.
