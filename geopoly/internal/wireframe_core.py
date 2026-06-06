"""GeoPoly v27 internal module: Wireframe kit core and visual controls."""
# v27.2f: named internal dependency import.
# Wildcard imports were removed to improve static analysis.
# v27.2f: named internal dependency imports; no wildcard imports.
from .sota_topology_symmetry import (
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
    run_v24_sota_self_tests, GeoPolyAppV240, main,
)


# ============================================================
# v25.0 — WIREFRAME KIT LAB SEM OPENSCAD
# ============================================================
# Primeira versão totalmente em Python. Gera malhas STL trianguladas para
# hastes, juntas simplificadas e wireframe completo. Não usa booleanas nem
# OpenSCAD. As juntas desta edição são peças simplificadas: núcleo esférico
# facetado + pinos cilíndricos sobrepostos. Para uso mecânico final, validar
# no fatiador e fazer teste de tolerância.

@dataclass
class WireframeParams:
    edge_scale_mm: float = 50.0
    rod_radius_mm: float = 2.0
    pin_radius_mm: float = 1.65
    clearance_mm: float = 0.25
    pin_length_mm: float = 8.0
    joint_radius_mm: float = 5.5
    cyl_segments: int = 24
    sphere_segments: int = 16
    length_tol_mm: float = 0.20
    angle_round_deg: float = 1.0


def _wf_norm(v):
    v=np.array(v,dtype=float); L=float(np.linalg.norm(v)); return v/L if L>EPS else v


def _wf_basis_from_dir(direction):
    w=_wf_norm(direction)
    if np.linalg.norm(w)<EPS: w=np.array([1.0,0,0])
    ref=np.array([0.0,0.0,1.0]) if abs(np.dot(w,[0,0,1]))<0.92 else np.array([0.0,1.0,0.0])
    u=np.cross(w,ref); u=_wf_norm(u)
    v=np.cross(w,u); v=_wf_norm(v)
    return u,v,w


def mesh_cylinder_between(p0,p1,radius=1.0,segments=24,caps=True):
    p0=np.array(p0,dtype=float); p1=np.array(p1,dtype=float); r=float(radius); n=max(8,int(segments))
    axis=p1-p0; L=float(np.linalg.norm(axis))
    if L<EPS: return [],[]
    u,v,w=_wf_basis_from_dir(axis)
    verts=[]
    for base in [p0,p1]:
        for k in range(n):
            a=2*math.pi*k/n
            verts.append((base + r*(math.cos(a)*u + math.sin(a)*v)).tolist())
    faces=[]
    for k in range(n):
        j=(k+1)%n
        faces.append([k,j,n+j]); faces.append([k,n+j,n+k])
    if caps:
        c0=len(verts); verts.append(p0.tolist())
        c1=len(verts); verts.append(p1.tolist())
        for k in range(n):
            j=(k+1)%n
            faces.append([c0,j,k])
            faces.append([c1,n+k,n+j])
    return verts,faces


def mesh_tube_along_x(length, outer_radius, inner_radius, segments=24):
    L=max(float(length), EPS); ro=float(outer_radius); ri=max(float(inner_radius), EPS); n=max(8,int(segments))
    if ri>=ro: ri=0.8*ro
    verts=[]
    for x in [0.0,L]:
        for rad in [ro,ri]:
            for k in range(n):
                a=2*math.pi*k/n; verts.append([x,rad*math.cos(a),rad*math.sin(a)])
    # indices: left outer 0..n-1, left inner n..2n-1, right outer 2n..3n-1, right inner 3n..4n-1
    lo=0; li=n; roff=2*n; ri2=3*n
    faces=[]
    for k in range(n):
        j=(k+1)%n
        # outer wall
        faces.append([lo+k,lo+j,roff+j]); faces.append([lo+k,roff+j,roff+k])
        # inner wall reversed
        faces.append([li+k,ri2+j,li+j]); faces.append([li+k,ri2+k,ri2+j])
        # left annulus
        faces.append([lo+k,li+j,lo+j]); faces.append([lo+k,li+k,li+j])
        # right annulus
        faces.append([roff+k,roff+j,ri2+j]); faces.append([roff+k,ri2+j,ri2+k])
    return verts,faces


