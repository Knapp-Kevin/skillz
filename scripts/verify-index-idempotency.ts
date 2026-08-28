#!/usr/bin/env node
/**
 * Prove generated catalog determinism in a fully materialized checkout.
 *
 * The first generation is allowed to update stale checked-in output.
 * The second generation must produce byte-identical INDEX.md and index.json.
 *
 * Usage:
 *   node scripts/verify-index-idempotency.ts
 */

import { readFileSync, existsSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

if (process.argv.includes("--help") || process.argv.includes("-h")) {
  console.log("verify-index-idempotency — regenerate the catalog twice and require byte-identical second-pass output\n\nUsage: node scripts/verify-index-idempotency.ts");
  process.exit(0);
}

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const BUILD = join(ROOT, "scripts", "build-index.ts");
const INDEX_JSON = join(ROOT, "index.json");
const INDEX_MD = join(ROOT, "INDEX.md");

function runGenerator(label: string): void {
  const result = spawnSync(process.execPath, [BUILD], {
    cwd: ROOT,
    encoding: "utf8",
    timeout: 120_000,
  });
  if (result.status !== 0) {
    console.error(`${label}: generator failed with exit ${result.status}`);
    if (result.stdout) console.error(result.stdout.trim());
    if (result.stderr) console.error(result.stderr.trim());
    process.exit(1);
  }
  if (result.stdout.trim()) console.log(`${label}: ${result.stdout.trim()}`);
}

function requireGeneratedFiles(): void {
  for (const path of [INDEX_JSON, INDEX_MD]) {
    if (!existsSync(path)) {
      console.error(`FAIL: expected generated file missing: ${path}`);
      process.exit(1);
    }
  }
}

runGenerator("first-pass");
requireGeneratedFiles();

const firstJson = readFileSync(INDEX_JSON);
const firstMd = readFileSync(INDEX_MD);
const parsed = JSON.parse(firstJson.toString("utf8"));

if (parsed.version !== 2) {
  console.error(`FAIL: expected index schema version 2, found ${parsed.version ?? "missing"}`);
  process.exit(1);
}

for (const key of [
  "localSkills",
  "vendorSkills",
  "totalIndexedSkillEntries",
  "uniqueSkillNames",
  "vendoredSources",
  "registeredSources",
]) {
  if (!Number.isInteger(parsed.counts?.[key]) || parsed.counts[key] < 0) {
    console.error(`FAIL: index.counts.${key} is missing or invalid`);
    process.exit(1);
  }
}

runGenerator("second-pass");

const secondJson = readFileSync(INDEX_JSON);
const secondMd = readFileSync(INDEX_MD);

const jsonStable = firstJson.equals(secondJson);
const mdStable = firstMd.equals(secondMd);

if (!jsonStable || !mdStable) {
  console.error(`FAIL: generated catalog is not idempotent (index.json=${jsonStable}, INDEX.md=${mdStable})`);
  process.exit(1);
}

console.log("PASS: generated catalog is byte-identical on the second pass.");
console.log(JSON.stringify({
  version: parsed.version,
  generated: parsed.generated,
  counts: parsed.counts,
  idempotent: true,
}, null, 2));
