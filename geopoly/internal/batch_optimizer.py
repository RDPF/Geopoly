"""GeoPoly v27 internal module: Batch material optimizer and headless export hardening."""
# v27.2f: named internal dependency import.
# Wildcard imports were removed to improve static analysis.
# v27.2f: named internal dependency imports; no wildcard imports.
from .fixed_scale_nesting import (
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
    _run_self_tests_before_v2524,
)

# ============================================================
# v25.2.5 — Batch Material Optimizer
# ============================================================
# Objetivo: manter todo o pipeline anterior e acrescentar otimização de lote.
# Onde há ganho real de material: várias redes/componentes competindo pelas
# sobras das mesmas páginas. O motor abaixo compara layout ingênuo (cada rede
# separada) contra empacotamento global first-fit decreasing com rotação 0/90.

@dataclass
class BatchNetJob:
    job_id:int
    catalog_key:str
    name:str
    scale_mm:float
    quantity:int=1
    page_policy:str='fixed_tile'

@dataclass
class BatchPiece:
    piece_id:int
    job_id:int
    copy_index:int
    solid_name:str
    component_index:int
    kind:str                 # 'component' ou 'tile'
    width_mm:float
    height_mm:float
    material_area_mm2:float
    payload:dict

@dataclass
class BatchPiecePlacement:
    page:int
    piece_id:int
    x_mm:float
    y_mm:float
    rotation:int
    width_mm:float
    height_mm:float

@dataclass
class BatchOptimizationResult:
    page_name:str
    page_dims_mm:Tuple[float,float]
    usable_dims_mm:Tuple[float,float]
    margin_mm:float
    jobs:List[BatchNetJob]
    pieces:List[BatchPiece]
    placements:List[BatchPiecePlacement]
    baseline_pages:int
    optimized_pages:int
    saved_pages:int
    baseline_utilization_percent:float
    optimized_utilization_percent:float
    page_utilization:List[dict]
    warnings:List[str]
    layout_engine:str='v25.2.5 batch first-fit decreasing + 0/90 rotation'
    technical_label:str='otimização heurística de lote; verificada computacionalmente sob tolerância geométrica'


def _v2525_page_setup(page='A4', margin_mm=10.0):
    base=_v252_page_dims(page)
    # Usa a orientação com maior largura útil para peças longas; o pack considera rotação das peças.
    candidates=[]
    for orient,dims in [('portrait',base),('landscape',(base[1],base[0]))]:
        usable=(max(1e-9,dims[0]-2*margin_mm),max(1e-9,dims[1]-2*margin_mm))
        candidates.append((orient,dims,usable))
    # Paisagem costuma aproveitar melhor redes alongadas; em empate, maior largura primeiro.
    candidates.sort(key=lambda t:(t[2][0]*t[2][1],t[2][0]),reverse=True)
    return candidates[0]


def _v2525_poly_area_mm2(polys, scale_mm):
    total=0.0
    for P in polys or []:
        try:
            total += abs(poly_area2d(np.asarray(P,dtype=float))) * float(scale_mm)**2
        except Exception:
            pass
    return float(max(0.0,total))


def _v2525_component_material_area(comp, scale_mm):
    return _v2525_poly_area_mm2(list(getattr(comp,'polygons',[]))+list(getattr(comp,'tabs',[])),scale_mm)


def _v2525_catalog_item_keys():
    keys=[]
    try:
        keys=[it.key for it in CATALOG_ITEMS]
    except Exception:
        keys=[]
    return keys


def _v2525_build_poly_from_key(key):
    for it in CATALOG_ITEMS:
        if it.key == key or key in it.key:
            return it.build()
    raise KeyError(key)


def _v2525_default_platonic_jobs(scale_mm=50.0):
    names=['Platônicos / Tetraedro','Platônicos / Cubo','Platônicos / Octaedro','Platônicos / Dodecaedro','Platônicos / Icosaedro']
    jobs=[]
    for i,k in enumerate(names,1):
        jobs.append(BatchNetJob(i,k,k.split('/')[-1].strip(),float(scale_mm),1,'fixed_tile'))
    return jobs


def _v2525_piece_from_component(piece_id, job, copy_index, comp, scale_mm):
    return BatchPiece(
        int(piece_id),int(job.job_id),int(copy_index),str(job.name),int(comp.component_index),'component',
        float(comp.width_mm),float(comp.height_mm),
        _v2525_component_material_area(comp,scale_mm),
        {'component':comp,'scale_mm':float(scale_mm),'bbox':tuple(map(float,comp.bbox))}
    )


def _v2525_piece_from_tile(piece_id, job, copy_index, comp, window, scale_mm):
    # Área material aproximada pela fração da área retangular do tile com respeito à área do componente.
    comp_area=max(1e-9,float(comp.width_mm)*float(comp.height_mm))
    tile_area=max(0.0,float(window.get('window_width_mm',0.0))*float(window.get('window_height_mm',0.0)))
    material=_v2525_component_material_area(comp,scale_mm)*min(1.0,tile_area/comp_area)
    return BatchPiece(
        int(piece_id),int(job.job_id),int(copy_index),str(job.name),int(comp.component_index),'tile',
        float(window.get('window_width_mm',0.0)),float(window.get('window_height_mm',0.0)),float(material),
        {'component':comp,'scale_mm':float(scale_mm),'window':dict(window),'bbox':tuple(map(float,comp.bbox))}
    )


