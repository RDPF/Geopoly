"""GeoPoly v27 internal module: Fixed-scale tiled nesting and material layout policies."""
# v27.2f: named internal dependency import.
# Wildcard imports were removed to improve static analysis.
# v27.2f: named internal dependency imports; no wildcard imports.
from .johnson_toroidal_certified import (
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
    _run_self_tests_before_v2522,
)


# ============================================================
# v25.2.3 — Fixed-Scale Tiled Nesting
# ============================================================
# Esta versão preserva todas as funcionalidades/menus anteriores e corrige o
# último ponto de acabamento do nesting: quando a rede não cabe na página na
# escala solicitada, o usuário pode preservar a escala e ladrilhar a rede em
# múltiplas páginas com janelas físicas, marcas de registro e payload JSON.
#
# Políticas de página:
# - fixed_tile: preserva a escala solicitada e divide em páginas quando necessário;
# - autoscale: reduz a escala para caber em uma página, como na v25.2.2;
# - auto: tenta caber na escala solicitada; se não couber, ladrilha preservando a escala.

VERSION='25.2.3'
EDITION='Fixed-Scale Tiled Nesting + Embedded Johnson Formal Bundle'


def _v2523_polygon_area(poly2d):
    P=np.asarray(poly2d,dtype=float)
    if len(P)<3: return 0.0
    s=0.0
    for i in range(len(P)):
        x1,y1=P[i]; x2,y2=P[(i+1)%len(P)]
        s += x1*y2-x2*y1
    return abs(0.5*s)


def _v2523_component_material_area_mm2(comp, scale_mm):
    area=0.0
    for P in comp.polygons:
        area += _v2523_polygon_area(P)*(scale_mm**2)
    for T in comp.tabs:
        area += _v2523_polygon_area(T)*(scale_mm**2)
    return float(area)


def _v2523_component_dims_for_rotation(comp, rotation):
    if int(rotation)%180==90:
        return float(comp.height_mm), float(comp.width_mm)
    return float(comp.width_mm), float(comp.height_mm)


def _v2523_choose_page_orientation_for_tiling(page='A4', margin_mm=10.0, components=None, allow_rotate=True):
    """Escolhe retrato/paisagem para minimizar páginas de ladrilhamento.

    A orientação da página é diferente de rotação do componente. Para o modo
    tiled, preferimos uma orientação de página que reduza a grade total de
    janelas necessárias.
    """
    base=_v252_page_dims(page)
    candidates=[('portrait',base)]
    if allow_rotate:
        candidates.append(('landscape',(base[1],base[0])))
    components=components or []
    best=None
    for name,dims in candidates:
        usable=(max(1.0,dims[0]-2*margin_mm), max(1.0,dims[1]-2*margin_mm))
        pages=0; waste=0.0
        for comp in components:
            nx=max(1,int(math.ceil(comp.width_mm/usable[0]-1e-12)))
            ny=max(1,int(math.ceil(comp.height_mm/usable[1]-1e-12)))
            pages += nx*ny
            waste += nx*ny*usable[0]*usable[1] - min(comp.width_mm, nx*usable[0])*min(comp.height_mm, ny*usable[1])
        score=(pages,waste, -usable[0]*usable[1])
        if best is None or score<best[0]:
            best=(score,name,dims,usable)
    _,name,dims,usable=best
    return str(name),(float(dims[0]),float(dims[1])),(float(usable[0]),float(usable[1]))


def _legacy_v2523_make_tiled_windows_for_component(comp, usable_w, usable_h, start_page=1, overlap_mm=0.0):
    """Cria janelas de página em coordenadas locais do componente, em mm.

    As janelas cobrem o retângulo envolvente do componente na escala aplicada.
    O overlap é reservado para marca de registro/colagem visual entre páginas;
    por padrão fica zero para não alterar a métrica de aproveitamento.
    """
    windows=[]
    step_x=max(1.0, usable_w-float(overlap_mm))
    step_y=max(1.0, usable_h-float(overlap_mm))
    nx=max(1,int(math.ceil(comp.width_mm/step_x-1e-12)))
    ny=max(1,int(math.ceil(comp.height_mm/step_y-1e-12)))
    pg=int(start_page)
    for iy in range(ny):
        for ix in range(nx):
            x0=ix*step_x; y0=iy*step_y
            x1=min(x0+usable_w, comp.width_mm); y1=min(y0+usable_h, comp.height_mm)
            windows.append({
                'page':int(pg), 'component_index':int(comp.component_index),
                'tile_x':int(ix+1), 'tile_y':int(iy+1),
                'tiles_x':int(nx), 'tiles_y':int(ny),
                'window_x0_mm':float(x0), 'window_y0_mm':float(y0),
                'window_x1_mm':float(x1), 'window_y1_mm':float(y1),
                'window_width_mm':float(max(0.0,x1-x0)),
                'window_height_mm':float(max(0.0,y1-y0)),
            })
            pg += 1
    return windows, pg


_v2523_make_tiled_windows_for_component = _legacy_v2523_make_tiled_windows_for_component  # public compatibility alias; legacy implementation retained, no active override

def _v2523_component_to_page_polys(comp, scale_mm, margin_mm, window=None):
    """Converte polígonos de um componente para coordenadas físicas de página.

    Se window for None, posiciona o componente inteiro na origem útil (para
    exportações não-tiled). Se houver window, desloca pela janela de ladrilhamento;
    o clipping é feito pelos limites do eixo/PDF ou por clipPath no SVG.
    """
    x0,y0,x1,y1=comp.bbox
    dx=0.0 if window is None else float(window.get('window_x0_mm',0.0))
    dy=0.0 if window is None else float(window.get('window_y0_mm',0.0))
    out_faces=[]; out_tabs=[]
    for P in comp.polygons:
        Q=(np.asarray(P,dtype=float)-np.array([x0,y0]))*scale_mm
        Q=Q-np.array([dx,dy])+np.array([margin_mm,margin_mm])
        out_faces.append(Q)
    for T in comp.tabs:
        Q=(np.asarray(T,dtype=float)-np.array([x0,y0]))*scale_mm
        Q=Q-np.array([dx,dy])+np.array([margin_mm,margin_mm])
        out_tabs.append(Q)
    return out_faces,out_tabs


