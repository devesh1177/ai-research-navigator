from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(host="localhost", port=6333)

collections = client.get_collections()

existing = [c.name for c in collections.collections]

if "research_navigator" not in existing:
    client.create_collection(
        collection_name="research_navigator",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )

    print("Collection created!")

else:
    print("Collection already exists.")