def _v2525_make_pieces_for_job(job, page='A4', margin_mm=10.0, attempts=120, tab_frac=0.22):
    pieces=[]; warnings=[]; baseline_pages=0; pid_start=1
    poly=_v2525_build_poly_from_key(job.catalog_key)
    for copy_index in range(1,int(max(1,job.quantity))+1):
        cert=search_certified_net(poly,attempts=attempts,scale_mm=float(job.scale_mm),tab_frac=tab_frac,max_seconds=8.0)
        nest=solve_certified_nesting(poly,cert,page=page,scale_mm=float(job.scale_mm),margin_mm=float(margin_mm),page_policy=str(job.page_policy or 'fixed_tile'),auto_scale=False,attempts=attempts,tab_frac=tab_frac)
        baseline_pages += int(max(1,getattr(nest,'page_count',1)))
        comps_by_id={int(c.component_index):c for c in getattr(nest,'components',[])}
        if getattr(nest,'tiled',False) and getattr(nest,'page_windows',None):
            for w in nest.page_windows:
                c=comps_by_id.get(int(w.get('component_index',1)))
                if c is None: continue
                pieces.append(_v2525_piece_from_tile(pid_start+len(pieces),job,copy_index,c,w,float(job.scale_mm)))
        else:
            for c in getattr(nest,'components',[]):
                pieces.append(_v2525_piece_from_component(pid_start+len(pieces),job,copy_index,c,float(job.scale_mm)))
        if getattr(nest,'warnings',None):
            warnings += [f'{job.name}: {w}' for w in nest.warnings[:3]]
    return pieces, baseline_pages, warnings


def _v2525_rects_overlap(a,b,gap=0.0):
    ax,ay,aw,ah=a; bx,by,bw,bh=b
    return not (ax+aw+gap <= bx or bx+bw+gap <= ax or ay+ah+gap <= by or by+bh+gap <= ay)


def _v2525_pack_pieces_first_fit(pieces, usable_w, usable_h, allow_rotate=True, gap=3.0):
    """Empacotamento global first-fit decreasing com pontos candidatos bottom-left."""
    order=sorted(pieces,key=lambda p:max(p.width_mm,p.height_mm)*min(p.width_mm,p.height_mm),reverse=True)
    pages=[]  # list of occupied rects [(x,y,w,h,piece_id)]
    placements=[]
    for pc in order:
        dims=[(pc.width_mm,pc.height_mm,0)]
        if allow_rotate and abs(pc.width_mm-pc.height_mm)>1e-9:
            dims.append((pc.height_mm,pc.width_mm,90))
        placed=False
        for pg_idx,occ in enumerate(pages,1):
            candidates=[(0.0,0.0)]
            for x,y,w,h,_pid in occ:
                candidates.append((x+w+gap,y))
                candidates.append((x,y+h+gap))
            # Remove candidatos fora e ordena por bottom-left, depois menor desperdício lateral.
            candidates=list(dict.fromkeys((round(x,6),round(y,6)) for x,y in candidates))
            candidates=sorted(candidates,key=lambda xy:(xy[1],xy[0]))
            best=None
            for w,h,rot in dims:
                if w>usable_w+1e-9 or h>usable_h+1e-9:
                    continue
                for x,y in candidates:
                    if x+w>usable_w+1e-9 or y+h>usable_h+1e-9:
                        continue
                    rect=(x,y,w,h)
                    if all(not _v2525_rects_overlap(rect,(ox,oy,ow,oh),gap=0.0) for ox,oy,ow,oh,_ in occ):
                        score=(y+h, x+w, y, x)
                        if best is None or score<best[0]:
                            best=(score,x,y,w,h,rot)
            if best is not None:
                _score,x,y,w,h,rot=best
                occ.append((x,y,w,h,pc.piece_id))
                placements.append(BatchPiecePlacement(pg_idx,pc.piece_id,float(x),float(y),int(rot),float(w),float(h)))
                placed=True; break
        if not placed:
            # Nova página.
            chosen=None
            for w,h,rot in dims:
                if w<=usable_w+1e-9 and h<=usable_h+1e-9:
                    chosen=(w,h,rot); break
            if chosen is None:
                # Peça maior que página; mantém em página própria e sinaliza via dimensões, sem mentir.
                w,h,rot=dims[0]
            else:
                w,h,rot=chosen
            pages.append([(0.0,0.0,float(w),float(h),pc.piece_id)])
            placements.append(BatchPiecePlacement(len(pages),pc.piece_id,0.0,0.0,int(rot),float(w),float(h)))
    return placements, max(1,len(pages))


