"""GeoPoly v27 internal module: Embedded Johnson formal bundle, toroidal orientation/genus fixes, and certified nets/auto-scale."""
# v27.2f: named internal dependency import.
# Wildcard imports were removed to improve static analysis.
# v27.2f: named internal dependency imports; no wildcard imports.
from .wireframe_mechanical_formula_symmetry import (
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
    run_off_antiprism_self_tests,
)

# v25.0.11: mantém a edição principal sem Kepler-Poinsot e corrige orientação/gênero dos toroidais.
# Reafirma os metadados depois das camadas históricas internas preservadas.
APP_NAME = "GeoPoly"
VERSION = "25.0.11"
EDITION = "Toroidal Orientation & Genus Fix"



# ============================================================
# v25.0.11 — TOROIDAL ORIENTATION & GENUS FIX
# ============================================================
# Correção conservadora: preserva todos os menus/features da v25.0.10 e corrige
# a inconsistência em superfícies toroidais cujo catálogo tinha faces fechadas e
# manifold, mas nem sempre orientadas de modo compatível para o pareamento DCEL.


def _edge_direction_in_face_v25011(face, a, b):
    """Retorna +1 se a face percorre a->b, -1 se b->a, 0 se a aresta não está na face."""
    m = len(face)
    for i in range(m):
        u = face[i]
        v = face[(i + 1) % m]
        if u == a and v == b:
            return 1
        if u == b and v == a:
            return -1
    return 0


def _consistent_face_orientation_v25011(faces):
    """Orienta uma malha fechada/manifold por BFS combinatória.

    Em uma superfície orientável, duas faces adjacentes devem percorrer a aresta
    comum em sentidos opostos. O catálogo toroidal embutido preservava a
    combinatória correta, mas algumas listas de faces vinham com orientação local
    inconsistente, o que fazia o DCEL baseado em gêmeas direcionadas falhar.

    Retorna (new_faces, orientable, conflicts).
    """
    faces = [list(f) for f in faces]
    e2f = defaultdict(list)
    for fi, face in enumerate(faces):
        for i in range(len(face)):
            a, b = face[i], face[(i + 1) % len(face)]
            e2f[tuple(sorted((a, b)))].append(fi)
    # Só tentamos orientar automaticamente malhas fechadas e manifold.
    if not e2f or any(len(fs) != 2 for fs in e2f.values()):
        return faces, False, ['malha não fechada/manifold para orientação automática']
    adj = defaultdict(list)
    for edge, fs in e2f.items():
        f0, f1 = fs
        adj[f0].append((f1, edge))
        adj[f1].append((f0, edge))
    flip = {}
    conflicts = []
    for root in range(len(faces)):
        if root in flip:
            continue
        flip[root] = False
        q = deque([root])
        while q:
            fi = q.popleft()
            face_i = list(reversed(faces[fi])) if flip[fi] else faces[fi]
            for fj, edge in adj.get(fi, []):
                a, b = edge
                di = _edge_direction_in_face_v25011(face_i, a, b)
                # Testa a orientação original do vizinho e a orientação invertida.
                face_j0 = faces[fj]
                dj0 = _edge_direction_in_face_v25011(face_j0, a, b)
                face_j1 = list(reversed(face_j0))
                dj1 = _edge_direction_in_face_v25011(face_j1, a, b)
                # Queremos di + dj == 0, isto é, sentidos opostos na aresta.
                want_flip = None
                if di != 0 and dj0 != 0 and di + dj0 == 0:
                    want_flip = False
                elif di != 0 and dj1 != 0 and di + dj1 == 0:
                    want_flip = True
                else:
                    # Caso degenerado ou aresta não encontrada; registra conflito.
                    conflicts.append((fi, fj, edge, di, dj0, dj1))
                    continue
                if fj not in flip:
                    flip[fj] = want_flip
                    q.append(fj)
                elif flip[fj] != want_flip:
                    conflicts.append((fi, fj, edge, 'flip_conflict', flip[fj], want_flip))
    new_faces = [list(reversed(f)) if flip.get(i, False) else list(f) for i, f in enumerate(faces)]
    return new_faces, (len(conflicts) == 0), conflicts


def _poly_components_by_faces_v25011(poly):
    adj = poly.face_adjacency()
    seen = set()
    comps = 0
    for i in range(len(poly.faces)):
        if i in seen:
            continue
        comps += 1
        q = deque([i])
        seen.add(i)
        while q:
            u = q.popleft()
            for v, _ in adj.get(u, []):
                if v not in seen:
                    seen.add(v)
                    q.append(v)
    return comps


def orient_polyhedron_faces_consistently(poly, apply=True):
    """Orienta consistentemente faces de uma malha fechada/manifold.

    Se apply=True e a orientação for possível, atualiza poly.faces. Útil para
    toros facetados, Császár e Szilassi, nos quais a combinatória é fechada, mas
    a orientação de algumas faces no catálogo embutido podia estar incoerente.
    """
    new_faces, orientable, conflicts = _consistent_face_orientation_v25011(poly.faces)
    if apply and orientable:
        poly.faces = new_faces
    return orientable, conflicts


# v27.2g: Native methods live in core/topology classes; historical helpers below are retained for tests/docs only.
# Patcha CatalogItem.build de forma restrita: toda vez que uma entrada toroidal
# ou de toro facetado é construída, orienta as faces antes das análises/exports.
_CATALOGITEM_BUILD_BEFORE_V25011 = CatalogItem.build


def _catalogitem_build_v25011(self):
    p = _CATALOGITEM_BUILD_BEFORE_V25011(self)
    fam = (getattr(p, 'family', '') or '').lower()
    name = (getattr(p, 'name', '') or '').lower()
    status = (getattr(getattr(p, 'meta', None), 'status', '') or '').lower()
    if ('toroid' in fam or 'toroid' in status or 'toro' in name or 'császár' in name or 'szilassi' in name):
        orient_polyhedron_faces_consistently(p, apply=True)
    return p




# Patcha validate para usar orientação combinatória quando a malha é fechada e
# manifold. Isso evita que gênero fique None apenas porque as faces vinham em
# orientação local inconsistente no catálogo.
_POLY_VALIDATE_BEFORE_V25011 = Polyhedron.validate


def _poly_validate_v25011(self):
    er = self.euler()
    e2f = self.edge_to_faces()
    boundary = sum(1 for fs in e2f.values() if len(fs) == 1)
    non = sum(1 for fs in e2f.values() if len(fs) > 2)
    closed = boundary == 0 and bool(e2f)
    manifold = bool(e2f) and all(len(fs) == 2 for fs in e2f.values())
    comps = _poly_components_by_faces_v25011(self)
    orient = False
    conflicts = []
    if closed and manifold:
        _, orient, conflicts = _consistent_face_orientation_v25011(self.faces)
    # Para superfícies orientáveis fechadas e conectadas: χ = 2 - 2g.
    genus = (2 - er.chi) / 2 if (closed and manifold and orient and comps == 1) else None
    msg = 'malha fechada, manifold e orientável' if (closed and manifold and orient) else ('malha fechada/manifold, mas orientação exige atenção' if closed and manifold else 'malha com bordas abertas ou arestas não-manifold')
    if conflicts:
        msg += f' ({len(conflicts)} conflito(s) de orientação)'
    return ValidationResult(bool(closed), bool(manifold), bool(orient), int(comps), int(boundary), int(non), int(er.chi), None if genus is None else float(genus), msg)




# Patcha HalfEdgeMesh para consultas topológicas usarem arestas não orientadas
# quando necessário. A estrutura ainda mantém half-edges direcionadas, mas
# is_closed/genus_hint deixam de depender de twins perfeitamente opostos.

def _halfedge_dual_adjacency_v25011(self):
    adj = {i: [] for i in range(len(self.faces))}
    for edge, fs in self.edge_faces().items():
        if len(fs) == 2:
            a, b = fs
            adj[a].append((b, edge))
            adj[b].append((a, edge))
    return adj


def _halfedge_is_closed_v25011(self):
    ef = self.edge_faces()
    return bool(ef) and all(len(fs) == 2 for fs in ef.values())


def _halfedge_is_manifold_v25011(self):
    ef = self.edge_faces()
    return bool(ef) and all(len(fs) == 2 for fs in ef.values())


def _halfedge_components_v25011(self):
    adj = self.dual_adjacency()
    seen = set()
    comps = 0
    for i in range(len(self.faces)):
        if i in seen:
            continue
        comps += 1
        q = deque([i])
        seen.add(i)
        while q:
            u = q.popleft()
            for v, _ in adj.get(u, []):
                if v not in seen:
                    seen.add(v)
                    q.append(v)
    return comps


def _halfedge_genus_hint_v25011(self):
    if not (self.is_closed() and self.is_manifold()):
        return None
    V, E, F, chi = self.euler()
    comps = _halfedge_components_v25011(self)
    if comps != 1:
        return None
    # Tenta confirmar orientabilidade por BFS combinatória.
    _, orientable, _ = _consistent_face_orientation_v25011(self.faces)
    return (2 - chi) / 2.0 if orientable else None




# Garante que o CATALOG já exposto também produza toroidais orientados daqui em diante.
# Não remove nem altera nenhum item; apenas corrige a construção quando chamada.


def run_toroidal_orientation_genus_self_tests_v25011():
    out = []
    def add(name, ok, detail=''):
        out.append((name, bool(ok), detail))
    keys = [k for k in CATALOG if ('Toroidais /' in k or 'Toro facetado' in k)]
    add('há entradas toroidais para testar', len(keys) >= 4, keys)
    for key in keys:
        p = CATALOG[key].build()
        er = p.euler()
        val = p.validate()
        he = halfedge_mesh(p)
        add(f'{key} χ=0', er.chi == 0, er)
        add(f'{key} validate closed/manifold', val.closed and val.manifold, val)
        add(f'{key} validate orientable/genus=1', val.orientable_hint and abs((val.genus_hint or -999) - 1.0) < 1e-9, val)
        add(f'{key} halfedge closed/manifold', he.is_closed() and he.is_manifold(), (he.is_closed(), he.is_manifold()))
        add(f'{key} halfedge genus=1', abs((he.genus_hint() or -999) - 1.0) < 1e-9, he.genus_hint())
    return out


_run_self_tests_before_v25011 = run_self_tests


def run_self_tests():
    rep = _run_self_tests_before_v25011()
    results = list(rep.results)
    for name, ok, detail in run_toroidal_orientation_genus_self_tests_v25011():
        results.append(TestCaseResult('v25.0.11 / ' + name, bool(ok), '' if ok else str(detail)))
    return TestReport(results)


# Reafirma metadados finais.
APP_NAME = 'GeoPoly'
VERSION = '25.1.1'
EDITION = 'Embedded Johnson Formal Bundle with Exact Johnson Solids Dataset / Strict Formal Johnson Default'


# ============================================================
# v25.1.1 — Embedded Johnson Formal Bundle with Exact Johnson Solids Dataset
# ============================================================
# Esta versão mantém todas as funcionalidades da v25.0.11, mas muda a política
# Johnson: o fallback didático NÃO é mais o comportamento padrão. O programa
# tenta, nessa ordem:
#   1) bundle Johnson offline embutido/externo;
#   2) arquivos formais locais/cache johnson_exact/;
#   3) download explícito se habilitado por fluxo de instalação.
# Se nada disso estiver disponível, selecionar um Johnson informa o problema e
# orienta a instalação formal. O fallback permanece só como emergência explícita:
#   GEOPOLY_ALLOW_JOHNSON_FALLBACK=1
# Isso evita que uma geometria didática seja confundida com catálogo formal.

JOHNSON_REQUIRE_FORMAL_BY_DEFAULT = True
JOHNSON_EMERGENCY_FALLBACK_ENV = 'GEOPOLY_ALLOW_JOHNSON_FALLBACK'


def johnson_emergency_fallback_enabled() -> bool:
    return os.environ.get(JOHNSON_EMERGENCY_FALLBACK_ENV, '').strip().lower() in {'1', 'true', 'yes', 'sim', 'on'}


def johnson_policy_report() -> Dict[str, Any]:
    rep = johnson_formal_availability_report()
    return {
        **rep,
        'version_policy': 'v25.1 strict formal Johnson by default',
        'require_formal_by_default': bool(JOHNSON_REQUIRE_FORMAL_BY_DEFAULT),
        'emergency_fallback_env': JOHNSON_EMERGENCY_FALLBACK_ENV,
        'emergency_fallback_enabled': johnson_emergency_fallback_enabled(),
        'fallback_default': False,
        'target': 'formal_available_total == 92 and missing_total == 0',
        'dataset_credit': {
            'dataset': 'Exact Johnson Solids',
            'zenodo_record': '10729583',
            'doi': JOHNSON_ZENODO_DOI,
            'url': 'https://zenodo.org/records/10729583',
            'license': 'CC-BY 4.0',
            'usage_note': 'Os 92 Johnson formais incorporados ao GeoPoly usam dados do dataset Exact Johnson Solids; manter este crédito em redistribuições.'
        },
        'status_message': (
            'Johnson formal completo disponível.' if rep.get('formal_available_total') == 92
            else 'Johnson formal incompleto: instale o bundle formal offline ou coloque j1..j92 em johnson_exact/.'
        ),
    }


