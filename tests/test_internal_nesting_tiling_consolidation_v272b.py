from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import geopoly

JOHNSON = ROOT / "geopoly" / "internal" / "johnson_toroidal_certified.py"
FIXED = ROOT / "geopoly" / "internal" / "fixed_scale_nesting.py"

def test_version_v272b():
    assert geopoly.VERSION == "27.3"

def test_single_active_solve_certified_nesting_def():
    text = "\n".join([JOHNSON.read_text(encoding="utf-8"), FIXED.read_text(encoding="utf-8")])
    assert text.count("def solve_certified_nesting(") == 1
    assert "def _legacy_solve_certified_nesting_v2520(" in text
    assert "def _legacy_solve_certified_nesting_v2522_autoscale(" in text
    assert "def _legacy_solve_certified_nesting_v2523_fixed_tile(" in text

def test_tiling_behavior_preserved_for_dodecahedron_fixed_scale():
    item = geopoly.CATALOG["Platônicos / Dodecaedro"]
    poly = item.build()
    cert = geopoly.search_certified_net(poly, attempts=80, scale_mm=50.0, max_seconds=4.0)
    nest = geopoly.solve_certified_nesting(poly, cert=cert, page="A4", scale_mm=50.0, page_policy="fixed_tile")
    assert getattr(nest, "tiled", False) is True
    assert getattr(nest, "scale_adjusted", True) is False
    assert nest.all_fit is True
    assert nest.page_count >= 2