def solve_batch_material_optimizer(jobs, page='A4', margin_mm=10.0, attempts=120, allow_rotate=True, tab_frac=0.22):
    """Otimiza lote de redes: cada rede separada vs pool global de peças/tiles.

    O ganho esperado aparece quando pequenas redes ocupam sobras dos tiles de redes maiores.
    A métrica principal é redução de páginas ou aumento de aproveitamento retangular global.
    """
    orient,page_dims,usable=_v2525_page_setup(page,margin_mm)
    all_pieces=[]; baseline_pages=0; warnings=[]
    # Renumera jobs se vierem sem ids únicos.
    norm_jobs=[]
    for i,j in enumerate(jobs,1):
        if isinstance(j,dict):
            jj=BatchNetJob(i,j.get('catalog_key') or j.get('key'),j.get('name') or str(j.get('catalog_key')),float(j.get('scale_mm',50.0)),int(j.get('quantity',1)),j.get('page_policy','fixed_tile'))
        else:
            jj=BatchNetJob(i,j.catalog_key,j.name,float(j.scale_mm),int(getattr(j,'quantity',1)),getattr(j,'page_policy','fixed_tile'))
        norm_jobs.append(jj)
        pieces,pages,warn=_v2525_make_pieces_for_job(jj,page,margin_mm,attempts,tab_frac)
        # Renumeração global dos pieces.
        for p in pieces:
            p.piece_id=len(all_pieces)+1
            all_pieces.append(p)
        baseline_pages += pages
        warnings += warn
    placements,opt_pages=_v2525_pack_pieces_first_fit(all_pieces,usable[0],usable[1],allow_rotate=allow_rotate,gap=3.0)
    rect_area=sum(float(p.width_mm)*float(p.height_mm) for p in all_pieces)
    baseline_util=min(100.0,max(0.0,100.0*rect_area/(max(1,baseline_pages)*usable[0]*usable[1])))
    opt_util=min(100.0,max(0.0,100.0*rect_area/(max(1,opt_pages)*usable[0]*usable[1])))
    bypage=defaultdict(float)
    for pl in placements:
        bypage[int(pl.page)] += float(pl.width_mm)*float(pl.height_mm)
    page_util=[]
    for pg in range(1,opt_pages+1):
        page_util.append({'page':pg,'utilization_percent':float(min(100.0,max(0.0,100.0*bypage.get(pg,0.0)/(usable[0]*usable[1]))))})
    saved=max(0,int(baseline_pages)-int(opt_pages))
    if opt_pages>baseline_pages:
        warnings.append('O empacotamento heurístico usou mais páginas que o layout separado; considerar layout ingênuo para este lote.')
    if saved==0 and opt_util<=baseline_util+1e-9:
        warnings.append('Sem ganho material mensurável neste lote; a otimização é mais útil com várias redes/peças pequenas misturadas a redes grandes.')
    return BatchOptimizationResult(str(page),(float(page_dims[0]),float(page_dims[1])),(float(usable[0]),float(usable[1])),float(margin_mm),norm_jobs,all_pieces,placements,int(baseline_pages),int(opt_pages),int(max(0,baseline_pages-opt_pages)),float(baseline_util),float(opt_util),page_util,warnings)


def batch_optimizer_payload(result):
    return {
        'version':'25.2.5',
        'title':'GeoPoly Batch Material Optimizer',
        'technical_label':result.technical_label,
        'layout_engine':result.layout_engine,
        'page':{'name':result.page_name,'dims_mm':result.page_dims_mm,'usable_dims_mm':result.usable_dims_mm,'margin_mm':result.margin_mm},
        'baseline_pages':result.baseline_pages,
        'optimized_pages':result.optimized_pages,
        'saved_pages':result.saved_pages,
        'baseline_utilization_percent':result.baseline_utilization_percent,
        'optimized_utilization_percent':result.optimized_utilization_percent,
        'page_utilization':result.page_utilization,
        'jobs':[asdict(j) for j in result.jobs],
        'pieces':[{'piece_id':p.piece_id,'job_id':p.job_id,'copy_index':p.copy_index,'solid_name':p.solid_name,'component_index':p.component_index,'kind':p.kind,'width_mm':p.width_mm,'height_mm':p.height_mm,'material_area_mm2':p.material_area_mm2} for p in result.pieces],
        'placements':[asdict(pl) for pl in result.placements],
        'warnings':list(result.warnings),
    }


