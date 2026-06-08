from research_navigator.ingest.parsers.pdf_parser import parse_pdf
from research_navigator.ingest.parsers.section_parser import extract_sections

text = parse_pdf("documents/arxiv/arxiv-1706.03762.pdf")

sections = extract_sections(text)

print("Sections found:", len(sections))

for section in sections[:10]:
    print(section["section_title"])