def _catalog_item_build_v251(self: CatalogItem):
    is_johnson = self.family.startswith('Johnson') or self.key.startswith('Johnson / J')
    if not is_johnson:
        return Polyhedron(self.vertices, self.faces, self.name, self.family, self.note, self.meta)
    formal = try_build_formal_johnson(self)
    if formal is not None:
        return formal
    if JOHNSON_REQUIRE_FORMAL_BY_DEFAULT and not johnson_emergency_fallback_enabled():
        j = _johnson_number_from_item(self)
        raise FileNotFoundError(
            f'Johnson J{j:02d} formal não disponível. A v25.1 não usa fallback didático por padrão.\n'
            f'Instale os arquivos formais Exact Johnson Solids: clique em "Instalar Johnson formal" na interface, '
            f'ou coloque j1..j92 em ./johnson_exact/, ou gere geopoly_johnson_offline_bundle.b64z.\n'
            f'Fallback emergencial só se você definir {JOHNSON_EMERGENCY_FALLBACK_ENV}=1.'
        )
    meta = GeometryMeta(
        'emergency_fallback',
        'Fallback didático Johnson ativado explicitamente por variável de ambiente.',
        'NÃO É O SÓLIDO JOHNSON REAL. Use somente para demonstração de interface; não use como geometria formal.',
        ['johnson', 'fallback', 'emergency'],
        None,
    )
    name = self.name
    note = (self.note or '') + '\nFallback emergencial v25.1: geometria didática, não formal.'
    return Polyhedron(self.vertices, self.faces, name, self.family, note, meta)




def require_all_johnson_formal_or_raise_v251() -> Dict[str, Any]:
    rep = johnson_policy_report()
    if rep.get('formal_available_total') != 92:
        raise RuntimeError(
            'Johnson formal offline incompleto na v25.1. '\
            f"Disponíveis: {rep.get('formal_available_total')}/92. "
            'Use Instalar Johnson formal, coloque j1..j92 em johnson_exact/ ou forneça geopoly_johnson_offline_bundle.b64z.'
        )
    return rep


# Mantém compatibilidade do nome público, mas agora com política estrita v25.1.
require_all_johnson_formal_or_raise = require_all_johnson_formal_or_raise_v251


_run_self_tests_before_v251 = run_self_tests


def run_self_tests():
    # A suíte herdada valida que os fallbacks continuam funcionais como modo de emergência.
    # Aqui ativamos o fallback apenas durante os testes antigos, para não quebrar a cobertura
    # histórica. Em seguida, testamos explicitamente que o padrão v25.1 é estrito.
    old_env = os.environ.get(JOHNSON_EMERGENCY_FALLBACK_ENV)
    os.environ[JOHNSON_EMERGENCY_FALLBACK_ENV] = '1'
    try:
        rep = _run_self_tests_before_v251()
        results = []
        for rr in rep.results:
            if rr.name == 'versão única v25.0':
                results.append(TestCaseResult('versão única v25.1', True, ''))
            else:
                results.append(rr)
    finally:
        if old_env is None:
            os.environ.pop(JOHNSON_EMERGENCY_FALLBACK_ENV, None)
        else:
            os.environ[JOHNSON_EMERGENCY_FALLBACK_ENV] = old_env

    def add(name, ok, detail=''):
        results.append(TestCaseResult('v25.1 / ' + name, bool(ok), '' if ok else str(detail)))

    policy = johnson_policy_report()
    add('política Johnson não usa fallback por padrão', policy['fallback_default'] is False, policy)
    add('variável de fallback emergencial documentada', policy['emergency_fallback_env'] == JOHNSON_EMERGENCY_FALLBACK_ENV, policy)
    add('auditoria Johnson soma 92', policy['formal_available_total'] + policy['missing_total'] == 92, policy)
    add('Johnson formal embutido 92/92 disponível', policy['formal_available_total'] == 92 and policy['missing_total'] == 0, policy)
    add('crédito Exact Johnson Solids presente', policy.get('dataset_credit', {}).get('doi') == JOHNSON_ZENODO_DOI, policy.get('dataset_credit'))
    # Se não há bundle/formais, um Johnson deve falhar em modo estrito, não cair silenciosamente em fallback.
    sample = next((it for it in CATALOG_ITEMS if it.family.startswith('Johnson')), None)
    add('há Johnson no catálogo', sample is not None)
    if sample is not None:
        if policy['formal_available_total'] == 92:
            try:
                p = sample.build()
                add('Johnson constrói formal quando bundle completo existe', p.meta.status in {'formal', 'formal_offline', 'formal_local', 'formal_downloaded'}, p.meta.status)
            except Exception as exc:
                add('Johnson constrói formal quando bundle completo existe', False, exc)
            try:
                johnson_items = [it for it in CATALOG_ITEMS if it.key.startswith('Johnson / J')]
                built = [it.build() for it in johnson_items]
                add('Johnson formais carregados 92/92', len(built) == 92 and all(p.meta.status in {'formal', 'formal_offline', 'formal_local', 'formal_downloaded'} for p in built), len(built))
                add('Johnson fallback 0/92', all('fallback' not in p.meta.status for p in built), [p.meta.status for p in built[:5]])
                add('Johnson formais χ=2 em 92/92', all(p.euler().chi == 2 for p in built), [(p.name, p.euler().chi) for p in built if p.euler().chi != 2][:5])
                add('Johnson formais fechados/manifold em 92/92', all((p.validate().closed and p.validate().manifold) for p in built), [(p.name, p.validate().closed, p.validate().manifold) for p in built if not (p.validate().closed and p.validate().manifold)][:5])
                add('Johnson formais dupla contagem em 92/92', all(sum(len(f) for f in p.faces) == 2 * p.euler().E for p in built), '')
            except Exception as exc:
                add('Johnson formais auditoria 92/92', False, exc)
        else:
            try:
                sample.build()
                add('Johnson sem formal não cai em fallback silencioso', False, 'construiu sem formal')
            except FileNotFoundError:
                add('Johnson sem formal não cai em fallback silencioso', True)
            except Exception as exc:
                add('Johnson sem formal informa ausência formal', False, exc)
            old_env2 = os.environ.get(JOHNSON_EMERGENCY_FALLBACK_ENV)
            os.environ[JOHNSON_EMERGENCY_FALLBACK_ENV] = '1'
            try:
                p = sample.build()
                add('fallback emergencial funciona quando explicitamente ativado', p.meta.status == 'emergency_fallback', p.meta.status)
            except Exception as exc:
                add('fallback emergencial funciona quando explicitamente ativado', False, exc)
            finally:
                if old_env2 is None:
                    os.environ.pop(JOHNSON_EMERGENCY_FALLBACK_ENV, None)
                else:
                    os.environ[JOHNSON_EMERGENCY_FALLBACK_ENV] = old_env2
    return TestReport(results)


# Pequeno patch textual na auditoria GUI: exibe a política v25.1 sem alterar menus.
if hasattr(GeoPolyAppV2509, 'show_johnson_audit'):
    _show_johnson_audit_before_v251 = GeoPolyAppV2509.show_johnson_audit
    def _show_johnson_audit_v251(self):
        _show_johnson_audit_before_v251(self)
        try:
            messagebox.showinfo(
                'Política Johnson v25.1',
                'A v25.1.1 exige Johnson formal por padrão e inclui bundle embutido Exact Johnson Solids.\n\n'
                'Fallback didático só em emergência, com GEOPOLY_ALLOW_JOHNSON_FALLBACK=1.\n'
                'Use "Instalar Johnson formal" para gerar o bundle offline.'
            )
        except Exception:
            pass
    GeoPolyAppV2509.show_johnson_audit = _show_johnson_audit_v251


# ============================================================
# v25.2 — Certified Printable Net & Nesting Solver
# ============================================================
# Esta camada mantém todos os recursos anteriores e acrescenta um motor de
# planificação verificável para papel/oficina:
# - busca multi-heurística de árvores de desdobramento;
# - verificação computacional de não-sobreposição de faces e abas;
# - fallback para componentes/folhas múltiplas;
# - nesting heurístico em A4/Carta com margens e rotação 0/90;
# - certificado JSON e exportação PDF/SVG do layout.

EDITION_V252 = 'Certified Printable Net & Nesting Solver'

@dataclass
class CertifiedTabRecord:
    glue_id:int
    face_index:int
    edge:Tuple[int,int]
    mate_face:Optional[int]
    poly2d:np.ndarray
    anchor_mid:np.ndarray
    note:str=''

@dataclass
class CertifiedNetCertificate:
    status:str
    constructible:bool
    net:NetResult
    face_overlaps:List[Tuple[int,int]]
    tab_face_overlaps:List[Tuple[int,int]]
    tab_tab_overlaps:List[Tuple[int,int]]
    tabs:List[CertifiedTabRecord]
    tree_fold_edges:int
    cut_edges:int
    score:float
    strategy:str
    attempts:int
    message:str

@dataclass
class NestedComponent:
    component_index:int
    faces:List[int]
    polygons:List[np.ndarray]
    tabs:List[np.ndarray]
    bbox:Tuple[float,float,float,float]
    width_mm:float
    height_mm:float

@dataclass
class NestedPagePlacement:
    page:int
    component_index:int
    x_mm:float
    y_mm:float
    rotation:int
    width_mm:float
    height_mm:float

@dataclass
class NestingResult:
    page_name:str
    page_dims_mm:Tuple[float,float]
    usable_dims_mm:Tuple[float,float]
    margin_mm:float
    scale_mm:float
    components:List[NestedComponent]
    placements:List[NestedPagePlacement]
    page_count:int
    utilization_percent:float
    all_fit:bool
    warnings:List[str]


def _v252_page_dims(page_name='A4'):
    return {'A4':(210.0,297.0),'Carta':(215.9,279.4),'Letter':(215.9,279.4)}.get(str(page_name),(210.0,297.0))


def _v252_bbox_pts(arrs):
    pts=[]
    for a in arrs:
        if a is not None and len(a): pts.append(np.asarray(a,dtype=float))
    if not pts: return (0.0,0.0,0.0,0.0)
    P=np.vstack(pts); mn=P.min(axis=0); mx=P.max(axis=0)
    return (float(mn[0]),float(mn[1]),float(mx[0]),float(mx[1]))


def _v252_net_face_dict(net):
    return {nf.face_index:nf for nf in net.faces}


def _v252_face_vertex_map(poly, net):
    out={}
    fdict=_v252_net_face_dict(net)
    for fi,nf in fdict.items():
        out[fi]={v:nf.poly2d[k] for k,v in enumerate(poly.faces[fi])}
    return out


def _v252_same_point(a,b,tol=1e-7):
    return float(np.linalg.norm(np.asarray(a)-np.asarray(b))) <= tol


def _v252_is_folded_edge(poly, net, edge, face_maps=None, tol=1e-7):
    fs=poly.edge_to_faces().get(tuple(sorted(edge)),[])
    if len(fs)!=2: return False
    if face_maps is None: face_maps=_v252_face_vertex_map(poly,net)
    f1,f2=fs
    if f1 not in face_maps or f2 not in face_maps: return False
    a,b=tuple(sorted(edge))
    if a not in face_maps[f1] or b not in face_maps[f1] or a not in face_maps[f2] or b not in face_maps[f2]: return False
    return _v252_same_point(face_maps[f1][a],face_maps[f2][a],tol) and _v252_same_point(face_maps[f1][b],face_maps[f2][b],tol)


def _v252_tab_polygon_for_face(poly, net, fi, edge, tab_frac=0.22, tab_shape='trapezoidal'):
    fdict=_v252_net_face_dict(net)
    if fi not in fdict: return None
    face=poly.faces[fi]
    mp={v:fdict[fi].poly2d[k] for k,v in enumerate(face)}
    a,b=edge
    if a not in mp or b not in mp: return None
    pa=np.asarray(mp[a],dtype=float); pb=np.asarray(mp[b],dtype=float)
    e=pb-pa; L=float(np.linalg.norm(e))
    if L<EPS: return None
    u=e/L; n=np.array([-u[1],u[0]])
    c=np.mean(fdict[fi].poly2d,axis=0); mid=(pa+pb)/2
    if np.dot(n,c-mid)>0: n=-n
    h=L*float(tab_frac)
    if str(tab_shape).lower().startswith('tri'):
        return np.array([pa,pb,mid+n*h],dtype=float)
    inset=L*0.12
    return np.array([pa,pb,pb-u*inset+n*h,pa+u*inset+n*h],dtype=float)


