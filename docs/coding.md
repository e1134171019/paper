# Coding guide

Collector Core favors small domain modules and explicit boundaries. Avoid global mutable state. Business decisions belong in pure functions. Network, SQLite, filesystem, and export operations must be obvious from function/module names and must not be hidden inside canonicalization code.

The v0.1 identity contract is conservative: normalize DOI first; use normalized title only when both records have no DOI. A DOI-bearing record and DOI-less record with the same title remain separate until a later metadata-enrichment stage resolves identity.