def _legacy_solve_certified_nesting_v2523_fixed_tile(poly, cert=None, page='A4', scale_mm=50.0, margin_mm=10.0,
                            allow_rotate=True, tab_frac=0.22, tab_shape='trapezoidal',
                            attempts=300, auto_scale=True, min_scale_mm=5.0,
                            page_policy='auto', tile_overlap_mm=0.0):
    """Nesting v25.2.3 com política de página.

    page_policy:
      - 'fixed_tile': preserva escala e ladrilha em múltiplas páginas quando necessário;
      - 'autoscale': reduz escala para caber em uma página, como v25.2.2;
      - 'auto': usa uma página se couber; se não couber, ladrilha preservando escala.

    Compatibilidade: chamadas antigas com auto_scale=True/False continuam aceitas.
    Se page_policy não for informado explicitamente, auto_scale=True mantém o modo
    de autoescala da versão anterior; a UI nova usa page_policy='auto' por padrão.
    """
    cert=cert or search_certified_net(poly,attempts=attempts,page=page,scale_mm=scale_mm,margin_mm=margin_mm,tab_frac=tab_frac,tab_shape=tab_shape)
    requested_scale=float(scale_mm)
    policy=str(page_policy or ('autoscale' if auto_scale else 'fixed_tile')).lower()
    if policy in {'tile','fixed','fixed-scale','preserve','preservar'}:
        policy='fixed_tile'
    if policy in {'autoscale_1page','scale','auto_scale'}:
        policy='autoscale'
    if policy not in {'fixed_tile','autoscale','auto'}:
        policy='auto'

    # Componentes na escala solicitada.
    components=_v2522_make_components_from_cert(poly,cert,requested_scale)
    orient,page_dims,usable,minfit,suggested_rel=_v2522_best_page_orientation_for_components(page,components,float(margin_mm),allow_rotate)
    requested_components=components
    requested_usable=usable
    requested_orient=orient
    requested_page_dims=page_dims
    warnings=[]

    # Primeiro tenta empacotar na escala solicitada, sem invalidar métrica.
    placements_req,pages_req,all_fit_req,pack_warnings_req=_v2522_bottom_left_pack(components,usable[0],usable[1],gap=4.0,allow_rotate=allow_rotate)
    oversized=not all_fit_req

    # Política: auto tenta manter escala e ladrilhar se necessário.
    if policy=='autoscale' and oversized:
        suggested_scale=max(float(min_scale_mm), requested_scale*max(0.0,suggested_rel)*0.995)
        applied_scale=suggested_scale if suggested_scale < requested_scale else requested_scale
        scale_adjusted=applied_scale < requested_scale-1e-9
        warnings.append(f'Autoescala aplicada: {requested_scale:.3f} → {applied_scale:.3f} mm/unid. para caber na página útil.')
        components=_v2522_make_components_from_cert(poly,cert,applied_scale)
        orient,page_dims,usable,minfit,suggested_rel=_v2522_best_page_orientation_for_components(page,components,float(margin_mm),allow_rotate)
        placements,pages,all_fit,pack_warnings=_v2522_bottom_left_pack(components,usable[0],usable[1],gap=4.0,allow_rotate=allow_rotate)
        warnings.extend(pack_warnings)
        used_area=sum(_v2523_component_material_area_mm2(c,applied_scale) for c in components)
        util=min(100.0,max(0.0,100.0*used_area/(max(1,pages)*usable[0]*usable[1]))) if all_fit else None
        layout_status='fit_rescaled' if all_fit else 'component_too_large'
        res=NestingResult(str(page),(float(page_dims[0]),float(page_dims[1])),(float(usable[0]),float(usable[1])),float(margin_mm),float(applied_scale),components,placements,int(max(1,pages)),util,bool(all_fit),warnings)
        res.page_windows=[]; res.page_policy=policy; res.tiled=False
        res.requested_scale_mm=float(requested_scale); res.applied_scale_mm=float(applied_scale)
        res.scale_adjusted=bool(scale_adjusted); res.suggested_scale_mm=float(suggested_scale)
        res.page_orientation=str(orient); res.layout_status=str(layout_status); res.auto_scale=True
        return res

    # Se cabe na escala solicitada, usa o layout normal em uma ou mais páginas.
    if not oversized:
        applied_scale=requested_scale
        used_area=sum(_v2523_component_material_area_mm2(c,applied_scale) for c in components)
        util=min(100.0,max(0.0,100.0*used_area/(max(1,pages_req)*usable[0]*usable[1])))
        res=NestingResult(str(page),(float(page_dims[0]),float(page_dims[1])),(float(usable[0]),float(usable[1])),float(margin_mm),float(applied_scale),components,placements_req,int(max(1,pages_req)),util,True,list(pack_warnings_req))
        res.page_windows=[]; res.page_policy=policy; res.tiled=False
        res.requested_scale_mm=float(requested_scale); res.applied_scale_mm=float(applied_scale)
        res.scale_adjusted=False; res.suggested_scale_mm=float(requested_scale)
        res.page_orientation=str(orient); res.layout_status='fit_fixed_scale'; res.auto_scale=False
        return res

    # Modo fixed_tile/auto: preserva escala e divide o componente em janelas.
    # Escolhe orientação de página específica para reduzir o número total de tiles.
    orient,page_dims,usable=_v2523_choose_page_orientation_for_tiling(page,float(margin_mm),components,allow_rotate)
    page_windows=[]; placements=[]; next_page=1
    for comp in components:
        windows,next_page=_v2523_make_tiled_windows_for_component(comp,usable[0],usable[1],start_page=next_page,overlap_mm=tile_overlap_mm)
        for w in windows:
            page_windows.append(w)
            placements.append(NestedPagePlacement(int(w['page']),int(comp.component_index),0.0,0.0,0,int(w['window_width_mm']),int(w['window_height_mm'])))
    pages=max([w['page'] for w in page_windows],default=1)
    material_area=sum(_v2523_component_material_area_mm2(c,requested_scale) for c in components)
    util=min(100.0,max(0.0,100.0*material_area/(pages*usable[0]*usable[1]))) if pages>0 else None
    # No modo tiled, avisos antigos de 'não cabe' deixam de ser falha: a solução é ladrilhar.
    warnings.append('Escala fixa preservada; componente(s) maior(es) que a página foram ladrilhados em múltiplas páginas com marcas de registro.')
    suggested_scale=max(float(min_scale_mm), requested_scale*max(0.0,suggested_rel)*0.995)
    res=NestingResult(str(page),(float(page_dims[0]),float(page_dims[1])),(float(usable[0]),float(usable[1])),float(margin_mm),float(requested_scale),components,placements,int(max(1,pages)),util,True,warnings)
    res.page_windows=page_windows; res.page_policy=policy; res.tiled=True
    res.requested_scale_mm=float(requested_scale); res.applied_scale_mm=float(requested_scale)
    res.scale_adjusted=False; res.suggested_scale_mm=float(suggested_scale)
    res.page_orientation=str(orient); res.layout_status='fixed_scale_tiled'
    res.auto_scale=False; res.tile_overlap_mm=float(tile_overlap_mm)
    return res


def _legacy_certified_net_report_v2523(poly, cert, nesting=None):
    lines=[]
    lines.append('Certified Printable Net & Nesting Solver v25.2.3')
    lines.append('='*56)
    lines.append(f'Sólido: {poly.name}')
    lines.append(f'Estratégia: {cert.strategy}')
    lines.append(f'Tentativas: {cert.attempts}')
    lines.append(f'Status da rede: {cert.status}')
    lines.append(f'Rede de faces construível: {"sim" if cert.constructible else "não"}')
    lines.append(f'Faces: {len(cert.net.faces)}/{len(poly.faces)}')
    lines.append(f'Sobreposição de faces: {len(cert.face_overlaps)}')
    lines.append(f'Conflitos aba-face (aviso): {len(cert.tab_face_overlaps)}')
    lines.append(f'Conflitos aba-aba (aviso): {len(cert.tab_tab_overlaps)}')
    lines.append(f'Arestas de dobra estimadas: {cert.tree_fold_edges}')
    lines.append(f'Arestas de corte/contorno: {cert.cut_edges}')
    lines.append(f'Abas numeradas: {len(cert.tabs)}')
    lines.append(f'Score: {cert.score:.3f}')
    lines.append('')
    lines.append('Abas de colagem')
    lines.append('-'*18)
    for t in cert.tabs[:200]:
        if t.mate_face is None:
            lines.append(f'{t.glue_id}: face {t.face_index+1}, borda {t.edge}')
        else:
            lines.append(f'{t.glue_id}: face {t.face_index+1} cola na face {t.mate_face+1}, aresta {t.edge}')
    if len(cert.tabs)>200:
        lines.append(f'... {len(cert.tabs)-200} abas restantes')
    if nesting:
        lines += ['', 'Nesting em páginas', '-'*19]
        lines.append(f'Página: {nesting.page_name} {nesting.page_dims_mm[0]:.1f}×{nesting.page_dims_mm[1]:.1f} mm ({getattr(nesting,"page_orientation","n/d")})')
        lines.append(f'Área útil: {nesting.usable_dims_mm[0]:.1f}×{nesting.usable_dims_mm[1]:.1f} mm')
        lines.append(f'Política de página: {getattr(nesting,"page_policy","n/d")}')
        req=getattr(nesting,'requested_scale_mm',nesting.scale_mm)
        app=getattr(nesting,'applied_scale_mm',nesting.scale_mm)
        lines.append(f'Escala solicitada: {req:.3f} mm/unidade')
        lines.append(f'Escala aplicada: {app:.3f} mm/unidade')
        lines.append(f'Escala preservada: {"sim" if abs(req-app)<1e-9 else "não"}')
        if getattr(nesting,'scale_adjusted',False): lines.append('Autoescala: sim')
        else: lines.append('Autoescala: não aplicada')
        lines.append(f'Margem: {nesting.margin_mm:.1f} mm')
        lines.append(f'Componentes: {len(nesting.components)}')
        lines.append(f'Páginas: {nesting.page_count}')
        if getattr(nesting,'tiled',False):
            lines.append(f'Ladrilhamento multipágina: sim ({len(getattr(nesting,"page_windows",[]))} janelas)')
        else:
            lines.append('Ladrilhamento multipágina: não')
        if nesting.utilization_percent is None:
            lines.append('Aproveitamento estimado: n/a')
        else:
            lines.append(f'Aproveitamento estimado: {nesting.utilization_percent:.2f}%')
        lines.append(f'Todos cabem: {"sim" if nesting.all_fit else "não"}')
        lines.append(f'Status do layout: {getattr(nesting,"layout_status","n/d")}')
        if getattr(nesting,'page_windows',None):
            lines.append('Janelas de página:')
            for w in nesting.page_windows[:60]:
                lines.append(f'  página {w["page"]}: componente {w["component_index"]}, tile {w["tile_x"]}/{w["tiles_x"]} × {w["tile_y"]}/{w["tiles_y"]}, janela X={w["window_x0_mm"]:.1f}–{w["window_x1_mm"]:.1f} mm, Y={w["window_y0_mm"]:.1f}–{w["window_y1_mm"]:.1f} mm')
            if len(nesting.page_windows)>60: lines.append(f'  ... {len(nesting.page_windows)-60} janelas restantes')
        for w in nesting.warnings: lines.append('Aviso: '+w)
    lines.append('')
    lines.append('Critério: rede de faces verificada computacionalmente sem sobreposição de interiores. Abas são tratadas como qualidade/otimização, não como falha automática.')
    lines.append('Nota: a busca é heurística e não prova inexistência de rede melhor; a verificação usa predicados robustos/adaptativos com tolerância geométrica para a geometria exportada.')
    return '\n'.join(lines)


