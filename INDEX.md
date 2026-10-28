# Skill Catalog Snapshot

**Snapshot date:** 2026-10-28

This is a passive, hand-maintained catalog snapshot of the governed `skillz` corpus. It is navigation and accounting evidence only. The external host agent performs discovery, comparison, evaluation, security assessment, and reconciliation. The repository owns no runtime, scripts, tests, CI workflows, or background services.

Canonical inputs are `registry/categories.yaml`, `registry/sources.yaml`, `registry/local-verification.json`, `registry/skills/`, and `registry/verification/`.

## Current totals

| Surface | Count |
|---|---:|
| First-party user-facing skills | 44 |
| First-party provenance-complete | 44 / 44 |
| Pinned external corpora | 12 |
| Unique registered source identities | 22 |
| Persisted third-party exact-version reviews | 795 |
| Jwynia Agent Skills selectively reviewed units | 54 |
| Dan Dewhurst Story Skills current-standard companions | 23 / 23 |
| Dan Dewhurst Story Skills current-standard gaps | 0 |
| Anthropic Skills current-standard companions | 19 / 19 |
| Anthropic Knowledge Work Plugins current-standard companions | 74 / 74 |
| Anthropic Knowledge Work Plugins current-standard gaps | 0 |
| AWS current-standard companion-complete | 72 / 72 |
| Microsoft Skills current-standard companions | 186 / 186 |
| Microsoft Azure Skills current-standard companions | 34 / 34 |
| Cole Medin Skills current-standard companions | 33 / 33 |
| David Ondrej Skills current-standard companions | 55 / 55 |
| David Ondrej Skills current-standard gaps | 0 |
| Corey Haines Marketing Skills current-standard companions | 50 / 50 |
| Corey Haines Marketing Skills current-standard gaps | 0 |
| Matt Pocock Skills current-standard companions | 29 / 29 |
| Cloudflare Skills current-standard companions | 13 / 13 |
| Addy Osmani Agent Skills current-standard companions | 24 / 24 |
| Vercel Agent Skills current-standard companions | 9 / 9 |
| OpenHands Extensions current-standard companions | 1 / 1 |
| OpenHands Extensions current-standard gaps | 0 |
| Google Agents CLI current-standard companions | 7 / 7 |
| Google Agents CLI current-standard gaps | 0 |
| Cline Skills published current-standard companions | 36 / 36 |
| Cline Skills published current-standard gaps | 0 |
| Microsoft .NET direct-package companions | 29 / 29 |
| Microsoft Java direct-package companions | 26 / 26 |
| Microsoft Python direct-package companions | 40 / 40 |
| Microsoft Rust direct-package companions | 9 / 9 |
| Microsoft TypeScript direct-package companions | 25 / 25 |

Every explicitly current-standard-complete family above has **0** current-standard gaps at its registered exact pin. Selectively tracked corpora are bounded to the individually governed units and are not silently treated as whole-family complete.

`jwynia/agent-skills` is tracked at `e02ec7e226a6e4f8419fd3b88a1d8e472d421b32` for selective curation. Its exact fiction denominator is now **54/54 governed**: **39 VERIFIED** exact-version static references and **15 REJECTED unchanged** references retained as prior art. The final application/orchestrator tranche VERIFIED `book-marketing`, `dna-extraction`, `flash-fiction`, `interactive-fiction`, `media-adaptation`, `paradox-fables`, and `table-tone`; it rejected `adaptation-synthesis`, `game-facilitator`, `list-builder`, `multi-order-evolution`, `sensitivity-check`, `shared-world`, `sleep-story`, and `chapter-drafter` unchanged. The most important Celestara outcome is not the pass count: `shared-world`, `game-facilitator`, and `chapter-drafter` remain high-value adaptation inputs despite unchanged authority/oracle failures, while `systemic-worldbuilding`, `interactive-fiction`, `table-tone`, and `world-fates` provide strong governed references for persistent campaign behavior. Behavioral validation remains `not-run` for all 54.

Dan Dewhurst Story Skills is **23/23 current-standard complete** at `b113a8298ae5deb37929a5b1d0cc1536d98a508c`. All 23 first-class packages are individually **VERIFIED exact-version static references** with scores from 16/20 to 18/20 and behavioral validation `not-run`. The primary operational caveat is medium portability because the family assumes the upstream Story Skills Markdown/YAML project model and optional `story` CLI; source-owned runtime remains upstream-only.

