from research_navigator.ingest.utils import (
    generate_content_hash,
    generate_chunk_id,
)

text = "hello world"

hash_value = generate_content_hash(text)

chunk_id = generate_chunk_id(
    "arxiv-1706.03762",
    0,
    hash_value,
)

print(chunk_id)