def _legacy_certified_net_payload_v2523(poly, cert, nesting=None):
    nest_payload=None
    if nesting is not None:
        nest_payload={
            'page':nesting.page_name,
            'page_dims_mm':list(nesting.page_dims_mm),
            'usable_dims_mm':list(nesting.usable_dims_mm),
            'margin_mm':float(nesting.margin_mm),
            'requested_scale_mm':float(getattr(nesting,'requested_scale_mm',nesting.scale_mm)),
            'applied_scale_mm':float(getattr(nesting,'applied_scale_mm',nesting.scale_mm)),
            'scale_adjusted':bool(getattr(nesting,'scale_adjusted',False)),
            'suggested_scale_mm':float(getattr(nesting,'suggested_scale_mm',nesting.scale_mm)),
            'page_orientation':str(getattr(nesting,'page_orientation','')),
            'layout_status':str(getattr(nesting,'layout_status','')),
            'page_policy':str(getattr(nesting,'page_policy','')),
            'tiled':bool(getattr(nesting,'tiled',False)),
            'tile_overlap_mm':float(getattr(nesting,'tile_overlap_mm',0.0)),
            'auto_scale':bool(getattr(nesting,'auto_scale',False)),
            'page_count':int(nesting.page_count),
            'utilization_percent':None if nesting.utilization_percent is None else float(nesting.utilization_percent),
            'all_fit':bool(nesting.all_fit),
            'warnings':list(nesting.warnings),
            'placements':[asdict(p) for p in nesting.placements],
            'page_windows':list(getattr(nesting,'page_windows',[])),
        }
    return {
        'version':'25.2.3', 'solid':poly.name, 'family':poly.family,
        'constructible':bool(cert.constructible), 'status':cert.status,
        'strategy':cert.strategy, 'attempts':int(cert.attempts),
        'certification_note':'Rede de faces verificada computacionalmente sob tolerância geométrica; busca heurística, não prova inexistência de outra rede melhor.',
        'face_overlaps':[list(map(int,p)) for p in cert.face_overlaps],
        'tab_face_overlaps':[list(map(int,p)) for p in cert.tab_face_overlaps],
        'tab_tab_overlaps':[list(map(int,p)) for p in cert.tab_tab_overlaps],
        'tree_fold_edges':int(cert.tree_fold_edges), 'cut_edges':int(cert.cut_edges),
        'tab_warning_count':int(len(cert.tab_face_overlaps)+len(cert.tab_tab_overlaps)),
        'tabs':[{'glue_id':int(t.glue_id),'face':int(t.face_index+1),'edge':[int(t.edge[0]),int(t.edge[1])],'mate_face':None if t.mate_face is None else int(t.mate_face+1),'note':str(t.note)} for t in cert.tabs],
        'nesting':nest_payload,
    }


def _v2523_draw_register_marks(ax, page_w, page_h, margin, label='', color='#444'):
    L=6.0
    pts=[(margin,margin),(page_w-margin,margin),(margin,page_h-margin),(page_w-margin,page_h-margin)]
    for x,y in pts:
        ax.plot([x-L/2,x+L/2],[y,y],color=color,linewidth=0.5)
        ax.plot([x,x],[y-L/2,y+L/2],color=color,linewidth=0.5)
    if label:
        ax.text(page_w/2, page_h-4, label, ha='center', va='top', fontsize=7, color=color)


def export_certified_layout_pdf(poly, cert, nesting, path, title=None):
    title=title or f'Rede verificada — {poly.name}'
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    page_w,page_h=nesting.page_dims_mm
    comp_by_id={c.component_index:c for c in nesting.components}
    with PdfPages(path) as pdf:
        fig,ax=plt.subplots(figsize=(page_w/25.4,page_h/25.4)); ax.axis('off')
        ax.text(0.05,0.95,certified_net_report(poly,cert,nesting),va='top',ha='left',family='monospace',fontsize=7,transform=ax.transAxes)
        pdf.savefig(fig); plt.close(fig)
        if getattr(nesting,'tiled',False) and getattr(nesting,'page_windows',None):
            windows=nesting.page_windows
            for w in windows:
                pg=int(w['page']); comp=comp_by_id[int(w['component_index'])]
                fig,ax=plt.subplots(figsize=(page_w/25.4,page_h/25.4))
                ax.set_xlim(0,page_w); ax.set_ylim(0,page_h); ax.set_aspect('equal'); ax.axis('off')
                ax.add_patch(MplPolygon(np.array([[nesting.margin_mm,nesting.margin_mm],[page_w-nesting.margin_mm,nesting.margin_mm],[page_w-nesting.margin_mm,page_h-nesting.margin_mm],[nesting.margin_mm,page_h-nesting.margin_mm]]),closed=True,fill=False,edgecolor='#888',linestyle=':',linewidth=0.8))
                face_polys,tab_polys=_v2523_component_to_page_polys(comp,nesting.scale_mm,nesting.margin_mm,w)
                for T in tab_polys:
                    ax.add_patch(MplPolygon(T,closed=True,facecolor='#fff2a8',edgecolor='#777',linestyle='--',linewidth=0.8,alpha=.85,clip_on=True))
                for k,P in enumerate(face_polys):
                    ax.add_patch(MplPolygon(P,closed=True,facecolor='#dfefff',edgecolor='#111',linewidth=0.9,alpha=.92,clip_on=True))
                    c=P.mean(axis=0); fid=comp.faces[k] if k < len(comp.faces) else k
                    if nesting.margin_mm-20 <= c[0] <= page_w-nesting.margin_mm+20 and nesting.margin_mm-20 <= c[1] <= page_h-nesting.margin_mm+20:
                        ax.text(c[0],c[1],str(fid+1),ha='center',va='center',fontsize=7,clip_on=True)
                _v2523_draw_register_marks(ax,page_w,page_h,nesting.margin_mm,label=f'página {pg}/{nesting.page_count} — tile {w["tile_x"]}/{w["tiles_x"]}, {w["tile_y"]}/{w["tiles_y"]}')
                ax.set_title(f'{title} — página {pg}/{nesting.page_count}',fontsize=9)
                pdf.savefig(fig); plt.close(fig)
        else:
            comp_by_id={c.component_index:c for c in nesting.components}
            for pg in range(1,nesting.page_count+1):
                fig,ax=plt.subplots(figsize=(page_w/25.4,page_h/25.4))
                ax.set_xlim(0,page_w); ax.set_ylim(0,page_h); ax.set_aspect('equal'); ax.axis('off')
                ax.add_patch(MplPolygon(np.array([[nesting.margin_mm,nesting.margin_mm],[page_w-nesting.margin_mm,nesting.margin_mm],[page_w-nesting.margin_mm,page_h-nesting.margin_mm],[nesting.margin_mm,page_h-nesting.margin_mm]]),closed=True,fill=False,edgecolor='#888',linestyle=':',linewidth=0.8))
                for pl in [p for p in nesting.placements if p.page==pg]:
                    comp=comp_by_id[pl.component_index]
                    face_polys=_v252_transform_poly(comp.polygons,comp,pl,nesting)
                    tab_polys=_v252_transform_poly(comp.tabs,comp,pl,nesting)
                    for T in tab_polys: ax.add_patch(MplPolygon(T,closed=True,facecolor='#fff2a8',edgecolor='#777',linestyle='--',linewidth=0.8,alpha=.85))
                    for k,P in enumerate(face_polys):
                        ax.add_patch(MplPolygon(P,closed=True,facecolor='#dfefff',edgecolor='#111',linewidth=0.9,alpha=.92))
                        c=P.mean(axis=0); fid=comp.faces[k] if k < len(comp.faces) else k
                        ax.text(c[0],c[1],str(fid+1),ha='center',va='center',fontsize=7)
                _v2523_draw_register_marks(ax,page_w,page_h,nesting.margin_mm,label=f'página {pg}/{nesting.page_count}')
                ax.set_title(f'{title} — página {pg}/{nesting.page_count}',fontsize=9)
                pdf.savefig(fig); plt.close(fig)


