from research_navigator.ingest.parsers.pdf_parser import parse_pdf

text = parse_pdf(
    "documents/arxiv/arxiv-1706.03762.pdf"
)

print(text[-3000:])