from app.services.pdf_downloader import PDFDownloader


pdf_url = "https://pageind.com/cdn/shop/files/Earning_Call_Notification_Q2_2025.pdf?v=16310887371741971107"

downloader = PDFDownloader()

metadata = downloader.download(
    company="Page Industries",
    pdf_url=pdf_url
)

print(metadata)