"""GeoPoly public self-tests API (v27.1d).

The smoke-test and self-test API is now exported with explicit named imports,
including the v26/v27 compatibility aliases.
"""
from .runtime import (
    TestCaseResult,
    TestReport,
    run_self_tests,
    run_export_smoke_tests_v25253,
    export_smoke_test_report_v25253,
    run_export_smoke_tests,
    export_smoke_test_report,
)

__all__ = [
    'TestCaseResult',
    'TestReport',
    'run_self_tests',
    'run_export_smoke_tests_v25253',
    'export_smoke_test_report_v25253',
    'run_export_smoke_tests',
    'export_smoke_test_report',
]
