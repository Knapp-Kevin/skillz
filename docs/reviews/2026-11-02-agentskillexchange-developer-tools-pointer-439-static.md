# AgentSkillExchange: Developer Tools install-pointer cluster, 439 packages (2026-11-02)

**Source:** `agentskillexchange/skills` at `a6017b4af9d0298b7be3af7a6ec7485943d2c3e7` (discovery-only; root MIT; linked upstream rights separate).
**Scope:** source-vetting candidate decisions only. No admission, governed review, security scan, behavioral validation or installation.

## Coverage

This tranche covers every `catalog-card-install-pointer` path in Developer Tools, the largest category: 439 cards. Exact package records are in the [ledger](../../registry/discovery/agentskillexchange-developer-tools-pointer-439-static-20261102.json).

| Measure | Before | After |
|---|---:|---:|
| AgentSkillExchange terminal exact-path decisions | 1,406 | **1,845** (+3 DEFER unchanged) |
| Four-source current-standard exact-path decisions | 1,615 | **2,054 / 4,813** |
| Install-pointer cards still pending | 1,790 | **1,351** |

Results: 438 REJECT unchanged and 1 REFERENCE-ONLY. Scores range from 0 to 12 out of 20; the most common score is 9.

## Method

- **Review:** 8 parallel read-only reviewers worked disjoint lists under the shared install-pointer brief.
- **Interrupted batches:** a container restart stopped batches 4, 6 and 8 partway through. They were re-run from scratch, and only complete, validated outputs were integrated.
- **Integration checks:** one integration owner validated identity, taxonomy, rubric agreement and hard-fail/disposition consistency.

## Macro findings

### Real tools, but no procedures
Developer Tools has more pointers to real tools than the ops and security clusters. Even so, no card contains an authored task procedure. Real-tool pointers are kept as discovery leads under REJECT unchanged.

### Capability not supported by content
53 cards claim capabilities their content does not support:
- synthetic wrappers over big repos, such as `terraform`, `webpack`, `vite`, VS Code, `node-postgres` "EXPLAIN/HypoPG" analyzers, moby Compose cards, and an AWS SDK README presented as cost analysis;
- wrong install lines, such as a card that clones a benchmark repository instead of the server;
- empty-description MCP-server cards, which score 0.

### Ungated consequential operations
24 cards advertise consequential operations with no gate:
- self-hosted deploys: Coolify, LibreChat, LaunchDarkly, Dockge, Dokku and Wrangler;
- S3 bulk delete;
- issue-to-fix-PR automation;
- GPU job submission.

### Private-data egress
8 cards send code, session memory or private data to hosted LLM or embedding services. Examples: `claude-context` (to OpenAI and Zilliz), memanto, stash, caliber and the Gemini MCP card.

### Remote code
6 cards install remote code (`curl | bash`, PowerShell `irm | iex`) or tell the user to follow whatever upstream currently says.

### REFERENCE-ONLY
The only REFERENCE-ONLY is `delegate-and-resume-repository-tasks-through-pi-bolt-mcp` (11/20). It verifies downloads against SHA256SUMS, bounds the prompt with an absolute cwd and grants no blanket approval. Its upstream claims are unverified.

## Next

Integrate the Templates & Workflows and Data Extraction & Transformation cluster (443 cards), then review the remaining categories.
