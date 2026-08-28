import { test } from "node:test";
import assert from "node:assert/strict";
import { readdirSync, readFileSync, statSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const CURATION = join(ROOT, "registry", "skills");

function yamlFiles(dir) {
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

const required = [
  "schema_version", "skill_name", "display_name", "source_id", "source_repository",
  "source_path", "source_class", "license", "relationship", "source_snapshot_revision",
  "upstream_revision", "upstream_last_updated_at", "curated_at", "last_checked_at",
  "availability", "permission_tier", "portability", "review_status", "dependency_status",
  "dependencies", "import_eligibility", "rationale",
];

test("every curated third-party skill has auditable provenance and freshness metadata", () => {
  const files = yamlFiles(CURATION);
  assert.ok(files.length >= 13, `expected first curation wave to contain at least 13 records, found ${files.length}`);

  for (const file of files) {
    const text = readFileSync(file, "utf8");
    for (const key of required) assert.ok(field(text, key), `${file}: missing ${key}`);

    assert.match(field(text, "source_repository"), /^https:\/\/github\.com\//, `${file}: source_repository must be a GitHub URL`);
    assert.match(field(text, "source_path"), /SKILL\.md$/, `${file}: source_path must identify the canonical skill file`);
    assert.match(field(text, "source_snapshot_revision"), /^[0-9a-f]{40}$/, `${file}: source snapshot must be a full commit SHA`);
    assert.match(field(text, "upstream_revision"), /^[0-9a-f]{40}$/, `${file}: upstream revision must be a full commit SHA`);
    assert.ok(!Number.isNaN(Date.parse(field(text, "upstream_last_updated_at"))), `${file}: invalid upstream_last_updated_at`);
    assert.ok(!Number.isNaN(Date.parse(field(text, "curated_at"))), `${file}: invalid curated_at`);
    assert.ok(!Number.isNaN(Date.parse(field(text, "last_checked_at"))), `${file}: invalid last_checked_at`);

    const availability = field(text, "availability");
    assert.ok(["vendored", "imported", "external"].includes(availability), `${file}: invalid availability ${availability}`);
    const localPath = field(text, "local_path");
    if (availability === "external") assert.equal(localPath, undefined, `${file}: external skill must not claim a local_path`);
    else {
      assert.ok(localPath, `${file}: ${availability} skill must identify local_path`);
      assert.ok(statSync(join(ROOT, localPath)).isFile(), `${file}: local_path does not resolve to a file: ${localPath}`);
    }
  }
});

test("shared-reference skills are never represented as broken standalone imports", () => {
  const guarded = ["code-review-and-quality", "incremental-implementation", "observability-and-instrumentation", "test-driven-development"];
  for (const name of guarded) {
    const file = join(CURATION, "addyosmani-agent-skills", `${name}.yaml`);
    const text = readFileSync(file, "utf8");
    assert.equal(field(text, "availability"), "vendored");
    assert.equal(field(text, "dependency_status"), "source-intact");
    assert.equal(field(text, "import_eligibility"), "already-vendored");
  }
});

test("Addy Osmani source is pinned as a real submodule, not merely described as local", () => {
  const modules = readFileSync(join(ROOT, ".gitmodules"), "utf8");
  const sources = readFileSync(join(ROOT, "registry", "sources.yaml"), "utf8");
  assert.match(modules, /vendor\/addyosmani-agent-skills/);
  assert.match(modules, /https:\/\/github\.com\/addyosmani\/agent-skills\.git/);
  assert.match(sources, /id: addyosmani-agent-skills[\s\S]*inclusion: vendored/);
  assert.match(sources, /pinned_revision: f63ec56a3cc936408d792956ae583c3c96a825bd/);
});