def batch_optimizer_report(result):
    lines=[]
    lines.append('GeoPoly v25.2.5 — Batch Material Optimizer')
    lines.append('='*58)
    lines.append('Objetivo: empacotar várias redes/componentes no mesmo pool para aproveitar sobras de páginas.')
    lines.append(f'Motor: {result.layout_engine}')
    lines.append(f'Página: {result.page_name} {result.page_dims_mm[0]:.1f}×{result.page_dims_mm[1]:.1f} mm; área útil {result.usable_dims_mm[0]:.1f}×{result.usable_dims_mm[1]:.1f} mm')
    lines.append('')
    lines.append('Fila de impressão')
    lines.append('-'*18)
    for j in result.jobs:
        lines.append(f'{j.job_id}. {j.name} | escala={j.scale_mm:.3f} mm/unid. | qtd={j.quantity} | política={j.page_policy}')
    lines.append('')
    lines.append('Eficiência')
    lines.append('-'*10)
    lines.append(f'Páginas no layout ingênuo/separado: {result.baseline_pages}')
    lines.append(f'Páginas no layout otimizado em lote: {result.optimized_pages}')
    lines.append(f'Economia de folhas: {result.saved_pages}')
    lines.append(f'Aproveitamento ingênuo: {result.baseline_utilization_percent:.2f}%')
    lines.append(f'Aproveitamento otimizado: {result.optimized_utilization_percent:.2f}%')
    lines.append('Aproveitamento por página otimizada:')
    for u in result.page_utilization:
        lines.append(f'  página {u["page"]}: {u["utilization_percent"]:.2f}%')
    lines.append('')
    lines.append('Peças empacotadas')
    lines.append('-'*18)
    byid={p.piece_id:p for p in result.pieces}
    for pl in result.placements:
        p=byid.get(pl.piece_id)
        label=f'{p.solid_name} ({p.kind})' if p else f'peça {pl.piece_id}'
        lines.append(f'página {pl.page}: {label}, peça {pl.piece_id}, x={pl.x_mm:.1f}, y={pl.y_mm:.1f}, rot={pl.rotation}°, caixa={pl.width_mm:.1f}×{pl.height_mm:.1f} mm')
    lines.append('')
    lines.append('Nota sobre modos')
    lines.append('-'*16)
    lines.append('Modo faces inteiras por página: objetivo é facilitar montagem; custo esperado é usar mais papel.')
    lines.append('Otimização de lote: objetivo é reduzir páginas/aproveitar sobras; é heurística, não prova mínimo global.')
    if result.warnings:
        lines.append('')
        lines.append('Avisos')
        lines.append('-'*6)
        for w in result.warnings:
            lines.append(f'- {w}')
    return '\n'.join(lines)


def _v2525_draw_piece_on_axis(ax, piece, placement, margin_mm=10.0, edgecolor='#111'):
    x0=float(margin_mm)+float(placement.x_mm); y0=float(margin_mm)+float(placement.y_mm)
    rot=int(placement.rotation)
    scale=float(piece.payload.get('scale_mm',50.0))
    comp=piece.payload.get('component')
    if comp is None:
        ax.add_patch(MplPolygon(np.array([[x0,y0],[x0+placement.width_mm,y0],[x0+placement.width_mm,y0+placement.height_mm],[x0,y0+placement.height_mm]]),closed=True,fill=False,edgecolor=edgecolor,linewidth=.6))
        return
    bb=piece.payload.get('bbox',comp.bbox)
    bx0,by0,bx1,by1=bb
    win=piece.payload.get('window') if piece.kind=='tile' else None
    wx0=float(win.get('window_x0_mm',0.0)) if win else 0.0
    wy0=float(win.get('window_y0_mm',0.0)) if win else 0.0
    if piece.kind=='component':
        wx0=float(bx0)*scale; wy0=float(by0)*scale
    def tr(P):
        P=np.asarray(P,dtype=float)*scale
        Q=P-np.array([wx0,wy0])
        if rot==90:
            Q=np.column_stack([float(piece.height_mm)-Q[:,1], Q[:,0]])
        return Q+np.array([x0,y0])
    clip=None
    if win:
        # Clip no retângulo da peça/tile já empacotado na página.
        clip=Rectangle((x0,y0),float(placement.width_mm),float(placement.height_mm),transform=ax.transData)
        ax.add_patch(Rectangle((x0,y0),float(placement.width_mm),float(placement.height_mm),fill=False,edgecolor='#999',linestyle=':',linewidth=.6))
    for T in list(getattr(comp,'tabs',[])):
        poly_patch=MplPolygon(tr(T),closed=True,facecolor='#fff2a8',edgecolor='#777',linestyle='--',linewidth=.5,alpha=.8)
        if clip is not None: poly_patch.set_clip_path(clip)
        ax.add_patch(poly_patch)
    for k,P in enumerate(list(getattr(comp,'polygons',[]))):
        poly_patch=MplPolygon(tr(P),closed=True,facecolor='#dfefff',edgecolor=edgecolor,linewidth=.6,alpha=.9)
        if clip is not None: poly_patch.set_clip_path(clip)
        ax.add_patch(poly_patch)
    ax.text(x0+2,y0+2,f'{piece.solid_name}\n#{piece.piece_id}',fontsize=5,ha='left',va='bottom')


def export_batch_optimizer_pdf(result, path, title=None):
    from matplotlib.backends.backend_pdf import PdfPages
    path=Path(path)
    byid={p.piece_id:p for p in result.pieces}
    with PdfPages(path) as pdf:
        for pg in range(1,result.optimized_pages+1):
            fig=plt.Figure(figsize=(result.page_dims_mm[0]/25.4,result.page_dims_mm[1]/25.4),dpi=150)
            ax=fig.add_subplot(111); ax.set_xlim(0,result.page_dims_mm[0]); ax.set_ylim(0,result.page_dims_mm[1]); ax.set_aspect('equal'); ax.axis('off')
            ax.add_patch(Rectangle((result.margin_mm,result.margin_mm),result.usable_dims_mm[0],result.usable_dims_mm[1],fill=False,edgecolor='#888',linestyle=':',linewidth=.8))
            ax.text(result.margin_mm,result.page_dims_mm[1]-result.margin_mm+2,(title or 'GeoPoly Batch')+f' — página {pg}/{result.optimized_pages}',fontsize=7,ha='left',va='bottom')
            for pl in [p for p in result.placements if p.page==pg]:
                piece=byid.get(pl.piece_id)
                if piece: _v2525_draw_piece_on_axis(ax,piece,pl,result.margin_mm)
            pdf.savefig(fig,bbox_inches='tight')
            plt.close(fig)


