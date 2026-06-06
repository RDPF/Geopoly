from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import geopoly

JOHNSON = ROOT / 'geopoly' / 'internal' / 'johnson_toroidal_certified.py'


def test_version_v272b():
    assert geopoly.VERSION == '27.3'


def test_internal_net_certification_has_single_active_final_defs():
    src = JOHNSON.read_text(encoding='utf-8')
    assert src.count('def verify_constructible_net(') == 1
    assert src.count('def robust_polygon_overlap_area(') == 1
    assert 'def _legacy_verify_constructible_net_v2520(' in src
    assert 'def _legacy_verify_constructible_net_v2521_pre_final(' in src
    assert 'def _legacy_robust_polygon_overlap_area_v2520(' in src
    assert 'def _legacy_robust_polygon_overlap_area_v2521_pre_final(' in src


def test_certified_net_behavior_preserved_for_dodecahedron():
    item = geopoly.CATALOG['Platônicos / Dodecaedro']
    poly = item.build()
    cert = geopoly.search_certified_net(poly, attempts=80, scale_mm=50.0, max_seconds=4.0)
    assert cert.constructible is True
    assert len(cert.face_overlaps) == 0
