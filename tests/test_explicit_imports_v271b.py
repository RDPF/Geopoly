from pathlib import Path


def test_geometry_topology_catalog_use_explicit_imports():
    root = Path(__file__).resolve().parents[1] / "geopoly"
    for name in ["geometry.py", "topology.py", "catalog.py"]:
        text = (root / name).read_text(encoding="utf-8")
        assert "def __getattr__" not in text
        assert "getattr(_rt" not in text
        assert "from .runtime import" in text


def test_public_api_aliases_survive():
    import geopoly
    from geopoly.geometry import Polyhedron
    from geopoly.topology import HalfEdgeMesh
    from geopoly.catalog import CATALOG
    assert geopoly.VERSION == "27.3"
    assert Polyhedron is geopoly.Polyhedron
    assert HalfEdgeMesh is not None
    assert len(CATALOG) >= 200
    assert callable(geopoly.run_export_smoke_tests)
