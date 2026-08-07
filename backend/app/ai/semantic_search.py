from app.ai.embedding_service import EmbeddingService
from app.ai.vector_store import VectorStore

class SemanticSearch:
    def __init__(self):
        self.embedding_service=EmbeddingService()
        self.vector_store=VectorStore()

    def search(self,query:str,n_results:int=5):
        query_embedding=self.embedding_service.generate_embedding(query)
        results=self.vector_store.search(
            query_embedding=query_embedding,
            n_results=n_results
        )

        return results    