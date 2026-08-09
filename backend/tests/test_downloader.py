from app.services.pdf_downloader import PDFDownloader


pdf_url = "https://pageind.com/cdn/shop/files/Investor_Meet_on_18_and_19_June_2026.pdf?v=3125502281450764386"

downloader = PDFDownloader()

metadata = downloader.download(
    company="Page Industries",
    pdf_url=pdf_url
)

print(metadata)