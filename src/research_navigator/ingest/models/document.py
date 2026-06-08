from dataclasses import dataclass
from typing import List


@dataclass
class Document:
    doc_id: str
    title: str
    authors: List[str]
    year: int
    content_type: str
    source_url: str
    local_path: str
    tags: List[str]
    text: str