from dataclasses import dataclass
from typing import Optional


@dataclass
class ChunkPayload:
    doc_id: str
    content_type: str
    title: str

    year: int
    primary_category: str
    tags: list[str]

    section_title: str
    section_index: int
    chunk_index: int

    content: str

    content_hash: Optional[str] = None