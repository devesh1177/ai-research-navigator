from research_navigator.ingest.manifest_loader import load_manifest

manifest = load_manifest("manifest.json")

documents = manifest["documents"]

print("Document count:", len(documents))

doc = documents[0]

print("\nAvailable fields:")

for key in doc.keys():
    print(key)
