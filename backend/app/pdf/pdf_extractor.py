import fitz


class PDFExtractor:

    def extract(self, pdf_path: str):

        document = fitz.open(pdf_path)

        full_text = []

        page_count = len(document)

        for page in document:

            full_text.append(page.get_text())

        document.close()

        return {
            "page_count": page_count,
            "text": "\n".join(full_text)
        }