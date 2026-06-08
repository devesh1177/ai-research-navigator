from typing import Any
from typing import TypedDict


class NavigatorState(TypedDict):
    query: str
    route: str
    answer: str
    citations: list[Any]
    metadata: dict[str, Any]
