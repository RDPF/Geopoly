from pathlib import Path


def test_internal_modules_do_not_use_globals_update():
    root = Path(__file__).resolve().parents[1]
    internal = root / 'geopoly' / 'internal'
    offenders = []
    for path in internal.glob('*.py'):
        text = path.read_text(encoding='utf-8')
        if 'globals().update' in text:
            offenders.append(path.name)
    assert offenders == []


def test_internal_modules_use_named_imports_not_wildcards():
    root = Path(__file__).resolve().parents[1]
    internal = root / 'geopoly' / 'internal'
    offenders = []
    for path in internal.glob('*.py'):
        text = path.read_text(encoding='utf-8')
        if 'import *' in text:
            offenders.append(path.name)
    assert offenders == []


def test_internal_modules_have_named_dependency_imports():
    root = Path(__file__).resolve().parents[1]
    expected_prefixes = {
        'sota_topology_symmetry.py': 'from .core_geometry_catalog import (',
        'wireframe_core.py': 'from .sota_topology_symmetry import (',
        'printable_nets.py': 'from .wireframe_core import (',
        'wireframe_mechanical_formula_symmetry.py': 'from .printable_nets import (',
        'johnson_toroidal_certified.py': 'from .wireframe_mechanical_formula_symmetry import (',
        'fixed_scale_nesting.py': 'from .johnson_toroidal_certified import (',
        'batch_optimizer.py': 'from .fixed_scale_nesting import (',
        'export_smoke_universal.py': 'from .batch_optimizer import (',
    }
    for filename, needle in expected_prefixes.items():
        text = (root / 'geopoly' / 'internal' / filename).read_text(encoding='utf-8')
        assert needle in text


def test_runtime_does_not_use_globals_update_or_wildcard_imports():
    root = Path(__file__).resolve().parents[1]
    text = (root / 'geopoly' / 'runtime.py').read_text(encoding='utf-8')
    assert 'globals().update' not in text
    assert 'import *' not in text


def test_runtime_and_smoke_still_work_after_named_internal_imports():
    import geopoly
    assert geopoly.VERSION == '27.3'
    rep = geopoly.run_self_tests()
    assert len(rep.results) == 1167
    assert all(r.ok for r in rep.results)
    smoke = geopoly.run_export_smoke_tests()
    assert smoke['ok'] is True
    assert smoke['passed'] == 19
    assert smoke['total'] == 19
