import fixcompliance


def test_benchmarks_from_files() -> None:
    benchmarks = fixcompliance.benchmarks_from_files()
    assert benchmarks
    assert len(benchmarks) > 1


def test_checks_from_files() -> None:
    checks = fixcompliance.checks_from_files()
    assert checks
    assert len(checks) > 1