def export_batch_optimizer_json(result, path):
    Path(path).write_text(json.dumps(batch_optimizer_payload(result),indent=2,ensure_ascii=False,default=str),encoding='utf-8')


_full_report_before_v2525 = full_report

def full_report(poly,scale_mm=50.0,density_g_cm3=1.24,cost_per_kg=100.0):
    md,payload=_full_report_before_v2525(poly,scale_mm,density_g_cm3,cost_per_kg)
    md += '\n\n## Nota v25.2.5 — Otimizador de lote\n'
    md += '- O modo “faces inteiras por página” é mantido como modo de montagem amigável; pode usar mais papel.\n'
    md += '- A economia material mensurável é feita no otimizador de lote, que empacota várias redes/tiles no mesmo pool.\n'
    payload['batch_optimizer_v2525_note']='Use solve_batch_material_optimizer(jobs, ...) ou a aba Lote/Nesting para comparar páginas ingênuas vs otimizadas.'
    return md,payload


def export_batch_optimizer_report_txt(result, path):
    """Write the batch optimizer textual report to disk."""
    path = Path(path)
    path.write_text(batch_optimizer_report(result), encoding='utf-8')
    return path


class GeoPolyAppV2525(GeoPolyAppV2524):
    """v25.2.5: adiciona aba de fila de impressão e otimização global de lote."""
    def _build_ui(self):
        super()._build_ui()
        self.title(f'{APP_NAME} v{VERSION} — {EDITION}')
        self.tabbatch=ttk.Frame(self.nb,padding=6)
        try:
            idx=self.nb.index(self.tabcert)+1
            self.nb.insert(idx,self.tabbatch,text='Lote/Nesting')
        except Exception:
            self.nb.add(self.tabbatch,text='Lote/Nesting')
        self._build_batch_tab()

    def _build_batch_tab(self):
        self.tabbatch.rowconfigure(2,weight=1); self.tabbatch.columnconfigure(0,weight=1)
        top=ttk.LabelFrame(self.tabbatch,text='Batch Material Optimizer — fila de redes para turma/oficina',padding=8)
        top.grid(row=0,column=0,sticky='ew',pady=(0,6)); top.columnconfigure(1,weight=1)
        self.batch_key_var=tk.StringVar(value=(self.combo.get() if hasattr(self,'combo') else (_v2525_catalog_item_keys()[0] if _v2525_catalog_item_keys() else '')))
        self.batch_scale_var=tk.DoubleVar(value=50.0)
        self.batch_qty_var=tk.IntVar(value=1)
        self.batch_page_var=tk.StringVar(value='A4')
        self.batch_margin_var=tk.DoubleVar(value=10.0)
        self.batch_jobs=[]; self.batch_result=None
        ttk.Label(top,text='Sólido:').grid(row=0,column=0,sticky='e')
        ttk.Combobox(top,textvariable=self.batch_key_var,values=_v2525_catalog_item_keys(),width=48,state='readonly').grid(row=0,column=1,sticky='ew',padx=3)
        ttk.Label(top,text='Escala:').grid(row=0,column=2,sticky='e')
        ttk.Spinbox(top,from_=1,to=500,increment=1,textvariable=self.batch_scale_var,width=7).grid(row=0,column=3,padx=3)
        ttk.Label(top,text='Qtd:').grid(row=0,column=4,sticky='e')
        ttk.Spinbox(top,from_=1,to=100,increment=1,textvariable=self.batch_qty_var,width=5).grid(row=0,column=5,padx=3)
        ttk.Label(top,text='Página:').grid(row=0,column=6,sticky='e')
        ttk.Combobox(top,textvariable=self.batch_page_var,values=['A4','Carta'],state='readonly',width=7).grid(row=0,column=7,padx=3)
        ttk.Label(top,text='Margem:').grid(row=0,column=8,sticky='e')
        ttk.Spinbox(top,from_=0,to=40,increment=1,textvariable=self.batch_margin_var,width=6).grid(row=0,column=9,padx=3)
        ttk.Button(top,text='Adicionar ao lote',command=self.batch_add_current).grid(row=0,column=10,padx=3)
        ttk.Button(top,text='Lote platônico teste',command=self.batch_add_platonic_test).grid(row=0,column=11,padx=3)
        ttk.Button(top,text='Limpar',command=self.batch_clear).grid(row=0,column=12,padx=3)
        ttk.Button(top,text='Otimizar lote',command=self.batch_optimize).grid(row=0,column=13,padx=3)
        ttk.Button(top,text='Exportar PDF/JSON/TXT',command=self.batch_export).grid(row=0,column=14,padx=3)
        note=ttk.Label(self.tabbatch,text='Comparação automática: layout ingênuo separado versus empacotamento global first-fit decreasing com rotação 0/90. Modo faces inteiras é de montagem amigável, não de economia de papel.',wraplength=1150)
        note.grid(row=1,column=0,sticky='ew',pady=(0,6))
        pan=ttk.PanedWindow(self.tabbatch,orient='horizontal')
        pan.grid(row=2,column=0,sticky='nsew')
        left=ttk.Frame(pan); right=ttk.Frame(pan)
        pan.add(left,weight=1); pan.add(right,weight=2)
        left.rowconfigure(1,weight=1); left.columnconfigure(0,weight=1)
        self.batch_list=tk.Listbox(left,height=8)
        self.batch_list.grid(row=0,column=0,sticky='ew',pady=(0,4))
        self.batch_text=tk.Text(left,wrap='word',font=('Consolas',9))
        self.batch_text.grid(row=1,column=0,sticky='nsew')
        self.figbatch=plt.Figure(figsize=(7,6),dpi=100); self.axbatch=self.figbatch.add_subplot(111)
        self.canvasbatch=FigureCanvasTkAgg(self.figbatch,master=right); self.canvasbatch.get_tk_widget().pack(fill='both',expand=True)
        self.batch_add_platonic_test(silent=True)

    def _batch_refresh_list(self):
        if not hasattr(self,'batch_list'): return
        self.batch_list.delete(0,'end')
        for j in self.batch_jobs:
            self.batch_list.insert('end',f'{j.job_id}. {j.name} | escala={j.scale_mm:g} | qtd={j.quantity}')

    def batch_add_current(self):
        key=self.batch_key_var.get()
        name=key.split('/')[-1].strip() if key else 'Sólido'
        jid=len(self.batch_jobs)+1
        self.batch_jobs.append(BatchNetJob(jid,key,name,float(self.batch_scale_var.get()),int(self.batch_qty_var.get()),'fixed_tile'))
        self._batch_refresh_list()

    def batch_add_platonic_test(self,silent=False):
        self.batch_jobs=_v2525_default_platonic_jobs(float(self.batch_scale_var.get()) if hasattr(self,'batch_scale_var') else 50.0)
        self._batch_refresh_list()
        if not silent and hasattr(self,'batch_text'):
            self.batch_text.delete('1.0','end'); self.batch_text.insert('end','Lote platônico de teste carregado. Clique em Otimizar lote.\n')

    def batch_clear(self):
        self.batch_jobs=[]; self.batch_result=None; self._batch_refresh_list()
        if hasattr(self,'batch_text'):
            self.batch_text.delete('1.0','end')

    def batch_optimize(self):
        if not self.batch_jobs:
            messagebox.showwarning('Lote vazio','Adicione pelo menos um sólido ao lote.'); return
        try:
            self.batch_result=solve_batch_material_optimizer(self.batch_jobs,page=self.batch_page_var.get(),margin_mm=float(self.batch_margin_var.get()),attempts=120,allow_rotate=True)
            self.batch_text.delete('1.0','end'); self.batch_text.insert('end',batch_optimizer_report(self.batch_result))
            self._draw_batch_preview()
        except Exception as exc:
            self.batch_text.delete('1.0','end'); self.batch_text.insert('end','Erro no otimizador de lote:\n'+repr(exc))
            messagebox.showerror('Otimizar lote',str(exc))

    def _draw_batch_preview(self):
        ax=self.axbatch; ax.clear()
        if not self.batch_result:
            ax.text(.5,.5,'Otimize o lote para visualizar.',ha='center',va='center',transform=ax.transAxes); ax.axis('off'); self.canvasbatch.draw_idle(); return
        res=self.batch_result; ax.set_xlim(0,res.page_dims_mm[0]); ax.set_ylim(0,res.page_dims_mm[1]); ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(Rectangle((res.margin_mm,res.margin_mm),res.usable_dims_mm[0],res.usable_dims_mm[1],fill=False,edgecolor='#888',linestyle=':',linewidth=.8))
        byid={p.piece_id:p for p in res.pieces}
        for pl in [p for p in res.placements if p.page==1]:
            piece=byid.get(pl.piece_id)
            if piece: _v2525_draw_piece_on_axis(ax,piece,pl,res.margin_mm)
        ax.set_title(f'Lote otimizado — página 1/{res.optimized_pages} | economia: {res.saved_pages} folha(s)')
        self.canvasbatch.draw_idle()

    def batch_export(self):
        if self.batch_result is None:
            self.batch_optimize()
        if self.batch_result is None: return
        folder=filedialog.askdirectory(title='Pasta para exportar lote otimizado')
        if not folder: return
        try:
            base=Path(folder)/'geopoly_batch_material_optimizer'
            export_batch_optimizer_pdf(self.batch_result,base.with_suffix('.pdf'),'GeoPoly Batch Material Optimizer')
            export_batch_optimizer_json(self.batch_result,base.with_suffix('.json'))
            base.with_suffix('.txt').write_text(batch_optimizer_report(self.batch_result),encoding='utf-8')
            messagebox.showinfo('Exportação concluída',f'Arquivos salvos em:\n{folder}')
        except Exception as exc:
            messagebox.showerror('Exportar lote',str(exc))


