from research_navigator.ingest.models.chunk_model import ChunkPayload

chunk = ChunkPayload(
    doc_id="paper1",
    content_type="arxiv_paper",
    title="Attention Is All You Need",
    year=2017,
    primary_category="cs.CL",
    section_title="Introduction",
    section_index=0,
    chunk_index=0,
    content="sample text",
)

print(chunk)