def export_certified_layout_svg(poly, cert, nesting, path, title=None):
    title=title or f'Rede verificada — {poly.name}'
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    page_w,page_h=nesting.page_dims_mm
    total_h=page_h*max(1,nesting.page_count)
    comp_by_id={c.component_index:c for c in nesting.components}
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{page_w:.2f}mm" height="{total_h:.2f}mm" viewBox="0 0 {page_w:.2f} {total_h:.2f}">',f'<title>{title}</title>','<rect width="100%" height="100%" fill="white"/>']
    def yflip(y,pg): return (pg-1)*page_h + (page_h-y)
    def polyline(points, fill, stroke, dash='', clip=''):
        return f'<polygon points="{points}" fill="{fill}" stroke="{stroke}" stroke-width="0.5" {dash} {clip}/>'
    if getattr(nesting,'tiled',False) and getattr(nesting,'page_windows',None):
        for w in nesting.page_windows:
            pg=int(w['page']); comp=comp_by_id[int(w['component_index'])]
            clip_id=f'clip_page_{pg}'
            lines.append(f'<clipPath id="{clip_id}"><rect x="{nesting.margin_mm:.2f}" y="{(pg-1)*page_h+nesting.margin_mm:.2f}" width="{nesting.usable_dims_mm[0]:.2f}" height="{nesting.usable_dims_mm[1]:.2f}"/></clipPath>')
            lines.append(f'<rect x="{nesting.margin_mm:.2f}" y="{(pg-1)*page_h+nesting.margin_mm:.2f}" width="{nesting.usable_dims_mm[0]:.2f}" height="{nesting.usable_dims_mm[1]:.2f}" fill="none" stroke="#888" stroke-dasharray="2 2" stroke-width="0.4"/>')
            face_polys,tab_polys=_v2523_component_to_page_polys(comp,nesting.scale_mm,nesting.margin_mm,w)
            for T in tab_polys:
                ps=' '.join(f'{x:.2f},{yflip(y,pg):.2f}' for x,y in T)
                lines.append(polyline(ps,'#fff2a8','#777','stroke-dasharray="2 1"',f'clip-path="url(#{clip_id})"'))
            for k,P in enumerate(face_polys):
                ps=' '.join(f'{x:.2f},{yflip(y,pg):.2f}' for x,y in P)
                lines.append(polyline(ps,'#dfefff','#111','',f'clip-path="url(#{clip_id})"'))
                c=P.mean(axis=0); fid=comp.faces[k] if k < len(comp.faces) else k
                if nesting.margin_mm-20 <= c[0] <= page_w-nesting.margin_mm+20 and nesting.margin_mm-20 <= c[1] <= page_h-nesting.margin_mm+20:
                    lines.append(f'<text x="{c[0]:.2f}" y="{yflip(c[1],pg):.2f}" font-size="4" text-anchor="middle" dominant-baseline="middle" clip-path="url(#{clip_id})">{fid+1}</text>')
            lines.append(f'<text x="{page_w/2:.2f}" y="{(pg-1)*page_h+6:.2f}" font-size="4" text-anchor="middle">página {pg}/{nesting.page_count} — tile {w["tile_x"]}/{w["tiles_x"]}, {w["tile_y"]}/{w["tiles_y"]}</text>')
    else:
        for pg in range(1,nesting.page_count+1):
            lines.append(f'<rect x="{nesting.margin_mm:.2f}" y="{(pg-1)*page_h+nesting.margin_mm:.2f}" width="{nesting.usable_dims_mm[0]:.2f}" height="{nesting.usable_dims_mm[1]:.2f}" fill="none" stroke="#888" stroke-dasharray="2 2" stroke-width="0.4"/>')
            for pl in [p for p in nesting.placements if p.page==pg]:
                comp=comp_by_id[pl.component_index]
                for T in _v252_transform_poly(comp.tabs,comp,pl,nesting):
                    ps=' '.join(f'{x:.2f},{yflip(y,pg):.2f}' for x,y in T); lines.append(polyline(ps,'#fff2a8','#777','stroke-dasharray="2 1"',''))
                for k,P in enumerate(_v252_transform_poly(comp.polygons,comp,pl,nesting)):
                    ps=' '.join(f'{x:.2f},{yflip(y,pg):.2f}' for x,y in P); lines.append(polyline(ps,'#dfefff','#111','',''))
                    c=P.mean(axis=0); fid=comp.faces[k] if k < len(comp.faces) else k
                    lines.append(f'<text x="{c[0]:.2f}" y="{yflip(c[1],pg):.2f}" font-size="4" text-anchor="middle" dominant-baseline="middle">{fid+1}</text>')
    lines.append('</svg>')
    path.write_text('\n'.join(lines),encoding='utf-8')


_full_report_before_v2523 = full_report

def full_report(poly,scale_mm=50.0,density_g_cm3=1.24,cost_per_kg=100.0):
    md,payload=_full_report_before_v2523(poly,scale_mm,density_g_cm3,cost_per_kg)
    try:
        cert=search_certified_net(poly,attempts=80,scale_mm=scale_mm,tab_frac=0.22)
        nesting=solve_certified_nesting(poly,cert,scale_mm=scale_mm,attempts=80,page_policy='auto')
        payload['certified_printable_net_v2523']=certified_net_payload(poly,cert,nesting)
        md += '\n\n## Rede imprimível verificada v25.2.3\n'
        md += f'- Rede de faces construível: {"sim" if cert.constructible else "não"}\n'
        md += f'- Sobreposições de faces: {len(cert.face_overlaps)}\n'
        md += f'- Conflitos aba-face: {len(cert.tab_face_overlaps)}\n'
        md += f'- Conflitos aba-aba: {len(cert.tab_tab_overlaps)}\n'
        md += f'- Política de página: {getattr(nesting,"page_policy","n/d")}\n'
        md += f'- Páginas estimadas: {nesting.page_count}\n'
        md += f'- Escala aplicada: {getattr(nesting,"applied_scale_mm",nesting.scale_mm):.3f} mm/unid.\n'
        md += f'- Ladrilhamento: {"sim" if getattr(nesting,"tiled",False) else "não"}\n'
        if nesting.utilization_percent is None: md += '- Aproveitamento estimado: n/a\n'
        else: md += f'- Aproveitamento estimado: {nesting.utilization_percent:.2f}%\n'
    except Exception as exc:
        payload['certified_printable_net_v2523_error']=str(exc)
        md += '\n\n## Rede imprimível verificada v25.2.3\n- Não foi possível gerar certificado automático: '+str(exc)+'\n'
    return md,payload


class GeoPolyAppV2523(GeoPolyAppV2522):
    """v25.2.3: mantém menus e adiciona política de página + ladrilhamento em escala fixa."""
    def _build_certified_net_tab(self):
        super()._build_certified_net_tab()
        try:
            self.cert_page_policy_var=tk.StringVar(value='Auto: preservar escala; ladrilhar se necessário')
            extra=ttk.LabelFrame(self.tabcert,text='v25.2.3 — política de página e ladrilhamento',padding=6)
            extra.grid(row=4,column=0,sticky='ew',pady=(6,0))
            ttk.Label(extra,text='Política:').pack(side='left',padx=(0,4))
            cb=ttk.Combobox(extra,textvariable=self.cert_page_policy_var,state='readonly',width=42,values=[
                'Auto: preservar escala; ladrilhar se necessário',
                'Preservar escala e ladrilhar',
                'Autoescala para caber em 1 página',
            ])
            cb.pack(side='left',padx=4)
            ttk.Label(extra,text='O modo ladrilhado preserva a escala e cria múltiplas páginas com marcas de registro.').pack(side='left',padx=8)
        except Exception:
            pass
    def _cert_page_policy_code(self):
        txt=str(getattr(self,'cert_page_policy_var',tk.StringVar(value='')).get()) if hasattr(self,'cert_page_policy_var') else ''
        if txt.startswith('Preservar'): return 'fixed_tile'
        if txt.startswith('Autoescala'): return 'autoscale'
        return 'auto'
    def update_certified_net_tab(self,auto=False):
        if not hasattr(self,'cert_text') or not self.poly: return
        if auto:
            attempts=min(80,int(self.cert_attempts_var.get()) if hasattr(self,'cert_attempts_var') else 80)
        else:
            attempts=int(self.cert_attempts_var.get())
        try:
            params=self._current_cert_params(); params['attempts']=attempts
            self.cert_result=search_certified_net(self.poly,**params)
            policy=self._cert_page_policy_code()
            # Compatibilidade visual: a checkbox de autoescala antiga continua existindo,
            # mas a nova combobox é a política principal.
            auto_scale=(policy=='autoscale')
            self.nesting_result=solve_certified_nesting(self.poly,self.cert_result,page=params['page'],scale_mm=params['scale_mm'],margin_mm=params['margin_mm'],allow_rotate=bool(self.cert_rotate_var.get()),tab_frac=params['tab_frac'],tab_shape=params['tab_shape'],attempts=attempts,auto_scale=auto_scale,page_policy=policy)
            self.cert_text.delete('1.0','end'); self.cert_text.insert('end',certified_net_report(self.poly,self.cert_result,self.nesting_result))
            self._draw_certified_preview()
        except Exception as exc:
            self.cert_text.delete('1.0','end'); self.cert_text.insert('end','Erro no solver certificado:\n'+str(exc))


_run_self_tests_before_v2523 = run_self_tests

def run_self_tests():
    rep=_run_self_tests_before_v2523(); results=list(rep.results)
    def add(name,ok,detail=''):
        results.append(TestCaseResult('v25.2.3 / '+name,bool(ok),'' if ok else str(detail)))
    try:
        dod=_v252_catalog_poly('Platônicos / Dodecaedro')
        cert=search_certified_net(dod,attempts=220,tab_frac=0.22,max_seconds=10.0)
        nest_tile=solve_certified_nesting(dod,cert,page='A4',scale_mm=50.0,margin_mm=10.0,page_policy='fixed_tile',auto_scale=False)
        add('dodecaedro 50 mm preserva escala', abs(getattr(nest_tile,'applied_scale_mm',0)-50.0)<1e-9 and not getattr(nest_tile,'scale_adjusted',True), certified_net_report(dod,cert,nest_tile))
        add('dodecaedro 50 mm ladrilhado cabe em páginas', nest_tile.all_fit and getattr(nest_tile,'tiled',False) and nest_tile.page_count>=2, certified_net_payload(dod,cert,nest_tile))
        add('dodecaedro 50 mm tem janelas JSON', len(getattr(nest_tile,'page_windows',[]))==nest_tile.page_count and isinstance(json.dumps(certified_net_payload(dod,cert,nest_tile),default=str),str), certified_net_payload(dod,cert,nest_tile))
        add('dodecaedro 50 mm aproveitamento válido', nest_tile.utilization_percent is not None and 0.0 <= nest_tile.utilization_percent <= 100.0, nest_tile.utilization_percent)
        nest_auto=solve_certified_nesting(dod,cert,page='A4',scale_mm=50.0,margin_mm=10.0,page_policy='autoscale',auto_scale=True)
        add('dodecaedro política autoescala ainda reduz para caber', nest_auto.all_fit and getattr(nest_auto,'scale_adjusted',False), certified_net_payload(dod,cert,nest_auto))
        ico=_v252_catalog_poly('Platônicos / Icosaedro')
        cert_i=search_certified_net(ico,attempts=220,tab_frac=0.22,max_seconds=10.0)
        nest_i=solve_certified_nesting(ico,cert_i,page='A4',scale_mm=50.0,margin_mm=10.0,page_policy='fixed_tile',auto_scale=False)
        add('icosaedro 50 mm fixed-tile preserva escala e serializa', abs(getattr(nest_i,'applied_scale_mm',0)-50.0)<1e-9 and isinstance(json.dumps(certified_net_payload(ico,cert_i,nest_i),default=str),str), certified_net_payload(ico,cert_i,nest_i))
    except Exception as exc:
        add('suíte v25.2.3 sem exceção', False, repr(exc))
    return TestReport(results)



