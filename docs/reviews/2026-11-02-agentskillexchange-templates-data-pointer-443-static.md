# AgentSkillExchange: Templates & Workflows and Data Extraction install-pointer cluster, 443 packages (2026-11-02)

**Source:** `agentskillexchange/skills` at `a6017b4af9d0298b7be3af7a6ec7485943d2c3e7` (discovery-only; root MIT; linked upstream rights separate).
**Scope:** source-vetting candidate decisions only. No admission, governed review, security scan, behavioral validation or installation.

## Coverage

This tranche covers every `catalog-card-install-pointer` path in two categories:

| Category | Cards |
|---|---:|
| Templates & Workflows | 234 |
| Data Extraction & Transformation | 209 |
| **Total** | **443** |

Exact package records are in the [ledger](../../registry/discovery/agentskillexchange-templates-data-pointer-443-static-20261102.json).

| Measure | Before | After |
|---|---:|---:|
| AgentSkillExchange terminal exact-path decisions | 1,845 | **2,288** (+3 DEFER unchanged) |
| Four-source current-standard exact-path decisions | 2,054 | **2,497 / 4,813** |
| Install-pointer cards still pending | 1,351 | **908** (currently in review) |

Results: 439 REJECT unchanged and 4 REFERENCE-ONLY.

## Method

- **Review:** 8 parallel read-only reviewers worked disjoint lists under the shared install-pointer brief. The whole tranche was re-run after a container restart.
- **Integration checks:** one integration owner validated identity, taxonomy, rubric agreement and hard-fail/disposition consistency.
- **Adjustments:** one taxonomy entry was corrected. One upstream example API key was redacted from the record; the `literal-credential` flag is retained.

## Macro findings

### Capability not supported by content
107 cards claim capabilities their content does not support:
- synthetic wrappers over Apache monorepos: dbt, Tika, Kafka, Airflow, Spark, Avro and Camel;
- pandas, parquet, jq, graphql-js and kafkajs wrappers;
- six `terraform-module-*` cards over `hashicorp/terraform`;
- ten cookiecutter variants;
- cards whose install lines belong to a different tool. Examples: qsv cards that install `zipsign`, a Postgres MCP card with a `golangci-lint` line, and an XSLT 3.0 card over `lxml`.

### Misattribution
39 cards name the wrong author, chiefly the Apache Software Foundation, dbt Labs or Salesforce credited for synthetic or community wrappers.

### Ungated consequential operations
37 cards advertise consequential operations with no gate:
- Salesforce bulk loads and schema-registry registration;
- Terraform apply, DigitalOcean droplet management and Cloudflare Workers deploys;
- Stripe subscription portals;
- n8n automations, Backstage changes and data publishing.

### Private-data egress
13 cards send private documents, résumés or workspace data to hosted extraction or LLM services.

### Credentials, remote code and remote instructions
- The Typesense card prints an upstream example API key in a `docker` command. It is flagged `literal-credential`, and the key is redacted in this repository's record.
- 5 cards install remote code.
- 2 cards tell the agent to fetch and follow remote instructions.

### REFERENCE-ONLY
- `co-edit-and-verify-a-live-spreadsheet-session-through-gridcraft-mcp` (12/20) and `convert-iwork-documents-to-office-files-with-fidelity-checks-through-officeimo` (12/20): pinned versions or commits and scoped access.
- `run-github-issues-as-a-spec-build-review-ship-pipeline-with-workkit` (12/20): status-label gates, a blind verifier and no commits before tests pass.
- `make-rails-active-job-workloads-resumable-with-job-iteration` (10/20): a short, accurate integration recipe for the job-iteration gem.

## Next

Integrate the final 908 install-pointer cards (nine remaining categories), which are under review now.
