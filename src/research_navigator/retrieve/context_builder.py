from typing import Any


def build_context(
    results: list[Any],
) -> str:

    context_parts: list[str] = []

    for result in results:
        payload = result.payload

        context_parts.append(payload["content"])

    return "\n\n".join(context_parts)
