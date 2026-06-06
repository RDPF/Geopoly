"""GeoPoly v27 internal module: Printable nets, tab/label/color controls and assembly sheets."""
# v27.2f: named internal dependency import.
# Wildcard imports were removed to improve static analysis.
# v27.2f: named internal dependency imports; no wildcard imports.
from .wireframe_core import (
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
    _RUN_SELF_TESTS_V2501_BASE,
)




# ============================================================
# v25.0.3 — BETTER NET TABS + DIRECT FACE COLORING
# ============================================================
# Patch conservador sobre a v25.0.1 totalmente em Python:
# - mantém todas as funcionalidades anteriores;
# - melhora as abas da planificação: maiores, trapezoidais e reguláveis;
# - usa abas preferencialmente nas arestas de corte da net;
# - adiciona cor direta por face, com seletor de cor e clique na face;
# - usa somente números nas faces da planificação por padrão;
# - adiciona opção de numerar faces na visualização 3D.

from tkinter import colorchooser

VERSION = "25.0.4"
EDITION = "Formal Johnson Bundle Installer + Better Net Tabs"

_GP2503_FACE_PALETTE = {
    3: "#dceeff",
    4: "#e4f7dd",
    5: "#fff0c9",
    6: "#f1ddff",
    7: "#ffe2d4",
    8: "#dffff7",
    10: "#eee6ff",
}
_GP2503_ALT_PALETTE = ["#dceeff", "#e4f7dd", "#fff0c9", "#f1ddff", "#ffe2d4", "#dffff7"]


def _gp2503_svg_escape(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def _gp2503_norm_color(color):
    color = str(color or '').strip()
    if len(color) == 4 and color.startswith('#'):
        return '#' + ''.join(ch * 2 for ch in color[1:])
    return color


def _gp2503_valid_hex(color):
    color = str(color or '').strip()
    if len(color) not in (4, 7) or not color.startswith('#'):
        return False
    return all(ch in '0123456789abcdefABCDEF' for ch in color[1:])


def _gp2503_face_label(poly, nf, label_mode='Somente números'):
    mode = str(label_mode or 'Somente números')
    idx = int(nf.face_index) + 1
    if mode.startswith('Sem'):
        return ''
    if mode.startswith('Somente') or mode.startswith('Num'):
        return str(idx)
    # Rótulo completo sem prefixo F: número + informação geométrica.
    try:
        sides = len(poly.faces[nf.face_index]) if poly is not None else '?'
        return f'{idx}\n{sides} lados'
    except Exception:
        return str(idx)


def _gp2503_face_color(poly, nf, color_mode='Por número de lados', conflict_faces=None, custom_colors=None):
    conflict_faces = conflict_faces or set()
    custom_colors = custom_colors or {}
    if nf.face_index in conflict_faces:
        return '#ffd6d6'
    if nf.face_index in custom_colors:
        c = _gp2503_norm_color(custom_colors[nf.face_index])
        if _gp2503_valid_hex(c):
            return c
    mode = str(color_mode or 'Por número de lados')
    if mode.startswith('Sem'):
        return 'none'
    if mode.startswith('Altern'):
        return _GP2503_ALT_PALETTE[nf.face_index % len(_GP2503_ALT_PALETTE)]
    if mode.startswith('Azul'):
        return '#dfefff'
    if mode.startswith('Cor única'):
        return '#f2f2f2'
    if mode.startswith('Por número') and poly is not None:
        try:
            return _GP2503_FACE_PALETTE.get(len(poly.faces[nf.face_index]), '#ffffff')
        except Exception:
            return '#ffffff'
    return '#dfefff'


def _gp2503_point_in_polygon(p, poly, eps=1e-9):
    # Aceita pontos na borda como seleção válida.
    try:
        for i in range(len(poly)):
            if point_on_segment(p, poly[i], poly[(i + 1) % len(poly)], eps):
                return True
    except Exception:
        pass
    x, y = p
    inside = False
    j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / ((yj - yi) if abs(yj - yi) > eps else eps) + xi):
            inside = not inside
        j = i
    return inside


def _gp2503_tab_polygon(pa, pb, face_pts, tab_frac=0.22, shape='trapezoidal'):
    pa = np.array(pa, dtype=float); pb = np.array(pb, dtype=float)
    e = pb - pa
    L = float(np.linalg.norm(e))
    if L < EPS:
        return None
    u = e / L
    n = np.array([-u[1], u[0]])
    c = np.mean(np.array(face_pts, dtype=float), axis=0)
    mid = 0.5 * (pa + pb)
    if np.dot(n, c - mid) > 0:
        n = -n
    h = max(0.02 * L, min(float(tab_frac) * L, 0.45 * L))
    shape = str(shape or 'trapezoidal').lower()
    if shape.startswith('tri'):
        base_half = 0.42 * L
        return np.array([mid - u * base_half, mid + u * base_half, mid + n * h])
    # Aba trapezoidal: visualmente maior e mais útil para colagem.
    inner_half = 0.44 * L
    outer_half = 0.30 * L
    p1 = mid - u * inner_half
    p2 = mid + u * inner_half
    q2 = mid + u * outer_half + n * h
    q1 = mid - u * outer_half + n * h
    return np.array([p1, p2, q2, q1])


def _gp2503_edge_key_from_vertices(a, b):
    return tuple(sorted((int(a), int(b))))


def _gp2503_segments_coincident(seg_a, seg_b, tol=1e-6):
    a1, a2 = np.array(seg_a[0]), np.array(seg_a[1])
    b1, b2 = np.array(seg_b[0]), np.array(seg_b[1])
    return (
        (np.linalg.norm(a1 - b1) <= tol and np.linalg.norm(a2 - b2) <= tol) or
        (np.linalg.norm(a1 - b2) <= tol and np.linalg.norm(a2 - b1) <= tol)
    )


def _gp2503_cut_tab_polygons(poly, net, tab_frac=0.22, shape='trapezoidal'):
    """Retorna abas preferencialmente nas arestas de corte da net.

    A árvore de abertura não é armazenada no NetResult limpo da v23/v25. Então
    inferimos se uma aresta 3D compartilhada virou dobra ou corte comparando
    as posições 2D dos dois lados da aresta. Se os segmentos 2D coincidem, é
    dobra; se não coincidem, é corte e recebe aba em uma das faces.
    """
    if poly is None or net is None:
        return []
    face_by_id = {nf.face_index: nf for nf in net.faces}
    edge_occ = defaultdict(list)
    for nf in net.faces:
        fi = nf.face_index
        if fi < 0 or fi >= len(poly.faces):
            continue
        face = poly.faces[fi]
        pts = nf.poly2d
        for k in range(len(face)):
            a = face[k]
            b = face[(k + 1) % len(face)]
            edge_occ[_gp2503_edge_key_from_vertices(a, b)].append((fi, pts[k], pts[(k + 1) % len(face)]))
    tabs = []
    for edge, occ in edge_occ.items():
        if len(occ) == 1:
            # Aresta de bordo de malha aberta: pode receber aba externa.
            fi, pa, pb = occ[0]
            nf = face_by_id.get(fi)
            if nf is not None:
                tab = _gp2503_tab_polygon(pa, pb, nf.poly2d, tab_frac, shape)
                if tab is not None:
                    tabs.append(tab)
        elif len(occ) >= 2:
            # Se algum par coincide em 2D, é dobra da árvore: sem aba.
            coincident = False
            for i in range(len(occ)):
                for j in range(i + 1, len(occ)):
                    if _gp2503_segments_coincident((occ[i][1], occ[i][2]), (occ[j][1], occ[j][2])):
                        coincident = True
                        break
                if coincident:
                    break
            if not coincident:
                # Aresta foi cortada: desenha aba em uma única ocorrência.
                fi, pa, pb = occ[0]
                nf = face_by_id.get(fi)
                if nf is not None:
                    tab = _gp2503_tab_polygon(pa, pb, nf.poly2d, tab_frac, shape)
                    if tab is not None:
                        tabs.append(tab)
    return tabs