Corey Haines Marketing Skills remains **50/50 current-standard complete**. The final macro tranche adds `sales-enablement`, `schema`, `seo-audit`, and `site-architecture` as **VERIFIED exact-version static reviews** and rejects `revops`, `signup`, `sms`, `social`, and `video` unchanged while preserving adaptation/extraction/reference value. Behavioral validation remains `not-run`.

**Candidate freshness note (2026-10-28):** The [canonical denominator review](docs/reviews/2026-10-27-microsoft-canonical-denominator-and-ungoverned-exposures.md) establishes **208 structurally eligible** packages at candidate `61fe0305ea70389ed8705eec6026a786f57865cf` (212 physical manifests minus 3 non-first-class references and 1 exact mirror): **106 exact-tree carry-forwards + 76 changed-existing + 26 new/previously ungoverned**. Changed-existing screening **76/76** is not full requalification. **26/26 new candidates** now have complete exact-version static companions (**4 VERIFIED semantic only, 22 REJECT unchanged**); **31 changed-existing** full current-version reviews remain (45/76 fully requalified). Four removed paths have candidate-only [retirement/no-proven-successor decisions](docs/reviews/2026-10-27-microsoft-four-removed-path-candidate-retirements.md). Registered July remains **186/186** at unchanged pin; no candidate security scan, behavioral validation, source-pin movement or admission was claimed.

**Candidate full-package static reviews (2026-10-28):** Kusto (3), AKS/Advisor/Cost (8), authority/privacy (8), AKS/prereq/Entra (3), AKS app-deploy (1), Azure App Onboard (1), Slack-to-Teams (1), and [Foundry IQ 85-skill-file + 17-plugin-file review](docs/reviews/2026-10-28-microsoft-foundry-iq-102-blob-exact-static.md) (1). **26/26** new candidates have full exact-version static companions (4 semantic VERIFIED only / 22 REJECT unchanged); **31 changed-existing** packages still require full candidate-version requalification (45/76 complete). Persisted third-party verification companions: **795** after Rust (8), Python Azure AI (8), Python data/storage/events (8), Python identity/telemetry (6), Python services/management (8), and Python final seven (7) changed-existing tranches. Foundry IQ's default-on plugin telemetry/native installer is an unchanged-use privacy/authority hard fail despite strong core approval controls. No admission, scanner execution, behavioral evidence or pin changes.

**Changed-existing Rust qualification (2026-10-28):** [Eight complete single-file Rust reviews](docs/reviews/2026-10-28-microsoft-rust-eight-changed-exact-static.md) finished **8/76** changed-existing Microsoft candidates, leaving **68**. All eight are **REJECT unchanged** (8–11/20) for authorization and sensitive-data failures; Key Vault Keys also contains a four-byte DEK example. Exact candidate provenance and static verification are recorded; security and behavioral states `not-run`. Third-party companions **758 at this Rust checkpoint**. Registered July **186/186** and source pin unchanged.

**Changed-existing Python Azure AI qualification (2026-10-28):** [Eight complete three-file exact-version reviews](docs/reviews/2026-10-28-microsoft-python-ai-multimodal-eight-exact-static.md) finished **16/76** changed-existing Microsoft candidates, leaving **60** (29 Python, 30 Azure operations, one skill-creator). All eight are **REJECT unchanged** (9–13/20) for unapproved external data transmission, persistent service effects and privacy/retention failures; document translation also exposes SAS-bearing URL patterns. Exact provenance, all 24 blob identities and individual semantic dispositions are recorded. Security and behavioral states remain `not-run`; third-party companions **766**, total verification YAML **810** (44 first-party + 766 third-party). Registered July **186/186** and source pin unchanged.
**Changed-existing Python data/storage/events qualification (2026-10-28):** [Eight complete three-file exact-version static reviews](docs/reviews/2026-10-28-microsoft-python-data-storage-events-eight-exact-static.md) advance **16/76 → 24/76** changed-existing Microsoft packages, leaving **52** (21 Python, 30 Azure operations, one skill-creator). All eight are **REJECT unchanged** (10–12/20) for unapproved production mutations, tenant/sensitive-data disclosure, destructive storage/queue effects and event publication. All 24 exact blobs and individual companions are recorded. Security and behavioral states remain `not-run`; third-party verification companions **774**, total verification YAML **818** (44 first-party + 774 third-party). Registered July **186/186** and source pin unchanged.

