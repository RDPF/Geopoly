"""GeoPoly public exporters API (v27.1d).

This module exposes the final exporter functions through explicit named imports.
It intentionally avoids the older public __getattr__/getattr shim pattern so the
export surface is visible to static analysis and import-time smoke tests.
"""
from .runtime import (
    write_obj,
    write_stl_ascii,
    write_stl_binary,
    write_3mf_basic,
    write_off_file,
    write_svg_net,
    export_multi_sheet_pdf_png_svg,
    export_certified_layout_pdf,
    export_certified_layout_svg,
    export_batch_optimizer_pdf,
    export_batch_optimizer_json,
)

__all__ = [
    'write_obj',
    'write_stl_ascii',
    'write_stl_binary',
    'write_3mf_basic',
    'write_off_file',
    'write_svg_net',
    'export_multi_sheet_pdf_png_svg',
    'export_certified_layout_pdf',
    'export_certified_layout_svg',
    'export_batch_optimizer_pdf',
    'export_batch_optimizer_json',
]