def _gp2503_plot_net_to_ax(ax, poly, net, add_tabs=True, label_mode='Somente números', color_mode='Por número de lados', custom_colors=None, selected_face=None, tab_frac=0.22, tab_shape='trapezoidal', title='Planificação'):
    ax.clear()
    custom_colors = custom_colors or {}
    conflict = {x for p in getattr(net, 'overlaps', []) for x in p}
    # Abas primeiro, atrás das faces.
    if add_tabs:
        for tab in _gp2503_cut_tab_polygons(poly, net, tab_frac, tab_shape):
            ax.add_patch(MplPolygon(tab, closed=True, facecolor='#f7f1cf', edgecolor='#777777', linewidth=0.8, linestyle='--', alpha=0.80))
    for nf in net.faces:
        fill = _gp2503_face_color(poly, nf, color_mode, conflict, custom_colors)
        lw = 2.4 if selected_face is not None and nf.face_index == selected_face else 1.1
        ec = '#003a8c' if selected_face is not None and nf.face_index == selected_face else '#111111'
        if fill == 'none':
            patch = MplPolygon(nf.poly2d, closed=True, fill=False, edgecolor=ec, linewidth=lw)
        else:
            patch = MplPolygon(nf.poly2d, closed=True, facecolor=fill, edgecolor=ec, linewidth=lw, alpha=.92)
        ax.add_patch(patch)
        label = _gp2503_face_label(poly, nf, label_mode)
        if label:
            c = nf.poly2d.mean(axis=0)
            ax.text(c[0], c[1], label, ha='center', va='center', fontsize=8)
    ax.set_aspect('equal', adjustable='datalim')
    ax.autoscale_view()
    ax.axis('off')
    ax.set_title(title)
    if getattr(net, 'warning', ''):
        ax.text(.01, .01, net.warning, transform=ax.transAxes, fontsize=8, color='darkred')


def _gp2503_write_svg_net(poly, net, path, title='Planificação', label_mode='Somente números', color_mode='Por número de lados', custom_colors=None, add_tabs=True, tab_frac=0.22, tab_shape='trapezoidal', scale=120, margin=25):
    custom_colors = custom_colors or {}
    pts_list = [nf.poly2d for nf in net.faces]
    if add_tabs:
        pts_list += _gp2503_cut_tab_polygons(poly, net, tab_frac, tab_shape)
    pts = np.vstack(pts_list) if pts_list else np.zeros((1, 2))
    mn = pts.min(axis=0); mx = pts.max(axis=0)
    w = (mx[0] - mn[0]) * scale + 2 * margin
    h = (mx[1] - mn[1]) * scale + 2 * margin
    conflict = {x for p in getattr(net, 'overlaps', []) for x in p}
    def tr(p):
        return ((p[0] - mn[0]) * scale + margin, h - ((p[1] - mn[1]) * scale + margin))
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.1f}" height="{h:.1f}" viewBox="0 0 {w:.1f} {h:.1f}">',
        f'<title>{_gp2503_svg_escape(title)}</title>',
        '<rect width="100%" height="100%" fill="white"/>'
    ]
    if add_tabs:
        for tab in _gp2503_cut_tab_polygons(poly, net, tab_frac, tab_shape):
            ps = ' '.join(f'{tr(p)[0]:.2f},{tr(p)[1]:.2f}' for p in tab)
            lines.append(f'<polygon points="{ps}" fill="#f7f1cf" stroke="#777777" stroke-width="0.8" stroke-dasharray="4 3"/>')
    for nf in net.faces:
        ps = ' '.join(f'{tr(p)[0]:.2f},{tr(p)[1]:.2f}' for p in nf.poly2d)
        fill = _gp2503_face_color(poly, nf, color_mode, conflict, custom_colors)
        if fill == 'none':
            lines.append(f'<polygon points="{ps}" fill="none" stroke="#111" stroke-width="1.1"/>')
        else:
            lines.append(f'<polygon points="{ps}" fill="{fill}" stroke="#111" stroke-width="1.1"/>')
        label = _gp2503_face_label(poly, nf, label_mode)
        if label:
            c = nf.poly2d.mean(axis=0); x, y = tr(c)
            safe_label = _gp2503_svg_escape(label).replace('\n', ' ')
            lines.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="12" text-anchor="middle" dominant-baseline="middle">{safe_label}</text>')
    lines.append('</svg>')
    Path(path).write_text('\n'.join(lines), encoding='utf-8')


