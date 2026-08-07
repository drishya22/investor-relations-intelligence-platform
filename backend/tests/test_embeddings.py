from app.ai.embedding_service import EmbeddingService

embedding_service = EmbeddingService()

embedding = embedding_service.generate_embedding(
    "Investor conference call regarding quarterly earnings."
)

print(type(embedding))

print(len(embedding))

print(embedding[:10])