"""GeoPoly v27 internal module: Robust predicates, half-edge topology, symmetry and canonical lab."""
# v27.2f: named internal dependency import.
# Wildcard imports were removed to improve static analysis.
# v27.2f: named internal dependency imports; no wildcard imports.
from .core_geometry_catalog import (
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
    _ORIENT2D_BOUND, _ORIENT3D_BOUND, _consistent_face_orientation_v272g,
)

def _frac(x: float) -> Fraction:
    return Fraction(float(x))

def robust_orient2d(a, b, c):
    """Adaptive exact sign of the oriented area of triangle (a,b,c).

    Returns +1, -1 or 0. A fast float path is used when safe; near-degenerate
    cases fall back to exact rational arithmetic over the actual IEEE-754 values.
    """
    ax, ay = float(a[0]), float(a[1]); bx, by = float(b[0]), float(b[1]); cx, cy = float(c[0]), float(c[1])
    det = (bx-ax)*(cy-ay) - (by-ay)*(cx-ax)
    if abs(det) > _ORIENT2D_BOUND:
        return 1 if det > 0 else -1
    AX, AY, BX, BY, CX, CY = map(_frac, [ax, ay, bx, by, cx, cy])
    exact = (BX-AX)*(CY-AY) - (BY-AY)*(CX-AX)
    return 1 if exact > 0 else (-1 if exact < 0 else 0)

def robust_orient3d(a, b, c, d):
    """Adaptive exact sign of the oriented volume of tetrahedron (a,b,c,d)."""
    A=np.array(a,dtype=float); B=np.array(b,dtype=float); C=np.array(c,dtype=float); D=np.array(d,dtype=float)
    M=np.vstack([B-A,C-A,D-A])
    det=float(np.linalg.det(M))
    if abs(det)>_ORIENT3D_BOUND:
        return 1 if det>0 else -1
    af=[_frac(x) for x in A]
    rows=[]
    for P in [B,C,D]: rows.append([_frac(P[i])-af[i] for i in range(3)])
    exact=(rows[0][0]*(rows[1][1]*rows[2][2]-rows[1][2]*rows[2][1])
           -rows[0][1]*(rows[1][0]*rows[2][2]-rows[1][2]*rows[2][0])
           +rows[0][2]*(rows[1][0]*rows[2][1]-rows[1][1]*rows[2][0]))
    return 1 if exact>0 else (-1 if exact<0 else 0)

def segments_properly_intersect_robust(p1,p2,p3,p4):
    d1=robust_orient2d(p3,p4,p1); d2=robust_orient2d(p3,p4,p2); d3=robust_orient2d(p1,p2,p3); d4=robust_orient2d(p1,p2,p4)
    return (d1!=0 and d2!=0 and d3!=0 and d4!=0 and ((d1>0)!=(d2>0)) and ((d3>0)!=(d4>0)))

# Keep old function names used by poly_overlap.
def robust_seg_inter(a,b,c,d,eps=1e-8):
    return segments_properly_intersect_robust(a,b,c,d)

def robust_point_on_segment(p,a,b,eps=1e-8):
    if robust_orient2d(a,b,p)!=0: return False
    p=np.array(p,dtype=float); a=np.array(a,dtype=float); b=np.array(b,dtype=float)
    return min(a[0],b[0])-eps<=p[0]<=max(a[0],b[0])+eps and min(a[1],b[1])-eps<=p[1]<=max(a[1],b[1])+eps

# ============================================================
# v24.0 — SOTA FUSION: HALF-EDGE / DCEL TOPOLOGY
# ============================================================
@dataclass
class HalfEdge:
    origin:int
    face:int
    next:int=-1
    twin:int=-1
    index:int=-1