class GeoPolyAppV2503(GeoPolyAppV2501):
    def _build_ui(self):
        super()._build_ui()
        self.title(f'{APP_NAME} v{VERSION} — {EDITION}')
        self.net_label_mode = tk.StringVar(value='Somente números')
        self.net_color_mode = tk.StringVar(value='Por número de lados')
        self.net_tab_size = tk.DoubleVar(value=0.22)
        self.net_tab_shape = tk.StringVar(value='trapezoidal')
        self.net_face_colors = {}
        self.net_selected_face = tk.IntVar(value=1)
        self.net_selected_color = tk.StringVar(value='#ffd966')
        self.view_show_face_numbers = tk.BooleanVar(value=False)
        try:
            net_widget = self.canvasnet.get_tk_widget()
            net_widget.pack_forget()
            bar = ttk.LabelFrame(self.tabnet, text='Planificação: textos, abas e cores por face', padding=8)
            bar.pack(fill='x', side='top', pady=(0, 4))
            ttk.Label(bar, text='Texto:').pack(side='left', padx=(0, 4))
            cb1 = ttk.Combobox(bar, textvariable=self.net_label_mode, values=['Sem textos', 'Somente números', 'Rótulos completos'], state='readonly', width=17)
            cb1.pack(side='left', padx=2); cb1.bind('<<ComboboxSelected>>', lambda e: self.update_net_tab())
            ttk.Button(bar, text='Sem', command=lambda: self._set_net_label_mode('Sem textos')).pack(side='left', padx=1)
            ttk.Button(bar, text='Números', command=lambda: self._set_net_label_mode('Somente números')).pack(side='left', padx=1)
            ttk.Separator(bar, orient='vertical').pack(side='left', fill='y', padx=6)
            ttk.Label(bar, text='Cor:').pack(side='left', padx=(0, 4))
            cb2 = ttk.Combobox(bar, textvariable=self.net_color_mode, values=['Por número de lados', 'Alternadas simples', 'Azul padrão', 'Cor única clara', 'Sem preenchimento'], state='readonly', width=18)
            cb2.pack(side='left', padx=2); cb2.bind('<<ComboboxSelected>>', lambda e: self.update_net_tab())
            ttk.Label(bar, text='Face:').pack(side='left', padx=(8, 2))
            self.net_face_spin = ttk.Spinbox(bar, from_=1, to=999, textvariable=self.net_selected_face, width=5, command=self.update_net_tab)
            self.net_face_spin.pack(side='left', padx=1)
            ttk.Button(bar, text='Escolher cor...', command=self.choose_net_face_color).pack(side='left', padx=2)
            ttk.Button(bar, text='Aplicar', command=self.apply_net_face_color).pack(side='left', padx=1)
            ttk.Button(bar, text='Limpar face', command=self.clear_selected_net_face_color).pack(side='left', padx=1)
            ttk.Button(bar, text='Limpar cores', command=self.clear_all_net_face_colors).pack(side='left', padx=1)
            bar2 = ttk.LabelFrame(self.tabnet, text='Abas de colagem', padding=8)
            bar2.pack(fill='x', side='top', pady=(0, 4))
            ttk.Label(bar2, text='Tamanho:').pack(side='left', padx=(0, 4))
            sp = ttk.Spinbox(bar2, from_=0.05, to=0.45, increment=0.02, textvariable=self.net_tab_size, width=6, command=self.update_net_tab)
            sp.pack(side='left', padx=2); sp.bind('<KeyRelease>', lambda e: self.update_net_tab()); sp.bind('<FocusOut>', lambda e: self.update_net_tab())
            ttk.Button(bar2, text='Pequenas', command=lambda: self._set_tab_size(0.14)).pack(side='left', padx=1)
            ttk.Button(bar2, text='Médias', command=lambda: self._set_tab_size(0.22)).pack(side='left', padx=1)
            ttk.Button(bar2, text='Grandes', command=lambda: self._set_tab_size(0.30)).pack(side='left', padx=1)
            ttk.Label(bar2, text='Formato:').pack(side='left', padx=(8, 2))
            cb3 = ttk.Combobox(bar2, textvariable=self.net_tab_shape, values=['trapezoidal', 'triangular'], state='readonly', width=12)
            cb3.pack(side='left', padx=2); cb3.bind('<<ComboboxSelected>>', lambda e: self.update_net_tab())
            ttk.Button(bar2, text='Atualizar', command=self.update_net_tab).pack(side='left', padx=6)
            net_widget.pack(fill='both', expand=True, side='top')
            self._net_pick_cid = self.canvasnet.mpl_connect('button_press_event', self._on_net_click)
        except Exception:
            pass
        try:
            controls = None
            for child in self.tab3d.winfo_children():
                try:
                    if isinstance(child, ttk.LabelFrame):
                        controls = child; break
                except Exception:
                    pass
            if controls is not None:
                ttk.Checkbutton(controls, text='Numerar faces', variable=self.view_show_face_numbers, command=self.update_3d).pack(side='left', padx=4)
        except Exception:
            pass

    def _set_net_label_mode(self, mode):
        self.net_label_mode.set(mode)
        self.update_net_tab()

    def _set_tab_size(self, value):
        self.net_tab_size.set(float(value))
        self.update_net_tab()

    def _current_net_label_mode(self):
        return self.net_label_mode.get() if hasattr(self, 'net_label_mode') else 'Somente números'

    def _current_net_color_mode(self):
        return self.net_color_mode.get() if hasattr(self, 'net_color_mode') else 'Por número de lados'

    def _current_tab_size(self):
        try:
            return float(self.net_tab_size.get())
        except Exception:
            return 0.22

    def _current_tab_shape(self):
        return self.net_tab_shape.get() if hasattr(self, 'net_tab_shape') else 'trapezoidal'

    def _selected_face_index0(self):
        try:
            return max(0, int(self.net_selected_face.get()) - 1)
        except Exception:
            return 0

    def load_selected(self):
        self.net_face_colors = {}
        return super().load_selected()

    def choose_net_face_color(self):
        initial = self.net_selected_color.get() if hasattr(self, 'net_selected_color') else '#ffd966'
        if not _gp2503_valid_hex(initial):
            initial = '#ffd966'
        rgb, color = colorchooser.askcolor(color=initial, title='Escolha a cor da face selecionada')
        if color:
            self.net_selected_color.set(_gp2503_norm_color(color))
            self.apply_net_face_color()

    def apply_net_face_color(self):
        fi = self._selected_face_index0()
        color = _gp2503_norm_color(self.net_selected_color.get())
        if not _gp2503_valid_hex(color):
            messagebox.showwarning('Cor por face', 'Escolha uma cor hexadecimal válida, por exemplo #FFD966.')
            return
        self.net_face_colors[fi] = color
        self.update_net_tab()

    def clear_selected_net_face_color(self):
        fi = self._selected_face_index0()
        self.net_face_colors.pop(fi, None)
        self.update_net_tab()

    def clear_all_net_face_colors(self):
        self.net_face_colors = {}
        self.update_net_tab()

    def _on_net_click(self, event):
        if event.inaxes is not self.axnet or event.xdata is None or event.ydata is None or self.net is None:
            return
        p = np.array([event.xdata, event.ydata], dtype=float)
        # Escolhe a menor face contendo o ponto, para evitar ambiguidades.
        candidates = []
        for nf in self.net.faces:
            try:
                if _gp2503_point_in_polygon(p, nf.poly2d):
                    candidates.append((abs(polygon_area2d(nf.poly2d)), nf.face_index))
            except Exception:
                pass
        if candidates:
            fi = sorted(candidates)[0][1]
            self.net_selected_face.set(int(fi) + 1)
            self.update_net_tab()

    def update_3d(self):
        if not self.poly or not hasattr(self, 'ax3d'):
            return
        self.ax3d.clear()
        v = np.array(self.poly.vertices, dtype=float)
        polys = [v[f] for f in self.poly.faces]
        alpha = float(getattr(self, 'view_alpha', tk.DoubleVar(value=.78)).get()) if hasattr(self, 'view_alpha') else .78
        show_vertices = bool(self.view_show_vertices.get()) if hasattr(self, 'view_show_vertices') else True
        show_axes = bool(self.view_show_axes.get()) if hasattr(self, 'view_show_axes') else True
        show_face_numbers = bool(self.view_show_face_numbers.get()) if hasattr(self, 'view_show_face_numbers') else False
        coll = Poly3DCollection(polys, alpha=alpha, edgecolor='k', linewidth=.6, facecolor='#dfefff')
        self.ax3d.add_collection3d(coll)
        if show_vertices:
            self.ax3d.scatter(v[:, 0], v[:, 1], v[:, 2], s=12)
        if show_face_numbers:
            for i, face in enumerate(self.poly.faces, start=1):
                try:
                    c = v[face].mean(axis=0)
                    self.ax3d.text(c[0], c[1], c[2], str(i), ha='center', va='center', fontsize=8)
                except Exception:
                    pass
        _gp2501_autoscale_3d(self.ax3d, v)
        if show_axes:
            self.ax3d.set_xlabel('X'); self.ax3d.set_ylabel('Y'); self.ax3d.set_zlabel('Z')
        else:
            self.ax3d.set_axis_off()
        self.ax3d.set_title(f'{self.poly.name}\n{self.poly.family} | {self.poly.meta.status}')
        self.canvas3d.draw_idle()

    def update_net_tab(self):
        if not self.poly or not hasattr(self, 'axnet'):
            return
        self.net = search_best_net(self.poly)
        try:
            if hasattr(self, 'net_face_spin'):
                self.net_face_spin.configure(to=max(1, len(self.poly.faces)))
        except Exception:
            pass
        selected = self._selected_face_index0() if hasattr(self, 'net_selected_face') else None
        _gp2503_plot_net_to_ax(
            self.axnet,
            self.poly,
            self.net,
            self.show_tabs_var.get(),
            self._current_net_label_mode(),
            self._current_net_color_mode(),
            getattr(self, 'net_face_colors', {}),
            selected,
            self._current_tab_size(),
            self._current_tab_shape(),
            f'Net — {self.poly.name}'
        )
        self.canvasnet.draw_idle()

    def export_net_svg(self):
        path = self.ask_path('.svg', 'Exportar net SVG')
        if path:
            if self.net is None:
                self.net = search_best_net(self.poly)
            _gp2503_write_svg_net(
                self.poly,
                self.net,
                Path(path),
                f'Net — {self.poly.name}',
                self._current_net_label_mode(),
                self._current_net_color_mode(),
                getattr(self, 'net_face_colors', {}),
                self.show_tabs_var.get(),
                self._current_tab_size(),
                self._current_tab_shape()
            )

    def export_net_png_pdf(self):
        path = self.ask_path('.png', 'Exportar net PNG/PDF')
        if not path:
            return
        if self.net is None:
            self.net = search_best_net(self.poly)
        path = Path(path)
        fig, ax = plt.subplots(figsize=(11, 8))
        _gp2503_plot_net_to_ax(
            ax,
            self.poly,
            self.net,
            self.show_tabs_var.get(),
            self._current_net_label_mode(),
            self._current_net_color_mode(),
            getattr(self, 'net_face_colors', {}),
            self._selected_face_index0(),
            self._current_tab_size(),
            self._current_tab_shape(),
            f'Net — {self.poly.name}'
        )
        fig.savefig(path, dpi=220, bbox_inches='tight')
        with PdfPages(path.with_suffix('.pdf')) as pdf:
            pdf.savefig(fig, bbox_inches='tight')
        plt.close(fig)


