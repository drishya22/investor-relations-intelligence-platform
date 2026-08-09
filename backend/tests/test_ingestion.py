from app.services.ingestion_service import IngestionService


def main():

    service = IngestionService()

    result = service.ingest(
        company="Page Industries",
        pdf_url=(
            "https://pageind.com/cdn/shop/files/"
            "Investor_Meet_on_18_and_19_June_2026.pdf"
            "?v=3125502281450764386"
        ),
    )

    print("\n" + "=" * 60)
    print("INGESTION COMPLETE")
    print("=" * 60)

    print(f"Company: {result['company']}")
    print(f"Filename: {result['filename']}")
    print(f"Local path: {result['local_path']}")
    print(f"Pages: {result['page_count']}")
    print(f"Chunks: {result['chunk_count']}")


if __name__ == "__main__":
    main()