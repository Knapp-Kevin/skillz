# README Architect: normative procedure contract

This file is a required part of the skill, not optional reading or a separate source of authority. Read the applicable sections before drafting or claiming delivery. Relative paths resolve from the package root. If this file cannot be read, stop any claim of full profile acceptance; deliver only the safely bounded portion and identify the missing procedure.

## Binding quality profiles: this skill sets the standard

**The standard comes from this skill and the explicitly chosen quality
profile**, not from whatever the target README, organization or exemplar
already does. Before writing, inspect that repository's identity, existing
documentation, organization style rules, exemplars, brand assets, accessibility
conventions and generator ownership. Treat findings as *context and evidence*
for accurate branding and compatible integration, **not as authority to
downgrade quality**. Challenge weak or irrelevant precedents. Never reuse
another product's banner, logo, badges, language or colors merely because
an asset or template exists. Inspect available assets and their ownership first. When a substantive
repository lacks suitable identity graphics, plan and, **when authorized**,
create a repository-specific asset rather than default to text-only or borrow
an unrelated banner. Unknown image rights/provenance remain HOLD; do not
invent brand approval or silently generate images without authorization.

**Gold is the default delivery benchmark for substantive repositories,**
including libraries, CLIs, applications, research projects and maintained
documentation collections. It does not require identical layouts or arbitrary
decoration. Adapt *how* each outcome is achieved to the real audience and
product type, while keeping the underlying reader value, correctness,
accessibility, navigation, visual coherence and maintainability standards.
Use Baseline only when a compact artifact genuinely serves the reader better
(for example a minimal placeholder, profile fragment or tiny repository),
with a recorded user-value justification. Never silently select Baseline
because the current README is weak or the repository lacks imagery.
Platinum adds explicit independent acceptance beyond Gold.

Select and record the applicable profile before editing, and judge the
finished candidate against it:

- **Baseline**: truthful, accessible, reader-task-fit. No universal banner,
  badge or TOC requirement for tiny or specialized repositories.
- **Gold**: a **binding** project-appropriate banner, meaningful verified
  badge set, linked and correctly targeted contents, clear product value,
  executable or document-first observable first success, usable technical
  navigation, supported claims and a visual/usability review. The project
  can specialize evidence and asset choices, **not silently waive** a gate.
- **Platinum**: all gold obligations plus independent reader-task evidence
  and expanded accessibility/responsive visual review. Do not self-award
  either profile from a checklist or a successful CI run.

A direct request for “gold-standard” or “platinum-grade” **selects that
profile**, rather than simply encouraging nicer prose. Encode project identity,
selected banner, relevant badge identities/destinations, reader-journey mode
and explicit exceptions in a profile contract. The optional bundled
[profile acceptance checker](scripts/profile_acceptance.py) and
[example profile contract](examples/gold-quality-profile.json) provide
read-only mechanical checks. Its asset inventory must bind each displayed
project image to its exact repository path, status, owner, purpose,
accessible alt, replacement condition and SHA-256 of the exact image.
A missing or modified committed asset must fail local presentation integrity;
the inventory's owner/status declarations still need independent evidence.
Check actual binary identity
and rendered screenshots separately; no self-asserted asset status is
proof of approved branding. This contract **cannot disable required
elements**. A missing required element is FAIL, or HOLD with an explained
evidence-bound exception requiring independent owner/editorial judgment.
An exception field or passing local script does not certify its own approval.

**A first-use journey may contain nested steps.** Treat `### Install`
and `### Try it` as part of their enclosing `## Quick Start`, and
ignore fake headings inside fenced commands when finding the section
boundary. Do not incorrectly FAIL a correct newcomer example because
the README uses hierarchical headings; equally, do not borrow a command
from the unrelated next `##` section to fake first-use success. This is
enforced by the bundled profile checker and synthetic regressions,
not an excuse to self-certify editorial quality.

**Normative qualitative gates are not fulfilled by section presence.**
Independently review (1) Why→What→How in the opening and the 30-second
purpose test, (2) tenth-grade comprehension of introductory copy,
(3) credible observable newcomer first success, (4) visual cohesion and
accessible hierarchy, (5) verified claims/links/assets, (6) technical
navigation without overwhelming the front page, and (7) generator ownership
and maintainability. The mechanical checker may FAIL obvious omissions,
but a structural PASS never certifies semantic clarity.