class HalfEdgeMesh:
    """Half-edge/DCEL mesh built from the current Polyhedron faces."""
    def __init__(self, vertices, faces):
        self.vertices=np.asarray(vertices,dtype=float)
        self.faces=[list(map(int,f)) for f in faces]
        self.half_edges=[]
        self.face_half_edge=[]
        self.vertex_half_edge=[-1]*len(self.vertices)
        self._edge_lookup={}
        self._build()
    def _build(self):
        for fi,face in enumerate(self.faces):
            base=len(self.half_edges); n=len(face)
            self.face_half_edge.append(base)
            for k in range(n):
                he=HalfEdge(origin=face[k],face=fi,index=base+k,next=base+(k+1)%n)
                self.half_edges.append(he)
                if 0<=face[k]<len(self.vertex_half_edge) and self.vertex_half_edge[face[k]]<0:
                    self.vertex_half_edge[face[k]]=he.index
            for k in range(n):
                a,b=face[k],face[(k+1)%n]
                self._edge_lookup[(a,b)]=base+k
        for (a,b),hi in list(self._edge_lookup.items()):
            self.half_edges[hi].twin=self._edge_lookup.get((b,a),-1)
    def edge_faces(self):
        out={}
        for he in self.half_edges:
            nxt=self.half_edges[he.next].origin
            key=tuple(sorted((he.origin,nxt)))
            out.setdefault(key,[])
            if he.face not in out[key]: out[key].append(he.face)
        return out
    def dual_adjacency(self):
        adj = {i: [] for i in range(len(self.faces))}
        for edge, fs in self.edge_faces().items():
            if len(fs) == 2:
                a, b = fs
                adj[a].append((b, edge))
                adj[b].append((a, edge))
        return adj
    def faces_around_vertex(self,vi):
        out=[]; seen=set()
        for he in self.half_edges:
            if he.origin==vi and he.face not in seen:
                seen.add(he.face); out.append(he.face)
        return out
    def euler(self):
        V=len({v for f in self.faces for v in f}); E=len(self.edge_faces()); F=len(self.faces); return V,E,F,V-E+F
    def is_closed(self):
        ef = self.edge_faces()
        return bool(ef) and all(len(fs) == 2 for fs in ef.values())
    def is_manifold(self):
        ef = self.edge_faces()
        return bool(ef) and all(len(fs) == 2 for fs in ef.values())
    def _components(self):
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
    def genus_hint(self):
        if not (self.is_closed() and self.is_manifold()):
            return None
        V, E, F, chi = self.euler()
        if self._components() != 1:
            return None
        _, orientable, _ = _consistent_face_orientation_v272g(self.faces)
        return (2 - chi) / 2.0 if orientable else None

def halfedge_mesh(poly):
    return HalfEdgeMesh(poly.vertices, poly.faces)

# ============================================================
# v24.2 — ADVANCED SYMMETRY AND ORBIT REPORT
# ============================================================
@dataclass
class SymmetryReportV242:
    rotation_order:int
    axis_counts:Dict[int,int]
    group:str
    has_inversion:bool
    vertex_orbits:List[List[int]]=field(default_factory=list)
    edge_orbits:List[List[Tuple[int,int]]]=field(default_factory=list)
    face_orbits:List[List[int]]=field(default_factory=list)
    vertex_transitive:bool=False
    edge_transitive:bool=False
    face_transitive:bool=False
    vertex_stabilizers:List[float]=field(default_factory=list)
    edge_stabilizers:List[float]=field(default_factory=list)
    face_stabilizers:List[float]=field(default_factory=list)
    max_mapping_error:float=0.0
    mean_mapping_error:float=0.0
    warning:str='Análise aproximada por rotações que permutam vértices em tolerância numérica; não é prova algébrica completa do grupo de simetria.'
    def as_dict(self):
        d=asdict(self)
        d['edge_orbits']=[[list(e) for e in orb] for orb in self.edge_orbits]
        return d

# Backward-compatible name used by some earlier comments/tests.
SymmetryReportV24 = SymmetryReportV242

def _rot_matrix(axis, angle):
    axis=np.array(axis,dtype=float); L=np.linalg.norm(axis); axis=axis/(L if L>EPS else 1.0)
    x,y,z=axis; c=math.cos(angle); s=math.sin(angle); t=1-c
    return np.array([[t*x*x+c,t*x*y-s*z,t*x*z+s*y],[t*x*y+s*z,t*y*y+c,t*y*z-s*x],[t*x*z-s*y,t*y*z+s*x,t*z*z+c]])