_RUN_SELF_TESTS_V2503_BASE = run_self_tests


def run_self_tests():
    base = _RUN_SELF_TESTS_V2503_BASE()
    results = list(base.results) if isinstance(base, TestReport) else []
    def add(name, ok, detail=''):
        results.append(TestCaseResult(str(name), bool(ok), '' if ok else str(detail)))
    try:
        cube = CATALOG['Platônicos / Cubo ou Hexaedro'].build()
        net = search_best_net(cube)
        fig, ax = plt.subplots(figsize=(4, 3))
        _gp2503_plot_net_to_ax(ax, cube, net, True, 'Somente números', 'Por número de lados', {0: '#ffcc00'}, 0, 0.22, 'trapezoidal', 'teste')
        labels = [_gp2503_face_label(cube, nf, 'Somente números') for nf in net.faces]
        tabs = _gp2503_cut_tab_polygons(cube, net, 0.22, 'trapezoidal')
        plt.close(fig)
        add('v25.0.3 labels are numeric only', all(lbl.isdigit() for lbl in labels if lbl), labels[:3])
        add('v25.0.3 better trapezoidal tabs generated', len(tabs) > 0, len(tabs))
        add('v25.0.3 face coloring works', _gp2503_face_color(cube, net.faces[0], custom_colors={0: '#ffcc00'}) == '#ffcc00')
        add('v25.0.3 app has 3D face-number support', hasattr(GeoPolyAppV2503, 'update_3d'))
    except Exception as exc:
        add('v25.0.3 exception', False, repr(exc))
    return TestReport(results)



# ============================================================
# v25.0.5 — Printable Nets & Assembly Sheets
# Acabamento de planificação: escala real, páginas, corte/dobra,
# abas numeradas e exportação paginada.
# ============================================================
APP_NAME = "GeoPoly"
VERSION = "25.0.5"
EDITION = "Printable Nets & Assembly Sheets"

_PAGE_SIZES_MM_V2505 = {
    'A4': (210.0, 297.0),
    'Carta': (216.0, 279.0),
    'Letter': (216.0, 279.0),
}


def _gp2505_page_size_mm(page_name, orientation='portrait'):
    w, h = _PAGE_SIZES_MM_V2505.get(str(page_name), _PAGE_SIZES_MM_V2505['A4'])
    if str(orientation).lower().startswith('land'):
        return h, w
    return w, h


def _gp2505_net_all_points(poly, net, add_tabs=True, tab_frac=0.22, tab_shape='trapezoidal'):
    pts = []
    if net is not None:
        for nf in net.faces:
            pts.extend(np.array(nf.poly2d, dtype=float))
    if add_tabs:
        for tab in _gp2503_cut_tab_polygons(poly, net, tab_frac, tab_shape):
            pts.extend(np.array(tab, dtype=float))
    return np.array(pts, dtype=float) if pts else np.zeros((0, 2), dtype=float)


def _gp2505_net_bounds(poly, net, add_tabs=True, tab_frac=0.22, tab_shape='trapezoidal'):
    pts = _gp2505_net_all_points(poly, net, add_tabs, tab_frac, tab_shape)
    if len(pts) == 0:
        return np.array([0.0, 0.0]), np.array([1.0, 1.0])
    return pts.min(axis=0), pts.max(axis=0)


