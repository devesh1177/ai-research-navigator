from research_navigator.ingest.parsers.pdf_parser import (
    parse_pdf,
)

from research_navigator.ingest.parsers.section_parser import (
    extract_sections,
)

from research_navigator.ingest.chunker import (
    chunk_sections,
)


def test_chunk_sections() -> None:

    text = parse_pdf(
        "documents/arxiv/arxiv-1706.03762.pdf",
    )

    sections = extract_sections(
        text,
    )

    chunks = chunk_sections(
        sections,
    )

    assert len(sections) > 0

    assert len(chunks) > 0

    first_chunk = chunks[0]

    assert "section_title" in first_chunk
    assert "section_index" in first_chunk
    assert "chunk_index" in first_chunk
    assert "content" in first_chunk