**Changed-existing Python identity/telemetry qualification (2026-10-28):** [Six complete three-file exact-version static reviews](docs/reviews/2026-10-28-microsoft-python-identity-telemetry-six-exact-static.md) advance **24/76 → 30/76**, leaving **46** (15 Python, 30 Azure operations, one skill-creator). All six are **REJECT unchanged** (10–12/20) for authority/privacy hard fails. All 18 source blobs and individual companions are recorded. Security and behavioral states `not-run`; third-party companions **780**, total YAML verification **824**. July pin **186/186** unchanged.

**Changed-existing Python services/management qualification (2026-10-28):** [Eight complete exact-version static reviews](docs/reviews/2026-10-28-microsoft-python-services-management-eight-exact-static.md) advance **30/76 → 38/76**, leaving **38** (7 Python, 30 Azure operations, one skill-creator). Deep nine-file Cosmos service-layer review plus seven management/messaging/agent packages; **29 source blobs**, eight individual provenance/verification pairs, all **REJECT unchanged** (10–12/20) for authorization, credential/PII disclosure, destructive resource changes and billable capacity operations. Cosmos additionally has a potential untrusted SQL-fragment sink and substring-based emulator TLS bypass. Security and behavioral states remain `not-run`; third-party companions **788**, total YAML verification **832**. July pin **186/186** unchanged.

**Changed-existing Python final seven qualification (2026-10-28):** [Seven complete exact-version package reviews](docs/reviews/2026-10-28-microsoft-python-final-seven-exact-static.md) advance **38/76 → 45/76**, leaving **31** (30 Azure operations, one skill-creator); Python changed-existing **37/37** complete. **32 source blobs**, seven individual provenance/verification pairs, **six REJECT unchanged (10–11/20)** for cloud agent/ML/data/audio authority or FastAPI resource-ownership failures and **one Pydantic VERIFIED semantic only (17/20)**. All package-security and behavioral states remain `not-run`; third-party companions **795**, total verification YAML **839**. Registered July **186/186** and source pin unchanged.

## First-party skills by purpose

### Planning & Productivity
`daily-briefing`, `decision-log`, `inbox-triage`, `learning-plan`, `task-surface`, `week-in-review`

### Writing & Communication
`brief-writer`, `deck-outline`, `devlog-draft`, `handoff-writer`, `standup-writer`

### Research & Analysis
`compare`, `deep-dive`, `fact-check`, `paper-digest`

### Software & Repositories
`repo-doctor`, `repo-pulse`, `todo-harvester`

### Agent Operations & Security
`agent-home-doctor`, `agent-postmortem`, `automation-receipts`, `mcp-vetting`, `permissions-review`, `session-continuity`

### Monitoring & Intelligence
`claude-pulse`, `deepseek-pulse`, `gemini-pulse`, `github-pulse`, `glm-pulse`, `governance-pulse`, `hf-pulse`, `inference-pulse`, `kimi-pulse`, `llama-pulse`, `mcp-pulse`, `memory-pulse`, `mistral-pulse`, `openai-pulse`, `perplexity-pulse`, `qwen-pulse`, `xai-pulse`

### Business & Career
`career-radar`, `finance-review`, `smallbiz-ops`

## Registered source roles

**Pinned reference corpora:** `anthropic-skills`, `anthropic-knowledge-work-plugins`, `vercel-agent-skills`, `microsoft-skills`, `microsoft-azure-skills`, `aws-agent-toolkit`, `mattpocock-skills`, `addyosmani-agent-skills`, `openhands-extensions`, `cline-skills`, `cloudflare-skills`, `google-agents-cli`.

**Tracked corpora:** `cole-medin-skills`, `david-ondrej-skills`, `bm629-agent-skills`, `openclaw-agent-skills`, `archieindian-superpowers`, `corey-haines-marketing-skills`, `jwynia-agent-skills`, `danjdewhurst-story-skills`.

**Normative/discovery:** `agentskills-spec` is a normative specification; `github-awesome-copilot` is a dynamic discovery surface.

## Interpretation

Physical presence, registration, or a `verified` static review does not by itself establish behavioral validation or automatic unchanged-use eligibility. For unchanged third-party consideration, use exact-version companion evidence and apply:

**user fit → exact-version quality → operational fit → skill freshness → provenance/source context**