def _nearest_permutation(V,W,tol=1e-4):
    """Return permutation p such that W[i] maps to V[p[i]], or None.

    O(N^2) implementation avoids a hard scipy dependency and is acceptable for
    the educational catalog sizes used here.  The returned permutation acts on
    vertex indices.
    """
    V=np.asarray(V); W=np.asarray(W); used=set(); perm=[]
    for w in W:
        d=np.linalg.norm(V-w,axis=1)
        idx=int(np.argmin(d))
        if d[idx]>tol or idx in used: return None
        used.add(idx); perm.append(idx)
    return perm

def _permutation_residual(V,W,perm):
    if perm is None or len(perm)==0: return float('inf')
    return float(max(np.linalg.norm(W[i]-V[perm[i]]) for i in range(len(perm))))

def _maps_vertex_set(V,R,tol=1e-4):
    W=V@R.T
    return _nearest_permutation(V,W,tol) is not None

def _classify_symmetry(order, axis_counts, vtrans=False, etrans=False, ftrans=False):
    if order>=60 or axis_counts.get(5,0)>=6: base='Icosaédrico aproximado (I)'
    elif order>=24 or axis_counts.get(4,0)>=3: base='Octaédrico aproximado (O)'
    elif order>=12 and axis_counts.get(3,0)>=4: base='Tetraédrico aproximado (T)'
    else:
        principal=max([k for k in axis_counts if k>=2], default=1)
        if principal>=2 and order>=2*principal: base=f'Diédrico/cíclico aproximado (ordem {order})'
        else: base=f'Baixa simetria / assimétrico (ordem {order})'
    flags=[]
    if vtrans: flags.append('V-transitivo')
    if etrans: flags.append('E-transitivo')
    if ftrans: flags.append('F-transitivo')
    return base + ((' — ' + ', '.join(flags)) if flags else '')

def _rotation_group_matrices(poly, tol=1e-4, max_axes=360):
    V=poly.vertices - np.mean(poly.vertices,axis=0)
    scale=np.max(np.linalg.norm(V,axis=1)) if len(V) else 1.0
    V=V/(scale if scale>EPS else 1.0)
    axes=[]; candidates=[]
    candidates.extend(list(V))
    for a,b in poly.edges(): candidates.append((V[a]+V[b])/2)
    for f in poly.faces: candidates.append(V[f].mean(axis=0))
    for c in candidates:
        L=np.linalg.norm(c)
        if L<1e-7: continue
        u=c/L
        if not any(abs(abs(np.dot(u,e))-1)<1e-5 for e in axes): axes.append(u)
        if len(axes)>=max_axes: break
    mats=[np.eye(3)]; axis_counts={}
    for u in axes:
        best=0
        # 2..6 covers classical Platonic/Archimedean and common prism/antiprism axes.
        for k in (2,3,4,5,6):
            if _maps_vertex_set(V,_rot_matrix(u,2*math.pi/k),tol): best=k
        if best>=2:
            axis_counts[best]=axis_counts.get(best,0)+1
            for m in range(1,best): mats.append(_rot_matrix(u,2*math.pi*m/best))
    uniq=[]
    for R in mats:
        if not any(np.allclose(R,Q,atol=1e-3) for Q in uniq): uniq.append(R)
    return V, uniq, axis_counts

def _orbits_from_permutations(n, perms):
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]; x=parent[x]
        return x
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb: parent[rb]=ra
    for perm in perms:
        for i,j in enumerate(perm): union(i,j)
    groups=defaultdict(list)
    for i in range(n): groups[find(i)].append(i)
    return sorted([sorted(v) for v in groups.values()], key=lambda g:(len(g),g[0]))

def _edge_orbits_from_perms(poly, perms):
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
    idx_orbits=_orbits_from_permutations(len(edge_sets), edge_perms) if edge_sets and edge_perms else [[i] for i in range(len(edge_sets))]
    return [[edge_sets[i] for i in orb] for orb in idx_orbits]

def _face_orbits_from_perms(poly, perms):
    face_keys=[tuple(sorted(f)) for f in poly.faces]; face_index={k:i for i,k in enumerate(face_keys)}
    face_perms=[]
    for p in perms:
        fp=[]; ok=True
        for f in poly.faces:
            key=tuple(sorted(p[i] for i in f))
            if key not in face_index: ok=False; break
            fp.append(face_index[key])
        if ok: face_perms.append(fp)
    return _orbits_from_permutations(len(face_keys), face_perms) if face_keys and face_perms else [[i] for i in range(len(face_keys))]

