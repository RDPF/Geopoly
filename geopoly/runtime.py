"""Final assembled GeoPoly v27.2g runtime namespace.

This release removes the broad runtime re-merge that previously copied the final
namespace back into every internal module. To preserve the validated historical
late-binding behavior while avoiding ``vars(module).update(vars(final))``, only a
small, explicit list of historical override symbols is rebound in the modules
where older self-test wrappers still resolve names through their original module
``__globals__``.
"""
# Public runtime namespace: expose the final validated implementation with named imports.
from .internal.export_smoke_universal import (
    annotations, base64, hashlib, json, math, os, re, struct, tempfile, urllib, zipfile, zlib,
    Counter, defaultdict, deque, Fraction, dataclass, asdict, field, Path, Any, Dict, List,
    Optional, Sequence, Tuple, tk, ttk, filedialog, messagebox, np, matplotlib,
    _geopoly_select_matplotlib_backend, GEOPOLY_MPL_BACKEND, plt, FigureCanvasTkAgg, PdfPages,
    MplPolygon, Rectangle, Poly3DCollection, APP_NAME, VERSION, EDITION, EPS, CATALOG_B64_ZLIB,
    GeometryMeta, EulerResult, ValidationResult, Polyhedron, CatalogItem, _load_embedded_catalog,
    _geometry_status_rank, deduplicate_catalog_items, JOHNSON_ZENODO_RECORD, JOHNSON_ZENODO_DOI,
    JOHNSON_CACHE_DIR, JOHNSON_LOCAL_DIRS, JOHNSON_OFFLINE_BUNDLE_B64_ZLIB,
    JOHNSON_OFFLINE_BUNDLE_FILENAMES, _JOHNSON_OFFLINE_CACHE, _decode_johnson_offline_payload,
    load_johnson_offline_bundle, build_johnson_offline_bundle_from_folder,
    save_johnson_offline_bundle_from_folder, download_johnson_exact_folder_from_zenodo,
    install_johnson_offline_bundle_from_zenodo, require_all_johnson_formal_or_raise,
    johnson_formal_availability_report, _johnson_number_from_item, johnson_exact_url,
    _johnson_candidate_paths, parse_zenodo_johnson_json, parse_off, parse_obj_simple,
    load_johnson_exact_data, try_build_formal_johnson, CATALOG_ITEMS, CATALOG, group_values,
    face_internal_angles, vertex_signature, regularity_report, revolution_error_report,
    faceted_revolution_error_analysis, polyhedral_regularity_analysis,
    vertex_transitivity_analysis, fdm_estimate, full_report, NetFace, NetResult, MultiSheetResult,
    face_local_2d, sim_edge, orient2d, point_on_segment, point_in_poly_strict, seg_inter, bbox,
    bbox_overlap, poly_overlap, detect_overlaps, generate_tree_net, search_best_net, sheet_bbox,
    estimate_page_fit, solve_multi_sheet, safe_name, tri_normal, write_obj, write_stl_ascii,
    write_stl_binary, write_3mf_basic, draw_tabs, plot_net_to_ax, write_svg_net,
    export_multi_sheet_pdf_png_svg, polygon_area2d, TestCaseResult, TestReport,
    EXPECTED_SIGNATURES_V2301, _signature, FORMULA_LAB_CASES, FORMULA_DEFAULTS,
    FORMULA_PARAM_LABELS, _regular_polygon_area, _regular_polygon_apothem, _regular_polygon_radius,
    _poly_area_3d, _poly_volume_3d, _regular_ngon_xy, _mesh_box, _mesh_regular_prism,
    _mesh_regular_pyramid, _mesh_regular_frustum, _mesh_cylinder, _mesh_cone, _mesh_sphere,
    formula_lab_compute, formula_lab_text, formula_lab_plot, run_formula_lab_self_tests,
    run_self_tests, GeoPolyApp, analyze_face_combination_ui, exercise_text_ui, GeoPolyAppV2322,
    _ORIENT2D_BOUND, _ORIENT3D_BOUND, _frac, robust_orient2d, robust_orient3d,
    segments_properly_intersect_robust, robust_seg_inter, robust_point_on_segment, HalfEdge,
    HalfEdgeMesh, halfedge_mesh, SymmetryReportV242, SymmetryReportV24, _rot_matrix,
    _nearest_permutation, _permutation_residual, _maps_vertex_set, _classify_symmetry,
    _rotation_group_matrices, _orbits_from_permutations, _edge_orbits_from_perms,
    _face_orbits_from_perms, _stabilizers, _round_sig, _vertex_signature, _edge_signature,
    _face_signature, _orbit_signature_table, detect_symmetry_v24, detect_symmetry_v242,
    symmetry_report_advanced_dict, _format_orbit_rows, symmetry_report_text, midsphere_defect,
    _planarize_vertices, _tangentify_vertices, canonical_form_v24, canonical_lab_report,
    run_v24_sota_self_tests, GeoPolyAppV240, main, WireframeParams, _wf_norm, _wf_basis_from_dir,
    mesh_cylinder_between, mesh_tube_along_x, mesh_uv_sphere, combine_meshes, transform_mesh,
    _rotation_from_x_to_dir, write_mesh_stl_ascii, _poly_neighbors, wireframe_edge_groups,
    _joint_angles_for_dirs, wireframe_joint_groups, wireframe_manifest, wireframe_report,
    mesh_wireframe_full, mesh_rod_type, mesh_joint_type, mesh_rod_groups_display,
    mesh_joint_groups_display, export_wireframe_kit_zip, _RUN_SELF_TESTS_V242, GeoPolyAppV250,
    _gp2501_mesh_to_collection, _gp2501_autoscale_3d, _gp2501_plot_mesh, GeoPolyAppV2501,
    _RUN_SELF_TESTS_V2501_BASE, colorchooser, _GP2503_FACE_PALETTE, _GP2503_ALT_PALETTE,
    _gp2503_svg_escape, _gp2503_norm_color, _gp2503_valid_hex, _gp2503_face_label,
    _gp2503_face_color, _gp2503_point_in_polygon, _gp2503_tab_polygon,
    _gp2503_edge_key_from_vertices, _gp2503_segments_coincident, _gp2503_cut_tab_polygons,
    _gp2503_plot_net_to_ax, _gp2503_write_svg_net, GeoPolyAppV2503, _RUN_SELF_TESTS_V2503_BASE,
    _PAGE_SIZES_MM_V2505, _gp2505_page_size_mm, _gp2505_net_all_points, _gp2505_net_bounds,
    _gp2505_print_layout_report, _gp2505_edge_occurrences_2d, _gp2505_tab_and_fold_records,
    _gp2505_plot_printable_net_to_ax, _gp2505_write_svg_printable_net, _gp2505_draw_page_tile,
    _gp2505_export_paginated_pdf, _gp2505_write_assembly_report, GeoPolyAppV2505,
    _RUN_SELF_TESTS_V2505_BASE, _WF_MATERIAL_PRESETS, _WF_COLOR_PALETTE, _wf_material_name,
    _wf_material_profile, _wf_with_recommended_clearance, _wf_type_color,
    _wf_centerline_collision_threshold_deg, wireframe_connector_collision_report,
    _wf_edge_type_map, _wf_joint_type_map, wireframe_assembly_sequence,
    wireframe_print_orientation_report, _WF_BASE_MESH_TUBE_ALONG_X, _WF_BASE_MESH_JOINT_TYPE,
    _WF_BASE_EXPORT_ZIP, _wf_mesh_marker_rings_along_x, _wf_mesh_pin_collar,
    _wf_mesh_joint_marker_bumps, export_wireframe_parts_folder, _RUN_SELF_TESTS_V2506_BASE,
    GeoPolyAppV2506, _FORMULA_PREV_CASES_V2507, _FORMULA_PREV_DEFAULTS_V2507,
    _FORMULA_PREV_LABELS_V2507, _formula_lab_compute_base_v2507, _formula_lab_plot_base_v2507,
    _formula_lab_text_base_v2507, FORMULA_ADVANCED_CASES, _case, _PLATONIC_ARCH_FORMULAS,
    _mesh_torus_formula, _mesh_ellipsoid_formula, _scaled_catalog_mesh_for_edge,
    _formula_mesh_values, _ellipsoid_area_knud_thomsen, _formula_lab_text_rich,
    formula_lab_student_prompt, formula_lab_exercise_sheet_text, formula_lab_exercise_sheet_latex,
    _formula_plot_cylinder_animation, _formula_plot_cone_animation,
    _formula_plot_frustum_cone_animation, GeoPolyAppV2507, _run_self_tests_before_v2507,
    run_formula_lab_advanced_self_tests, CombinatorialSymmetryReport, _face_set_index,
    _vertex_initial_colors_for_automorphism, _refine_vertex_colors, _is_face_preserving_perm,
    _automorphisms_combinatorial, _edge_orbits_from_vertex_perms, _face_orbits_from_vertex_perms,
    combinatorial_symmetry_report, _local_face_regular_hint, classify_polyhedron_advanced,
    symmetry_comparison_report_text, advanced_symmetry_payload, canonical_lab_advanced,
    _plot_poly_on_ax, _full_report_before_v2508, GeoPolyAppV2508, _run_self_tests_before_v2508,
    run_symmetry_canonical_advanced_self_tests, _off_clean_lines, read_off_file, write_off_file,
    off_antiprism_report, current_poly_off_summary, GeoPolyAppV2509, _run_self_tests_before_v2509,
    run_off_antiprism_self_tests, _edge_direction_in_face_v25011,
    _consistent_face_orientation_v25011, _poly_components_by_faces_v25011,
    orient_polyhedron_faces_consistently, _CATALOGITEM_BUILD_BEFORE_V25011,
    _catalogitem_build_v25011, _POLY_VALIDATE_BEFORE_V25011, _poly_validate_v25011,
    _halfedge_dual_adjacency_v25011, _halfedge_is_closed_v25011, _halfedge_is_manifold_v25011,
    _halfedge_components_v25011, _halfedge_genus_hint_v25011,
    run_toroidal_orientation_genus_self_tests_v25011, _run_self_tests_before_v25011,
    JOHNSON_REQUIRE_FORMAL_BY_DEFAULT, JOHNSON_EMERGENCY_FALLBACK_ENV,
    johnson_emergency_fallback_enabled, johnson_policy_report, _catalog_item_build_v251,
    require_all_johnson_formal_or_raise_v251, _run_self_tests_before_v251,
    _show_johnson_audit_before_v251, _show_johnson_audit_v251, EDITION_V252, CertifiedTabRecord,
    CertifiedNetCertificate, NestedComponent, NestedPagePlacement, NestingResult, _v252_page_dims,
    _v252_bbox_pts, _v252_net_face_dict, _v252_face_vertex_map, _v252_same_point,
    _v252_is_folded_edge, _v252_tab_polygon_for_face, certified_glue_tabs,
    _legacy_verify_constructible_net_v2520, _v252_face_adjacency_order, generate_guided_tree_net,
    search_certified_net, _v252_component_from_sheet, _v252_bottom_left_pack,
    _legacy_solve_certified_nesting_v2520, _legacy_certified_net_report_v2520,
    _legacy_certified_net_payload_v2520, _v252_transform_poly,
    _legacy_export_certified_layout_pdf_v2520, _legacy_export_certified_layout_svg_v2520,
    _full_report_before_v252, GeoPolyAppV252, _v252_catalog_poly, _run_self_tests_before_v252,
    random, time, EDITION_V2521, robust_bbox_overlap, robust_point_in_poly_strict,
    _legacy_robust_polygon_overlap_area_v2520, robust_polygon_overlap_area,
    _legacy_verify_constructible_net_v2521_pre_final, _legacy_certified_net_report_v2521,
    _legacy_certified_net_payload_v2521, _build_certified_net_tab_before_v2521,
    _build_certified_net_tab_v2521, GeoPolyAppV2521, _run_self_tests_before_v2521,
    _robust_has_proper_segment_crossing, detect_face_overlaps_for_poly, verify_constructible_net,
    tolerant_orient2d_value, tolerant_point_on_segment,
    _legacy_robust_polygon_overlap_area_v2521_pre_final, robust_area_segment_intersect,
    EDITION_V2522, _v2522_orientations_for_page, _v2522_fit_factor_for_component,
    _v2522_best_page_orientation_for_components, _v2522_choose_rect_orientation,
    _v2522_bottom_left_pack, _v2522_make_components_from_cert,
    _legacy_solve_certified_nesting_v2522_autoscale, _legacy_certified_net_report_v2522,
    _legacy_certified_net_payload_v2522, _full_report_before_v2522, GeoPolyAppV2522,
    _run_self_tests_before_v2522, _v2523_polygon_area, _v2523_component_material_area_mm2,
    _v2523_component_dims_for_rotation, _v2523_choose_page_orientation_for_tiling,
    _legacy_v2523_make_tiled_windows_for_component, _v2523_make_tiled_windows_for_component,
    _v2523_component_to_page_polys, _legacy_solve_certified_nesting_v2523_fixed_tile,
    _legacy_certified_net_report_v2523, _legacy_certified_net_payload_v2523,
    _v2523_draw_register_marks, export_certified_layout_pdf, export_certified_layout_svg,
    _full_report_before_v2523, GeoPolyAppV2523, _run_self_tests_before_v2523, EDITION_V2524,
    _v2524_copy_component_rotated, _v2524_component_material_area_mm2, _v2524_rects_overlap,
    _v2524_pack_rectangles_candidate, _v2524_pack_components_best, _v2524_tile_plan_for_component,
    _v2524_choose_tiled_layout, _v2524_make_tiled_windows_for_component,
    _v2524_face_records_by_index, _v2524_group_boundary_tabs, _v2524_component_from_face_group,
    _v2524_groups_fit, _v2524_make_whole_face_components, _v2524_page_utilization_from_placements,
    _solve_certified_nesting_before_v2524, solve_certified_nesting,
    _certified_net_report_before_v2524, certified_net_report, _certified_net_payload_before_v2524,
    certified_net_payload, GeoPolyAppV2524, _full_report_before_v2524,
    _run_self_tests_before_v2524, BatchNetJob, BatchPiece, BatchPiecePlacement,
    BatchOptimizationResult, _v2525_page_setup, _v2525_poly_area_mm2,
    _v2525_component_material_area, _v2525_catalog_item_keys, _v2525_build_poly_from_key,
    _v2525_default_platonic_jobs, _v2525_piece_from_component, _v2525_piece_from_tile,
    _v2525_make_pieces_for_job, _v2525_rects_overlap, _v2525_pack_pieces_first_fit,
    solve_batch_material_optimizer, batch_optimizer_payload, batch_optimizer_report,
    _v2525_draw_piece_on_axis, export_batch_optimizer_pdf, export_batch_optimizer_json,
    _full_report_before_v2525, export_batch_optimizer_report_txt, GeoPolyAppV2525,
    _run_self_tests_before_v2525, EDITION_V25252, _v25252_file_ok, _v25252_current_backend_name,
    run_export_smoke_tests_v25252, export_smoke_test_report_v25252, _run_self_tests_before_v25252,
    EDITION_V25253, _v25253_text_startswith, _v25253_text_contains, _v25253_zip_contains,
    _v25253_binary_stl_ok, run_export_smoke_tests_v25253, export_smoke_test_report_v25253,
    _run_self_tests_before_v25253,
)

