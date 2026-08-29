#!/usr/bin/env node
/**
 * Render only the public agent-facing portion of the current blind journey set.
 * Evaluator-only decisions and scoring criteria must remain outside the public
 * repository and outside treatment-agent context.
 *
 * Usage:
 *   node scripts/render-alpha-scenario.ts <scenario-id>
 *   node scripts/render-alpha-scenario.ts <scenario-id> --json
 */

import { parseArgs } from "node:util";
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const FIXTURE = join(ROOT, "docs", "evals", "fixtures", "share-ready-scenarios-v3.json");

const { positionals, values } = parseArgs({
  allowPositionals: true,
  options: {
    json: { type: "boolean", default: false },
    help: { type: "boolean", default: false },
  },
});

if (values.help || !positionals[0]) {
  console.log("render-alpha-scenario — print the current public blind treatment input\n\nUsage: node scripts/render-alpha-scenario.ts <scenario-id> [--json]");
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
  scenario_set: fixture.set_id,
  scenario_id: scenario.id,
  mode: scenario.mode,
};

for (const key of ["user_evidence", "existing_set", "current_user_evidence"]) {
  if (scenario[key] !== undefined) safeInput[key] = scenario[key];
}

const prompt = "Use this repository as intended. Build or refine the smallest dependable skill system for the supplied synthetic user context. Follow the repository's normal bootstrap path, use only legitimately available evidence, and complete the workflow as far as this host permits. Include truthful quality/validation and installation or portable-handoff states. Do not assume unavailable evidence or evaluator expectations.";

if (values.json) {
  console.log(JSON.stringify({ prompt, ...safeInput }, null, 2));
  process.exit(0);
}

console.log(`# Blind Journey Scenario ${scenario.id}`);
console.log(`\nScenario set: ${fixture.set_id}`);
console.log(`\nMode: ${scenario.mode}`);
console.log(`\n${prompt}`);
console.log("\n## Synthetic user context\n");
console.log(JSON.stringify(safeInput, null, 2));
