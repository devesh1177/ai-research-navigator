# test_pdf_parser.py

from research_navigator.ingest.parsers.pdf_parser import parse_pdf

text = parse_pdf(
    "documents/arxiv/arxiv-1706.03762.pdf"
)

print(type(text))
print(len(text))
print(text[:1000])