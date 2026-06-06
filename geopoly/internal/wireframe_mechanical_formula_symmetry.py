"""GeoPoly v27 internal module: Mechanical wireframe refinements, formula/symmetry/OFF-related late additions."""
# v27.2f: named internal dependency import.
# Wildcard imports were removed to improve static analysis.
# v27.2f: named internal dependency imports; no wildcard imports.
from .printable_nets import (
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
    _RUN_SELF_TESTS_V2505_BASE,
)





# ============================================================
# v25.0.6 — WIREFRAME KIT MECHANICAL REFINEMENT, PURE PYTHON
# ============================================================
# Evolução conservadora sobre v25.0.5:
# - mantém todos os menus e funcionalidades anteriores;
# - fortalece o Wireframe Kit sem OpenSCAD/CadQuery;
# - adiciona folgas por material, colisão de pinos, códigos de cor/número,
#   orientação de impressão, sequência de montagem e exportação por tipo.

APP_NAME = "GeoPoly"
VERSION = "25.0.6"
EDITION = "Wireframe Mechanical Refinement — Pure Python"

_WF_MATERIAL_PRESETS = {
    "PLA": {
        "clearance_mm": 0.20,
        "description": "PLA: boa rigidez; folga típica 0,15–0,25 mm para encaixe manual.",
        "print_note": "Evitar encaixe excessivamente justo; PLA trinca antes de deformar.",
    },
    "PETG": {
        "clearance_mm": 0.30,
        "description": "PETG: mais tenaz e levemente flexível; folga típica 0,25–0,40 mm.",
        "print_note": "Boa escolha para juntas; pode formar fios e exige retração bem ajustada.",
    },
    "ABS": {
        "clearance_mm": 0.35,
        "description": "ABS/ASA: maior retração; folga típica 0,30–0,50 mm e ambiente controlado.",
        "print_note": "Considerar contração dimensional e empenamento em peças longas.",
    },
    "TPU": {
        "clearance_mm": 0.10,
        "description": "TPU: flexível; pode usar folga menor, mas hastes muito finas deformam.",
        "print_note": "Útil para juntas flexíveis; imprimir devagar.",
    },
    "Manual": {
        "clearance_mm": None,
        "description": "Manual: usa a folga digitada pelo usuário.",
        "print_note": "Faça corpo de prova de encaixe antes do kit completo.",
    },
}

_WF_COLOR_PALETTE = [
    ("vermelho", "#e41a1c"), ("azul", "#377eb8"), ("verde", "#4daf4a"),
    ("roxo", "#984ea3"), ("laranja", "#ff7f00"), ("amarelo", "#ffd92f"),
    ("marrom", "#a65628"), ("rosa", "#f781bf"), ("cinza", "#999999"),
    ("ciano", "#00bfc4"), ("oliva", "#8da000"), ("preto", "#333333"),
]


def _wf_material_name(params):
    return str(getattr(params, 'material', 'PLA') or 'PLA')


def _wf_material_profile(params):
    return _WF_MATERIAL_PRESETS.get(_wf_material_name(params), _WF_MATERIAL_PRESETS['Manual'])


def _wf_with_recommended_clearance(params):
    material = _wf_material_name(params)
    prof = _WF_MATERIAL_PRESETS.get(material, _WF_MATERIAL_PRESETS['Manual'])
    rec = prof.get('clearance_mm')
    if rec is not None and bool(getattr(params, 'auto_material_clearance', False)):
        params.clearance_mm = float(rec)
    return params


def _wf_type_color(type_index):
    name, hexv = _WF_COLOR_PALETTE[(int(type_index)-1) % len(_WF_COLOR_PALETTE)]
    return {"index": int(type_index), "name": name, "hex": hexv, "tactile_marker_rings": int(type_index)}


def _wf_centerline_collision_threshold_deg(params):
    R = max(float(params.joint_radius_mm), EPS)
    # Critério conservador na saída do núcleo da junta:
    # separação entre eixos = 2 R sin(theta/2). Exigimos espaço para dois pinos
    # mais uma pequena folga para parede/ponte de material.
    required = 2.0 * float(params.pin_radius_mm) + float(params.clearance_mm)
    ratio = min(1.0, max(0.0, required / (2.0 * R)))
    return math.degrees(2.0 * math.asin(ratio))


def wireframe_connector_collision_report(poly, params: WireframeParams):
    params = _wf_with_recommended_clearance(params)
    threshold = _wf_centerline_collision_threshold_deg(params)
    groups = wireframe_joint_groups(poly, params)
    reports = []
    global_pairs = []
    for gi, g in enumerate(groups, start=1):
        dirs = [np.array(d, dtype=float) for d in g['directions']]
        pairs = []
        min_angle = None
        for i in range(len(dirs)):
            for j in range(i+1, len(dirs)):
                c = float(np.clip(np.dot(dirs[i], dirs[j]), -1.0, 1.0))
                ang = math.degrees(math.acos(c))
                if min_angle is None or ang < min_angle:
                    min_angle = ang
                clearance_at_exit = 2.0 * params.joint_radius_mm * math.sin(math.radians(ang) / 2.0) - 2.0 * params.pin_radius_mm
                risky = ang < threshold
                rec = {
                    'joint_type': g['type'],
                    'local_connector_pair': [i+1, j+1],
                    'angle_deg': float(ang),
                    'threshold_deg': float(threshold),
                    'estimated_clearance_at_joint_exit_mm': float(clearance_at_exit),
                    'risky': bool(risky),
                }
                if risky:
                    pairs.append(rec); global_pairs.append(rec)
        reports.append({
            'joint_type': g['type'],
            'count': int(g['count']),
            'valence': int(g['valence']),
            'min_angle_deg': float(min_angle) if min_angle is not None else None,
            'threshold_deg': float(threshold),
            'collision_pairs': pairs,
            'ok': bool(len(pairs) == 0),
        })
    return {
        'threshold_deg': float(threshold),
        'total_risky_pairs': int(len(global_pairs)),
        'ok': bool(len(global_pairs) == 0),
        'joint_reports': reports,
        'risky_pairs': global_pairs,
        'criterion': '2 R_joint sin(theta/2) deve exceder aproximadamente 2 r_pin + folga.',
    }


def _wf_edge_type_map(poly, params):
    mp = {}
    for g in wireframe_edge_groups(poly, params):
        for e in g['edges']:
            mp[tuple(sorted(e))] = g['type']
    return mp


def _wf_joint_type_map(poly, params):
    mp = {}
    for g in wireframe_joint_groups(poly, params):
        for vi in g['vertices']:
            mp[int(vi)] = g['type']
    return mp


def wireframe_assembly_sequence(poly, params: WireframeParams):
    e_type = _wf_edge_type_map(poly, params)
    j_type = _wf_joint_type_map(poly, params)
    adj = defaultdict(list)
    for a, b in poly.edges():
        adj[a].append(b); adj[b].append(a)
    if not adj:
        return []
    start = min(adj)
    visited = {start}
    q = deque([start])
    steps = []
    step_id = 1
    used_edges = set()
    while q:
        u = q.popleft()
        for v in sorted(adj[u]):
            e = tuple(sorted((u, v)))
            if e in used_edges:
                continue
            if v not in visited:
                used_edges.add(e)
                visited.add(v); q.append(v)
                steps.append({
                    'step': step_id,
                    'phase': 'estrutura principal',
                    'action': f'Conectar V{u+1} ({j_type.get(u,"J?")}) a V{v+1} ({j_type.get(v,"J?")}) com haste {e_type.get(e,"H?")}.',
                    'edge': [int(u), int(v)],
                    'rod_type': e_type.get(e, 'H?'),
                    'joint_types': [j_type.get(u, 'J?'), j_type.get(v, 'J?')],
                })
                step_id += 1
    # Fechamentos/ciclos após árvore de montagem.
    for a, b in poly.edges():
        e = tuple(sorted((a, b)))
        if e in used_edges:
            continue
        steps.append({
            'step': step_id,
            'phase': 'fechamento de ciclos',
            'action': f'Fechar ciclo conectando V{a+1} ({j_type.get(a,"J?")}) a V{b+1} ({j_type.get(b,"J?")}) com haste {e_type.get(e,"H?")}.',
            'edge': [int(a), int(b)],
            'rod_type': e_type.get(e, 'H?'),
            'joint_types': [j_type.get(a, 'J?'), j_type.get(b, 'J?')],
        })
        step_id += 1
    return steps


def wireframe_print_orientation_report(poly, params: WireframeParams):
    rods = []
    for idx, g in enumerate(wireframe_edge_groups(poly, params), start=1):
        rods.append({
            'type': g['type'],
            'count': int(g['count']),
            'orientation': 'Deitar no leito, eixo longitudinal paralelo a X ou Y.',
            'reason': 'A resistência à tração/flexão melhora quando as camadas não se empilham ao longo do comprimento.',
            'supports': 'não deve precisar de suporte se a haste tubular estiver bem apoiada.',
            'suggested_color': _wf_type_color(idx),
        })
    joints = []
    for idx, g in enumerate(wireframe_joint_groups(poly, params), start=1):
        joints.append({
            'type': g['type'],
            'count': int(g['count']),
            'orientation': 'Apoiar a junta pelo lado com menor interferência entre pinos; se necessário, usar brim e suporte leve.',
            'reason': 'Juntas com pinos inclinados podem criar balanços; priorizar estabilidade da base e qualidade dos pinos.',
            'supports': 'provável em juntas de alta valência ou com pinos muito inclinados.',
            'suggested_color': _wf_type_color(idx),
        })
    return {'rods': rods, 'joints': joints}


# Guardamos referências da malha original para composição.
_WF_BASE_MESH_TUBE_ALONG_X = mesh_tube_along_x
_WF_BASE_MESH_JOINT_TYPE = mesh_joint_type
_WF_BASE_EXPORT_ZIP = export_wireframe_kit_zip


def _wf_mesh_marker_rings_along_x(length, outer_radius, type_index, segments=24):
    meshes = []
    n = max(1, min(int(type_index), 9))
    width = max(0.35, 0.22 * outer_radius)
    gap = max(0.45, 0.28 * outer_radius)
    total = n * width + (n - 1) * gap
    start = min(max(outer_radius * 1.5, length * 0.12), max(outer_radius * 1.5, length * 0.5 - total * 0.5))
    for k in range(n):
        x0 = start + k * (width + gap)
        if x0 + width > length - outer_radius:
            break
        v, f = _WF_BASE_MESH_TUBE_ALONG_X(width, outer_radius * 1.22, outer_radius * 0.98, segments)
        v, f = transform_mesh(v, f, t=[x0, 0, 0])
        meshes.append((v, f))
    return combine_meshes(meshes) if meshes else ([], [])


def mesh_rod_type(length_mm, params: WireframeParams, type_index=1):
    """Haste tubular real por malha, com marcação tátil por anéis.

    A haste é um tubo em torno do eixo X, já com raio interno para receber os
    pinos da junta. Os anéis elevados codificam o tipo H1, H2, ... sem exigir
    texto 3D nem biblioteca CAD externa.
    """
    params = _wf_with_recommended_clearance(params)
    base = _WF_BASE_MESH_TUBE_ALONG_X(length_mm, params.rod_radius_mm, params.pin_radius_mm + params.clearance_mm, params.cyl_segments)
    rings = _wf_mesh_marker_rings_along_x(max(float(length_mm), EPS), float(params.rod_radius_mm), int(type_index), int(params.cyl_segments))
    return combine_meshes([base, rings])


def _wf_mesh_pin_collar(direction, params: WireframeParams):
    d = _wf_norm(direction)
    R = _rotation_from_x_to_dir(d)
    collar_len = max(0.75, min(2.5, 0.22 * params.pin_length_mm))
    collar_radius = max(params.pin_radius_mm * 1.20, params.pin_radius_mm + 0.35)
    x0 = params.joint_radius_mm * 0.60
    v, f = mesh_cylinder_between([x0, 0, 0], [x0 + collar_len, 0, 0], collar_radius, params.cyl_segments, True)
    return transform_mesh(v, f, R=R, t=[0, 0, 0])


