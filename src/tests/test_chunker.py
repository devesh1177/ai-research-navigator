from research_navigator.ingest.chunker import (
    chunk_sections,
)


sample_sections = [
    {
        "section_title": "Introduction",
        "content": "Hello world " * 1000,
    }
]

chunks = chunk_sections(
    sample_sections,
)

print("Chunks:", len(chunks))

for chunk in chunks[:3]:
    print(chunk["section_title"])
    print(chunk["chunk_index"])
