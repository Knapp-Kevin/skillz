import { test } from "node:test";
import assert from "node:assert/strict";
import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const PROVENANCE = join(ROOT, "registry", "skills");
const VERIFICATION = join(ROOT, "registry", "verification");

function yamlFiles(dir) {
  if (!existsSync(dir)) return [];
  const out = [];
  for (const entry of readdirSync(dir)) {
    const path = join(dir, entry);
    if (statSync(path).isDirectory()) out.push(...yamlFiles(path));
    else if (entry.endsWith(".yaml")) out.push(path);
  }
  return out;
}

function field(text, name) {
  return text.match(new RegExp(`^${name}:\\s*(.+)$`, "m"))?.[1]?.trim().replace(/^['\"]|['\"]$/g, "");
}

const provenanceRequired = [
  "schema_version", "skill_name", "display_name", "source_id", "source_repository",
  "source_path", "source_class", "license", "relationship", "source_snapshot_revision",
  "upstream_revision", "upstream_last_updated_at", "curated_at", "last_checked_at",
  "availability", "permission_tier", "portability", "review_status", "dependency_status",
  "dependencies", "import_eligibility", "rationale",
];

const verificationRequired = [
  "schema_version", "skill_name", "source_id", "source_snapshot_revision", "local_path",
  "fingerprint_algorithm", "content_blob_sha", "characterized_at", "last_verified_at",
  "verification_status", "verification_basis", "validation_status",
];

test("curated third-party skills keep auditable provenance separate from quality state", () => {
  const files = yamlFiles(PROVENANCE);
  assert.ok(files.length >= 16, `expected at least 16 provenance records, found ${files.length}`);
  for (const file of files) {
    const text = readFileSync(file, "utf8");
    for (const key of provenanceRequired) assert.ok(field(text, key), `${file}: missing ${key}`);
    assert.match(field(text, "source_repository"), /^https:\/\/github\.com\//);
    assert.match(field(text, "source_path"), /SKILL\.md$/);
    assert.match(field(text, "source_snapshot_revision"), /^[0-9a-f]{40}$/);
    assert.match(field(text, "upstream_revision"), /^[0-9a-f]{40}$/);
  }
});

test("source registry separates source role from individual verification default", () => {
  const sources = readFileSync(join(ROOT, "registry", "sources.yaml"), "utf8");
  assert.match(sources, /^version: 2$/m);
  assert.match(sources, /source_role:/);
  assert.match(sources, /verification_default:/);
  assert.match(sources, /id: mattpocock-skills[\s\S]*?verification_default: trusted-baseline/);

  const blocks = sources.split(/\n\s*- id: /).slice(1);
  for (const raw of blocks) {
    const block = `id: ${raw}`;
    const id = field(block, "id");
    const qualityDefault = field(block, "verification_default");
    if (id === "mattpocock-skills") assert.equal(qualityDefault, "trusted-baseline");
    else if (id === "agentskills-spec") assert.equal(qualityDefault, "not-applicable");
    else assert.equal(qualityDefault, "unverified", `${id}: only Matt may default trusted-baseline`);
  }
});

test("characterization is bound to exact Git blob fingerprints", () => {
  const files = yamlFiles(VERIFICATION);
  assert.ok(files.length >= 16, `expected at least 16 verification records, found ${files.length}`);
  for (const file of files) {
    const text = readFileSync(file, "utf8");
    for (const key of verificationRequired) assert.ok(field(text, key), `${file}: missing ${key}`);
    assert.equal(field(text, "fingerprint_algorithm"), "git-blob-sha1");
    assert.match(field(text, "content_blob_sha"), /^[0-9a-f]{40}$/);
    assert.ok(readFileSync(join(ROOT, "registry", "taxonomy.yaml"), "utf8").includes("verification_statuses:"));
  }
});

test("Addy characterized skills remain unverified until the new rubric is run", () => {
  const dir = join(VERIFICATION, "addyosmani-agent-skills");
  const files = yamlFiles(dir);
  assert.equal(files.length, 10);
  for (const file of files) {
    const text = readFileSync(file, "utf8");
    assert.equal(field(text, "verification_status"), "unverified");
    assert.equal(field(text, "validation_status"), "not-run");
  }
});

test("Matt characterized skills use trusted baseline without pretending behavioral validation", () => {
  const dir = join(VERIFICATION, "mattpocock-skills");
  const files = yamlFiles(dir);
  assert.equal(files.length, 3);
  for (const file of files) {
    const text = readFileSync(file, "utf8");
    assert.equal(field(text, "verification_status"), "trusted-baseline");
    assert.equal(field(text, "validation_status"), "not-run");
  }
});

test("first non-Matt verification sample earned structured verification only", () => {
  for (const [source, skill] of [
    ["cline-skills", "review-team"],
    ["cloudflare-skills", "agents-sdk"],
    ["google-agents-cli", "google-agents-cli-eval"],
  ]) {
    const text = readFileSync(join(VERIFICATION, source, `${skill}.yaml`), "utf8");
    assert.equal(field(text, "verification_status"), "verified");
    assert.equal(field(text, "verification_basis"), "structured-static-review");
    assert.equal(field(text, "validation_status"), "not-run");
  }
});

test("integrity checker exists and uses git hash-object without network access", () => {
  const script = readFileSync(join(ROOT, "engine", "skills", "source-vetting", "scripts", "verify-characterization-integrity.ts"), "utf8");
  assert.match(script, /hash-object/);
  assert.match(script, /STALE \/ REVERIFY REQUIRED/);
  assert.doesNotMatch(script, /fetch\(|https:\/\//);
});

test("new source corpora are real submodules and discovery/spec sources stay tracked", () => {
  const modules = readFileSync(join(ROOT, ".gitmodules"), "utf8");
  for (const path of ["vendor/openhands-extensions", "vendor/cline-skills", "vendor/cloudflare-skills", "vendor/google-agents-cli"]) {
    assert.match(modules, new RegExp(path.replaceAll("/", "\\/")));
  }
  const sources = readFileSync(join(ROOT, "registry", "sources.yaml"), "utf8");
  assert.match(sources, /id: agentskills-spec[\s\S]*?source_role: normative-spec[\s\S]*?inclusion: tracked/);
  assert.match(sources, /id: github-awesome-copilot[\s\S]*?source_role: dynamic-discovery[\s\S]*?inclusion: tracked/);
});

test("GitHub Actions remains manual-only while budget is protected", () => {
  const ci = readFileSync(join(ROOT, ".github", "workflows", "ci.yml"), "utf8");
  assert.match(ci, /workflow_dispatch:/);
  assert.doesNotMatch(ci, /^\s*(push|pull_request):/m);
});
