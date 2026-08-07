from app.ai.vector_store import VectorStore

vector_store = VectorStore()

vector_store.delete_collection()

print("Collection deleted successfully.")