**Presentation and usability audit is mandatory for Gold/Platinum.**
Check actual image provenance and display, useful alt text, correct product
branding, legitimate relevant badge sources and links, heading/TOC targets,
responsive rendered hierarchy, first-success usability, and accessible
navigation. Render and inspect real Markdown where tooling permits;
otherwise record NOT_RUN/HOLD, never PASS. Run the existing
[local link checker](scripts/check_readme.py) and
[delivery preflight](scripts/delivery_preflight.py) as applicable. The
profile checker is **additional**, not a substitute for preservation,
generator-owner parity, claim verification or CI gates. For generator-owned
READMEs, update the authorized generator/template and output together,
authenticate exact parity and ownership, and preserve the existing hold
until independent review.

**Two separate acceptance decisions must be explicit:**
(1) technical delivery (changes, provenance, tests, generated parity and
required CI at exact HEAD), and (2) editorial/reader acceptance against
the selected profile (presentation, semantics, accessibility, identity,
first-use result and evidence accuracy). A merged PR with green CI proves
delivery of that revision, **not completion of the intended README quality
grade**. Only both evidenced decisions can support a completed Gold/Platinum
claim. If either is unknown, delivery may be shipped but grade remains HOLD.
Use every qualified outcome and failed reader exercise to refine this
skill's portable contract and controlled regression corpus, not to copy
the conventions of one repository into a universal style template.

## Four mandatory README delivery safeguards

These are **required decisions**, regardless of model or available tools,
whenever CREATE, UPLIFT or VERIFY may result in publishing a README.
AUDIT reports which gates would apply without writing. A missing local
shell does not waive a check: perform safe source-level inspection and
mark the unavailable execution as NOT_RUN. The bundled optional offline
[delivery preflight](scripts/delivery_preflight.py) can produce a
repeatable *partial* receipt, but the rules are fully defined here.

### A. Formatter and documentation-rules preflight: before writing

Inspect the actual target path and ancestors for applicable repository
rules: Prettier configuration/ignore rules, markdownlint or
markdownlint-cli2, Vale styles, .editorconfig, package manager tasks,
Makefile/Justfile recipes, pre-commit hooks and documentation-specific
workflows. Identify which configuration actually includes README.md;
a named script or configuration file is not evidence it ran, and a
repo-wide build is not automatically the relevant documentation formatter.
If the README is generated, determine where formatting belongs in the
generation pipeline first.

