#!/usr/bin/env node
/**
 * share-ready-preflight — deterministic repository/corpus gate before the
 * independent blind engine proof.
 *
 * This command does not run or fake model behavior. Passing it means the
 * repository is coherent enough to run the separate weak-model/adversarial
 * evaluation defined by issue #59.
 *
 * Usage:
 *   node scripts/share-ready-preflight.ts
 */

import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

if (process.argv.includes("--help") || process.argv.includes("-h")) {
  console.log("share-ready-preflight — run governed-corpus closure plus the deterministic alpha preflight before blind engine evaluation\n\nUsage: node scripts/share-ready-preflight.ts");
  process.exit(0);
}

const ROOT = resolve(join(dirname(fileURLToPath(import.meta.url)), ".."));
const steps = [
  {
    name: "governed corpus closure",
    args: [join(ROOT, "scripts", "verify-share-ready-corpus.ts")],
  },
  {
    name: "repository deterministic preflight",
    args: [join(ROOT, "scripts", "initial-alpha-preflight.ts")],
  },
];

const results = [];
for (const step of steps) {
  console.log(`\n=== ${step.name} ===`);
  const result = spawnSync(process.execPath, step.args, {
    cwd: ROOT,
    encoding: "utf8",
    timeout: 300_000,
  });
  if (result.stdout?.trim()) console.log(result.stdout.trim());
  if (result.stderr?.trim()) console.error(result.stderr.trim());

  const passed = result.status === 0;
  results.push({ name: step.name, status: passed ? "PASS" : "FAIL", exit: result.status });
  if (!passed) {
    console.error(`\nSHARE-READY PREFLIGHT BLOCKED at: ${step.name}`);
    console.error(JSON.stringify({ results }, null, 2));
    process.exit(1);
  }
}

console.log("\n=== share-ready deterministic preflight ===");
console.log(JSON.stringify({ status: "PASS", results }, null, 2));
console.log("READY FOR BLIND ENGINE PROOF. This is not weak-model or behavioral proof by itself.");
