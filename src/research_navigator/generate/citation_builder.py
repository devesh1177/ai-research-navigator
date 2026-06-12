from collections import OrderedDict
from typing import Any


def build_citations(
    results: list[Any],
) -> list[dict[str, Any]]:

    citations: OrderedDict[str, dict[str, Any]] = OrderedDict()

    citation_number = 1

    for result in results:
        payload = result.payload

        doc_id = str(payload["doc_id"])

        if doc_id in citations:
            continue

        citations[doc_id] = {
            "citation_id": citation_number,
            "title": payload["title"],
            "year": payload["year"],
            "section": payload["section_title"],
            "doc_id": payload["doc_id"],
            "content_type": payload.get(
                "content_type",
                "unknown",
            ),
        }

        citation_number += 1

    return list(citations.values())
