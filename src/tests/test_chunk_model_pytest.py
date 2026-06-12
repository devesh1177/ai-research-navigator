from research_navigator.ingest.models.chunk_model import (
    ChunkPayload,
)


def test_chunk_payload() -> None:

    chunk = ChunkPayload(
        doc_id="1",
        content_type="paper",
        title="Test",
        year=2024,
        primary_category="AI",
        tags=["rag"],
        section_title="Intro",
        section_index=0,
        chunk_index=0,
        content="hello",
    )

    assert chunk.doc_id == "1"
    assert chunk.tags == ["rag"]
