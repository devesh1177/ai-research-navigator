from qdrant_client import QdrantClient

client = QdrantClient(
    host="localhost",
    port=6333,
)

points = client.scroll(
    collection_name="research_navigator",
    limit=1,
    with_payload=True,
)[0]

payload = points[0].payload

print("Payload Keys:")
print(payload.keys())
