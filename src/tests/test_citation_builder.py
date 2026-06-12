from research_navigator.retrieve.retriever import (
    retrieve,
)

from research_navigator.generate.citation_builder import (
    build_citations,
)


def test_citation_generation() -> None:

    results = retrieve(
        "recent RAG papers",
    )

    citations = build_citations(
        results,
    )

    assert isinstance(
        citations,
        list,
    )

    if citations:
        citation = citations[0]

        assert "citation_id" in citation
        assert "title" in citation
        assert "year" in citation
        assert "section" in citation
