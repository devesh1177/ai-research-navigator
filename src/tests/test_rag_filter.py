from qdrant_client import QdrantClient
from qdrant_client.models import (
    Filter,
    FieldCondition,
    MatchValue,
)

client = QdrantClient(
    host="localhost",
    port=6333,
)

points, _ = client.scroll(
    collection_name="research_navigator",
    scroll_filter=Filter(must=[FieldCondition(key="tags", match=MatchValue(value="RAG"))]),
    limit=10,
)

print("Matches:", len(points))

for point in points:
    print(point.payload["title"])
