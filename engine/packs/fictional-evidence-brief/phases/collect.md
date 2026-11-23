# Collect phase

Input: text explicitly supplied in the current task.

Read only those notes. Output a ledger assigning each note a stable local
index, with explicit UNKNOWN values for missing dates or attribution. Do
not infer missing facts. Do not fetch external sources or persist a profile.

Handoff: a complete ledger for `check`, or HOLD if the required notes
are absent and cannot be supplied.
