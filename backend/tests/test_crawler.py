from app.crawler.crawler_factory import CrawlerFactory
from app.crawler.parser import (
    extract_all_links,
    extract_pdf_links,
)

URL =  "https://pageind.com/pages/investors-relations"


def main():

    crawler = CrawlerFactory.get_crawler(URL)

    soup = crawler.get_soup()

    links = extract_all_links(soup, URL)

    print("=" * 80)
    print(f"Total Links : {len(links)}")
    print("=" * 80)

    pdfs = extract_pdf_links(links)

    print(f"\nPDF Links : {len(pdfs)}")
    print("=" * 80)

    for pdf in pdfs:

        print(pdf["title"])
        print(pdf["url"])
        print("-" * 80)


if __name__ == "__main__":
    main()