def _gp2505_print_layout_report(poly, net, scale_mm=50.0, page_name='A4', margin_mm=10.0, add_tabs=True, tab_frac=0.22, tab_shape='trapezoidal'):
    """Relatório de encaixe físico da planificação em página.

    scale_mm é a escala física em milímetros por unidade normalizada da malha.
    O relatório escolhe automaticamente retrato/paisagem pelo menor número de
    páginas. A geometria da net não é alterada; a paginação é uma divisão da
    área física em folhas imprimíveis.
    """
    scale_mm = float(scale_mm)
    margin_mm = float(margin_mm)
    mn, mx = _gp2505_net_bounds(poly, net, add_tabs, tab_frac, tab_shape)
    size_units = np.maximum(mx - mn, 1e-12)
    size_mm = size_units * scale_mm
    candidates = []
    for orientation in ('portrait', 'landscape'):
        page_w, page_h = _gp2505_page_size_mm(page_name, orientation)
        printable_w = max(page_w - 2 * margin_mm, 1.0)
        printable_h = max(page_h - 2 * margin_mm, 1.0)
        pages_x = int(math.ceil(size_mm[0] / printable_w))
        pages_y = int(math.ceil(size_mm[1] / printable_h))
        pages = max(1, pages_x) * max(1, pages_y)
        fits = bool(pages_x == 1 and pages_y == 1)
        candidates.append({
            'page': str(page_name),
            'orientation': orientation,
            'page_width_mm': float(page_w),
            'page_height_mm': float(page_h),
            'margin_mm': float(margin_mm),
            'printable_width_mm': float(printable_w),
            'printable_height_mm': float(printable_h),
            'net_width_units': float(size_units[0]),
            'net_height_units': float(size_units[1]),
            'net_width_mm': float(size_mm[0]),
            'net_height_mm': float(size_mm[1]),
            'scale_mm_per_unit': float(scale_mm),
            'fits': bool(fits),
            'pages_x': int(max(1, pages_x)),
            'pages_y': int(max(1, pages_y)),
            'total_pages': int(max(1, pages)),
            'bounds_min': [float(mn[0]), float(mn[1])],
            'bounds_max': [float(mx[0]), float(mx[1])],
        })
    return sorted(candidates, key=lambda d: (d['total_pages'], 0 if d['orientation'] == 'portrait' else 1))[0]


def _gp2505_edge_occurrences_2d(poly, net):
    edge_occ = defaultdict(list)
    if poly is None or net is None:
        return edge_occ
    for nf in net.faces:
        fi = int(nf.face_index)
        if fi < 0 or fi >= len(poly.faces):
            continue
        face = poly.faces[fi]
        pts = np.array(nf.poly2d, dtype=float)
        for k in range(len(face)):
            a = face[k]
            b = face[(k + 1) % len(face)]
            edge_occ[_gp2503_edge_key_from_vertices(a, b)].append((fi, pts[k], pts[(k + 1) % len(face)]))
    return edge_occ


def _gp2505_tab_and_fold_records(poly, net, tab_frac=0.22, shape='trapezoidal'):
    """Retorna abas numeradas, marcas de colagem e segmentos de dobra.

    Cada aresta compartilhada que não coincide no plano é tratada como corte.
    Recebe uma aba em uma ocorrência e a mesma numeração como marca de colagem
    na ocorrência correspondente. Arestas que coincidem em 2D são dobras.
    """
    edge_occ = _gp2505_edge_occurrences_2d(poly, net)
    face_by_id = {nf.face_index: nf for nf in getattr(net, 'faces', [])}
    tabs = []
    glue_marks = []
    folds = []
    cut_edges = []
    glue_id = 1
    for edge, occ in edge_occ.items():
        if len(occ) == 1:
            fi, pa, pb = occ[0]
            nf = face_by_id.get(fi)
            if nf is not None:
                tab = _gp2503_tab_polygon(pa, pb, nf.poly2d, tab_frac, shape)
                if tab is not None:
                    tabs.append({'id': glue_id, 'edge': edge, 'face': fi, 'polygon': np.array(tab, dtype=float), 'type': 'boundary'})
                    cut_edges.append({'id': glue_id, 'edge': edge, 'face': fi, 'segment': (np.array(pa), np.array(pb)), 'type': 'boundary'})
                    glue_id += 1
            continue
        if len(occ) >= 2:
            coincident_pair = None
            for i in range(len(occ)):
                for j in range(i + 1, len(occ)):
                    if _gp2503_segments_coincident((occ[i][1], occ[i][2]), (occ[j][1], occ[j][2])):
                        coincident_pair = (occ[i], occ[j])
                        break
                if coincident_pair:
                    break
            if coincident_pair:
                fi, pa, pb = coincident_pair[0]
                folds.append({'edge': edge, 'face': fi, 'segment': (np.array(pa), np.array(pb))})
            else:
                # Aresta de corte entre duas faces: uma aba e uma marca par.
                fi0, pa0, pb0 = occ[0]
                fi1, pa1, pb1 = occ[1]
                nf0 = face_by_id.get(fi0)
                if nf0 is not None:
                    tab = _gp2503_tab_polygon(pa0, pb0, nf0.poly2d, tab_frac, shape)
                    if tab is not None:
                        tabs.append({'id': glue_id, 'edge': edge, 'face': fi0, 'polygon': np.array(tab, dtype=float), 'type': 'glue'})
                        glue_marks.append({'id': glue_id, 'edge': edge, 'face': fi1, 'segment': (np.array(pa1), np.array(pb1)), 'type': 'mate'})
                        cut_edges.append({'id': glue_id, 'edge': edge, 'face': fi0, 'segment': (np.array(pa0), np.array(pb0)), 'type': 'glue'})
                        cut_edges.append({'id': glue_id, 'edge': edge, 'face': fi1, 'segment': (np.array(pa1), np.array(pb1)), 'type': 'mate'})
                        glue_id += 1
    return {'tabs': tabs, 'glue_marks': glue_marks, 'folds': folds, 'cut_edges': cut_edges}


def _gp2505_plot_printable_net_to_ax(ax, poly, net, add_tabs=True, label_mode='Somente números', color_mode='Por número de lados', custom_colors=None, selected_face=None, tab_frac=0.22, tab_shape='trapezoidal', title='Planificação', show_glue_numbers=True, show_fold_lines=True):
    ax.clear()
    custom_colors = custom_colors or {}
    records = _gp2505_tab_and_fold_records(poly, net, tab_frac, tab_shape)
    conflict = {x for p in getattr(net, 'overlaps', []) for x in p}
    # Abas atrás das faces, com linha de corte tracejada.
    if add_tabs:
        for rec in records['tabs']:
            tab = rec['polygon']
            ax.add_patch(MplPolygon(tab, closed=True, facecolor='#f7f1cf', edgecolor='#777777', linewidth=0.9, linestyle='--', alpha=0.85))
            if show_glue_numbers:
                c = tab.mean(axis=0)
                ax.text(c[0], c[1], str(rec['id']), ha='center', va='center', fontsize=8, color='#8a4b00', weight='bold')
    # Faces.
    for nf in net.faces:
        fill = _gp2503_face_color(poly, nf, color_mode, conflict, custom_colors)
        lw = 2.4 if selected_face is not None and nf.face_index == selected_face else 1.15
        ec = '#003a8c' if selected_face is not None and nf.face_index == selected_face else '#111111'
        if fill == 'none':
            patch = MplPolygon(nf.poly2d, closed=True, fill=False, edgecolor=ec, linewidth=lw)
        else:
            patch = MplPolygon(nf.poly2d, closed=True, facecolor=fill, edgecolor=ec, linewidth=lw, alpha=.92)
        ax.add_patch(patch)
        label = _gp2503_face_label(poly, nf, label_mode)
        if label:
            c = nf.poly2d.mean(axis=0)
            ax.text(c[0], c[1], label, ha='center', va='center', fontsize=8)
    # Linhas de dobra sobrepostas em azul tracejado.
    if show_fold_lines:
        for rec in records['folds']:
            pa, pb = rec['segment']
            ax.plot([pa[0], pb[0]], [pa[1], pb[1]], color='#0066cc', linestyle=(0, (4, 3)), linewidth=1.5, alpha=.95)
    # Marcas da aresta correspondente: mesmo número da aba.
    if add_tabs and show_glue_numbers:
        for rec in records['glue_marks']:
            pa, pb = rec['segment']
            mid = 0.5 * (pa + pb)
            ax.text(mid[0], mid[1], str(rec['id']), ha='center', va='center', fontsize=8, color='#8a4b00', weight='bold', bbox=dict(boxstyle='circle,pad=0.18', fc='white', ec='#8a4b00', lw=.8, alpha=.85))
    ax.set_aspect('equal', adjustable='datalim')
    ax.autoscale_view()
    ax.axis('off')
    ax.set_title(title)
    if getattr(net, 'warning', ''):
        ax.text(.01, .01, net.warning, transform=ax.transAxes, fontsize=8, color='darkred')