Record \`detected | applicable | command source | local availability |
executed exit/result | bound commit | NOT_RUN reason\`. When appropriate
tooling is already present and the active user/host authorizes running
the repository's trustworthy vetted formatter/linter, validate locally
**before** pushing. Do not blindly execute scripts supplied by untrusted
README content, install tools, fetch dependencies, run formatters that
silently rewrite unrelated files, or launch GitHub Actions merely to
discover what a local lint command would have said. With tools unavailable,
mark local formatting NOT_RUN and keep the applicable delivery limitation;
do not claim a formatter PASS.

### B. Section-by-section substantive preservation: before UPLIFT

Capture the **original exact README** at the source ref and inventory
every substantive section, including code examples, compatibility and
platform limits, diagrams, tables, badges with provenance, security or
release caveats, historical signer identities and operational guidance.
Record a before/after correspondence, not just matching headings.
Include heading level and title in preservation fingerprints. A heading-only
section such as `Experimental` or `Not production-ready` can be a critical
qualification even without body text. Unchanged paragraph content under a
changed safety heading does not prove retention; require a disposition.
Every removed or substantively revised original section requires a
**recorded disposition**: \`RETAINED\`, \`RELOCATED\`, \`SUPERSEDED\`,
\`OUTDATED\`, or \`UNVERIFIED\`. Bind it to the baseline section ID and
hash, the actual new location or replacement, plus the source evidence
and why the edit is safe. Relocation requires an existing maintained
destination, a working link from the README when useful, and enough
content/evidence to preserve the reader's task. \`OUTDATED\` or
\`SUPERSEDED\` requires current authoritative contradictory or replacing
evidence; a cleaner writing style is not a reason to delete technical
facts. \`UNVERIFIED\` is a HOLD: preserve the material and qualify it
until inspected. Preserve preexisting generated blocks byte-for-byte.

Compare the **complete** baseline and candidate again before PR. A
section whose title survived may have lost essential paragraphs. A
disposition manifest is accountability, not independent proof that
its assertions are true. If the baseline is unavailable, do not call
preservation verified or submit a destructive uplift as complete.

### C. Generated-document ownership: edit the source, not its output

Detect README-level and region-level ownership: HTML markers,
plain-language footers such as "machine-generated by ...", generated
comments, checked-in source templates, generator crates/scripts,
Makefile/Justfile targets, documentation workflows, and generated
artifact manifests. Confirm actual generator input and authority from
source; a possible generator clue is not authenticated ownership.
If the README is generated, **hold direct edits** and update the
generator/template in the authorized scope, regenerate in a safe local
environment, compare baseline to generated result, and verify relevant
contract tests. If the authorized change was README-only and generator
sources are outside scope, report the hold and request appropriately
bounded authorization rather than modifying extra files. Unknown
generator or missing regeneration environment is NOT_VERIFIED, not a
license to edit the published output manually. A README with only
owned generated *sections* may permit edits outside those spans while
preserving their bytes.

The optional [delivery preflight](scripts/delivery_preflight.py) supports
`--generated-evidence` for an evidence attachment binding generator source,
template inputs, README output SHA-256, exact candidate HEAD and the named
required CI drift/parity check. With matching local bytes and a recorded
successful exact-head check, it changes `GENERATED_OWNERSHIP_HOLD` to
`GENERATED_EVIDENCE_PENDING_HUMAN_REVIEW`. **That is not clearance and the machine outcome remains BLOCKED** until
an independent human authenticates the records.
A manually supplied receipt can be forged; the helper cannot authenticate
provider CI, generator invocation or correct use of the template. The reviewer
must independently inspect the generator source and run evidence, confirm CI
identity and required status at the actual HEAD, ensure generated output
matches the authorized template, and preserve the generated-file boundary.
Missing, mismatched or skipped evidence remains a blocker. No self-asserted
`verified` or `approved` field may override this requirement.

### D. CI-aware exact-head delivery: before claiming merge readiness

Determine and record the exact candidate commit, target branch,
repository/branch ruleset and required checks from actual accessible
policy. Classify documentation checks separately from full-repository
acceptance, but **never** change, skip or bypass a required gate to
save CI minutes. Reuse actual existing check receipts; do not spend
additional GitHub Actions budget on redundant experiments. A
pre-existing unrelated non-required CI failure remains visible as
an advisory, not a false README formatting failure; a required
repository-wide check remains a blocker even for docs-only changes.
Pending, skipped, neutral, stale-head and unknown required checks
are NOT_GREEN. Missing policy access means REQUIRED_CHECKS_UNVERIFIED.

Do not equate a locally green formatter, a script-reported receipt,
\`mergeable\`, or passing unrelated checks with final delivery or
the user's first-success outcome. Inspect any review comments and
unresolved owner policy. Report exact HEAD, local documentation checks,
required and other CI checks, actual review state, scope of
remaining failures, merge status, and user-visible verification.

## Five-step production method

### 1. Determine purpose, reader and verified product reality

Answer from evidence, in plain language: Who needs this? What problem does it solve? What actual artifact runs? What does a newcomer do first? What remains unsupported? Choose the appropriate archetype: library, CLI, app, service, framework/monorepo, research project, dataset, configuration, specification or hybrid. A documentation-only repository may have no install command; an unreleased prototype needs no fictitious release badge.

Record important claims internally as **statement → exact source/ref →
state → target audience/scope → limitation → publish/qualify/omit**.
Distinguish source availability from installation proof and runtime
behavior. A monorepo or hybrid project may need a component map before
a single quick start; a documentation corpus may need a reading order
rather than an installation command. A claimed feature lacking corroboration must be qualified or omitted, not upgraded through eloquent writing.

### 2. Lead with Why → What → How, then build technical depth

**Why, then What, then How is the binding communication sequence** for the
opening of a substantive public-facing repository README. First answer
what real problem exists, who experiences it, and why its solution matters.
Then explain *what* verified project capability addresses that problem,
with one concrete example or outcome. Next give a credible *how* to use,
evaluate, read or contribute. A banner, title, or badge must not displace
this explanation. Put practical value ahead of architecture, mathematics,
component inventories, and implementation mechanisms. The headings need
not literally say Why/What/How; a coherent introduction may use natural
prose. A rushed reader should understand the relevance within 30 seconds.

**Default introductions to approximately tenth-grade accessibility.**
Use short, concrete language, define technical terms at first use,
expand unfamiliar acronyms, defer equations and unexplained notation
to linked technical references, and introduce complexity progressively.
A readability score is a diagnostic only: both the accessible prose and
technical accuracy require deliberate editorial judgment. A novice should
be able to explain the project purpose without domain expertise.

The root README is the public front door, not an automatically generated
developer reference or a changelog. If `scripts/check_readme.py` emits
`CHRONOLOGICAL_LOG_ADVISORY`, inspect the section for a repeated dated
commit/PR running log. Move durable history to release notes or a maintained
history/evidence file when authorized, while retaining current user-facing
status and essential project context. This heuristic is **advisory only**:
it neither establishes a defective README nor fails the local checker.
Sparse milestone references, release summaries and fenced examples do not
justify automatic content deletion. Keep technical depth accessible by
linked developer references, architecture pages, specification or tutorial
material in repository-appropriate paths. If root README generation
overwrites human writing, inspect generator code, templates, build and
CI contracts; update the *true source* and output with parity evidence,
or restructure generator-owned references separately when authorized.
Never claim that a hand-edited generated output will survive regeneration.

**First-user success is a hard outcome gate.** A new reader should know
the first useful action *and* recognize an observable success result.
A generic dependency install, import list, lint command or cargo test
is not automatically evidence that a first-time user achieved the product
goal. Adapt the journey for a library, CLI, UI, service, dataset,
framework, research/specification repository or organization profile.
If no runnable first step exists, present an honest evaluation/reading
path and release limitation instead of fabricating one.

**Assets follow an explicit lifecycle.** Inventory project-specific
image source, purpose, owner/rights, accessible alt text, exact reference,
and status (verified existing, newly generated and committed, proposed
placeholder, approved final). Do not equate a preview or local temporary
image with the committed rendered README. Create missing assets when
authorized and add them to an appropriate permanent repository path.
Check the exact committed asset, including light/dark presentation where
relevant, and retain replacement requirements for placeholders.

Make the reader's first action **safe and actually applicable**: state
prerequisites, which repository/source checkout or published channel it
targets, execution effects or privilege needs, and a bounded observable
result. Prefer a real source-checkout example over a fabricated install.
When a command cannot be executed with current permissions, check that
its referenced entrypoint exists and mark runtime verification NOT_RUN.
Use the **five-second skim test**: the name, concrete function and next action can be found quickly. Use the **skeptical-engineer test**: the most important claim can be traced to actual code, release or measured evidence. Write concisely and naturally; no hype, fake adoption metrics or unsupported guarantees.

## Portfolio and multi-project information architecture: abstraction-first when useful

A README that introduces **a collection of repositories or components**
must help readers form a mental model, not merely provide an inventory.
When trustworthy evidence shows that projects occupy different conceptual
layers, **evaluate an abstraction-first presentation as the primary
navigation**. Start with the most recognizable outcomes and products,
then show the orchestration/interfaces that make them possible, then
shared services/frameworks, and finally the reusable primitives, core
libraries, protocols or specifications beneath them. The examples of
layers are *roles*, not mandatory headings or an architectural claim.

**This is a decision rule, not a universal forced hierarchy.**
A small collection of unrelated projects may be clearer as a flat
shortlist. Multiple independent product lines may need use-case groupings
or a two-dimensional index. A research catalog might be more useful by
topic or learning sequence. Choose the ordering that answers the
reader's actual question fastest; explain the chosen axis in plain
language. Do not treat chronology, release maturity, alphabetical order,
repository size, stars, or ownership as a substitute for abstraction.
Never assign a layer simply because the repository name sounds foundational.
Unknown roles belong in an explicit **Other or unclassified** group until
evidence supports placement, not in a fabricated dependency chain.

When building or improving a repository portfolio, organization profile,
multi-package monorepo or documented ecosystem:

1. **Inventory before composing.** From authorized canonical metadata,
   record every in-scope project, accurate link and intended audience;
   record its evidenced function, implementation status and relevant
   relationships. Scope/exclusions must be explicit. Do not silently drop
   small or less impressive projects.
2. **Identify conceptual altitude, not hypothetical dependencies.**
   Describe each project's role in one useful sentence. Distinguish
   `conceptual layer` (how to understand the collection),
   `integration` (verified interface), `dependency` (proven
   build/runtime prerequisite), and `roadmap` (planned relationship).
   A visual arrow or nesting must not turn an inferred relationship
   into a factual dependency claim.
3. **Choose and label a primary reader path.** When supported, orient
   from `experiences → coordination/interfaces → shared capabilities
   → primitives/foundations`. Offer a reverse entry for implementers
   when their most likely first action begins at the foundational
   layer. Use audience and conceptual labels instead of repeating
   jargon in every row. Place each project once in the main inventory;
   cross-link legitimately cross-cutting work rather than duplicate it.
4. **Preserve choice and scale.** Give each item a short description,
   a verified repo link, and status only if grounded. A few links
   can appear horizontally as a compact navigation strip; with many
   options, prefer grouped vertical bullets, a small table, or an
   accessible text outline. Avoid huge dense multi-column grids,
   ornate unsupported diagrams, and walls of nested headings.
   An optional diagram must have an equally useful text counterpart,
   accessible alt text, and source/rights evidence.
5. **Verify the result, not only the formatting.** Reconcile the
   revised entries against the canonical inventory and the previous
   README; flag omissions, duplicates, unsupported category labels,
   broken local anchors, inaccessible or stale destinations, and
   apparent arrows implying unverified dependence. Run a novice
   `where do I start?` task and an implementer `where is the
   underlying mechanism?` task. If independent readers are unavailable,
   mark both as controlled emulations, not observed outcomes.

A practical self-contained example and decision comparison are bundled
in [abstraction-first portfolio navigation](examples/abstraction-portfolio-example.md),
with adversarial cases in
[controlled scenarios](examples/controlled-scenarios.md).
**Do not copy a single organization's product taxonomy or identifiers
into other repositories.** This method is provider-agnostic and works
offline; outside repositories, diagram generators, or installed sibling
skills are not prerequisites.

### 3. Construct the right README, including from zero

For CREATE, build **the entire** `README.md` from scratch. First
classify what exists. An absent or empty project still receives a
truthful complete minimal document, not an outline or a promised draft.
Start with a factual project title, a concise value statement and
working navigation; add only sections and assets supported by the
project. Use the elements below as an adaptive menu, not obligatory
boilerplate.

For UPLIFT, complete the mandatory section-by-section disposition and generated-owner checks above before rewriting. Make a before/after preservation inventory of verified
unique content, existing voice, historical provenance, generated blocks
and links before rewriting. Compare the entire old and new documents,
not only the edited paragraphs. Keep important sources of truth unless
legitimately superseded and authorized. If generated spans or historic
issuer identities cannot be safely updated, preserve them and surface
the limitation, rather than silently changing them.

- Title with appropriate project identity; logo/banner and badge requirements follow the **selected quality profile**, not general preference.
- One-screen explanation of reader problem, product, main differentiator and first useful action.
- Small **real** quick start with prerequisites, source-compatible commands and expected observable output; if an install cannot be verified, mark the exact unverified step.
- Contents for longer READMEs; correct GitHub anchor generation and meaningful navigation.
- Functional capabilities grouped by user outcome, explicitly separating supported from roadmap/proposed items.
- Appropriate diagram, example or screenshot *only if evidence and asset rights support it*. Assets may be generated or changed only under the current user-authorized image/edit scope.
- Architecture orientation and maps to deeper maintained documentation rather than copy-pasting entire reference manuals. For a multi-project portfolio, evaluate an **abstraction-first map** with one-line roles and verified links before defaulting to alphabetic, chronological or release-order inventories; preserve the independent project's identities and unverified relationship boundaries.
- Verification methodology and realistic limitations (particularly for security, cryptography, AI, formal proofs, performance and medical/financial claims).
- License (only if evidenced), support/contribution/security reporting and release provenance when relevant.
- For empty/minimal repositories, honestly prefer a small functional README over a fake “complete” enterprise site.

Never invent working links, badges, release versions, platform support, build scripts, API endpoints, test results, maintainer contact addresses, sponsor programs or licenses. Dynamic badges are appropriate for changing facts only if their target and labels are verified; decorative badges are not achievement evidence. Never force a generated image or extensive table of contents onto a tiny **baseline-profile** project. Gold/Platinum presentation requirements are binding unless a justified exception is independently accepted.

### 4. Protect existing sources of truth

Inventory generated document sections, markers, source-driven tables, published artifact digests, signer identities, policy files and provenance-sensitive links. Preserve generated regions **byte-for-byte** unless the authorized generator is run and its output verified. Correct current canonical links while retaining historical cryptographic issuer identities where necessary. Do not duplicate volatile counters, counts, CI states or release support in text when a canonical register exists; link to it or date a verified snapshot.
Keep a README's opening and navigation oriented around **reader outcomes**,
not a chronological commit/PR changelog. Historical work belongs in
release notes, history or maintained evidence receipts. Check access,
rights and attribution before embedding or generating any image or
screenshot, and include meaningful alt text for informational images.

Prefer a focused change. Do not modify unrelated code, CI, governance, sensitive configuration or releases to make README claims true. If the user's requested narrative exceeds shipped functionality, disclose the gap rather than quietly expanding the implementation task.

### 5. Verify actual reader success and deliver

**Static minimum (whenever the source is available):** README exists and renders as Markdown; headings and TOC anchors match; relative links resolve; no broken internal asset references; important commands exist in actual CLI/config sources; badges and versions reflect the right repo; claims agree with source; generated content is intact; no unconsented information disclosure; no inaccessible images without alt text.

**Mandatory pre-delivery audit, optional executable assistance:** The
safeguards in A–D above are required decisions. The portable Python
3.9+ [delivery preflight](scripts/delivery_preflight.py) can detect
common formatter configurations, require a distinct original README
for UPLIFT, flag missing/stale section dispositions, detect explicit
generated-document ownership and evaluate **host-supplied** exact-head
CI receipts without running a workflow:

~~~text
python3 scripts/delivery_preflight.py --root /approved/repository --mode UPLIFT --readme README.md --baseline .review/README-before.md --dispositions .review/section-dispositions.json
~~~

Pass \`--mode CREATE\`, \`AUDIT\` or \`VERIFY\` for the other paths;
optionally add \`--head-sha <actual candidate commit>\` and
\`--ci-receipt .review/ci-receipt.json\`. The receipt schema and a
sample disposition are in the [bundled quality contract](references/readme-quality-contract.md).
The helper **never executes** formatters, reads GitHub ruleset policy,
authenticates a claimed CI receipt, validates the semantic correctness
of removals or declares a PR mergeable. Exit 0 means only that its
narrow deterministic blocker set was empty; it still reports
\`repository_merge_ready: false\`. If there is no Python/snapshot,
perform the same mandatory reasoning manually and mark execution
NOT_RUN.

**Optional repeatable offline links and generated-span checks:** The bundled Python 3.9+ standard-
library helper [scripts/check_readme.py](scripts/check_readme.py)
checks common local file links, heading anchors, reference definitions
and explicit generated-region markers against a supplied authorized
local repository snapshot. For a normal checkout:

~~~text
python3 scripts/check_readme.py --root /approved/repository --readme README.md
python3 -m unittest discover -s tests -v
~~~

For a generated block comparison, additionally pass
`--baseline .review/old-README.md` **only when that file exists
inside the approved root**. The tool is optional: use safer native
host capabilities, parsers or evidence-based manual checks when
appropriate. It reads but does not mutate files, rejects symlinked
paths and parent escapes, makes no network requests, never executes
README commands, and prints a bounded JSON record. Exit 0 means
**no detected blocker among the supported local checks only**, not
that the README is correct. It intentionally labels complex/unparsed
Markdown and external URLs as NOT_CHECKED; source/claim verification,
actual installability, user comprehension, privacy and
accessibility need independent assessment. The standalone
[method contract](references/readme-quality-contract.md)
describes inputs, statuses, blind spots and fallback. Never report a
script check as executed if the host did not actually run it.

**Stronger checks only when authorized and genuinely available:** verify external URLs and badges without secrets; test the quick start in a safe isolated environment; render Markdown/Mermaid; test install from an actual published artifact. An HTTP 200 does not guarantee the linked artifact is correct. No local shell means do not claim a locally executed test.

**Adversarial reader exercise:** simulate at least two perspectives using available evidence: (a) a newcomer asking “what problem, why this, can I start?” and (b) a skeptical maintainer asking “what is verified, what is not, where are the source-of-truth and policy boundaries?” Exercise an empty/new repo separately when validating CREATE. Controlled text emulations are not independent user tests.

If writing is authorized, deliver the actual README or a focused PR; avoid blocking on embellishments. State concrete artifact/reference, edits made, verified tests, not-run checks and blockers. Respect repository acceptance gates; a green unrelated workflow is not proof of README usability.