_run_self_tests_before_v2525 = run_self_tests

def run_self_tests():
    rep=_run_self_tests_before_v2525(); results=list(rep.results)
    def add(name,ok,detail=''):
        results.append(TestCaseResult('v25.2.5 / '+name,bool(ok),'' if ok else str(detail)))
    try:
        jobs=_v2525_default_platonic_jobs(50.0)
        res=solve_batch_material_optimizer(jobs,page='A4',margin_mm=10.0,attempts=100,allow_rotate=True)
        add('lote platônico gera peças', len(res.pieces)>=5, batch_optimizer_payload(res))
        add('layout otimizado usa <= páginas do ingênuo', res.optimized_pages <= res.baseline_pages, batch_optimizer_payload(res))
        add('aproveitamento otimizado >= ingênuo', res.optimized_utilization_percent + 1e-9 >= res.baseline_utilization_percent, batch_optimizer_payload(res))
        add('relatório registra economia de folhas', 'Economia de folhas' in batch_optimizer_report(res), batch_optimizer_report(res))
        add('payload batch serializa JSON', isinstance(json.dumps(batch_optimizer_payload(res),ensure_ascii=False,default=str),str), '')
        add('modo faces inteiras rotulado como montagem amigável', 'facilitar montagem' in batch_optimizer_report(res), batch_optimizer_report(res))
        # Caso mínimo solicitado explicitamente: dodecaedro + cubo + tetraedro.
        jobs2=[BatchNetJob(1,'Platônicos / Dodecaedro','Dodecaedro',50.0,1,'fixed_tile'),BatchNetJob(2,'Platônicos / Cubo','Cubo',50.0,1,'fixed_tile'),BatchNetJob(3,'Platônicos / Tetraedro','Tetraedro',50.0,1,'fixed_tile')]
        res2=solve_batch_material_optimizer(jobs2,page='A4',margin_mm=10.0,attempts=100,allow_rotate=True)
        add('lote dodecaedro+cubo+tetraedro não piora páginas', res2.optimized_pages <= res2.baseline_pages, batch_optimizer_payload(res2))
        add('lote dodecaedro+cubo+tetraedro não piora aproveitamento', res2.optimized_utilization_percent + 1e-9 >= res2.baseline_utilization_percent, batch_optimizer_payload(res2))
        # Regressão v25.2.5.1: o caminho visual/exportador precisa importar Rectangle
        # e gerar PDF real em backend headless sem NameError.
        import tempfile, os
        with tempfile.TemporaryDirectory() as td:
            pdf_path=os.path.join(td,'batch_optimizer_render_test.pdf')
            export_batch_optimizer_pdf(res, pdf_path)
            add('exportação PDF do lote renderiza sem Rectangle NameError', os.path.exists(pdf_path) and os.path.getsize(pdf_path)>1000, pdf_path)
    except Exception as exc:
        add('suíte v25.2.5 sem exceção', False, repr(exc))
    return TestReport(results)


