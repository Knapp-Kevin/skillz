# Governed Discovery Surfaces

`skillz` uses intentional discovery surfaces to find candidate skills, creators, standards, methods, and source corpora. Discovery surfaces are **lead-generation and research inputs only**. They do not grant trust, quality, provenance, redistribution rights, installation authority, or corpus admission.

The external host agent performs discovery. `skillz` remains passive and owns no crawler, scanner, monitor, scheduler, polling process, ingestion service, or autonomous discovery machinery.

## Standard discovery rule

When looking for potential new material, prefer high-signal existing discovery surfaces before broad undirected searching. A discovery result becomes repository work only when it is worth opening an issue under the issue-first candidate workflow in `docs/candidate-intake.md`.

For every lead promoted into an evaluation issue, resolve the candidate independently to its canonical source. Do not treat a discovery-surface row, summary, score, creator attribution, popularity signal, or recommendation as provenance or quality evidence.

The evaluation issue must still establish, as applicable:

- canonical source and publisher/author identity;
- exact source revision or exact content identity;
- package boundary and fingerprint when establishable;
- license, attribution, redistribution, and applicable terms;
- freshness and skill-specific update evidence;
- dependencies and supporting references/assets/tooling;
- authority, credentials, privacy, cost, and side-effect assumptions;
- portability and host/tool assumptions;
- overlap/differentiation against the governed corpus;
- controlled tags;
- decisive exact-version static review state;
- behavioral-evidence state, normally `not-run` during static intake.

## Creator Technical Resource Catalog

The connected Google Drive spreadsheet **Creator Technical Resource Catalog** is an intentional internal discovery surface for `skillz` curation.

It currently provides structured resource intelligence across surfaces including Catalog, Resource Explorer, Creator Intelligence, Capability Portfolio, Trust & Control, Assessment Queue, Decision Ledger, Compare Tools, Solution Builder, and related governed workbook views.

Use it to:

- identify promising repositories, creators, standards, techniques, and capability clusters;
- find potential gaps in the current `skillz` corpus;
- discover upstream recommendations or adjacent resources worth resolving to canonical sources;
- compare likely duplication before opening a candidate issue;
- prioritize candidates where the catalog already exposes meaningful capability, trust, burden, or provenance questions.

Do **not** use it to:

- admit a skill directly;
- copy a catalog score into `skillz` as a verification result;
- infer licensing, exact revisions, package identity, freshness, or author identity without checking the canonical source;
- treat catalog verification status as individual `skillz` verification;
- persist restricted or unclear-license material merely because it appears in the catalog.

The workbook is intentionally not registered in `registry/sources.yaml` as an admitted third-party skill source. It is internal discovery intelligence, not a canonical upstream source for the candidate material it references.

## Other discovery surfaces

Current useful discovery inputs include, where relevant:

- GitHub Awesome Copilot as a registered dynamic-discovery source;
- Agent Skills Specification as a normative portability/format reference;
- Hugging Face Skills and other source-vetted candidate corpora recorded in the living curation ledger;
- creator/source candidates already tracked through GitHub issues and curation records;
- targeted web/GitHub research when existing discovery surfaces do not cover a demonstrated gap.

Broad web or GitHub discovery is appropriate when it answers a sharp question. It should not become count-driven harvesting.

## Promotion into evaluation

A discovery lead should become a candidate issue when there is enough evidence to state:

1. what capability or method appears differentiated or useful;
2. where the likely canonical source is;
3. why the existing governed corpus may not already cover it sufficiently;
4. what source/terms/authority questions need evaluation.

Once an issue exists, `docs/candidate-intake.md` controls the evaluation and admission lifecycle.
