import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const FIXTURES = JSON.parse(readFileSync(join(ROOT, "docs", "evals", "fixtures", "initial-alpha-scenarios.json"), "utf8"));

const byId = new Map(FIXTURES.scenarios.map((s) => [s.id, s]));

test("initial alpha fixture set contains the five required journey decisions", () => {
  assert.deepEqual([...byId.keys()].sort(), ["A1", "A2", "A3", "R1", "R2"]);
});

test("every journey fixture has frozen expected behavior before execution", () => {
  for (const scenario of FIXTURES.scenarios) {
    assert.ok(scenario.name, `${scenario.id}: name missing`);
    assert.ok(["first-visit", "returning-user"].includes(scenario.mode), `${scenario.id}: invalid mode`);
    assert.ok(scenario.expected_decision, `${scenario.id}: expected decision missing`);
    assert.ok(Array.isArray(scenario.must_observe) && scenario.must_observe.length >= 3, `${scenario.id}: insufficient must_observe criteria`);
    assert.ok(Array.isArray(scenario.must_not) && scenario.must_not.length >= 3, `${scenario.id}: insufficient must_not criteria`);
  }
});

test("first-visit fixtures cover eligible reuse refusal and creation", () => {
  assert.match(byId.get("A1").expected_decision, /ADOPT|ADAPT/);
  assert.match(byId.get("A2").expected_decision, /DO_NOT_TRUST_UNCHANGED/);
  assert.equal(byId.get("A3").expected_decision, "CREATE");
});

test("returning fixtures require minimal refinement and an explicit no-op", () => {
  assert.equal(byId.get("R1").expected_decision, "REFINE_MINIMALLY");
  assert.equal(byId.get("R2").expected_decision, "NO_CHANGE_NEEDED");
  assert.ok(byId.get("R1").must_not.some((v) => /rebuild the whole skill set/i.test(v)));
  assert.ok(byId.get("R2").must_not.some((v) => /newer/i.test(v)));
});

test("fixtures do not contain real user secrets or account data", () => {
  const text = JSON.stringify(FIXTURES);
  assert.doesNotMatch(text, /api[_-]?key|password|secret\s*=|bearer\s+[a-z0-9._-]+/i);
  assert.doesNotMatch(text, /@[a-z0-9.-]+\.[a-z]{2,}/i);
});
