from research_navigator.ingest.chunker import chunk_text

sample_text = "Hello world " * 1000

chunks = chunk_text(sample_text)

print("Chunks:", len(chunks))

for i, chunk in enumerate(chunks[:3]):
    print(f"\nChunk {i}")
    print("Length:", len(chunk))