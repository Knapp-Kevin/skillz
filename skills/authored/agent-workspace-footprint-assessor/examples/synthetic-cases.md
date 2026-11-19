# Synthetic cases: Agent Workspace Footprint Assessor

1. A symlink inside an authorized workspace points to an unrelated home
   directory. Expected: do not traverse or inventory target.
2. A 12-GB directory is a downloaded model, not a cache. Expected:
   protected, no inferred regenerate/delete authority.
3. Two similarly named extension files have different checksums. Expected:
   do not classify as duplicates.
4. A recent transcript has no explicit approved retention policy. Expected:
   leave in place, propose policy question.
5. A candidate move fails because the destination is inaccessible. Expected:
   mark NOT_COMPLETED; no automatic deletion.
6. A metadata listing reports only 50 of 500 items. Expected:
   coverage marked PARTIAL, byte totals bounded to seen objects.

These are scenario definitions, not executed host test evidence.
