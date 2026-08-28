const COUNT_KEYS = [
  "localSkills",
  "vendorSkills",
  "totalIndexedSkillEntries",
  "uniqueSkillNames",
  "vendoredSources",
  "registeredSources",
];

function nonNegativeInteger(value) {
  return Number.isInteger(value) && value >= 0;
}

function sourceSkillCount(source, label, errors) {
  if (Array.isArray(source?.plugins)) {
    let total = 0;
    for (const plugin of source.plugins) {
      if (!Array.isArray(plugin?.skills)) {
        errors.push(`${label}: plugin ${plugin?.name ?? "<unnamed>"} is missing a skills array`);
        continue;
      }
      total += plugin.skills.length;
    }
    return total;
  }

  if (Array.isArray(source?.skills)) return source.skills.length;

  errors.push(`${label}: vendored source has neither plugins[] nor skills[]`);
  return 0;
}

/**
 * Validate semantic invariants for generated schema-v2 catalog output.
 * Returns an array of human-readable errors; an empty array means the catalog
 * is internally coherent enough for the separate exact-source and behavioral
 * proof stages to continue.
 */
export function validateCatalogInvariants(index) {
  const errors = [];

  if (index?.version !== 2) {
    errors.push(`expected schema version 2, found ${index?.version ?? "missing"}`);
  }

  const counts = index?.counts ?? {};
  for (const key of COUNT_KEYS) {
    if (!nonNegativeInteger(counts[key])) {
      errors.push(`index.counts.${key} is missing or invalid`);
    }
  }

  // Stop arithmetic checks from turning malformed values into misleading NaN
  // follow-on failures. Shape checks below can still report useful detail.
  const countsValid = COUNT_KEYS.every((key) => nonNegativeInteger(counts[key]));

  const localSkills = Array.isArray(index?.skills) ? index.skills : null;
  if (!localSkills) {
    errors.push("index.skills is missing or is not an array");
  } else if (countsValid && localSkills.length !== counts.localSkills) {
    errors.push(`local skill array length ${localSkills.length} does not match counts.localSkills ${counts.localSkills}`);
  }

  const vendorEntries = index?.vendor && typeof index.vendor === "object" && !Array.isArray(index.vendor)
    ? Object.entries(index.vendor)
    : null;

  if (!vendorEntries) {
    errors.push("index.vendor is missing or is not an object");
  } else {
    if (countsValid && vendorEntries.length !== counts.vendoredSources) {
      errors.push(`vendor source entries ${vendorEntries.length} do not match counts.vendoredSources ${counts.vendoredSources}`);
    }

    const sourceIds = new Set();
    let computedVendorSkills = 0;

    for (const [key, source] of vendorEntries) {
      const label = `vendor.${key}`;
      if (typeof source?.sourceId !== "string" || !source.sourceId.trim()) {
        errors.push(`${label}: missing sourceId`);
      } else if (sourceIds.has(source.sourceId)) {
        errors.push(`${label}: duplicate sourceId ${source.sourceId}`);
      } else {
        sourceIds.add(source.sourceId);
      }

      const count = sourceSkillCount(source, label, errors);
      computedVendorSkills += count;
      if (count <= 0) {
        errors.push(`${label}: contributed zero indexed skills`);
      }
    }

    if (countsValid && computedVendorSkills !== counts.vendorSkills) {
      errors.push(`computed vendor skill count ${computedVendorSkills} does not match counts.vendorSkills ${counts.vendorSkills}`);
    }
  }

  if (countsValid) {
    if (counts.localSkills <= 0) errors.push("counts.localSkills must be greater than zero");
    if (counts.vendorSkills <= 0) errors.push("counts.vendorSkills must be greater than zero");
    if (counts.vendoredSources <= 0) errors.push("counts.vendoredSources must be greater than zero");
    if (counts.registeredSources < counts.vendoredSources) {
      errors.push(`registeredSources ${counts.registeredSources} cannot be less than vendoredSources ${counts.vendoredSources}`);
    }

    const expectedTotal = counts.localSkills + counts.vendorSkills;
    if (counts.totalIndexedSkillEntries !== expectedTotal) {
      errors.push(`totalIndexedSkillEntries ${counts.totalIndexedSkillEntries} does not equal localSkills + vendorSkills (${expectedTotal})`);
    }

    if (counts.uniqueSkillNames <= 0) errors.push("counts.uniqueSkillNames must be greater than zero");
    if (counts.uniqueSkillNames > counts.totalIndexedSkillEntries) {
      errors.push(`uniqueSkillNames ${counts.uniqueSkillNames} cannot exceed totalIndexedSkillEntries ${counts.totalIndexedSkillEntries}`);
    }
  }

  return errors;
}
