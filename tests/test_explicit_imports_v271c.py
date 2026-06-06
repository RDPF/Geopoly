from pathlib import Path


def test_certified_nets_and_nesting_use_explicit_imports():
    root = Path(__file__).resolve().parents[1] / "geopoly"
    for name in ["certified_nets.py", "nesting.py"]:
        text = (root / name).read_text(encoding="utf-8")
        assert "def __getattr__" not in text
        assert "getattr(_rt" not in text
        assert "from .internal.fixed_scale_nesting import" in text


def test_certified_nets_public_imports_are_callable():
    import geopoly
    from geopoly.certified_nets import (
        CertifiedNetCertificate,
        search_certified_net,
        verify_constructible_net,
        solve_certified_nesting,
        certified_net_payload,
    )
    from geopoly.nesting import solve_certified_nesting as nesting_solve
    from geopoly.catalog import CATALOG

    assert geopoly.VERSION == "27.3"
    assert CertifiedNetCertificate is not None
    assert callable(search_certified_net)
    assert callable(verify_constructible_net)
    assert callable(solve_certified_nesting)
    assert callable(certified_net_payload)
    assert callable(nesting_solve)

    poly = CATALOG["Platônicos / Cubo ou Hexaedro"].build()
    cert = search_certified_net(poly, attempts=10)
    assert cert is not None
    assert len(cert.face_overlaps) == 0
    nesting = nesting_solve(poly, cert=cert, page="A4", scale_mm=40.0, page_policy="auto")
    payload = certified_net_payload(poly, cert, nesting)
    assert len(payload["face_overlaps"]) == 0
    assert payload["nesting"]["all_fit"] is True
