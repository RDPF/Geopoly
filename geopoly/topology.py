"""GeoPoly public topology API (v27.1b).

Explicit public imports for the topology/half-edge layer.
"""
from .runtime import (
    HalfEdge, HalfEdgeMesh, halfedge_mesh,
    _consistent_face_orientation_v25011, orient_polyhedron_faces_consistently,
)

__all__ = [
    'HalfEdge', 'HalfEdgeMesh', 'halfedge_mesh',
    '_consistent_face_orientation_v25011', 'orient_polyhedron_faces_consistently',
]
