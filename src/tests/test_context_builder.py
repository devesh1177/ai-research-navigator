from research_navigator.retrieve.retriever import retrieve
from research_navigator.retrieve.context_builder import build_context

results = retrieve("What is transformer architecture?")

context = build_context(results)

print(context[:3000])