def _wf_mesh_joint_marker_bumps(type_index, params: WireframeParams):
    meshes = []
    n = max(1, min(int(type_index), 9))
    # Pequenas saliências no hemisfério superior para identificação tátil do tipo de junta.
    bump_r = max(0.45, 0.11 * params.joint_radius_mm)
    ring_r = params.joint_radius_mm * 0.72
    z = params.joint_radius_mm * 0.72
    for k in range(n):
        a = 2 * math.pi * k / n
        c = [ring_r * math.cos(a), ring_r * math.sin(a), z]
        meshes.append(mesh_uv_sphere(c, bump_r, max(8, int(params.sphere_segments)//2)))
    return combine_meshes(meshes) if meshes else ([], [])


def mesh_joint_type(directions, params: WireframeParams, type_index=1):
    """Junta imprimível simplificada: núcleo facetado + pinos + colares + marcas táteis."""
    params = _wf_with_recommended_clearance(params)
    meshes = [mesh_uv_sphere((0, 0, 0), params.joint_radius_mm, params.sphere_segments)]
    for d in directions:
        d = _wf_norm(d)
        p0 = d * (params.joint_radius_mm * 0.30)
        p1 = d * (params.joint_radius_mm + params.pin_length_mm)
        meshes.append(mesh_cylinder_between(p0, p1, params.pin_radius_mm, params.cyl_segments, True))
        meshes.append(_wf_mesh_pin_collar(d, params))
    meshes.append(_wf_mesh_joint_marker_bumps(type_index, params))
    return combine_meshes(meshes)


def mesh_rod_groups_display(poly, params: WireframeParams):
    meshes = []
    y = 0.0
    for idx, g in enumerate(wireframe_edge_groups(poly, params), start=1):
        v, f = mesh_rod_type(g['rod_body_length_mm'], params, type_index=idx)
        v2, f2 = transform_mesh(v, f, t=[0, y, 0])
        meshes.append((v2, f2))
        y += 4 * params.rod_radius_mm + 7
    return combine_meshes(meshes)


def mesh_joint_groups_display(poly, params: WireframeParams):
    meshes = []
    x = 0.0
    for idx, g in enumerate(wireframe_joint_groups(poly, params), start=1):
        v, f = mesh_joint_type(g['directions'], params, type_index=idx)
        v2, f2 = transform_mesh(v, f, t=[x, 0, 0])
        meshes.append((v2, f2))
        x += 2 * (params.joint_radius_mm + params.pin_length_mm) + 10
    return combine_meshes(meshes)


def wireframe_manifest(poly, params: WireframeParams):
    params = _wf_with_recommended_clearance(params)
    edges = wireframe_edge_groups(poly, params)
    joints = wireframe_joint_groups(poly, params)
    collisions = wireframe_connector_collision_report(poly, params)
    orientation = wireframe_print_orientation_report(poly, params)
    sequence = wireframe_assembly_sequence(poly, params)
    warnings = []
    if params.pin_radius_mm + params.clearance_mm >= params.rod_radius_mm:
        warnings.append('Raio interno da haste tubular >= raio externo; aumente o raio externo da haste ou reduza pino/folga.')
    wall = params.rod_radius_mm - (params.pin_radius_mm + params.clearance_mm)
    if wall < 0.60:
        warnings.append(f'Parede da haste tubular pequena ({wall:.2f} mm). Para FDM, considerar >= 0,8–1,2 mm.')
    for g in edges:
        if g['rod_body_length_mm'] <= 1.0:
            warnings.append(f'{g["type"]}: comprimento útil da haste muito curto para a profundidade de encaixe configurada.')
    if not collisions['ok']:
        warnings.append(f'Possível colisão/fusão de pinos em juntas: {collisions["total_risky_pairs"]} par(es) arriscado(s).')
    material = _wf_material_name(params)
    mat_profile = _wf_material_profile(params)
    rod_groups = []
    for idx, g in enumerate(edges, start=1):
        d = {k: v for k, v in g.items() if k not in ('edges', 'lengths_mm')}
        d['color_code'] = _wf_type_color(idx)
        d['stl_file_hint'] = f'haste_{g["type"]}_{g["count"]}x.stl'
        d['print_orientation'] = orientation['rods'][idx-1]
        d['wall_thickness_mm'] = float(wall)
        rod_groups.append(d)
    joint_groups = []
    for idx, g in enumerate(joints, start=1):
        d = {k: (v if k != 'directions' else [np.array(x).round(6).tolist() for x in v]) for k, v in g.items() if k != 'vertices'}
        d['vertices'] = [int(v) for v in g['vertices']]
        d['color_code'] = _wf_type_color(idx)
        d['stl_file_hint'] = f'junta_{g["type"]}_{g["count"]}x.stl'
        d['print_orientation'] = orientation['joints'][idx-1]
        # localiza relatório de colisão correspondente
        d['collision_check'] = next((r for r in collisions['joint_reports'] if r['joint_type'] == g['type']), {})
        joint_groups.append(d)
    params_payload = asdict(params)
    params_payload['material'] = material
    params_payload['material_profile'] = mat_profile
    params_payload['auto_material_clearance'] = bool(getattr(params, 'auto_material_clearance', False))
    manifest = {
        'app': APP_NAME,
        'version': VERSION,
        'edition': 'Wireframe Mechanical Refinement sem OpenSCAD/CadQuery',
        'solid': poly.name,
        'family': poly.family,
        'geometry_status': getattr(poly.meta, 'status', 'unknown'),
        'parameters': params_payload,
        'counts': {'vertices': len(poly.vertices), 'edges': len(poly.edges()), 'faces': len(poly.faces), 'rod_types': len(edges), 'joint_types': len(joints)},
        'rod_groups': rod_groups,
        'joint_groups': joint_groups,
        'connector_collision_report': collisions,
        'print_orientation_report': orientation,
        'assembly_sequence': sequence,
        'warnings': warnings,
        'notes': [
            'Versão sem OpenSCAD/CadQuery: todas as peças são malhas trianguladas diretas em Python.',
            'Hastes tubulares recebem pinos das juntas; o raio interno já inclui folga.',
            'Cores não são gravadas em STL ASCII; o código de cor aparece no manifesto e nos nomes/tipos. Marcadores táteis por anéis/saliências foram adicionados às malhas.',
            'Validar tolerâncias no fatiador e imprimir peça de teste antes do kit completo.',
        ],
    }
    return manifest


def wireframe_report(poly, params: WireframeParams):
    m = wireframe_manifest(poly, params)
    lines = []
    lines.append(f'Wireframe Kit Lab mecânico — {poly.name}')
    lines.append('=' * max(30, len(lines[0])))
    lines.append(f'Família: {poly.family}')
    lines.append(f'Status geométrico: {m["geometry_status"]}')
    lines.append('')
    lines.append('Material e tolerância')
    lines.append('-' * 40)
    mat = m['parameters'].get('material', 'PLA')
    lines.append(f'Material: {mat}')
    lines.append(f'Descrição: {m["parameters"].get("material_profile", {}).get("description", "") }')
    lines.append(f'Nota de impressão: {m["parameters"].get("material_profile", {}).get("print_note", "") }')
    lines.append('')
    lines.append('Parâmetros maker')
    lines.append('-' * 40)
    for k, v in m['parameters'].items():
        if k != 'material_profile':
            lines.append(f'{k}: {v}')
    lines.append('')
    lines.append('Hastes por comprimento — tubos reais por malha')
    lines.append('-' * 40)
    for g in m['rod_groups']:
        cc = g['color_code']
        lines.append(f'{g["type"]}: {g["count"]} un.; aresta={g["length_mm"]:.3f} mm; corpo={g["rod_body_length_mm"]:.3f} mm; raio externo={g["tube_outer_radius_mm"]:.3f} mm; raio interno≈{g["tube_inner_radius_mm"]:.3f} mm; parede≈{g["wall_thickness_mm"]:.3f} mm; código={cc["index"]}/{cc["name"]} {cc["hex"]}; marcas táteis={cc["tactile_marker_rings"]}')
    lines.append('')
    lines.append('Juntas por assinatura angular — núcleo + pinos + colares + marcas')
    lines.append('-' * 40)
    for g in m['joint_groups']:
        sig = g['signature']; angles = sig[1]
        preview = ', '.join(f'{a:g}°' for a in angles[:12]) + (' ...' if len(angles) > 12 else '')
        cc = g['color_code']; col = g.get('collision_check', {})
        risk = 'OK' if col.get('ok', True) else f'RISCO: {len(col.get("collision_pairs", []))} par(es)'
        lines.append(f'{g["type"]}: {g["count"]} un.; valência={g["valence"]}; representante=V{g["representative_vertex"]+1}; código={cc["index"]}/{cc["name"]} {cc["hex"]}; marcas={cc["tactile_marker_rings"]}; colisão={risk}; ângulos={preview}')
    lines.append('')
    lines.append('Verificação de colisão/fusão entre pinos')
    lines.append('-' * 40)
    cr = m['connector_collision_report']
    lines.append(f'Limiar angular conservador: {cr["threshold_deg"]:.2f}°')
    lines.append(f'Pares arriscados: {cr["total_risky_pairs"]}')
    if cr['risky_pairs']:
        for rec in cr['risky_pairs'][:20]:
            lines.append(f'- {rec["joint_type"]}, conectores {rec["local_connector_pair"]}: ângulo={rec["angle_deg"]:.2f}°, folga estimada na saída={rec["estimated_clearance_at_joint_exit_mm"]:.2f} mm')
        if len(cr['risky_pairs']) > 20:
            lines.append(f'... mais {len(cr["risky_pairs"])-20} par(es).')
    else:
        lines.append('Nenhum par de pinos abaixo do limiar conservador.')
    lines.append('')
    lines.append('Orientação de impressão sugerida')
    lines.append('-' * 40)
    for r in m['print_orientation_report']['rods']:
        lines.append(f'{r["type"]}: {r["orientation"]} Suporte: {r["supports"]}')
    for j in m['print_orientation_report']['joints']:
        lines.append(f'{j["type"]}: {j["orientation"]} Suporte: {j["supports"]}')
    lines.append('')
    lines.append('Sequência de montagem sugerida')
    lines.append('-' * 40)
    for st in m['assembly_sequence'][:80]:
        lines.append(f'{st["step"]:02d}. [{st["phase"]}] {st["action"]}')
    if len(m['assembly_sequence']) > 80:
        lines.append(f'... mais {len(m["assembly_sequence"])-80} etapa(s).')
    if m['warnings']:
        lines.append(''); lines.append('Avisos'); lines.append('-' * 40)
        lines.extend('- ' + w for w in m['warnings'])
    lines.append('')
    lines.append('Observação de escopo')
    lines.append('-' * 40)
    lines.append('Sem booleanas complexas: as peças STL são malhas trianguladas diretas. Juntas com furos fêmea reais continuam sendo melhor tratadas por CadQuery opcional, mas esta versão gera tubos, pinos, colares e marcadores diretamente em Python.')
    return '\n'.join(lines)


def export_wireframe_parts_folder(poly, params: WireframeParams, folder_path):
    folder = Path(folder_path)
    folder.mkdir(parents=True, exist_ok=True)
    base = safe_name(poly.name)
    files = []
    # Um STL por tipo de haste.
    for idx, g in enumerate(wireframe_edge_groups(poly, params), start=1):
        v, f = mesh_rod_type(g['rod_body_length_mm'], params, type_index=idx)
        p = folder / f'{base}_haste_{g["type"]}_{g["count"]}x_codigo_{idx}.stl'
        write_mesh_stl_ascii(v, f, p, f'haste_{g["type"]}')
        files.append(str(p))
    # Um STL por tipo de junta.
    for idx, g in enumerate(wireframe_joint_groups(poly, params), start=1):
        v, f = mesh_joint_type(g['directions'], params, type_index=idx)
        p = folder / f'{base}_junta_{g["type"]}_{g["count"]}x_codigo_{idx}.stl'
        write_mesh_stl_ascii(v, f, p, f'junta_{g["type"]}')
        files.append(str(p))
    # Também salva manifesto e relatório.
    manifest = wireframe_manifest(poly, params)
    p = folder / f'{base}_manifesto_wireframe_mecanico.json'
    p.write_text(json.dumps(manifest, indent=2, ensure_ascii=False, default=str), encoding='utf-8')
    files.append(str(p))
    p = folder / f'{base}_relatorio_montagem_wireframe_mecanico.txt'
    p.write_text(wireframe_report(poly, params), encoding='utf-8')
    files.append(str(p))
    return files


def export_wireframe_kit_zip(poly, params: WireframeParams, zip_path):
    zip_path = Path(zip_path)
    tmp = Path(tempfile.mkdtemp(prefix='geopoly_wireframe_mech_'))
    files = []
    base = safe_name(poly.name)
    try:
        v, f = mesh_wireframe_full(poly, params)
        p = tmp / f'{base}_wireframe_completo.stl'
        write_mesh_stl_ascii(v, f, p, base + '_wireframe')
        files.append(p)
        for file in export_wireframe_parts_folder(poly, params, tmp):
            files.append(Path(file))
        # Arquivos de compatibilidade com testes/fluxos da v25.0: nomes genéricos antigos.
        compat_manifest = tmp / f'{base}_manifesto_wireframe.json'
        compat_manifest.write_text(json.dumps(wireframe_manifest(poly, params), indent=2, ensure_ascii=False, default=str), encoding='utf-8')
        files.append(compat_manifest)
        compat_report = tmp / f'{base}_relatorio_montagem.txt'
        compat_report.write_text(wireframe_report(poly, params), encoding='utf-8')
        files.append(compat_report)
        with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for file in files:
                z.write(file, arcname=file.name)
    finally:
        for file in tmp.glob('*'):
            try: file.unlink()
            except Exception: pass
        try: tmp.rmdir()
        except Exception: pass
    return zip_path


_RUN_SELF_TESTS_V2506_BASE = run_self_tests


def run_self_tests():
    base = _RUN_SELF_TESTS_V2506_BASE()
    results = list(base.results) if isinstance(base, TestReport) else []
    def add(name, ok, detail=''):
        results.append(TestCaseResult(str(name), bool(ok), '' if ok else str(detail)))
    try:
        cube = CATALOG['Platônicos / Cubo ou Hexaedro'].build()
        params = WireframeParams(edge_scale_mm=40.0)
        params.material = 'PLA'; params.auto_material_clearance = True
        manifest = wireframe_manifest(cube, params)
        add('v25.0.6 material preset aplicado', manifest['parameters']['material'] == 'PLA', manifest['parameters'])
        add('v25.0.6 manifesto tem colisão de pinos', 'connector_collision_report' in manifest, manifest.keys())
        add('v25.0.6 manifesto tem sequência montagem', len(manifest.get('assembly_sequence', [])) == len(cube.edges()), len(manifest.get('assembly_sequence', [])))
        add('v25.0.6 manifesto tem orientação impressão', 'print_orientation_report' in manifest, manifest.keys())
        add('v25.0.6 hastes têm código cor/número', all('color_code' in g for g in manifest['rod_groups']), manifest['rod_groups'][:1])
        add('v25.0.6 juntas têm checagem colisão', all('collision_check' in g for g in manifest['joint_groups']), manifest['joint_groups'][:1])
        v, f = mesh_rod_type(25.0, params, type_index=3)
        add('v25.0.6 haste tubular com marcadores gera malha', len(v) > 0 and len(f) > 0, (len(v), len(f)))
        jg = wireframe_joint_groups(cube, params)[0]
        vj, fj = mesh_joint_type(jg['directions'], params, type_index=2)
        add('v25.0.6 junta com colares/marcadores gera malha', len(vj) > 0 and len(fj) > 0, (len(vj), len(fj)))
        col = wireframe_connector_collision_report(cube, params)
        add('v25.0.6 colisão retorna bool nativo', isinstance(col['ok'], bool), type(col['ok']))
        with tempfile.TemporaryDirectory() as td:
            files = export_wireframe_parts_folder(cube, params, td)
            add('v25.0.6 exporta peças por tipo em pasta', len(files) >= 3 and all(Path(x).exists() for x in files), files[:3])
            z = Path(td) / 'kit.zip'
            export_wireframe_kit_zip(cube, params, z)
            add('v25.0.6 zip mecânico exporta', z.exists() and z.stat().st_size > 0, str(z))
    except Exception as exc:
        add('v25.0.6 exception', False, repr(exc))
    return TestReport(results)


class GeoPolyAppV2506(GeoPolyAppV2505):
    def _build_ui(self):
        super()._build_ui()
        # Faixa adicional no Wireframe Kit. Não remove nem altera os menus existentes.
        try:
            adv = ttk.LabelFrame(self.tabwire, text='Wireframe mecânico v25.0.6 — material, colisão, códigos e exportação por tipo', padding=8)
            adv.grid(row=3, column=0, sticky='ew', pady=(6, 0))
            self.wf_material = tk.StringVar(value='PLA')
            self.wf_auto_clearance = tk.BooleanVar(value=False)
            ttk.Label(adv, text='Material:').pack(side='left', padx=(4, 2))
            cb = ttk.Combobox(adv, textvariable=self.wf_material, values=list(_WF_MATERIAL_PRESETS.keys()), width=8, state='readonly')
            cb.pack(side='left', padx=(0, 6)); cb.bind('<<ComboboxSelected>>', lambda e: self._wf_apply_material_and_update(False))
            ttk.Checkbutton(adv, text='Usar folga sugerida do material', variable=self.wf_auto_clearance, command=lambda: self._wf_apply_material_and_update(True)).pack(side='left', padx=4)
            ttk.Button(adv, text='Checar colisão de pinos', command=self.show_wireframe_collision_ui).pack(side='left', padx=4)
            ttk.Button(adv, text='Exportar peças por tipo em pasta', command=self.export_wireframe_parts_folder_ui).pack(side='left', padx=4)
            ttk.Button(adv, text='Manifesto mecânico JSON', command=self.export_wireframe_manifest_ui).pack(side='left', padx=4)
        except Exception:
            pass
    def _wf_apply_material_and_update(self, force_set=False):
        try:
            mat = self.wf_material.get()
            prof = _WF_MATERIAL_PRESETS.get(mat, _WF_MATERIAL_PRESETS['Manual'])
            rec = prof.get('clearance_mm')
            if force_set and rec is not None and hasattr(self, 'wf_clear'):
                self.wf_clear.set(float(rec))
            self.update_wireframe_tab()
        except Exception:
            pass
    def _wf_params(self):
        p = super()._wf_params()
        try:
            p.material = self.wf_material.get() if hasattr(self, 'wf_material') else 'PLA'
            p.auto_material_clearance = bool(self.wf_auto_clearance.get()) if hasattr(self, 'wf_auto_clearance') else False
            _wf_with_recommended_clearance(p)
        except Exception:
            p.material = 'PLA'; p.auto_material_clearance = False
        return p
    def show_wireframe_collision_ui(self):
        if not self.poly:
            return
        try:
            rep = wireframe_connector_collision_report(self.poly, self._wf_params())
            msg = f'Limiar: {rep["threshold_deg"]:.2f}°\nPares arriscados: {rep["total_risky_pairs"]}\nOK: {"sim" if rep["ok"] else "não"}'
            if rep['risky_pairs']:
                msg += '\n\nPrimeiros riscos:\n' + '\n'.join(f'{r["joint_type"]} {r["local_connector_pair"]}: {r["angle_deg"]:.2f}°' for r in rep['risky_pairs'][:8])
            messagebox.showinfo('Checagem de colisão de pinos', msg)
        except Exception as exc:
            messagebox.showerror('Checagem de colisão', str(exc))
    def export_wireframe_parts_folder_ui(self):
        if not self.poly:
            return
        folder = filedialog.askdirectory(title='Escolha a pasta para salvar um STL por tipo de haste/junta')
        if not folder:
            return
        try:
            files = export_wireframe_parts_folder(self.poly, self._wf_params(), folder)
            messagebox.showinfo('Peças por tipo', f'{len(files)} arquivo(s) salvos em:\n{folder}')
        except Exception as exc:
            messagebox.showerror('Exportar peças por tipo', str(exc))
    def export_wireframe_manifest_ui(self):
        if not self.poly:
            return
        path = filedialog.asksaveasfilename(title='Salvar manifesto mecânico JSON', defaultextension='.json', initialfile=safe_name(self.poly.name)+'_wireframe_mecanico.json')
        if not path:
            return
        try:
            Path(path).write_text(json.dumps(wireframe_manifest(self.poly, self._wf_params()), indent=2, ensure_ascii=False, default=str), encoding='utf-8')
            messagebox.showinfo('Manifesto mecânico', f'Arquivo salvo:\n{path}')
        except Exception as exc:
            messagebox.showerror('Manifesto mecânico', str(exc))




# ============================================================
# v25.0.7 — Formula Lab Avançado para licenciatura em matemática
# ============================================================
# Adendo didático sem remoção de menus/features da v25.0.6:
# - novos sólidos: toro, elipsoide, Platônicos e Arquimedianos selecionados;
# - modo aluno: esconde dedução e pede cálculo;
# - exercícios gerados pelos parâmetros atuais;
# - exportação da folha de exercícios em LaTeX e PDF;
# - comparação fórmula exata × malha facetada/procedural;
# - diagramas 2D ampliados e animação simples para cilindro/cone.

APP_NAME = "GeoPoly"
VERSION = "25.0.7"
EDITION = "Formula Lab Avançado + Wireframe Mechanical Refinement"

_FORMULA_PREV_CASES_V2507 = list(FORMULA_LAB_CASES)
_FORMULA_PREV_DEFAULTS_V2507 = dict(FORMULA_DEFAULTS)
_FORMULA_PREV_LABELS_V2507 = dict(FORMULA_PARAM_LABELS)
_formula_lab_compute_base_v2507 = formula_lab_compute
_formula_lab_plot_base_v2507 = formula_lab_plot
_formula_lab_text_base_v2507 = formula_lab_text

FORMULA_ADVANCED_CASES = [
    'Toro circular',
    'Elipsoide triaxial',
    'Tetraedro regular',
    'Octaedro regular',
    'Dodecaedro regular',
    'Icosaedro regular',
    'Cuboctaedro regular',
    'Tetraedro truncado regular',
]
for _case in FORMULA_ADVANCED_CASES:
    if _case not in FORMULA_LAB_CASES:
        FORMULA_LAB_CASES.append(_case)
FORMULA_DEFAULTS.update({
    'Toro circular': {'R': 5.0, 'r': 1.5, 'm': 32, 'rings': 16},
    'Elipsoide triaxial': {'a': 4.0, 'b': 3.0, 'c': 2.0, 'm': 32, 'rings': 16},
    'Tetraedro regular': {'a': 4.0},
    'Octaedro regular': {'a': 4.0},
    'Dodecaedro regular': {'a': 2.0},
    'Icosaedro regular': {'a': 3.0},
    'Cuboctaedro regular': {'a': 3.0},
    'Tetraedro truncado regular': {'a': 3.0},
})
FORMULA_PARAM_LABELS.update({
    'R': 'raio maior R',
    'c': 'semieixo c',
})

_PLATONIC_ARCH_FORMULAS = {
    'Tetraedro regular': {
        'catalog_key': 'Platônicos / Tetraedro',
        'A': lambda a: math.sqrt(3.0)*a*a,
        'V': lambda a: a**3/(6.0*math.sqrt(2.0)),
        'lines': [
            'O tetraedro regular possui 4 faces triangulares equiláteras.',
            'Área de um triângulo equilátero: A_f = (√3/4)a².',
            'Área total: A_T = 4·(√3/4)a² = √3 a².',
            'A altura do tetraedro é h = a√(2/3).',
            'Volume: V = (área da base · altura)/3 = a³/(6√2).',
        ]
    },
    'Octaedro regular': {
        'catalog_key': 'Platônicos / Octaedro',
        'A': lambda a: 2.0*math.sqrt(3.0)*a*a,
        'V': lambda a: math.sqrt(2.0)*a**3/3.0,
        'lines': [
            'O octaedro regular possui 8 faces triangulares equiláteras.',
            'Área total: A_T = 8·(√3/4)a² = 2√3 a².',
            'Ele pode ser visto como duas pirâmides quadradas congruentes unidas pela base.',
            'Volume: V = (√2/3)a³.',
        ]
    },
    'Dodecaedro regular': {
        'catalog_key': 'Platônicos / Dodecaedro',
        'A': lambda a: 3.0*math.sqrt(25.0+10.0*math.sqrt(5.0))*a*a,
        'V': lambda a: (15.0+7.0*math.sqrt(5.0))*a**3/4.0,
        'lines': [
            'O dodecaedro regular possui 12 faces pentagonais regulares.',
            'A área total é 12 vezes a área do pentágono regular de lado a.',
            'Fórmula fechada: A_T = 3√(25+10√5)a².',
            'Volume: V = ((15+7√5)/4)a³.',
        ]
    },
    'Icosaedro regular': {
        'catalog_key': 'Platônicos / Icosaedro',
        'A': lambda a: 5.0*math.sqrt(3.0)*a*a,
        'V': lambda a: 5.0*(3.0+math.sqrt(5.0))*a**3/12.0,
        'lines': [
            'O icosaedro regular possui 20 faces triangulares equiláteras.',
            'Área total: A_T = 20·(√3/4)a² = 5√3 a².',
            'Volume: V = [5(3+√5)/12]a³.',
        ]
    },
    'Cuboctaedro regular': {
        'catalog_key': 'Arquimedianos / Cuboctaedro',
        'A': lambda a: (6.0+2.0*math.sqrt(3.0))*a*a,
        'V': lambda a: 5.0*math.sqrt(2.0)*a**3/3.0,
        'lines': [
            'O cuboctaedro possui 6 faces quadradas e 8 faces triangulares equiláteras.',
            'Área total: A_T = 6a² + 8(√3/4)a² = (6+2√3)a².',
            'O volume pode ser obtido por decomposição em pirâmides/tetraedros congruentes.',
            'Fórmula fechada: V = (5√2/3)a³.',
        ]
    },
    'Tetraedro truncado regular': {
        'catalog_key': 'Arquimedianos / Tetraedro truncado',
        'A': lambda a: 7.0*math.sqrt(3.0)*a*a,
        'V': lambda a: 23.0*math.sqrt(2.0)*a**3/12.0,
        'lines': [
            'O tetraedro truncado possui 4 triângulos equiláteros e 4 hexágonos regulares.',
            'Área de um hexágono regular: A_hex = (3√3/2)a².',
            'Área total: 4(√3/4)a² + 4(3√3/2)a² = 7√3 a².',
            'Volume: V = (23√2/12)a³.',
        ]
    },
}

def _mesh_torus_formula(M, N, R, r):
    M = int(max(8, round(M))); N = int(max(6, round(N)))
    verts=[]
    for i in range(M):
        u=2*math.pi*i/M
        for j in range(N):
            v=2*math.pi*j/N
            x=(R+r*math.cos(v))*math.cos(u)
            y=(R+r*math.cos(v))*math.sin(u)
            z=r*math.sin(v)
            verts.append([x,y,z])
    faces=[]
    for i in range(M):
        for j in range(N):
            faces.append([i*N+j, ((i+1)%M)*N+j, ((i+1)%M)*N+(j+1)%N, i*N+(j+1)%N])
    return verts, faces

def _mesh_ellipsoid_formula(M, rings, a, b, c):
    verts, faces = _mesh_sphere(M, rings, 1.0)
    verts = [[a*x, b*y, c*z] for x,y,z in verts]
    return verts, faces

def _scaled_catalog_mesh_for_edge(catalog_key: str, edge_a: float):
    poly = CATALOG[catalog_key].build()
    lengths = poly.edge_lengths()
    L = float(np.median(lengths)) if lengths else 1.0
    scale = float(edge_a) / max(L, 1e-12)
    return (poly.vertices*scale).tolist(), [list(f) for f in poly.faces]

def _formula_mesh_values(vertices, faces):
    return _poly_area_3d(vertices, faces), _poly_volume_3d(vertices, faces)

def _ellipsoid_area_knud_thomsen(a,b,c):
    # Aproximação clássica de Knud Thomsen, p≈1.6075.
    p = 1.6075
    return 4.0*math.pi*((a**p*b**p + a**p*c**p + b**p*c**p)/3.0)**(1.0/p)

def formula_lab_compute(case, params):
    if case in _FORMULA_PREV_DEFAULTS_V2507 and case not in FORMULA_ADVANCED_CASES:
        return _formula_lab_compute_base_v2507(case, params)
    p = {k: float(v) for k, v in params.items()}
    if case == 'Toro circular':
        R=max(p.get('R',5.0),1e-9); r=max(p.get('r',1.5),1e-9); m=int(max(8,round(p.get('m',32)))); rings=int(max(6,round(p.get('rings',16))))
        A=4*math.pi*math.pi*R*r; V=2*math.pi*math.pi*R*r*r
        verts, faces = _mesh_torus_formula(m, rings, R, r)
        lines=[
            'O toro circular é obtido pela rotação de um círculo de raio r cujo centro percorre uma circunferência de raio R.',
            'Pelo teorema de Pappus-Guldinus, a área da superfície é área/contorno gerador multiplicado pelo caminho do centroide.',
            'Área: A = (comprimento do círculo gerador)·(caminho do centroide) = (2πr)(2πR) = 4π²Rr.',
            'Volume: V = (área do disco gerador)·(caminho do centroide) = (πr²)(2πR) = 2π²Rr².',
            'A malha facetada usa m divisões ao redor do eixo maior e rings divisões no círculo gerador.',
        ]
        values={'Área total':A, 'Volume':V, 'Raio maior R':R, 'Raio menor r':r}
    elif case == 'Elipsoide triaxial':
        a=max(p.get('a',4.0),1e-9); b=max(p.get('b',3.0),1e-9); c=max(p.get('c',2.0),1e-9); m=int(max(8,round(p.get('m',32)))); rings=int(max(4,round(p.get('rings',16))))
        A=_ellipsoid_area_knud_thomsen(a,b,c); V=4*math.pi*a*b*c/3.0
        verts, faces = _mesh_ellipsoid_formula(m, rings, a, b, c)
        lines=[
            'O elipsoide triaxial é dado por x²/a² + y²/b² + z²/c² = 1.',
            'O volume vem por mudança de escala da esfera unitária: V = (4π/3)abc.',
            'A área superficial não possui fórmula elementar simples em geral.',
            'Usa-se aqui a aproximação de Knud Thomsen: A ≈ 4π[(aᵖbᵖ+aᵖcᵖ+bᵖcᵖ)/3]^(1/p), p≈1,6075.',
            'A malha facetada é uma esfera latitude-longitude escalada pelos semieixos.',
        ]
        values={'Área total aproximada':A, 'Área total':A, 'Volume':V, 'Semieixo a':a, 'Semieixo b':b, 'Semieixo c':c}
    elif case in _PLATONIC_ARCH_FORMULAS:
        a=max(p.get('a',3.0),1e-9)
        info=_PLATONIC_ARCH_FORMULAS[case]
        A=info['A'](a); V=info['V'](a)
        verts, faces = _scaled_catalog_mesh_for_edge(info['catalog_key'], a)
        lines=list(info['lines']) + ['A comparação com a malha usa a geometria canônica do catálogo escalada para aresta a.']
        values={'Aresta':a, 'Área total':A, 'Volume':V}
    else:
        raise ValueError(f'Caso de fórmula desconhecido: {case}')
    mesh_area, mesh_vol = _formula_mesh_values(verts, faces)
    analytic_total = values.get('Área total', values.get('Área total aproximada'))
    analytic_vol = values.get('Volume')
    err_area = None if not analytic_total else 100*(mesh_area-analytic_total)/analytic_total
    err_vol = None if not analytic_vol else 100*(mesh_vol-analytic_vol)/analytic_vol
    return {'case':case,'params':p,'values':values,'derivation':lines,'mesh_area':mesh_area,'mesh_volume':mesh_vol,'area_error_pct':err_area,'volume_error_pct':err_vol,'vertices':verts,'faces':faces}

def formula_lab_text(result, hide_formula=False):
    if not hide_formula:
        return _formula_lab_text_base_v2507(result) if result['case'] not in FORMULA_ADVANCED_CASES else _formula_lab_text_rich(result)
    return formula_lab_student_prompt(result)

def _formula_lab_text_rich(result):
    lines=[f"Formula Lab avançado — {result['case']}", '='*72, '']
    lines.append('Parâmetros:')
    for k,v in result['params'].items(): lines.append(f'  {k} = {v:g}')
    lines.append('')
    lines.append('Dedução didática:')
    for i,line in enumerate(result['derivation'],1): lines.append(f'{i}. {line}')
    lines.append('')
    lines.append('Resultados:')
    for k,v in result['values'].items():
        if isinstance(v,(int,float,np.floating)): lines.append(f'  {k}: {float(v):.8g}')
    lines.append('')
    lines.append('Comparação fórmula × malha:')
    lines.append(f"  Área medida na malha: {result['mesh_area']:.8g}")
    if result['area_error_pct'] is not None: lines.append(f"  Erro relativo de área: {result['area_error_pct']:+.6f}%")
    lines.append(f"  Volume medido na malha: {result['mesh_volume']:.8g}")
    if result['volume_error_pct'] is not None: lines.append(f"  Erro relativo de volume: {result['volume_error_pct']:+.6f}%")
    lines.append('')
    lines.append('Uso didático: peça ao estudante identificar a decomposição geométrica, aplicar a fórmula e comparar com a medição da malha.')
    return '\n'.join(lines)

def formula_lab_student_prompt(result):
    lines=[f"Modo aluno — {result['case']}", '='*72, '']
    lines.append('Dados do problema:')
    for k,v in result['params'].items(): lines.append(f'  {k} = {v:g}')
    lines.append('')
    lines.append('Calcule:')
    for k in result['values']:
        if k.startswith('Área') or k == 'Volume' or k in ('Geratriz','Apótema lateral','Apótema da base'):
            lines.append(f'  {k}: __________________________')
    lines.append('')
    lines.append('Perguntas orientadoras:')
    lines.append('1. Qual figura plana aparece na base ou na seção geradora?')
    lines.append('2. Que grandeza funciona como altura, apótema ou geratriz?')
    lines.append('3. Como a área lateral é formada pela planificação?')
    lines.append('4. Compare seu resultado com a medição da malha facetada.')
    lines.append('')
    lines.append('A fórmula e a solução estão ocultas neste modo.')
    return '\n'.join(lines)

def formula_lab_exercise_sheet_text(result, with_answers=True):
    lines=[f'Folha de exercícios — {result["case"]}', '='*72, '']
    lines.append('Dados:')
    for k,v in result['params'].items(): lines.append(f'  {k} = {v:g}')
    lines.append('')
    lines.append('Questões:')
    lines.append('1. Desenhe a seção, a base ou a planificação lateral relevante.')
    lines.append('2. Identifique apótema, altura ou geratriz quando existirem.')
    lines.append('3. Calcule a área lateral, quando aplicável.')
    lines.append('4. Calcule a área total.')
    lines.append('5. Calcule o volume.')
    lines.append('6. Compare o valor analítico com a área/volume medidos na malha.')
    if with_answers:
        lines.append('')
        lines.append('Gabarito numérico:')
        for k,v in result['values'].items():
            if isinstance(v,(int,float,np.floating)): lines.append(f'  {k}: {float(v):.8g}')
        lines.append(f"  Área da malha: {result['mesh_area']:.8g}")
        lines.append(f"  Volume da malha: {result['mesh_volume']:.8g}")
        if result['area_error_pct'] is not None: lines.append(f"  Erro relativo de área: {result['area_error_pct']:+.6f}%")
        if result['volume_error_pct'] is not None: lines.append(f"  Erro relativo de volume: {result['volume_error_pct']:+.6f}%")
        lines.append('')
        lines.append('Resumo da dedução:')
        for i,line in enumerate(result['derivation'],1): lines.append(f'{i}. {line}')
    return '\n'.join(lines)

def formula_lab_exercise_sheet_latex(result, with_answers=True):
    def esc(s):
        return str(s).replace('\\','\\textbackslash{}').replace('&','\\&').replace('%','\\%').replace('$','\\$').replace('#','\\#').replace('_','\\_').replace('{','\\{').replace('}','\\}')
    lines=[r'\documentclass[12pt,a4paper]{article}',r'\usepackage[utf8]{inputenc}',r'\usepackage[T1]{fontenc}',r'\usepackage[brazil]{babel}',r'\usepackage{amsmath}',r'\usepackage{geometry}',r'\geometry{margin=2cm}',r'\begin{document}']
    lines.append(r'\section*{Folha de exercícios --- '+esc(result['case'])+'}')
    lines.append(r'\subsection*{Dados}')
    lines.append(r'\begin{itemize}')
    for k,v in result['params'].items(): lines.append(r'\item '+esc(k)+f' = {v:g}')
    lines.append(r'\end{itemize}')
    lines.append(r'\subsection*{Questões}')
    lines.append(r'\begin{enumerate}')
    for q in ['Desenhe a seção, base ou planificação lateral relevante.','Identifique apótema, altura ou geratriz quando existirem.','Calcule a área lateral, quando aplicável.','Calcule a área total.','Calcule o volume.','Compare o valor analítico com a área/volume medidos na malha.']:
        lines.append(r'\item '+esc(q))
    lines.append(r'\end{enumerate}')
    if with_answers:
        lines.append(r'\subsection*{Gabarito}')
        lines.append(r'\begin{itemize}')
        for k,v in result['values'].items():
            if isinstance(v,(int,float,np.floating)): lines.append(r'\item '+esc(k)+f': {float(v):.8g}')
        lines.append(r'\item Área da malha: '+f"{result['mesh_area']:.8g}")
        lines.append(r'\item Volume da malha: '+f"{result['mesh_volume']:.8g}")
        lines.append(r'\end{itemize}')
        lines.append(r'\subsection*{Dedução resumida}')
        lines.append(r'\begin{enumerate}')
        for line in result['derivation']: lines.append(r'\item '+esc(line))
        lines.append(r'\end{enumerate}')
    lines.append(r'\end{document}')
    return '\n'.join(lines)

def formula_lab_plot(ax, result, anim_step=0):
    case=result['case']; p=result['params']
    if case not in FORMULA_ADVANCED_CASES:
        # diagramas animados para cilindro/cone/tronco de cone, demais usam base.
        if case == 'Cilindro circular reto':
            _formula_plot_cylinder_animation(ax, p, anim_step); return
        if case == 'Cone circular reto':
            _formula_plot_cone_animation(ax, p, anim_step); return
        if case == 'Tronco de cone circular reto':
            _formula_plot_frustum_cone_animation(ax, p, anim_step); return
        return _formula_lab_plot_base_v2507(ax, result)
    ax.clear(); ax.set_aspect('equal', adjustable='datalim'); ax.grid(True, alpha=.25)
    if case == 'Toro circular':
        R=p.get('R',5); r=p.get('r',1.5)
        t=np.linspace(0,2*math.pi,240)
        ax.plot((R+r*np.cos(t)), r*np.sin(t), 'k-')
        ax.plot([0,R],[0,0],'--'); ax.text(R/2,.15,'R',ha='center')
        ax.plot([R,R+r],[0,0],':'); ax.text(R+r/2,.25,'r',ha='center')
        ax.set_title('Seção geradora do toro: círculo de raio r com centro a distância R')
    elif case == 'Elipsoide triaxial':
        a=p.get('a',4); b=p.get('b',3)
        t=np.linspace(0,2*math.pi,240); ax.plot(a*np.cos(t), b*np.sin(t),'k-')
        ax.plot([0,a],[0,0],'--'); ax.text(a/2,.15,'a',ha='center')
        ax.plot([0,0],[0,b],'--'); ax.text(.15,b/2,'b',va='center')
        ax.set_title('Seção elíptica: x²/a² + y²/b² = 1')
    else:
        a=p.get('a',3.0)
        # Mostra as faces planas usadas na fórmula: triângulo, quadrado, pentágono, hexágono.
        if 'Tetraedro' in case or 'Octaedro' in case or 'Icosaedro' in case:
            h=math.sqrt(3)*a/2; pts=np.array([[0,0],[a,0],[a/2,h]])
            title='Face triangular equilátera'
        elif 'Dodecaedro' in case:
            n=5; R=_regular_polygon_radius(n,a); pts=np.array([[R*math.cos(2*math.pi*k/n+math.pi/n),R*math.sin(2*math.pi*k/n+math.pi/n)] for k in range(n)]); title='Face pentagonal regular'
        elif 'Cuboctaedro' in case:
            pts=np.array([[0,0],[a,0],[a,a],[0,a]]); title='Cuboctaedro: quadrados + triângulos equiláteros'
        else:
            n=6; R=_regular_polygon_radius(n,a); pts=np.array([[R*math.cos(2*math.pi*k/n),R*math.sin(2*math.pi*k/n)] for k in range(n)]); title='Tetraedro truncado: triângulos + hexágonos'
        ax.add_patch(MplPolygon(pts, closed=True, facecolor='#dfefff', edgecolor='black'))
        ax.text(np.mean(pts[:,0]),np.mean(pts[:,1]),'face usada\nna fórmula',ha='center',va='center')
        ax.set_title(title)
    ax.autoscale_view()

def _formula_plot_cylinder_animation(ax, p, step):
    ax.clear(); ax.set_aspect('equal', adjustable='datalim'); ax.grid(True, alpha=.25)
    r=p.get('r',2); h=p.get('h',6); step=int(step)%4
    if step==0:
        ax.add_patch(MplPolygon(np.array([[0,0],[2*r,0],[2*r,h],[0,h]]), closed=True, facecolor='#e8f1ff', edgecolor='black'))
        ax.text(r,h/2,'cilindro\n(vista lateral)',ha='center',va='center')
        ax.set_title('1/4 — superfície lateral antes de desenrolar')
    elif step==1:
        ax.add_patch(MplPolygon(np.array([[0,0],[math.pi*r,0],[math.pi*r,h],[0,h]]), closed=True, facecolor='#e8f1ff', edgecolor='black'))
        ax.text(math.pi*r/2,h/2,'meio caminho\npara retângulo',ha='center',va='center')
        ax.set_title('2/4 — desenrolando a lateral')
    else:
        L=2*math.pi*r
        ax.add_patch(MplPolygon(np.array([[0,0],[L,0],[L,h],[0,h]]), closed=True, facecolor='#dfefff', edgecolor='black'))
        ax.text(L/2,h/2,'retângulo lateral\n2πr × h',ha='center',va='center')
        ax.set_title('3/4 — A_lateral = 2πrh')
    ax.autoscale_view()

def _formula_plot_cone_animation(ax, p, step):
    ax.clear(); ax.set_aspect('equal', adjustable='datalim'); ax.grid(True, alpha=.25)
    r=p.get('r',2); h=p.get('h',6); g=math.sqrt(r*r+h*h); step=int(step)%4
    if step==0:
        ax.plot([0,r],[0,0],'k-', [r,0],[0,h],'k-', [0,0],[0,h],'k--')
        ax.text(r/2,-.25,'r',ha='center'); ax.text(-.25,h/2,'h',ha='right'); ax.text(r/2,h/2,'g',ha='left')
        ax.set_title('1/4 — triângulo gerador: g²=r²+h²')
    elif step==1:
        th=np.linspace(0,math.pi,80); ax.plot(g*np.cos(th), g*np.sin(th),'k-'); ax.plot([0,g],[0,0],'k-'); ax.plot([0,-g],[0,0],'k-')
        ax.text(0,g*.45,'setor lateral\nraio g',ha='center')
        ax.set_title('2/4 — a lateral vira um setor circular')
    else:
        theta=2*math.pi*r/g; th=np.linspace(0,theta,120)
        ax.plot(g*np.cos(th),g*np.sin(th),'k-'); ax.plot([0,g],[0,0],'k-'); ax.plot([0,g*math.cos(theta)],[0,g*math.sin(theta)],'k-')
        ax.text(0,0,'ângulo θ=2πr/g',ha='center',va='center')
        ax.set_title('3/4 — área do setor = πrg')
    ax.autoscale_view()

def _formula_plot_frustum_cone_animation(ax, p, step):
    ax.clear(); ax.set_aspect('equal', adjustable='datalim'); ax.grid(True, alpha=.25)
    r1=p.get('r1',3); r2=p.get('r2',1.5); h=p.get('h',6); g=math.sqrt((r1-r2)**2+h*h); step=int(step)%3
    if step==0:
        ax.plot([0,r1],[0,0],'k-', [0,r2],[h,h],'k-', [r1,r2],[0,h],'k-', [0,0],[0,h],'k--')
        ax.text((r1+r2)/2,h/2,f'g={g:.3g}',ha='left'); ax.set_title('1/3 — geratriz do tronco')
    else:
        ax.add_patch(MplPolygon(np.array([[0,0],[2*math.pi*r1,0],[2*math.pi*r2,h],[0,h]]), closed=True, facecolor='#dfefff', edgecolor='black'))
        ax.text(math.pi*(r1+r2)/2,h/2,'trapézio curvo\naproximado',ha='center',va='center')
        ax.set_title('2/3 — A_lateral = π(r₁+r₂)g')
    ax.autoscale_view()

class GeoPolyAppV2507(GeoPolyAppV2506):
    def _build_formula_lab(self):
        self.formula_case_var = tk.StringVar(value=FORMULA_LAB_CASES[0])
        self.formula_param_vars = {}
        self.formula_hide_var = tk.BooleanVar(value=False)
        self.formula_answers_var = tk.BooleanVar(value=True)
        self.formula_anim_step = tk.IntVar(value=0)
        root = ttk.Frame(self.tabformula, padding=8); root.pack(fill='both', expand=True)
        top = ttk.LabelFrame(root, text='Formula Lab avançado — dedução, exercícios e malha', padding=8); top.pack(fill='x')
        ttk.Label(top, text='Sólido:').pack(side='left')
        cb = ttk.Combobox(top, textvariable=self.formula_case_var, values=FORMULA_LAB_CASES, state='readonly', width=46)
        cb.pack(side='left', padx=6); cb.bind('<<ComboboxSelected>>', lambda e: self._formula_case_changed())
        ttk.Button(top, text='Atualizar', command=self.update_formula_lab).pack(side='left', padx=3)
        ttk.Checkbutton(top, text='Modo aluno (esconder fórmulas)', variable=self.formula_hide_var, command=self.update_formula_lab).pack(side='left', padx=6)
        ttk.Button(top, text='Quadro animação', command=self.next_formula_animation_frame).pack(side='left', padx=3)
        ttk.Button(top, text='Exportar exercícios LaTeX', command=self.export_formula_exercises_latex).pack(side='left', padx=3)
        ttk.Button(top, text='Exportar exercícios PDF', command=self.export_formula_exercises_pdf).pack(side='left', padx=3)
        ttk.Checkbutton(top, text='Com gabarito', variable=self.formula_answers_var).pack(side='left', padx=3)
        body = ttk.Panedwindow(root, orient='horizontal'); body.pack(fill='both', expand=True, pady=(8,0))
        left = ttk.Frame(body); right = ttk.Frame(body); body.add(left, weight=1); body.add(right, weight=1)
        self.formula_param_frame = ttk.LabelFrame(left, text='Parâmetros interativos', padding=8); self.formula_param_frame.pack(fill='x')
        self.formula_text = tk.Text(left, wrap='word', font=('Consolas', 10), height=26); self.formula_text.pack(fill='both', expand=True, pady=(8,0))
        self.formula_fig = plt.Figure(figsize=(6.2,5.2)); self.axformula = self.formula_fig.add_subplot(111)
        self.canvasformula = FigureCanvasTkAgg(self.formula_fig, master=right); self.canvasformula.get_tk_widget().pack(fill='both', expand=True)
        hint = ttk.Label(right, text='Diagramas: bases, seções, geratriz, setor lateral e comparação fórmula × malha. Use “Quadro animação” para cilindro/cone.', wraplength=520)
        hint.pack(fill='x', pady=(4,0))
        self._formula_case_changed()
    def _formula_case_changed(self):
        if not hasattr(self, 'formula_param_frame'): return
        for w in self.formula_param_frame.winfo_children(): w.destroy()
        self.formula_param_vars = {}
        self.formula_anim_step.set(0)
        case = self.formula_case_var.get(); defaults = FORMULA_DEFAULTS.get(case, {})
        for key, value in defaults.items():
            row = ttk.Frame(self.formula_param_frame); row.pack(fill='x', pady=2)
            ttk.Label(row, text=FORMULA_PARAM_LABELS.get(key, key), width=30).pack(side='left')
            if key in ('n','m','rings'):
                var = tk.IntVar(value=int(value)); lo = 3 if key=='n' else 4; hi = 256
                spin = ttk.Spinbox(row, from_=lo, to=hi, increment=1, textvariable=var, width=10, command=self.update_formula_lab)
            else:
                var = tk.DoubleVar(value=float(value)); spin = ttk.Spinbox(row, from_=0.01, to=1000, increment=0.1, textvariable=var, width=10, command=self.update_formula_lab)
            spin.pack(side='left'); spin.bind('<KeyRelease>', lambda e: self.update_formula_lab()); spin.bind('<FocusOut>', lambda e: self.update_formula_lab())
            self.formula_param_vars[key] = var
        self.update_formula_lab()
    def _current_formula_result(self):
        case = self.formula_case_var.get()
        params = {k: v.get() for k, v in self.formula_param_vars.items()}
        return formula_lab_compute(case, params)
    def update_formula_lab(self):
        try:
            res = self._current_formula_result()
            self.formula_text.delete('1.0','end')
            self.formula_text.insert('end', formula_lab_text(res, hide_formula=bool(self.formula_hide_var.get())))
            formula_lab_plot(self.axformula, res, anim_step=self.formula_anim_step.get())
            self.canvasformula.draw_idle()
        except Exception as exc:
            if hasattr(self, 'formula_text'):
                self.formula_text.delete('1.0','end'); self.formula_text.insert('end','Erro no Formula Lab avançado:\n'+str(exc))
    def next_formula_animation_frame(self):
        self.formula_anim_step.set((int(self.formula_anim_step.get())+1)%4)
        self.update_formula_lab()
    def export_formula_exercises_latex(self):
        try:
            res=self._current_formula_result()
            path=filedialog.asksaveasfilename(title='Exportar folha de exercícios em LaTeX', defaultextension='.tex', initialfile=safe_name(res['case'])+'_exercicios.tex', filetypes=[('LaTeX','*.tex'),('Todos','*.*')])
            if not path: return
            Path(path).write_text(formula_lab_exercise_sheet_latex(res, with_answers=bool(self.formula_answers_var.get())), encoding='utf-8')
            messagebox.showinfo('Formula Lab', f'LaTeX salvo em:\n{path}')
        except Exception as exc:
            messagebox.showerror('Formula Lab LaTeX', str(exc))
    def export_formula_exercises_pdf(self):
        try:
            res=self._current_formula_result()
            path=filedialog.asksaveasfilename(title='Exportar folha de exercícios em PDF', defaultextension='.pdf', initialfile=safe_name(res['case'])+'_exercicios.pdf', filetypes=[('PDF','*.pdf')])
            if not path: return
            text=formula_lab_exercise_sheet_text(res, with_answers=bool(self.formula_answers_var.get()))
            fig=plt.Figure(figsize=(8.27,11.69))
            ax=fig.add_subplot(111); ax.axis('off')
            wrapped='\n'.join([line if len(line)<96 else line[:93]+'...' for line in text.splitlines()])
            ax.text(0.02,0.98,wrapped,ha='left',va='top',family='monospace',fontsize=9,transform=ax.transAxes)
            with PdfPages(path) as pp: pp.savefig(fig, bbox_inches='tight')
            messagebox.showinfo('Formula Lab', f'PDF salvo em:\n{path}')
        except Exception as exc:
            messagebox.showerror('Formula Lab PDF', str(exc))

# Amplia testes mantendo a suíte anterior.
_run_self_tests_before_v2507 = run_self_tests

def run_formula_lab_advanced_self_tests():
    out=[]
    for case in FORMULA_ADVANCED_CASES:
        res=formula_lab_compute(case, FORMULA_DEFAULTS[case])
        ok = res['mesh_area'] > 0 and res['mesh_volume'] > 0 and any(k.startswith('Área') for k in res['values']) and 'Volume' in res['values']
        out.append((f'Formula Lab avançado calcula {case}', bool(ok), res['values']))
    tor=formula_lab_compute('Toro circular', {'R':5,'r':1,'m':48,'rings':16})
    out.append(('Toro fórmula volume 2π²Rr²', abs(tor['values']['Volume'] - 10*math.pi*math.pi) < 1e-9, tor['values']))
    tet=formula_lab_compute('Tetraedro regular', {'a':2})
    out.append(('Tetraedro regular área √3 a²', abs(tet['values']['Área total'] - 4*math.sqrt(3)) < 1e-9, tet['values']))
    cuboct=formula_lab_compute('Cuboctaedro regular', {'a':2})
    out.append(('Cuboctaedro área positiva e erro pequeno', abs(cuboct['area_error_pct']) < 1e-6, cuboct.get('area_error_pct')))
    return out

def run_self_tests():
    rep=_run_self_tests_before_v2507()
    results=list(rep.results)
    for name, ok, detail in run_formula_lab_advanced_self_tests():
        results.append(TestCaseResult(name, bool(ok), '' if ok else str(detail)))
    return TestReport(results)



# ============================================================
# v25.0.8 — SIMETRIA COMBINATÓRIA AVANÇADA E CANONICAL LAB PLUS
# ============================================================
VERSION = '25.0.8'
EDITION = 'Symmetry & Canonicalization Advanced'
# Esta camada preserva menus e funcionalidades da v25.0.7 e adiciona:
# - automorfismos combinatórios com backtracking e preservação de faces;
# - comparação entre simetria combinatória e geométrica;
# - classificação regular / semirregular / Catalan / toroidal / maker;
# - relatório avançado de transitividade por órbitas;
# - Canonical Lab com gráfico de convergência, antes/depois e exportação do modelo.

@dataclass
class CombinatorialSymmetryReport:
    enabled: bool
    complete: bool
    vertex_count: int
    automorphism_count: int
    vertex_orbits: List[List[int]]
    edge_orbits: List[List[Tuple[int,int]]]
    face_orbits: List[List[int]]
    vertex_transitive: bool
    edge_transitive: bool
    face_transitive: bool
    reason: str = ''
    cap: int = 0
    def as_dict(self):
        d=asdict(self)
        d['edge_orbits']=[[list(e) for e in orb] for orb in self.edge_orbits]
        return d

def _face_set_index(poly):
    return {tuple(sorted(f)):i for i,f in enumerate(poly.faces)}

def _vertex_initial_colors_for_automorphism(poly):
    eadj=defaultdict(set)
    for a,b in poly.edges():
        eadj[a].add(b); eadj[b].add(a)
    incident=defaultdict(list)
    for fi,f in enumerate(poly.faces):
        for v in f: incident[v].append(len(f))
    return {i:(len(eadj[i]), tuple(sorted(incident[i]))) for i in range(len(poly.vertices))}

def _refine_vertex_colors(poly, colors):
    adj=defaultdict(set)
    for a,b in poly.edges():
        adj[a].add(b); adj[b].add(a)
    col=dict(colors)
    for _ in range(20):
        keys=[]
        for i in range(len(poly.vertices)):
            keys.append((col[i], tuple(sorted(col[j] for j in adj[i]))))
        uniq={k:n for n,k in enumerate(sorted(set(keys), key=str))}
        new={i:uniq[keys[i]] for i in range(len(keys))}
        if all(new[i]==col[i] for i in new): break
        col=new
    return col

def _is_face_preserving_perm(poly, perm):
    face_index=_face_set_index(poly)
    if not face_index: return False
    for f in poly.faces:
        key=tuple(sorted(perm[i] for i in f))
        if key not in face_index: return False
    return True

def _automorphisms_combinatorial(poly, max_vertices=80, max_aut=20000, time_limit=8.0):
    """Enumera automorfismos combinatórios preservando arestas e faces.

    É um algoritmo exato para o espaço explorado, mas com limites práticos.
    Quando o limite de tempo/quantidade é atingido, o relatório marca complete=False.
    """
    import time
    n=len(poly.vertices)
    if n==0: return [], True, 'sem vértices'
    if n>max_vertices:
        return [], False, f'modelo com {n} vértices excede limite combinatório desta aba ({max_vertices})'
    edges=set(tuple(sorted(e)) for e in poly.edges())
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    colors=_refine_vertex_colors(poly, _vertex_initial_colors_for_automorphism(poly))
    color_classes=defaultdict(list)
    for i,c in colors.items(): color_classes[c].append(i)
    candidates={i:set(color_classes[colors[i]]) for i in range(n)}
    # Matriz de distâncias no grafo ajuda a podar mapas impossíveis.
    dmat=[]
    for s in range(n):
        dist=[999999]*n; dist[s]=0; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if dist[v]>dist[u]+1:
                    dist[v]=dist[u]+1; q.append(v)
        dmat.append(dist)
    order=sorted(range(n), key=lambda i:(len(candidates[i]), -len(adj[i]), i))
    perms=[]; start=time.time(); complete=True; reason='enumeração completa'
    assigned={}; used=set()
    def feasible(v,w):
        if w in used: return False
        if colors[v]!=colors[w]: return False
        # preserva adjacência/não adjacência e distâncias contra vértices já atribuídos
        for u,pu in assigned.items():
            if ((u in adj[v]) != (pu in adj[w])): return False
            if dmat[v][u] != dmat[w][pu]: return False
        return True
    def backtrack(pos=0):
        nonlocal complete, reason
        if time.time()-start>time_limit:
            complete=False; reason='limite de tempo atingido'; return
        if len(perms)>=max_aut:
            complete=False; reason='limite de automorfismos atingido'; return
        if pos>=len(order):
            perm=[assigned[i] for i in range(n)]
            if _is_face_preserving_perm(poly, perm): perms.append(perm)
            return
        v=order[pos]
        # candidatos ordenados por proximidade geométrica apenas para saída determinística
        vc=poly.vertices[v]
        cand=sorted(candidates[v], key=lambda w: float(np.linalg.norm(poly.vertices[w]-vc)))
        for w in cand:
            if not feasible(v,w): continue
            assigned[v]=w; used.add(w)
            backtrack(pos+1)
            used.remove(w); del assigned[v]
            if not complete or len(perms)>=max_aut: return
    backtrack(0)
    # sempre garante identidade se válida e não apareceu
    ident=list(range(n))
    if _is_face_preserving_perm(poly, ident) and ident not in perms:
        perms.insert(0,ident)
    return perms, complete, reason

def _edge_orbits_from_vertex_perms(poly, perms):
    edge_sets=[tuple(sorted(e)) for e in poly.edges()]
    edge_index={e:i for i,e in enumerate(edge_sets)}
    edge_perms=[]
    for p in perms:
        ep=[]; ok=True
        for a,b in edge_sets:
            ee=tuple(sorted((p[a],p[b])))
            if ee not in edge_index: ok=False; break
            ep.append(edge_index[ee])
        if ok: edge_perms.append(ep)
    idx_orbits=_orbits_from_permutations(len(edge_sets), edge_perms) if edge_perms else [[i] for i in range(len(edge_sets))]
    return [[edge_sets[i] for i in orb] for orb in idx_orbits]

def _face_orbits_from_vertex_perms(poly, perms):
    face_keys=[tuple(sorted(f)) for f in poly.faces]
    face_index={k:i for i,k in enumerate(face_keys)}
    face_perms=[]
    for p in perms:
        fp=[]; ok=True
        for f in poly.faces:
            key=tuple(sorted(p[i] for i in f))
            if key not in face_index: ok=False; break
            fp.append(face_index[key])
        if ok: face_perms.append(fp)
    return _orbits_from_permutations(len(face_keys), face_perms) if face_perms else [[i] for i in range(len(face_keys))]

def combinatorial_symmetry_report(poly, max_vertices=80, max_aut=20000):
    perms,complete,reason=_automorphisms_combinatorial(poly, max_vertices=max_vertices, max_aut=max_aut)
    if not perms:
        vo=[[i] for i in range(len(poly.vertices))]; eo=[[e] for e in poly.edges()]; fo=[[i] for i in range(len(poly.faces))]
        return CombinatorialSymmetryReport(False,False,len(poly.vertices),0,vo,eo,fo,False,False,False,reason,max_aut)
    vo=_orbits_from_permutations(len(poly.vertices), perms)
    eo=_edge_orbits_from_vertex_perms(poly, perms)
    fo=_face_orbits_from_vertex_perms(poly, perms)
    return CombinatorialSymmetryReport(True,complete,len(poly.vertices),len(perms),vo,eo,fo,len(vo)==1,len(eo)==1,len(fo)==1,reason,max_aut)

def _local_face_regular_hint(poly, tol=1e-5):
    """Retorna se todas as faces são localmente regulares por lados/ângulos."""
    reg=polyhedral_regularity_analysis(poly)
    # Usa campos existentes quando presentes; fallback por comprimentos/áreas.
    if isinstance(reg,dict):
        if 'face_regular_by_sides_and_angles_hint' in reg:
            return bool(reg.get('face_regular_by_sides_and_angles_hint'))
        if 'face_type_table' in reg:
            try:
                return all(row.get('regular_hint',False) for row in reg.get('face_type_table',[]))
            except Exception: pass
    ok=True
    for f in poly.faces:
        pts=poly.vertices[f]; L=[]
        for i in range(len(f)): L.append(float(np.linalg.norm(pts[(i+1)%len(f)]-pts[i])))
        if L and (max(L)-min(L))/max(min(L),EPS)>tol: ok=False
    return ok

def classify_polyhedron_advanced(poly, comb=None, geom=None):
    er=poly.euler(); hist=poly.face_histogram(); status=getattr(poly.meta,'status','unknown') if hasattr(poly,'meta') else 'unknown'
    comb=comb or combinatorial_symmetry_report(poly)
    geom=geom or detect_symmetry_v242(poly)
    all_edges=poly.edge_lengths(); edge_uniform=bool(all_edges and (max(all_edges)-min(all_edges))/max(min(all_edges),EPS)<1e-5)
    faces_regular=_local_face_regular_hint(poly)
    one_face_type=(len(hist)==1)
    if 'toroidal' in status or er.chi==0:
        return 'poliedro toroidal/generalizado', 'χ=0 ou status toroidal; útil para topologia/gênero, fora do universo convexo clássico χ=2.'
    if 'catalan' in status or 'Catalan' in poly.family:
        return 'Catalan / dual isoedral', 'Classificação apoiada no status/família e na dualidade; faces geralmente congruentes, mas não necessariamente regulares.'
    if one_face_type and edge_uniform and faces_regular and comb.vertex_transitive and comb.edge_transitive and comb.face_transitive:
        return 'regular', 'Uma classe de face, arestas uniformes, faces regulares e transitividade V/E/F por automorfismos.'
    if edge_uniform and faces_regular and comb.vertex_transitive and not one_face_type:
        return 'semirregular / Arquimediano-like', 'Faces regulares, arestas uniformes e vértice-transitividade; classificação numérica/combinatória compatível com semirregularidade.'
    if comb.face_transitive and not comb.vertex_transitive:
        return 'face-transitivo / dual-like', 'Automorfismos indicam uma órbita de faces, mas múltiplas órbitas de vértices.'
    if 'procedural' in status:
        return 'procedural/maker', 'Sólido gerado por procedimento; classificação depende do construtor e dos parâmetros.'
    return 'geral/baixa simetria', 'Não satisfaz os critérios computacionais fortes de regularidade/semirregularidade nesta análise.'

def symmetry_comparison_report_text(poly):
    geom=detect_symmetry_v242(poly)
    comb=combinatorial_symmetry_report(poly)
    cls,why=classify_polyhedron_advanced(poly,comb,geom)
    lines=[]
    lines.append(f'Simetria e órbitas avançadas — {poly.name}')
    lines.append('='*78)
    lines.append('1) Simetria geométrica aproximada')
    lines.append(f'Grupo estimado: {geom.group}')
    lines.append(f'Ordem rotacional estimada: {geom.rotation_order}')
    lines.append(f'Órbitas geométricas de vértices/arestas/faces: {len(geom.vertex_orbits)} / {len(geom.edge_orbits)} / {len(geom.face_orbits)}')
    lines.append(f'Vertex/edge/face-transitive geométrico: {geom.vertex_transitive} / {geom.edge_transitive} / {geom.face_transitive}')
    lines.append(f'Erro máximo de mapeamento: {geom.max_mapping_error:.3e}')
    lines.append('')
    lines.append('2) Automorfismos combinatórios')
    lines.append(f'Ativo: {comb.enabled}; completo: {comb.complete}; motivo: {comb.reason}')
    lines.append(f'Automorfismos enumerados: {comb.automorphism_count}')
    lines.append(f'Órbitas combinatórias de vértices/arestas/faces: {len(comb.vertex_orbits)} / {len(comb.edge_orbits)} / {len(comb.face_orbits)}')
    lines.append(f'Vertex/edge/face-transitive combinatório: {comb.vertex_transitive} / {comb.edge_transitive} / {comb.face_transitive}')
    lines.append('')
    lines.append('3) Comparação geométrica × combinatória')
    lines.append(f'Vértices: {"compatível" if len(geom.vertex_orbits)==len(comb.vertex_orbits) else "diferente"}')
    lines.append(f'Arestas:  {"compatível" if len(geom.edge_orbits)==len(comb.edge_orbits) else "diferente"}')
    lines.append(f'Faces:    {"compatível" if len(geom.face_orbits)==len(comb.face_orbits) else "diferente"}')
    if not comb.complete:
        lines.append('Atenção: a enumeração combinatória foi limitada; a comparação é indicativa.')
    lines.append('')
    lines.append('4) Classificação')
    lines.append(f'Classe sugerida: {cls}')
    lines.append(f'Justificativa: {why}')
    lines.append('')
    lines.append('5) Tabelas de órbitas combinatórias')
    def fmt_orbs(title,orbs):
        lines.append(title)
        for i,o in enumerate(orbs[:12],1): lines.append(f'  O{i}: tamanho {len(o)}; amostra {o[:12]}')
        if len(orbs)>12: lines.append(f'  ... {len(orbs)-12} órbitas adicionais')
    fmt_orbs('Vértices:',comb.vertex_orbits)
    fmt_orbs('Arestas:',[[list(e) for e in orb] for orb in comb.edge_orbits])
    fmt_orbs('Faces:',comb.face_orbits)
    lines.append('')
    lines.append('Nota: automorfismo combinatório preserva grafo de arestas e conjuntos de faces. A simetria geométrica exige também uma rotação/reflexão numérica que realize a permutação no espaço.')
    return '\n'.join(lines)

def advanced_symmetry_payload(poly):
    geom=detect_symmetry_v242(poly); comb=combinatorial_symmetry_report(poly); cls,why=classify_polyhedron_advanced(poly,comb,geom)
    return {'geometric':geom.as_dict(), 'combinatorial':comb.as_dict(), 'classification':cls, 'classification_reason':why}

def canonical_lab_advanced(poly,iterations=120,rate=0.25):
    before_reg=polyhedral_regularity_analysis(poly)
    before_mid=midsphere_defect(poly)
    can=canonical_form_v24(poly,iterations,rate)
    after_reg=polyhedral_regularity_analysis(can)
    after_mid=midsphere_defect(can)
    hist=list(getattr(can,'canonical_history',[]))
    payload={
        'iterations':int(iterations),'rate':float(rate),
        'midsphere_before':float(before_mid),'midsphere_after':float(after_mid),
        'midsphere_history':[float(x) for x in hist],
        'edge_dispersion_before':before_reg.get('edge_relative_dispersion'),
        'edge_dispersion_after':after_reg.get('edge_relative_dispersion'),
        'area_before':poly.area(),'area_after':can.area(),
        'volume_before':poly.volume_abs(),'volume_after':can.volume_abs(),
    }
    lines=[]
    lines.append(f'Canonical Lab avançado — {poly.name}')
    lines.append('='*78)
    lines.append('Método didático: planarização de faces + ajuste de tangência das arestas a uma midsphere.')
    lines.append('Aviso: não substitui o canonical robusto do Antiprism; é laboratório visual/numérico.')
    lines.append('')
    lines.append(f'Iterações: {iterations}; taxa: {rate:.4f}')
    lines.append(f'Erro de midsphere antes: {before_mid:.6e}')
    lines.append(f'Erro de midsphere depois: {after_mid:.6e}')
    lines.append(f'Melhoria relativa: {((before_mid-after_mid)/before_mid*100) if before_mid>EPS else 0:.3f}%')
    lines.append(f'Dispersão de arestas antes: {before_reg.get("edge_relative_dispersion")}')
    lines.append(f'Dispersão de arestas depois: {after_reg.get("edge_relative_dispersion")}')
    lines.append(f'Área antes/depois: {poly.area():.6f} / {can.area():.6f}')
    lines.append(f'Volume antes/depois: {poly.volume_abs():.6f} / {can.volume_abs():.6f}')
    lines.append('')
    lines.append('Histórico do erro de midsphere:')
    lines.append(', '.join(f'{x:.3e}' for x in hist))
    return '\n'.join(lines), can, payload

def _plot_poly_on_ax(ax, poly, title, alpha=0.72):
    ax.clear()
    verts=poly.vertices
    polys=[[verts[i] for i in f] for f in poly.faces]
    coll=Poly3DCollection(polys, alpha=alpha, edgecolor='k', linewidth=0.45)
    ax.add_collection3d(coll)
    if len(verts): ax.scatter(verts[:,0],verts[:,1],verts[:,2],s=10)
    if len(verts):
        d=np.max(np.ptp(verts,axis=0)) or 1.0; c=verts.mean(axis=0)
        ax.set_xlim(c[0]-d/2,c[0]+d/2); ax.set_ylim(c[1]-d/2,c[1]+d/2); ax.set_zlim(c[2]-d/2,c[2]+d/2)
    ax.set_box_aspect((1,1,1)); ax.set_title(title); ax.set_axis_off()

# Estende o relatório principal com análise avançada, sem remover conteúdo anterior.
_full_report_before_v2508 = full_report
def full_report(poly, scale_mm=50.0, density_g_cm3=1.24, cost_per_kg=100.0):
    md,payload=_full_report_before_v2508(poly, scale_mm, density_g_cm3, cost_per_kg)
    try:
        sp=advanced_symmetry_payload(poly)
        md += '\n\n## Simetria avançada v25.0.8\n'
        md += f"- Classificação sugerida: {sp.get('classification')}\n"
        md += f"- Ordem geométrica aproximada: {sp['geometric'].get('rotation_order')}\n"
        md += f"- Automorfismos combinatórios enumerados: {sp['combinatorial'].get('automorphism_count')}\n"
        md += f"- V/E/F transitivo combinatório: {sp['combinatorial'].get('vertex_transitive')} / {sp['combinatorial'].get('edge_transitive')} / {sp['combinatorial'].get('face_transitive')}\n"
        payload['advanced_symmetry_v2508']=sp
    except Exception as exc:
        payload['advanced_symmetry_v2508_error']=str(exc)
    return md,payload

class GeoPolyAppV2508(GeoPolyAppV2507):
    def _build_symmetry_tab(self):
        self.tabsymmetry.rowconfigure(1,weight=1); self.tabsymmetry.columnconfigure(0,weight=1)
        bar=ttk.LabelFrame(self.tabsymmetry,text='Simetria avançada: geométrica × automorfismos combinatórios',padding=8)
        bar.grid(row=0,column=0,sticky='ew',pady=(0,6))
        ttk.Button(bar,text='Atualizar simetria',command=self.update_symmetry_tab).pack(side='left',padx=4)
        ttk.Button(bar,text='Exportar JSON',command=self.export_symmetry_json_v2508).pack(side='left',padx=4)
        ttk.Label(bar,text='Inclui órbitas por automorfismo, comparação geométrica/combinatória e classificação.').pack(side='left',padx=8)
        self.symmetry_text=tk.Text(self.tabsymmetry,wrap='word',font=('Consolas',10)); self.symmetry_text.grid(row=1,column=0,sticky='nsew')
    def _build_canonical_tab(self):
        self.tabcanonical.rowconfigure(1,weight=1); self.tabcanonical.columnconfigure(0,weight=1); self.tabcanonical.columnconfigure(1,weight=1)
        bar=ttk.LabelFrame(self.tabcanonical,text='Canonical Lab avançado',padding=8); bar.grid(row=0,column=0,columnspan=2,sticky='ew',pady=(0,6))
        self.canon_iter_var=tk.IntVar(value=120); self.canon_rate_var=tk.DoubleVar(value=0.25)
        ttk.Label(bar,text='Iterações').pack(side='left'); ttk.Spinbox(bar,from_=5,to=2000,increment=5,textvariable=self.canon_iter_var,width=8).pack(side='left',padx=4)
        ttk.Label(bar,text='Taxa').pack(side='left'); ttk.Spinbox(bar,from_=0.01,to=1.0,increment=0.05,textvariable=self.canon_rate_var,width=8).pack(side='left',padx=4)
        ttk.Button(bar,text='Rodar',command=self.update_canonical_tab).pack(side='left',padx=4)
        ttk.Button(bar,text='Usar forma canônica como modelo atual',command=self.use_canonical_as_current_v2508).pack(side='left',padx=4)
        ttk.Button(bar,text='Exportar OBJ/STL',command=self.export_canonical_mesh_v2508).pack(side='left',padx=4)
        self.canonical_text=tk.Text(self.tabcanonical,wrap='word',font=('Consolas',10)); self.canonical_text.grid(row=1,column=0,sticky='nsew',padx=(0,4))
        self.figcanon_adv=plt.Figure(figsize=(8,6),dpi=100)
        self.axcanon_orig=self.figcanon_adv.add_subplot(221,projection='3d')
        self.axcanon_new=self.figcanon_adv.add_subplot(222,projection='3d')
        self.axcanon_hist=self.figcanon_adv.add_subplot(212)
        self.canvascanon_adv=FigureCanvasTkAgg(self.figcanon_adv,master=self.tabcanonical)
        self.canvascanon_adv.get_tk_widget().grid(row=1,column=1,sticky='nsew')
        self.canonical_poly_v2508=None
    def update_symmetry_tab(self):
        if not self.poly or not hasattr(self,'symmetry_text'): return
        self.symmetry_text.delete('1.0','end')
        try:
            self.symmetry_text.insert('end',symmetry_comparison_report_text(self.poly))
            self.symmetry_text.insert('end','\n\nPayload JSON resumido\n'+'-'*40+'\n')
            payload=advanced_symmetry_payload(self.poly)
            # reduz o tamanho exibido para não travar em catálogos grandes
            small={k:payload[k] for k in ['classification','classification_reason']}
            small['geometric_summary']={k:payload['geometric'].get(k) for k in ['rotation_order','group','vertex_transitive','edge_transitive','face_transitive']}
            small['combinatorial_summary']={k:payload['combinatorial'].get(k) for k in ['enabled','complete','automorphism_count','vertex_transitive','edge_transitive','face_transitive','reason']}
            self.symmetry_text.insert('end',json.dumps(small,indent=2,ensure_ascii=False,default=str))
        except Exception as exc:
            self.symmetry_text.insert('end','Erro na simetria avançada:\n'+str(exc))
    def export_symmetry_json_v2508(self):
        if not self.poly: return
        path=filedialog.asksaveasfilename(title='Exportar relatório de simetria JSON',defaultextension='.json',initialfile=safe_name(self.poly.name)+'_simetria_v2508.json',filetypes=[('JSON','*.json')])
        if not path: return
        Path(path).write_text(json.dumps(advanced_symmetry_payload(self.poly),indent=2,ensure_ascii=False,default=str),encoding='utf-8')
        messagebox.showinfo('Simetria',f'JSON salvo em:\n{path}')
    def update_canonical_tab(self):
        if not self.poly or not hasattr(self,'canonical_text'): return
        self.canonical_text.delete('1.0','end')
        try:
            txt,can,payload=canonical_lab_advanced(self.poly,self.canon_iter_var.get(),self.canon_rate_var.get())
            self.canonical_poly_v2508=can; self.canonical_payload_v2508=payload
            self.canonical_text.insert('end',txt)
            _plot_poly_on_ax(self.axcanon_orig,self.poly,'Antes',0.72)
            _plot_poly_on_ax(self.axcanon_new,can,'Depois',0.72)
            self.axcanon_hist.clear()
            hist=payload.get('midsphere_history',[])
            if hist:
                self.axcanon_hist.plot(list(range(len(hist))),hist,marker='o')
                self.axcanon_hist.set_yscale('log')
            self.axcanon_hist.set_title('Convergência do erro de midsphere')
            self.axcanon_hist.set_xlabel('amostras da iteração'); self.axcanon_hist.set_ylabel('erro relativo')
            self.axcanon_hist.grid(True,alpha=0.3)
            self.figcanon_adv.tight_layout(); self.canvascanon_adv.draw_idle()
        except Exception as exc:
            self.canonical_text.insert('end','Erro no Canonical Lab avançado:\n'+str(exc))
    def use_canonical_as_current_v2508(self):
        can=getattr(self,'canonical_poly_v2508',None)
        if can is None:
            messagebox.showwarning('Canonical Lab','Rode a canonicalização antes.'); return
        self.poly=can; self.net=search_best_net(self.poly); self.update_all(); self.nb.select(self.tab3d)
    def export_canonical_mesh_v2508(self):
        can=getattr(self,'canonical_poly_v2508',None)
        if can is None:
            messagebox.showwarning('Canonical Lab','Rode a canonicalização antes.'); return
        folder=filedialog.askdirectory(title='Escolha a pasta para OBJ/STL da forma canônica')
        if not folder: return
        folder=Path(folder); folder.mkdir(parents=True,exist_ok=True)
        base=safe_name(can.name)
        write_obj(can,folder/(base+'.obj'),self.scale_var.get())
        write_stl_ascii(can,folder/(base+'.stl'),self.scale_var.get())
        Path(folder/(base+'_canonical_payload.json')).write_text(json.dumps(getattr(self,'canonical_payload_v2508',{}),indent=2,ensure_ascii=False,default=str),encoding='utf-8')
        messagebox.showinfo('Canonical Lab',f'Arquivos salvos em:\n{folder}')

# Amplia testes mantendo a suíte anterior.
_run_self_tests_before_v2508 = run_self_tests

def run_symmetry_canonical_advanced_self_tests():
    out=[]
    def add(name,ok,detail=''):
        out.append((name,bool(ok),detail))
    cube=CATALOG['Platônicos / Cubo ou Hexaedro'].build()
    comb=combinatorial_symmetry_report(cube)
    add('automorfismos combinatórios cubo completos', comb.complete and comb.automorphism_count>=24, comb.as_dict())
    add('cubo combinatorial V/E/F transitivo', comb.vertex_transitive and comb.edge_transitive and comb.face_transitive, comb.as_dict())
    tet=CATALOG['Platônicos / Tetraedro'].build(); combt=combinatorial_symmetry_report(tet)
    add('tetraedro combinatorial regular', combt.vertex_transitive and combt.edge_transitive and combt.face_transitive and combt.automorphism_count>=12, combt.as_dict())
    cls,why=classify_polyhedron_advanced(cube,comb,detect_symmetry_v242(cube))
    add('classificação cubo regular', cls=='regular', (cls,why))
    cuboct=CATALOG['Arquimedianos / Cuboctaedro'].build()
    c2=combinatorial_symmetry_report(cuboct, max_vertices=80)
    cls2,why2=classify_polyhedron_advanced(cuboct,c2,detect_symmetry_v242(cuboct))
    add('classificação cuboctaedro semirregular', 'semirregular' in cls2 or c2.vertex_transitive, (cls2,why2,c2.as_dict()))
    txt=namespace_safe_symmetry_text = symmetry_comparison_report_text(cube)
    add('relatório de simetria avançada contém comparação', 'Comparação geométrica' in txt and 'Automorfismos combinatórios' in txt)
    ctxt,can,payload=canonical_lab_advanced(cube,20,0.15)
    add('canonical avançado retorna payload e histórico', isinstance(can,Polyhedron) and len(payload.get('midsphere_history',[]))>=2, payload)
    add('canonical avançado preserva Euler', can.euler().chi==cube.euler().chi)
    return out

def run_self_tests():
    rep=_run_self_tests_before_v2508()
    results=list(rep.results)
    for name,ok,detail in run_symmetry_canonical_advanced_self_tests():
        results.append(TestCaseResult('v25.0.8 / '+name, bool(ok), '' if ok else str(detail)))
    return TestReport(results)


def main():
    GeoPolyAppV2508().mainloop()

if False and __name__ == '__main__':
    main()

# ============================================================
# v25.0.9 — OFF / Antiprism Interoperability
# Mantém todas as funcionalidades anteriores e acrescenta aba de
# importação/exportação OFF para interoperar com Antiprism e outros
# programas matemáticos baseados em OFF.
# ============================================================

VERSION = '25.0.9'
EDITION = 'OFF / Antiprism Interoperability'


def _off_clean_lines(text: str):
    """Remove comentários e linhas vazias de um arquivo OFF.

    Aceita comentários iniciados por # em qualquer linha. Mantém apenas tokens
    úteis para leitura do cabeçalho, contagens, vértices e faces.
    """
    lines=[]
    for raw in str(text).splitlines():
        line=raw.split('#',1)[0].strip()
        if line:
            lines.append(line)
    return lines


def read_off_file(path) -> Polyhedron:
    """Lê um arquivo OFF simples e retorna um Polyhedron.

    Compatível com a forma usual usada pelo Antiprism:
        OFF
        V F E
        x y z
        ...
        n i1 i2 ... in

    Também aceita a variante em que o cabeçalho aparece como:
        OFF V F E

    Limitações honestas:
    - COFF/NOFF/OFF com cores/normais são lidos apenas como geometria, quando
      possível, ignorando atributos extras após coordenadas ou índices.
    - Faces com menos de 3 vértices são ignoradas.
    """
    path=Path(path)
    text=path.read_text(encoding='utf-8',errors='ignore')
    lines=_off_clean_lines(text)
    if not lines:
        raise ValueError('Arquivo OFF vazio.')
    first=lines[0].split()
    header=first[0].upper()
    supported={'OFF','COFF','NOFF','STOFF','CNOFF'}
    if header not in supported:
        raise ValueError(f'Cabeçalho OFF não reconhecido: {first[0]!r}')
    idx=1
    if len(first)>=4:
        nv=int(first[1]); nf=int(first[2]); ne=int(first[3])
    else:
        if idx>=len(lines): raise ValueError('Arquivo OFF sem linha de contagens V F E.')
        counts=lines[idx].split(); idx+=1
        if len(counts)<2: raise ValueError('Linha de contagens OFF inválida.')
        nv=int(counts[0]); nf=int(counts[1]); ne=int(counts[2]) if len(counts)>2 else 0
    if nv<=0 or nf<0:
        raise ValueError(f'Contagens OFF inválidas: V={nv}, F={nf}.')
    if idx+nv>len(lines):
        raise ValueError('Arquivo OFF terminou antes de listar todos os vértices.')
    vertices=[]
    for k in range(nv):
        vals=lines[idx+k].split()
        if len(vals)<3: raise ValueError(f'Linha de vértice inválida: {lines[idx+k]!r}')
        vertices.append([float(vals[0]),float(vals[1]),float(vals[2])])
    idx+=nv
    faces=[]
    for k in range(nf):
        if idx+k>=len(lines):
            raise ValueError('Arquivo OFF terminou antes de listar todas as faces.')
        vals=lines[idx+k].split()
        if not vals: continue
        m=int(vals[0])
        if m<3: continue
        if len(vals)<m+1:
            raise ValueError(f'Face OFF incompleta na linha: {lines[idx+k]!r}')
        f=[int(x) for x in vals[1:m+1]]
        if min(f)<0 or max(f)>=nv:
            raise ValueError(f'Face com índice fora do intervalo 0..{nv-1}: {f}')
        faces.append(f)
    meta=GeometryMeta(
        status='imported_off',
        source=f'Imported OFF file: {path.name}',
        warning='Modelo externo importado. A validade matemática depende da fonte; use validação, relatório e planificação antes de fabricar.',
        tags=['external','off','antiprism_interoperability'],
        expected_signature=None
    )
    poly=Polyhedron(vertices,faces,path.stem,'Modelo externo OFF/Antiprism',f'Importado de {path}',meta)
    # Guarda caminho de origem como atributo dinâmico para relatório.
    poly.off_source_path=str(path)
    return poly


def write_off_file(poly: Polyhedron, path, scale: float=1.0, comments: bool=True):
    """Exporta o poliedro atual em OFF simples, compatível com Antiprism.

    Por padrão, usa coordenadas normalizadas multiplicadas por scale. Para
    interoperar com Antiprism, scale=1 preserva a geometria interna do GeoPoly;
    para fabricar/inspecionar em milímetros, use scale_mm quando desejado.
    """
    path=Path(path)
    verts=np.array(poly.vertices,dtype=float)*float(scale)
    edges=len(poly.edges())
    with path.open('w',encoding='utf-8') as f:
        f.write('OFF\n')
        if comments:
            f.write(f'# Exported by {APP_NAME} v{VERSION} — {EDITION}\n')
            f.write(f'# Name: {poly.name}\n')
            f.write(f'# Family: {poly.family}\n')
            f.write(f'# Geometry status: {poly.meta.status}\n')
        f.write(f'{len(verts)} {len(poly.faces)} {edges}\n')
        for p in verts:
            f.write(f'{p[0]:.12g} {p[1]:.12g} {p[2]:.12g}\n')
        for face in poly.faces:
            f.write(str(len(face))+' '+' '.join(str(int(i)) for i in face)+'\n')


def off_antiprism_report(poly: Polyhedron) -> str:
    er=poly.euler(); val=poly.validate(); hist=poly.face_histogram(); lengths=poly.edge_lengths()
    source=getattr(poly,'off_source_path','modelo atual do GeoPoly')
    lines=[]
    lines.append('Interoperabilidade OFF / Antiprism')
    lines.append('='*55)
    lines.append(f'Modelo: {poly.name}')
    lines.append(f'Família: {poly.family}')
    lines.append(f'Origem: {source}')
    lines.append(f'Status geométrico: {poly.meta.status}')
    if poly.meta.warning:
        lines.append(f'Aviso: {poly.meta.warning}')
    lines.append('')
    lines.append('Resumo combinatório')
    lines.append('-'*55)
    lines.append(f'V = {er.V}')
    lines.append(f'E = {er.E}')
    lines.append(f'F = {er.F}')
    lines.append(f'χ = V - E + F = {er.chi}')
    lines.append(f'Histograma de faces: {hist}')
    lines.append(f'Dupla contagem Σ lados = {sum(len(f) for f in poly.faces)}, 2E = {2*er.E}')
    lines.append('')
    lines.append('Validação topológica')
    lines.append('-'*55)
    lines.append(f'Fechado: {"sim" if val.closed else "não"}')
    lines.append(f'Manifold: {"sim" if val.manifold else "não"}')
    lines.append(f'Orientável (indício): {"sim" if val.orientable_hint else "não"}')
    lines.append(f'Componentes: {val.components}')
    lines.append(f'Bordas abertas: {val.boundary_edges}')
    lines.append(f'Arestas não-manifold: {val.nonmanifold_edges}')
    lines.append(f'Gênero estimado: {val.genus_hint}')
    lines.append('')
    lines.append('Métrica normalizada')
    lines.append('-'*55)
    lines.append(f'Área da malha: {poly.area():.10g}')
    lines.append(f'Volume assinado absoluto: {poly.volume_abs():.10g}')
    if lengths:
        lines.append(f'Aresta mínima: {min(lengths):.10g}')
        lines.append(f'Aresta máxima: {max(lengths):.10g}')
        lines.append(f'Dispersão relativa das arestas: {((max(lengths)-min(lengths))/(sum(lengths)/len(lengths)) if sum(lengths) else 0):.6g}')
    lines.append('')
    lines.append('Fluxo sugerido com Antiprism')
    lines.append('-'*55)
    lines.append('1. Exporte o sólido atual em OFF para usar no Antiprism.')
    lines.append('2. Aplique operações externas, por exemplo canonical, conway, off_util etc.')
    lines.append('3. Reimporte o OFF modificado no GeoPoly.')
    lines.append('4. Use as abas de Euler, Planificação, Multi-folha, Simetria, Formula Lab e Relatório.')
    lines.append('')
    lines.append('Observação: o GeoPoly não tenta substituir o Antiprism; esta aba serve para interoperar com ele.')
    return '\n'.join(lines)


def current_poly_off_summary(poly: Polyhedron) -> dict:
    er=poly.euler(); val=poly.validate()
    return {
        'name': poly.name,
        'family': poly.family,
        'status': poly.meta.status,
        'V': int(er.V), 'E': int(er.E), 'F': int(er.F), 'chi': int(er.chi),
        'closed': bool(val.closed), 'manifold': bool(val.manifold),
        'genus_hint': None if val.genus_hint is None else float(val.genus_hint),
        'face_histogram': {str(k): int(v) for k,v in poly.face_histogram().items()},
        'source': getattr(poly,'off_source_path','GeoPoly catalog/current model')
    }


class GeoPolyAppV2509(GeoPolyAppV2508):
    """Versão v25.0.9 com aba OFF/Antiprism, preservando as abas anteriores."""
    def _build_ui(self):
        super()._build_ui()
        self.title(f'{APP_NAME} v{VERSION} — {EDITION}')
        self.taboff=ttk.Frame(self.nb,padding=6)
        self.nb.add(self.taboff,text='Antiprism / OFF')
        self._build_off_tab()
    def _build_off_tab(self):
        self.taboff.rowconfigure(2,weight=1); self.taboff.columnconfigure(0,weight=1)
        intro=ttk.LabelFrame(self.taboff,text='Interoperabilidade com Antiprism e arquivos OFF',padding=8)
        intro.grid(row=0,column=0,sticky='ew',pady=(0,6))
        intro.columnconfigure(4,weight=1)
        ttk.Button(intro,text='Importar .OFF',command=self.import_off_ui).grid(row=0,column=0,sticky='ew',padx=3)
        ttk.Button(intro,text='Exportar atual .OFF',command=self.export_current_off_ui).grid(row=0,column=1,sticky='ew',padx=3)
        ttk.Button(intro,text='Exportar atual .OFF em mm',command=self.export_current_off_mm_ui).grid(row=0,column=2,sticky='ew',padx=3)
        ttk.Button(intro,text='Exportar resumo JSON',command=self.export_off_summary_json_ui).grid(row=0,column=3,sticky='ew',padx=3)
        ttk.Label(intro,text='Use OFF para trocar modelos com Antiprism. Depois de importar, todas as abas do GeoPoly passam a trabalhar no modelo externo.',wraplength=620).grid(row=0,column=4,sticky='w',padx=8)
        opts=ttk.LabelFrame(self.taboff,text='Opções',padding=8)
        opts.grid(row=1,column=0,sticky='ew',pady=(0,6))
        self.off_scale_var=tk.DoubleVar(value=1.0)
        self.off_mm_scale_var=tk.DoubleVar(value=50.0)
        self.off_comments_var=tk.BooleanVar(value=True)
        ttk.Label(opts,text='Escala OFF normalizada:').pack(side='left')
        ttk.Spinbox(opts,from_=0.001,to=10000,increment=0.1,textvariable=self.off_scale_var,width=10).pack(side='left',padx=4)
        ttk.Label(opts,text='Escala OFF em mm:').pack(side='left',padx=(12,0))
        ttk.Spinbox(opts,from_=0.1,to=10000,increment=1,textvariable=self.off_mm_scale_var,width=10).pack(side='left',padx=4)
        ttk.Checkbutton(opts,text='Comentários no OFF exportado',variable=self.off_comments_var).pack(side='left',padx=12)
        self.off_text=tk.Text(self.taboff,wrap='word',font=('Consolas',10))
        self.off_text.grid(row=2,column=0,sticky='nsew')
        self.update_off_tab()
    def update_all(self):
        super().update_all()
        if hasattr(self,'off_text'):
            self.update_off_tab()
    def update_off_tab(self):
        if not hasattr(self,'off_text') or not self.poly: return
        self.off_text.delete('1.0','end')
        self.off_text.insert('end',off_antiprism_report(self.poly))
    def import_off_ui(self):
        path=filedialog.askopenfilename(title='Importar arquivo OFF / Antiprism',filetypes=[('OFF files','*.off *.OFF'),('Todos','*.*')])
        if not path: return
        try:
            p=read_off_file(path)
            self.poly=p; self.net=search_best_net(self.poly); self.ms=solve_multi_sheet_net(self.poly,self.net)
            self.key_var.set('')
            self.status_var.set(f'OFF importado: {Path(path).name}')
            self.update_all(); self.nb.select(self.taboff)
        except Exception as exc:
            messagebox.showerror('Importar OFF',str(exc))
    def export_current_off_ui(self):
        if not self.poly: return
        path=filedialog.asksaveasfilename(title='Exportar OFF normalizado',defaultextension='.off',initialfile=safe_name(self.poly.name)+'.off',filetypes=[('OFF','*.off'),('Todos','*.*')])
        if not path: return
        try:
            write_off_file(self.poly,path,scale=float(self.off_scale_var.get()),comments=bool(self.off_comments_var.get()))
            messagebox.showinfo('Exportar OFF',f'Arquivo salvo em:\n{path}')
        except Exception as exc:
            messagebox.showerror('Exportar OFF',str(exc))
    def export_current_off_mm_ui(self):
        if not self.poly: return
        path=filedialog.asksaveasfilename(title='Exportar OFF em mm',defaultextension='.off',initialfile=safe_name(self.poly.name)+'_mm.off',filetypes=[('OFF','*.off'),('Todos','*.*')])
        if not path: return
        try:
            write_off_file(self.poly,path,scale=float(self.off_mm_scale_var.get()),comments=bool(self.off_comments_var.get()))
            messagebox.showinfo('Exportar OFF em mm',f'Arquivo salvo em:\n{path}')
        except Exception as exc:
            messagebox.showerror('Exportar OFF em mm',str(exc))
    def export_off_summary_json_ui(self):
        if not self.poly: return
        path=filedialog.asksaveasfilename(title='Exportar resumo OFF/Antiprism JSON',defaultextension='.json',initialfile=safe_name(self.poly.name)+'_off_summary.json',filetypes=[('JSON','*.json'),('Todos','*.*')])
        if not path: return
        try:
            payload=current_poly_off_summary(self.poly)
            Path(path).write_text(json.dumps(payload,indent=2,ensure_ascii=False,default=str),encoding='utf-8')
            messagebox.showinfo('Resumo OFF/Antiprism',f'JSON salvo em:\n{path}')
        except Exception as exc:
            messagebox.showerror('Resumo OFF/Antiprism',str(exc))


_run_self_tests_before_v2509 = run_self_tests

def run_off_antiprism_self_tests():
    out=[]
    def add(name,ok,detail=''):
        out.append((name,bool(ok),detail))
    import tempfile
    cube=CATALOG['Platônicos / Cubo ou Hexaedro'].build()
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'cube.off'
        write_off_file(cube,p,scale=1.0)
        q=read_off_file(p)
        er=q.euler()
        add('OFF export/import cubo VEF', (er.V,er.E,er.F)==(8,12,6), (er.V,er.E,er.F))
        add('OFF import cubo fechado manifold', q.validate().closed and q.validate().manifold, q.validate())
        add('OFF relatório contém Antiprism', 'Antiprism' in off_antiprism_report(q))
        js=Path(td)/'summary.json'
        js.write_text(json.dumps(current_poly_off_summary(q),default=str),encoding='utf-8')
        add('OFF resumo JSON serializável', js.exists() and js.stat().st_size>20)
    # Testa variante OFF com contagens no cabeçalho e comentário.
    txt='''OFF 4 4 6\n# tetra\n1 1 1\n-1 -1 1\n-1 1 -1\n1 -1 -1\n3 0 2 1\n3 0 1 3\n3 0 3 2\n3 1 2 3\n'''
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'tetra_inline.off'; p.write_text(txt,encoding='utf-8')
        t=read_off_file(p); er=t.euler()
        add('OFF inline header tetra VEF', (er.V,er.E,er.F)==(4,6,4), (er.V,er.E,er.F))
    return out


def run_self_tests():
    rep=_run_self_tests_before_v2509()
    results=list(rep.results)
    for name,ok,detail in run_off_antiprism_self_tests():
        results.append(TestCaseResult('v25.0.10 / '+name,bool(ok),'' if ok else str(detail)))
    return TestReport(results)




# v27.2f: explicit export list so internal star imports preserve historical
# single-underscore helper symbols without using wholesale update calls.
__all__ = [k for k in globals() if not k.startswith('__')]
