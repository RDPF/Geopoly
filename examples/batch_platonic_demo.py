from geopoly import runtime as rt
from geopoly.batch_optimizer import solve_batch_material_optimizer, batch_optimizer_report
keys=[]
for needle in ['Tetraedro','Cubo','Octaedro','Dodecaedro','Icosaedro']:
    keys.append(next(it.key for it in rt.CATALOG_ITEMS if needle in it.key and 'Platônicos' in it.key))
jobs=[rt.BatchNetJob(i,k,k,50,1) for i,k in enumerate(keys,1)]
res=solve_batch_material_optimizer(jobs)
print(batch_optimizer_report(res))
