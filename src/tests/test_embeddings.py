from research_navigator.ingest.embeddings import embed

print("Generating embedding...")

vector = embed("Attention is all you need")

print(type(vector))
print(len(vector))
print(vector[:10])
