from research_navigator.retrieve.retriever import retrieve

from research_navigator.generate.citation_builder import (
    build_citations,
)

query = "recent RAG papers"

results = retrieve(query)

citations = build_citations(results)

for citation in citations:

    print()

    print(
        f"[{citation['citation_id']}]"
    )

    print(
        citation["title"]
    )

    print(
        f"Year: {citation['year']}"
    )

    print(
        f"Section: {citation['section']}"
    )