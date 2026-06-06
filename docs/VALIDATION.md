# Validation Summary

GeoPoly v27.3 preserves the validated v25.2.5.3 functional reference and exposes it through a publication-oriented architecture.

Validation targets:

- `run_self_tests()`: 1167/1167 tests passing.
- `run_export_smoke_tests()`: 19/19 universal export smoke checks passing.
- Headless Matplotlib backend: automatic Agg fallback in CLI/headless environments.
- Exported artifacts checked by file existence, minimum size and basic structural checks.
- Johnson formal dataset is credited to Exact Johnson Solids, Zenodo DOI 10.5281/zenodo.10729583.

The printable-net verification is computational and tolerance-based. It certifies the generated layout under the exported numeric geometry and does not prove that a better or globally optimal unfolding/nesting does not exist. Batch material optimization currently uses rectangular first-fit-decreasing packing with 0/90 degree rotations.
