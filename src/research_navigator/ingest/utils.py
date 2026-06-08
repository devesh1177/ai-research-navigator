import hashlib


def generate_content_hash(text: str) -> str:
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def generate_chunk_id(
    doc_id: str,
    chunk_index: int,
    content_hash: str,
) -> str:
    return (
        f"{doc_id}_{chunk_index}_{content_hash[:12]}"
    )