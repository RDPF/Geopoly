"""GeoPoly public formula_lab API."""
from . import runtime as _rt

formula_lab_compute = getattr(_rt, 'formula_lab_compute')
formula_lab_text = getattr(_rt, 'formula_lab_text')
formula_lab_plot = getattr(_rt, 'formula_lab_plot')
run_formula_lab_self_tests = getattr(_rt, 'run_formula_lab_self_tests')

def __getattr__(name):
    return getattr(_rt, name)

__all__ = ['formula_lab_compute', 'formula_lab_text', 'formula_lab_plot', 'run_formula_lab_self_tests']