# v27.3: no persistent runtime compatibility rebinds.
#
# Historical self-test wrappers are still part of the validated regression suite.
# A few early wrappers resolve selected names through their original module
# globals. Instead of rebinding those modules at import time, v27.3 applies a
# narrow temporary compatibility context only while running the legacy self-test
# chain. This keeps normal runtime imports explicit and side-effect free, while
# preserving the 1167-test validated reference behavior.
from contextlib import contextmanager
from .internal import core_geometry_catalog as _core
from .internal import johnson_toroidal_certified as _johnson
from .internal import export_smoke_universal as _final

_run_self_tests_validated_reference = run_self_tests

_SELFTEST_COMPATIBILITY_BINDINGS = {
    _core: {
        'formula_lab_compute': _final.formula_lab_compute,
        'formula_lab_text': _final.formula_lab_text,
        'formula_lab_plot': _final.formula_lab_plot,
        'detect_overlaps': _final.detect_overlaps,
        'full_report': _final.full_report,
        'run_v24_sota_self_tests': _final.run_v24_sota_self_tests,
    },
    _johnson: {
        'verify_constructible_net': _final.verify_constructible_net,
        'robust_polygon_overlap_area': _final.robust_polygon_overlap_area,
        'robust_point_in_poly_strict': _final.robust_point_in_poly_strict,
        '_robust_has_proper_segment_crossing': _final._robust_has_proper_segment_crossing,
        'solve_certified_nesting': _final.solve_certified_nesting,
        'certified_net_payload': _final.certified_net_payload,
        'certified_net_report': _final.certified_net_report,
        'export_certified_layout_pdf': _final.export_certified_layout_pdf,
        'export_certified_layout_svg': _final.export_certified_layout_svg,
    },
}

