# Capability dashboard maintenance

The README dashboard is **generated, not hand-redrawn**. It offers a polished SVG summary, an expandable 33-domain table, and a CSV that GitHub and spreadsheet apps can open. The older date-stamped graphs remain historical evidence.

**Single source of truth:** `registry/capability-dashboard-sources.json` points to the current, explicitly dated research audit and the current selected-method catalog. Do not edit generated rows or draw another chart manually. Research-link coverage includes rejected-only leads; Valuable References are study methods, not unchanged-use approvals. The global eligible count is still unknown.

Use Node.js 20+ (built-in modules only, no `npm install`):

```sh
node scripts/build-capability-dashboard.mjs --self-test
node scripts/build-capability-dashboard.mjs
node scripts/build-capability-dashboard.mjs --check
```

When meaningful new evidence is approved:
1. Commit the new source ledger, with exact source pins, grades, license status, and a dated review. Do **not** overwrite historical ledgers.
2. Point the manifest to that ledger (and any newer research audit); run the generator.
3. Review README readability, SVG labels and colors, CSV dimensions and exact totals; use `--check` to ensure committed files are consistent.
4. Only then merge. `--check` fails for stale content, invalid source taxonomy, duplicated selections or inconsistent catalog totals. It uses no network and performs no installation or external action.

The SVG is deliberately generated from the exact same model as the table and CSV. GitHub README pages cannot execute a live spreadsheet. These outputs are deterministic static views, so the next update is regeneration, not graphic design work.

**Known evidence limits:** This pipeline checks consistency and presentation, not licensing clearance, security or actual skill behavior. It never counts a raw candidate link as a recommended method. The 2026-11-02 Q4 audit and Q7 20-method catalog are the currently declared inputs.
