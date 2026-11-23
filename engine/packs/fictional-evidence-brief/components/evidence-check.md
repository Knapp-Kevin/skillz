# Evidence check component

Input: the complete `collect` ledger. Compare each candidate statement
against supplied notes. Output supported statement-to-note mappings,
contradictions and UNKNOWNs. Never promote an inferred guess into a fact.
A missing ledger or unresolvable conflicting source holds the dependent
summary claim, rather than being marked passed.

This is a portable textual decision component, not an executable tool.
