#!/usr/bin/env python3
import tomllib


def get_version():
    with open("pyproject.toml", "rb") as f:
        pyproject_data = tomllib.load(f)

    return pyproject_data["project"]["version"]


if __name__ == "__main__":
    print(get_version())
