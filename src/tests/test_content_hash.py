from research_navigator.ingest.utils import generate_content_hash

text1 = "hello world"
text2 = "hello world"
text3 = "different text"

hash1 = generate_content_hash(text1)
hash2 = generate_content_hash(text2)
hash3 = generate_content_hash(text3)

print("Hash1:", hash1)
print("Hash2:", hash2)
print("Hash3:", hash3)

print("\nSame text:")
print(hash1 == hash2)

print("\nDifferent text:")
print(hash1 == hash3)
