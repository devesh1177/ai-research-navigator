from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
)

from research_navigator.config.settings import (
    settings,
)


client = QdrantClient(
    host=settings.qdrant_host,
    port=settings.qdrant_port,
)

collections = client.get_collections()

existing = [c.name for c in collections.collections]

if settings.collection_name not in existing:
    client.create_collection(
        collection_name=settings.collection_name,
        vectors_config=VectorParams(
            size=settings.vector_size,
            distance=Distance.COSINE,
        ),
    )
