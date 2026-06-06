# GeoPoly v27.0 — Real Modular Core Refactor

GeoPoly is an offline educational and maker-oriented Python application for polyhedra, Euler analysis, verified printable nets, batch material optimization, fabrication exports, and formal Johnson solids.

This v27.0 release keeps all validated behavior, GUI menus and results from v25.2.5.3, but removes the duplicated single-file legacy monolith from the release. The implementation is split into ordered internal modules and exposed through stable thematic public modules.

## Run
```bash
pip install -r requirements.txt
python run_geopoly.py
```

## Test
```bash
python -m pytest
```

The suite keeps the 1167 regression checks and 19 universal headless export smoke checks.

## Technical note
Printable net validation is computational verification under geometric tolerance, not a formal proof of all possible unfoldings. Batch material optimization uses rectangular first-fit-decreasing packing with 0/90 rotation.

## Johnson dataset credit
Exact Johnson Solids, Zenodo record 10729583, DOI `10.5281/zenodo.10729583`, CC-BY 4.0.


## v27.3.1 note

This patch starts the explicit-import refactor at the public API boundary: `geopoly.geometry`, `geopoly.topology` and `geopoly.catalog` now declare named imports directly instead of using `getattr` pass-through shims. The validated internal staged runtime is intentionally preserved to avoid changing numerical results or the GUI.


## GeoPoly v27.3.1 — JOSS Paper Completion Release

This release preserves all validated functionality while consolidating the architecture for publication: explicit public/internal imports, no internal `globals().update`/`import *` chain, consolidated core net/nesting/batch functions, native class methods, and universal headless export smoke tests.

Validation: `run_self_tests()` returns 1167/1167 passing tests and `run_export_smoke_tests()` returns 19/19 passing checks.

## JOSS paper status

Version 27.3.1 does not change the computational core. It completes the JOSS-facing scholarly material: an expanded `paper/paper.md`, a substantially broader `paper/paper.bib`, ORCID metadata, and clearer README context. The software should be cited through `CITATION.cff`; the formal Johnson-solid data are credited to the Exact Johnson Solids Zenodo dataset (DOI: `10.5281/zenodo.10729583`).

GeoPoly's research-software contribution is an integrated workflow for mathematics education and maker fabrication: named polyhedra, formal Johnson solids, computationally verified printable nets, glue-tab and page-layout support, fixed-scale tiled printing, universal export smoke tests, and batch material optimization for classroom sets.
