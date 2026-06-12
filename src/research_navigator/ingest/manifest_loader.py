from typing import Any, cast
import json


def load_manifest(
    manifest_path: str,
) -> dict[str, Any]:

    with open(
        manifest_path,
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    return cast(
        dict[str, Any],
        data,
    )
