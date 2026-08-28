#!/usr/bin/env node
/**
 * Run the deterministic preflight required before initial alpha journey tests.
 *
 * This command does not execute behavioral journey scenarios. It proves the
 * repository/catalog/tooling state is coherent enough to run them.
 *
 * Usage:
 *   node scripts/initial-alpha-preflight.ts
 */

import { readdirSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");

interface Step {
  name: string;
  args: string[];
}

const testFiles = readdirSync(join(ROOT, "tests"))
  .filter((name) => name.endsWith(".test.mjs"))
  .sort()
  .map((name) => join(ROOT, "tests", name));

const steps: Step[] = [
  {
    name: "catalog determinism",
    args: [join(ROOT, "scripts", "verify-index-idempotency.ts")],
  },
  {
    name: "library structural audit",
    args: [join(ROOT, "engine", "skills", "skill-audit", "scripts", "audit.ts")],
  },
  {
    name: "library risk audit",
    args: [join(ROOT, "engine", "skills", "skill-audit", "scripts", "risk-audit.ts")],
  },
  {
    name: "repository contract tests",
    args: ["--test", ...testFiles],
  },
  {
    name: "characterization fingerprint integrity",
    args: [join(ROOT, "engine", "skills", "source-vetting", "scripts", "verify-characterization-integrity.ts")],
  },
];

const results: Array<{ name: string; status: "PASS" | "FAIL"; exit: number | null }> = [];

for (const step of steps) {
  console.log(`\n=== ${step.name} ===`);
  const result = spawnSync(process.execPath, step.args, {
    cwd: ROOT,
    encoding: "utf8",
    timeout: 180_000,
  });

  if (result.stdout?.trim()) console.log(result.stdout.trim());
  if (result.stderr?.trim()) console.error(result.stderr.trim());

  const passed = result.status === 0;
  results.push({ name: step.name, status: passed ? "PASS" : "FAIL", exit: result.status });

  if (!passed) {
    console.error(`\nALPHA PREFLIGHT BLOCKED at: ${step.name}`);
    console.error(JSON.stringify({ results }, null, 2));
    process.exit(1);
  }
}

console.log("\n=== initial alpha preflight ===");
console.log(JSON.stringify({ status: "PASS", results }, null, 2));
console.log("READY FOR JOURNEY EVALUATION. This is not behavioral proof by itself.");
