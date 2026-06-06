from pathlib import Path


def test_runtime_allowlist_audited_and_reduced():
    text = Path("geopoly/runtime.py").read_text(encoding="utf-8")
    assert "_EXPLICIT_OVERRIDE_BINDINGS" not in text
    assert "_SELFTEST_COMPATIBILITY_BINDINGS" in text
    assert "from .internal import wireframe_core as _wire_core" not in text
    assert "from .internal import wireframe_mechanical_formula_symmetry as _wire_mech" not in text
    assert "from .internal import fixed_scale_nesting as _fixed" not in text
    assert "from .internal import batch_optimizer as _batch" not in text
    assert "vars(_mod).update" not in text
    assert "globals().update" not in text


def test_runtime_compatibility_bindings_are_minimal_and_selftests_pass():
    import geopoly.runtime as rt
    groups = rt._SELFTEST_COMPATIBILITY_BINDINGS
    names = {m.__name__: set(v) for m, v in groups.items()}
    assert set(names) == {
        "geopoly.internal.core_geometry_catalog",
        "geopoly.internal.johnson_toroidal_certified",
    }
    assert len(names["geopoly.internal.core_geometry_catalog"]) == 6
    assert "solve_certified_nesting" in names["geopoly.internal.johnson_toroidal_certified"]


def test_public_selftest_aliases_are_present():
    import geopoly
    assert callable(geopoly.run_self_tests)
    assert callable(geopoly.run_export_smoke_tests)
    assert callable(geopoly.export_smoke_test_report)
    assert geopoly.VERSION == "27.3"