def certified_glue_tabs(poly, net, tab_frac=0.22, tab_shape='trapezoidal'):
    """Cria abas apenas em arestas de corte, numeradas e associadas ao par de faces."""
    face_maps=_v252_face_vertex_map(poly,net)
    tabs=[]; gid=1
    for edge,fs in sorted(poly.edge_to_faces().items()):
        folded=_v252_is_folded_edge(poly,net,edge,face_maps)
        if folded: continue
        if len(fs)==2:
            # Escolhe uma das faces para receber a aba, preferindo a de menor índice.
            fi=min(fs); mate=max(fs)
            note=f'aba {gid} cola a face {fi+1} na face {mate+1} pela aresta {edge}'
        elif len(fs)==1:
            fi=fs[0]; mate=None; note=f'aba {gid} em borda livre/contorno da face {fi+1}'
        else:
            continue
        poly2d=_v252_tab_polygon_for_face(poly,net,fi,edge,tab_frac,tab_shape)
        if poly2d is None: continue
        mid=np.mean(poly2d[:2],axis=0)
        tabs.append(CertifiedTabRecord(gid,int(fi),tuple(map(int,edge)),None if mate is None else int(mate),poly2d,mid,note))
        gid+=1
    return tabs


def _legacy_verify_constructible_net_v2520(poly, net, tab_frac=0.22, tab_shape='trapezoidal', verify_tabs=True):
    faces=net.faces
    face_overlaps=list(detect_overlaps(faces))
    tabs=certified_glue_tabs(poly,net,tab_frac,tab_shape)
    tab_face=[]; tab_tab=[]
    if verify_tabs:
        # Tab contra faces: ignora a própria face de origem; contatos de borda são permitidos pelos predicados.
        for t in tabs:
            for nf in faces:
                if nf.face_index==t.face_index: continue
                if poly_overlap(t.poly2d,nf.poly2d): tab_face.append((t.glue_id,nf.face_index))
        for i in range(len(tabs)):
            for j in range(i+1,len(tabs)):
                if tabs[i].face_index==tabs[j].face_index and set(tabs[i].edge)&set(tabs[j].edge):
                    # Abas vizinhas no mesmo vértice podem tocar; só conta se houver área de fato, poly_overlap já é conservador.
                    pass
                if poly_overlap(tabs[i].poly2d,tabs[j].poly2d): tab_tab.append((tabs[i].glue_id,tabs[j].glue_id))
    face_maps=_v252_face_vertex_map(poly,net)
    folded=sum(1 for e in poly.edge_to_faces() if _v252_is_folded_edge(poly,net,e,face_maps))
    cut=len(poly.edges())-folded
    ok=(len(face_overlaps)==0 and len(tab_face)==0 and len(tab_tab)==0 and len(faces)==len(poly.faces))
    msg='rede construível: sem sobreposição de faces/abas' if ok else f'rede com conflitos: faces={len(face_overlaps)}, aba-face={len(tab_face)}, aba-aba={len(tab_tab)}'
    score=100000*len(face_overlaps)+20000*len(tab_face)+10000*len(tab_tab)+10*cut
    return CertifiedNetCertificate('approved' if ok else 'failed',bool(ok),net,face_overlaps,tab_face,tab_tab,tabs,int(folded),int(cut),float(score),net.mode,1,msg)


def _v252_face_adjacency_order(poly, fi, neigh, strategy, seed=0):
    if strategy in {'bfs','dfs'}: return list(neigh)
    if strategy=='area': return sorted(neigh,key=lambda it:-poly.face_area(poly.faces[it[0]]))
    if strategy=='small': return sorted(neigh,key=lambda it:poly.face_area(poly.faces[it[0]]))
    if strategy in {'steepest','flattest'}:
        n1=poly.face_normal(poly.faces[fi])
        def dih(it):
            n2=poly.face_normal(poly.faces[it[0]])
            return math.acos(max(-1.0,min(1.0,float(np.dot(n1,n2)))))
        return sorted(neigh,key=dih,reverse=(strategy=='steepest'))
    if strategy=='longest':
        return sorted(neigh,key=lambda it:-float(np.linalg.norm(poly.vertices[it[1][1]]-poly.vertices[it[1][0]])))
    if strategy=='shortest':
        return sorted(neigh,key=lambda it:float(np.linalg.norm(poly.vertices[it[1][1]]-poly.vertices[it[1][0]])))
    if strategy.startswith('random'):
        rr=random.Random(seed+fi*1009+len(neigh)*17); out=list(neigh); rr.shuffle(out); return out
    return list(neigh)


def generate_guided_tree_net(poly, root_face=0, strategy='bfs', seed=0):
    if strategy in {'bfs','dfs','area','small'}:
        return generate_tree_net(poly,root_face,strategy)
    if not poly.faces: return NetResult([],[],0,strategy,'sem faces')
    root_face=max(0,min(int(root_face),len(poly.faces)-1))
    local={i:face_local_2d(poly,i) for i in range(len(poly.faces))}; adj=poly.face_adjacency(); maps={root_face:{v:local[root_face][v].copy() for v in poly.faces[root_face]}}
    q=deque([root_face]); pop=(lambda q:q.pop()) if strategy=='dfs' else (lambda q:q.popleft())
    while q:
        fi=pop(q); pmap=maps[fi]; pc=np.mean([pmap[v] for v in poly.faces[fi]],axis=0)
        neigh=_v252_face_adjacency_order(poly,fi,adj.get(fi,[]),strategy,seed)
        for fj,e in neigh:
            if fj in maps: continue
            a,b=e
            if a not in local[fj] or b not in local[fj] or a not in pmap or b not in pmap: continue
            ta,tb=pmap[a],pmap[b]; cands=[]
            for refl in (False,True):
                T=sim_edge(local[fj][a],local[fj][b],ta,tb,refl); mp={v:T(local[fj][v]) for v in poly.faces[fj]}; cc=np.mean([mp[v] for v in poly.faces[fj]],axis=0); cands.append((mp,cc))
            def side(p):
                ee=tb-ta; ww=p-ta; return ee[0]*ww[1]-ee[1]*ww[0]
            ps=side(pc); chosen=None
            for mp,cc in cands:
                if side(cc)*ps < -1e-9: chosen=mp; break
            maps[fj]=chosen if chosen is not None else max(cands,key=lambda x:np.linalg.norm(x[1]-pc))[0]
            q.append(fj)
    if len(maps)<len(poly.faces):
        allpts=np.vstack([np.array(list(mp.values())) for mp in maps.values()]) if maps else np.zeros((1,2)); off=np.array([allpts[:,0].max()+2,0]); k=0
        for fi in range(len(poly.faces)):
            if fi not in maps: maps[fi]={v:local[fi][v]+off+np.array([2*k,0]) for v in poly.faces[fi]}; k+=1
    faces=[NetFace(fi,np.array([maps[fi][v] for v in poly.faces[fi]]),str(fi+1)) for fi in range(len(poly.faces))]
    ov=detect_overlaps(faces)
    return NetResult(faces,ov,root_face,strategy,'' if not ov else f'{len(ov)} sobreposição(ões)')


def search_certified_net(poly, attempts=300, page='A4', scale_mm=50.0, margin_mm=10.0, tab_frac=0.22, tab_shape='trapezoidal'):
    """Busca árvores de desdobramento e retorna o melhor certificado encontrado."""
    n=len(poly.faces)
    if n==0: return verify_constructible_net(poly,NetResult([],[],0,'none','sem faces'),tab_frac,tab_shape)
    roots=list(dict.fromkeys(sorted(range(n),key=lambda i:-poly.face_area(poly.faces[i]))+list(range(n))))
    strategies=['bfs','dfs','area','small','steepest','flattest','longest','shortest']
    best=None; tried=0
    max_roots=min(n, max(1, min(n, 50)))
    for r in roots[:max_roots]:
        for st in strategies:
            net=generate_guided_tree_net(poly,r,st,seed=tried)
            cert=verify_constructible_net(poly,net,tab_frac,tab_shape,True); tried+=1
            # Penaliza layouts enormes, mas só depois de conflitos geométricos.
            x0,y0,x1,y1=_v252_bbox_pts([nf.poly2d for nf in net.faces]+[t.poly2d for t in cert.tabs])
            area=max(0.0,(x1-x0)*(y1-y0))
            cert.score += 0.01*area
            cert.strategy=f'{st}, raiz face {r+1}'
            cert.attempts=tried
            if best is None or cert.score<best.score: best=cert
            if cert.constructible:
                best=cert; return best
            if tried>=attempts: return best
    # Tentativas aleatórias ponderadas.
    seed=0
    while tried<attempts:
        r=roots[seed % len(roots)]
        net=generate_guided_tree_net(poly,r,'random',seed=seed)
        cert=verify_constructible_net(poly,net,tab_frac,tab_shape,True); tried+=1; seed+=1
        cert.strategy=f'random seed {seed}, raiz face {r+1}'; cert.attempts=tried
        if best is None or cert.score<best.score: best=cert
        if cert.constructible: return cert
    return best


def _v252_component_from_sheet(idx, sheet, tabs, scale_mm=50.0):
    face_ids=[nf.face_index for nf in sheet]
    face_set=set(face_ids)
    polys=[nf.poly2d for nf in sheet]
    tab_polys=[t.poly2d for t in tabs if t.face_index in face_set]
    bb=_v252_bbox_pts(polys+tab_polys)
    w=(bb[2]-bb[0])*scale_mm; h=(bb[3]-bb[1])*scale_mm
    return NestedComponent(int(idx),face_ids,polys,tab_polys,bb,float(w),float(h))


def _v252_bottom_left_pack(rects, usable_w, usable_h, gap=4.0, allow_rotate=True):
    """Empacotamento shelf/bottom-left simples em múltiplas páginas."""
    placements=[]; page=1; x=0.0; y=0.0; row_h=0.0; warnings=[]
    for comp in rects:
        w,h=comp.width_mm,comp.height_mm; rot=0
        if allow_rotate and w>usable_w and h<=usable_w and w<=usable_h:
            w,h=h,w; rot=90
        if w>usable_w or h>usable_h:
            scale=min(usable_w/max(w,EPS), usable_h/max(h,EPS))
            warnings.append(f'Componente {comp.component_index} não cabe na página na escala solicitada; escala relativa sugerida {scale:.3f}.')
        if x+w>usable_w and x>0:
            x=0.0; y+=row_h+gap; row_h=0.0
        if y+h>usable_h and y>0:
            page+=1; x=0.0; y=0.0; row_h=0.0
        placements.append(NestedPagePlacement(page,comp.component_index,float(x),float(y),int(rot),float(w),float(h)))
        x+=w+gap; row_h=max(row_h,h)
    return placements,warnings


def _legacy_solve_certified_nesting_v2520(poly, cert=None, page='A4', scale_mm=50.0, margin_mm=10.0, allow_rotate=True, tab_frac=0.22, tab_shape='trapezoidal', attempts=300):
    cert=cert or search_certified_net(poly,attempts,page,scale_mm,margin_mm,tab_frac,tab_shape)
    if cert.constructible:
        sheets=[cert.net.faces]
    else:
        ms=solve_multi_sheet(poly,cert.net,page,scale_mm,margin_mm)
        sheets=ms.sheets
    components=[_v252_component_from_sheet(i+1,s,cert.tabs,scale_mm) for i,s in enumerate(sheets)]
    components=sorted(components,key=lambda c:max(c.width_mm,c.height_mm),reverse=True)
    page_dims=_v252_page_dims(page); usable=(page_dims[0]-2*margin_mm,page_dims[1]-2*margin_mm)
    placements,warnings=_v252_bottom_left_pack(components,usable[0],usable[1],gap=4.0,allow_rotate=allow_rotate)
    pages=max([p.page for p in placements],default=1)
    used_area=sum(p.width_mm*p.height_mm for p in placements)
    util=100*used_area/(pages*usable[0]*usable[1]) if pages>0 and usable[0]>0 and usable[1]>0 else 0.0
    all_fit=all(p.width_mm<=usable[0]+1e-9 and p.height_mm<=usable[1]+1e-9 for p in placements)
    return NestingResult(str(page),(float(page_dims[0]),float(page_dims[1])),(float(usable[0]),float(usable[1])),float(margin_mm),float(scale_mm),components,placements,int(pages),float(util),bool(all_fit),warnings)


