#!/usr/bin/env node
/**
 * Render only the agent-facing portion of an initial alpha journey fixture.
 * Expected decisions and scoring criteria are deliberately withheld.
 *
 * Usage:
 *   node scripts/render-alpha-scenario.ts A1
 *   node scripts/render-alpha-scenario.ts R2 --json
 */

import { parseArgs } from "node:util";
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const FIXTURE = join(ROOT, "docs", "evals", "fixtures", "initial-alpha-scenarios.json");

const { positionals, values } = parseArgs({
  allowPositionals: true,
  options: {
    json: { type: "boolean", default: false },
    help: { type: "boolean", default: false },
  },
});

if (values.help || !positionals[0]) {
  console.log("render-alpha-scenario — print leak-safe journey input\n\nUsage: node scripts/render-alpha-scenario.ts <A1|A2|A3|R1|R2> [--json]");
  process.exit(values.help ? 0 : 2);
}

const requestedId = positionals[0].toUpperCase();
const fixture = JSON.parse(readFileSync(FIXTURE, "utf8"));
const scenario = fixture.scenarios.find((s: any) => s.id === requestedId);

if (!scenario) {
  console.error(`Unknown scenario: ${requestedId}`);
  process.exit(2);
}

const safeInput: Record<string, unknown> = {
  scenario_id: scenario.id,
  mode: scenario.mode,
};

for (const key of ["user_evidence", "existing_set", "current_user_evidence"]) {
  if (scenario[key] !== undefined) safeInput[key] = scenario[key];
}

const prompt = "Use this repository as intended. Build or refine the smallest dependable skill set for the supplied synthetic user context. Complete the workflow as far as this host permits, including selection/creation decisions, evaluation state, and installation or portable-handoff state. Do not assume unavailable evidence.";

if (values.json) {
  console.log(JSON.stringify({ prompt, ...safeInput }, null, 2));
  process.exit(0);
}

console.log(`# Initial Alpha Scenario ${scenario.id}`);
console.log(`\nMode: ${scenario.mode}`);
console.log(`\n${prompt}`);
console.log("\n## Synthetic user context\n");
console.log(JSON.stringify(safeInput, null, 2));
