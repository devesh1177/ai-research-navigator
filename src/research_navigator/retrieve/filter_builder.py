from typing import Any

from qdrant_client.models import (
    FieldCondition,
    Filter,
    MatchValue,
    Range,
)

from research_navigator.retrieve.query_understanding import (
    QueryFilters,
)


def build_filter(
    filters: QueryFilters,
) -> Filter | None:

    conditions: list[Any] = []

    if filters["year_gte"] is not None:
        conditions.append(
            FieldCondition(
                key="year",
                range=Range(
                    gte=filters["year_gte"],
                ),
            )
        )

    for tag in filters["tags"]:
        conditions.append(
            FieldCondition(
                key="tags",
                match=MatchValue(
                    value=tag,
                ),
            )
        )

    if not conditions:
        return None

    return Filter(
        must=conditions,
    )
