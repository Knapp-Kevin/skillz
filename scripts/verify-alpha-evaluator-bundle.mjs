#!/usr/bin/env node
/**
 * Verify that a private evaluator-only rubric is bound to the exact current
 * public share-ready treatment fixture committed in this repository.
 *
 * The private rubric must remain outside the public repository and outside the
 * treatment-agent context. Publicly mapping scenario IDs to expected decisions
 * invalidates the treatment set and requires another rotation.
 *
 * Usage:
 *   node scripts/verify-alpha-evaluator-bundle.mjs --rubric /private/path/rubric.json
 */

import { createHash } from "node:crypto";
import { existsSync, readFileSync, realpathSync } from "node:fs";
import { dirname, isAbsolute, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { parseArgs } from "node:util";

const ROOT = resolve(join(dirname(fileURLToPath(import.meta.url)), ".."));
const PUBLIC_FIXTURE = join(ROOT, "docs", "evals", "fixtures", "share-ready-scenarios-v3.json");

const { values } = parseArgs({
  options: {
    rubric: { type: "string" },
    help: { type: "boolean", default: false },
  },
});

if (values.help || !values.rubric) {
  console.log("verify-alpha-evaluator-bundle — bind a private evaluator rubric to the exact current public share-ready scenario set\n\nUsage: node scripts/verify-alpha-evaluator-bundle.mjs --rubric <private-rubric.json>");
  process.exit(values.help ? 0 : 2);
}

function isInside(parent, candidate) {
  const rel = relative(parent, candidate);
  return rel === "" || (!rel.startsWith("..") && !isAbsolute(rel));
}

const rubricPath = resolve(values.rubric);
if (!existsSync(rubricPath)) {
  console.error(`FAIL: private evaluator rubric not found: ${rubricPath}`);
  process.exit(1);
}

const rootReal = realpathSync(ROOT);
const rubricReal = realpathSync(rubricPath);
if (isInside(ROOT, rubricPath) || isInside(rootReal, rubricReal)) {
  console.error("FAIL: private evaluator rubric is inside the repository/treatment workspace; keep it on a separate evaluator-only path");
  process.exit(1);
}

const publicBytes = readFileSync(PUBLIC_FIXTURE);
const publicSha256 = createHash("sha256").update(publicBytes).digest("hex");
const publicFixture = JSON.parse(publicBytes.toString("utf8"));
const rubric = JSON.parse(readFileSync(rubricPath, "utf8"));
const errors = [];

if (rubric.schema_version !== 2) errors.push(`private rubric schema_version must be 2, found ${rubric.schema_version ?? "missing"}`);
if (rubric.set_id !== publicFixture.set_id) errors.push(`set_id mismatch: public=${publicFixture.set_id} private=${rubric.set_id ?? "missing"}`);
if (rubric.public_fixture_sha256 !== publicSha256) errors.push(`public fixture SHA-256 mismatch: expected ${publicSha256}, private bundle records ${rubric.public_fixture_sha256 ?? "missing"}`);

const publicIds = new Set((publicFixture.scenarios ?? []).map((scenario) => scenario.id));
const rubricScenarios = Array.isArray(rubric.scenarios) ? rubric.scenarios : [];
const privateIds = new Set();

for (const scenario of rubricScenarios) {
  if (!scenario?.id) {
    errors.push("private rubric contains a scenario without id");
    continue;
  }
  if (privateIds.has(scenario.id)) errors.push(`private rubric duplicates scenario id ${scenario.id}`);
  privateIds.add(scenario.id);
  if (!publicIds.has(scenario.id)) errors.push(`private rubric contains unknown scenario id ${scenario.id}`);
  if (!scenario.expected_decision) errors.push(`${scenario.id}: expected_decision missing`);
  if (!Array.isArray(scenario.must_observe) || scenario.must_observe.length < 3) errors.push(`${scenario.id}: must_observe must contain at least 3 criteria`);
  if (!Array.isArray(scenario.must_not) || scenario.must_not.length < 3) errors.push(`${scenario.id}: must_not must contain at least 3 criteria`);
}

for (const id of publicIds) {
  if (!privateIds.has(id)) errors.push(`private rubric is missing public scenario id ${id}`);
}
if (privateIds.size !== publicIds.size) errors.push(`scenario count mismatch: public=${publicIds.size} private=${privateIds.size}`);

if (errors.length > 0) {
  console.error("FAIL: private evaluator bundle does not match the frozen public share-ready scenario set:");
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`PASS: private evaluator bundle matches ${publicFixture.set_id}.`);
console.log(JSON.stringify({
  set_id: publicFixture.set_id,
  public_fixture_sha256: publicSha256,
  scenario_ids: [...publicIds].sort(),
  evaluator_bundle: "PRIVATE / VERIFIED",
  rubric_location: "OUTSIDE REPOSITORY",
}, null, 2));
