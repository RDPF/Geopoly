# GeoPoly v27.0 — Real Modular Core Refactor

GeoPoly é uma aplicação Python offline educacional e maker para Poliedros, análise de Euler, planificações impimíveis, exportação em STL, e sólidos formais de Johnson.

## Rodar
```bash
pip install -r requirements.txt
python run_geopoly.py
```

## Testar
```bash
python -m pytest
```

The suite keeps the 1167 regression checks and 19 universal headless export smoke checks.

## Technical note
Printable net validation is computational verification under geometric tolerance, not a formal proof of all possible unfoldings. Batch material optimization uses rectangular first-fit-decreasing packing with 0/90 rotation.

## Johnson dataset credit
Exact Johnson Solids, Zenodo record 10729583, DOI `10.5281/zenodo.10729583`, CC-BY 4.0.


## v27.3 note

This patch starts the explicit-import refactor at the public API boundary: `geopoly.geometry`, `geopoly.topology` and `geopoly.catalog` now declare named imports directly instead of using `getattr` pass-through shims. The validated internal staged runtime is intentionally preserved to avoid changing numerical results or the GUI.

### Nota v27.3

Esta versão remove os `globals().update(...)` internos em `geopoly/internal`, preservando o comportamento validado e a API pública. A cadeia interna passa a usar imports explícitos de dependência e listas de símbolos exportados, com testes de regressão para impedir a volta do re-merge amplo de namespace.



## GeoPoly v27.3.1 — JOSS Paper Completion Release

Esta versão preserva todas as funcionalidades validadas e consolida a arquitetura para publicação: imports públicos/internos explícitos, ausência de `globals().update`/`import *` no núcleo interno, funções centrais consolidadas, métodos de classe nativos e smoke tests universais de exportação em modo headless.

Validação: `run_self_tests()` retorna 1167/1167 testes OK e `run_export_smoke_tests()` retorna 19/19 verificações OK.

## Status do paper JOSS

A versão 27.3.1 não altera o núcleo computacional. Ela completa o material acadêmico voltado ao JOSS: `paper/paper.md` expandido, `paper/paper.bib` com referências de trabalho relacionado, metadados ORCID e README mais claro. A citação do software está em `CITATION.cff`; os dados formais dos sólidos de Johnson são creditados ao dataset Exact Johnson Solids no Zenodo (DOI: `10.5281/zenodo.10729583`).

A contribuição do GeoPoly como software de pesquisa está na integração de geometria de poliedros, educação matemática e fabricação maker: catálogo de sólidos nomeados, Johnson formais, redes imprimíveis verificadas computacionalmente, abas numeradas, ladrilhamento em escala fixa, smoke tests universais de exportação e otimização de material em lote para atividades de turma.