# ============================================================
# v25.2.4 — Material-Efficient Layout & Headless Export Fix
# ============================================================
# Esta camada preserva todas as funcionalidades da v25.2.3 e acrescenta:
# - exportação headless mais segura via seleção automática de backend Matplotlib;
# - layout retangular mais eficiente por busca bottom-left com múltiplas páginas;
# - escolha de orientação da página e rotação da rede/componente para reduzir tiles;
# - aproveitamento por página/tile e global;
# - modo de impressão em escala fixa com faces inteiras por página;
# - rótulo técnico mais honesto: verificação computacional sob tolerância.

EDITION_V2524 = 'Material-Efficient Layout & Headless Export Fix'


def _v2524_copy_component_rotated(comp, rotation=0):
    """Retorna cópia geométrica do componente com rotação 0/90/180/270 e bbox normalizada.

    Importante: a normalização é global ao componente inteiro, não por polígono;
    isso preserva as distâncias relativas da rede e as dimensões físicas.
    """
    rot = int(rotation) % 360
    x0,y0,x1,y1 = comp.bbox
    old_w_units=max(EPS, float(x1-x0)); old_h_units=max(EPS, float(y1-y0))
    scale_x=float(comp.width_mm)/old_w_units if old_w_units>EPS else 1.0
    scale_y=float(comp.height_mm)/old_h_units if old_h_units>EPS else scale_x
    phys_scale=(scale_x+scale_y)/2.0

    def raw(P):
        Q=np.asarray(P,dtype=float)-np.array([x0,y0],dtype=float)
        if rot == 0:
            return Q.copy()
        if rot == 90:
            return np.column_stack([Q[:,1], -Q[:,0]])
        if rot == 180:
            return -Q
        if rot == 270:
            return np.column_stack([-Q[:,1], Q[:,0]])
        ang=math.radians(rot); c,s=math.cos(ang),math.sin(ang)
        M=np.array([[c,-s],[s,c]],dtype=float)
        return Q @ M.T

    raw_polys=[raw(P) for P in comp.polygons]
    raw_tabs=[raw(T) for T in comp.tabs]
    allpts=np.vstack(raw_polys+raw_tabs) if (raw_polys or raw_tabs) else np.zeros((1,2))
    mn=allpts.min(axis=0)
    polys=[P-mn for P in raw_polys]
    tabs=[T-mn for T in raw_tabs]
    bb=_v252_bbox_pts(polys+tabs) if (polys or tabs) else (0.0,0.0,0.0,0.0)
    w=max(0.0,(bb[2]-bb[0]))*phys_scale; h=max(0.0,(bb[3]-bb[1]))*phys_scale
    out=NestedComponent(int(comp.component_index), list(comp.faces), polys, tabs, bb, float(w), float(h))
    out.source_rotation_degrees=int(rot)
    out.source_component_index=int(comp.component_index)
    return out


def _v2524_component_material_area_mm2(comp, scale_mm):
    return _v2523_component_material_area_mm2(comp, float(scale_mm))


def _v2524_rects_overlap(a,b,eps=1e-9):
    ax,ay,aw,ah=a; bx,by,bw,bh=b
    return not (ax+aw <= bx+eps or bx+bw <= ax+eps or ay+ah <= by+eps or by+bh <= ay+eps)


def _v2524_pack_rectangles_candidate(components, usable_w, usable_h, gap=4.0, allow_rotate=True):
    """Empacotamento heurístico bottom-left por candidatos, melhor que shelf simples.

    Cada componente é aproximado por seu retângulo envolvente. A rotina tenta 0/90°
    para cada retângulo, coloca em páginas existentes quando possível e só abre nova
    página quando necessário. Retorna placements, páginas, fit e avisos.
    """
    comps=sorted(list(components), key=lambda c:(c.width_mm*c.height_mm, max(c.width_mm,c.height_mm)), reverse=True)
    pages=[]  # lista de retângulos ocupados por página: (x,y,w,h)
    placements=[]; warnings=[]; all_fit=True
    for comp in comps:
        dims=[(0,float(comp.width_mm),float(comp.height_mm))]
        if allow_rotate and abs(float(comp.width_mm)-float(comp.height_mm))>1e-9:
            dims.append((90,float(comp.height_mm),float(comp.width_mm)))
        # remove orientações impossíveis individualmente se houver alternativa que cabe
        fitting_dims=[d for d in dims if d[1] <= usable_w+1e-9 and d[2] <= usable_h+1e-9]
        if fitting_dims:
            dims=fitting_dims
        else:
            all_fit=False
            bestrel=max(min(usable_w/max(d[1],EPS), usable_h/max(d[2],EPS)) for d in dims)
            warnings.append(f'Componente {comp.component_index} excede a página útil nesta escala; razão relativa máxima {bestrel:.3f}.')
        best=None
        # tenta páginas existentes e uma página nova
        for pidx in range(len(pages)+1):
            occ = pages[pidx] if pidx < len(pages) else []
            candidates={(0.0,0.0)}
            for x,y,w,h in occ:
                candidates.add((x+w+gap,y)); candidates.add((x,y+h+gap))
            for rot,w,h in dims:
                for x,y in candidates:
                    if x < -1e-9 or y < -1e-9: continue
                    if x+w > usable_w+1e-9 or y+h > usable_h+1e-9: continue
                    rect=(x,y,w,h)
                    if any(_v2524_rects_overlap(rect, r) for r in occ):
                        continue
                    # menor página, menor y, menor x, menor área desperdiçada local
                    score=(pidx, y, x, (usable_w-(x+w))+(usable_h-(y+h)))
                    if best is None or score < best[0]:
                        best=(score,pidx,rot,w,h,x,y)
        if best is None:
            # posicionamento diagnóstico em página nova, mesmo que exceda
            pidx=len(pages); pages.append([])
            rot,w,h=max(dims, key=lambda d:min(usable_w/max(d[1],EPS), usable_h/max(d[2],EPS)))
            x=y=0.0
        else:
            _,pidx,rot,w,h,x,y=best
            if pidx==len(pages): pages.append([])
        pages[pidx].append((float(x),float(y),float(w),float(h)))
        placements.append(NestedPagePlacement(int(pidx+1), int(comp.component_index), float(x), float(y), int(rot), float(w), float(h)))
    page_count=max(1,len(pages))
    return placements,page_count,bool(all_fit),warnings


def _v2524_pack_components_best(components, page='A4', margin_mm=10.0, allow_rotate=True, gap=4.0):
    """Testa retrato/paisagem e escolhe menor número de páginas, melhor aproveitamento."""
    base=_v252_page_dims(page)
    candidates=[('portrait',(float(base[0]),float(base[1])))]
    if abs(base[0]-base[1])>1e-9:
        candidates.append(('landscape',(float(base[1]),float(base[0]))))
    best=None
    material_area=sum(_v2524_component_material_area_mm2(c, 1.0) for c in components) # unidades de bbox normalizadas; só desempate
    for orient,dims in candidates:
        usable=(max(1.0,dims[0]-2*margin_mm), max(1.0,dims[1]-2*margin_mm))
        placements,pages,all_fit,warnings=_v2524_pack_rectangles_candidate(components,usable[0],usable[1],gap=gap,allow_rotate=allow_rotate)
        used_rect=sum(p.width_mm*p.height_mm for p in placements)
        util_rect=100.0*used_rect/(max(1,pages)*usable[0]*usable[1])
        score=(0 if all_fit else 1, pages, -util_rect, min(usable))
        if best is None or score < best[0]:
            best=(score,orient,dims,usable,placements,pages,all_fit,warnings,util_rect)
    _,orient,dims,usable,placements,pages,all_fit,warnings,util_rect=best
    return str(orient),(float(dims[0]),float(dims[1])),(float(usable[0]),float(usable[1])),placements,int(pages),bool(all_fit),list(warnings),float(min(100.0,max(0.0,util_rect)))


def _v2524_tile_plan_for_component(comp, usable_w, usable_h, allow_network_rotate=True, overlap_mm=0.0):
    """Escolhe rotação 0/90 da rede que minimiza número de tiles e desperdício."""
    candidates=[]
    for rot in ([0,90] if allow_network_rotate else [0]):
        c=_v2524_copy_component_rotated(comp, rot)
        step_x=max(1.0, usable_w-float(overlap_mm)); step_y=max(1.0, usable_h-float(overlap_mm))
        nx=max(1,int(math.ceil(c.width_mm/step_x-1e-12)))
        ny=max(1,int(math.ceil(c.height_mm/step_y-1e-12)))
        pages=nx*ny
        waste=pages*usable_w*usable_h - min(c.width_mm,nx*usable_w)*min(c.height_mm,ny*usable_h)
        candidates.append((pages,waste,max(c.width_mm,c.height_mm),rot,c,nx,ny))
    return min(candidates, key=lambda z:(z[0],z[1],z[2]))


