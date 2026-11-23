# Skill Packs: one outcome, composable execution, governed learning

A **Skill Pack** represents one user-visible capability that genuinely benefits
from multiple independently owned behaviors, ordered phases, or reusable
components. A pack is **not** a new runtime, hosted service, skill count
multiplier, or mandatory wrapper around every skill. Single-file skills
remain the default when they deliver the outcome coherently.

It is **not another user-facing skill**, installed tool or independently
scheduled improvement agent.

This is an **optional engine-level composition contract** shared by
[Bootstrap](../skills/skill-bootstrap/SKILL.md),
[Forge](../skills/skill-forge/SKILL.md), and
[Eval](../skills/skill-eval/SKILL.md). The pack manifest is declarative and
**does not execute or authorize actions**. The canonical normal consumer
orchestrator remains Skill Bootstrap.

## Architecture selection tree

1. **Can one self-contained skill deliver the complete outcome**, including
   its real required scripts, assets and failure handling? **YES:** keep one
   skill/package; do not introduce phases and manifests for decoration.
2. **Are there sequential obligations with materially different evidence,
   authorization or handoffs**, but a single owner and no independently
   reusable behavior? **YES:** one skill with explicit internal phases may
   suffice. Use a pack only when phase boundaries actually improve recovery,
   testing, dependencies or reuse.
3. **Are two or more independently meaningful behaviors, shared components,
   or independently verifiable phases needed?** **YES:** consider a pack
   with one entrypoint, a directed acyclic module graph and a single frozen
   user-outcome completion contract.
4. **Would composition create duplicate authority, repeated verification,
   incompatible requirements or an unsupported cross-host dependency?**
   **YES:** redraw responsibilities or stop at one skill. Do not ship a
   prettier graph that makes completion less reliable.
5. **Can the pack be delivered as a complete portable unit?**
   **NO:** mark its missing dependencies, host limitations and handoff
   honestly; never claim all phases installed or runnable.
6. **Do the completed phases actually satisfy the original user outcome?**
   **NO / UNKNOWN:** HOLD/NOT_TESTED. A phase-local green checklist cannot
   promote the entire pack to success.

A *phase* is a checkpoint with explicit input/output. A *skill* is a
separately usable instruction entrypoint. A *component* supplies shared
decision rules, references, scripts or evidence contracts. A component is
not automatically a callable tool. The agent selects relevant paths based
on the request and declared dependencies. Optional branches must have
complete non-deceptive fallbacks.

## Portable package shape

A standalone example is in [fictional-evidence-brief](fictional-evidence-brief/).
Optional complex packages may use:

\`\`\`text
my-capability-pack/
  SKILL.md                  # user-visible trigger, overall authority and outcome
  pack.json                 # optional composition inventory, not executable
  LICENSE                   # controlling license for first-party text
  phases/intake.md          # ordered phase with evidence handoff
  components/check.md       # owned reusable check
  skills/compose/SKILL.md   # independently usable subskill
  phases/style.md           # optional branch with safe fallback
\`\`\`

The [manifest contract](manifest-contract.md) defines the deliberately small
v1 wire format. Paths are **relative to the package**; no network locators,
parent traversal, external/implicit dependencies or unaccounted required
components. Record the exact complete package tree and component source
identities during review. Mixed licensing and redistributed third-party
material require their own resolved provenance and rights. A claimed
\`origin: authorized-adaptation\` is **not evidence of permission**.

Dependency arrows define *order*, not delegation authority. A phase can
propose an action, but cannot turn a read-only user instruction into
autonomous write/send/schedule power. Explicit owner approval is required
for consequential host actions.

## Hierarchical feedback routing: canonical vs consumer

Run the [decision tree](feedback-decision-tree.md) after meaningful
execution, material failure or explicit feedback. The hierarchy is:

\`\`\`text
User outcome + evidence + current instructions
  ├─ unsafe, unauthorized or untrusted proposal? → HOLD, don't persist
  ├─ shared invariant/outcome failed? → CANONICAL_IMPROVEMENT candidate
  ├─ only valid user-specific variation? → LOCAL_PREFERENCE
  ├─ both a real defect and a user preference? → MIXED; split receipts
  └─ no supported defect or preference? → NO_ACTION / HOLD if material unknown
\`\`\`

For canonical candidates: locate the **narrowest real owner** (component,
phase, subskill or pack-level orchestration), reproduce, preserve previously
successful behavior, challenge counterexamples, and submit for qualified
maintainer approval. Shared component changes require regression evaluation
for every affected dependent pack. No self-review automatically edits an
upstream package.

For local preferences: honor the current instruction when safe. Persist
only opt-in, allowlisted values in actual **user-private host storage**;
do not store user IDs, preference values, transcripts or private overlays
inside \`pack.json\`, Skillz, published bundles or shared source. Keep
version-aware revocation and compatibility checks. Reuse the existing
[preference routing](../../skills/authored/evidence-driven-refinement-loop/preferences/routing.md)
as guidance, not an automatically installed dependency or new manager.

Bound the loop with
[engine refinement handoff](../refinement/README.md): OBSERVE, EXPLAIN,
CHANGE, CHALLENGE, DECIDE; stop when no material improvement remains.
Separate observed consumer outcomes from static evidence, and do not
increment SemVer for each micro-correction. Source fingerprints and
review freshness still change with every changed package byte.

## Review and delivery

Assess the **pack as one delivered outcome** and each independently
failing module. Test relevant positive, non-trigger, missing-phase,
authorization, dependency-cycle, regression, preference-contamination,
and false-green scenarios. A passing subskill test does not qualify
the pack's handoffs, and an overall pack review does not automatically
grant every individual subskill the \`validated\` status.

The optional Python-standard-library
[structural checker](check_pack.py) verifies only declarative graph shape,
local files, permission ceilings and absence of consumer values. It does
**not** inspect runtime behavior, establish license rights, execute
scripts, prove external host compatibility, save preferences, install,
merge or publish anything. A consuming agent with no Python may apply
this written contract without installing another engine component.

**Consumer destination:** only an authorized user host or a complete
portable handoff, never the Skillz source repository. **Maintainer
destination:** only explicitly approved first-party repository edits;
a PR is not delivered until merged and its exact source verified.

The goal is **better capability completion and reuse**, not maximum
number of subskills, manifests, test fixtures or package versions.
