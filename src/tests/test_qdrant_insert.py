from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

from research_navigator.ingest.embeddings import embed

client = QdrantClient(
    host="localhost",
    port=6333,
)

vector = embed(
    "Attention is all you need"
).tolist()

client.upsert(
    collection_name="research_navigator",
    points=[
        PointStruct(
            id=1,
            vector=vector,
            payload={
                "doc_id": "test_doc",
                "title": "Attention Is All You Need",
                "section_title": "Introduction",
            },
        )
    ],
)

print("Inserted successfully!")
