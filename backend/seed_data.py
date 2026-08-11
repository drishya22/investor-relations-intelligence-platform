from app.services.ingestion_service import IngestionService
from app.ai.vector_store import VectorStore


PDF_URL = (
    "https://pageind.com/cdn/shop/files/"
    "Investor_Meet_on_18_and_19_June_2026.pdf"
    "?v=3125502281450764386"
)

COMPANY = "Page Industries"


def main():
    vector_store = VectorStore()

    count = vector_store.count()

    print(f"Existing documents in Chroma: {count}")

    if count > 0:
        print("Chroma already contains documents. Skipping ingestion.")
        return

    print("Starting initial document ingestion...")

    ingestion_service = IngestionService()

    result = ingestion_service.ingest(
        company=COMPANY,
        pdf_url=PDF_URL
    )

    print("INGESTION COMPLETE")
    print(result)


if __name__ == "__main__":
    main()