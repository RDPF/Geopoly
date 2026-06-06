from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "geopoly" / "internal" / "core_geometry_catalog.py"
SOTA = ROOT / "geopoly" / "internal" / "sota_topology_symmetry.py"
JOHNSON = ROOT / "geopoly" / "internal" / "johnson_toroidal_certified.py"


def test_version_v272g():
    import geopoly
    assert geopoly.VERSION == "27.3"


def test_no_class_monkey_patch_or_hook_assignment_remains():
    joined = "\n".join(
        p.read_text(encoding="utf-8") for p in (CORE, SOTA, JOHNSON)
    )
    forbidden = [
        "Polyhedron.validate =",
        "CatalogItem.build =",
        "HalfEdgeMesh.dual_adjacency =",
        "HalfEdgeMesh.is_closed =",
        "HalfEdgeMesh.is_manifold =",
        "HalfEdgeMesh.genus_hint =",
        "Polyhedron._validate_impl =",
        "CatalogItem._build_impl =",
        "CatalogItem._build_toroidal_orientation_impl =",
        "HalfEdgeMesh._dual_adjacency_impl =",
        "HalfEdgeMesh._is_closed_impl =",
        "HalfEdgeMesh._is_manifold_impl =",
        "HalfEdgeMesh._genus_hint_impl =",
        "getattr(type(self), '_validate_impl'",
        "getattr(type(self), '_build_impl'",
        "getattr(type(self), '_dual_adjacency_impl'",
        "getattr(type(self), '_is_closed_impl'",
        "getattr(type(self), '_is_manifold_impl'",
        "getattr(type(self), '_genus_hint_impl'",
    ]
    for marker in forbidden:
        assert marker not in joined


def test_native_methods_are_defined_in_owning_classes():
    core = CORE.read_text(encoding="utf-8")
    sota = SOTA.read_text(encoding="utf-8")
    assert "def validate(self):" in core
    assert "def build(self):" in core
    assert "def dual_adjacency(self):" in sota
    assert "def is_closed(self):" in sota
    assert "def is_manifold(self):" in sota
    assert "def genus_hint(self):" in sota
    assert "_consistent_face_orientation_v272g" in core


def test_toroidal_validate_and_halfedge_still_work_native_methods():
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