def _stabilizers(group_order, orbits):
    out=[]
    for orb in orbits:
        out.append(float(group_order)/max(1,len(orb)))
    return out

def _round_sig(x, nd=6):
    try: return round(float(x), nd)
    except Exception: return x

def _vertex_signature(poly, vi):
    incident_faces=[fi for fi,f in enumerate(poly.faces) if vi in f]
    face_sides=sorted(len(poly.faces[fi]) for fi in incident_faces)
    incident_edges=[]
    for a,b in poly.edges():
        if a==vi or b==vi: incident_edges.append(float(np.linalg.norm(poly.vertices[a]-poly.vertices[b])))
    if incident_edges:
        emin,emax=min(incident_edges),max(incident_edges); edisp=(emax-emin)/max(emin,EPS)
    else: edisp=0.0
    return {'valence':len(incident_edges),'face_sides':face_sides,'edge_dispersion':_round_sig(edisp,8)}

def _edge_signature(poly, edge):
    a,b=edge; e2f=poly.edge_to_faces(); fs=e2f.get(tuple(sorted(edge)),[])
    L=float(np.linalg.norm(poly.vertices[a]-poly.vertices[b]))
    return {'length':_round_sig(L,8),'adjacent_face_sides':sorted(len(poly.faces[fi]) for fi in fs)}

def _face_signature(poly, fi):
    f=poly.faces[fi]
    return {'sides':len(f),'area':_round_sig(poly.face_area(f),8)}

def _orbit_signature_table(poly, kind, orbits):
    rows=[]
    for oi,orb in enumerate(orbits,1):
        if kind=='vertex':
            sigs=[_vertex_signature(poly,i) for i in orb]
        elif kind=='edge':
            sigs=[_edge_signature(poly,e) for e in orb]
        else:
            sigs=[_face_signature(poly,i) for i in orb]
        counter=Counter(json.dumps(s,sort_keys=True) for s in sigs)
        rows.append({'orbit':oi,'size':len(orb),'signature_types':len(counter),'signature_preview':json.loads(counter.most_common(1)[0][0]) if counter else {},'sample':orb[:10]})
    return rows

def detect_symmetry_v24(poly, tol=1e-4):
    """Backward-compatible wrapper for the advanced v24.2 report."""
    return detect_symmetry_v242(poly, tol)

def detect_symmetry_v242(poly, tol=1e-4):
    try:
        V,mats,axis_counts=_rotation_group_matrices(poly,tol)
        perms=[]; residuals=[]
        for R in mats:
            W=V@R.T
            p=_nearest_permutation(V,W,tol)
            if p is not None:
                perms.append(p); residuals.append(_permutation_residual(V,W,p))
        vertex_orbits=_orbits_from_permutations(len(poly.vertices), perms) if perms else [[i] for i in range(len(poly.vertices))]
        edge_orbits=_edge_orbits_from_perms(poly, perms)
        face_orbits=_face_orbits_from_perms(poly, perms)
        vtrans=(len(vertex_orbits)==1 and len(poly.vertices)>0)
        etrans=(len(edge_orbits)==1 and len(poly.edges())>0)
        ftrans=(len(face_orbits)==1 and len(poly.faces)>0)
        has_inv=_nearest_permutation(V,-V,tol) is not None
        order=len(mats)
        group=_classify_symmetry(order,axis_counts,vtrans,etrans,ftrans)
        return SymmetryReportV242(
            rotation_order=order,
            axis_counts=dict(sorted(axis_counts.items())),
            group=group,
            has_inversion=bool(has_inv),
            vertex_orbits=vertex_orbits,
            edge_orbits=edge_orbits,
            face_orbits=face_orbits,
            vertex_transitive=vtrans,
            edge_transitive=etrans,
            face_transitive=ftrans,
            vertex_stabilizers=_stabilizers(order,vertex_orbits),
            edge_stabilizers=_stabilizers(order,edge_orbits),
            face_stabilizers=_stabilizers(order,face_orbits),
            max_mapping_error=float(max(residuals) if residuals else 0.0),
            mean_mapping_error=float(sum(residuals)/len(residuals) if residuals else 0.0),
        )
    except Exception as exc:
        return SymmetryReportV242(1,{},'Erro/indeterminado',False,[[i] for i in range(len(poly.vertices))],[[e] for e in poly.edges()],[[i] for i in range(len(poly.faces))],warning=f'Falha na análise: {exc}')

