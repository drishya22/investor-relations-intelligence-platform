from app.ai.embedding_service import EmbeddingService
from app.ai.text_chunker import TextChunker
from app.ai.vector_store import VectorStore
from app.pdf.pdf_extractor import PDFExtractor

PDF_PATH = "data/reports/page_industries/Earning_Call_Notification_Q2_2025.pdf"

extractor = PDFExtractor()
chunker = TextChunker()
embedding_service = EmbeddingService()
vector_store = VectorStore()

text = extractor.extract(PDF_PATH)["text"]
chunks = chunker.split(text)

embeddings = embedding_service.generate_embeddings(chunks)

ids = [f"page_industries_chunk_{i}" for i in range(len(chunks))]

documents = chunks

metadatas = [
    {
        "company": "Page Industries",
        "chunk": i
    }
    for i in range(len(chunks))
]

vector_store.add_documents(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)

print(f"Stored {len(chunks)} chunks.")