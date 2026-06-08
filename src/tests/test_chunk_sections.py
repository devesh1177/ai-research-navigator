from research_navigator.ingest.parsers.pdf_parser import parse_pdf
from research_navigator.ingest.parsers.section_parser import extract_sections
from research_navigator.ingest.chunker import chunk_sections

text = parse_pdf(
    "documents/arxiv/arxiv-1706.03762.pdf"
)

sections = extract_sections(text)

chunks = chunk_sections(sections)

print("Sections:", len(sections))
print("Chunks:", len(chunks))

print("\nFirst Chunk Metadata:")
print(chunks[0]["section_title"])
print(chunks[0]["section_index"])
print(chunks[0]["chunk_index"])

print("\nPreview:")
print(chunks[0]["content"][:300])