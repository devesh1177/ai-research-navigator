from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from research_navigator.ingest.manifest_loader import load_manifest

from research_navigator.ingest.parsers.pdf_parser import parse_pdf
from research_navigator.ingest.parsers.markdown_parser import parse_markdown

from research_navigator.ingest.parsers.section_parser import (
    extract_sections,
)

from research_navigator.ingest.parsers.markdown_section_parser import (
    extract_markdown_sections,
)

from research_navigator.ingest.chunker import chunk_sections

from research_navigator.ingest.utils import (
    generate_content_hash,
    generate_chunk_id,
)

from research_navigator.ingest.models.chunk_model import ChunkPayload
from research_navigator.ingest.embeddings import embed


def run_pipeline() -> None:

    manifest = load_manifest("manifest.json")

    client = QdrantClient(
        host="localhost",
        port=6333,
    )

    documents_processed = 0
    sections_processed = 0
    chunks_stored = 0

    for document in manifest["documents"]:
        print(f"\nProcessing: {document['title']}")

        try:
            path = document["local_path"]

            if path.endswith(".pdf"):
                text = parse_pdf(path)

                sections = extract_sections(text)

            elif path.endswith(".md"):
                text = parse_markdown(path)

                sections = extract_markdown_sections(text)

            else:
                print(f"Unsupported file type: {path}")

                continue

            chunks = chunk_sections(sections)

            print(f"Sections: {len(sections)} | Chunks: {len(chunks)}")

            sections_processed += len(sections)

            points = []

            for chunk in chunks:
                content_hash = generate_content_hash(chunk["content"])

                chunk_id = generate_chunk_id(
                    document["doc_id"],
                    chunk["chunk_index"],
                    content_hash,
                )

                payload = ChunkPayload(
                    doc_id=document["doc_id"],
                    content_type=document["content_type"],
                    title=document["title"],
                    year=document["year"],
                    primary_category=document["primary_category"],
                    tags=document["tags"],
                    section_title=chunk["section_title"],
                    section_index=chunk["section_index"],
                    chunk_index=chunk["chunk_index"],
                    content=chunk["content"],
                    content_hash=content_hash,
                )

                vector = embed(payload.content).tolist()

                point = PointStruct(
                    id=abs(hash(chunk_id)),
                    vector=vector,
                    payload={
                        "chunk_id": chunk_id,
                        "doc_id": payload.doc_id,
                        "content_type": payload.content_type,
                        "title": payload.title,
                        "year": payload.year,
                        "primary_category": payload.primary_category,
                        "tags": payload.tags,
                        "section_title": payload.section_title,
                        "section_index": payload.section_index,
                        "chunk_index": payload.chunk_index,
                        "content_hash": payload.content_hash,
                        "content": payload.content,
                    },
                )

                points.append(point)

                chunks_stored += 1

            client.upsert(
                collection_name="research_navigator",
                points=points,
            )

            documents_processed += 1

        except Exception as e:
            print(f"Failed: {document['title']}")

            print(e)

    print("\n==========================")
    print("INGESTION COMPLETE")
    print("==========================")

    print(f"Documents Processed: {documents_processed}")

    print(f"Sections Extracted: {sections_processed}")

    print(f"Chunks Stored: {chunks_stored}")


if __name__ == "__main__":
    run_pipeline()
