# Million-scale agent-skill discovery: research intake (2026-11-02)

Status: **OPEN-ENDED DISCOVERY**. This note does not admit, install, execute, score, or license any skill. Discovery may index metadata at ecosystem scale independently of qualification; storing or redistributing full third-party content remains subject to applicable rights. It is intentionally isolated from Claude's ongoing four-source qualification work.

## Evidence and population definitions

1. **GitSkills**, Destefanis et al. (2026), https://arxiv.org/abs/2608.10906 : July 2026 GitHub research dataset, **3,797,117 SKILL.md occurrences** in **282,200 repositories**, grouped into **1,877,981 distinct file contents**. Occurrences are not independent packages, distinct file contents are not distinct complete packages, and neither count is an eligibility denominator. Dataset reportedly includes a self-contained SQLite database, file paths, hashes, repository metadata, package-folder information and sampled history. Verify data availability, terms, integrity and schema before any ingestion.
2. **Skill Constellations**, Seddik (2026), https://arxiv.org/abs/2610.11169 : historical copy network over GitSkills, reporting **2,193,119 adoptions**. High-degree source families and security-fix propagation deserve targeted provenance review; do not treat copied instances as new original authors or independently maintained packages.
3. **State of agent skills**, Vercel (2026), https://vercel.com/blog/state-of-agent-skills : reports skills.sh reaching **one million registry listings** in seven months, through August 2026. A listing is not the same population as a GitHub SKILL.md occurrence or a unique package. Do not add these counts together.
4. **From Registry to Repository**, Gao et al. (2026), https://arxiv.org/abs/2607.00911 : registry/personal-repository reuse analysis; potentially useful to test source-family overlap and adaptation rather than assume copies are identical.

## Intake gates before indexing

- **Source and rights**: verify publisher, downloadable dataset/license, provenance, redistribution rights, API/robots/rate restrictions, and original package licenses separately. A research paper does not license all third-party skill content.
- **Identity**: retain occurrence identity (host, repo, path, revision), instruction blob hash, full package-tree fingerprint, upstream origin and known copy relationships. No hash-only assertion of complete-package equivalence.
- **Safety**: treat all external SKILL.md text and bundled scripts as untrusted data. No automatic execution, installation, private-data exposure, or network access on behalf of candidate instructions.
- **Coverage**: map candidates to the existing 33 domains / 247 subdomains with evidence-linked, potentially multi-label assignments; separate name-only leads from inspected-content assignments. Do not fabricate per-domain totals.
- **Quality**: keep distinct columns for raw occurrences, unique instruction blobs, reconciled package identities, exact-version static decisions, governed reviews, package security, behavioral validation and authorized reuse.
- **Scale**: index discoverable metadata broadly and continuously, with resumable source cursors, rate-limit compliance, per-source counts and provenance. Use a bounded sample to test ingestion quality, **not** to cap discovery. Avoid bulk copying full third-party packages without rights and resource review.
- **Concurrency**: reconcile against the current four-source frontier and Claude's ongoing qualification records by pinned identities; never overwrite or reset its ledgers.

## Parallel execution tracks

1. **Unbounded discovery frontier**: expand metadata indexing across GitSkills and independent registries, repositories, ecosystems and future sources; retain incomplete and rejected leads, checkpoint progress, and respect source access limits. Do not require review, license clearance for *use*, or a domain placement before recording a lawful metadata lead.
2. **Bounded ingestion QA**: verify dataset schema, rights and integrity, then use a 1,000-occurrence *diagnostic sample* to measure extraction fidelity, deduplication, overlap and coverage errors. This sample is not an upper bound or a gate on further metadata discovery.
3. **Independent qualification**: continue exact-package evaluation, static grades, security and behavioral checks, license-specific reuse decisions and domain mapping as capacity permits. Never promote discovered counts into approved counts.
4. **Progress reporting**: report cumulative occurrences, deduplicated blobs, package identities, sources and capability coverage alongside separately measured evaluated/qualified populations. Label unknown denominators.

**Acceptance:** discovery can expand without waiting for evaluation, with auditable source identity and checkpointing; evaluation and adoption remain independently gated.
