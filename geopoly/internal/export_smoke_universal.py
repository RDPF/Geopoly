"""GeoPoly v27 internal module: Universal export smoke coverage and final entry point."""
# v27.2f: named internal dependency import.
# Wildcard imports were removed to improve static analysis.
# v27.2f: named internal dependency imports; no wildcard imports.
from .batch_optimizer import (
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
)

# ============================================================
# v25.2.5.3 — Universal Export Smoke Coverage
# ============================================================
# Camada de robustez universal. Preserva todos os recursos/menus anteriores e
# amplia os smoke tests headless para cobrir os principais caminhos de saída:
# net verificada, lote, multi-folha, PDF paginado, SVG simples, malhas
# STL/OBJ/OFF/3MF e kit wireframe ZIP/pasta.

EDITION_V25253 = 'Universal Export Smoke Coverage'


def _v25253_text_startswith(path, prefix):
    try:
        return Path(path).read_text(encoding='utf-8', errors='ignore').lstrip().startswith(prefix)
    except Exception:
        return False


def _v25253_text_contains(path, *needles):
    try:
        txt = Path(path).read_text(encoding='utf-8', errors='ignore')
        return all(n in txt for n in needles)
    except Exception:
        return False


def _v25253_zip_contains(path, *members):
    try:
        if not zipfile.is_zipfile(path):
            return False
        with zipfile.ZipFile(path) as z:
            names = set(z.namelist())
            return all(any(m in n for n in names) for m in members)
    except Exception:
        return False


def _v25253_binary_stl_ok(path):
    try:
        p = Path(path)
        if not p.exists() or p.stat().st_size < 84:
            return False
        data = p.read_bytes()
        if len(data) < 84:
            return False
        tri_count = struct.unpack('<I', data[80:84])[0]
        return len(data) == 84 + 50 * tri_count and tri_count > 0
    except Exception:
        return False