APP_NAME='GeoPoly'
VERSION='25.2.5.1'
EDITION='Batch Material Optimizer + PDF/Preview Rectangle Fix + Headless Export Fix + Embedded Johnson Formal Bundle'


def main():
    GeoPolyAppV2525().mainloop()

if False and __name__ == '__main__':
    main()


# ============================================================
# v25.2.5.2 — Export Smoke Test Hardening
# ============================================================
# Camada de confiabilidade. Preserva todos os recursos/menus anteriores e
# acrescenta smoke tests headless para os caminhos principais de saída:
# PDF/SVG da net verificada, PDF/JSON/TXT do otimizador de lote, tamanho
# mínimo dos arquivos e relatório consolidado no run_self_tests().

EDITION_V25252 = 'Export Smoke Test Hardening'


def _v25252_file_ok(path, min_bytes=256):
    try:
        p = Path(path)
        return p.exists() and p.is_file() and p.stat().st_size >= int(min_bytes)
    except Exception:
        return False


def _v25252_current_backend_name():
    try:
        return str(matplotlib.get_backend())
    except Exception:
        return 'unknown'


def run_export_smoke_tests_v25252():
    """Executa smoke tests de exportação sem depender da GUI.

    Retorna dicionário serializável com status por artefato. A suíte usa peças
    pequenas para manter o tempo baixo e força apenas caminhos de renderização
    já usados pelo aplicativo.
    """
    import tempfile, os, json as _json
    out = {
        'version': '25.2.5.2',
        'backend': _v25252_current_backend_name(),
        'headless_expected_agg': (not os.environ.get('DISPLAY') and not os.environ.get('WAYLAND_DISPLAY')),
        'checks': [],
    }
    def add(name, path=None, min_bytes=256, ok=None, detail=''):
        if ok is None:
            ok = _v25252_file_ok(path, min_bytes)
        size = None
        if path:
            try: size = Path(path).stat().st_size
            except Exception: size = None
        out['checks'].append({'name': name, 'ok': bool(ok), 'path': str(path) if path else '', 'size_bytes': size, 'min_bytes': int(min_bytes), 'detail': str(detail)})

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        # 1-2. PDF/SVG da net verificada.
        try:
            poly = _v252_catalog_poly('Platônicos / Cubo')
            cert = search_certified_net(poly, attempts=60, page='A4', scale_mm=30.0, margin_mm=10.0, tab_frac=0.18, max_seconds=6.0)
            nest = solve_certified_nesting(poly, cert, page='A4', scale_mm=30.0, margin_mm=10.0, allow_rotate=True, attempts=60, page_policy='auto')
            pdf = td / 'certified_net_smoke.pdf'
            svg = td / 'certified_net_smoke.svg'
            export_certified_layout_pdf(poly, cert, nest, pdf, 'Smoke PDF — net verificada')
            export_certified_layout_svg(poly, cert, nest, svg, 'Smoke SVG — net verificada')
            add('PDF da net verificada renderiza', pdf, 1000)
            add('SVG da net verificada renderiza', svg, 500)
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
            pdf = td / 'batch_optimizer_smoke.pdf'
            jsn = td / 'batch_optimizer_smoke.json'
            txt = td / 'batch_optimizer_smoke.txt'
            export_batch_optimizer_pdf(res, pdf, 'Smoke PDF — lote')
            export_batch_optimizer_json(res, jsn)
            txt.write_text(batch_optimizer_report(res), encoding='utf-8')
            add('PDF do lote renderiza', pdf, 1000)
            add('JSON do lote exporta', jsn, 500)
            add('TXT/relatório do lote exporta', txt, 500)
            try:
                _json.loads(jsn.read_text(encoding='utf-8'))
                add('JSON do lote é parseável', ok=True)
            except Exception as exc:
                add('JSON do lote é parseável', ok=False, detail=repr(exc))
        except Exception as exc:
            add('PDF/JSON/TXT do lote sem exceção', ok=False, detail=repr(exc))

        # 7. Backend Agg garantido em CLI/headless.
        backend = _v25252_current_backend_name().lower()
        if out['headless_expected_agg']:
            add('backend Agg em ambiente headless', ok=('agg' in backend), detail=_v25252_current_backend_name())
        else:
            add('backend Matplotlib disponível', ok=(backend != 'unknown'), detail=_v25252_current_backend_name())

    out['passed'] = sum(1 for c in out['checks'] if c['ok'])
    out['total'] = len(out['checks'])
    out['ok'] = (out['passed'] == out['total'])
    return out


