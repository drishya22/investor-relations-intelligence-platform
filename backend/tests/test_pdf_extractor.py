from app.pdf.pdf_extractor import PDFExtractor


pdf = "data/reports/page_industries/Investor_Meet_on_18_and_19_June_2026.pdf"

extractor = PDFExtractor()

result = extractor.extract(pdf)

print("=" * 60)

print("Pages:", result["page_count"])

print("=" * 60)

print(result["text"][:2000])