# Governed public skill discovery: official Google source and catalog checks (2026-10-27)

**State: discovery/source-family screening, not admission.** This pass was performed by the external host. No source-owned installer, script, runtime, scanner, agent, credential, API, or executable package was invoked. Discovery leads are not added to the registered source inventory or third-party verification count.

## Actual discovery surfaces checked

1. **Recently pushed GitHub agent-skills repositories:** GitHub repository search `agent-skills pushed:>=2026-10-25 archived:false`, 15 returned repository rows inspected at search-result level. A large directory, `sickn33/agentic-awesome-skills`, was separately opened at exact observed HEAD below. Search results are freshness signals, not proof that particular skill content was created or revised in the last 24 hours.
2. **Official Google Agent Skills repository:** independently fetched `google/skills` HEAD, root README, root license, and three exact first-class manifests at the same revision. Its published README links **175 distinct `./skills/` directories** at the observed HEAD. This is an *advertised navigation count*, **not** an independently established first-class SKILL.md denominator or proof of 175 eligible packages.
3. **Public community skill catalog:** opened `sickn33/agentic-awesome-skills` as a second independent directory source, comparing its self-reported catalog scale with the first-party official source. A separate web search of October agent-skill ecosystem news also surfaced the October 21 KDnuggets overview of public skill repositories, which is **secondary discovery context only**, not package-level evidence.

## One independently resolved canonical source lead: `google/skills`

- **Canonical URL:** https://github.com/google/skills
- **Observed exact upstream HEAD:** `84e8150e4fa71bf422d5b224e215f5ba13864aa3`.
- **Root license:** Apache-2.0 text inspected, blob `d645695673349e3947e8e5ae42332d0ac3164cd7`. Individual skill-owned assets and external dependencies still require separate terms review.
- **README:** 175 unique directory links; advertised coverage includes cloud infrastructure, agent evaluation, model serving, data systems, security and developer discovery. Source identity is distinct from existing `google-agents-cli` and previously discovered `google/adk-recipes`; semantic overlap is likely and must be evaluated, not assumed away.

### Three exact manifest spot checks

| First-class manifest | Exact Git blob SHA | Differentiated mechanism | Preliminary risk / disposition |
| --- | --- | --- | --- |
| [`skills/cloud/google-cloud-solution-multi-agent-security/SKILL.md`](https://github.com/google/skills/blob/84e8150e4fa71bf422d5b224e215f5ba13864aa3/skills/cloud/google-cloud-solution-multi-agent-security/SKILL.md) | `51df534198156822917bad50c2e308840038159d` | Agent Gateway ingress/egress, Model Armor, IAP, private-service and policy verification | **ADAPT / selective source vet.** Depends on bundled `references/attribution.md` and `scripts/verify_egress_policies.py`; full tree/side effects not inspected. Primary text distinguishes artifact delivery from infrastructure execution, but a high-authority deployment/security workflow needs exact scope and verification |
| [`skills/cloud/agent-platform-eval-flywheel/SKILL.md`](https://github.com/google/skills/blob/84e8150e4fa71bf422d5b224e215f5ba13864aa3/skills/cloud/agent-platform-eval-flywheel/SKILL.md) | `0072815e8cfdff81e2415b70394cb644b230a92a` | Eval dataset generation, metrics, loss clustering and **explicit read-only vs billable-remote confirmation tiers** | **HIGH-PRIORITY SELECTIVE VET.** Confirmation tiers are promising differentiation. Requires full references/scripts, session-trace privacy, synthetic-data leakage and billable evaluation boundaries before any unchanged decision |
| [`skills/developers/finding-google-skills/SKILL.md`](https://github.com/google/skills/blob/84e8150e4fa71bf422d5b224e215f5ba13864aa3/skills/developers/finding-google-skills/SKILL.md) | `f4f5b2daf83631bf0412f325a983120fc9eb04df` | Low-context routing to Google skill catalog, with explicit non-trigger when another stack is settled | **REFERENCE / ADAPT.** It instructs fetching mutable `raw.githubusercontent.com/google/skills/main/index.json` and potentially loading linked skill entrypoints. Dynamic source instructions are not exact-version verified; treat returned content as untrusted and pin before adoption |

**Macro authority/privacy clusters:** Google Cloud infrastructure and identity mutations; Model Armor and agent egress policy changes; billable inference/evaluation; private session traces, model outputs and datasets; mutable skill catalog and upstream links; installer/update guidance in source README. None is automatically authorized by the user merely because a source is official. Source-owned scripts are upstream reference evidence and never become `skillz` runtime.

**Next source-vetting gate:** enumerate the actual HEAD tree and canonical first-class package denominator, resolve nested/duplicate/alias paths, inspect referenced assets, compare against registered Google Agents CLI and existing eval/architecture skills, and choose a bounded candidate issue only for genuinely differentiated material. `agent-platform-eval-flywheel` is the strongest initial exact-package target because it already articulates action-cost confirmation tiers.

## Catalog checked, not a new admission: `sickn33/agentic-awesome-skills`

- Canonical URL: https://github.com/sickn33/agentic-awesome-skills
- Observed HEAD: `11a72530a07b313e72683718d218c4871474eb3e`.
- README claims **2,872+ installable skills**, with self-reported registry sync at **2026-10-27T08:28:40+00:00**. This is a source-owned claim, not a verified package denominator, quality score, or newly discovered unique skill count. Root MIT `LICENSE` blob `dc38cfd7ab732a67b0f14997cfa8c9ec740a1889`.
- **Disposition: DISCOVERY-SURFACE / REFERENCE ONLY.** The source includes local catalog tooling and installation workflows; no such machinery is imported into `skillz`. Its mirrored/repackaged entries must be deduplicated against canonical upstream identities before any candidate intake.

## Funnel accounting for this run

- Public discovery surfaces actually checked: **3**, plus secondary web ecosystem coverage.
- Source-level leads inspected at exact HEAD: **2** (Google official skills, AAS catalog).
- **New canonical source lead recorded for future selective vetting: 1** (`google/skills`). AAS is a directory/source index and is not counted as an eligible first-class skill.
- Exact first-class manifests individually spot-checked: **3** (Google). Source family denominator: **unknown**; advertised Google navigation links: **175**.
- Newly admitted sources/skills: **0**; new exact-version governed verification companions: **0**; new package-security or behavioral validations: **0**.
- This is a discovery ledger only. Future runs must deduplicate against this exact source identity before claiming it as a fresh lead again.