def run_export_smoke_tests_v25253():
    """Smoke tests universais de exportação em modo headless/CLI.

    O objetivo não é validar toda a geometria, mas fechar a classe de regressões
    em caminhos de saída: backend errado, import ausente, arquivo vazio ou
    formato ilegível. Todos os artefatos são criados em diretório temporário.
    """
    import tempfile, os, json as _json
    out = {
        'version': '25.2.5.3',
        'backend': _v25252_current_backend_name(),
        'headless_expected_agg': (not os.environ.get('DISPLAY') and not os.environ.get('WAYLAND_DISPLAY')),
        'checks': [],
    }
    def add(name, path=None, min_bytes=256, ok=None, detail=''):
        if ok is None:
            ok = _v25252_file_ok(path, min_bytes)
        size = None
        if path:
            try:
                size = Path(path).stat().st_size
            except Exception:
                size = None
        out['checks'].append({
            'name': name,
            'ok': bool(ok),
            'path': str(path) if path else '',
            'size_bytes': size,
            'min_bytes': int(min_bytes),
            'detail': str(detail),
        })

    with tempfile.TemporaryDirectory() as td0:
        td = Path(td0)
        try:
            poly = _v252_catalog_poly('Platônicos / Cubo')
        except Exception:
            poly = build_cube()

        # Artefatos de net de base compartilhados por alguns exportadores.
        try:
            net = search_best_net(poly)
        except Exception:
            net = None
        try:
            cert = search_certified_net(poly, attempts=60, page='A4', scale_mm=30.0, margin_mm=10.0, tab_frac=0.18, max_seconds=6.0)
            nest = solve_certified_nesting(poly, cert, page='A4', scale_mm=30.0, margin_mm=10.0, allow_rotate=True, attempts=60, page_policy='auto')
        except Exception as exc:
            cert = nest = None
            add('preparação da net verificada', ok=False, detail=repr(exc))

        # 1-2. PDF/SVG da net verificada.
        try:
            if cert is None or nest is None:
                raise RuntimeError('cert/nest indisponíveis')
            pdf = td / 'certified_net_universal.pdf'
            svg = td / 'certified_net_universal.svg'
            export_certified_layout_pdf(poly, cert, nest, pdf, 'Universal smoke — net verificada')
            export_certified_layout_svg(poly, cert, nest, svg, 'Universal smoke — net verificada')
            add('PDF da net verificada', pdf, 1000)
            add('SVG da net verificada', svg, 500, ok=_v25252_file_ok(svg, 500) and _v25253_text_contains(svg, '<svg'))
        except Exception as exc:
            add('PDF/SVG da net verificada sem exceção', ok=False, detail=repr(exc))

        # 3-5. PDF/JSON/TXT do lote.
        try:
            jobs = [
                BatchNetJob(1, 'Platônicos / Tetraedro', 'Tetraedro', 30.0, 1, 'fixed_tile'),
                BatchNetJob(2, 'Platônicos / Cubo', 'Cubo', 30.0, 1, 'fixed_tile'),
                BatchNetJob(3, 'Platônicos / Octaedro', 'Octaedro', 30.0, 1, 'fixed_tile'),
            ]
            res = solve_batch_material_optimizer(jobs, page='A4', margin_mm=10.0, attempts=80, allow_rotate=True)
            pdf = td / 'batch_optimizer_universal.pdf'
            jsn = td / 'batch_optimizer_universal.json'
            txt = td / 'batch_optimizer_universal.txt'
            export_batch_optimizer_pdf(res, pdf, 'Universal smoke — lote')
            export_batch_optimizer_json(res, jsn)
            txt.write_text(batch_optimizer_report(res), encoding='utf-8')
            add('PDF do lote', pdf, 1000)
            add('JSON do lote', jsn, 500)
            add('TXT/relatório do lote', txt, 500)
            try:
                _json.loads(jsn.read_text(encoding='utf-8'))
                add('JSON do lote parseável', ok=True)
            except Exception as exc:
                add('JSON do lote parseável', ok=False, detail=repr(exc))
        except Exception as exc:
            add('PDF/JSON/TXT do lote sem exceção', ok=False, detail=repr(exc))

        # 6. PDF/SVG/PNG multifolha.
        try:
            if net is None:
                raise RuntimeError('net indisponível')
            ms = solve_multi_sheet(poly, net, page='A4', scale_mm=30.0, margin_mm=10.0)
            base = td / 'multisheet_universal'
            export_multi_sheet_pdf_png_svg(ms, base, 'Universal smoke — multifolha')
            pdf = base.with_suffix('.pdf')
            svgs = sorted(td.glob('multisheet_universal_sheet_*.svg'))
            pngs = sorted(td.glob('multisheet_universal_sheet_*.png'))
            add('PDF multifolha', pdf, 1000)
            add('SVG multifolha', svgs[0] if svgs else None, 300, ok=bool(svgs) and _v25252_file_ok(svgs[0], 300) and _v25253_text_contains(svgs[0], '<svg'))
            add('PNG multifolha', pngs[0] if pngs else None, 1000, ok=bool(pngs) and _v25252_file_ok(pngs[0], 1000))
        except Exception as exc:
            add('PDF/SVG/PNG multifolha sem exceção', ok=False, detail=repr(exc))

        # 7. PDF paginado antigo.
        try:
            if net is None:
                raise RuntimeError('net indisponível')
            pdf = td / 'paginated_old_universal.pdf'
            _gp2505_export_paginated_pdf(poly, net, pdf, scale_mm=30.0, page_name='A4', margin_mm=10.0, title='Universal smoke — PDF paginado')
            add('PDF paginado antigo', pdf, 1000)
        except Exception as exc:
            add('PDF paginado antigo sem exceção', ok=False, detail=repr(exc))

        # 8. SVG simples da planificação.
        try:
            if net is None:
                raise RuntimeError('net indisponível')
            svg = td / 'simple_net_universal.svg'
            write_svg_net(net, svg, 'Universal smoke — SVG simples')
            add('SVG simples da planificação', svg, 300, ok=_v25252_file_ok(svg, 300) and _v25253_text_contains(svg, '<svg', '<polygon'))
        except Exception as exc:
            add('SVG simples da planificação sem exceção', ok=False, detail=repr(exc))

        # 9-13. Escritores de malha.
        try:
            stla = td / 'mesh_ascii_universal.stl'
            stlb = td / 'mesh_binary_universal.stl'
            obj = td / 'mesh_universal.obj'
            off = td / 'mesh_universal.off'
            threemf = td / 'mesh_universal.3mf'
            write_stl_ascii(poly, stla, 20.0)
            write_stl_binary(poly, stlb, 20.0)
            write_obj(poly, obj, 20.0)
            write_off_file(poly, off, 20.0)
            write_3mf_basic(poly, threemf, 20.0)
            add('STL ASCII', stla, 500, ok=_v25252_file_ok(stla, 500) and _v25253_text_startswith(stla, 'solid'))
            add('STL binário', stlb, 84, ok=_v25253_binary_stl_ok(stlb))
            add('OBJ', obj, 300, ok=_v25252_file_ok(obj, 300) and _v25253_text_contains(obj, '\nv ', '\nf '))
            add('OFF', off, 100, ok=_v25252_file_ok(off, 100) and _v25253_text_startswith(off, 'OFF'))
            add('3MF básico', threemf, 500, ok=_v25252_file_ok(threemf, 500) and _v25253_zip_contains(threemf, '3D/3dmodel.model', '[Content_Types].xml'))
        except Exception as exc:
            add('escritores STL/OBJ/OFF/3MF sem exceção', ok=False, detail=repr(exc))

        # 14-15. Kit wireframe ZIP e pasta de peças.
        try:
            params = WireframeParams(edge_scale_mm=25.0, cyl_segments=12, sphere_segments=8)
            zpath = td / 'wireframe_kit_universal.zip'
            export_wireframe_kit_zip(poly, params, zpath)
            add('ZIP do kit wireframe', zpath, 1000, ok=_v25252_file_ok(zpath, 1000) and zipfile.is_zipfile(zpath) and _v25253_zip_contains(zpath, 'manifesto_wireframe', 'relatorio_montagem'))
            folder = td / 'wireframe_parts_folder'
            files = export_wireframe_parts_folder(poly, params, folder)
            existing = [Path(f) for f in files if Path(f).exists()]
            stls = [p for p in existing if p.suffix.lower() == '.stl']
            manifests = [p for p in existing if p.suffix.lower() == '.json']
            reports = [p for p in existing if p.suffix.lower() == '.txt']
            ok = bool(stls) and bool(manifests) and bool(reports) and all(p.stat().st_size > 100 for p in existing)
            add('pasta de peças wireframe', folder, 0, ok=ok, detail=f'{len(existing)} arquivo(s), {len(stls)} STL')
        except Exception as exc:
            add('wireframe ZIP/pasta sem exceção', ok=False, detail=repr(exc))

        # 16. Backend Agg garantido em CLI/headless.
        backend = _v25252_current_backend_name().lower()
        if out['headless_expected_agg']:
            add('backend Agg em ambiente headless', ok=('agg' in backend), detail=_v25252_current_backend_name())
        else:
            add('backend Matplotlib disponível', ok=(backend != 'unknown'), detail=_v25252_current_backend_name())

    out['passed'] = sum(1 for c in out['checks'] if c['ok'])
    out['total'] = len(out['checks'])
    out['ok'] = (out['passed'] == out['total'])
    return out