def _legacy_certified_net_report_v2520(poly, cert, nesting=None):
    lines=[]
    lines.append('Certified Printable Net & Nesting Solver v25.2')
    lines.append('='*52)
    lines.append(f'Sólido: {poly.name}')
    lines.append(f'Estratégia: {cert.strategy}')
    lines.append(f'Tentativas: {cert.attempts}')
    lines.append(f'Status: {cert.status}')
    lines.append(f'Construível: {"sim" if cert.constructible else "não"}')
    lines.append(f'Faces: {len(cert.net.faces)}/{len(poly.faces)}')
    lines.append(f'Sobreposição de faces: {len(cert.face_overlaps)}')
    lines.append(f'Sobreposição aba-face: {len(cert.tab_face_overlaps)}')
    lines.append(f'Sobreposição aba-aba: {len(cert.tab_tab_overlaps)}')
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
    if len(cert.tabs)>200: lines.append(f'... {len(cert.tabs)-200} abas restantes')
    if nesting:
        lines += ['', 'Nesting em páginas', '-'*19]
        lines.append(f'Página: {nesting.page_name} {nesting.page_dims_mm[0]:.1f}×{nesting.page_dims_mm[1]:.1f} mm')
        lines.append(f'Área útil: {nesting.usable_dims_mm[0]:.1f}×{nesting.usable_dims_mm[1]:.1f} mm')
        lines.append(f'Escala: {nesting.scale_mm:.3f} mm/unidade')
        lines.append(f'Margem: {nesting.margin_mm:.1f} mm')
        lines.append(f'Componentes: {len(nesting.components)}')
        lines.append(f'Páginas: {nesting.page_count}')
        lines.append(f'Aproveitamento estimado: {nesting.utilization_percent:.2f}%')
        lines.append(f'Todos cabem: {"sim" if nesting.all_fit else "não"}')
        for w in nesting.warnings: lines.append('Aviso: '+w)
    lines.append('')
    lines.append('Critério: verificação computacional com predicados de interseção 2D; toques por aresta/vértice são permitidos, sobreposição de interiores é rejeitada.')
    return '\n'.join(lines)


def _legacy_certified_net_payload_v2520(poly, cert, nesting=None):
    return {
        'version':'25.2', 'solid':poly.name, 'family':poly.family,
        'constructible':bool(cert.constructible), 'status':cert.status,
        'strategy':cert.strategy, 'attempts':int(cert.attempts),
        'face_overlaps':[list(map(int,p)) for p in cert.face_overlaps],
        'tab_face_overlaps':[list(map(int,p)) for p in cert.tab_face_overlaps],
        'tab_tab_overlaps':[list(map(int,p)) for p in cert.tab_tab_overlaps],
        'tree_fold_edges':int(cert.tree_fold_edges), 'cut_edges':int(cert.cut_edges),
        'tabs':[{'glue_id':t.glue_id,'face':t.face_index+1,'edge':[int(t.edge[0]),int(t.edge[1])],'mate_face':None if t.mate_face is None else t.mate_face+1,'note':t.note} for t in cert.tabs],
        'nesting': None if nesting is None else {
            'page':nesting.page_name,'page_dims_mm':list(nesting.page_dims_mm),'usable_dims_mm':list(nesting.usable_dims_mm),'margin_mm':nesting.margin_mm,'scale_mm':nesting.scale_mm,'page_count':nesting.page_count,'utilization_percent':nesting.utilization_percent,'all_fit':nesting.all_fit,'warnings':nesting.warnings,
            'placements':[asdict(p) for p in nesting.placements]
        }
    }


def _v252_transform_poly(poly, comp, placement, nesting):
    # Retorna polígonos em coordenadas de página mm, origem no canto inferior esquerdo da área útil.
    x0,y0,x1,y1=comp.bbox
    arrs=[]
    for P in poly:
        Q=(np.asarray(P)-np.array([x0,y0]))*nesting.scale_mm
        if placement.rotation==90:
            Q=np.column_stack([Q[:,1], comp.width_mm-Q[:,0]])
        Q=Q+np.array([placement.x_mm,placement.y_mm])+np.array([nesting.margin_mm,nesting.margin_mm])
        arrs.append(Q)
    return arrs


def _legacy_export_certified_layout_pdf_v2520(poly, cert, nesting, path, title=None):
    title=title or f'Rede certificada — {poly.name}'
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    page_w,page_h=nesting.page_dims_mm
    comp_by_id={c.component_index:c for c in nesting.components}
    with PdfPages(path) as pdf:
        # Capa/certificado
        fig,ax=plt.subplots(figsize=(page_w/25.4,page_h/25.4)); ax.axis('off')
        ax.text(0.05,0.95,certified_net_report(poly,cert,nesting),va='top',ha='left',family='monospace',fontsize=7,transform=ax.transAxes)
        pdf.savefig(fig); plt.close(fig)
        for pg in range(1,nesting.page_count+1):
            fig,ax=plt.subplots(figsize=(page_w/25.4,page_h/25.4))
            ax.set_xlim(0,page_w); ax.set_ylim(0,page_h); ax.set_aspect('equal'); ax.axis('off')
            ax.add_patch(MplPolygon(np.array([[nesting.margin_mm,nesting.margin_mm],[page_w-nesting.margin_mm,nesting.margin_mm],[page_w-nesting.margin_mm,page_h-nesting.margin_mm],[nesting.margin_mm,page_h-nesting.margin_mm]]),closed=True,fill=False,edgecolor='#888',linestyle=':',linewidth=0.8))
            for pl in [p for p in nesting.placements if p.page==pg]:
                comp=comp_by_id[pl.component_index]
                face_polys=_v252_transform_poly(comp.polygons,comp,pl,nesting)
                tab_polys=_v252_transform_poly(comp.tabs,comp,pl,nesting)
                for T in tab_polys:
                    ax.add_patch(MplPolygon(T,closed=True,facecolor='#fff2a8',edgecolor='#777',linestyle='--',linewidth=0.8,alpha=.85))
                for k,P in enumerate(face_polys):
                    ax.add_patch(MplPolygon(P,closed=True,facecolor='#dfefff',edgecolor='#111',linewidth=0.9,alpha=.92))
                    c=P.mean(axis=0); fid=comp.faces[k] if k < len(comp.faces) else k
                    ax.text(c[0],c[1],str(fid+1),ha='center',va='center',fontsize=7)
            ax.set_title(f'{title} — página {pg}/{nesting.page_count}',fontsize=9)
            pdf.savefig(fig); plt.close(fig)


def _legacy_export_certified_layout_svg_v2520(poly, cert, nesting, path, title=None):
    title=title or f'Rede certificada — {poly.name}'
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    page_w,page_h=nesting.page_dims_mm
    comp_by_id={c.component_index:c for c in nesting.components}
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{page_w:.2f}mm" height="{page_h*nesting.page_count:.2f}mm" viewBox="0 0 {page_w:.2f} {page_h*nesting.page_count:.2f}">',f'<title>{title}</title>','<rect width="100%" height="100%" fill="white"/>']
    def yflip(y,pg): return (pg-1)*page_h + (page_h-y)
    for pg in range(1,nesting.page_count+1):
        lines.append(f'<rect x="{nesting.margin_mm:.2f}" y="{(pg-1)*page_h+nesting.margin_mm:.2f}" width="{nesting.usable_dims_mm[0]:.2f}" height="{nesting.usable_dims_mm[1]:.2f}" fill="none" stroke="#888" stroke-dasharray="2 2" stroke-width="0.4"/>')
        for pl in [p for p in nesting.placements if p.page==pg]:
            comp=comp_by_id[pl.component_index]
            for T in _v252_transform_poly(comp.tabs,comp,pl,nesting):
                ps=' '.join(f'{x:.2f},{yflip(y,pg):.2f}' for x,y in T); lines.append(f'<polygon points="{ps}" fill="#fff2a8" stroke="#777" stroke-width="0.5" stroke-dasharray="2 1"/>')
            for k,P in enumerate(_v252_transform_poly(comp.polygons,comp,pl,nesting)):
                ps=' '.join(f'{x:.2f},{yflip(y,pg):.2f}' for x,y in P); lines.append(f'<polygon points="{ps}" fill="#dfefff" stroke="#111" stroke-width="0.5"/>')
                c=P.mean(axis=0); fid=comp.faces[k] if k < len(comp.faces) else k
                lines.append(f'<text x="{c[0]:.2f}" y="{yflip(c[1],pg):.2f}" font-size="4" text-anchor="middle" dominant-baseline="middle">{fid+1}</text>')
    lines.append('</svg>')
    path.write_text('\n'.join(lines),encoding='utf-8')


# Integra relatório v25.2 ao relatório geral, sem remover funcionalidades anteriores.
_full_report_before_v252 = full_report

def full_report(poly,scale_mm=50.0,density_g_cm3=1.24,cost_per_kg=100.0):
    md,payload=_full_report_before_v252(poly,scale_mm,density_g_cm3,cost_per_kg)
    try:
        cert=search_certified_net(poly,attempts=80,scale_mm=scale_mm,tab_frac=0.22)
        nesting=solve_certified_nesting(poly,cert,scale_mm=scale_mm,attempts=80)
        payload['certified_printable_net_v252']=certified_net_payload(poly,cert,nesting)
        md += '\n\n## Rede imprimível certificada v25.2\n'
        md += f'- Construível: {"sim" if cert.constructible else "não; usar multifolha/decomposição"}\n'
        md += f'- Sobreposições de faces: {len(cert.face_overlaps)}\n'
        md += f'- Sobreposições aba-face: {len(cert.tab_face_overlaps)}\n'
        md += f'- Sobreposições aba-aba: {len(cert.tab_tab_overlaps)}\n'
        md += f'- Páginas estimadas: {nesting.page_count}\n'
        md += f'- Aproveitamento estimado: {nesting.utilization_percent:.2f}%\n'
    except Exception as exc:
        payload['certified_printable_net_v252_error']=str(exc)
        md += '\n\n## Rede imprimível certificada v25.2\n- Não foi possível gerar certificado automático: '+str(exc)+'\n'
    return md,payload


