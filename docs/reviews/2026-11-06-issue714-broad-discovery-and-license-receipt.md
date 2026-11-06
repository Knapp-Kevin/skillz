# Issue #714: Broader corpus discovery and rights receipt

**Run date:** 2026-11-06. **Scope:** Healthcare Contract Forensics and adjacent PBM, payer/insurance, medical billing/claims, reimbursement and contract-review methods.

This is a **real bounded corpus-index search**, not a claim to have read the bodies of 61,326 skills. It corrects the prior 1,039-name-only search and demonstrates the [full-corpus discovery contract](../discovery/full-corpus-search-contract.md).

## What was searched

| Lane and snapshot | Records queried | Method | Relevant signal / limitation |
|---|---:|---|---|
| G1 pinned identity shards 1–6 (2026-11-03) | **27,832** | Checked all six JSON record arrays; repository/path keyword search | **124** lexical candidates |
| G2 pinned identity shards 1–4 (2026-11-03) | **17,939** | Checked all four record arrays; same query | **41** lexical candidates |
| G3 pinned identity shards 1–4 (2026-11-03) | **15,555** | Checked all four record arrays; same query | **68** lexical candidates |
| **G1–G3 combined** | **61,326** | **All 14 published shards successfully parsed** | **233 lexical hits**, not 233 unique, eligible or semantically relevant skills |
| OpenAI plugins capability index (2026-11-02) | 536 | Paths plus capability description | 0 exact healthcare-contract keyword hits |
| j4flmao capability index (2026-11-02) | 555 | Paths plus capability description | 1 incidental technical “health contracts” usage, not a healthcare contract auditor |
| AgentSkillExchange capability index (2026-11-02) | 3,199 | Paths plus capability description | 2 healthcare-themed hits, job search and FHIR, not an employer contract audit |
| Awesome Copilot capability index (2026-11-02) | 313 | Paths plus capability description | No direct keyword match |
| Q1–Q5 additional-source capability-routing ledgers (2026-11-03) | Five indexed ledgers | Inspected path/name/capability text | General contract-review and healthcare-law leads, not an identified PBM-specific replacement |
| Historical governed name index (2026-11-01) | 1,039 | Earlier name-only search | Adjacent reviewed general legal/contract/audit skills; **not corpus boundary** |

**Lexical filters:** case-insensitive matches in repository name or skill path for `healthcare`, `health-care`, `insurance`, `insuranc`, `pbm`, `pharmacy`, `pharmac`, `claims`, `medical-billing`, `billing-claims`, `reimburs`, `contract-audit`, `contract-review`, `payer`, `rebate`, `benefit-plan`, `medical-coding`, or `contract-law`. The four capability indices also used declared capability-description keywords.

**Important denominator limits:** G1–G3 are exact pinned package-identity *records*, including duplicate/versioned and off-task rows. The four-source indices have partly overlapping but nonidentical population definitions, not an additional count of unique eligible skills. The corpus is open-ended beyond dated source pins. The 233 hits exclude relevant skills whose names/paths do not mention a chosen term. This exercise was **index-wide lexical discovery**, not whole-corpus semantic review, behavioral testing, or current upstream revalidation.

## Actual skill files inspected at exact pinned sources

