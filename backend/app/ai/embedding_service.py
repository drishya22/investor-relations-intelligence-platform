import time

from google import genai
from google.genai import types

from app.config import GEMINI_API_KEY


class EmbeddingService:

    def __init__(self):

        if not GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        self.model_name = "gemini-embedding-001"

        self.output_dimensionality = 768

    # --------------------------------------------------
    # Single text embedding
    # --------------------------------------------------

    def generate_embedding(self, text: str):

        result = self.client.models.embed_content(
            model=self.model_name,
            contents=text,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_QUERY",
                output_dimensionality=self.output_dimensionality
            )
        )

        return result.embeddings[0].values

    # --------------------------------------------------
    # Multiple document embeddings
    # --------------------------------------------------

    def generate_embeddings(self, texts: list[str]):

        all_embeddings = []

        # Gemini allows at most 100 requests/items
        # in one batch. We deliberately use 50.
        batch_size = 50

        for start in range(0, len(texts), batch_size):

            end = min(
                start + batch_size,
                len(texts)
            )

            batch = texts[start:end]

            print(
                f"Generating embeddings "
                f"for chunks {start + 1}-{end} "
                f"of {len(texts)}..."
            )

            max_retries = 3

            for attempt in range(max_retries):

                try:

                    result = self.client.models.embed_content(
                        model=self.model_name,
                        contents=batch,
                        config=types.EmbedContentConfig(
                            task_type="RETRIEVAL_DOCUMENT",
                            output_dimensionality=self.output_dimensionality
                        )
                    )

                    batch_embeddings = [
                        embedding.values
                        for embedding in result.embeddings
                    ]

                    all_embeddings.extend(
                        batch_embeddings
                    )

                    print(
                        f"Batch complete: "
                        f"{len(batch_embeddings)} embeddings"
                    )

                    break

                except Exception as e:

                    error_message = str(e)

                    is_quota_error = (
                        "429" in error_message
                        or "RESOURCE_EXHAUSTED" in error_message
                        or "quota" in error_message.lower()
                    )

                    if not is_quota_error:
                        raise

                    if attempt == max_retries - 1:
                        raise

                    wait_time = 65

                    print(
                        "Gemini embedding quota reached."
                    )

                    print(
                        f"Waiting {wait_time} seconds "
                        f"before retry..."
                    )

                    time.sleep(wait_time)

        return all_embeddings