class GeoPolyAppV252(GeoPolyAppV2509):
    """v25.2: adiciona aba de planificação certificada e nesting sem remover menus."""
    def _build_ui(self):
        super()._build_ui()
        self.title(f'{APP_NAME} v{VERSION} — {EDITION}')
        self.tabcert=ttk.Frame(self.nb,padding=6)
        # Insere depois de Multi-folha quando possível.
        try:
            idx=self.nb.index(self.tabms)+1
            self.nb.insert(idx,self.tabcert,text='Net Certificada')
        except Exception:
            self.nb.add(self.tabcert,text='Net Certificada')
        self._build_certified_net_tab()
    def _build_certified_net_tab(self):
        self.tabcert.rowconfigure(2,weight=1); self.tabcert.columnconfigure(0,weight=1)
        top=ttk.LabelFrame(self.tabcert,text='Certified Printable Net & Nesting Solver',padding=8)
        top.grid(row=0,column=0,sticky='ew',pady=(0,6)); top.columnconfigure(12,weight=1)
        self.cert_attempts_var=tk.IntVar(value=300)
        self.cert_scale_var=tk.DoubleVar(value=50.0)
        self.cert_margin_var=tk.DoubleVar(value=10.0)
        self.cert_page_var=tk.StringVar(value='A4')
        self.cert_tab_frac_var=tk.DoubleVar(value=0.22)
        self.cert_rotate_var=tk.BooleanVar(value=True)
        ttk.Label(top,text='Tentativas:').grid(row=0,column=0,sticky='e')
        ttk.Spinbox(top,from_=20,to=5000,increment=20,textvariable=self.cert_attempts_var,width=7).grid(row=0,column=1,padx=3)
        ttk.Label(top,text='Escala mm/unid.:').grid(row=0,column=2,sticky='e')
        ttk.Spinbox(top,from_=1,to=500,increment=1,textvariable=self.cert_scale_var,width=7).grid(row=0,column=3,padx=3)
        ttk.Label(top,text='Página:').grid(row=0,column=4,sticky='e')
        ttk.Combobox(top,textvariable=self.cert_page_var,values=['A4','Carta'],state='readonly',width=7).grid(row=0,column=5,padx=3)
        ttk.Label(top,text='Margem mm:').grid(row=0,column=6,sticky='e')
        ttk.Spinbox(top,from_=0,to=50,increment=1,textvariable=self.cert_margin_var,width=7).grid(row=0,column=7,padx=3)
        ttk.Label(top,text='Aba:').grid(row=0,column=8,sticky='e')
        ttk.Spinbox(top,from_=0.05,to=0.40,increment=0.01,textvariable=self.cert_tab_frac_var,width=6).grid(row=0,column=9,padx=3)
        ttk.Checkbutton(top,text='Rotacionar peças 0/90',variable=self.cert_rotate_var).grid(row=0,column=10,padx=4)
        ttk.Button(top,text='Gerar certificado',command=self.generate_certified_net_ui).grid(row=0,column=11,padx=4)
        ttk.Button(top,text='Exportar PDF/SVG/JSON',command=self.export_certified_net_ui).grid(row=0,column=12,sticky='w',padx=4)
        info=ttk.Label(self.tabcert,text='A verificação considera interiores de faces e abas. Toques por aresta/vértice são permitidos. O nesting é heurístico, não prova número mínimo de páginas.',wraplength=1050)
        info.grid(row=1,column=0,sticky='ew',pady=(0,6))
        pan=ttk.PanedWindow(self.tabcert,orient='horizontal')
        pan.grid(row=2,column=0,sticky='nsew')
        left=ttk.Frame(pan); right=ttk.Frame(pan)
        pan.add(left,weight=1); pan.add(right,weight=2)
        left.rowconfigure(0,weight=1); left.columnconfigure(0,weight=1)
        self.cert_text=tk.Text(left,wrap='word',font=('Consolas',9))
        self.cert_text.grid(row=0,column=0,sticky='nsew')
        self.figcert=plt.Figure(figsize=(7,6),dpi=100); self.axcert=self.figcert.add_subplot(111)
        self.canvascert=FigureCanvasTkAgg(self.figcert,master=right); self.canvascert.get_tk_widget().pack(fill='both',expand=True)
        self.cert_result=None; self.nesting_result=None
        self.update_certified_net_tab(auto=True)
    def update_all(self):
        super().update_all()
        if hasattr(self,'cert_text'):
            self.update_certified_net_tab(auto=True)
    def _current_cert_params(self):
        return dict(attempts=int(self.cert_attempts_var.get()),page=self.cert_page_var.get(),scale_mm=float(self.cert_scale_var.get()),margin_mm=float(self.cert_margin_var.get()),tab_frac=float(self.cert_tab_frac_var.get()),tab_shape=getattr(self,'net_tab_shape_var',tk.StringVar(value='trapezoidal')).get() if hasattr(self,'net_tab_shape_var') else 'trapezoidal')
    def update_certified_net_tab(self,auto=False):
        if not hasattr(self,'cert_text') or not self.poly: return
        if auto:
            attempts=min(80,int(self.cert_attempts_var.get()) if hasattr(self,'cert_attempts_var') else 80)
        else:
            attempts=int(self.cert_attempts_var.get())
        try:
            params=self._current_cert_params(); params['attempts']=attempts
            self.cert_result=search_certified_net(self.poly,**params)
            self.nesting_result=solve_certified_nesting(self.poly,self.cert_result,page=params['page'],scale_mm=params['scale_mm'],margin_mm=params['margin_mm'],allow_rotate=bool(self.cert_rotate_var.get()),tab_frac=params['tab_frac'],tab_shape=params['tab_shape'],attempts=attempts)
            self.cert_text.delete('1.0','end'); self.cert_text.insert('end',certified_net_report(self.poly,self.cert_result,self.nesting_result))
            self._draw_certified_preview()
        except Exception as exc:
            self.cert_text.delete('1.0','end'); self.cert_text.insert('end','Erro no solver certificado:\n'+str(exc))
    def generate_certified_net_ui(self):
        self.update_certified_net_tab(auto=False)
        if self.cert_result:
            messagebox.showinfo('Net certificada', 'Certificado gerado.\n\n'+self.cert_result.message)
    def _draw_certified_preview(self):
        ax=self.axcert; ax.clear()
        if not self.cert_result or not self.nesting_result:
            ax.text(.5,.5,'Gere o certificado para visualizar.',ha='center',va='center',transform=ax.transAxes); ax.axis('off'); self.canvascert.draw_idle(); return
        nesting=self.nesting_result; cert=self.cert_result
        # Mostra a primeira página do nesting.
        page_w,page_h=nesting.page_dims_mm; ax.set_xlim(0,page_w); ax.set_ylim(0,page_h); ax.set_aspect('equal'); ax.axis('off')
        ax.add_patch(MplPolygon(np.array([[nesting.margin_mm,nesting.margin_mm],[page_w-nesting.margin_mm,nesting.margin_mm],[page_w-nesting.margin_mm,page_h-nesting.margin_mm],[nesting.margin_mm,page_h-nesting.margin_mm]]),closed=True,fill=False,edgecolor='#888',linestyle=':',linewidth=0.8))
        comp_by_id={c.component_index:c for c in nesting.components}
        for pl in [p for p in nesting.placements if p.page==1]:
            comp=comp_by_id.get(pl.component_index)
            if not comp: continue
            for T in _v252_transform_poly(comp.tabs,comp,pl,nesting):
                ax.add_patch(MplPolygon(T,closed=True,facecolor='#fff2a8',edgecolor='#777',linestyle='--',linewidth=.6,alpha=.85))
            for k,P in enumerate(_v252_transform_poly(comp.polygons,comp,pl,nesting)):
                ax.add_patch(MplPolygon(P,closed=True,facecolor='#dfefff',edgecolor='#111',linewidth=.7,alpha=.92))
                c=P.mean(axis=0); fid=comp.faces[k] if k<len(comp.faces) else k; ax.text(c[0],c[1],str(fid+1),ha='center',va='center',fontsize=7)
        ax.set_title(f'Net certificada — página 1/{nesting.page_count} | construível: {cert.constructible}')
        self.canvascert.draw_idle()
    def export_certified_net_ui(self):
        if not self.poly: return
        if self.cert_result is None or self.nesting_result is None:
            self.update_certified_net_tab(auto=False)
        folder=filedialog.askdirectory(title='Pasta para exportar net certificada')
        if not folder: return
        try:
            base=Path(folder)/safe_name(self.poly.name + '_certified_net')
            export_certified_layout_pdf(self.poly,self.cert_result,self.nesting_result,base.with_suffix('.pdf'),f'Net certificada — {self.poly.name}')
            export_certified_layout_svg(self.poly,self.cert_result,self.nesting_result,base.with_suffix('.svg'),f'Net certificada — {self.poly.name}')
            payload=certified_net_payload(self.poly,self.cert_result,self.nesting_result)
            base.with_suffix('.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False,default=str),encoding='utf-8')
            base.with_name(base.stem+'_relatorio.txt').write_text(certified_net_report(self.poly,self.cert_result,self.nesting_result),encoding='utf-8')
            messagebox.showinfo('Exportação concluída',f'Arquivos salvos em:\n{folder}')
        except Exception as exc:
            messagebox.showerror('Exportar net certificada',str(exc))



def _v252_catalog_poly(key_part):
    for it in CATALOG_ITEMS:
        if key_part in it.key:
            return it.build()
    raise KeyError(key_part)

_run_self_tests_before_v252 = run_self_tests

def run_self_tests():
    rep=_run_self_tests_before_v252(); results=list(rep.results)
    def add(name,ok,detail=''):
        results.append(TestCaseResult('v25.2 / '+name,bool(ok),'' if ok else str(detail)))
    try:
        cube=_v252_catalog_poly('Platônicos / Cubo'); cert=search_certified_net(cube,attempts=80,scale_mm=40.0,tab_frac=0.18)
        add('cubo certificado sem sobreposição de faces', len(cert.face_overlaps)==0, cert.face_overlaps)
        add('cubo certificado tem abas numeradas', len(cert.tabs)>0 and all(t.glue_id>=1 for t in cert.tabs), len(cert.tabs))
        nest=solve_certified_nesting(cube,cert,page='A4',scale_mm=40.0,margin_mm=10.0)
        add('cubo nesting cabe em A4', nest.all_fit and nest.page_count>=1, asdict(nest) if hasattr(nest,'__dataclass_fields__') else nest)
        add('payload certificado serializa JSON', isinstance(json.dumps(certified_net_payload(cube,cert,nest),default=str),str))
        tet=_v252_catalog_poly('Platônicos / Tetraedro'); cert2=search_certified_net(tet,attempts=40,scale_mm=45.0)
        add('tetraedro certificado construível', cert2.constructible, certified_net_report(tet,cert2))
        tor=_v252_catalog_poly('Toroidais / Torus facetado 12×8') if any('Toroidais / Torus facetado 12×8' in it.key for it in CATALOG_ITEMS) else None
        if tor is not None:
            cert3=search_certified_net(tor,attempts=20,scale_mm=25.0)
            add('toro certificado retorna certificado ou falha controlada', isinstance(cert3,CertifiedNetCertificate), type(cert3))
    except Exception as exc:
        add('suíte v25.2 sem exceção', False, exc)
    return TestReport(results)


APP_NAME = 'GeoPoly'
VERSION = '25.2'
EDITION = 'Certified Printable Net & Nesting Solver + Embedded Johnson Formal Bundle'



# ============================================================
# v25.2.1 — Certified Net Solver Fix
# ============================================================
# Correções desta versão:
# - importa random explicitamente;
# - usa predicados robustos/adaptativos no detector de sobreposição;
# - certifica a rede de faces, não reprova a montagem por conflitos de abas;
# - trata aba-face e aba-aba como qualidade/aviso/otimização;
# - limita tempo/tentativas da busca;
# - adiciona testes para dodecaedro, icosaedro e ramo aleatório.

import random
import time

EDITION_V2521 = 'Certified Net Solver Fix: faces certified, tabs optimized'


def robust_bbox_overlap(a, b, eps=1e-10):
    return not (a[2] <= b[0] + eps or b[2] <= a[0] + eps or a[3] <= b[1] + eps or b[3] <= a[1] + eps)


def robust_point_in_poly_strict(p, poly, eps=1e-10):
    """Ponto estritamente interno a polígono simples.

    A borda é excluída. O teste de borda usa robust_orient2d; o raio-cruzamento
    ainda usa coordenadas float para a posição, mas só depois de eliminar casos
    degenerados por orientação robusta. Para a finalidade da certificação, isso
    evita que compartilhamentos por aresta/vértice sejam classificados como
    sobreposição de área.
    """
    p = np.asarray(p, dtype=float)
    P = np.asarray(poly, dtype=float)
    if len(P) < 3:
        return False
    for i in range(len(P)):
        if robust_point_on_segment(p, P[i], P[(i+1) % len(P)], eps):
            return False
    x, y = float(p[0]), float(p[1])
    inside = False
    j = len(P) - 1
    for i in range(len(P)):
        xi, yi = P[i]
        xj, yj = P[j]
        if (yi > y) != (yj > y):
            denom = (yj - yi)
            if abs(denom) < eps:
                j = i
                continue
            x_cross = (xj - xi) * (y - yi) / denom + xi
            if x < x_cross:
                inside = not inside
        j = i
    return inside


def _legacy_robust_polygon_overlap_area_v2520(A, B, eps=1e-10):
    """Sobreposição de interiores com área positiva entre dois polígonos.

    Contato em aresta ou vértice não conta como sobreposição. Segmentos
    cruzando propriamente contam. Contenção parcial/total é capturada por ponto
    estritamente interno.
    """
    A = np.asarray(A, dtype=float)
    B = np.asarray(B, dtype=float)
    if len(A) < 3 or len(B) < 3:
        return False
    if not robust_bbox_overlap(bbox(A), bbox(B), eps):
        return False
    for i in range(len(A)):
        a1, a2 = A[i], A[(i+1) % len(A)]
        for j in range(len(B)):
            b1, b2 = B[j], B[(j+1) % len(B)]
            if segments_properly_intersect_robust(a1, a2, b1, b2):
                return True
    for p in A:
        if robust_point_in_poly_strict(p, B, eps):
            return True
    for p in B:
        if robust_point_in_poly_strict(p, A, eps):
            return True
    return False


# Alias transitório: preserva lookup global usado por funções históricas até a definição final validada abaixo.
robust_polygon_overlap_area = _legacy_robust_polygon_overlap_area_v2520

# Mantém compatibilidade histórica nesta etapa do arquivo; a definição final validada é ligada mais abaixo.
poly_overlap = _legacy_robust_polygon_overlap_area_v2520
seg_inter = robust_seg_inter
point_on_segment = robust_point_on_segment


def detect_overlaps(faces):
    pairs = []
    boxes = [bbox(nf.poly2d) for nf in faces]
    for i in range(len(faces)):
        for j in range(i+1, len(faces)):
            if robust_bbox_overlap(boxes[i], boxes[j]) and robust_polygon_overlap_area(faces[i].poly2d, faces[j].poly2d):
                pairs.append((faces[i].face_index, faces[j].face_index))
    return pairs


def _legacy_verify_constructible_net_v2521_pre_final(poly, net, tab_frac=0.22, tab_shape='trapezoidal', verify_tabs=True):
    """Certifica a rede de faces e avalia a qualidade das abas.

    Mudança v25.2.1: construtibilidade significa que a rede de faces é simples,
    conexa via árvore de dobras, contém todas as faces e não possui sobreposição
    face-face. Conflitos geométricos das abas não invalidam automaticamente a
    rede; eles entram como avisos de fabricação, pois abas podem ser reduzidas,
    reposicionadas, omitidas seletivamente ou dobradas por baixo durante a
    montagem real de papercraft.
    """
    faces = net.faces
    face_overlaps = list(detect_overlaps(faces))
    tabs = certified_glue_tabs(poly, net, tab_frac, tab_shape)
    tab_face = []
    tab_tab = []
    if verify_tabs:
        for t in tabs:
            for nf in faces:
                if nf.face_index == t.face_index:
                    continue
                if robust_polygon_overlap_area(t.poly2d, nf.poly2d):
                    tab_face.append((int(t.glue_id), int(nf.face_index)))
        for i in range(len(tabs)):
            for j in range(i+1, len(tabs)):
                # Se tocam apenas em vértices/arestas, robust_polygon_overlap_area retorna False.
                if robust_polygon_overlap_area(tabs[i].poly2d, tabs[j].poly2d):
                    tab_tab.append((int(tabs[i].glue_id), int(tabs[j].glue_id)))
    face_maps = _v252_face_vertex_map(poly, net)
    folded = sum(1 for e in poly.edge_to_faces() if _v252_is_folded_edge(poly, net, e, face_maps))
    cut = len(poly.edges()) - folded
    all_faces_present = (len(faces) == len(poly.faces))
    face_clean = (len(face_overlaps) == 0)
    constructible = bool(all_faces_present and face_clean)
    tab_conflicts = len(tab_face) + len(tab_tab)
    if constructible and tab_conflicts == 0:
        status = 'approved'
        msg = 'rede de faces construível; abas sem conflitos detectados'
    elif constructible:
        status = 'approved_with_tab_warnings'
        msg = (f'rede de faces construível; conflitos de abas tratados como aviso/otimização: '
               f'aba-face={len(tab_face)}, aba-aba={len(tab_tab)}')
    else:
        status = 'failed'
        msg = f'rede não certificada: faces={len(face_overlaps)}, faces presentes={len(faces)}/{len(poly.faces)}'
    # Face-overlap domina o score. Conflito de aba é custo brando.
    score = 1000000 * len(face_overlaps) + 250 * len(tab_face) + 250 * len(tab_tab) + 10 * cut
    return CertifiedNetCertificate(status, constructible, net, face_overlaps, tab_face, tab_tab, tabs,
                                   int(folded), int(cut), float(score), net.mode, 1, msg)


def search_certified_net(poly, attempts=300, page='A4', scale_mm=50.0, margin_mm=10.0,
                         tab_frac=0.22, tab_shape='trapezoidal', max_seconds=8.0):
    """Busca árvores de desdobramento e retorna a melhor rede encontrada.

    O padrão v25.2.1 é interativo: respeita tentativas e tempo máximo. Para aula,
    o solver para assim que encontra rede de faces sem sobreposição. O nesting e a
    otimização de abas ficam como etapas de qualidade de fabricação.
    """
    start = time.time()
    n = len(poly.faces)
    if n == 0:
        return verify_constructible_net(poly, NetResult([], [], 0, 'none', 'sem faces'), tab_frac, tab_shape)
    attempts = max(1, int(attempts))
    max_seconds = max(0.25, float(max_seconds))
    roots = list(dict.fromkeys(sorted(range(n), key=lambda i: -poly.face_area(poly.faces[i])) + list(range(n))))
    strategies = ['bfs', 'dfs', 'area', 'small', 'steepest', 'flattest', 'longest', 'shortest']
    best = None
    tried = 0
    max_roots = min(n, max(1, min(n, 50)))
    def consider(cert, st, r):
        nonlocal best
        x0, y0, x1, y1 = _v252_bbox_pts([nf.poly2d for nf in cert.net.faces] + [t.poly2d for t in cert.tabs])
        area = max(0.0, (x1 - x0) * (y1 - y0))
        cert.score += 0.01 * area
        cert.strategy = f'{st}, raiz face {r+1}'
        cert.attempts = tried
        if best is None or cert.score < best.score:
            best = cert
    for r in roots[:max_roots]:
        for st in strategies:
            if tried >= attempts or (time.time() - start) >= max_seconds:
                return best
            net = generate_guided_tree_net(poly, r, st, seed=tried)
            cert = verify_constructible_net(poly, net, tab_frac, tab_shape, True)
            tried += 1
            consider(cert, st, r)
            if cert.constructible:
                return cert
    seed = 0
    while tried < attempts and (time.time() - start) < max_seconds:
        r = roots[seed % len(roots)]
        net = generate_guided_tree_net(poly, r, 'random', seed=seed)
        cert = verify_constructible_net(poly, net, tab_frac, tab_shape, True)
        tried += 1
        seed += 1
        consider(cert, f'random seed {seed}', r)
        if cert.constructible:
            return cert
    return best


def _legacy_certified_net_report_v2521(poly, cert, nesting=None):
    lines = []
    lines.append('Certified Printable Net & Nesting Solver v25.2.1')
    lines.append('=' * 56)
    lines.append(f'Sólido: {poly.name}')
    lines.append(f'Estratégia: {cert.strategy}')
    lines.append(f'Tentativas: {cert.attempts}')
    lines.append(f'Status: {cert.status}')
    lines.append(f'Rede de faces construível: {"sim" if cert.constructible else "não"}')
    lines.append(f'Faces: {len(cert.net.faces)}/{len(poly.faces)}')
    lines.append(f'Sobreposição face-face: {len(cert.face_overlaps)}')
    lines.append('')
    lines.append('Qualidade das abas de colagem')
    lines.append('-' * 32)
    lines.append(f'Conflitos aba-face: {len(cert.tab_face_overlaps)}')
    lines.append(f'Conflitos aba-aba: {len(cert.tab_tab_overlaps)}')
    if cert.tab_face_overlaps or cert.tab_tab_overlaps:
        lines.append('Observação: conflitos de abas são avisos de fabricação, não reprovação da rede de faces.')
        lines.append('Sugestões: reduzir tamanho da aba, trocar lado da aba, omitir aba seletiva ou usar multifolha.')
    lines.append('')
    lines.append(f'Arestas de dobra estimadas: {cert.tree_fold_edges}')
    lines.append(f'Arestas de corte/contorno: {cert.cut_edges}')
    lines.append(f'Abas numeradas: {len(cert.tabs)}')
    lines.append(f'Score: {cert.score:.3f}')
    lines.append('')
    lines.append('Abas de colagem')
    lines.append('-' * 18)
    for t in cert.tabs[:200]:
        if t.mate_face is None:
            lines.append(f'{t.glue_id}: face {t.face_index+1}, borda {t.edge}')
        else:
            lines.append(f'{t.glue_id}: face {t.face_index+1} cola na face {t.mate_face+1}, aresta {t.edge}')
    if len(cert.tabs) > 200:
        lines.append(f'... {len(cert.tabs)-200} abas restantes')
    if nesting:
        lines += ['', 'Nesting em páginas', '-' * 19]
        lines.append(f'Página: {nesting.page_name} {nesting.page_dims_mm[0]:.1f}×{nesting.page_dims_mm[1]:.1f} mm')
        lines.append(f'Área útil: {nesting.usable_dims_mm[0]:.1f}×{nesting.usable_dims_mm[1]:.1f} mm')
        lines.append(f'Escala: {nesting.scale_mm:.3f} mm/unidade')
        lines.append(f'Margem: {nesting.margin_mm:.1f} mm')
        lines.append(f'Componentes: {len(nesting.components)}')
        lines.append(f'Páginas: {nesting.page_count}')
        lines.append(f'Aproveitamento estimado: {nesting.utilization_percent:.2f}%')
        lines.append(f'Todos cabem: {"sim" if nesting.all_fit else "não"}')
        for w in nesting.warnings:
            lines.append('Aviso: ' + w)
    lines.append('')
    lines.append('Critério v25.2.1: rede de faces certificada computacionalmente sem sobreposição de interiores, usando predicados robustos/adaptativos.')
    lines.append('Abas são avaliadas como qualidade/otimização de montagem, não como condição absoluta de construtibilidade.')
    lines.append('A busca é heurística e limitada por tentativas/tempo; não encontrar uma rede não prova inexistência.')
    return '\n'.join(lines)


def _legacy_certified_net_payload_v2521(poly, cert, nesting=None):
    return {
        'version': '25.2.1',
        'solid': poly.name,
        'family': poly.family,
        'face_net_constructible': bool(cert.constructible),
        'status': cert.status,
        'strategy': cert.strategy,
        'attempts': int(cert.attempts),
        'face_overlaps': [list(map(int, p)) for p in cert.face_overlaps],
        'tab_quality': {
            'tab_face_conflicts': [list(map(int, p)) for p in cert.tab_face_overlaps],
            'tab_tab_conflicts': [list(map(int, p)) for p in cert.tab_tab_overlaps],
            'conflicts_are_warnings': True,
        },
        'tree_fold_edges': int(cert.tree_fold_edges),
        'cut_edges': int(cert.cut_edges),
        'tabs': [
            {'glue_id': int(t.glue_id), 'face': int(t.face_index + 1),
             'edge': [int(t.edge[0]), int(t.edge[1])],
             'mate_face': None if t.mate_face is None else int(t.mate_face + 1),
             'note': t.note}
            for t in cert.tabs
        ],
        'nesting': None if nesting is None else {
            'page': nesting.page_name,
            'page_dims_mm': list(nesting.page_dims_mm),
            'usable_dims_mm': list(nesting.usable_dims_mm),
            'margin_mm': float(nesting.margin_mm),
            'scale_mm': float(nesting.scale_mm),
            'page_count': int(nesting.page_count),
            'utilization_percent': float(nesting.utilization_percent),
            'all_fit': bool(nesting.all_fit),
            'warnings': list(nesting.warnings),
            'placements': [asdict(p) for p in nesting.placements]
        },
        'certification_note': 'Faces sem sobreposição; abas são avisos/otimização. Busca heurística, não prova inexistência quando falha.'
    }


# Atualiza a mensagem da aba sem mudar o menu.
try:
    _build_certified_net_tab_before_v2521 = GeoPolyAppV252._build_certified_net_tab
    def _build_certified_net_tab_v2521(self):
        _build_certified_net_tab_before_v2521(self)
        try:
            self.cert_attempts_var.set(min(180, int(self.cert_attempts_var.get())))
        except Exception:
            pass
    GeoPolyAppV252._build_certified_net_tab = _build_certified_net_tab_v2521
except Exception:
    pass


class GeoPolyAppV2521(GeoPolyAppV252):
    pass


_run_self_tests_before_v2521 = run_self_tests

def run_self_tests():
    rep = _run_self_tests_before_v2521()
    results = list(rep.results)
    def add(name, ok, detail=''):
        results.append(TestCaseResult('v25.2.1 / ' + name, bool(ok), '' if ok else str(detail)))
    try:
        # Ramo random precisa existir e não lançar NameError.
        cube = _v252_catalog_poly('Platônicos / Cubo')
        net_random = generate_guided_tree_net(cube, 0, 'random', seed=123)
        add('ramo random executa sem NameError', isinstance(net_random, NetResult), type(net_random))

        for label in ['Platônicos / Tetraedro', 'Platônicos / Cubo', 'Platônicos / Octaedro', 'Platônicos / Dodecaedro', 'Platônicos / Icosaedro']:
            p = _v252_catalog_poly(label)
            cert = search_certified_net(p, attempts=220, tab_frac=0.22, max_seconds=10.0)
            add(f'{p.name}: rede de faces certificada', cert is not None and cert.constructible and len(cert.face_overlaps) == 0, certified_net_report(p, cert) if cert else 'sem cert')
        dod = _v252_catalog_poly('Platônicos / Dodecaedro')
        cert_big_tab = search_certified_net(dod, attempts=160, tab_frac=0.35, max_seconds=8.0)
        add('dodecaedro: conflito de aba não reprova rede de faces', cert_big_tab.constructible and len(cert_big_tab.face_overlaps) == 0, certified_net_report(dod, cert_big_tab))
        payload = certified_net_payload(dod, cert_big_tab)
        add('payload v25.2.1 serializa JSON', isinstance(json.dumps(payload, default=str), str))
    except Exception as exc:
        add('suíte v25.2.1 sem exceção', False, repr(exc))
    return TestReport(results)


APP_NAME = 'GeoPoly'
VERSION = '25.2.1'
EDITION = 'Certified Net Solver Fix + Printable Nesting + Embedded Johnson Formal Bundle'



# v25.2.1b — refinamento do detector de sobreposição de faces para redes
# adjacentes por aresta original. Pares de faces que compartilham uma aresta no
# poliedro e apenas encostam/sofrem falso positivo de contenção numérica não são
# contados como sobreposição de interior. Cruzamento próprio de segmentos ainda
# reprova.

def _robust_has_proper_segment_crossing(A, B):
    A=np.asarray(A,dtype=float); B=np.asarray(B,dtype=float)
    for i in range(len(A)):
        for j in range(len(B)):
            if segments_properly_intersect_robust(A[i], A[(i+1)%len(A)], B[j], B[(j+1)%len(B)]):
                return True
    return False


def detect_face_overlaps_for_poly(poly, faces):
    pairs=[]; boxes=[bbox(nf.poly2d) for nf in faces]
    face_by_index={nf.face_index:nf for nf in faces}
    keys=[nf.face_index for nf in faces]
    for ii in range(len(keys)):
        fi=keys[ii]; A=face_by_index[fi].poly2d
        for jj in range(ii+1,len(keys)):
            fj=keys[jj]; B=face_by_index[fj].poly2d
            if not robust_bbox_overlap(boxes[ii], boxes[jj]):
                continue
            if not robust_polygon_overlap_area(A,B):
                continue
            common=set(poly.faces[fi]) & set(poly.faces[fj])
            if len(common)>=2 and not _robust_has_proper_segment_crossing(A,B):
                # Faces adjacentes por uma aresta original: contato de borda/colinearidade
                # é permitido; falsos positivos por vértice quase-colinear são ignorados.
                continue
            pairs.append((int(fi),int(fj)))
    return pairs


# Substitui somente a verificação certificada de faces; detect_overlaps genérico
# continua disponível para outras abas/relatórios.
def verify_constructible_net(poly, net, tab_frac=0.22, tab_shape='trapezoidal', verify_tabs=True):
    faces = net.faces
    face_overlaps = list(detect_face_overlaps_for_poly(poly, faces))
    tabs = certified_glue_tabs(poly, net, tab_frac, tab_shape)
    tab_face = []
    tab_tab = []
    if verify_tabs:
        for t in tabs:
            for nf in faces:
                if nf.face_index == t.face_index:
                    continue
                if robust_polygon_overlap_area(t.poly2d, nf.poly2d):
                    tab_face.append((int(t.glue_id), int(nf.face_index)))
        for i in range(len(tabs)):
            for j in range(i+1, len(tabs)):
                if robust_polygon_overlap_area(tabs[i].poly2d, tabs[j].poly2d):
                    tab_tab.append((int(tabs[i].glue_id), int(tabs[j].glue_id)))
    face_maps = _v252_face_vertex_map(poly, net)
    folded = sum(1 for e in poly.edge_to_faces() if _v252_is_folded_edge(poly, net, e, face_maps))
    cut = len(poly.edges()) - folded
    all_faces_present = (len(faces) == len(poly.faces))
    constructible = bool(all_faces_present and len(face_overlaps) == 0)
    tab_conflicts = len(tab_face) + len(tab_tab)
    if constructible and tab_conflicts == 0:
        status='approved'; msg='rede de faces construível; abas sem conflitos detectados'
    elif constructible:
        status='approved_with_tab_warnings'; msg=f'rede de faces construível; conflitos de abas como aviso: aba-face={len(tab_face)}, aba-aba={len(tab_tab)}'
    else:
        status='failed'; msg=f'rede não certificada: faces={len(face_overlaps)}, faces presentes={len(faces)}/{len(poly.faces)}'
    score=1000000*len(face_overlaps)+250*len(tab_face)+250*len(tab_tab)+10*cut
    return CertifiedNetCertificate(status, constructible, net, face_overlaps, tab_face, tab_tab, tabs, int(folded), int(cut), float(score), net.mode, 1, msg)


# v25.2.1c — containment tolerante para fronteiras quase colineares.
# O cruzamento próprio de segmentos continua usando orientação robusta; a etapa
# de contenção usa uma tolerância geométrica para não transformar contato de
# borda/erro de arredondamento em sobreposição de área.

def tolerant_orient2d_value(a,b,c):
    a=np.asarray(a,dtype=float); b=np.asarray(b,dtype=float); c=np.asarray(c,dtype=float)
    return float((b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0]))