def mesh_uv_sphere(center=(0,0,0), radius=1.0, segments=16, rings=None):
    center=np.array(center,dtype=float); seg=max(8,int(segments)); rings=max(4,int(rings or segments//2))
    verts=[]
    # poles and rings without degeneracy
    verts.append((center+np.array([0,0,radius])).tolist())
    for i in range(1,rings):
        phi=math.pi*i/rings
        z=radius*math.cos(phi); rr=radius*math.sin(phi)
        for k in range(seg):
            a=2*math.pi*k/seg
            verts.append((center+np.array([rr*math.cos(a), rr*math.sin(a), z])).tolist())
    bottom=len(verts); verts.append((center+np.array([0,0,-radius])).tolist())
    faces=[]
    # top cap
    first=1
    for k in range(seg): faces.append([0, first+k, first+(k+1)%seg])
    # middle
    for i in range(rings-2):
        a0=1+i*seg; a1=1+(i+1)*seg
        for k in range(seg):
            j=(k+1)%seg
            faces.append([a0+k,a1+k,a1+j]); faces.append([a0+k,a1+j,a0+j])
    # bottom cap
    last=1+(rings-2)*seg if rings>=2 else 1
    for k in range(seg): faces.append([bottom, last+(k+1)%seg, last+k])
    return verts,faces


def combine_meshes(meshes):
    verts=[]; faces=[]
    for v,f in meshes:
        off=len(verts); verts.extend([list(map(float,p)) for p in v]); faces.extend([[int(i)+off for i in face] for face in f])
    return verts,faces


def transform_mesh(vertices, faces, R=None, t=None):
    R=np.array(R if R is not None else np.eye(3),dtype=float); t=np.array(t if t is not None else np.zeros(3),dtype=float)
    return [(R@np.array(p,dtype=float)+t).tolist() for p in vertices], [list(face) for face in faces]


def _rotation_from_x_to_dir(direction):
    u,v,w=_wf_basis_from_dir(direction)
    # local X maps to w, local Y maps to u, local Z maps to v
    return np.column_stack([w,u,v])


def write_mesh_stl_ascii(vertices, faces, path, solid_name='wireframe_mesh'):
    path=Path(path)
    verts=np.array(vertices,dtype=float)
    with open(path,'w',encoding='utf-8') as f:
        f.write(f'solid {safe_name(solid_name)}\n')
        for face in faces:
            if len(face)<3: continue
            for i in range(1,len(face)-1):
                tri=[face[0],face[i],face[i+1]]
                p0,p1,p2=verts[tri]
                n=np.cross(p1-p0,p2-p0); L=np.linalg.norm(n); n=n/L if L>EPS else np.array([0.0,0.0,0.0])
                f.write(f'  facet normal {n[0]:.8e} {n[1]:.8e} {n[2]:.8e}\n')
                f.write('    outer loop\n')
                for p in [p0,p1,p2]: f.write(f'      vertex {p[0]:.8e} {p[1]:.8e} {p[2]:.8e}\n')
                f.write('    endloop\n  endfacet\n')
        f.write(f'endsolid {safe_name(solid_name)}\n')


def _poly_neighbors(poly):
    adj=defaultdict(set)
    for a,b in poly.edges(): adj[a].add(b); adj[b].add(a)
    return {k:sorted(v) for k,v in adj.items()}


def wireframe_edge_groups(poly, params:WireframeParams):
    groups=[]
    for a,b in poly.edges():
        L=float(np.linalg.norm(poly.vertices[b]-poly.vertices[a])*params.edge_scale_mm)
        placed=False
        for g in groups:
            if abs(g['length_mm']-L)<=params.length_tol_mm:
                g['edges'].append((a,b)); g['count']+=1; g['lengths_mm'].append(L); placed=True; break
        if not placed:
            groups.append({'type':f'H{len(groups)+1}', 'length_mm':L, 'lengths_mm':[L], 'edges':[(a,b)], 'count':1})
    for g in groups:
        mean=float(np.mean(g['lengths_mm'])); g['length_mm']=mean
        g['min_mm']=float(min(g['lengths_mm'])); g['max_mm']=float(max(g['lengths_mm']))
        g['rod_body_length_mm']=max(0.5, mean-2*params.pin_length_mm)
        g['tube_inner_radius_mm']=params.pin_radius_mm+params.clearance_mm
        g['tube_outer_radius_mm']=params.rod_radius_mm
    return groups


def _joint_angles_for_dirs(dirs, round_deg=1.0):
    ang=[]
    for i in range(len(dirs)):
        for j in range(i+1,len(dirs)):
            c=float(np.clip(np.dot(dirs[i],dirs[j]),-1,1)); a=math.degrees(math.acos(c))
            if round_deg>0: a=round(a/round_deg)*round_deg
            ang.append(round(a,3))
    return tuple(sorted(ang))


def wireframe_joint_groups(poly, params:WireframeParams):
    adj=_poly_neighbors(poly); groups=[]; mp={}
    for vi in sorted(adj):
        dirs=[]
        for nb in adj[vi]: dirs.append(_wf_norm(poly.vertices[nb]-poly.vertices[vi]))
        sig=(len(dirs), _joint_angles_for_dirs(dirs, params.angle_round_deg))
        key=json.dumps(sig)
        if key not in mp:
            mp[key]=len(groups)
            groups.append({'type':f'J{len(groups)+1}', 'signature':sig, 'valence':len(dirs), 'vertices':[], 'count':0, 'representative_vertex':vi, 'directions':dirs})
        g=groups[mp[key]]; g['vertices'].append(vi); g['count']+=1
    return groups


def wireframe_manifest(poly, params:WireframeParams):
    edges=wireframe_edge_groups(poly,params); joints=wireframe_joint_groups(poly,params)
    warnings=[]
    if params.pin_radius_mm+params.clearance_mm>=params.rod_radius_mm:
        warnings.append('Raio interno da haste tubular >= raio externo; o modelo ajustará internamente, mas os parâmetros são mecanicamente inconsistentes.')
    for g in edges:
        if g['rod_body_length_mm']<=1.0: warnings.append(f'{g["type"]}: comprimento útil da haste muito curto para a profundidade de encaixe configurada.')
    manifest={
        'app':APP_NAME, 'version':VERSION, 'edition':'Wireframe Kit Lab sem OpenSCAD',
        'solid':poly.name, 'family':poly.family, 'geometry_status':getattr(poly.meta,'status','unknown'),
        'parameters':asdict(params),
        'counts':{'vertices':len(poly.vertices),'edges':len(poly.edges()),'faces':len(poly.faces),'rod_types':len(edges),'joint_types':len(joints)},
        'rod_groups':[{k:v for k,v in g.items() if k not in ('edges','lengths_mm')} for g in edges],
        'joint_groups':[{k:(v if k!='directions' else [np.array(d).round(6).tolist() for d in v]) for k,v in g.items() if k!='vertices'} | {'vertices':g['vertices']} for g in joints],
        'warnings':warnings,
        'notes':['Primeira versão sem OpenSCAD/CadQuery.', 'Juntas são malhas simplificadas: núcleo esférico facetado + pinos cilíndricos sobrepostos.', 'Validar tolerâncias no fatiador e imprimir peças de teste antes do kit completo.']
    }
    return manifest


def wireframe_report(poly, params:WireframeParams):
    m=wireframe_manifest(poly,params)
    lines=[]
    lines.append(f'Wireframe Kit Lab — {poly.name}')
    lines.append('='*max(30,len(lines[0])))
    lines.append(f'Família: {poly.family}')
    lines.append(f'Status geométrico: {m["geometry_status"]}')
    lines.append('')
    lines.append('Parâmetros maker')
    lines.append('-'*40)
    for k,v in m['parameters'].items(): lines.append(f'{k}: {v}')
    lines.append('')
    lines.append('Hastes por comprimento')
    lines.append('-'*40)
    for g in m['rod_groups']:
        lines.append(f'{g["type"]}: {g["count"]} unidade(s); aresta={g["length_mm"]:.3f} mm; corpo tubular={g["rod_body_length_mm"]:.3f} mm; raio externo={g["tube_outer_radius_mm"]:.3f} mm; raio interno≈{g["tube_inner_radius_mm"]:.3f} mm')
    lines.append('')
    lines.append('Juntas por assinatura angular')
    lines.append('-'*40)
    for g in m['joint_groups']:
        sig=g['signature']; angles=sig[1]
        preview=', '.join(f'{a:g}°' for a in angles[:12]) + (' ...' if len(angles)>12 else '')
        lines.append(f'{g["type"]}: {g["count"]} unidade(s); valência={g["valence"]}; representante=V{g["representative_vertex"]}; ângulos={preview}')
    if m['warnings']:
        lines.append(''); lines.append('Avisos'); lines.append('-'*40)
        lines.extend('- '+w for w in m['warnings'])
    lines.append('')
    lines.append('Orientação de impressão sugerida')
    lines.append('-'*40)
    lines.append('Hastes: imprimir deitadas no leito para favorecer resistência ao longo do comprimento.')
    lines.append('Juntas: validar suporte/aderência; esta versão simplificada não otimiza orientação automaticamente.')
    lines.append('')
    lines.append('Observação de escopo')
    lines.append('-'*40)
    lines.append('Sem booleanas complexas: as peças STL são malhas trianguladas diretas. Juntas com furos fêmea reais ficam para versão CadQuery/opcional futura.')
    return '\n'.join(lines)


def mesh_wireframe_full(poly, params:WireframeParams):
    V=poly.vertices*params.edge_scale_mm
    meshes=[]
    # rods as cylinders clipped short near joints
    for a,b in poly.edges():
        p0=V[a]; p1=V[b]; d=p1-p0; L=np.linalg.norm(d)
        if L<EPS: continue
        u=d/L; q0=p0+u*params.joint_radius_mm*0.75; q1=p1-u*params.joint_radius_mm*0.75
        if np.linalg.norm(q1-q0)>EPS: meshes.append(mesh_cylinder_between(q0,q1,params.rod_radius_mm,params.cyl_segments,True))
    for p in V: meshes.append(mesh_uv_sphere(p,params.joint_radius_mm,params.sphere_segments))
    return combine_meshes(meshes)


def mesh_rod_type(length_mm, params:WireframeParams):
    # tubular rod along X with inner radius for male pins
    return mesh_tube_along_x(length_mm, params.rod_radius_mm, params.pin_radius_mm+params.clearance_mm, params.cyl_segments)


def mesh_joint_type(directions, params:WireframeParams):
    meshes=[mesh_uv_sphere((0,0,0),params.joint_radius_mm,params.sphere_segments)]
    for d in directions:
        d=_wf_norm(d)
        p0=d*(params.joint_radius_mm*0.35); p1=d*(params.joint_radius_mm+params.pin_length_mm)
        meshes.append(mesh_cylinder_between(p0,p1,params.pin_radius_mm,params.cyl_segments,True))
    return combine_meshes(meshes)


def mesh_rod_groups_display(poly, params:WireframeParams):
    meshes=[]; y=0.0
    for g in wireframe_edge_groups(poly,params):
        v,f=mesh_rod_type(g['rod_body_length_mm'],params)
        v2,f2=transform_mesh(v,f,t=[0,y,0]); meshes.append((v2,f2)); y+=4*params.rod_radius_mm+6
    return combine_meshes(meshes)


def mesh_joint_groups_display(poly, params:WireframeParams):
    meshes=[]; x=0.0
    for g in wireframe_joint_groups(poly,params):
        v,f=mesh_joint_type(g['directions'],params)
        v2,f2=transform_mesh(v,f,t=[x,0,0]); meshes.append((v2,f2)); x+=2*(params.joint_radius_mm+params.pin_length_mm)+8
    return combine_meshes(meshes)


def export_wireframe_kit_zip(poly, params:WireframeParams, zip_path):
    zip_path=Path(zip_path); tmp=Path(tempfile.mkdtemp(prefix='geopoly_wireframe_'))
    base=safe_name(poly.name)
    files=[]
    try:
        # full model
        v,f=mesh_wireframe_full(poly,params); p=tmp/f'{base}_wireframe_completo.stl'; write_mesh_stl_ascii(v,f,p,base+'_wireframe'); files.append(p)
        # rods per type
        for g in wireframe_edge_groups(poly,params):
            v,f=mesh_rod_type(g['rod_body_length_mm'],params); p=tmp/f'{base}_haste_{g["type"]}_{g["count"]}x.stl'; write_mesh_stl_ascii(v,f,p,f'haste_{g["type"]}'); files.append(p)
        # joints per type
        for g in wireframe_joint_groups(poly,params):
            v,f=mesh_joint_type(g['directions'],params); p=tmp/f'{base}_junta_{g["type"]}_{g["count"]}x.stl'; write_mesh_stl_ascii(v,f,p,f'junta_{g["type"]}'); files.append(p)
        manifest=wireframe_manifest(poly,params); p=tmp/f'{base}_manifesto_wireframe.json'; p.write_text(json.dumps(manifest,indent=2,ensure_ascii=False,default=str),encoding='utf-8'); files.append(p)
        p=tmp/f'{base}_relatorio_montagem.txt'; p.write_text(wireframe_report(poly,params),encoding='utf-8'); files.append(p)
        with zipfile.ZipFile(zip_path,'w',compression=zipfile.ZIP_DEFLATED) as z:
            for file in files: z.write(file,arcname=file.name)
    finally:
        # keep simple cleanup
        for file in tmp.glob('*'):
            try: file.unlink()
            except Exception: pass
        try: tmp.rmdir()
        except Exception: pass
    return zip_path

# Preserve testes anteriores e amplia com Wireframe Lab.
_RUN_SELF_TESTS_V242 = run_self_tests

def run_self_tests():
    base=_RUN_SELF_TESTS_V242()
    if isinstance(base, TestReport):
        results=list(base.results)
    else:
        results=[TestCaseResult(str(x.get('name','teste')), bool(x.get('ok',False)), str(x.get('detail',''))) for x in base]
    def add(name,ok,detail=''):
        results.append(TestCaseResult(str(name), bool(ok), '' if ok else str(detail)))
    try:
        cube=CATALOG['Platônicos / Cubo ou Hexaedro'].build(); params=WireframeParams(edge_scale_mm=40.0)
        eg=wireframe_edge_groups(cube,params); jg=wireframe_joint_groups(cube,params)
        add('wireframe cubo um tipo de haste', len(eg)==1, eg)
        add('wireframe cubo um tipo de junta', len(jg)==1, jg)
        add('wireframe cubo 12 hastes', eg[0]['count']==12, eg[0])
        add('wireframe cubo 8 juntas', jg[0]['count']==8, jg[0])
        add('wireframe cubo valência 3', jg[0]['valence']==3, jg[0])
        man=wireframe_manifest(cube,params)
        add('wireframe manifesto serializável', bool(json.dumps(man,default=str)), '')
        v,f=mesh_wireframe_full(cube,params)
        add('wireframe completo tem vértices/faces', len(v)>0 and len(f)>0, (len(v),len(f)))
        v2,f2=mesh_rod_type(20.0,params); add('wireframe haste tubular mesh', len(v2)>0 and len(f2)>0, (len(v2),len(f2)))
        v3,f3=mesh_joint_type(jg[0]['directions'],params); add('wireframe junta mesh', len(v3)>0 and len(f3)>0, (len(v3),len(f3)))
        with tempfile.TemporaryDirectory() as td:
            z=Path(td)/'kit.zip'; export_wireframe_kit_zip(cube,params,z)
            add('wireframe zip exporta', z.exists() and z.stat().st_size>0, str(z))
            with zipfile.ZipFile(z) as zz: names=zz.namelist()
            add('wireframe zip tem manifesto', any(n.endswith('manifesto_wireframe.json') for n in names), names)
    except Exception as exc:
        add('wireframe self-test exception', False, repr(exc))
    return TestReport(results)

class GeoPolyAppV250(GeoPolyAppV240):
    def _build_ui(self):
        super()._build_ui()
        self.tabwire=ttk.Frame(self.nb,padding=6)
        self.nb.add(self.tabwire,text='Wireframe Kit')
        self._build_wireframe_tab()
    def _build_wireframe_tab(self):
        self.tabwire.rowconfigure(1,weight=1); self.tabwire.columnconfigure(0,weight=1)
        bar=ttk.LabelFrame(self.tabwire,text='Wireframe Kit Lab v25.0 — STL direto em Python, sem OpenSCAD',padding=8)
        bar.grid(row=0,column=0,sticky='ew',pady=(0,6))
        self.wf_scale=tk.DoubleVar(value=50.0); self.wf_rod=tk.DoubleVar(value=2.0); self.wf_pin=tk.DoubleVar(value=1.65)
        self.wf_clear=tk.DoubleVar(value=0.25); self.wf_pinlen=tk.DoubleVar(value=8.0); self.wf_joint=tk.DoubleVar(value=5.5); self.wf_seg=tk.IntVar(value=24)
        specs=[('Escala aresta mm/unid',self.wf_scale,1,300,1),('Raio haste',self.wf_rod,0.5,20,0.1),('Raio pino',self.wf_pin,0.3,20,0.1),('Folga',self.wf_clear,0.0,2.0,0.05),('Comp. pino',self.wf_pinlen,1,50,0.5),('Raio junta',self.wf_joint,1,50,0.5),('Segmentos',self.wf_seg,8,64,1)]
        for label,var,a,b,inc in specs:
            ttk.Label(bar,text=label).pack(side='left',padx=(4,1))
            ttk.Spinbox(bar,from_=a,to=b,increment=inc,textvariable=var,width=6).pack(side='left',padx=(0,4))
        row=ttk.Frame(self.tabwire); row.grid(row=2,column=0,sticky='ew',pady=(6,0))
        ttk.Button(row,text='Atualizar relatório',command=self.update_wireframe_tab).pack(side='left',padx=3)
        ttk.Button(row,text='Exportar wireframe completo STL',command=self.export_wireframe_full_ui).pack(side='left',padx=3)
        ttk.Button(row,text='Exportar hastes STL',command=self.export_wireframe_rods_ui).pack(side='left',padx=3)
        ttk.Button(row,text='Exportar juntas STL',command=self.export_wireframe_joints_ui).pack(side='left',padx=3)
        ttk.Button(row,text='Exportar kit ZIP',command=self.export_wireframe_zip_ui).pack(side='left',padx=3)
        self.wire_text=tk.Text(self.tabwire,wrap='word',font=('Consolas',10)); self.wire_text.grid(row=1,column=0,sticky='nsew')
    def _wf_params(self):
        return WireframeParams(edge_scale_mm=float(self.wf_scale.get()), rod_radius_mm=float(self.wf_rod.get()), pin_radius_mm=float(self.wf_pin.get()), clearance_mm=float(self.wf_clear.get()), pin_length_mm=float(self.wf_pinlen.get()), joint_radius_mm=float(self.wf_joint.get()), cyl_segments=int(self.wf_seg.get()), sphere_segments=max(8,int(self.wf_seg.get())))
    def update_all(self):
        super().update_all()
        if hasattr(self,'wire_text'): self.update_wireframe_tab()
    def update_wireframe_tab(self):
        if not self.poly or not hasattr(self,'wire_text'): return
        self.wire_text.delete('1.0','end')
        self.wire_text.insert('end',wireframe_report(self.poly,self._wf_params()))
    def _ask_wire_path(self,ext,label):
        if not self.poly: return None
        return filedialog.asksaveasfilename(title=label,defaultextension=ext,initialfile=safe_name(self.poly.name)+'_'+label.lower().replace(' ','_')+ext)
    def export_wireframe_full_ui(self):
        if not self.poly: return
        path=self._ask_wire_path('.stl','wireframe completo')
        if not path: return
        try:
            v,f=mesh_wireframe_full(self.poly,self._wf_params()); write_mesh_stl_ascii(v,f,path,self.poly.name+'_wireframe')
            messagebox.showinfo('Wireframe STL',f'Arquivo salvo:\n{path}')
        except Exception as exc: messagebox.showerror('Wireframe STL',str(exc))
    def export_wireframe_rods_ui(self):
        if not self.poly: return
        path=self._ask_wire_path('.stl','hastes')
        if not path: return
        try:
            v,f=mesh_rod_groups_display(self.poly,self._wf_params()); write_mesh_stl_ascii(v,f,path,self.poly.name+'_hastes')
            messagebox.showinfo('Hastes STL',f'Arquivo salvo:\n{path}')
        except Exception as exc: messagebox.showerror('Hastes STL',str(exc))
    def export_wireframe_joints_ui(self):
        if not self.poly: return
        path=self._ask_wire_path('.stl','juntas')
        if not path: return
        try:
            v,f=mesh_joint_groups_display(self.poly,self._wf_params()); write_mesh_stl_ascii(v,f,path,self.poly.name+'_juntas')
            messagebox.showinfo('Juntas STL',f'Arquivo salvo:\n{path}')
        except Exception as exc: messagebox.showerror('Juntas STL',str(exc))
    def export_wireframe_zip_ui(self):
        if not self.poly: return
        path=self._ask_wire_path('.zip','kit wireframe')
        if not path: return
        try:
            export_wireframe_kit_zip(self.poly,self._wf_params(),path)
            messagebox.showinfo('Kit Wireframe',f'ZIP salvo:\n{path}')
        except Exception as exc: messagebox.showerror('Kit Wireframe',str(exc))



# ============================================================
# v25.0.1 — WIREVIEW + CONTROLES DA VISUALIZAÇÃO 3D
# ============================================================
# Patch conservador sobre a v25.0 totalmente em Python:
# - adiciona controles de eixos/vértices/transparência na visualização 3D;
# - adiciona preview 3D das peças wireframe, ainda com matplotlib;
# - mantém OpenSCAD/CadQuery fora desta versão.

def _gp2501_mesh_to_collection(vertices, faces, alpha=0.78, facecolor="#dfefff", edgecolor="black", linewidth=0.35):
    verts=np.array(vertices,dtype=float)
    if len(verts)==0 or not faces:
        return None
    polys=[verts[f] for f in faces if len(f)>=3]
    if not polys:
        return None
    return Poly3DCollection(polys, alpha=float(alpha), facecolor=facecolor, edgecolor=edgecolor, linewidth=float(linewidth))

def _gp2501_autoscale_3d(ax, vertices, pad=0.08):
    verts=np.array(vertices,dtype=float)
    if len(verts)==0:
        ax.set_xlim(-1,1); ax.set_ylim(-1,1); ax.set_zlim(-1,1); return
    mn=verts.min(axis=0); mx=verts.max(axis=0); c=0.5*(mn+mx); span=float(max(mx-mn))
    if span<EPS: span=1.0
    r=0.5*span*(1.0+2.0*pad)
    ax.set_xlim(c[0]-r,c[0]+r); ax.set_ylim(c[1]-r,c[1]+r); ax.set_zlim(c[2]-r,c[2]+r)
    ax.set_box_aspect((1,1,1))

def _gp2501_plot_mesh(ax, vertices, faces, title="", alpha=0.78, show_axes=True, show_vertices=False, vertex_size=4):
    ax.clear()
    coll=_gp2501_mesh_to_collection(vertices,faces,alpha=alpha)
    if coll is not None:
        ax.add_collection3d(coll)
    verts=np.array(vertices,dtype=float)
    if show_vertices and len(verts):
        ax.scatter(verts[:,0],verts[:,1],verts[:,2],s=vertex_size)
    _gp2501_autoscale_3d(ax,verts)
    ax.set_title(title)
    if show_axes:
        ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')
    else:
        ax.set_axis_off()

class GeoPolyAppV2501(GeoPolyAppV250):
    def _build_ui(self):
        super()._build_ui()
        # Controles adicionais na aba 3D do poliedro.
        self.view_show_axes=tk.BooleanVar(value=False)
        self.view_show_vertices=tk.BooleanVar(value=True)
        self.view_alpha=tk.DoubleVar(value=0.78)
        try:
            canvas_widget=self.canvas3d.get_tk_widget()
            canvas_widget.pack_forget()
            bar=ttk.LabelFrame(self.tab3d,text='Controles de visualização 3D',padding=8)
            bar.pack(fill='x',side='top',pady=(0,4))
            ttk.Checkbutton(bar,text='Ligar eixos',variable=self.view_show_axes,command=self.update_3d).pack(side='left',padx=4)
            ttk.Checkbutton(bar,text='Mostrar vértices',variable=self.view_show_vertices,command=self.update_3d).pack(side='left',padx=4)
            ttk.Label(bar,text='Transparência das faces').pack(side='left',padx=(16,4))
            ttk.Scale(bar,from_=0.15,to=1.0,variable=self.view_alpha,orient='horizontal',command=lambda _=None:self.update_3d()).pack(side='left',fill='x',expand=True,padx=4)
            ttk.Button(bar,text='Atualizar vista',command=self.update_3d).pack(side='left',padx=4)
            canvas_widget.pack(fill='both',expand=True,side='top')
        except Exception:
            pass
    def update_3d(self):
        if not self.poly or not hasattr(self,'ax3d'):
            return
        self.ax3d.clear()
        v=np.array(self.poly.vertices,dtype=float)
        polys=[v[f] for f in self.poly.faces]
        alpha=float(getattr(self,'view_alpha',tk.DoubleVar(value=.78)).get()) if hasattr(self,'view_alpha') else .78
        show_vertices=bool(self.view_show_vertices.get()) if hasattr(self,'view_show_vertices') else True
        show_axes=bool(self.view_show_axes.get()) if hasattr(self,'view_show_axes') else True
        coll=Poly3DCollection(polys,alpha=alpha,edgecolor='k',linewidth=.6,facecolor='#dfefff')
        self.ax3d.add_collection3d(coll)
        if show_vertices:
            self.ax3d.scatter(v[:,0],v[:,1],v[:,2],s=12)
        _gp2501_autoscale_3d(self.ax3d,v)
        if show_axes:
            self.ax3d.set_xlabel('X'); self.ax3d.set_ylabel('Y'); self.ax3d.set_zlabel('Z')
        else:
            self.ax3d.set_axis_off()
        self.ax3d.set_title(f'{self.poly.name}\n{self.poly.family} | {self.poly.meta.status}')
        self.canvas3d.draw_idle()
    def _build_wireframe_tab(self):
        self.tabwire.rowconfigure(1,weight=1); self.tabwire.columnconfigure(0,weight=1)
        bar=ttk.LabelFrame(self.tabwire,text='Wireframe Kit Lab v25.0.1 — STL direto em Python, sem OpenSCAD',padding=8)
        bar.grid(row=0,column=0,sticky='ew',pady=(0,6))
        self.wf_scale=tk.DoubleVar(value=50.0); self.wf_rod=tk.DoubleVar(value=2.0); self.wf_pin=tk.DoubleVar(value=1.65)
        self.wf_clear=tk.DoubleVar(value=0.25); self.wf_pinlen=tk.DoubleVar(value=8.0); self.wf_joint=tk.DoubleVar(value=5.5); self.wf_seg=tk.IntVar(value=24)
        specs=[('Escala aresta mm/unid',self.wf_scale,1,300,1),('Raio haste',self.wf_rod,0.5,20,0.1),('Raio pino',self.wf_pin,0.3,20,0.1),('Folga',self.wf_clear,0.0,2.0,0.05),('Comp. pino',self.wf_pinlen,1,50,0.5),('Raio junta',self.wf_joint,1,50,0.5),('Segmentos',self.wf_seg,8,64,1)]
        for label,var,a,b,inc in specs:
            ttk.Label(bar,text=label).pack(side='left',padx=(4,1))
            sp=ttk.Spinbox(bar,from_=a,to=b,increment=inc,textvariable=var,width=6,command=self.update_wireframe_tab)
            sp.pack(side='left',padx=(0,4)); sp.bind('<KeyRelease>',lambda e:self.update_wireframe_tab()); sp.bind('<FocusOut>',lambda e:self.update_wireframe_tab())
        tools=ttk.Frame(self.tabwire); tools.grid(row=2,column=0,sticky='ew',pady=(6,0))
        self.wf_preview_mode=tk.StringVar(value='Wireframe completo')
        ttk.Label(tools,text='Preview 3D:').pack(side='left',padx=(0,4))
        ttk.Combobox(tools,textvariable=self.wf_preview_mode,values=['Wireframe completo','Hastes agrupadas','Juntas agrupadas'],state='readonly',width=22).pack(side='left',padx=3)
        ttk.Button(tools,text='Atualizar relatório/preview',command=self.update_wireframe_tab).pack(side='left',padx=3)
        ttk.Button(tools,text='Exportar wireframe completo STL',command=self.export_wireframe_full_ui).pack(side='left',padx=3)
        ttk.Button(tools,text='Exportar hastes STL',command=self.export_wireframe_rods_ui).pack(side='left',padx=3)
        ttk.Button(tools,text='Exportar juntas STL',command=self.export_wireframe_joints_ui).pack(side='left',padx=3)
        ttk.Button(tools,text='Exportar kit ZIP',command=self.export_wireframe_zip_ui).pack(side='left',padx=3)
        body=ttk.Panedwindow(self.tabwire,orient='horizontal')
        body.grid(row=1,column=0,sticky='nsew')
        left=ttk.Frame(body); right=ttk.Frame(body)
        body.add(left,weight=1); body.add(right,weight=2)
        self.wire_text=tk.Text(left,wrap='word',font=('Consolas',10)); self.wire_text.pack(fill='both',expand=True)
        self.figwire=plt.Figure(figsize=(6,5)); self.axwire=self.figwire.add_subplot(111,projection='3d')
        self.canvaswire=FigureCanvasTkAgg(self.figwire,master=right); self.canvaswire.get_tk_widget().pack(fill='both',expand=True)
    def update_wireframe_tab(self):
        if not self.poly or not hasattr(self,'wire_text'):
            return
        params=self._wf_params()
        self.wire_text.delete('1.0','end')
        self.wire_text.insert('end',wireframe_report(self.poly,params))
        self._update_wireframe_preview()
    def _update_wireframe_preview(self):
        if not self.poly or not hasattr(self,'axwire'):
            return
        params=self._wf_params(); mode=self.wf_preview_mode.get() if hasattr(self,'wf_preview_mode') else 'Wireframe completo'
        try:
            if mode=='Hastes agrupadas':
                v,f=mesh_rod_groups_display(self.poly,params); title='Hastes agrupadas por comprimento'
            elif mode=='Juntas agrupadas':
                v,f=mesh_joint_groups_display(self.poly,params); title='Juntas agrupadas por assinatura angular'
            else:
                v,f=mesh_wireframe_full(self.poly,params); title='Wireframe completo — hastes + juntas simplificadas'
            _gp2501_plot_mesh(self.axwire,v,f,title=title,alpha=0.80,show_axes=False,show_vertices=False,vertex_size=2)
            self.canvaswire.draw_idle()
        except Exception as exc:
            self.axwire.clear(); self.axwire.axis('off'); self.axwire.text(.05,.95,'Erro no preview wireframe:\n'+str(exc),va='top',ha='left',transform=self.axwire.transAxes)
            self.canvaswire.draw_idle()

_RUN_SELF_TESTS_V2501_BASE=run_self_tests

def run_self_tests():
    base=_RUN_SELF_TESTS_V2501_BASE()
    results=list(base.results) if isinstance(base,TestReport) else []
    def add(name,ok,detail=''):
        results.append(TestCaseResult(str(name),bool(ok),'' if ok else str(detail)))
    try:
        cube=CATALOG['Platônicos / Cubo ou Hexaedro'].build(); params=WireframeParams(edge_scale_mm=40.0)
        for label,fn in [('preview wireframe',mesh_wireframe_full),('preview hastes',mesh_rod_groups_display),('preview juntas',mesh_joint_groups_display)]:
            v,f=fn(cube,params); add(label+' gera malha',len(v)>0 and len(f)>0,(len(v),len(f)))
        add('controles 3D existem na classe',hasattr(GeoPolyAppV2501,'update_3d'),'')
    except Exception as exc:
        add('v25.0.1 exception',False,repr(exc))
    return TestReport(results)

def main():
    GeoPolyAppV2501().mainloop()


# v27.2f: explicit export list so internal star imports preserve historical
# single-underscore helper symbols without using wholesale update calls.
__all__ = [k for k in globals() if not k.startswith('__')]
