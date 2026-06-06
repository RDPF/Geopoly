from geopoly import run_self_tests
rep=run_self_tests(); print(rep.summary()); assert rep.failed==0
