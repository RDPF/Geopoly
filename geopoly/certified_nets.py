"""GeoPoly public certified-net API with explicit imports.

This module exposes the final v25.2.x verified-net behavior from the
consolidated internal implementation, without public ``getattr`` shims.
"""
from .internal.fixed_scale_nesting import (
    CertifiedNetCertificate,
    certified_glue_tabs,
    detect_face_overlaps_for_poly,
    robust_polygon_overlap_area,
    search_certified_net,
    verify_constructible_net,
    solve_certified_nesting,
    certified_net_report,
    certified_net_payload,
    export_certified_layout_pdf,
    export_certified_layout_svg,
)

# Backward-compatible aliases requested by earlier public API drafts.
CertifiedNetResult = CertifiedNetCertificate
CertifiedNetComponent = CertifiedNetCertificate

__all__ = [
    'CertifiedNetCertificate',
    'CertifiedNetResult',
    'CertifiedNetComponent',
    'certified_glue_tabs',
    'detect_face_overlaps_for_poly',
    'robust_polygon_overlap_area',
    'search_certified_net',
    'verify_constructible_net',
    'solve_certified_nesting',
    'certified_net_report',
    'certified_net_payload',
    'export_certified_layout_pdf',
    'export_certified_layout_svg',
]
