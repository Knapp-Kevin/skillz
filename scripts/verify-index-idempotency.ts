#!/usr/bin/env node
/**
 * Prove generated catalog determinism and semantic coherence in a fully
 * materialized checkout.
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
import { validateCatalogInvariants } from "./lib/catalog-invariants.mjs";

if (process.argv.includes("--help") || process.argv.includes("-h")) {
  console.log("verify-index-idempotency — regenerate the catalog twice, require semantic schema-v2 invariants, and require byte-identical second-pass output\n\nUsage: node scripts/verify-index-idempotency.ts");
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

const invariantErrors = validateCatalogInvariants(parsed);
if (invariantErrors.length > 0) {
  console.error("FAIL: generated catalog violates schema-v2 semantic invariants:");
  for (const error of invariantErrors) console.error(`- ${error}`);
  process.exit(1);
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

console.log("PASS: generated catalog satisfies semantic invariants and is byte-identical on the second pass.");
console.log(JSON.stringify({
  version: parsed.version,
  generated: parsed.generated,
  counts: parsed.counts,
  semanticInvariants: true,
  idempotent: true,
}, null, 2));