def export_smoke_test_report_v25253(smoke=None):
    smoke = smoke or run_export_smoke_tests_v25253()
    lines = []
    lines.append('GeoPoly v25.2.5.3 — Universal Export Smoke Coverage')
    lines.append(f'Backend Matplotlib: {smoke.get("backend", "unknown")}')
    lines.append(f'Resultado: {smoke.get("passed", 0)}/{smoke.get("total", 0)} smoke tests OK')
    lines.append('')
    for c in smoke.get('checks', []):
        mark = 'OK' if c.get('ok') else 'FALHA'
        size = c.get('size_bytes')
        size_s = 'n/a' if size is None else f'{size} bytes'
        lines.append(f'[{mark}] {c.get("name", "")}: {size_s}')
        if c.get('detail') and (not c.get('ok')):
            lines.append(f'      detalhe: {c.get("detail")}')
    return '\n'.join(lines)


_run_self_tests_before_v25253 = run_self_tests

def run_self_tests():
    rep = _run_self_tests_before_v25253()
    results = list(rep.results)
    def add(name, ok, detail=''):
        results.append(TestCaseResult('v25.2.5.3 / ' + name, bool(ok), '' if ok else str(detail)))
    try:
        smoke = run_export_smoke_tests_v25253()
        report = export_smoke_test_report_v25253(smoke)
        required = [
            'PDF da net verificada', 'SVG da net verificada', 'PDF do lote',
            'JSON do lote', 'TXT/relatório do lote', 'PDF multifolha',
            'SVG multifolha', 'PNG multifolha', 'PDF paginado antigo',
            'SVG simples da planificação', 'STL ASCII', 'STL binário', 'OBJ',
            'OFF', '3MF básico', 'ZIP do kit wireframe', 'pasta de peças wireframe'
        ]
        add('smoke tests universais executam', smoke['total'] >= len(required), report)
        for name in required:
            add(name + ' exporta', any(c['name'] == name and c['ok'] for c in smoke['checks']), report)
        add('todos os caminhos universais exportam sem erro', smoke.get('ok', False), report)
        backend = _v25252_current_backend_name().lower()
        if not os.environ.get('DISPLAY') and not os.environ.get('WAYLAND_DISPLAY'):
            add('backend Agg garantido em headless', 'agg' in backend, _v25252_current_backend_name())
        else:
            add('backend gráfico/headless selecionado sem erro', backend != 'unknown', _v25252_current_backend_name())
        add('relatório universal de smoke tests disponível', 'Universal Export Smoke Coverage' in report, report)
    except Exception as exc:
        add('suíte v25.2.5.3 sem exceção', False, repr(exc))
    return TestReport(results)


APP_NAME='GeoPoly'
VERSION='25.2.5.3'
EDITION='Universal Export Smoke Coverage + Batch Material Optimizer + Headless Export Fix + Embedded Johnson Formal Bundle'


def main():
    GeoPolyAppV2525().mainloop()



# v27.2f: explicit export list so internal star imports preserve historical
# single-underscore helper symbols without using wholesale update calls.
__all__ = [k for k in globals() if not k.startswith('__')]
