from pathlib import Path


def test_exporters_and_selftests_use_explicit_imports():
    root = Path(__file__).resolve().parents[1] / "geopoly"
    for name in ["exporters.py", "selftests.py"]:
        text = (root / name).read_text(encoding="utf-8")
        assert "def __getattr__" not in text
        assert "getattr(_rt" not in text
        assert "from .runtime import" in text


def test_exporters_and_smoke_public_imports_work_headless(tmp_path):
    import geopoly
    from geopoly.catalog import CATALOG
    from geopoly.certified_nets import search_certified_net
    from geopoly.nesting import solve_certified_nesting
    from geopoly.exporters import (
        export_certified_layout_pdf,
        export_certified_layout_svg,
        write_stl_ascii,
        write_stl_binary,
        write_obj,
        write_off_file,
        write_3mf_basic,
    )
    from geopoly.selftests import run_export_smoke_tests, export_smoke_test_report

    assert geopoly.VERSION == "27.3"
    poly = CATALOG["Platônicos / Cubo ou Hexaedro"].build()
    cert = search_certified_net(poly, attempts=5)
    nesting = solve_certified_nesting(poly, cert=cert, page="A4", scale_mm=30.0, page_policy="auto")

    pdf = tmp_path / "net.pdf"
    svg = tmp_path / "net.svg"
    stl_a = tmp_path / "mesh_ascii.stl"
    stl_b = tmp_path / "mesh_binary.stl"
    obj = tmp_path / "mesh.obj"
    off = tmp_path / "mesh.off"
    threemf = tmp_path / "mesh.3mf"

    export_certified_layout_pdf(poly, cert, nesting, pdf)
    export_certified_layout_svg(poly, cert, nesting, svg)
    write_stl_ascii(poly, stl_a)
    write_stl_binary(poly, stl_b)
    write_obj(poly, obj)
    write_off_file(poly, off)
    write_3mf_basic(poly, threemf)

    for path in [pdf, svg, stl_a, stl_b, obj, off, threemf]:
        assert path.exists()
        assert path.stat().st_size > 100

    smoke = run_export_smoke_tests()
    assert smoke["ok"] is True
    assert smoke["passed"] == smoke["total"] == 19
    report = export_smoke_test_report(smoke)
    assert "smoke tests" in report and "19/19" in report
