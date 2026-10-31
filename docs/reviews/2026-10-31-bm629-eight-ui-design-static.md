# Bhushan Modi: eight UI design and implementation exact-pin reviews (2026-10-31)

## Scope and macro-first denominator
Registered tracked source `bm629/agent-skills`, MIT, exact pin `f6a700ea94a16cf8e0b5e563d4d48d85503e41f6`. Direct pinned-tree enumeration: 68 first-class `skills/<name>/SKILL.md` packages, no counted nested first-class packages or duplicate aliases. Before this tranche, 26 exact-version provenance/verification pairs existed and 42 genuine gaps remained. The eight selected gaps are disjoint from the 26 prior companions and from all five held first-party PRs. After: 34/68 governed, 34 gaps, no source-pin or admitted-denominator change.

The 42-gap frontier divides into: UI wireframes/hi-fi and adjacent implementation; document discovery/review; large market, visual, security and user-research prior-art families with 30+ bundled files and validators requiring separate deep inspection; developer-tool/framework references; and provider operations (Atlassian, Cloudflare Pages, Jenkins, GitHub CLI, Netlify) with higher authority risk. This tranche isolates eight coherent UI-design and implementation procedures, rather than mixing high-authority provider operations or pretending to review the large prior-art packages in bulk.

## Individual exact-version decisions

| Package | Files (including SKILL.md) | Score | Static decision | Decisive finding |
|---|---:|---:|---|---|
| `authoring-hi-fi` | 4 | 14/20 | REJECTED | mandatory generation and headless rendering of code with realistic content and CDN-permitted assets, followed by persistent screenshots, lacks an explicit authorized data scope, network-egress/sandbox boundary, and screenshot destination/retention gate |
| `reviewing-hi-fi` | 3 | 14/20 | REJECTED | independently re-rendering submitted code and screenshotting every viewport/state is mandatory, but the procedure does not establish isolation, network denial/approval, authorized private input scope or screenshot disclosure/retention before executing potentially untrusted UI |
| `authoring-wireframes` | 4 | 17/20 | VERIFIED | produces annotated textual/ASCII screen structure with inventory, empty/loading/error/recovery states, responsive and accessibility composition, scoped amendments and explicit missing-input assumptions |
| `reviewing-wireframes` | 3 | 16/20 | VERIFIED | independent text-only approve/revise gate checks screen/state coverage, buildability, accessible names, annotations and bounded delta scope without editing or executing |
| `design-review` | 2 | 18/20 | VERIFIED | scoped adversarial pre-approval gap review verifies claims with file:line evidence, avoids whole-tree scans, distinguishes recommendations from human sign-off, and writes review.md only on explicit opt-in |
| `motion-react` | 6 | 14/20 | REJECTED | Step 2 directly instructs npm install motion and app-root MotionConfig mutation without an independent approved dependency, network/supply-chain and repository-change scope |
| `react-component-testing` | 6 | 16/20 | VERIFIED | user-visible component tests mock the network at MSW with onUnhandledRequest:error, assert serialized request bodies and accessibility, and separate the test layer from runner/CI ownership |
| `ui-illustrations` | 5 | 16/20 | VERIFIED | explicit live per-asset license recheck and provenance/attribution record, consistent illustration family, token-safe theming, accessible alt/decorative treatment and reduced-motion defaults |

Every package has its own exact pin, Git package-tree SHA, SKILL.md blob, upstream last-change commit/date, bundled reference inventory, dependency and authority characterization, controlled tags, score/rationale and explicit `validation_status: not-run`. These are static semantic judgments, not executed tests, security passes or unchanged-use approvals. The upstream source's own documentation, tests and scripts remain source-owned evidence, not repository runtime.

## Macro findings

1. **Render/vision evidence needs an authorization boundary.** The hi-fi author and reviewer both require executing or re-rendering code and retaining screenshots. Neither establishes network isolation/egress approval, private screen-content scope or screenshot retention/destination before doing so. Both are REJECT unchanged despite strong bounded render-and-review methods.
2. **Package installation is an action.** `motion-react` gives `npm install motion` and app-root changes as a default step. Its reduced-motion and performance guidance is valuable, but the dependency and repository mutation need separately scoped host authority.
3. **Review rubric drift is real.** The hi-fi author includes a conditional capability condition beyond the reviewing reference's stated 13. The wireframe reviewer lists 15 conditions while its expanded reference advertises 13. Both need a single canonical applicable-condition map before automated verdict parsing is trusted.
4. **Good bounded methods remain.** Textual wireframes, independent wireframe review, generic design-review, network-intercepted React component tests and license-aware UI illustrations supply differentiated, reusable design/verification knowledge. `react-component-testing` has a disclosed network-restricted forge and requires fresh version/API confirmation; `ui-illustrations` requires current per-asset licensing and attribution checks.
5. **No fabricated validation.** No browser render, screenshots, npm install, external source scan, test execution, network access to private inputs, or behavioral/adversarial acceptance occurred. All eight retain `not-run` validation and no package-security pass.

## Accounting and lifecycle

Source 68 → 68; current-standard companions 26 → 34; genuine gaps 42 → 34. Third-party persisted reviews 891 → 899 (registered/tracked 770 → 778; candidate-only 121 unchanged); first-party 44 unchanged; total verification/provenance pairs 935 → 943. README, SYSTEM_STATE, CURATION_QUEUE, INDEX and index.json reconciled together. Corrected a stale current-depth line in CURATION_QUEUE that still said 867/746 and a relative link in SYSTEM_STATE. No source admissions or candidate discovery decisions.

Open first-party drafts #489 (29), #492 (5), #496 (2) remain DRAFT/HOLD pending pinned SkillSpector v2.12.0 complete exact-tree reports and independently executed adversarial acceptance for 36 distinct changed trees, then shared-registry reconciliation. Draft admissions #412/#413 require separate qualification. Their seven associated open issues are not evidence-complete; no false closure or merge is warranted.

## Next frontier

Continue bounded review of remaining 34 Bhushan Modi gaps, separating the large prior-art research/validator packages and provider operations for deeper source/authority/privacy assessment. External first-party qualification remains the highest priority when evidence becomes available.
