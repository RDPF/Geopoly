def test_selftests_full():
    import geopoly
    rep=geopoly.run_self_tests()
    assert rep.failed == 0, rep.as_text()
    assert rep.total >= 1167

def test_export_smokes():
    from geopoly.selftests import run_export_smoke_tests
    smoke=run_export_smoke_tests()
    assert smoke["ok"] and smoke["total"] >= 19
