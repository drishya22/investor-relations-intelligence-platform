from bs4 import BeautifulSoup

from app.crawler.crawler_factory import CrawlerFactory
from app.crawler.parser import extract_all_links, extract_pdf_links
from app.services.ingestion_service import IngestionService
from app.ai.vector_store import VectorStore


# --------------------------------------------------
# Configuration
# --------------------------------------------------

IR_URL = "https://pageind.com/pages/investors-relations"

COMPANY = "Page Industries"


# --------------------------------------------------
# Main ingestion pipeline
# --------------------------------------------------

def main():

    vector_store = VectorStore()

    count = vector_store.count()

    print(f"Existing documents in Chroma: {count}")

    # Do not ingest again if data already exists
    if count > 0:
        print("Chroma already contains documents. Skipping ingestion.")
        return

    print()
    print("Fetching Page Industries Investor Relations page...")

    # --------------------------------------------------
    # 1. Crawl Investor Relations page
    # --------------------------------------------------

    crawler = CrawlerFactory.get_crawler(IR_URL)

    html = crawler.fetch_page()

    print("Investor Relations page fetched successfully.")

    # --------------------------------------------------
    # 2. Parse HTML
    # --------------------------------------------------

    soup = BeautifulSoup(html, "html.parser")

    links = extract_all_links(
        soup,
        IR_URL
    )

    print(f"Total links discovered: {len(links)}")

    # --------------------------------------------------
    # 3. Extract PDF links
    # --------------------------------------------------

    pdf_links = extract_pdf_links(links)

    print(f"PDF links discovered: {len(pdf_links)}")

    # --------------------------------------------------
    # 4. Select recent and relevant documents
    # --------------------------------------------------

    selected = []

    for pdf in pdf_links:

        url = pdf["url"].lower()

        # Focus on recent FY2025-26 / 2026 documents
        recent = any(
            year in url
            for year in [
                "2025-26",
                "2026",
                "q4fy26",
            ]
        )

        # Focus on useful investor-relations documents
        relevant = any(
            keyword in url
            for keyword in [
                "annual_report",
                "results",
                "press_release",
                "investor_presentation",
                "transcript",
                "investor_meet",
                "earnings_call",
            ]
        )

        if recent and relevant:
            selected.append(pdf)

    # --------------------------------------------------
    # 5. Display selected documents
    # --------------------------------------------------

    print()
    print(f"Relevant recent PDFs found: {len(selected)}")

    for i, pdf in enumerate(selected, start=1):

        print(f"{i}. {pdf['url']}")

    # --------------------------------------------------
    # Safety check
    # --------------------------------------------------

    if not selected:

        print("No suitable PDF documents were found.")
        return

    # --------------------------------------------------
    # 6. Ingest documents
    # --------------------------------------------------

    print()
    print("Starting document ingestion...")

    ingestion_service = IngestionService()

    for i, pdf in enumerate(selected, start=1):

        print()
        print("=" * 70)
        print(f"INGESTING DOCUMENT {i}/{len(selected)}")
        print(f"URL: {pdf['url']}")
        print("=" * 70)

        try:

            result = ingestion_service.ingest(
                company=COMPANY,
                pdf_url=pdf["url"]
            )

            print()
            print("INGESTION COMPLETE")
            print(result)

        except Exception as e:

            print()
            print("INGESTION FAILED")
            print(f"URL: {pdf['url']}")
            print(f"ERROR: {e}")

    # --------------------------------------------------
    # 7. Final status
    # --------------------------------------------------

    print()
    print("=" * 70)
    print("ALL INGESTION FINISHED")
    print(f"Total chunks in Chroma: {vector_store.count()}")
    print("=" * 70)


# --------------------------------------------------
# Entry point
# --------------------------------------------------

if __name__ == "__main__":
    main()