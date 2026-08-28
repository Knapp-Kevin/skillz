import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const FIXTURE_PATH = join(ROOT, "docs", "evals", "fixtures", "initial-alpha-scenarios.json");
const FIXTURES = JSON.parse(readFileSync(FIXTURE_PATH, "utf8"));
const byId = new Map(FIXTURES.scenarios.map((s) => [s.id, s]));
const FORBIDDEN_EVALUATOR_KEYS = new Set([
  "candidate_hint",
  "expected_decision",
  "must_observe",
  "must_not",
  "scoring",
  "answer_key",
]);

function collectForbiddenKeys(value, path = "$", found = []) {
  if (Array.isArray(value)) {
    value.forEach((item, index) => collectForbiddenKeys(item, `${path}[${index}]`, found));
    return found;
  }
  if (!value || typeof value !== "object") return found;
  for (const [key, child] of Object.entries(value)) {
    if (FORBIDDEN_EVALUATOR_KEYS.has(key)) found.push(`${path}.${key}`);
    collectForbiddenKeys(child, `${path}.${key}`, found);
  }
  return found;
}

test("public initial alpha fixture is v2 with neutral rotated scenario identifiers", () => {
  assert.equal(FIXTURES.schema_version, 2);
  assert.equal(FIXTURES.set_id, "initial-alpha-v2-2026-08-28");
  assert.deepEqual([...byId.keys()].sort(), ["D8N", "K7M", "L9C", "Q2F", "W4H"]);
});

test("public fixture contains treatment context only and no evaluator answer keys", () => {
  assert.deepEqual(collectForbiddenKeys(FIXTURES), []);
  for (const scenario of FIXTURES.scenarios) {
    assert.ok(scenario.name, `${scenario.id}: name missing`);
    assert.ok(["first-visit", "returning-user"].includes(scenario.mode), `${scenario.id}: invalid mode`);
    assert.ok(scenario.user_evidence || scenario.current_user_evidence, `${scenario.id}: synthetic user context missing`);
  }
});

test("public fixture still covers three first visits and two returning reviews without encoding outcomes", () => {
  const first = FIXTURES.scenarios.filter((scenario) => scenario.mode === "first-visit");
  const returning = FIXTURES.scenarios.filter((scenario) => scenario.mode === "returning-user");
  assert.equal(first.length, 3);
  assert.equal(returning.length, 2);
  assert.ok(returning.every((scenario) => Array.isArray(scenario.existing_set) && scenario.existing_set.length > 0));
});

test("public fixtures do not contain real user secrets or account data", () => {
  const text = JSON.stringify(FIXTURES);
  assert.doesNotMatch(text, /api[_-]?key|password|secret\s*=|bearer\s+[a-z0-9._-]+/i);
  assert.doesNotMatch(text, /@[a-z0-9.-]+\.[a-z]{2,}/i);
});