@contextmanager
def _temporary_selftest_compatibility():
    previous = []
    try:
        for module, mapping in _SELFTEST_COMPATIBILITY_BINDINGS.items():
            for name, value in mapping.items():
                sentinel = object()
                previous.append((module, name, getattr(module, name, sentinel), sentinel))
                setattr(module, name, value)
        yield
    finally:
        for module, name, old_value, sentinel in reversed(previous):
            if old_value is sentinel:
                try:
                    delattr(module, name)
                except AttributeError:
                    pass
            else:
                setattr(module, name, old_value)

def run_self_tests():
    """Run the full validated regression suite without persistent runtime rebinds."""
    with _temporary_selftest_compatibility():
        return _run_self_tests_validated_reference()

APP_NAME = 'GeoPoly'
VERSION = '27.3'
EDITION = 'JOSS-ready Architecture Release'

# v27.1a public compatibility aliases restored from v26.x API
run_export_smoke_tests = run_export_smoke_tests_v25253
export_smoke_test_report = export_smoke_test_report_v25253

def version_info():
    return {
        'app': APP_NAME,
        'version': VERSION,
        'edition': EDITION,
        'implementation': 'JOSS-ready modular architecture: explicit public imports and explicit internal imports, no internal globals.update/import-star chain, consolidated net-certification/nesting/batch stacks, class-native behavior, no persistent runtime re-merge, universal export smoke coverage, and temporary self-test compatibility only while executing historical regression wrappers',
        'validated_reference': 'v25.2.5.3 universal export smoke coverage',
    }
