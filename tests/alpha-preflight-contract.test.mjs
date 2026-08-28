import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const read = (path) => readFileSync(join(ROOT, path), "utf8");

test("alpha preflight proves exact vendor materialization before catalog generation", () => {
  const preflight = read("scripts/initial-alpha-preflight.ts");
  const materialization = preflight.indexOf('name: "vendored source materialization"');
  const catalog = preflight.indexOf('name: "catalog determinism"');

  assert.ok(materialization >= 0, "preflight must include vendored source materialization proof");
  assert.ok(catalog > materialization, "vendor materialization must be proven before catalog generation");
  assert.match(preflight, /verify-vendor-materialization\.ts/);
});

test("alpha preflight requires every characterized skill to be available after materialization", () => {
  const preflight = read("scripts/initial-alpha-preflight.ts");
  assert.match(preflight, /verify-characterization-integrity\.ts/);
  assert.match(preflight, /--require-available/);
});

test("vendor materialization proof binds source registry paths to clean exact gitlinks", () => {
  const verifier = read("scripts/verify-vendor-materialization.ts");
  assert.match(verifier, /inclusion === "vendored"/);
  assert.match(verifier, /ls-tree/);
  assert.match(verifier, /160000/);
  assert.match(verifier, /rev-parse/);
  assert.match(verifier, /does not match pinned gitlink/);
  assert.match(verifier, /--porcelain/);
  assert.match(verifier, /is dirty/);
});
