from pathlib import Path

def test_runtime_no_wholesale_internal_remerge():
    import geopoly
    text = Path(geopoly.__file__).with_name("runtime.py").read_text(encoding="utf-8")
    assert "vars(_mod).update" not in text
    assert "_INTERNAL_MODULES" not in text
    assert "_SELFTEST_COMPATIBILITY_BINDINGS" in text
    assert geopoly.run_export_smoke_tests()["ok"]
