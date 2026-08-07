from app.pdf.pdf_extractor import PDFExtractor


pdf = "data/reports/page_industries/Earning_Call_Notification_Q2_2025.pdf"

extractor = PDFExtractor()

result = extractor.extract(pdf)

print("=" * 60)

print("Pages:", result["page_count"])

print("=" * 60)

print(result["text"][:2000])