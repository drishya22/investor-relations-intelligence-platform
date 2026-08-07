from app.ai.text_chunker import TextChunker
from app.pdf.pdf_extractor import PDFExtractor


pdf = "data/reports/page_industries/Earning_Call_Notification_Q2_2025.pdf"

extractor = PDFExtractor()

text = extractor.extract(pdf)["text"]

chunker = TextChunker()

chunks = chunker.split(text)

print(f"Total Chunks: {len(chunks)}")

print("=" * 80)

for i, chunk in enumerate(chunks):

    print(f"\nChunk {i+1}\n")

    print(chunk[:400])

    print("=" * 80)