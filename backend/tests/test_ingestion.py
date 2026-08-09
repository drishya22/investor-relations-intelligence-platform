from app.services.ingestion_service import IngestionService


PDF_URL = "https://pageind.com/cdn/shop/files/Earning_Call_Notification_Q2_2025.pdf?v=16310887371741971107"


service = IngestionService()

result = service.ingest(
    company="Page Industries",
    pdf_url=PDF_URL,
)

print("=" * 60)
print("INGESTION COMPLETE")
print("=" * 60)

for key, value in result.items():
    print(f"{key}: {value}")