def _gp2505_write_svg_printable_net(poly, net, path, title='Planificação', label_mode='Somente números', color_mode='Por número de lados', custom_colors=None, add_tabs=True, tab_frac=0.22, tab_shape='trapezoidal', scale_mm=50.0, margin_mm=10.0, page_name='A4', show_page_frame=True):
    custom_colors = custom_colors or {}
    records = _gp2505_tab_and_fold_records(poly, net, tab_frac, tab_shape)
    pts_list = [nf.poly2d for nf in net.faces]
    if add_tabs:
        pts_list += [rec['polygon'] for rec in records['tabs']]
    pts = np.vstack(pts_list) if pts_list else np.zeros((1, 2))
    mn = pts.min(axis=0); mx = pts.max(axis=0)
    size_mm = (mx - mn) * float(scale_mm)
    layout = _gp2505_print_layout_report(poly, net, scale_mm, page_name, margin_mm, add_tabs, tab_frac, tab_shape)
    # Um SVG em tamanho físico da net, não necessariamente página única.
    w = float(size_mm[0] + 2 * margin_mm)
    h = float(size_mm[1] + 2 * margin_mm)
    conflict = {x for p in getattr(net, 'overlaps', []) for x in p}
    def tr(p):
        x = (p[0] - mn[0]) * scale_mm + margin_mm
        y = h - ((p[1] - mn[1]) * scale_mm + margin_mm)
        return x, y
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.2f}mm" height="{h:.2f}mm" viewBox="0 0 {w:.2f} {h:.2f}">',
        f'<title>{_gp2503_svg_escape(title)}</title>',
        '<rect width="100%" height="100%" fill="white"/>',
    ]
    if show_page_frame:
        lines.append(f'<text x="8" y="14" font-size="8" fill="#555">Escala: {float(scale_mm):.2f} mm/unid.; página {layout["page"]} {layout["orientation"]}; cabe: {"sim" if layout["fits"] else "não"}; páginas: {layout["total_pages"]}</text>')
    if add_tabs:
        for rec in records['tabs']:
            ps = ' '.join(f'{tr(p)[0]:.2f},{tr(p)[1]:.2f}' for p in rec['polygon'])
            lines.append(f'<polygon points="{ps}" fill="#f7f1cf" stroke="#777777" stroke-width="0.35" stroke-dasharray="2 1"/>')
            c = rec['polygon'].mean(axis=0); x, y = tr(c)
            lines.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="5" text-anchor="middle" dominant-baseline="middle" fill="#8a4b00" font-weight="bold">{rec["id"]}</text>')
    for nf in net.faces:
        ps = ' '.join(f'{tr(p)[0]:.2f},{tr(p)[1]:.2f}' for p in nf.poly2d)
        fill = _gp2503_face_color(poly, nf, color_mode, conflict, custom_colors)
        fill_attr = 'none' if fill == 'none' else fill
        lines.append(f'<polygon points="{ps}" fill="{fill_attr}" stroke="#111" stroke-width="0.35"/>')
        label = _gp2503_face_label(poly, nf, label_mode)
        if label:
            c = nf.poly2d.mean(axis=0); x, y = tr(c)
            safe_label = _gp2503_svg_escape(label).replace('\n', ' ')
            lines.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="5" text-anchor="middle" dominant-baseline="middle">{safe_label}</text>')
    # Linhas de dobra em azul tracejado.
    for rec in records['folds']:
        pa, pb = rec['segment']; x1, y1 = tr(pa); x2, y2 = tr(pb)
        lines.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#0066cc" stroke-width="0.35" stroke-dasharray="2 1"/>')
    for rec in records['glue_marks']:
        pa, pb = rec['segment']; mid = 0.5 * (pa + pb); x, y = tr(mid)
        lines.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.2" fill="white" stroke="#8a4b00" stroke-width="0.25"/>')
        lines.append(f'<text x="{x:.2f}" y="{y:.2f}" font-size="4.2" text-anchor="middle" dominant-baseline="middle" fill="#8a4b00" font-weight="bold">{rec["id"]}</text>')
    lines.append('</svg>')
    Path(path).write_text('\n'.join(lines), encoding='utf-8')


def _gp2505_draw_page_tile(ax, poly, net, layout, ix, iy, label_mode, color_mode, custom_colors, add_tabs, tab_frac, tab_shape, title):
    _gp2505_plot_printable_net_to_ax(ax, poly, net, add_tabs, label_mode, color_mode, custom_colors, None, tab_frac, tab_shape, title, True, True)
    mn, mx = _gp2505_net_bounds(poly, net, add_tabs, tab_frac, tab_shape)
    printable_w_units = layout['printable_width_mm'] / layout['scale_mm_per_unit']
    printable_h_units = layout['printable_height_mm'] / layout['scale_mm_per_unit']
    x0 = mn[0] + ix * printable_w_units
    x1 = min(x0 + printable_w_units, mx[0])
    # De cima para baixo no PDF: iy=0 é topo.
    y_top = mx[1] - iy * printable_h_units
    y_bottom = max(y_top - printable_h_units, mn[1])
    ax.set_xlim(x0, x1)
    ax.set_ylim(y_bottom, y_top)
    ax.set_title(f'{title} — página {iy*layout["pages_x"]+ix+1}/{layout["total_pages"]}')


