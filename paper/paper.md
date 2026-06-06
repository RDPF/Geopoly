---
title: 'GeoPoly: an offline educational and maker-oriented polyhedra laboratory with verified printable nets and batch material optimization'
tags:
  - Python
  - computational geometry
  - mathematics education
  - polyhedra
  - digital fabrication
  - printable nets
  - paper modeling
authors:
  - name: Renato Dutra Pereira Filho
    orcid: 0000-0002-5411-0745
    affiliation: 1
affiliations:
  - name: Universidade Federal do Rio Grande (FURG), Brazil
    index: 1
date: 6 June 2026
bibliography: paper.bib
---

# Summary

GeoPoly is an offline Python application and package for exploring, validating, teaching, and fabricating polyhedra. It combines a named-solid catalog, formal data for the 92 Johnson solids, Euler and topological reports, interactive visualization, printable net generation, glue-tab labeling, fixed-scale page tiling, fabrication-oriented exports, and batch material optimization for classroom or makerspace print jobs. The software is intended for mathematics teachers, teacher educators, students, and digital-fabrication practitioners who need a workflow that starts from a polyhedron name or construction and ends in validated, printable, labeled material.

The project emphasizes reproducible output rather than only visual exploration. GeoPoly exports SVG, PDF, PNG, STL, OBJ, OFF, 3MF, TXT, JSON, and ZIP artifacts, and it includes headless smoke tests for these export paths. Printable nets are verified computationally under a documented geometric tolerance: face overlap is treated as the criterion for a valid net, while glue-tab conflicts are reported as fabrication-quality warnings rather than as mathematical failure. For physical classroom use, GeoPoly supports two complementary page policies: automatic scale reduction to fit a page, and fixed-scale tiled printing with registration marks. A batch optimizer packs multiple nets into shared pages using a first-fit-decreasing rectangular heuristic with 0/90 degree rotations, allowing a teacher to prepare a set of solids for an activity while reporting pages saved and page utilization.

# Statement of need

Polyhedra are a central topic across geometry, visualization, mathematical art, and physical modeling. Mature tools exist for research-oriented polyhedral computation, such as polymake [@polymake], for exploratory polyhedral operations and formula-driven construction, such as Antiprism [@antiprism] and polyHédronisme [@polyhedronisme], and for commercial three- and four-dimensional polyhedron modeling and net printing, such as Stella [@stella]. These systems are valuable, but their main design centers differ from the classroom/makerspace workflow targeted by GeoPoly. A teacher often needs not only to view or construct a polyhedron, but also to generate a scale-aware printable net, label faces and glue tabs, obtain a report suitable for instruction, export fabrication files, and pack many nets for a group activity using ordinary A4 or Letter paper.

The mathematical background is also non-trivial. Johnson solids originate in the classification of convex polyhedra with regular faces by Johnson [@johnson1966] and Zalgaller [@zalgaller1969]. GeoPoly embeds and credits the Exact Johnson Solids dataset [@exact_johnson_solids], which provides formal vertex, facet, and incidence data for all 92 proper Johnson solids. Printable edge unfoldings connect to a long-standing line of work on nets of polytopes. Shephard's work on convex nets [@shephard1975], later treatments in computational folding [@demaine2007], and modern discussions of Dürer's unfolding problem [@barvinok2018] motivate why a program should be explicit about what it verifies: finding a non-overlapping net is a witness for that generated layout, whereas failure of a heuristic search is not a proof that no net exists.

GeoPoly addresses this gap by integrating educational presentation and fabrication validation in a single installable Python package. Its contributions are practical rather than algorithmic novelty: (1) a bilingual, classroom-facing polyhedra laboratory; (2) formal Johnson-solid support and transparent status labels for exact, canonical, procedural, fallback, and experimental geometry; (3) computationally verified printable nets with glue-tab labeling and fixed-scale tiling; (4) headless export validation suitable for continuous integration; and (5) batch material optimization for activities that require many physical nets. This combination is particularly relevant in contexts where offline software, low-cost printing, and local fabrication workflows are important.

# Functionality

GeoPoly exposes both a graphical interface and a programmatic API. The GUI organizes solid selection, 3D visualization, Euler checks, printable nets, certified-net generation, fixed-scale tiling, batch nesting, wireframe-kit generation, formula-lab activities, and export tools. The Python API exposes geometry, topology, catalog, Johnson, nets, certified nets, nesting, batch optimizer, exporters, wireframe, formula lab, symmetry, and self-test modules. This allows the same validated routines to support an interactive lesson, a command-line batch export, or a scripted reproducibility check.

The fabrication workflow separates mathematical validity from fabrication convenience. A net is approved when all faces are present, the unfolding tree is valid, and there are no face-face overlaps in the exported numeric layout. Glue tabs are generated and numbered, but tab-face or tab-tab conflicts are reported as quality warnings because tabs may be folded underneath during assembly. Page layout is then solved by policy: single-page fitting with optional auto-scale, fixed-scale tiled printing with registration marks, whole-face grouping for easier assembly at possible paper cost, or batch packing of many nets. The batch optimizer uses a rectangular first-fit-decreasing strategy related to classical bottom-left and two-dimensional bin-packing heuristics [@chazelle1983; @berkey1987; @chwatal2011]. It is not a polygonal nesting optimizer, but it provides measurable savings for classroom sets by placing small nets into unused regions left by larger nets.

# Validation and limitations

GeoPoly v27.3.1 preserves the validated computational core of v27.3. The package reports 1167/1167 internal tests passing and 19/19 universal export smoke checks passing. The smoke tests run headlessly with the Agg backend and verify that representative PDF, SVG, PNG, STL ASCII, STL binary, OBJ, OFF, 3MF, JSON, TXT, ZIP, and folder exports are produced, non-empty, and structurally parseable where applicable. The public tests also check the architectural refactor: no internal `globals().update`, no `import *`, no persistent runtime allow-list, no class monkey-patching for core methods, and consolidated single definitions for net-certification, nesting, and batch-optimization functions.

The main limitations are deliberately documented. Net verification is computational and tolerance-based for the generated floating-point layout; it is not a formal proof over exact algebraic coordinates. A successful layout is a witness for that output, while a failed heuristic search does not prove that no edge unfolding exists. Batch optimization currently packs rectangular bounding boxes rather than true polygonal outlines, so it may leave concavities unused. Polygonal nesting, freer rotations, and stronger optimization heuristics are planned future work. GeoPoly therefore positions its verification claims as engineering validation for exported artifacts, not as a resolution of open mathematical unfolding problems.

# Acknowledgements

The author acknowledges the Exact Johnson Solids dataset archived on Zenodo [@exact_johnson_solids]. GeoPoly also builds on the open scientific Python ecosystem, especially NumPy [@harris2020] and Matplotlib [@hunter2007].

# References
