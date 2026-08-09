class EmbeddingService:

    def __init__(self):
        self.model = None

    def _get_model(self):
        if self.model is None:
            from sentence_transformers import SentenceTransformer

            self.model = SentenceTransformer(
                "sentence-transformers/all-MiniLM-L6-V2"
            )

        return self.model

    def generate_embedding(self, text: str):
        model = self._get_model()

        embedding = model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding.tolist()

    def generate_embeddings(self, texts: list[str]):
        model = self._get_model()

        embeddings = model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings.tolist()