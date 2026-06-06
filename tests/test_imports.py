def test_public_imports():
    import geopoly
    assert geopoly.VERSION == "27.3"
    from geopoly.geometry import Polyhedron
    from geopoly.catalog import CATALOG
    from geopoly.batch_optimizer import BatchNetJob
    assert Polyhedron is not None and len(CATALOG) >= 200 and BatchNetJob is not None
    assert callable(geopoly.run_export_smoke_tests)

def test_version_info():
    import geopoly
    info=geopoly.version_info()
    assert info["version"]=="27.3"
    assert "explicit public imports" in info["implementation"]
