from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
BATCH = ROOT / "geopoly" / "internal" / "batch_optimizer.py"
PUBLIC = ROOT / "geopoly" / "batch_optimizer.py"


def test_version_v272c():
    import geopoly
    assert geopoly.VERSION == "27.3"


def test_single_active_solve_batch_material_optimizer_def():
    text = BATCH.read_text(encoding="utf-8")
    assert text.count("def solve_batch_material_optimizer(") == 1


def test_batch_optimizer_public_api_uses_explicit_imports():
    text = PUBLIC.read_text(encoding="utf-8")
    assert "def __getattr__" not in text
    assert "getattr(_rt" not in text
    assert "from .runtime import" in text


def test_batch_optimizer_exports_and_metrics(tmp_path):
    import geopoly
    from geopoly.batch_optimizer import (
        BatchNetJob, solve_batch_material_optimizer, batch_optimizer_payload,
        batch_optimizer_report, export_batch_optimizer_pdf, export_batch_optimizer_json,
        export_batch_optimizer_report_txt,
    )

    keys = []
    for needle in ["Tetraedro", "Cubo", "Octaedro", "Dodecaedro", "Icosaedro"]:
        keys.append(next(it.key for it in geopoly.runtime.CATALOG_ITEMS if needle in it.key and "Platônicos" in it.key))
    jobs = [BatchNetJob(i, k, k, 50.0, 1) for i, k in enumerate(keys, 1)]
    res = solve_batch_material_optimizer(jobs, page="A4", margin_mm=10.0, attempts=80, allow_rotate=True)
    assert res.optimized_pages <= res.baseline_pages
    assert res.optimized_utilization_percent >= res.baseline_utilization_percent
    assert 0.0 <= res.optimized_utilization_percent <= 100.0

    payload = batch_optimizer_payload(res)
    assert payload["optimized_pages"] == res.optimized_pages
    assert payload["baseline_pages"] == res.baseline_pages
    assert len(payload["placements"]) == len(res.placements)
    assert "Batch Material Optimizer" in batch_optimizer_report(res)

    pdf = tmp_path / "batch.pdf"
    jsn = tmp_path / "batch.json"
    txt = tmp_path / "batch.txt"
    export_batch_optimizer_pdf(res, pdf)
    export_batch_optimizer_json(res, jsn)
    export_batch_optimizer_report_txt(res, txt)
    assert pdf.stat().st_size > 1000
    assert jsn.stat().st_size > 500
    assert txt.stat().st_size > 500
    assert json.loads(jsn.read_text(encoding="utf-8"))["optimized_pages"] == res.optimized_pages
