# Architecture

GeoPoly v27.3 uses a package-oriented architecture with thematic public modules and consolidated internal implementation modules.

Public API modules include `geometry`, `topology`, `catalog`, `johnson`, `nets`, `certified_nets`, `nesting`, `batch_optimizer`, `exporters`, `wireframe`, `formula_lab`, `symmetry`, `gui` and `selftests`.

Internal modules no longer use the historical `globals().update(...)` or wildcard import chain. The central stacks for net certification, nesting/tiling and batch optimization have been consolidated to one active final definition per function. Former class monkey-patches have been replaced by class-native behavior.

The runtime namespace keeps the stable public API and applies temporary compatibility only while executing historical regression wrappers. Normal imports do not rebind internal modules persistently.