def symmetry_report_advanced_dict(poly, tol=1e-4):
    rep=detect_symmetry_v242(poly,tol)
    return {
        'summary': rep.as_dict(),
        'vertex_orbit_table': _orbit_signature_table(poly,'vertex',rep.vertex_orbits),
        'edge_orbit_table': _orbit_signature_table(poly,'edge',rep.edge_orbits),
        'face_orbit_table': _orbit_signature_table(poly,'face',rep.face_orbits),
        'interpretation': {
            'vertex_transitive_hint': rep.vertex_transitive,
            'edge_transitive_hint': rep.edge_transitive,
            'face_transitive_hint': rep.face_transitive,
            'regular_hint': bool(rep.vertex_transitive and rep.edge_transitive and rep.face_transitive),
            'archimedean_hint': bool(rep.vertex_transitive and poly.meta.status in ('canonical','procedural') and len(set(len(f) for f in poly.faces))>=1),
            'catalan_hint': bool(rep.face_transitive and 'Catalan' in poly.family),
        }
    }

def _format_orbit_rows(title, rows, stabilizers=None):
    lines=[title,'-'*len(title)]
    for i,row in enumerate(rows[:20]):
        stab='' if stabilizers is None or i>=len(stabilizers) else f', estabilizador≈{stabilizers[i]:.3g}'
        lines.append(f"Órbita {row['orbit']:02d}: tamanho={row['size']}{stab}, tipos_de_assinatura={row['signature_types']}, assinatura={row['signature_preview']}, amostra={row['sample']}")
    if len(rows)>20: lines.append(f'... {len(rows)-20} órbitas adicionais omitidas na prévia.')
    return lines

def symmetry_report_text(poly):
    rep=detect_symmetry_v242(poly)
    data=symmetry_report_advanced_dict(poly)
    vsizes=Counter(len(o) for o in rep.vertex_orbits)
    esizes=Counter(len(o) for o in rep.edge_orbits)
    fsizes=Counter(len(o) for o in rep.face_orbits)
    interp=data['interpretation']
    lines=[
        f'Simetria avançada — {poly.name}',
        '='*72,
        f'Família: {poly.family}',
        f'Status geométrico: {poly.meta.status}',
        '',
        'Grupo rotacional aproximado',
        '-'*31,
        f'Classificação sugerida: {rep.group}',
        f'Ordem rotacional aproximada: {rep.rotation_order}',
        f'Eixos por ordem: {rep.axis_counts}',
        f'Inversão central: {"sim" if rep.has_inversion else "não"}',
        f'Erro máximo de mapeamento vértice→vértice: {rep.max_mapping_error:.3e}',
        f'Erro médio de mapeamento vértice→vértice: {rep.mean_mapping_error:.3e}',
        '',
        'Transitividade por órbitas',
        '-'*27,
        f'Vértice-transitivo: {"sim" if rep.vertex_transitive else "não"} | órbitas={len(rep.vertex_orbits)} | tamanhos={dict(sorted(vsizes.items()))}',
        f'Aresta-transitivo: {"sim" if rep.edge_transitive else "não"} | órbitas={len(rep.edge_orbits)} | tamanhos={dict(sorted(esizes.items()))}',
        f'Face-transitivo: {"sim" if rep.face_transitive else "não"} | órbitas={len(rep.face_orbits)} | tamanhos={dict(sorted(fsizes.items()))}',
        '',
        'Leituras sugeridas',
        '-'*19,
        f'Indício de regularidade global (V/E/F transitive): {"sim" if interp["regular_hint"] else "não"}',
        f'Indício de comportamento arquimediano: {"sim" if interp["archimedean_hint"] else "não"}',
        f'Indício de comportamento Catalan/dual: {"sim" if interp["catalan_hint"] else "não"}',
        '',
        rep.warning,
        ''
    ]
    lines.extend(_format_orbit_rows('Órbitas de vértices com assinaturas locais', data['vertex_orbit_table'], rep.vertex_stabilizers)); lines.append('')
    lines.extend(_format_orbit_rows('Órbitas de arestas com assinaturas locais', data['edge_orbit_table'], rep.edge_stabilizers)); lines.append('')
    lines.extend(_format_orbit_rows('Órbitas de faces com assinaturas locais', data['face_orbit_table'], rep.face_stabilizers)); lines.append('')
    lines.append('Payload JSON resumido')
    lines.append('-'*21)
    lines.append(json.dumps(data,ensure_ascii=False,indent=2,default=str)[:10000])
    return '\n'.join(lines)
