import json
from typing import Any


def load_manifest(manifest_path: str) -> list[dict[str, Any]]:
    with open(manifest_path, "r", encoding="utf-8") as f:
        return json.load(f)