def export_smoke_test_report_v25252(smoke=None):
    smoke = smoke or run_export_smoke_tests_v25252()
    lines = []
    lines.append('GeoPoly v25.2.5.2 — Export Smoke Test Hardening')
    lines.append(f'Backend Matplotlib: {smoke.get("backend", "unknown")}')
    lines.append(f'Resultado: {smoke.get("passed", 0)}/{smoke.get("total", 0)} smoke tests OK')
    lines.append('')
    for c in smoke.get('checks', []):
        mark = 'OK' if c.get('ok') else 'FALHA'
        size = c.get('size_bytes')
        size_s = 'n/a' if size is None else f'{size} bytes'
        lines.append(f'[{mark}] {c.get("name", "")}: {size_s}')
        if c.get('detail') and not c.get('ok'):
            lines.append(f'      detalhe: {c.get("detail")}')
    return '\n'.join(lines)


_run_self_tests_before_v25252 = run_self_tests

def run_self_tests():
    rep = _run_self_tests_before_v25252()
    results = list(rep.results)
    def add(name, ok, detail=''):
        results.append(TestCaseResult('v25.2.5.2 / ' + name, bool(ok), '' if ok else str(detail)))
    try:
        smoke = run_export_smoke_tests_v25252()
        add('smoke tests de exportação executam', smoke['total'] >= 6, export_smoke_test_report_v25252(smoke))
        add('PDF da net verificada headless', any(c['name']=='PDF da net verificada renderiza' and c['ok'] for c in smoke['checks']), export_smoke_test_report_v25252(smoke))
        add('SVG da net verificada headless', any(c['name']=='SVG da net verificada renderiza' and c['ok'] for c in smoke['checks']), export_smoke_test_report_v25252(smoke))
        add('PDF do lote headless', any(c['name']=='PDF do lote renderiza' and c['ok'] for c in smoke['checks']), export_smoke_test_report_v25252(smoke))
        add('JSON do lote headless', any(c['name']=='JSON do lote exporta' and c['ok'] for c in smoke['checks']), export_smoke_test_report_v25252(smoke))
        add('TXT/relatório do lote headless', any(c['name']=='TXT/relatório do lote exporta' and c['ok'] for c in smoke['checks']), export_smoke_test_report_v25252(smoke))
        add('tamanhos mínimos dos arquivos exportados', smoke.get('ok', False), export_smoke_test_report_v25252(smoke))
        backend = _v25252_current_backend_name().lower()
        if not os.environ.get('DISPLAY') and not os.environ.get('WAYLAND_DISPLAY'):
            add('backend Agg garantido em headless', 'agg' in backend, _v25252_current_backend_name())
        else:
            add('backend gráfico/headless selecionado sem erro', backend != 'unknown', _v25252_current_backend_name())
        add('relatório de smoke tests disponível', 'Smoke Test Hardening' in export_smoke_test_report_v25252(smoke), export_smoke_test_report_v25252(smoke))
    except Exception as exc:
        add('suíte v25.2.5.2 sem exceção', False, repr(exc))
    return TestReport(results)


APP_NAME='GeoPoly'
VERSION='25.2.5.2'
EDITION='Export Smoke Test Hardening + Batch Material Optimizer + Headless Export Fix + Embedded Johnson Formal Bundle'


def main():
    GeoPolyAppV2525().mainloop()

if False and __name__ == '__main__':
    main()




# v27.2f: explicit export list so internal star imports preserve historical
# single-underscore helper symbols without using wholesale update calls.
__all__ = [k for k in globals() if not k.startswith('__')]
