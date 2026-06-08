from qdrant_client import QdrantClient

client = QdrantClient(
    host="localhost",
    port=6333,
)

points, _ = client.scroll(
    collection_name="research_navigator",
    limit=1,
    with_payload=True,
)

print(points[0].payload)
