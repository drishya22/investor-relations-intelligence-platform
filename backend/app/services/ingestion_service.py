from pathlib import Path

from app.pdf.pdf_extractor import PDFExtractor
from app.ai.text_chunker import TextChunker
from app.ai.embedding_service import EmbeddingService
from app.ai.vector_store import VectorStore
from app.services.pdf_downloader import PDFDownloader

class IngestionService:
    def __init__(self):
        self.downloader=PDFDownloader()
        self.extractor=PDFExtractor()
        self.chunker=TextChunker()
        self.embedding_service=EmbeddingService()
        self.vector_store=VectorStore()

    def ingest(self,company:str,pdf_url:str):
        file_info=self.downloader.download(company=company, pdf_url=pdf_url)
        pdf_path=file_info["local_path"]
        extraction=self.extractor.extract(pdf_path)
        text=extraction["text"]
        page_count=extraction["page_count"]

        chunks=self.chunker.split(text)
        embeddings=(self.embedding_service.generate_embeddings(chunks))

        filename=Path(pdf_path).stem
        ids=[f"{company}_{filename}_chunk_{i}" for i in range(len(chunks))]
        metadatas=[
            {
                "company":company,
                "filename":Path(pdf_path).name,
                "page_count":page_count,
                "chunk_index":i,
                "source":pdf_url,
            }
            for i in range(len(chunks))
        ]
        self.vector_store.add_documents(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )

        return {
            "company": company,
            "filename": Path(pdf_path).name,
            "local_path": pdf_path,
            "page_count": page_count,
            "chunk_count": len(chunks),
        }


