"""GeoPoly public nets API."""
from . import runtime as _rt

NetFace = getattr(_rt, 'NetFace')
NetResult = getattr(_rt, 'NetResult')
MultiSheetResult = getattr(_rt, 'MultiSheetResult')
face_local_2d = getattr(_rt, 'face_local_2d')
sim_edge = getattr(_rt, 'sim_edge')
generate_tree_net = getattr(_rt, 'generate_tree_net')
search_best_net = getattr(_rt, 'search_best_net')
solve_multi_sheet = getattr(_rt, 'solve_multi_sheet')
plot_net_to_ax = getattr(_rt, 'plot_net_to_ax')
write_svg_net = getattr(_rt, 'write_svg_net')
export_multi_sheet_pdf_png_svg = getattr(_rt, 'export_multi_sheet_pdf_png_svg')

def __getattr__(name):
    return getattr(_rt, name)

__all__ = ['NetFace', 'NetResult', 'MultiSheetResult', 'face_local_2d', 'sim_edge', 'generate_tree_net', 'search_best_net', 'solve_multi_sheet', 'plot_net_to_ax', 'write_svg_net', 'export_multi_sheet_pdf_png_svg']
