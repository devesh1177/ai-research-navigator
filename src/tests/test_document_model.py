from research_navigator.ingest.models.document import (
    Document,
)


def test_document_model() -> None:

    document = Document(
        doc_id="1",
        title="Test Paper",
        authors=["Author A"],
        year=2024,
        content_type="paper",
        source_url="https://example.com",
        local_path="paper.pdf",
        tags=["rag"],
        text="sample text",
    )

    assert document.doc_id == "1"
    assert document.title == "Test Paper"
    assert document.year == 2024