def _v2524_choose_tiled_layout(page='A4', margin_mm=10.0, components=None, allow_rotate=True, overlap_mm=0.0):
    """Testa orientação da página e rotação da rede para reduzir número de tiles."""
    base=_v252_page_dims(page)
    page_orients=[('portrait',(float(base[0]),float(base[1])))]
    if abs(base[0]-base[1])>1e-9:
        page_orients.append(('landscape',(float(base[1]),float(base[0]))))
    components=list(components or [])
    best=None
    for po,dims in page_orients:
        usable=(max(1.0,dims[0]-2*margin_mm), max(1.0,dims[1]-2*margin_mm))
        rotated=[]; total_pages=0; total_waste=0.0; tile_meta=[]
        for comp in components:
            pages,waste,_,rot,c,nx,ny=_v2524_tile_plan_for_component(comp,usable[0],usable[1],allow_rotate,overlap_mm)
            rotated.append(c); total_pages+=pages; total_waste+=waste
            tile_meta.append({'component_index':int(comp.component_index),'network_rotation':int(rot),'tiles_x':int(nx),'tiles_y':int(ny),'pages':int(pages),'waste_mm2':float(max(0.0,waste))})
        score=(total_pages,total_waste, -usable[0]*usable[1])
        if best is None or score<best[0]:
            best=(score,po,dims,usable,rotated,tile_meta)
    _,po,dims,usable,rotated,tile_meta=best
    return str(po),(float(dims[0]),float(dims[1])),(float(usable[0]),float(usable[1])),rotated,tile_meta


def _v2524_make_tiled_windows_for_component(comp, usable_w, usable_h, start_page=1, overlap_mm=0.0):
    windows=[]
    step_x=max(1.0, usable_w-float(overlap_mm)); step_y=max(1.0, usable_h-float(overlap_mm))
    nx=max(1,int(math.ceil(comp.width_mm/step_x-1e-12)))
    ny=max(1,int(math.ceil(comp.height_mm/step_y-1e-12)))
    pg=int(start_page)
    for iy in range(ny):
        for ix in range(nx):
            x0=ix*step_x; y0=iy*step_y
            x1=min(x0+usable_w, comp.width_mm); y1=min(y0+usable_h, comp.height_mm)
            u=max(0.0,min(100.0,100.0*max(0.0,x1-x0)*max(0.0,y1-y0)/(usable_w*usable_h)))
            windows.append({
                'page':int(pg), 'component_index':int(comp.component_index),
                'tile_x':int(ix+1), 'tile_y':int(iy+1), 'tiles_x':int(nx), 'tiles_y':int(ny),
                'window_x0_mm':float(x0), 'window_y0_mm':float(y0),
                'window_x1_mm':float(x1), 'window_y1_mm':float(y1),
                'window_width_mm':float(max(0.0,x1-x0)),
                'window_height_mm':float(max(0.0,y1-y0)),
                'tile_utilization_percent':float(u),
                'register_marks': True,
            })
            pg += 1
    return windows, pg


def _v2524_face_records_by_index(net):
    return {nf.face_index:nf for nf in net.faces}


def _v2524_group_boundary_tabs(poly, cert, group_faces, tab_frac=0.22, tab_shape='trapezoidal'):
    group=set(map(int,group_faces)); tabs=[]
    for edge,fs in sorted(poly.edge_to_faces().items()):
        inside=[f for f in fs if f in group]
        outside=[f for f in fs if f not in group]
        if not inside: continue
        # Se a aresta não é interna ao grupo, precisa de aba/indicação para montagem.
        if outside or len(fs)==1:
            fi=min(inside)
            poly2d=_v252_tab_polygon_for_face(poly,cert.net,fi,edge,tab_frac,tab_shape)
            if poly2d is not None:
                tabs.append(poly2d)
    return tabs


def _v2524_component_from_face_group(poly, cert, idx, group_faces, scale_mm=50.0, tab_frac=0.22, tab_shape='trapezoidal'):
    fdict=_v2524_face_records_by_index(cert.net)
    faces=[int(f) for f in group_faces if int(f) in fdict]
    polys=[fdict[f].poly2d for f in faces]
    tabs=_v2524_group_boundary_tabs(poly,cert,faces,tab_frac,tab_shape)
    bb=_v252_bbox_pts(polys+tabs) if (polys or tabs) else (0.0,0.0,0.0,0.0)
    return NestedComponent(int(idx),faces,polys,tabs,bb,float((bb[2]-bb[0])*scale_mm),float((bb[3]-bb[1])*scale_mm))


def _v2524_groups_fit(poly, cert, faces, scale_mm, usable_w, usable_h, tab_frac=0.22, tab_shape='trapezoidal'):
    comp=_v2524_component_from_face_group(poly,cert,1,faces,scale_mm,tab_frac,tab_shape)
    return (comp.width_mm <= usable_w+1e-9 and comp.height_mm <= usable_h+1e-9) or (comp.height_mm <= usable_w+1e-9 and comp.width_mm <= usable_h+1e-9)


def _v2524_make_whole_face_components(poly, cert, scale_mm, usable_w, usable_h, tab_frac=0.22, tab_shape='trapezoidal'):
    """Agrupa faces conectadas que caibam inteiras na página, em escala fixa."""
    adj=poly.face_adjacency(); unassigned=set(range(len(poly.faces))); groups=[]
    areas={i:poly.face_area(poly.faces[i]) for i in range(len(poly.faces))}
    while unassigned:
        seed=max(unassigned,key=lambda i:areas.get(i,0.0))
        group={seed}; unassigned.remove(seed)
        changed=True
        while changed:
            changed=False
            cand=[]
            for f in group:
                for nb,_edge in adj.get(f,[]):
                    if nb in unassigned: cand.append(nb)
            cand=sorted(set(cand), key=lambda i:-areas.get(i,0.0))
            for nb in cand:
                trial=group|{nb}
                if _v2524_groups_fit(poly,cert,trial,scale_mm,usable_w,usable_h,tab_frac,tab_shape):
                    group.add(nb); unassigned.remove(nb); changed=True
        groups.append(sorted(group))
    comps=[_v2524_component_from_face_group(poly,cert,i+1,g,scale_mm,tab_frac,tab_shape) for i,g in enumerate(groups)]
    # Rotaciona componentes se melhorar encaixe individual.
    fixed=[]
    for c in comps:
        r0=c; r90=_v2524_copy_component_rotated(c,90)
        if r90.width_mm <= usable_w+1e-9 and r90.height_mm <= usable_h+1e-9 and (r0.width_mm>usable_w+1e-9 or r0.height_mm>usable_h+1e-9):
            fixed.append(r90)
        else:
            fixed.append(r0)
    return fixed


def _v2524_page_utilization_from_placements(placements, usable_w, usable_h, material_area_by_comp=None):
    bypage=defaultdict(float)
    if material_area_by_comp:
        placed_once=set()
        for p in placements:
            key=(p.page,p.component_index)
            if key in placed_once: continue
            placed_once.add(key)
            bypage[int(p.page)] += float(material_area_by_comp.get(int(p.component_index), p.width_mm*p.height_mm))
    else:
        for p in placements:
            bypage[int(p.page)] += float(p.width_mm)*float(p.height_mm)
    out=[]
    for pg in range(1, max(bypage.keys() or [1])+1):
        u=100.0*bypage.get(pg,0.0)/(usable_w*usable_h) if usable_w>0 and usable_h>0 else 0.0
        out.append({'page':int(pg),'utilization_percent':float(min(100.0,max(0.0,u)))})
    return out


_solve_certified_nesting_before_v2524 = _legacy_solve_certified_nesting_v2523_fixed_tile

