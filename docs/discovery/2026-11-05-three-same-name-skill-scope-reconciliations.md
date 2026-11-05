# Three source-pinned same-name skill scope reconciliations (2026-11-05)

**Issues:** #624 (identity/throughput), #599 (discovery), #588 (capability mapping).  
**Type:** passive research evidence. No package imported, installed, executed, graded, security scanned, approved for unchanged use, or marked behaviorally validated.

## Question and method

The four-source identity crosswalk `registry/discovery/pinned-four-source-identity-crosswalk-20261102.json` flags 14 cross-source same-leaf-name groups containing 35 paths. A shared leaf name is not sufficient to collapse identities or to declare that two skills supply identical capabilities. This tranche reads six actual pinned upstream `SKILL.md` files, two per name. The exact paths, source revisions and returned Git file blobs below preserve independent source identity. Bundled references, plugin manifests, package-tree hashes, licensing obligations, and executable behavior are **not** fully inspected here. Therefore these are **scope/routing distinctions**, not complete-package terminal reviews.

| Shared leaf | Official OpenAI plugin source at `0722921d5542fc593105c27bd52630babd8b8c2a` | Community source `j4flmao/agent-skills` at `982203e52afe0b726a7847599a8bfb293890e0c5` | Observed difference in source-declared coverage |
|---|---|---|---|
| `nextjs` | `plugins/vercel/skills/nextjs/SKILL.md`, Git blob `ab252649c550cd34a5fac7e7a03d5c9f0a796767` | `skills/frontend/react/nextjs/SKILL.md`, Git blob `bab0c7cda0973c08e75ec46f0850b9757ef5827b` | Both address Next.js App Router. Official plugin explicitly covers v15/16 migration, cache/runtime/directive semantics and links multiple detailed reference files; community skill emphasizes generated component structure and application architecture. **Potential functional overlap**, but neither source identity nor package evidence may be collapsed. |
| `supabase` | `plugins/supabase/skills/supabase/SKILL.md`, Git blob `198c9855058fb6db3e865b3f8b766d2f0156a2f1` | `skills/backend/universal/supabase/SKILL.md`, Git blob `89da9ae3fe03265079f44a73643fdaf9bbec520b` | Both cover Supabase. Official plugin explicitly begins with changelog/current-doc verification and post-change testing, plus auth/data API troubleshooting. Community version emphasizes schema, RLS, storage, auth, realtime and edge-function output artifacts. **Overlapping service, different procedures**, not a proven mirror. |
| `observability` | `plugins/vercel/skills/observability/SKILL.md`, Git blob `39653194f418bab7fb0016f404b2720020d8f706` | `skills/devops/observability/SKILL.md`, Git blob `db11c5691064fe850140a75ba1d60e20566ccf3b` | Official plugin targets **Vercel platform** log/trace drains, Web Analytics, Speed Insights and telemetry integration. Community version targets **stack-agnostic services**, structured logs, OpenTelemetry, metrics, SLOs and symptom-based alerts; explicitly excludes frontend analytics. These are **complementary routing scopes**, not an interchangeable duplicate. |

## Consumer-facing routing consequence

- For a Vercel-hosted web app's Speed Insights or Analytics configuration, the Vercel-specific observability skill is a more directly scoped *candidate*; for service-wide OpenTelemetry and SLO planning, the general observability skill is a more directly scoped *candidate*. Neither is an approved install recommendation.
- For Next.js and Supabase, retain **both** separately and request actual task, framework version and host context before comparing candidate methods. Shared subject matter is not source/code identity, package safety or quality.
- Preserve upstream source ownership and package terms. `openai/plugins` uses per-plugin licenses and may bundle third-party content; community front-matter claims are insufficient as complete-package redistribution clearance.

## Bounded evidence and remaining work

**Observed:** 3 of 14 flagged cross-source same-name groups have been read at their six exact pinned source blobs and have documented distinct routing scope or potential overlap. **Not established:** complete package tree identity, bundled reference coverage, upstream license-chain admissibility, static security state, individual 10-dimension review grade, actual usefulness or comparative runtime behavior. Do not subtract six entries from the 4,813 raw-path denominator, add any approved skills, or change public counts.

**Next qualified tranche:** independently inspect whole package trees and rights for these six candidates and adjudicate semantic overlap versus complementary method at the complete-package level. Continue the other 11 same-name groups and reconcile distinct governed review identities. The first-party/third-party security backfill remains under #402, and the eligible distinct denominator remains UNKNOWN.

**Source evidence:** exact pinned upstream paths and Git blob identities listed above, compared against `registry/discovery/pinned-four-source-identity-crosswalk-20261102.json`. This record makes no claim of elapsed reviewer-time improvement, so #624 throughput acceptance remains OPEN.
