
## v27.3.1 — JOSS Paper Completion Release

- Expanded `paper/paper.md` into a substantive JOSS manuscript with Summary, Statement of need, Functionality, Validation and limitations, and Acknowledgements.
- Expanded `paper/paper.bib` from a single dataset reference to related work on Johnson solids, edge unfoldings, computational folding, polyhedral software, bin packing, NumPy, and Matplotlib.
- Added ORCID metadata for Renato Dutra Pereira Filho (`0000-0002-5411-0745`) to the paper, `CITATION.cff`, and `.zenodo.json`.
- Updated README/README.pt-BR to describe the JOSS paper status and the integrated education/fabrication contribution.
- No functional code changes beyond version/edition metadata.

# Changelog

## v27.3 — JOSS-ready Architecture Release

- Preserves all GeoPoly functionality, GUI menus, public API, exports and validated results.
- Removes persistent runtime compatibility rebinding; historical self-test compatibility is applied only inside a temporary test context.
- Keeps explicit public/internal imports and the consolidated net-certification, nesting/tiling and batch-optimizer stacks.
- Adds JOSS-oriented documentation: statement of need, validation summary and paper draft.
- Confirms the validated reference: 1167/1167 self-tests and 19/19 universal export smoke checks.


## v27.3 — Remove Internal globals().update

- Removed internal `globals().update(...)` namespace re-merge calls from `geopoly/internal/*.py`.
- Replaced internal chained namespace updates with explicit dependency imports using stable module boundaries.
- Added regression tests ensuring internal modules do not contain `globals().update`.
- Preserved all GUI behavior, public API, self-tests and universal export smoke tests.

## v27.3 — Runtime Allow-list Audit

- Consolidates the batch material optimizer boundary around a single active final implementation of `solve_batch_material_optimizer`.
- Converts the public `geopoly.batch_optimizer` module to explicit named imports.
- Adds regression tests for batch optimizer API importability, page savings, report/JSON/PDF export, and single active definition.
- Preserves all GUI behavior, public API, self-tests and universal export smoke tests.
# Changelog

## v27.2b — Internal Nesting/Tiling Consolidation Patch
- Preserves all v27.3 functionality, menus, tests and public behavior.
- Consolidates the active internal net-certification functions so only the final validated `verify_constructible_net` and `robust_polygon_overlap_area` definitions remain public in `johnson_toroidal_certified.py`.
- Renames historical superseded definitions to explicit `_legacy_*` names, turning the old override stack into documented compatibility history rather than active redefinitions.
- Keeps public API, GUI and export behavior unchanged.

## v27.2b — Consolidated Exporters/Smoke Tests Patch
- Preserves all v27.1c functionality, menus, tests and public behavior.
- Consolidates public `geopoly.exporters` and `geopoly.selftests` APIs with explicit named imports.
- Removes public `__getattr__`/`getattr(_rt, ...)` shims from exporters and selftests modules.
- Preserves universal export smoke coverage: 19/19 smoke checks.

## v27.2b — Consolidated Exporters/Smoke Tests Patch
- Preserves all v27.1a functionality, menus, tests and public behavior.
- Replaces the public geometry/topology/catalog getattr pass-through shims with explicit named imports.
- Restores and preserves public smoke-test aliases.
- Keeps the validated internal staged runtime unchanged for behavior stability.
- Adds pytest coverage ensuring geometry.py, topology.py and catalog.py use explicit imports.

# Changelog

## v27.0
- Split implementation into internal modules; removed duplicated monolithic reference.
- Preserved all v25.2.5.3 functionality, GUI menus, tests and export behavior.
