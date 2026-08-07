from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(self):
        self.model=SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-V2" #fast,excellent semantic search, used in RAG. 
        )

    def generate_embedding(self,text:str):
        embedding=self.model.encode(
            text,
            convert_to_numpy=True
        )
        return embedding.tolist()

    def generate_embeddings(self,texts:str):
        embeddings=self.model.encode(
            texts,
            convert_to_numpy=True
            )
        return embeddings.tolist()