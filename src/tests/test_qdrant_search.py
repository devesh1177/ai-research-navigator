from qdrant_client import QdrantClient

from research_navigator.ingest.embeddings import embed

client = QdrantClient(
    host="localhost",
    port=6333,
)

query_vector = embed("transformer architecture").tolist()

results = client.query_points(
    collection_name="research_navigator",
    query=query_vector,
    limit=3,
)

print(results)