# ============================================================
# v24.2 — SOTA FUSION: CANONICAL FORM LAB
# ============================================================
def midsphere_defect(poly):
    V=poly.vertices-np.mean(poly.vertices,axis=0)
    dists=[]
    for a,b in poly.edges():
        pa,pb=V[a],V[b]; d=pb-pa; den=float(np.dot(d,d)) or 1.0
        t=max(0.0,min(1.0,-float(np.dot(pa,d))/den)); dists.append(float(np.linalg.norm(pa+t*d)))
    if not dists: return 0.0
    arr=np.array(dists); mean=float(arr.mean()) or 1.0
    return float(np.max(np.abs(arr-mean))/mean)

def _planarize_vertices(V,faces,rate):
    new=V.copy()
    for f in faces:
        pts=V[f]; c=pts.mean(axis=0)
        try:
            _,_,vt=np.linalg.svd(pts-c); n=vt[-1]
        except Exception:
            continue
        for idx in f:
            d=float(np.dot(V[idx]-c,n)); new[idx]-=rate*d*n
    return new

def _tangentify_vertices(V,edges,rate):
    new=V.copy(); origin=V.mean(axis=0)
    for a,b in edges:
        pa,pb=V[a]-origin,V[b]-origin; d=pb-pa; den=float(np.dot(d,d)) or 1.0
        t=max(0.0,min(1.0,-float(np.dot(pa,d))/den)); near=pa+t*d; dist=float(np.linalg.norm(near))
        if dist<EPS: continue
        corr=(1.0-dist)*near/dist
        new[a]+=rate*0.5*corr; new[b]+=rate*0.5*corr
    return new

def canonical_form_v24(poly,iterations=120,rate=0.25):
    V=poly.vertices.astype(float).copy(); V-=V.mean(axis=0)
    r=float(np.max(np.linalg.norm(V,axis=1))) if len(V) else 1.0
    if r>EPS: V/=r
    edges=poly.edges()
    hist=[]
    tmp=Polyhedron(V,poly.faces,poly.name,poly.family,poly.note,poly.meta)
    hist.append(midsphere_defect(tmp))
    for k in range(int(iterations)):
        V=_planarize_vertices(V,poly.faces,float(rate))
        V=_tangentify_vertices(V,edges,float(rate))
        V-=V.mean(axis=0)
        if (k+1) in {1,5,10,25,50,100,iterations}:
            tmp=Polyhedron(V,poly.faces,poly.name,poly.family,poly.note,poly.meta); hist.append(midsphere_defect(tmp))
    meta=GeometryMeta(status='procedural_canonical_lab',source='Canonicalização didática v24.0 por planarização + midsphere',warning='Resultado experimental; não substitui o canonical do Antiprism.',tags=['canonical_lab'])
    out=Polyhedron(V,poly.faces,poly.name+' — forma canônica experimental',poly.family,poly.note,meta)
    out.canonical_history=hist
    return out

