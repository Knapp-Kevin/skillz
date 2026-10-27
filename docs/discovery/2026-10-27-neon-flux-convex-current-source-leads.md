# Current public discovery: Neon, Flux and Convex skill source leads (2026-10-27)

**State: three new candidate source leads, selective vetting only; no admission, installation, execution, package-security pass or behavioral validation.** All discovery and GitHub inspection were performed by the external host. `skillz` remains entirely passive.

## Actual discovery funnel

- **Current public discovery surfaces:** (1) GitHub repository search for agent skills pushed since **2026-10-26** (recent-update signal); (2) GitHub `SKILL.md` description search for repositories pushed since **2026-10-20** (seven-day discovery window); (3) public skills-directory and Hugging Face official skills documentation checks. GitHub search terms were rotated across name/description and `agent-skills` variants.
- Three GitHub repository search queries returned **75 rows** in total, representing **70 distinct canonical repository names** after name-level deduplication (**5 overlapping result rows**). This is **not** 70 new skills or 70 new eligible source families. Many hits are already registered or previously reviewed, including Microsoft, Vercel, Google, Matt Pocock, K-Dense, Sentry and Auth0.
- Three distinct, potentially differentiated source repositories were selected for actual README/license/manifest inspection. Exact canonical name strings returned **0 code-search hits** within current `Knapp-Kevin/skillz`, but this is preliminary and does not prove absence from every prior ledger alias or issue.
- **Source leads directly inspected: 3. Representative SKILL.md manifests individually read: 3. Direct package directory entries observed: 45 (9 + 3 + 33).** These 45 directory entries are **not** an eligible first-class SKILL.md denominator; nested first-class manifests, aliases, mirrors and generated exposure paths have not been exhaustively resolved. **Admissions: 0.** No repository-owned crawler, scripts, scheduler, CI, scanner or installer introduced.

## Source-family macro map

| Canonical source and immutable observed HEAD | Root license evidence | Observed direct package directories | One exact manifest read and preliminary disposition |
| --- | --- | ---: | --- |
| [Neon Agent Skills](https://github.com/neondatabase/agent-skills) `0ec3f2e270c5c04955e1db61f2eb31911137b6fd` | Apache-2.0 root blob `d645695673349e3947e8e5ae42332d0ac3164cd7` | **9** under `skills/` | [`neon-postgres-branches`](https://github.com/neondatabase/agent-skills/blob/0ec3f2e270c5c04955e1db61f2eb31911137b6fd/skills/neon-postgres-branches/SKILL.md) blob `d9cc2f8ac1f9aafcc992695037461683c533df73`: **ADAPT/EXTRACT candidate** |
| [Flux CD Agent Skills](https://github.com/fluxcd/agent-skills) `de81eb4ed7e991cac9da05adc2271b1bea8a4304` | Apache-2.0 root blob `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64` | **3** under `skills/` | [`gitops-cluster-debug`](https://github.com/fluxcd/agent-skills/blob/de81eb4ed7e991cac9da05adc2271b1bea8a4304/skills/gitops-cluster-debug/SKILL.md) blob `2b32375259f8a97131b90f4244f39ca9ac23f22a`: **SELECTIVE VET** |
| [Convex Agent Skills](https://github.com/convex/agent-skills) `bd403cb048c8bb6c1e99d898e15ed61f9ddd430b` | Apache-2.0 root blob `c61b66391a3c1545c8c274bc6d7d764bafb84993`; README warns that older revisions may differ | **33** under `skills/` | [`convex-migrate-rehearse`](https://github.com/convex/agent-skills/blob/bd403cb048c8bb6c1e99d898e15ed61f9ddd430b/skills/convex-migrate-rehearse/SKILL.md) blob `85c881c07a72a19d7f4fc879d91b016e41d6a281`: **SELECTIVE VET / possible high-value governed pattern** |

### Neon: real-data branching and cloud resource authority

The inspected `neon-postgres-branches` manifest distinguishes realistic data branches from schema-only branches for sensitive workloads, identifies CLI/MCP fallback, and documents migration-test branches. The core workflow says to **create** a cloud branch, including from production-like data. It also recommends `neon skills -s neon -y` if the parent skill is unavailable. This is upstream installation guidance, **not** an instruction for `skillz` to install anything. Missing explicit project/parent/data-copy/cost authorization before creating or resetting a branch is a hard unchanged-use concern. **Preserve** the schema-only privacy distinction and parent-source check for adaptation.

### Flux: valuable read-only diagnosis but consequential cluster actions

The `gitops-cluster-debug` manifest requires `flux-operator-mcp v0.60+`, distinguishes read-only tools from mutating tools, masks Kubernetes Secret values and traces live resource ownership. Its **Changing the Cluster** section says not to mutate unless the user explicitly asks and recommends preview via `diff_kubernetes_manifest`. Those are useful safeguards. But a general request to debug is not automatically approval to `apply_kubernetes_manifest`, `patch_kubernetes_resource`, delete resources or reconcile production traffic. **Deep-vet** context binding, resource scope, finalizer/rollback consequences, logs and credential leakage, and exact preview-versus-apply boundaries. Source-owned Flux Operator/OCI/cosign installation remains upstream evidence, not repository machinery.

### Convex: a differentiated explicit-approval rehearsal mechanism

The `convex-migrate-rehearse` manifest describes snapshot-seeded preview deployments, schema validation, optional-then-tighten backfills and a production promotion gate. Unlike many generic cloud skills, it explicitly requires a **fresh yes** before production promotion and warns that snapshot restore loses writes after the snapshot. That is a promising, concrete authority mechanism, but **not** proof of complete security: exporting production snapshots, using preview deployment keys, transferring private data, paid-tier preview creation, local snapshot deletion and any promotion still need separately scoped authorization and privacy controls. The manifest is marked **generated from upstream capability JSON**; evaluate its canonical source and dependencies before treating it as an independent reusable procedure. Do not execute `npx convex` or access real data.

## Dispositions, omission risk and next intake

- **Neon:** ADAPT/EXTRACT candidate; differentiated schema-only branching, but remote database/resource authority and data-copy consent remain unresolved.
- **Flux:** SELECTIVE VET; potentially useful read-only incident triage and GitOps ownership tracing; mutating cluster tools and logs require deep adversarial inspection.
- **Convex:** SELECTIVE VET; the explicit production promotion gate and rehearsal mechanics are especially worth evaluating against existing cloud migration and safety patterns. Generated skill wrappers may duplicate canonical capability material.

No candidate issue was opened merely to park these leads. When one source is selected for actual admission, use a bounded issue-first review, establish its complete canonical SKILL.md denominator and per-package license/dependency/authority evidence, make a terminal disposition, and close the issue. Do not treat source reputation, official branding, freshness, installation counts or successful CLI examples as permission or quality evidence.

**This pass:** GitHub search **75 raw rows / 70 unique repositories**, three additional canonical source leads characterized, **3** exact manifests inspected, **0** admissions, **0** new verification companions, **0** package-security passes, **0** behavioral validations, **0** catalog changes. Together with the independently documented Supabase lead, this cycle recorded **four** new candidate source leads without inflating the 22 registered source identities.
