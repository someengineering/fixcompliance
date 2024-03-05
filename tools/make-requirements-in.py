#!/usr/bin/env python3
import tomllib


def create_in_files(pyproject_path: str):
    """Create requirements.in and requirements-test.in from pyproject.toml."""
    with open(pyproject_path, "rb") as f:
        pyproject = tomllib.load(f)

    dependencies = pyproject.get("project", {}).get("dependencies", [])
    test_dependencies = pyproject.get("pyproject", {}).get("optional-dependencies", {}).get("test", [])
    dev_dependencies = pyproject.get("pyproject", {}).get("optional-dependencies", {}).get("dev", [])

    # Write main dependencies to requirements.in
    with open("requirements.in", "w") as f:
        for dep in dependencies:
            f.write(dep + "\n")

    # Write test dependencies to requirements-test.in
    with open("requirements-test.in", "w") as f:
        for test_dep in test_dependencies:
            f.write(test_dep + "\n")

    # Write dev dependencies to requirements-dev.in
    with open("requirements-dev.in", "w") as f:
        for dev_dep in dev_dependencies:
            f.write(dev_dep + "\n")


if __name__ == "__main__":
    pyproject_path = "pyproject.toml"
    create_in_files(pyproject_path)
