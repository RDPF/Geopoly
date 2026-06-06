"""GeoPoly public johnson API."""
from . import runtime as _rt

load_johnson_offline_bundle = getattr(_rt, 'load_johnson_offline_bundle')
build_johnson_offline_bundle_from_folder = getattr(_rt, 'build_johnson_offline_bundle_from_folder')
save_johnson_offline_bundle_from_folder = getattr(_rt, 'save_johnson_offline_bundle_from_folder')
require_all_johnson_formal_or_raise = getattr(_rt, 'require_all_johnson_formal_or_raise')
johnson_formal_availability_report = getattr(_rt, 'johnson_formal_availability_report')
johnson_policy_report = getattr(_rt, 'johnson_policy_report')
try_build_formal_johnson = getattr(_rt, 'try_build_formal_johnson')
load_johnson_exact_data = getattr(_rt, 'load_johnson_exact_data')

def __getattr__(name):
    return getattr(_rt, name)

__all__ = ['load_johnson_offline_bundle', 'build_johnson_offline_bundle_from_folder', 'save_johnson_offline_bundle_from_folder', 'require_all_johnson_formal_or_raise', 'johnson_formal_availability_report', 'johnson_policy_report', 'try_build_formal_johnson', 'load_johnson_exact_data']
