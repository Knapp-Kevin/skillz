# Fresh skill discovery: security, identity and operational documentation (2026-10-27)

**State:** public discovery evidence, not source admission, package-security approval, behavioral validation or endorsement. The host performed all searches; `skillz` remains passive. This is a disjoint discovery slice relative to the October 26 waves and the earlier October 27 four-source and three-source records.

## Actual search coverage and deduplication

- **Public discovery surfaces (three distinct types):**
  1. GitHub repository topic discovery, rolling ~24-hour filter `topic:agent-skills pushed:>=2026-10-26T05:12:21Z`, first 30 returned repositories.
  2. GitHub full-description/keyword discovery, rolling ~7-day filter `"SKILL.md" pushed:>=2026-10-20T05:12:21Z`, first 30 returned repositories, plus current `"agent skills"` recent-push slice (30 returned).
  3. Public agent-skills marketplace/news discovery: the [SkillsMP Cognition listing](https://skillsmp.com/creators/cognitionai/devin-vuln-fixes) (three entries, source activity October 22) and the [October 24–25 public report](https://www.marktechpost.com/2026/10/24/cognition-devin-vulnerability-fixes-plugin-php2shell-nodejs-gitlab/) linking the canonical source. These are discovery pointers only, not exact provenance or quality evidence.
- **Search result exposure:** three capped GitHub slices of 30 each, with duplicates and many ordinary applications/aggregators. Do **not** report these as 90 unique eligible skills or exhaustive global results.
- **Four distinct selected canonical source leads**, individually resolved on GitHub, checked against the 22 registered source IDs and the October 26/27 discovery records, and queried by exact repository string against the current `skillz` code index (0 matching hits each). These are preliminary identity/alias deduplication checks; they do not establish exhaustive semantic novelty.
- **Complete Git tree counts at observed HEADs:** 3 + 1 + 30 + 1 = **35 distinct first-class SKILL.md paths** across these four source trees, all returned with `truncated=false`. This is **observed package exposure**, not 35 reviewed/approved skills. Three Cognition packages received individual source-vetting; the DavidHuji, Sentry and Auth0 samples below were read only as initial screening. The rest are unreviewed.
- **Newly recorded source leads:** 4; **fully source-vetted packages:** 3; **admitted source identities:** 0; **new third-party governed verification companions:** 0; **scanner passes:** 0; **behavioral validations:** 0. **Last successful new source discovery in this run:** 2026-10-27.

## Lead 1: CognitionAI/devin-vuln-fixes

- Canonical: https://github.com/CognitionAI/devin-vuln-fixes
- Observed HEAD `39a04007a1cb19aafd3c487d615c524479963ebf`, MIT LICENSE blob `dd8e23d2f78ed24988b13f746a79106085bc0374`, complete tree **3 SKILL.md**.
- **Disposition: EXTRACT / ADAPT ONLY, no unchanged admission**. All three exact packages were individually screened and failed current authority hard fail because discovery defaults can expand to every accessible repository, while sensitive build/test, PR publication and log disclosure are insufficiently bounded. Their explicit *pre-edit* approval, verified artifact, baseline/after evidence and rollback mechanics are strong extractable methods. Scanner and behavioral states `not-run`.
- **Evidence:** [exact three-package review](../reviews/2026-10-27-cognition-vulnerability-skill-family-vetting.md), [candidate issue #427](https://github.com/Knapp-Kevin/skillz/issues/427).

## Lead 2: DavidHuji/PHP2Shell-SKILL

- Canonical: https://github.com/DavidHuji/PHP2Shell-SKILL
- Observed HEAD `58bd9ef65f973da5887ce205316fd0b5c0b7afa3`; root MIT LICENSE text inspected; complete Git tree **1 SKILL.md**, `skills/php2shell/SKILL.md` blob `c7bfd76fcf6696a41c80d64965a9b6546d960ad4`.
- **Disposition: REFERENCE-ONLY / selective extraction**, no unchanged admission. The source advertises `curl .../install.sh | bash` installation and a shell helper that can inspect local containers and propose production mitigation. The manifest requires user approval before edits and explicitly says not to run `sudo` automatically; nevertheless shell provenance, installation safety, production scope, credential handling and complete package security are unqualified. Strong overlap with Cognition PHP skill; do not count it as a separate new *capability* without a mechanism comparison.
- No installer, script, vulnerability scan or production mitigation executed.

## Lead 3: getsentry/skills

- Canonical: https://github.com/getsentry/skills
- Observed HEAD `d12f250460ffd961f549dbebf7eeb0cf4afd4c2e`; root Apache-2.0 LICENSE text inspected; complete Git tree **30 SKILL.md** paths. Representative `skills/agents-md/SKILL.md` blob `bd92e4a9df47f63bd943bc3d5011da0b3d6e04ff`.
- **Disposition: TRACK / selective source-vetting**, not admitted. README explicitly says these are skills for Sentry employees; some procedures may be internal-context-dependent or not useful unchanged outside that organization. The `agents-md` sample has a concise, reference-backed AGENTS/CLAUDE instructions method but also writes repo files and prescribes commit attribution; scope/authority and fit must be evaluated. Other 29 manifests remain unreviewed. Differentiate public general-purpose methods from employee-specific internal procedures before issue-first admission.
- This is distinct from the separate `getsentry/sentry-for-ai` repository linked in the README. Do not conflate the two.

## Lead 4: auth0/agent-skills

- Canonical: https://github.com/auth0/agent-skills
- Observed HEAD `7b3821d533430eef35fd7406a87b7b8d02302bdf`; root Apache-2.0 LICENSE text inspected; complete Git tree **1 SKILL.md** at `plugins/auth0/skills/auth0/SKILL.md`, blob `938748737b2ee8ed1f9ad6197925366e6699b809`. Many bundled reference assets exist; 312 tree entries are **not** 312 skills.
- **Disposition: TRACK / high-authority selective vetting**, not admitted. The consolidated Auth0 v2.6.0 skill routes authentication, token, tenant, RBAC, MFA, custom domain, branding and security audits through framework-specific references. Its broad trigger can activate even when Auth0 is not mentioned. Auth0 CLI installation, private identity/tenant data, credentials, tenant mutations, security controls, custom domains and paid plan changes require explicit per-action authorization and secure secret paths. No credential/tenant access or tool execution occurred.

## Macro synthesis and next frontier

**Discovery is not the bottleneck.** This slice exposes 35 canonical first-class manifests in four previously unregistered sources. Yet exact quality and operational trust remain different questions. High-value new material clusters around (a) artifact-verified security patching, (b) concise agent instructions, and (c) identity integration. The recurring risks are broad implicit repository access, external action and credential authority, private telemetry, networked build scripts, volatile vulnerability targets and duplication.

**Next bounded discovery priority:** Auth0's single high-authority router with its bundled reference tree, or a coherent Sentry subset after source-level public-vs-internal partitioning. Do not create an unowned issue for all 30 Sentry skills. Independently keep existing first-party PR #416's exact 21-package external security gate in its own lane.

**Public accounting effect:** `README.md`, `docs/SYSTEM_STATE.md`, `CURATION_QUEUE.md`, `INDEX.md`, `index.json`, and `registry/sources.yaml` unchanged. First-party **44**, source identities **22**, persisted third-party exact-version reviews **721**. The source-family denominator delta is **0** because none of these four discoveries has been admitted.
