"""GeoPoly public geometry API (v27.1b).

This module now declares its public dependencies explicitly instead of using
getattr/__getattr__ pass-through shims. The validated runtime remains the
source of truth while the public surface is explicit and linter-friendly.
"""
from .runtime import (
    GeometryMeta, EulerResult, ValidationResult, Polyhedron,
    robust_orient2d, robust_orient3d, segments_properly_intersect_robust,
)

__all__ = [
    'GeometryMeta', 'EulerResult', 'ValidationResult', 'Polyhedron',
    'robust_orient2d', 'robust_orient3d', 'segments_properly_intersect_robust',
]