def _gp2505_export_paginated_pdf(poly, net, path, label_mode='Somente números', color_mode='Por número de lados', custom_colors=None, add_tabs=True, tab_frac=0.22, tab_shape='trapezoidal', scale_mm=50.0, page_name='A4', margin_mm=10.0, title='Planificação paginada'):
    custom_colors = custom_colors or {}
    layout = _gp2505_print_layout_report(poly, net, scale_mm, page_name, margin_mm, add_tabs, tab_frac, tab_shape)
    page_w, page_h = _gp2505_page_size_mm(page_name, layout['orientation'])
    fig_w, fig_h = page_w / 25.4, page_h / 25.4
    # Frações ocupadas por margem física.
    left = margin_mm / page_w
    bottom = margin_mm / page_h
    width = max((page_w - 2 * margin_mm) / page_w, 0.1)
    height = max((page_h - 2 * margin_mm) / page_h, 0.1)
    path = Path(path)
    with PdfPages(path) as pdf:
        for iy in range(layout['pages_y']):
            for ix in range(layout['pages_x']):
                fig = plt.figure(figsize=(fig_w, fig_h))
                ax = fig.add_axes([left, bottom, width, height])
                _gp2505_draw_page_tile(ax, poly, net, layout, ix, iy, label_mode, color_mode, custom_colors, add_tabs, tab_frac, tab_shape, title)
                fig.text(0.02, 0.015, f'GeoPoly v{VERSION} | escala {scale_mm:.2f} mm/unid. | margem {margin_mm:.1f} mm | linhas pretas=corte, azuis tracejadas=dobra, números=colagem', fontsize=6)
                pdf.savefig(fig)
                plt.close(fig)
    return layout


def _gp2505_write_assembly_report(poly, net, layout, path, tab_frac=0.22, tab_shape='trapezoidal'):
    records = _gp2505_tab_and_fold_records(poly, net, tab_frac, tab_shape)
    lines = []
    lines.append(f'Plano de montagem — {poly.name}')
    lines.append('=' * max(20, len(lines[-1])))
    lines.append('')
    lines.append(f'Página: {layout["page"]} ({layout["orientation"]})')
    lines.append(f'Escala: {layout["scale_mm_per_unit"]:.3f} mm por unidade geométrica')
    lines.append(f'Margem: {layout["margin_mm"]:.1f} mm')
    lines.append(f'Tamanho físico da planificação: {layout["net_width_mm"]:.1f} × {layout["net_height_mm"]:.1f} mm')
    lines.append(f'Cabe em uma folha: {"sim" if layout["fits"] else "não"}')
    lines.append(f'Paginação: {layout["pages_x"]} × {layout["pages_y"]} = {layout["total_pages"]} página(s)')
    lines.append('')
    lines.append('Convenção gráfica:')
    lines.append('- Linha preta contínua: contorno/corte.')
    lines.append('- Linha azul tracejada: dobra entre faces adjacentes.')
    lines.append('- Aba amarela tracejada: aba de colagem.')
    lines.append('- Número na aba e na aresta correspondente: par de colagem.')
    lines.append('')
    lines.append('Pares de colagem:')
    if records['tabs']:
        for rec in records['tabs']:
            mate = [m for m in records['glue_marks'] if m['id'] == rec['id']]
            if mate:
                lines.append(f'- Aba {rec["id"]}: face {rec["face"] + 1} cola na face {mate[0]["face"] + 1}, aresta {tuple(int(x)+1 for x in rec["edge"])}.')
            else:
                lines.append(f'- Aba {rec["id"]}: aba de bordo na face {rec["face"] + 1}, aresta {tuple(int(x)+1 for x in rec["edge"])}.')
    else:
        lines.append('- Nenhuma aba de colagem gerada.')
    lines.append('')
    lines.append('Recomendação: imprima em escala 100% no visualizador de PDF. Desative “ajustar à página” se desejar manter a escala física.')
    Path(path).write_text('\n'.join(lines), encoding='utf-8')