def canonical_lab_report(poly,iterations=120,rate=0.25):
    before=midsphere_defect(poly)
    before_reg=polyhedral_regularity_analysis(poly)
    can=canonical_form_v24(poly,iterations,rate)
    after=midsphere_defect(can)
    after_reg=polyhedral_regularity_analysis(can)
    lines=[f'Canonical Lab — {poly.name}','='*70,'Método: planarização de faces + ajuste iterativo de tangência das arestas a uma midsphere.','Aviso: laboratório didático/experimental; não é equivalente completo ao Antiprism canonical.','',f'Iterações: {iterations}',f'Taxa: {rate:.3f}','',f'Defeito de midsphere antes: {before:.6e}',f'Defeito de midsphere depois: {after:.6e}',f'Melhoria relativa: {((before-after)/before*100) if before>0 else 0:.3f}%','',f'Dispersão relativa de arestas antes: {before_reg.get("edge_relative_dispersion")}',f'Dispersão relativa de arestas depois: {after_reg.get("edge_relative_dispersion")}',f'Histórico parcial do defeito: {getattr(can,"canonical_history",[])}']
    return '\n'.join(lines), can

# ============================================================
# v24.2 — TESTES ADICIONAIS SOTA
# ============================================================
def run_v24_sota_self_tests():
    tests=[]
    def add(name,ok,detail=''):
        tests.append((f'v24 SOTA / {name}',bool(ok),detail))
    # Robust predicates
    add('orient2d robusto colinear', robust_orient2d((0,0),(1,1),(2,2))==0)
    add('orient2d robusto anti-horário', robust_orient2d((0,0),(1,0),(0,1))==1)
    add('orient3d existe', robust_orient3d((0,0,0),(1,0,0),(0,1,0),(0,0,1))!=0)
    # Half-edge on cube / tetra
    for key in ['Platônicos / Cubo ou Hexaedro','Platônicos / Tetraedro']:
        p=CATALOG[key].build(); he=halfedge_mesh(p); V,E,F,chi=he.euler()
        add(f'half-edge Euler {p.name}', (V,E,F,chi)==(p.euler().V,p.euler().E,p.euler().F,p.euler().chi))
        add(f'half-edge fechado/manifold {p.name}', he.is_closed() and he.is_manifold())
    # Symmetry expected minimal orders
    expected=[('Platônicos / Tetraedro',12),('Platônicos / Cubo ou Hexaedro',24),('Platônicos / Icosaedro',60)]
    for key,order in expected:
        p=CATALOG[key].build(); rep=detect_symmetry_v24(p)
        add(f'simetria ordem mínima {p.name}', rep.rotation_order>=order, rep.as_dict())
        add(f'simetria uma órbita vértices {p.name}', len(rep.vertex_orbits)==1, rep.vertex_orbits)
    # Canonical lab sanity
    p=CATALOG['Platônicos / Cubo ou Hexaedro'].build(); txt,can=canonical_lab_report(p,20,0.15)
    add('canonical lab retorna Polyhedron', isinstance(can,Polyhedron))
    add('canonical lab mantém Euler', can.euler().chi==p.euler().chi)
    add('canonical lab relatório', 'Defeito de midsphere' in txt)
    # Advanced symmetry/orbit report v24.2
    cube=CATALOG['Platônicos / Cubo ou Hexaedro'].build(); rep=detect_symmetry_v242(cube); data=symmetry_report_advanced_dict(cube)
    add('simetria avançada cubo V/E/F transitivo', rep.vertex_transitive and rep.edge_transitive and rep.face_transitive, rep.as_dict())
    add('simetria avançada cubo uma órbita de arestas', len(rep.edge_orbits)==1, rep.edge_orbits)
    add('simetria avançada cubo uma órbita de faces', len(rep.face_orbits)==1, rep.face_orbits)
    add('simetria avançada gera tabelas de órbitas', bool(data['vertex_orbit_table']) and bool(data['edge_orbit_table']) and bool(data['face_orbit_table']))
    tet=CATALOG['Platônicos / Tetraedro'].build(); r2=detect_symmetry_v242(tet)
    add('simetria avançada tetraedro ordem 12', r2.rotation_order>=12, r2.as_dict())
    add('simetria avançada tetraedro regular hint', symmetry_report_advanced_dict(tet)['interpretation']['regular_hint'])
    return tests