def solve_certified_nesting(poly, cert=None, page='A4', scale_mm=50.0, margin_mm=10.0,
                            allow_rotate=True, tab_frac=0.22, tab_shape='trapezoidal',
                            attempts=300, auto_scale=True, min_scale_mm=5.0,
                            page_policy='auto', tile_overlap_mm=0.0):
    """Nesting v25.2.4.

    Políticas:
    - 'auto': preserva escala; se necessário, ladrilha com orientação material-efficient.
    - 'fixed_tile': preserva escala e ladrilha quando preciso.
    - 'autoscale': reduz escala para caber em 1 página.
    - 'whole_faces': preserva escala e distribui grupos de faces inteiras por página.
    """
    cert=cert or search_certified_net(poly,attempts=attempts,page=page,scale_mm=scale_mm,margin_mm=margin_mm,tab_frac=tab_frac,tab_shape=tab_shape)
    requested_scale=float(scale_mm)
    policy=str(page_policy or ('autoscale' if auto_scale else 'fixed_tile')).lower()
    aliases={
        'tile':'fixed_tile','fixed':'fixed_tile','fixed-scale':'fixed_tile','preserve':'fixed_tile','preservar':'fixed_tile',
        'autoscale_1page':'autoscale','scale':'autoscale','auto_scale':'autoscale',
        'whole':'whole_faces','whole_faces':'whole_faces','faces':'whole_faces','faces_inteiras':'whole_faces','inteiras':'whole_faces'
    }
    policy=aliases.get(policy,policy)
    if policy not in {'fixed_tile','autoscale','auto','whole_faces'}:
        policy='auto'

    if policy=='autoscale':
        res=_solve_certified_nesting_before_v2524(poly,cert,page,scale_mm,margin_mm,allow_rotate,tab_frac,tab_shape,attempts,True,min_scale_mm,'autoscale',tile_overlap_mm)
        res.layout_engine='v25.2.4 autoscale compatibility'
        res.certification_label='verificado computacionalmente sob tolerância geométrica'
        return res

    components=_v2522_make_components_from_cert(poly,cert,requested_scale)

    # Modo faces inteiras por página: alternativa ao pôster que corta faces.
    if policy=='whole_faces':
        # Escolhe orientação e cria grupos com base na maior área útil.
        orient,page_dims,usable,_,_= _v2522_best_page_orientation_for_components(page,components,float(margin_mm),allow_rotate)
        # Se a orientação oposta tiver área/lado mais favorável para faces individuais, o pack final decide.
        comps=_v2524_make_whole_face_components(poly,cert,requested_scale,usable[0],usable[1],tab_frac,tab_shape)
        orient,page_dims,usable,placements,pages,all_fit,warnings,util_rect=_v2524_pack_components_best(comps,page,margin_mm,allow_rotate,gap=4.0)
        material_by={int(c.component_index):_v2524_component_material_area_mm2(c,requested_scale) for c in comps}
        total_material=sum(material_by.values())
        util=min(100.0,max(0.0,100.0*total_material/(max(1,pages)*usable[0]*usable[1]))) if all_fit else None
        warnings=list(warnings)+['Modo faces inteiras: evita cortar faces nas bordas da página; abas adicionais são geradas entre componentes.']
        res=NestingResult(str(page),(float(page_dims[0]),float(page_dims[1])),(float(usable[0]),float(usable[1])),float(margin_mm),float(requested_scale),comps,placements,int(max(1,pages)),util,bool(all_fit),warnings)
        res.page_windows=[]; res.page_policy='whole_faces'; res.tiled=False; res.whole_face_mode=True
        res.requested_scale_mm=float(requested_scale); res.applied_scale_mm=float(requested_scale); res.scale_adjusted=False
        res.suggested_scale_mm=float(requested_scale); res.page_orientation=str(orient); res.layout_status='fixed_scale_whole_faces' if all_fit else 'whole_faces_component_too_large'
        res.auto_scale=False; res.tile_overlap_mm=float(tile_overlap_mm); res.page_utilization=_v2524_page_utilization_from_placements(placements,usable[0],usable[1],material_by)
        res.layout_engine='v25.2.4 whole-face grouping + candidate bottom-left pack'
        res.certification_label='verificado computacionalmente sob tolerância geométrica'
        return res

    # Primeiro tenta empacotar componentes inteiros em escala fixa com pack melhorado.
    orient,page_dims,usable,placements,pages,all_fit,warnings,util_rect=_v2524_pack_components_best(components,page,margin_mm,allow_rotate,gap=4.0)
    if all_fit:
        material_by={int(c.component_index):_v2524_component_material_area_mm2(c,requested_scale) for c in components}
        total_material=sum(material_by.values())
        util=min(100.0,max(0.0,100.0*total_material/(max(1,pages)*usable[0]*usable[1])))
        res=NestingResult(str(page),(float(page_dims[0]),float(page_dims[1])),(float(usable[0]),float(usable[1])),float(margin_mm),float(requested_scale),components,placements,int(max(1,pages)),util,True,list(warnings))
        res.page_windows=[]; res.page_policy=policy; res.tiled=False
        res.requested_scale_mm=float(requested_scale); res.applied_scale_mm=float(requested_scale); res.scale_adjusted=False; res.suggested_scale_mm=float(requested_scale)
        res.page_orientation=str(orient); res.layout_status='fit_fixed_scale_material_efficient'; res.auto_scale=False
        res.page_utilization=_v2524_page_utilization_from_placements(placements,usable[0],usable[1],material_by)
        res.layout_engine='v25.2.4 candidate bottom-left pack'
        res.certification_label='verificado computacionalmente sob tolerância geométrica'
        return res

    # Se não couber inteiro: políticas auto/fixed_tile preservam escala com ladrilhamento material-efficient.
    orient,page_dims,usable,rot_components,tile_meta=_v2524_choose_tiled_layout(page,float(margin_mm),components,allow_rotate,tile_overlap_mm)
    page_windows=[]; placements=[]; next_page=1
    for comp in rot_components:
        windows,next_page=_v2524_make_tiled_windows_for_component(comp,usable[0],usable[1],start_page=next_page,overlap_mm=tile_overlap_mm)
        for w in windows:
            w['network_rotation_degrees']=int(getattr(comp,'source_rotation_degrees',0))
            page_windows.append(w)
            placements.append(NestedPagePlacement(int(w['page']),int(comp.component_index),0.0,0.0,0,float(w['window_width_mm']),float(w['window_height_mm'])))
    pages=max([w['page'] for w in page_windows],default=1)
    material_area=sum(_v2524_component_material_area_mm2(c,requested_scale) for c in rot_components)
    util=min(100.0,max(0.0,100.0*material_area/(max(1,pages)*usable[0]*usable[1]))) if pages>0 else None
    suggested_rel=min([_v2522_fit_factor_for_component(c,usable[0],usable[1],allow_rotate) for c in components] or [1.0])
    suggested_scale=max(float(min_scale_mm), requested_scale*max(0.0,suggested_rel)*0.995)
    warnings=['Escala fixa preservada; componente(s) maior(es) que a página foram ladrilhados em múltiplas páginas com marcas de registro. Layout v25.2.4 testou orientação da página e rotação da rede para reduzir tiles/desperdício.']
    res=NestingResult(str(page),(float(page_dims[0]),float(page_dims[1])),(float(usable[0]),float(usable[1])),float(margin_mm),float(requested_scale),rot_components,placements,int(max(1,pages)),util,True,warnings)
    res.page_windows=page_windows; res.page_policy=policy; res.tiled=True
    res.requested_scale_mm=float(requested_scale); res.applied_scale_mm=float(requested_scale); res.scale_adjusted=False; res.suggested_scale_mm=float(suggested_scale)
    res.page_orientation=str(orient); res.layout_status='fixed_scale_tiled_material_efficient'; res.auto_scale=False; res.tile_overlap_mm=float(tile_overlap_mm)
    res.page_utilization=[{'page':int(w['page']),'utilization_percent':float(w.get('tile_utilization_percent',0.0))} for w in page_windows]
    res.tile_layout_meta=tile_meta; res.layout_engine='v25.2.4 tiled orientation search'
    res.certification_label='verificado computacionalmente sob tolerância geométrica'
    return res


_certified_net_report_before_v2524 = _legacy_certified_net_report_v2523

def certified_net_report(poly, cert, nesting=None):
    lines=[]
    lines.append('Rede imprimível verificada computacionalmente v25.2.4')
    lines.append('='*62)
    lines.append(f'Sólido: {poly.name}')
    lines.append(f'Estratégia da rede: {cert.strategy}')
    lines.append(f'Tentativas: {cert.attempts}')
    lines.append(f'Status da rede: {cert.status}')
    lines.append(f'Rede de faces construível: {"sim" if cert.constructible else "não"}')
    lines.append(f'Faces: {len(cert.net.faces)}/{len(poly.faces)}')
    lines.append(f'Sobreposição de faces: {len(cert.face_overlaps)}')
    lines.append(f'Conflitos aba-face (aviso): {len(cert.tab_face_overlaps)}')
    lines.append(f'Conflitos aba-aba (aviso): {len(cert.tab_tab_overlaps)}')
    lines.append(f'Arestas de dobra estimadas: {cert.tree_fold_edges}')
    lines.append(f'Arestas de corte/contorno: {cert.cut_edges}')
    lines.append(f'Abas numeradas: {len(cert.tabs)}')
    lines.append(f'Score: {cert.score:.3f}')
    lines.append('')
    lines.append('Nota técnica')
    lines.append('-'*12)
    lines.append('Verificação computacional sob tolerância geométrica; usa predicados robustos/adaptativos para cruzamentos estritos.')
    lines.append('A busca é heurística: uma falha não prova inexistência de outra rede válida.')
    lines.append('')
    lines.append('Abas de colagem')
    lines.append('-'*18)
    for t in cert.tabs[:200]:
        if t.mate_face is None:
            lines.append(f'{t.glue_id}: face {t.face_index+1}, borda {t.edge}')
        else:
            lines.append(f'{t.glue_id}: face {t.face_index+1} cola na face {t.mate_face+1}, aresta {t.edge}')
    if len(cert.tabs)>200:
        lines.append(f'... {len(cert.tabs)-200} abas restantes')
    if nesting:
        lines += ['', 'Layout / nesting de páginas', '-'*27]
        lines.append(f'Política: {getattr(nesting,"page_policy","n/d")}')
        lines.append(f'Motor: {getattr(nesting,"layout_engine","n/d")}')
        lines.append(f'Página: {nesting.page_name} ({getattr(nesting,"page_orientation","n/d")}) {nesting.page_dims_mm[0]:.1f}×{nesting.page_dims_mm[1]:.1f} mm')
        lines.append(f'Área útil: {nesting.usable_dims_mm[0]:.1f}×{nesting.usable_dims_mm[1]:.1f} mm; margem {nesting.margin_mm:.1f} mm')
        lines.append(f'Escala solicitada: {getattr(nesting,"requested_scale_mm",nesting.scale_mm):.3f} mm/unid.')
        lines.append(f'Escala aplicada: {getattr(nesting,"applied_scale_mm",nesting.scale_mm):.3f} mm/unid.')
        lines.append(f'Escala ajustada: {"sim" if getattr(nesting,"scale_adjusted",False) else "não"}')
        lines.append(f'Ladrilhamento: {"sim" if getattr(nesting,"tiled",False) else "não"}')
        lines.append(f'Modo faces inteiras: {"sim" if getattr(nesting,"whole_face_mode",False) else "não"}')
        lines.append(f'Páginas: {nesting.page_count}')
        if nesting.utilization_percent is None:
            lines.append('Aproveitamento global: n/a')
        else:
            lines.append(f'Aproveitamento global: {nesting.utilization_percent:.2f}%')
        if getattr(nesting,'page_utilization',None):
            lines.append('Aproveitamento por página/tile:')
            for u in nesting.page_utilization[:80]:
                lines.append(f'  página {u.get("page")}: {u.get("utilization_percent",0.0):.2f}%')
            if len(nesting.page_utilization)>80:
                lines.append(f'  ... {len(nesting.page_utilization)-80} páginas restantes')
        if getattr(nesting,'page_windows',None):
            lines.append('Janelas de página:')
            for w in nesting.page_windows[:80]:
                lines.append(f'  p.{w["page"]}: comp {w["component_index"]}, tile {w["tile_x"]}/{w["tiles_x"]}, {w["tile_y"]}/{w["tiles_y"]}, janela=({w["window_x0_mm"]:.1f},{w["window_y0_mm"]:.1f})–({w["window_x1_mm"]:.1f},{w["window_y1_mm"]:.1f}), rot={w.get("network_rotation_degrees",0)}°')
            if len(nesting.page_windows)>80:
                lines.append(f'  ... {len(nesting.page_windows)-80} janelas restantes')
        if nesting.warnings:
            lines.append('Avisos:')
            for w in nesting.warnings:
                lines.append(f'- {w}')
    return '\n'.join(lines)


