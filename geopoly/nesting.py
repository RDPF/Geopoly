"""GeoPoly public nesting API with explicit imports.

This module exposes the final fixed-scale, auto-scale and tiled page-layout
solver without public ``getattr``/``__getattr__`` shims.
"""
from .internal.fixed_scale_nesting import (
    solve_certified_nesting,
    _v2523_make_tiled_windows_for_component,
    _v2524_choose_tiled_layout,
    _v2524_make_whole_face_components,
    _v2524_pack_components_best,
)

__all__ = [
    'solve_certified_nesting',
    '_v2523_make_tiled_windows_for_component',
    '_v2524_choose_tiled_layout',
    '_v2524_make_whole_face_components',
    '_v2524_pack_components_best',
]