# ============================================================
# v24.2 — UI: ABAS SIMETRIA E CANONICAL LAB
# ============================================================
class GeoPolyAppV240(GeoPolyAppV2322):
    def _build_ui(self):
        super()._build_ui()
        self.tabsymmetry=ttk.Frame(self.nb,padding=6)
        self.tabcanonical=ttk.Frame(self.nb,padding=6)
        self.nb.add(self.tabsymmetry,text='Simetria')
        self.nb.add(self.tabcanonical,text='Canonical Lab')
        self._build_symmetry_tab()
        self._build_canonical_tab()
    def _build_symmetry_tab(self):
        self.tabsymmetry.rowconfigure(1,weight=1); self.tabsymmetry.columnconfigure(0,weight=1)
        bar=ttk.LabelFrame(self.tabsymmetry,text='Análise de simetria avançada v24.2',padding=8); bar.grid(row=0,column=0,sticky='ew',pady=(0,6))
        ttk.Button(bar,text='Atualizar simetria',command=self.update_symmetry_tab).pack(side='left',padx=4)
        ttk.Label(bar,text='Mede rotações, órbitas, estabilizadores e assinaturas locais de vértices/arestas/faces.').pack(side='left',padx=8)
        self.symmetry_text=tk.Text(self.tabsymmetry,wrap='word',font=('Consolas',10)); self.symmetry_text.grid(row=1,column=0,sticky='nsew')
    def _build_canonical_tab(self):
        self.tabcanonical.rowconfigure(1,weight=1); self.tabcanonical.columnconfigure(0,weight=1)
        bar=ttk.LabelFrame(self.tabcanonical,text='Canonical Lab experimental',padding=8); bar.grid(row=0,column=0,sticky='ew',pady=(0,6))
        self.canon_iter_var=tk.IntVar(value=120); self.canon_rate_var=tk.DoubleVar(value=0.25)
        ttk.Label(bar,text='Iterações').pack(side='left'); ttk.Spinbox(bar,from_=5,to=1000,increment=5,textvariable=self.canon_iter_var,width=8).pack(side='left',padx=4)
        ttk.Label(bar,text='Taxa').pack(side='left'); ttk.Spinbox(bar,from_=0.01,to=1.0,increment=0.05,textvariable=self.canon_rate_var,width=8).pack(side='left',padx=4)
        ttk.Button(bar,text='Rodar canonicalização',command=self.update_canonical_tab).pack(side='left',padx=8)
        self.canonical_text=tk.Text(self.tabcanonical,wrap='word',font=('Consolas',10)); self.canonical_text.grid(row=1,column=0,sticky='nsew')
    def update_all(self):
        super().update_all()
        if hasattr(self,'symmetry_text'): self.update_symmetry_tab()
        if hasattr(self,'canonical_text'): self.canonical_text.delete('1.0','end'); self.canonical_text.insert('end','Clique em "Rodar canonicalização" para gerar a forma canônica experimental do sólido atual.')
    def update_symmetry_tab(self):
        if not self.poly or not hasattr(self,'symmetry_text'): return
        self.symmetry_text.delete('1.0','end')
        self.symmetry_text.insert('end',symmetry_report_text(self.poly))
        self.symmetry_text.insert('end','\n\nHalf-edge / DCEL\n'+'-'*40+'\n')
        he=halfedge_mesh(self.poly); V,E,F,chi=he.euler()
        self.symmetry_text.insert('end',f'V={V}, E={E}, F={F}, χ={chi}\nFechada: {he.is_closed()}\nManifold: {he.is_manifold()}\nGênero estimado: {he.genus_hint()}\n')
    def update_canonical_tab(self):
        if not self.poly or not hasattr(self,'canonical_text'): return
        self.canonical_text.delete('1.0','end')
        try:
            txt,can=canonical_lab_report(self.poly,self.canon_iter_var.get(),self.canon_rate_var.get())
            self.canonical_text.insert('end',txt)
            self.canonical_text.insert('end','\n\nObservação: a forma canônica é calculada em memória para análise. A malha original selecionada no app não é substituída automaticamente.')
        except Exception as exc:
            self.canonical_text.insert('end','Erro no Canonical Lab:\n'+str(exc))

def main():
    GeoPolyAppV240().mainloop()

# main() is redefined at the end by v25.0.


# v27.2f: explicit export list so internal star imports preserve historical
# single-underscore helper symbols without using wholesale update calls.
__all__ = [k for k in globals() if not k.startswith('__')]