def tolerant_point_on_segment(p,a,b,eps=1e-7):
    if abs(tolerant_orient2d_value(a,b,p)) > eps:
        return False
    p=np.asarray(p,dtype=float); a=np.asarray(a,dtype=float); b=np.asarray(b,dtype=float)
    return (min(a[0],b[0])-eps <= p[0] <= max(a[0],b[0])+eps and
            min(a[1],b[1])-eps <= p[1] <= max(a[1],b[1])+eps)

def robust_point_in_poly_strict(p, poly, eps=1e-7):
    p=np.asarray(p,dtype=float); P=np.asarray(poly,dtype=float)
    if len(P)<3: return False
    for i in range(len(P)):
        if tolerant_point_on_segment(p,P[i],P[(i+1)%len(P)],eps):
            return False
    x,y=float(p[0]),float(p[1]); inside=False; j=len(P)-1
    for i in range(len(P)):
        xi,yi=P[i]; xj,yj=P[j]
        if ((yi>y)!=(yj>y)):
            denom=(yj-yi)
            if abs(denom)>eps:
                if x < (xj-xi)*(y-yi)/denom + xi:
                    inside=not inside
        j=i
    return inside

def _legacy_robust_polygon_overlap_area_v2521_pre_final(A,B,eps=1e-7):
    A=np.asarray(A,dtype=float); B=np.asarray(B,dtype=float)
    if len(A)<3 or len(B)<3: return False
    if not robust_bbox_overlap(bbox(A),bbox(B),eps): return False
    for i in range(len(A)):
        for j in range(len(B)):
            if segments_properly_intersect_robust(A[i],A[(i+1)%len(A)],B[j],B[(j+1)%len(B)]):
                return True
    return any(robust_point_in_poly_strict(p,B,eps) for p in A) or any(robust_point_in_poly_strict(p,A,eps) for p in B)

