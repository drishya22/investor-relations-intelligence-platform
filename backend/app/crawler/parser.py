from urllib.parse import urljoin


def extract_all_links(soup, base_url):

    links = []

    for tag in soup.find_all("a", href=True):

        href = tag["href"]

        title = tag.get_text(strip=True)

        links.append(
            {
                "title": title if title else "Untitled",
                "url": urljoin(base_url, href)
            }
        )

    return links


def extract_pdf_links(links):
    """
    Extract unique PDF links.
    """

    unique_urls = set()
    pdfs = []

    for link in links:

        url = link["url"]

        if ".pdf" not in url.lower():
            continue

        if url in unique_urls:
            continue

        unique_urls.add(url)
        pdfs.append(link)

    return pdfs