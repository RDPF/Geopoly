def test_batch_platonic_savings_or_equal():
    from geopoly import runtime as rt
    from geopoly.batch_optimizer import solve_batch_material_optimizer
    keys=[]
    for needle in ['Tetraedro','Cubo','Octaedro','Dodecaedro','Icosaedro']:
        keys.append(next(it.key for it in rt.CATALOG_ITEMS if needle in it.key and 'Platônicos' in it.key))
    jobs=[rt.BatchNetJob(i,k,k,50,1) for i,k in enumerate(keys,1)]
    res=solve_batch_material_optimizer(jobs)
    assert res.optimized_pages <= res.baseline_pages
    assert res.optimized_utilization_percent >= res.baseline_utilization_percent
