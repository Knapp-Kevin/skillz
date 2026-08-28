import { test } from "node:test";
import assert from "node:assert/strict";
import { validateCatalogInvariants } from "../scripts/lib/catalog-invariants.mjs";

function validCatalog() {
  return {
    version: 2,
    counts: {
      localSkills: 2,
      vendorSkills: 3,
      totalIndexedSkillEntries: 5,
      uniqueSkillNames: 4,
      vendoredSources: 2,
      registeredSources: 3,
    },
    skills: [
      { name: "local-a" },
      { name: "local-b" },
    ],
    vendor: {
      "knowledge-work-plugins": {
        sourceId: "knowledge",
        plugins: [
          { name: "plugin-a", skills: [{ name: "vendor-a" }] },
        ],
      },
      "generic-source": {
        sourceId: "generic",
        skills: [{ name: "vendor-b" }, { name: "vendor-c" }],
      },
    },
  };
}

test("catalog invariants accept internally coherent schema-v2 output", () => {
  assert.deepEqual(validateCatalogInvariants(validCatalog()), []);
});

test("catalog invariants reject a vendored source that contributes zero skills", () => {
  const catalog = validCatalog();
  catalog.vendor["generic-source"].skills = [];
  catalog.counts.vendorSkills = 1;
  catalog.counts.totalIndexedSkillEntries = 3;
  catalog.counts.uniqueSkillNames = 3;

  const errors = validateCatalogInvariants(catalog);
  assert.ok(errors.some((error) => /contributed zero indexed skills/.test(error)));
});

test("catalog invariants reject source coverage and recomputed vendor-count mismatch", () => {
  const catalog = validCatalog();
  catalog.counts.vendoredSources = 3;
  catalog.counts.vendorSkills = 9;
  catalog.counts.totalIndexedSkillEntries = 11;

  const errors = validateCatalogInvariants(catalog);
  assert.ok(errors.some((error) => /vendor source entries 2 do not match counts\.vendoredSources 3/.test(error)));
  assert.ok(errors.some((error) => /computed vendor skill count 3 does not match counts\.vendorSkills 9/.test(error)));
});

test("catalog invariants reject local and aggregate count mismatch", () => {
  const catalog = validCatalog();
  catalog.counts.localSkills = 4;
  catalog.counts.totalIndexedSkillEntries = 5;

  const errors = validateCatalogInvariants(catalog);
  assert.ok(errors.some((error) => /local skill array length 2 does not match counts\.localSkills 4/.test(error)));
  assert.ok(errors.some((error) => /does not equal localSkills \+ vendorSkills/.test(error)));
});

test("catalog invariants reject duplicate vendored source identity", () => {
  const catalog = validCatalog();
  catalog.vendor["generic-source"].sourceId = "knowledge";

  const errors = validateCatalogInvariants(catalog);
  assert.ok(errors.some((error) => /duplicate sourceId knowledge/.test(error)));
});

test("catalog invariants reject impossible unique-name and source counts", () => {
  const catalog = validCatalog();
  catalog.counts.uniqueSkillNames = 6;
  catalog.counts.registeredSources = 1;

  const errors = validateCatalogInvariants(catalog);
  assert.ok(errors.some((error) => /uniqueSkillNames 6 cannot exceed totalIndexedSkillEntries 5/.test(error)));
  assert.ok(errors.some((error) => /registeredSources 1 cannot be less than vendoredSources 2/.test(error)));
});

test("catalog invariants reject malformed count fields and vendor shape", () => {
  const catalog = validCatalog();
  catalog.counts.vendorSkills = "three";
  catalog.vendor["generic-source"] = { sourceId: "generic" };

  const errors = validateCatalogInvariants(catalog);
  assert.ok(errors.some((error) => /index\.counts\.vendorSkills is missing or invalid/.test(error)));
  assert.ok(errors.some((error) => /has neither plugins\[\] nor skills\[\]/.test(error)));
});