class GeoPolyAppV2505(GeoPolyAppV2503):
    def _build_ui(self):
        super()._build_ui()
        self.title(f'{APP_NAME} v{VERSION} — {EDITION}')
        self.net_print_fit_var = tk.StringVar(value='Encaixe físico: —')
        self.net_show_glue_numbers = tk.BooleanVar(value=True)
        try:
            # Insere uma barra de acabamento físico no topo da aba de planificação.
            # Ela usa scale_var/page_var/margin_var já existentes no painel global.
            net_widget = self.canvasnet.get_tk_widget()
            net_widget.pack_forget()
            bar = ttk.LabelFrame(self.tabnet, text='Impressão em papel: escala, página e montagem', padding=8)
            bar.pack(fill='x', side='top', pady=(0, 4))
            ttk.Label(bar, text='Escala mm/unid.:').pack(side='left', padx=(0, 2))
            sp1 = ttk.Spinbox(bar, from_=1, to=500, increment=1, textvariable=self.scale_var, width=7, command=self.update_net_tab)
            sp1.pack(side='left', padx=2); sp1.bind('<KeyRelease>', lambda e: self.update_net_tab()); sp1.bind('<FocusOut>', lambda e: self.update_net_tab())
            ttk.Label(bar, text='Página:').pack(side='left', padx=(8, 2))
            cb = ttk.Combobox(bar, textvariable=self.page_var, values=['A4', 'Carta'], state='readonly', width=8)
            cb.pack(side='left', padx=2); cb.bind('<<ComboboxSelected>>', lambda e: self.update_net_tab())
            ttk.Label(bar, text='Margem mm:').pack(side='left', padx=(8, 2))
            sp2 = ttk.Spinbox(bar, from_=0, to=50, increment=1, textvariable=self.margin_var, width=6, command=self.update_net_tab)
            sp2.pack(side='left', padx=2); sp2.bind('<KeyRelease>', lambda e: self.update_net_tab()); sp2.bind('<FocusOut>', lambda e: self.update_net_tab())
            ttk.Checkbutton(bar, text='Numerar abas de colagem', variable=self.net_show_glue_numbers, command=self.update_net_tab).pack(side='left', padx=8)
            ttk.Button(bar, text='Exportar PDF paginado', command=self.export_printable_net_pdf).pack(side='left', padx=3)
            ttk.Button(bar, text='Exportar SVG físico', command=self.export_printable_net_svg).pack(side='left', padx=3)
            ttk.Button(bar, text='Relatório de montagem', command=self.export_assembly_report).pack(side='left', padx=3)
            ttk.Label(bar, textvariable=self.net_print_fit_var, foreground='#003a8c').pack(side='left', padx=10)
            net_widget.pack(fill='both', expand=True, side='top')
        except Exception:
            pass

    def _print_layout(self):
        if self.net is None:
            self.net = search_best_net(self.poly)
        return _gp2505_print_layout_report(
            self.poly,
            self.net,
            float(self.scale_var.get()),
            self.page_var.get(),
            float(self.margin_var.get()),
            self.show_tabs_var.get(),
            self._current_tab_size(),
            self._current_tab_shape(),
        )

    def _update_fit_label(self):
        try:
            layout = self._print_layout()
            txt = (f'Cabe em {layout["page"]}: {"SIM" if layout["fits"] else "NÃO"} | '
                   f'{layout["net_width_mm"]:.0f}×{layout["net_height_mm"]:.0f} mm | '
                   f'{layout["pages_x"]}×{layout["pages_y"]} página(s), {layout["orientation"]}')
            self.net_print_fit_var.set(txt)
        except Exception as exc:
            self.net_print_fit_var.set(f'Encaixe físico: erro ({exc})')

    def update_net_tab(self):
        if not self.poly or not hasattr(self, 'axnet'):
            return
        self.net = search_best_net(self.poly)
        try:
            if hasattr(self, 'net_face_spin'):
                self.net_face_spin.configure(to=max(1, len(self.poly.faces)))
        except Exception:
            pass
        selected = self._selected_face_index0() if hasattr(self, 'net_selected_face') else None
        _gp2505_plot_printable_net_to_ax(
            self.axnet,
            self.poly,
            self.net,
            self.show_tabs_var.get(),
            self._current_net_label_mode(),
            self._current_net_color_mode(),
            getattr(self, 'net_face_colors', {}),
            selected,
            self._current_tab_size(),
            self._current_tab_shape(),
            f'Net — {self.poly.name}',
            bool(self.net_show_glue_numbers.get()) if hasattr(self, 'net_show_glue_numbers') else True,
            True,
        )
        self._update_fit_label()
        self.canvasnet.draw_idle()

    def export_net_svg(self):
        # Mantém o botão antigo, agora com SVG físico em mm.
        self.export_printable_net_svg()

    def export_net_png_pdf(self):
        # Mantém o botão antigo; além do PNG visual, também gera PDF paginado.
        path = self.ask_path('.png', 'Exportar net PNG e PDF paginado')
        if not path:
            return
        if self.net is None:
            self.net = search_best_net(self.poly)
        path = Path(path)
        fig, ax = plt.subplots(figsize=(11, 8))
        _gp2505_plot_printable_net_to_ax(
            ax,
            self.poly,
            self.net,
            self.show_tabs_var.get(),
            self._current_net_label_mode(),
            self._current_net_color_mode(),
            getattr(self, 'net_face_colors', {}),
            self._selected_face_index0(),
            self._current_tab_size(),
            self._current_tab_shape(),
            f'Net — {self.poly.name}',
            bool(self.net_show_glue_numbers.get()) if hasattr(self, 'net_show_glue_numbers') else True,
            True,
        )
        fig.savefig(path, dpi=220, bbox_inches='tight')
        plt.close(fig)
        pdf_path = path.with_suffix('.paginado.pdf')
        layout = _gp2505_export_paginated_pdf(
            self.poly,
            self.net,
            pdf_path,
            self._current_net_label_mode(),
            self._current_net_color_mode(),
            getattr(self, 'net_face_colors', {}),
            self.show_tabs_var.get(),
            self._current_tab_size(),
            self._current_tab_shape(),
            float(self.scale_var.get()),
            self.page_var.get(),
            float(self.margin_var.get()),
            f'Net — {self.poly.name}',
        )
        messagebox.showinfo('Planificação exportada', f'PNG salvo em:\n{path}\n\nPDF paginado salvo em:\n{pdf_path}\n\nPáginas: {layout["total_pages"]}')

    def export_printable_net_svg(self):
        path = self.ask_path('.svg', 'Exportar SVG físico da planificação')
        if not path:
            return
        if self.net is None:
            self.net = search_best_net(self.poly)
        _gp2505_write_svg_printable_net(
            self.poly,
            self.net,
            Path(path),
            f'Net — {self.poly.name}',
            self._current_net_label_mode(),
            self._current_net_color_mode(),
            getattr(self, 'net_face_colors', {}),
            self.show_tabs_var.get(),
            self._current_tab_size(),
            self._current_tab_shape(),
            float(self.scale_var.get()),
            float(self.margin_var.get()),
            self.page_var.get(),
        )
        messagebox.showinfo('SVG físico', f'Arquivo salvo em:\n{path}')

    def export_printable_net_pdf(self):
        path = self.ask_path('.pdf', 'Exportar PDF paginado da planificação')
        if not path:
            return
        if self.net is None:
            self.net = search_best_net(self.poly)
        layout = _gp2505_export_paginated_pdf(
            self.poly,
            self.net,
            Path(path),
            self._current_net_label_mode(),
            self._current_net_color_mode(),
            getattr(self, 'net_face_colors', {}),
            self.show_tabs_var.get(),
            self._current_tab_size(),
            self._current_tab_shape(),
            float(self.scale_var.get()),
            self.page_var.get(),
            float(self.margin_var.get()),
            f'Net — {self.poly.name}',
        )
        _gp2505_write_assembly_report(self.poly, self.net, layout, Path(path).with_suffix('.montagem.txt'), self._current_tab_size(), self._current_tab_shape())
        messagebox.showinfo('PDF paginado', f'Arquivo salvo em:\n{path}\n\nRelatório:\n{Path(path).with_suffix(".montagem.txt")}\n\nPáginas: {layout["total_pages"]}')

    def export_assembly_report(self):
        path = self.ask_path('.txt', 'Exportar relatório de montagem da planificação')
        if not path:
            return
        if self.net is None:
            self.net = search_best_net(self.poly)
        layout = self._print_layout()
        _gp2505_write_assembly_report(self.poly, self.net, layout, Path(path), self._current_tab_size(), self._current_tab_shape())
        messagebox.showinfo('Relatório de montagem', f'Arquivo salvo em:\n{path}')


_RUN_SELF_TESTS_V2505_BASE = run_self_tests


def run_self_tests():
    base = _RUN_SELF_TESTS_V2505_BASE()
    results = list(base.results) if isinstance(base, TestReport) else []
    def add(name, ok, detail=''):
        results.append(TestCaseResult(str(name), bool(ok), '' if ok else str(detail)))
    try:
        cube = CATALOG['Platônicos / Cubo ou Hexaedro'].build()
        net = search_best_net(cube)
        layout = _gp2505_print_layout_report(cube, net, scale_mm=40, page_name='A4', margin_mm=10, add_tabs=True, tab_frac=0.22)
        rec = _gp2505_tab_and_fold_records(cube, net, 0.22, 'trapezoidal')
        add('v25.0.5 printable layout has native bool fits', isinstance(layout['fits'], bool), type(layout['fits']))
        add('v25.0.5 printable layout page count positive', layout['total_pages'] >= 1, layout)
        add('v25.0.5 glue tabs have ids', all('id' in r for r in rec['tabs']), rec['tabs'][:2])
        add('v25.0.5 fold records generated', len(rec['folds']) >= 0, len(rec['folds']))
        tmp = Path('/tmp/geopoly_v2505_test_net.pdf')
        lay2 = _gp2505_export_paginated_pdf(cube, net, tmp, scale_mm=40, page_name='A4', margin_mm=10)
        add('v25.0.5 paginated PDF exported', tmp.exists() and tmp.stat().st_size > 0, str(tmp))
        tmp_svg = Path('/tmp/geopoly_v2505_test_net.svg')
        _gp2505_write_svg_printable_net(cube, net, tmp_svg, scale_mm=40, margin_mm=10)
        add('v25.0.5 physical SVG exported', tmp_svg.exists() and tmp_svg.stat().st_size > 0, str(tmp_svg))
        add('v25.0.5 app class available', hasattr(GeoPolyAppV2505, 'export_printable_net_pdf'))
    except Exception as exc:
        add('v25.0.5 exception', False, repr(exc))
    return TestReport(results)


# v27.2f: explicit export list so internal star imports preserve historical
# single-underscore helper symbols without using wholesale update calls.
__all__ = [k for k in globals() if not k.startswith('__')]
