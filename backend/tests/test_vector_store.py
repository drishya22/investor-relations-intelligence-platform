from app.ai.embedding_service import EmbeddingService
from app.ai.vector_store import VectorStore

embedding_service = EmbeddingService()
vector_store = VectorStore()

text = "Quarterly earnings conference call."

embedding = embedding_service.generate_embedding(text)

vector_store.add_documents(
    ids=["doc1"],
    documents=[text],
    embeddings=[embedding],
    metadatas=[
        {
            "company": "Page Industries"
        }
    ]
)

print("Stored successfully.")