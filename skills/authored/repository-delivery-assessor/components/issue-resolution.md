# Component: issue resolution stewardship

**Select when:** The approved objective is to resolve a repository backlog
through actual implementation, justified consolidation or accurate disposition.
This component is not a substitute for source debt triage; source annotation
harvesting stays in `source-debt-triage`.

1. Bind exact repo, authorized issue subset, delivery outcome and current
   mutation rights. Review an issue's actual acceptance and relevant comments;
   a comment count or age alone never makes it unhealthy.
2. Group by real obligation and outcome: actionable defect; release blocker;
   unimplemented feature; duplicate; finished-but-unverified; research
   requiring an owner decision; obsolete requirement; or UNKNOWN. Preserve
   the canonical obligation when merging duplicates.
3. For each obligation identify `owner | exact next engineering operation |
   blocked reason/evidence | PR/source revision | necessary test |
   customer/operational acceptance | closure condition`.
4. Prefer implementing a bounded fix over creating another tracker, repeated
   audits or broad refactoring. Do not create a tracking issue where one
   appropriate issue already exists.
5. For closure, inspect code/review/merge plus any separate deployment and
   outcome evidence. Never close a real defect because CI is green, a commit
   exists or an agent says "done".
6. If a duplicate, retain its unique facts in the canonical record *before*
   proposing closure. If obsolete, show the owner decision/changed architecture.
   If blocked, name the precise external dependency and what is already ready.
7. Report proposed versus actually executed issue edits/closures with receipts.
   Issue write, merge, deletion, cross-repo linking and notifying a person each
   require the correct authorization; a read-only assessment does none of them.

Decision codes: ADVANCE to implementation; REPAIR a demonstrated defect;
VERIFY missing acceptance; CLOSE only with evidence; PARK genuinely optional
work without losing discoverability; ESCALATE only a real authority blocker.
A lower issue count is not an outcome metric.