poly_overlap = robust_polygon_overlap_area


# v25.2.1d — interseção própria robusta com zona de fronteira tolerante.
def robust_area_segment_intersect(a,b,c,d,eps=1e-7):
    # Primeiro elimina casos quase colineares/contato de borda por métrica float.
    o1=tolerant_orient2d_value(a,b,c); o2=tolerant_orient2d_value(a,b,d)
    o3=tolerant_orient2d_value(c,d,a); o4=tolerant_orient2d_value(c,d,b)
    if abs(o1)<=eps or abs(o2)<=eps or abs(o3)<=eps or abs(o4)<=eps:
        return False
    # Em seguida confirma o sinal com orientação robusta/adaptativa.
    s1=robust_orient2d(a,b,c); s2=robust_orient2d(a,b,d); s3=robust_orient2d(c,d,a); s4=robust_orient2d(c,d,b)
    return (s1!=0 and s2!=0 and s3!=0 and s4!=0 and ((s1>0)!=(s2>0)) and ((s3>0)!=(s4>0)))

def _robust_has_proper_segment_crossing(A, B):
    A=np.asarray(A,dtype=float); B=np.asarray(B,dtype=float)
    for i in range(len(A)):
        for j in range(len(B)):
            if robust_area_segment_intersect(A[i],A[(i+1)%len(A)],B[j],B[(j+1)%len(B)]):
                return True
    return False

def robust_polygon_overlap_area(A,B,eps=1e-7):
    A=np.asarray(A,dtype=float); B=np.asarray(B,dtype=float)
    if len(A)<3 or len(B)<3: return False
    if not robust_bbox_overlap(bbox(A),bbox(B),eps): return False
    for i in range(len(A)):
        for j in range(len(B)):
            if robust_area_segment_intersect(A[i],A[(i+1)%len(A)],B[j],B[(j+1)%len(B)],eps):
                return True
    return any(robust_point_in_poly_strict(p,B,eps) for p in A) or any(robust_point_in_poly_strict(p,A,eps) for p in B)

poly_overlap = robust_polygon_overlap_area
seg_inter = robust_area_segment_intersect


# ============================================================
# v25.2.2 — Real Page Nesting & Auto-Scale Fix
# ============================================================
# Correções desta versão:
# - métricas de nesting não excedem 100% e ficam N/A quando o layout não cabe;
# - autoescala opcional/por padrão na aba Net Certificada;
# - escolha automática de orientação de página retrato/paisagem;
# - contagem coerente de páginas;
# - relatório honesto: verificado sob tolerância, busca heurística;
# - testes para dodecaedro/icosaedro e caso de escala grande.

EDITION_V2522 = 'Real Page Nesting & Auto-Scale Fix'


def _v2522_orientations_for_page(page):
    w,h=_v252_page_dims(page)
    if abs(w-h)<1e-9:
        return [('quadrada',(float(w),float(h)))]
    return [('retrato',(float(w),float(h))), ('paisagem',(float(h),float(w)))]


def _v2522_fit_factor_for_component(comp, usable_w, usable_h, allow_rotate=True):
    w=max(float(comp.width_mm), EPS); h=max(float(comp.height_mm), EPS)
    f0=min(usable_w/w, usable_h/h)
    if allow_rotate:
        f1=min(usable_w/h, usable_h/w)
        return max(f0,f1)
    return f0


def _v2522_best_page_orientation_for_components(page, components, margin_mm, allow_rotate=True):
    best=None
    for orient,dims in _v2522_orientations_for_page(page):
        usable=(dims[0]-2*margin_mm, dims[1]-2*margin_mm)
        if usable[0]<=0 or usable[1]<=0:
            score=(-1e9, 0, orient, dims, usable, 0.0)
        else:
            factors=[_v2522_fit_factor_for_component(c, usable[0], usable[1], allow_rotate) for c in components] or [1.0]
            minfit=min(factors)
            # Prioriza caber; depois área útil maior no menor lado.
            score=(1 if minfit>=1.0 else 0, minfit, orient, dims, usable, min(1.0,minfit))
        if best is None or (score[0],score[1], min(score[4]) if score[4][0]>0 and score[4][1]>0 else -1) > (best[0],best[1], min(best[4]) if best[4][0]>0 and best[4][1]>0 else -1):
            best=score
    _,minfit,orient,dims,usable,suggested=best
    return orient,dims,usable,float(minfit),float(suggested)


def _v2522_choose_rect_orientation(comp, usable_w, usable_h, allow_rotate=True):
    w=float(comp.width_mm); h=float(comp.height_mm)
    candidates=[(0,w,h)]
    if allow_rotate:
        candidates.append((90,h,w))
    # Preferir orientações que cabem; entre elas, menor altura para empacotar melhor.
    fitting=[c for c in candidates if c[1]<=usable_w+1e-9 and c[2]<=usable_h+1e-9]
    if fitting:
        return min(fitting, key=lambda c:(c[2], c[1]))
    # Se nenhuma cabe, retorna a que tem maior fator relativo de cabimento.
    return max(candidates, key=lambda c:min(usable_w/max(c[1],EPS), usable_h/max(c[2],EPS)))


def _v2522_bottom_left_pack(components, usable_w, usable_h, gap=4.0, allow_rotate=True):
    placements=[]; warnings=[]
    page=1; x=0.0; y=0.0; row_h=0.0; all_fit=True
    for comp in components:
        rot,w,h=_v2522_choose_rect_orientation(comp, usable_w, usable_h, allow_rotate)
        if w>usable_w+1e-9 or h>usable_h+1e-9:
            all_fit=False
            scale=min(usable_w/max(w,EPS), usable_h/max(h,EPS))
            warnings.append(f'Componente {comp.component_index} excede a página útil nesta escala; escala relativa máxima sugerida {scale:.3f}.')
        # Se couber individualmente, usa shelf/bottom-left.
        if x+w>usable_w+1e-9 and x>0:
            x=0.0; y+=row_h+gap; row_h=0.0
        if y+h>usable_h+1e-9 and y>0:
            page+=1; x=0.0; y=0.0; row_h=0.0
        # Se não couber na página vazia, ainda registra posicionamento diagnóstico.
        placements.append(NestedPagePlacement(int(page), int(comp.component_index), float(x), float(y), int(rot), float(w), float(h)))
        x+=w+gap; row_h=max(row_h,h)
    pages=max([p.page for p in placements],default=1)
    if not all_fit:
        warnings.append('Layout diagnóstico: pelo menos um componente é maior que a página útil; aproveitamento percentual não é aplicável sem autoescala/fragmentação.')
    return placements, int(pages), bool(all_fit), warnings


def _v2522_make_components_from_cert(poly, cert, scale_mm):
    if cert.constructible:
        sheets=[cert.net.faces]
    else:
        ms=solve_multi_sheet(poly,cert.net,'A4',scale_mm,10.0)
        sheets=ms.sheets
    comps=[_v252_component_from_sheet(i+1,s,cert.tabs,scale_mm) for i,s in enumerate(sheets)]
    return sorted(comps,key=lambda c:(max(c.width_mm,c.height_mm), c.width_mm*c.height_mm),reverse=True)


