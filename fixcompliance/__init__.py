import os
import json
import time
import threading
from typing import Any, Dict
from importlib.resources import files as resource_filename
from pathlib import Path

__version__ = "0.4.1"

Json = Dict[str, Any]
CACHE_TIMEOUT = 3600
_cache = {}
_cache_lock = threading.Lock()


def benchmarks_from_files() -> Dict[str, Json]:
    return _from_files("data/benchmark", add_id=True)


def checks_from_files() -> Dict[str, Json]:
    return _from_files("data/checks", add_id=False)


def _from_files(json_path: str, add_id: bool = False) -> dict[str, Json]:
    package_dir = resource_filename(__package__)
    static_path: Path = package_dir.joinpath(json_path)
    static_path = static_path.resolve()

    result = {}
    if os.path.exists(static_path):
        for provider in (d.path for d in os.scandir(static_path) if d.is_dir()):
            for path in (d.path for d in os.scandir(provider) if d.is_file() and d.name.endswith(".json")):
                item_id = os.path.basename(path).rsplit(".", maxsplit=1)[0]
                item = cached_json_load(path)
                if add_id:
                    item["id"] = item_id
                result[item_id] = item
    return result


def cached_json_load(file_path: str) -> Json:
    global _cache
    now = time.time()
    mtime = os.path.getmtime(file_path)

    cache_entry = _cache.get(file_path)
    if cache_entry and cache_entry["mtime"] == mtime and now - cache_entry["cached"] < CACHE_TIMEOUT:
        return cache_entry["content"]
    else:
        with open(file_path, "rt", encoding="utf-8") as f:
            content = json.load(f)
        with _cache_lock:
            cache_entry = _cache.get(file_path)
            if not (cache_entry and cache_entry["mtime"] == mtime and now - cache_entry["cached"] < CACHE_TIMEOUT):
                _cache[file_path] = {"content": content, "mtime": mtime, "cached": now}
        return content
