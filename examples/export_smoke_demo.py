from geopoly.selftests import run_export_smoke_tests_v25253, export_smoke_test_report_v25253
smoke=run_export_smoke_tests_v25253(); print(export_smoke_test_report_v25253(smoke)); assert smoke["ok"]