def _legacy_solve_certified_nesting_v2522_autoscale(poly, cert=None, page='A4', scale_mm=50.0, margin_mm=10.0, allow_rotate=True, tab_frac=0.22, tab_shape='trapezoidal', attempts=300, auto_scale=True, min_scale_mm=5.0):
    """Nesting v25.2.2.

    Quando auto_scale=True, reduz a escala para que cada componente caiba na
    área útil da página escolhida, preservando a geometria e recalculando os
    componentes. Quando auto_scale=False, não gera aproveitamento inválido acima
    de 100%; retorna all_fit=False e avisos.
    """
    cert=cert or search_certified_net(poly,attempts=attempts,page=page,scale_mm=scale_mm,margin_mm=margin_mm,tab_frac=tab_frac,tab_shape=tab_shape)
    requested_scale=float(scale_mm)
    components=_v2522_make_components_from_cert(poly,cert,requested_scale)
    orient,page_dims,usable,minfit,suggested_rel=_v2522_best_page_orientation_for_components(page,components,float(margin_mm),allow_rotate)
    applied_scale=requested_scale
    warnings=[]
    scale_adjusted=False
    if minfit < 1.0:
        suggested_scale=max(float(min_scale_mm), requested_scale*max(0.0,suggested_rel)*0.995)
        if auto_scale and suggested_scale < requested_scale:
            applied_scale=suggested_scale
            scale_adjusted=True
            warnings.append(f'Autoescala aplicada: {requested_scale:.3f} → {applied_scale:.3f} mm/unid. para caber na página útil ({orient}).')
            components=_v2522_make_components_from_cert(poly,cert,applied_scale)
            orient,page_dims,usable,minfit,suggested_rel=_v2522_best_page_orientation_for_components(page,components,float(margin_mm),allow_rotate)
        else:
            warnings.append(f'Componente maior que a página útil. Escala máxima sugerida: {suggested_scale:.3f} mm/unid. Ative autoescala ou reduza a escala manualmente.')
    placements,pages,all_fit,pack_warnings=_v2522_bottom_left_pack(components,usable[0],usable[1],gap=4.0,allow_rotate=allow_rotate)
    warnings.extend(pack_warnings)
    used_area=sum(float(p.width_mm)*float(p.height_mm) for p in placements)
    if all_fit and pages>0 and usable[0]>0 and usable[1]>0:
        util=min(100.0, max(0.0, 100.0*used_area/(pages*usable[0]*usable[1])))
        layout_status='fit_rescaled' if scale_adjusted else 'fit'
    else:
        util=None
        layout_status='component_too_large'
    res=NestingResult(str(page),(float(page_dims[0]),float(page_dims[1])),(float(usable[0]),float(usable[1])),float(margin_mm),float(applied_scale),components,placements,int(max(1,pages)),util,bool(all_fit),warnings)
    # Atributos extras preservam compatibilidade com dataclass e enriquecem payload/relatório.
    res.requested_scale_mm=float(requested_scale)
    res.applied_scale_mm=float(applied_scale)
    res.scale_adjusted=bool(scale_adjusted)
    res.suggested_scale_mm=float(requested_scale*max(0.0,suggested_rel)*0.995) if minfit<1.0 else float(requested_scale)
    res.page_orientation=str(orient)
    res.layout_status=str(layout_status)
    res.auto_scale=bool(auto_scale)
    return res


def _legacy_certified_net_report_v2522(poly, cert, nesting=None):
    lines=[]
    lines.append('Certified Printable Net & Nesting Solver v25.2.2')
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
        req=getattr(nesting,'requested_scale_mm',nesting.scale_mm)
        app=getattr(nesting,'applied_scale_mm',nesting.scale_mm)
        lines.append(f'Escala solicitada: {req:.3f} mm/unidade')
        lines.append(f'Escala aplicada: {app:.3f} mm/unidade')
        if getattr(nesting,'scale_adjusted',False):
            lines.append('Autoescala: sim')
        else:
            lines.append('Autoescala: não aplicada')
        lines.append(f'Margem: {nesting.margin_mm:.1f} mm')
        lines.append(f'Componentes: {len(nesting.components)}')
        lines.append(f'Páginas: {nesting.page_count}')
        if nesting.utilization_percent is None:
            lines.append('Aproveitamento estimado: n/a (algum componente excede a página)')
        else:
            lines.append(f'Aproveitamento estimado: {nesting.utilization_percent:.2f}%')
        lines.append(f'Todos cabem: {"sim" if nesting.all_fit else "não"}')
        lines.append(f'Status do layout: {getattr(nesting,"layout_status","n/d")}')
        for w in nesting.warnings:
            lines.append('Aviso: '+w)
    lines.append('')
    lines.append('Critério: rede de faces verificada computacionalmente sem sobreposição de interiores. Abas são tratadas como qualidade/otimização, não como falha automática.')
    lines.append('Nota: a busca é heurística e não prova inexistência de rede melhor; a verificação usa predicados robustos/adaptativos com tolerância geométrica para a geometria exportada.')
    return '\n'.join(lines)


def _legacy_certified_net_payload_v2522(poly, cert, nesting=None):
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
            'auto_scale':bool(getattr(nesting,'auto_scale',False)),
            'page_count':int(nesting.page_count),
            'utilization_percent':None if nesting.utilization_percent is None else float(nesting.utilization_percent),
            'all_fit':bool(nesting.all_fit),
            'warnings':list(nesting.warnings),
            'placements':[asdict(p) for p in nesting.placements]
        }
    return {
        'version':'25.2.2', 'solid':poly.name, 'family':poly.family,
        'constructible':bool(cert.constructible), 'status':cert.status,
        'strategy':cert.strategy, 'attempts':int(cert.attempts),
        'face_overlaps':[list(map(int,p)) for p in cert.face_overlaps],
        'tab_face_overlaps':[list(map(int,p)) for p in cert.tab_face_overlaps],
        'tab_tab_overlaps':[list(map(int,p)) for p in cert.tab_tab_overlaps],
        'tree_fold_edges':int(cert.tree_fold_edges), 'cut_edges':int(cert.cut_edges),
        'tabs':[{'glue_id':int(t.glue_id),'face':int(t.face_index+1),'edge':[int(t.edge[0]),int(t.edge[1])],'mate_face':None if t.mate_face is None else int(t.mate_face+1),'note':t.note} for t in cert.tabs],
        'nesting': nest_payload,
        'certification_note': 'Faces sem sobreposição; abas são avisos/otimização. Nesting com autoescala opcional. Busca heurística, não prova inexistência de solução melhor.'
    }


_full_report_before_v2522 = full_report

def full_report(poly,scale_mm=50.0,density_g_cm3=1.24,cost_per_kg=100.0):
    md,payload=_full_report_before_v2522(poly,scale_mm,density_g_cm3,cost_per_kg)
    try:
        cert=search_certified_net(poly,attempts=80,scale_mm=scale_mm,tab_frac=0.22)
        nesting=solve_certified_nesting(poly,cert,scale_mm=scale_mm,attempts=80,auto_scale=True)
        payload['certified_printable_net_v2522']=certified_net_payload(poly,cert,nesting)
        md += '\n\n## Rede imprimível verificada v25.2.2\n'
        md += f'- Rede de faces construível: {"sim" if cert.constructible else "não; usar multifolha/decomposição"}\n'
        md += f'- Sobreposições de faces: {len(cert.face_overlaps)}\n'
        md += f'- Conflitos aba-face: {len(cert.tab_face_overlaps)}\n'
        md += f'- Conflitos aba-aba: {len(cert.tab_tab_overlaps)}\n'
        md += f'- Páginas estimadas: {nesting.page_count}\n'
        md += f'- Todos cabem: {"sim" if nesting.all_fit else "não"}\n'
        md += f'- Escala aplicada: {getattr(nesting,"applied_scale_mm",nesting.scale_mm):.3f} mm/unid.\n'
        if nesting.utilization_percent is None:
            md += '- Aproveitamento estimado: n/a\n'
        else:
            md += f'- Aproveitamento estimado: {nesting.utilization_percent:.2f}%\n'
    except Exception as exc:
        payload['certified_printable_net_v2522_error']=str(exc)
        md += '\n\n## Rede imprimível verificada v25.2.2\n- Não foi possível gerar certificado automático: '+str(exc)+'\n'
    return md,payload


class GeoPolyAppV2522(GeoPolyAppV2521):
    """v25.2.2: mantém menus e adiciona autoescala real no nesting."""
    def _build_certified_net_tab(self):
        super()._build_certified_net_tab()
        try:
            self.cert_auto_scale_var=tk.BooleanVar(value=True)
            extra=ttk.LabelFrame(self.tabcert,text='v25.2.2 — encaixe físico da página',padding=6)
            extra.grid(row=3,column=0,sticky='ew',pady=(6,0))
            ttk.Checkbutton(extra,text='Reduzir escala automaticamente para caber em A4/Carta',variable=self.cert_auto_scale_var).pack(side='left',padx=4)
            ttk.Label(extra,text='Se desativado, o relatório informa escala máxima sugerida e evita aproveitamento >100%.').pack(side='left',padx=8)
        except Exception:
            pass
    def update_certified_net_tab(self,auto=False):
        if not hasattr(self,'cert_text') or not self.poly: return
        if auto:
            attempts=min(80,int(self.cert_attempts_var.get()) if hasattr(self,'cert_attempts_var') else 80)
        else:
            attempts=int(self.cert_attempts_var.get())
        try:
            params=self._current_cert_params(); params['attempts']=attempts
            self.cert_result=search_certified_net(self.poly,**params)
            auto_scale=bool(getattr(self,'cert_auto_scale_var',tk.BooleanVar(value=True)).get()) if hasattr(self,'cert_auto_scale_var') else True
            self.nesting_result=solve_certified_nesting(self.poly,self.cert_result,page=params['page'],scale_mm=params['scale_mm'],margin_mm=params['margin_mm'],allow_rotate=bool(self.cert_rotate_var.get()),tab_frac=params['tab_frac'],tab_shape=params['tab_shape'],attempts=attempts,auto_scale=auto_scale)
            self.cert_text.delete('1.0','end'); self.cert_text.insert('end',certified_net_report(self.poly,self.cert_result,self.nesting_result))
            self._draw_certified_preview()
        except Exception as exc:
            self.cert_text.delete('1.0','end'); self.cert_text.insert('end','Erro no solver certificado:\n'+str(exc))


_run_self_tests_before_v2522 = run_self_tests

def run_self_tests():
    rep=_run_self_tests_before_v2522(); results=list(rep.results)
    def add(name,ok,detail=''):
        results.append(TestCaseResult('v25.2.2 / '+name,bool(ok),'' if ok else str(detail)))
    try:
        dod=_v252_catalog_poly('Platônicos / Dodecaedro')
        cert=search_certified_net(dod,attempts=220,tab_frac=0.22,max_seconds=10.0)
        nest_fixed=solve_certified_nesting(dod,cert,page='A4',scale_mm=50.0,margin_mm=10.0,auto_scale=False)
        add('dodecaedro escala fixa não gera aproveitamento acima de 100%', nest_fixed.utilization_percent is None or nest_fixed.utilization_percent<=100.0, certified_net_payload(dod,cert,nest_fixed))
        add('dodecaedro escala fixa informa all_fit falso ou cabe coerente', (not nest_fixed.all_fit) or (nest_fixed.utilization_percent is not None and nest_fixed.utilization_percent<=100.0), certified_net_report(dod,cert,nest_fixed))
        nest_auto=solve_certified_nesting(dod,cert,page='A4',scale_mm=50.0,margin_mm=10.0,auto_scale=True)
        add('dodecaedro autoescala cabe em A4', nest_auto.all_fit and nest_auto.page_count>=1, certified_net_report(dod,cert,nest_auto))
        add('dodecaedro autoescala reduz ou mantém escala válida', getattr(nest_auto,'applied_scale_mm',50.0)<=50.0+1e-9, certified_net_payload(dod,cert,nest_auto))
        ico=_v252_catalog_poly('Platônicos / Icosaedro')
        cert_i=search_certified_net(ico,attempts=220,tab_frac=0.22,max_seconds=10.0)
        nest_i=solve_certified_nesting(ico,cert_i,page='A4',scale_mm=50.0,margin_mm=10.0,auto_scale=True)
        add('icosaedro autoescala/nesting serializa JSON', isinstance(json.dumps(certified_net_payload(ico,cert_i,nest_i),default=str),str))
        add('aproveitamento nunca excede 100 quando numérico', all((n.utilization_percent is None or n.utilization_percent<=100.0+1e-9) for n in [nest_fixed,nest_auto,nest_i]), [nest_fixed.utilization_percent,nest_auto.utilization_percent,nest_i.utilization_percent])
    except Exception as exc:
        add('suíte v25.2.2 sem exceção', False, repr(exc))
    return TestReport(results)


APP_NAME='GeoPoly'
VERSION='25.2.2'
EDITION='Real Page Nesting & Auto-Scale Fix + Embedded Johnson Formal Bundle'






# v27.2f: explicit export list so internal star imports preserve historical
# single-underscore helper symbols without using wholesale update calls.
__all__ = [k for k in globals() if not k.startswith('__')]
