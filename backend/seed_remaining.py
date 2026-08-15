from app.services.ingestion_service import IngestionService
from app.ai.vector_store import VectorStore


COMPANY = "Page Industries"


REMAINING_DOCUMENTS = [
    {
        "name": "Annual Report 2025-26",
        "url": (
            "https://pageind.com/cdn/shop/files/"
            "Annual_Report_2025-26.pdf"
            "?v=10501698024136685069"
        ),
    },
    {
        "name": "Q4 FY26 Transcript",
        "url": (
            "https://pageind.com/cdn/shop/files/"
            "TRANSCRIPTQ4FY26.pdf"
            "?v=17097048218882977130"
        ),
    },
]


def main():

    vector_store = VectorStore()

    print(
        f"Existing chunks in Chroma: "
        f"{vector_store.count()}"
    )

    ingestion_service = IngestionService()

    for index, document in enumerate(
        REMAINING_DOCUMENTS,
        start=1
    ):

        print()
        print("=" * 70)
        print(
            f"INGESTING DOCUMENT "
            f"{index}/{len(REMAINING_DOCUMENTS)}"
        )
        print(
            f"Document: {document['name']}"
        )
        print("=" * 70)

        try:

            result = ingestion_service.ingest(
                company=COMPANY,
                pdf_url=document["url"]
            )

            print()
            print("INGESTION COMPLETE")
            print(result)

        except Exception as e:

            print()
            print("INGESTION FAILED")
            print(
                f"Document: {document['name']}"
            )
            print(
                f"Error: {e}"
            )

    print()
    print("=" * 70)
    print(
        f"FINAL CHROMA COUNT: "
        f"{vector_store.count()}"
    )
    print("=" * 70)


if __name__ == "__main__":
    main()