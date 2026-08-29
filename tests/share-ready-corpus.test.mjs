import assert from "node:assert/strict";
import { mkdtempSync, mkdirSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";

const ROOT = resolve(new URL("..", import.meta.url).pathname);
const SCRIPT = join(ROOT, "scripts", "verify-share-ready-corpus.ts");

function makeFixture(status = "verified", withProvenance = true) {
  const root = mkdtempSync(join(tmpdir(), "skillz-share-ready-"));
  const verification = join(root, "verification", "fixture-source");
  const provenance = join(root, "skills", "fixture-source");
  mkdirSync(verification, { recursive: true });
  mkdirSync(provenance, { recursive: true });

  writeFileSync(join(verification, "fixture-skill.yaml"), `schema_version: 1
skill_name: fixture-skill
source_id: fixture-source
source_snapshot_revision: 0123456789abcdef0123456789abcdef01234567
fingerprint_algorithm: git-blob-sha1
content_blob_sha: 0123456789abcdef0123456789abcdef01234567
characterized_at: 2026-08-29
last_verified_at: 2026-08-29
verification_status: ${status}
verification_basis: structured-static-review
validation_status: not-run
rubric_score: 18/20
tags:
  use_case: [testing]
  lifecycle: [verification]
  characteristic: [evidence-first]
  authority: [read-only]
  portability: [high]
notes: fixture
`);

  if (withProvenance) {
    writeFileSync(join(provenance, "fixture-skill.yaml"), `schema_version: 1
skill_name: fixture-skill
display_name: Fixture Skill
source_id: fixture-source
source_repository: https://example.invalid/source
source_path: skills/fixture-skill/SKILL.md
source_class: community-vetted
license: MIT
relationship: external-reference
source_snapshot_revision: 0123456789abcdef0123456789abcdef01234567
upstream_revision: 0123456789abcdef0123456789abcdef01234567
upstream_last_updated_at: 2026-08-29T00:00:00Z
curated_at: 2026-08-29
last_checked_at: 2026-08-29
availability: external
permission_tier: read-only
portability: high
review_status: curated-external
dependency_status: source-intact
dependencies: none
import_eligibility: eligible
rationale: fixture
`);
  }

  return { root, verification: join(root, "verification"), provenance: join(root, "skills") };
}

function run(fixture) {
  return spawnSync(process.execPath, [SCRIPT, "--verification-dir", fixture.verification, "--provenance-dir", fixture.provenance, "--json"], {
    cwd: ROOT,
    encoding: "utf8",
  });
}

test("verified companion-complete record passes share-ready corpus check", () => {
  const fixture = makeFixture();
  try {
    const result = run(fixture);
    assert.equal(result.status, 0, result.stderr || result.stdout);
    const parsed = JSON.parse(result.stdout);
    assert.equal(parsed.status, "PASS");
    assert.equal(parsed.governed_records, 1);
    assert.equal(parsed.quality_counts.verified, 1);
  } finally {
    rmSync(fixture.root, { recursive: true, force: true });
  }
});

test("unverified record blocks share-ready corpus closure", () => {
  const fixture = makeFixture("unverified");
  try {
    const result = run(fixture);
    assert.equal(result.status, 1);
    const parsed = JSON.parse(result.stdout);
    assert.equal(parsed.status, "FAIL");
    assert.match(JSON.stringify(parsed.blockers), /non-decisive share-ready verification_status: unverified/);
  } finally {
    rmSync(fixture.root, { recursive: true, force: true });
  }
});

test("missing provenance companion blocks share-ready corpus closure", () => {
  const fixture = makeFixture("verified", false);
  try {
    const result = run(fixture);
    assert.equal(result.status, 1);
    const parsed = JSON.parse(result.stdout);
    assert.equal(parsed.status, "FAIL");
    assert.match(JSON.stringify(parsed.blockers), /matching provenance companion not found/);
  } finally {
    rmSync(fixture.root, { recursive: true, force: true });
  }
});
