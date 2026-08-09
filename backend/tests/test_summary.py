from app.ai.summary_service import SummaryService
from app.pdf.pdf_extractor import PDFExtractor


PDF_PATH = (
    "data/reports/page_industries/"
    "Earning_Call_Notification_Q2_2025.pdf"
)


extractor = PDFExtractor()

extraction = extractor.extract(PDF_PATH)

text = extraction["text"]

summary_service = SummaryService()

summary = summary_service.summarize(text)

print("=" * 80)
print("AI SUMMARY")
print("=" * 80)
print(summary)