from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue,
    Range,
)


def build_filter(filters):

    conditions = []

    if filters["year_gte"] is not None:

        conditions.append(
            FieldCondition(
                key="year",
                range=Range(
                    gte=filters["year_gte"]
                ),
            )
        )

    for tag in filters["tags"]:

        conditions.append(
            FieldCondition(
                key="tags",
                match=MatchValue(
                    value=tag
                ),
            )
        )

    if not conditions:
        return None

    return Filter(
        must=conditions
    )