| Candidate | Pinned skill SHA | Root license inspected at same pin | Suitability / decision |
|---|---|---|---|
| [aks-builds/healthcareskills billing-claims](https://github.com/aks-builds/healthcareskills/blob/fbd2863bb77db173d33cce122daa0a1867b40d75/skills/billing-claims/SKILL.md) | `eecd39d69957bcd5950ab25fd8ead1e5a543e601` | **MIT** root LICENSE SHA `0b5fe9e75e8a87257a73160d3bcfeea1ac16383b` | US claims-processing/EDI *software engineering*, not fiduciary PBM contract forensics. Requires complete supporting-file review before adaptation. No import. |
| [aiunlocked1412/claude-skill-unlock insurance-advisor](https://github.com/aiunlocked1412/claude-skill-unlock/blob/f40e6c332784b7bd66999dd52aafa58cfd4c3816/skills/05-business/insurance-advisor/SKILL.md) | `72559faf11e2375581cbce4450d9c5883276aeb0` | Root `LICENSE` not found at pinned revision, **rights unresolved** | Thai consumer insurance advice, not US employer/PBM contract review. No material reuse. |
| [AlsKozlov/ru-legal contract-review](https://github.com/AlsKozlov/ru-legal/blob/7bfba770f6b2352c2308f3532e00be90924de323/packs/contract-law/skills/contract-review/SKILL.md) | `f0c955ea1cbd1588295b0a837791d04f2ecdae2f` | **Apache-2.0** root LICENSE SHA `25d4fd41d0ddcf1848685f4a018c00334bcd80b6` | Russia-specific legal contract review, with host/MCP assumptions. No import; jurisdiction wrong for current fixture. |
| [Autter-dev/agentic-sales-skills contract-reviewer](https://github.com/Autter-dev/agentic-sales-skills/blob/ed5191cb340be3100c9c7f33ed54584eea1f7823/04-proposals-and-close/skills/contract-reviewer/SKILL.md) | `34dc492a8b47c02c7d65adf3170b51de483bf775` | **MIT** root LICENSE SHA `593d62d3cfc489ad1d9a054a4678e807303b4d3d` | SaaS MSA/order-form negotiation, not health-benefit economics. No import. |
| [takusaotome/claude-skills-library contract-reviewer](https://github.com/takusaotome/claude-skills-library/blob/dd1fb14d0fc6937104657c9ff1770abc57e81683/skills/contract-reviewer/SKILL.md) | `46bcd9e58b0c66ffa1e08df12f9d3896ee694086` | **MIT** root LICENSE SHA `1d3316873bc75c676c76022840410006dc2f1369` | General business legal review; optional PDF/Python reliance and fixed risk scores. No import. |

**Rights caution:** A root license observed at an exact source pin is not by itself evidence that every required supporting file, nested library or third-party asset has the same rights. This receipt does **not** grant blanket permission to redistribute or adapt any of these packages. The new first-party Healthcare Contract Forensics text and fictional fixtures were independently authored without copying their protected text.

## Findings and next qualification

1. **The earlier 1,039-index search was inadequate for a no-equivalent claim.** The G1–G3 path corpus includes a concrete US healthcare billing/claims engineering skill plus contract-review skills outside the governed name index.
2. **No exact-reviewed five-candidate fit replaces the proposed employer/PBM financial workflow.** General legal structure, insurance advice and medical-claims software engineering are related but materially different tasks. This does not exclude an uninspected specialist elsewhere in the corpus.
3. **Licence checks found material variance.** Four pinned roots present MIT/Apache-2.0 licenses; the Thai insurance-advisor root `LICENSE` was unavailable. Actual permitted copying still depends on the complete material and nested rights.
4. **CREATE remains a supported provisional engineering choice, not a monopoly/novelty assertion.** Original authoring is a conservative way to avoid copying and to tailor to PBM definitions and reconciliation evidence.
5. **Unfinished:** full package and companion inspection for other top candidates, deeper semantic/index searches across versions and adjacent subdomains, reconciled duplicate/source identities, independent external host prompt-vs-skill testing and legal expert review. These remain open acceptance tasks, not invisible skips.

This is a **search receipt**, not a measured improvement, external scanner PASS, legal certification, or instruction to install/execute candidate packages.


## Follow-on deeper review and authored layout (2026-11-06)

Four additional complete exact-pinned source-package directories were independently inspected, including supporting references, fixtures and Python scripts (without execution). See the [full-package fit and rights receipt](2026-11-06-issue714-package-candidate-comparison.md). The first-party skill package is now stored under `skills/authored/healthcare-contract-forensics/`, recorded as `MIT` in `registry/authored-skills-index.json`, and fingerprinted in its current nine-file [static review](2026-11-06-issue714-healthcare-contract-forensics-static-review.md). No third-party content was copied or imported; no independent behavioral study was performed.