_certified_net_payload_before_v2524 = _legacy_certified_net_payload_v2523

def certified_net_payload(poly, cert, nesting=None):
    payload=_certified_net_payload_before_v2524(poly,cert,nesting)
    payload['version']='25.2.4'
    payload['technical_label']='verificado computacionalmente sob tolerância geométrica'
    payload['certification_note']='Verificação computacional sob tolerância geométrica; usa predicados robustos/adaptativos para cruzamentos estritos. A busca é heurística e não prova inexistência de outras redes.'
    if nesting is not None:
        payload.setdefault('nesting',{})
        payload['nesting'].update({
            'layout_engine':getattr(nesting,'layout_engine','v25.2.4'),
            'whole_face_mode':bool(getattr(nesting,'whole_face_mode',False)),
            'page_utilization':getattr(nesting,'page_utilization',[]),
            'tile_layout_meta':getattr(nesting,'tile_layout_meta',[]),
            'technical_label':getattr(nesting,'certification_label','verificado computacionalmente sob tolerância geométrica'),
        })
    return payload


# UI: preserva aba anterior e acrescenta política de faces inteiras.
class GeoPolyAppV2524(GeoPolyAppV2523):
    """v25.2.4: mantém menus e adiciona layout eficiente/material + modo faces inteiras."""
    def _build_certified_net_tab(self):
        super()._build_certified_net_tab()
        try:
            vals=list(self.cert_page_policy_var.get() for _ in [0])
            # Localiza combobox criada pela v25.2.3 e amplia opções, quando possível.
            def walk(w):
                out=[]
                for c in w.winfo_children():
                    out.append(c); out.extend(walk(c))
                return out
            for w in walk(self.tabcert):
                if isinstance(w, ttk.Combobox) and str(w.cget('width'))=='42':
                    w['values']=[
                        'Auto: preservar escala; ladrilhar se necessário',
                        'Preservar escala e ladrilhar',
                        'Autoescala para caber em 1 página',
                        'Preservar escala; faces inteiras por página',
                    ]
        except Exception:
            pass
    def _cert_page_policy_code(self):
        txt=str(getattr(self,'cert_page_policy_var',tk.StringVar(value='')).get()) if hasattr(self,'cert_page_policy_var') else ''
        if txt.startswith('Preservar escala; faces') or 'faces inteiras' in txt:
            return 'whole_faces'
        if txt.startswith('Preservar'): return 'fixed_tile'
        if txt.startswith('Autoescala'): return 'autoscale'
        return 'auto'


_full_report_before_v2524 = full_report

def full_report(poly,scale_mm=50.0,density_g_cm3=1.24,cost_per_kg=100.0):
    md,payload=_full_report_before_v2524(poly,scale_mm,density_g_cm3,cost_per_kg)
    try:
        cert=search_certified_net(poly,attempts=80,scale_mm=scale_mm,tab_frac=0.22)
        nesting=solve_certified_nesting(poly,cert,scale_mm=scale_mm,attempts=80,page_policy='auto')
        payload['certified_printable_net_v2524']=certified_net_payload(poly,cert,nesting)
        md += '\n\n## Rede imprimível verificada computacionalmente v25.2.4\n'
        md += f'- Rede de faces construível: {"sim" if cert.constructible else "não"}\n'
        md += f'- Sobreposições de faces: {len(cert.face_overlaps)}\n'
        md += f'- Política de página: {getattr(nesting,"page_policy","n/d")}\n'
        md += f'- Motor de layout: {getattr(nesting,"layout_engine","n/d")}\n'
        md += f'- Páginas estimadas: {nesting.page_count}\n'
        md += f'- Escala aplicada: {getattr(nesting,"applied_scale_mm",nesting.scale_mm):.3f} mm/unid.\n'
        md += f'- Ladrilhamento: {"sim" if getattr(nesting,"tiled",False) else "não"}\n'
        if nesting.utilization_percent is None: md += '- Aproveitamento global: n/a\n'
        else: md += f'- Aproveitamento global: {nesting.utilization_percent:.2f}%\n'
        md += '- Nota: verificação computacional sob tolerância geométrica; busca heurística.\n'
    except Exception as exc:
        payload['certified_printable_net_v2524_error']=str(exc)
        md += '\n\n## Rede imprimível verificada computacionalmente v25.2.4\n- Não foi possível gerar verificação automática: '+str(exc)+'\n'
    return md,payload


_run_self_tests_before_v2524 = run_self_tests

def run_self_tests():
    rep=_run_self_tests_before_v2524(); results=list(rep.results)
    def add(name,ok,detail=''):
        results.append(TestCaseResult('v25.2.4 / '+name,bool(ok),'' if ok else str(detail)))
    try:
        dod=_v252_catalog_poly('Platônicos / Dodecaedro')
        cert=search_certified_net(dod,attempts=220,tab_frac=0.22,max_seconds=10.0)
        nest=solve_certified_nesting(dod,cert,page='A4',scale_mm=50.0,margin_mm=10.0,page_policy='fixed_tile',auto_scale=False)
        add('dodecaedro fixed_tile preserva escala', abs(getattr(nest,'applied_scale_mm',0)-50.0)<1e-9 and not getattr(nest,'scale_adjusted',True), certified_net_payload(dod,cert,nest))
        add('dodecaedro fixed_tile tem janelas e cabe', nest.all_fit and getattr(nest,'tiled',False) and len(getattr(nest,'page_windows',[]))==nest.page_count and nest.page_count>=2, certified_net_payload(dod,cert,nest))
        add('aproveitamento global e por tile válido', nest.utilization_percent is not None and 0<=nest.utilization_percent<=100 and all(0<=u.get('utilization_percent',0)<=100 for u in getattr(nest,'page_utilization',[])), certified_net_payload(dod,cert,nest))
        whole=solve_certified_nesting(dod,cert,page='A4',scale_mm=50.0,margin_mm=10.0,page_policy='whole_faces',auto_scale=False)
        add('modo faces inteiras preserva escala', getattr(whole,'whole_face_mode',False) and abs(getattr(whole,'applied_scale_mm',0)-50.0)<1e-9, certified_net_payload(dod,cert,whole))
        add('modo faces inteiras não usa janelas de corte', not getattr(whole,'tiled',False) and len(getattr(whole,'page_windows',[]))==0 and whole.page_count>=1, certified_net_payload(dod,cert,whole))
        add('payload v25.2.4 serializa JSON', isinstance(json.dumps(certified_net_payload(dod,cert,nest),default=str),str), '')
        add('rótulo técnico honesto no payload', 'tolerância' in certified_net_payload(dod,cert,nest).get('technical_label',''), certified_net_payload(dod,cert,nest))
        # Export headless: deve funcionar com backend Agg ou TkAgg sem exigir display na importação.
        add('backend matplotlib selecionado', str(matplotlib.get_backend()).lower() in {'agg','tkagg'} or 'agg' in str(matplotlib.get_backend()).lower() or 'tk' in str(matplotlib.get_backend()).lower(), matplotlib.get_backend())
    except Exception as exc:
        add('suíte v25.2.4 sem exceção', False, repr(exc))
    return TestReport(results)


APP_NAME='GeoPoly'
VERSION='25.2.4'
EDITION='Material-Efficient Layout & Headless Export Fix + Embedded Johnson Formal Bundle'


def main():
    GeoPolyAppV2524().mainloop()

if False and __name__ == '__main__':
    main()




# v27.2f: explicit export list so internal star imports preserve historical
# single-underscore helper symbols without using wholesale update calls.
__all__ = [k for k in globals() if not k.startswith('__')]
