# AgentSkillExchange: final 908 install-pointer cards and full snapshot disposition (2026-11-02)

**Source:** `agentskillexchange/skills` at `a6017b4af9d0298b7be3af7a6ec7485943d2c3e7` (discovery-only; root MIT; linked upstream rights separate).
**Scope:** source-vetting candidate decisions only. No admission, governed review, security scan, behavioral validation or installation.

## Coverage

This tranche covers the last 908 `catalog-card-install-pointer` paths, across nine categories:

| Category | Cards |
|---|---:|
| Integrations & Connectors | 148 |
| Research & Scraping | 116 |
| Calendar, Email & Productivity | 114 |
| Browser Automation | 108 |
| Library & API Reference | 108 |
| Image & Creative Automation | 95 |
| Media & Transcription | 79 |
| WordPress & CMS | 70 |
| Content Writing & SEO | 70 |
| **Total** | **908** |

Exact package records are in the [ledger](../../registry/discovery/agentskillexchange-final-pointer-908-static-20261102.json). Results: 900 REJECT unchanged and 8 REFERENCE-ONLY.

## Full AgentSkillExchange snapshot disposition

| Cluster | Paths | REFERENCE-ONLY | REJECT unchanged | DEFER | Evidence |
|---|---:|---:|---:|---:|---|
| Description-only catalog stubs | 462 | 4 | 458 | 0 | [ledger](../../registry/discovery/agentskillexchange-catalog-stub-462-static-20261102.json) |
| Authored procedures (83 direct + 3 nested) | 86 | 51 | 32 | 3 | [ledger](../../registry/discovery/agentskillexchange-authored-procedures-86-static-20261102.json) |
| Ops install pointers | 453 | 2 | 451 | 0 | [ledger](../../registry/discovery/agentskillexchange-ops-pointer-453-static-20261102.json) |
| Security & code-quality pointers | 408 | 1 | 407 | 0 | [ledger](../../registry/discovery/agentskillexchange-security-quality-pointer-408-static-20261102.json) |
| Developer Tools pointers | 439 | 1 | 438 | 0 | [ledger](../../registry/discovery/agentskillexchange-developer-tools-pointer-439-static-20261102.json) |
| Templates & data pointers | 443 | 4 | 439 | 0 | [ledger](../../registry/discovery/agentskillexchange-templates-data-pointer-443-static-20261102.json) |
| Final nine-category pointers | 908 | 8 | 900 | 0 | [ledger](../../registry/discovery/agentskillexchange-final-pointer-908-static-20261102.json) |
| Contributor `template/SKILL.md` | 1 | — | — | — | excluded as a non-skill ([segmentation](../../registry/discovery/agentskillexchange-identity-segmentation-20261102.json)) |
| **Total** | **3,200** | **71** | **3,125** | **3** | |

All 3,200 pinned paths have an individual exact-pinned decision or exclusion. Four-source current-standard exact-path decisions went from **209 to 3,405 of 4,813** during this program. The remaining **1,408** belong to Awesome Copilot, j4flmao and OpenAI Plugins. Governed review records stay at **1,039**, and the eligible denominator remains **unknown**.

The [capability index](../../registry/discovery/agentskillexchange-capability-index-20261102.json) lists every decision by domain and subdomain, including negative evidence.

## Macro findings for this tranche

### Capability not supported by content
315 cards claim capabilities their content does not support:
- synthetic wrappers over SDKs and documentation sites: graphql-js, Puppeteer, Selenium Grid contributor build steps, Cloudinary, Figma and DALL-E doc pages, Swagger UI, npm, PyPI and MDN navigation text, and the ControlNet and SDXL research repositories;
- "MCP server" cards that install an SDK or unrelated servers.

### Ungated consequential actions
135 cards advertise consequential actions with no gate:
- publishing to WordPress, gh-pages, archive.org and X;
- messaging and telephony;
- ticket and page writes, and mailbox clean-up;
- payments, including an x402 USDC auto-pay tool with no spend cap;
- infrastructure provisioning.

### Private-data egress
40 cards send private content to third parties: call audio, bank transactions, documents and locations.

### Misattribution
94 cards name vendors as authors of synthetic cards that only link to the vendor's documentation.

### REFERENCE-ONLY
These cards have authored content with real boundaries. None is approved for unchanged use.

| Card | Score | Why it qualifies |
|---|---:|---|
| `maqami-travel-booking` | 14 | Per-action confirmation before prebook, amend or cancel; payment only on the vendor checkout; no card data in chat |
| `aperture-wallet-guide` | 14 | Explicit no-secrets and no-transaction boundary |
| `retrieve-permission-scoped-workplace-evidence-through-onyx-mcp` | 13 | Permission-scoped workplace retrieval |
| `pangolinfo-ai-serp` | 12 | Authored usage guidance (modes, output fields) |
| `debug-firefox-only-browser-issues-with-devtools-mcp-before-shipping-web-changes` | 11 | Dedicated browser profile; privileged tools opt-in |
| `plan-generate-and-review-gemini-images-with-banana-claude` | 11 | Authored image planning and review workflow |
| `hermes-tweet` | 11 | Write actions behind an explicit enablement gate with operator confirmation |
| `connect-agents-to-openrag-knowledge-bases-over-mcp` | 10 | Authored MCP connection guidance |

## Systemic conclusion for this source

- **Thin catalog:** the source is mostly a machine-generated catalog. 3,113 of 3,196 direct paths are description-only stubs or auto-extracted install pointers, and about 33% of cards wrap a shared upstream.
- **Labels and attribution:** publisher `security_reviewed` labels are unsupported by any evidence in the packages, and vendor misattribution is pervasive.
- **Where the value is:** the reusable material sits in the 71 REFERENCE-ONLY packages, mostly authored procedures. Every other card is useful only as an upstream discovery lead.
- **Consumer guidance:** search the capability index, then read the REFERENCE-ONLY records and the upstream project as separate, unreviewed identities.

## Next

Return to the remaining Awesome Copilot (313), j4flmao (555) and OpenAI Plugins (495 without any exact-path evidence) frontiers, which concurrent agents are working on. Choose disjoint clusters.
