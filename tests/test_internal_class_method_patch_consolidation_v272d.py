from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "geopoly" / "internal" / "core_geometry_catalog.py"
SOTA = ROOT / "geopoly" / "internal" / "sota_topology_symmetry.py"
JOHNSON = ROOT / "geopoly" / "internal" / "johnson_toroidal_certified.py"


def test_version_v272d():
    import geopoly
    assert geopoly.VERSION == "27.3"


def test_direct_method_monkey_patches_removed_from_internal_core():
    text = JOHNSON.read_text(encoding="utf-8")
    forbidden = [
        "CatalogItem.build = _catalogitem_build_v25011",
        "CatalogItem.build = _catalog_item_build_v251",
        "Polyhedron.validate = _poly_validate_v25011",
        "HalfEdgeMesh.dual_adjacency = _halfedge_dual_adjacency_v25011",
        "HalfEdgeMesh.is_closed = _halfedge_is_closed_v25011",
        "HalfEdgeMesh.is_manifold = _halfedge_is_manifold_v25011",
        "HalfEdgeMesh.genus_hint = _halfedge_genus_hint_v25011",
    ]
    for marker in forbidden:
        assert marker not in text
    assert "Polyhedron._validate_impl =" not in text
    assert "CatalogItem._build_impl =" not in text
    assert "HalfEdgeMesh._genus_hint_impl =" not in text


def test_classes_own_native_methods():
    core = CORE.read_text(encoding="utf-8")
    sota = SOTA.read_text(encoding="utf-8")
    assert "getattr(type(self), '_validate_impl'" not in core
    assert "getattr(type(self), '_build_impl'" not in core
    assert "getattr(type(self), '_dual_adjacency_impl'" not in sota
    assert "getattr(type(self), '_is_closed_impl'" not in sota
    assert "getattr(type(self), '_is_manifold_impl'" not in sota
    assert "getattr(type(self), '_genus_hint_impl'" not in sota


def test_toroidal_validate_and_halfedge_still_work():
    import geopoly
    from geopoly.topology import HalfEdgeMesh
    labels = ["Toro", "Császár", "Szilassi"]
    checked = 0
    for item in geopoly.runtime.CATALOG_ITEMS:
        if any(label in item.key or label in item.name for label in labels):
            p = item.build()
            v = p.validate()
            if v.chi == 0 and v.closed and v.manifold:
                assert v.genus_hint == 1.0
                hm = HalfEdgeMesh(p.vertices, p.faces)
                assert hm.is_closed()
                assert hm.is_manifold()
                assert hm.genus_hint() == 1.0
                checked += 1
    assert checked >= 2
