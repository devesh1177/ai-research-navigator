from research_navigator.ingest.manifest_loader import load_manifest

manifest = load_manifest("manifest.json")

print(manifest.keys())

print("\nFirst document:")
print(manifest["documents"][0])
