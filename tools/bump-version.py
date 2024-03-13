#!/usr/bin/env python3
from packaging.version import parse
import tomllib, tomli_w


def bump_version(original_version):
    version = parse(original_version)
    if version.is_prerelease:
        # Increase the pre-release number (e.g., 0.4.1a4 -> 0.4.1a5)
        return str(version.base_version) + version.pre[0] + str(int(version.pre[1]) + 1)
    else:
        # Increase the patch version (e.g., 0.4.1 -> 0.4.2)
        return str(version.major) + "." + str(version.minor) + "." + str(version.micro + 1)


def update_pyproject_version(new_version):
    with open("pyproject.toml", "rb") as f:
        pyproject_data = tomllib.load(f)
    pyproject_data["project"]["version"] = new_version
    with open("pyproject.toml", "wb") as f:
        tomli_w.dump(pyproject_data, f)


def update_init_version(new_version):
    init_path = "fixcompliance/__init__.py"
    with open(init_path, "r") as file:
        lines = file.readlines()
    with open(init_path, "w") as file:
        for line in lines:
            if line.startswith("__version__"):
                file.write(f'__version__ = "{new_version}"\n')
            else:
                file.write(line)


if __name__ == "__main__":
    with open("pyproject.toml", "rb") as f:
        pyproject_data = tomllib.load(f)
    current_version = pyproject_data["project"]["version"]
    new_version = bump_version(current_version)
    update_pyproject_version(new_version)
    update_init_version(new_version)
