from research_navigator.ingest.parsers.pdf_parser import parse_pdf
import re

text = parse_pdf("documents/arxiv/arxiv-1706.03762.pdf")

match = re.search(
    r"Abstract(.*?)1\s+Introduction",
    text,
    re.DOTALL,
)

if match:
    print(match.group(1)[:1000])
else:
    print("Abstract not found")
