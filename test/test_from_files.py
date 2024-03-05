import fixcompliance


def test_benchmarks_from_files():
    benchmarks = fixcompliance.benchmarks_from_files()
    assert benchmarks
    assert len(benchmarks) > 1


def test_checks_from_files():
    checks = fixcompliance.checks_from_files()
    assert checks
    assert len(checks) > 1
