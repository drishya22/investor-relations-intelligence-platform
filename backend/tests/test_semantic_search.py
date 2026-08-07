from app.ai.semantic_search import SemanticSearch

search = SemanticSearch()

results = search.search(
    "quarterly earnings conference call",
    n_results=3
)

print("=" * 80)

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"\nResult {i}\n")
    print(doc)
    print("-" * 80)