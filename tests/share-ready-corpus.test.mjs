import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { mkdtempSync, mkdirSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import test from "node:test";

const ROOT = resolve(new URL("..", import.meta.url).pathname);
const SCRIPT = join(ROOT, "scripts", "verify-share-ready-corpus.ts");

function gitBlobSha(text) {
  const bytes = Buffer.from(text, "utf8");
  return createHash("sha1").update(Buffer.from(`blob ${bytes.length}\0`)).update(bytes).digest("hex");
}

function makeFixture({ thirdPartyStatus = "verified", withProvenance = true, withLocalRecord = true, corruptLocalFingerprint = false } = {}) {
  const root = mkdtempSync(join(tmpdir(), "skillz-share-ready-"));
  const verification = join(root, "verification", "fixture-source");
  const provenance = join(root, "provenance", "fixture-source");
  const skills = join(root, "local-skills", "local-fixture");
  const localManifest = join(root, "local-verification.json");
  mkdirSync(verification, { recursive: true });
  mkdirSync(provenance, { recursive: true });
  mkdirSync(skills, { recursive: true });

  writeFileSync(join(verification, "fixture-skill.yaml"), `schema_version: 1
skill_name: fixture-skill
source_id: fixture-source
source_snapshot_revision: 0123456789abcdef0123456789abcdef01234567
fingerprint_algorithm: git-blob-sha1
content_blob_sha: 0123456789abcdef0123456789abcdef01234567
characterized_at: 2026-08-29
last_verified_at: 2026-08-29
verification_status: ${thirdPartyStatus}
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

  const localText = `---\nname: local-fixture\ndescription: Use when testing local verification.\nmetadata:\n  version: 1.0.0\n---\n\n# Local Fixture\n`;
  const localFile = join(skills, "SKILL.md");
  writeFileSync(localFile, localText);
  const fingerprint = corruptLocalFingerprint ? "f".repeat(40) : gitBlobSha(localText);

  const localRecords = withLocalRecord ? [{
    skill_name: "local-fixture",
    local_path: localFile,
    fingerprint_algorithm: "git-blob-sha1",
    content_blob_sha: fingerprint,
    verification_status: "verified",
    validation_status: "not-run",
    rubric_score: "18/20",
    tags: {
      use_case: ["testing"],
      lifecycle: ["verification"],
      characteristic: ["evidence-first"],
      authority: ["read-only"],
      portability: ["high"],
    },
    notes: "fixture",
  }] : [];

  writeFileSync(localManifest, JSON.stringify({
    schema_version: 1,
    source_id: "local-skills",
    source_class: "first-party",
    reviewed_at: "2026-08-29",
    rubric: "docs/skill-verification.md",
    skills: localRecords,
  }, null, 2));

  return {
    root,
    verification: join(root, "verification"),
    provenance: join(root, "provenance"),
    skills: join(root, "local-skills"),
    localManifest,
  };
}

function run(fixture) {
  return spawnSync(process.execPath, [
    SCRIPT,
    "--verification-dir", fixture.verification,
    "--provenance-dir", fixture.provenance,
    "--skills-dir", fixture.skills,
    "--local-manifest", fixture.localManifest,
    "--json",
  ], { cwd: ROOT, encoding: "utf8" });
}

test("companion-complete third-party and exact-reviewed local skill pass", () => {
  const fixture = makeFixture();
  try {
    const result = run(fixture);
    assert.equal(result.status, 0, result.stderr || result.stdout);
    const parsed = JSON.parse(result.stdout);
    assert.equal(parsed.status, "PASS");
    assert.equal(parsed.third_party.governed_records, 1);
    assert.equal(parsed.third_party.quality_counts.verified, 1);
    assert.equal(parsed.local.discovered_active_skills, 1);
    assert.equal(parsed.local.reviewed_active_skills, 1);
    assert.equal(parsed.local.quality_counts.verified, 1);
  } finally {
    rmSync(fixture.root, { recursive: true, force: true });
  }
});

test("unverified third-party record blocks share-ready corpus closure", () => {
  const fixture = makeFixture({ thirdPartyStatus: "unverified" });
  try {
    const result = run(fixture);
    assert.equal(result.status, 1);
    const parsed = JSON.parse(result.stdout);
    assert.match(JSON.stringify(parsed.blockers), /non-decisive share-ready verification_status: unverified/);
  } finally {
    rmSync(fixture.root, { recursive: true, force: true });
  }
});

test("missing third-party provenance companion blocks closure", () => {
  const fixture = makeFixture({ withProvenance: false });
  try {
    const result = run(fixture);
    assert.equal(result.status, 1);
    const parsed = JSON.parse(result.stdout);
    assert.match(JSON.stringify(parsed.blockers), /matching provenance companion not found/);
  } finally {
    rmSync(fixture.root, { recursive: true, force: true });
  }
});

test("active local skill without individual review blocks closure", () => {
  const fixture = makeFixture({ withLocalRecord: false });
  try {
    const result = run(fixture);
    assert.equal(result.status, 1);
    const parsed = JSON.parse(result.stdout);
    assert.match(JSON.stringify(parsed.blockers), /active local skill lacks exact-version review/);
  } finally {
    rmSync(fixture.root, { recursive: true, force: true });
  }
});

test("changed local skill fingerprint invalidates its review", () => {
  const fixture = makeFixture({ corruptLocalFingerprint: true });
  try {
    const result = run(fixture);
    assert.equal(result.status, 1);
    const parsed = JSON.parse(result.stdout);
    assert.match(JSON.stringify(parsed.blockers), /fingerprint mismatch/);
  } finally {
    rmSync(fixture.root, { recursive: true, force: true });
  }
});
