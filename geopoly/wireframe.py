"""GeoPoly public wireframe API."""
from . import runtime as _rt

WireframeParams = getattr(_rt, 'WireframeParams')
wireframe_edge_groups = getattr(_rt, 'wireframe_edge_groups')
wireframe_joint_groups = getattr(_rt, 'wireframe_joint_groups')
wireframe_manifest = getattr(_rt, 'wireframe_manifest')
wireframe_report = getattr(_rt, 'wireframe_report')
mesh_wireframe_full = getattr(_rt, 'mesh_wireframe_full')
mesh_rod_type = getattr(_rt, 'mesh_rod_type')
mesh_joint_type = getattr(_rt, 'mesh_joint_type')
export_wireframe_kit_zip = getattr(_rt, 'export_wireframe_kit_zip')
export_wireframe_parts_folder = getattr(_rt, 'export_wireframe_parts_folder')

def __getattr__(name):
    return getattr(_rt, name)

__all__ = ['WireframeParams', 'wireframe_edge_groups', 'wireframe_joint_groups', 'wireframe_manifest', 'wireframe_report', 'mesh_wireframe_full', 'mesh_rod_type', 'mesh_joint_type', 'export_wireframe_kit_zip', 'export_wireframe_parts_folder']
