from collections import OrderedDict


def build_citations(results):

    citations = OrderedDict()

    citation_number = 1

    for result in results:
        payload = result.payload

        doc_id = payload["doc_id"]

        if doc_id in citations:
            continue

        citations[doc_id] = {
            "citation_id": citation_number,
            "title": payload["title"],
            "year": payload["year"],
            "section": payload["section_title"],
            "doc_id": payload["doc_id"],
            "content_type": payload["content_type"],
        }

        citation_number += 1

    return list(citations.values())
