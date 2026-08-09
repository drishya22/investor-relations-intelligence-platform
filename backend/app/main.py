from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.ai.embedding_service import EmbeddingService
from app.ai.semantic_search import SemanticSearch
from app.ai.summary_service import SummaryService

from app.schemas.search import (
    SearchRequest,
    SearchResponse,
)

from app.schemas.summary import (
    SummaryRequest,
    SummaryResponse,
)


app = FastAPI(
    title="Investor Relations Intelligence Platform"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Services
# --------------------------------------------------

embedding_service = EmbeddingService()
semantic_search = SemanticSearch()
summary_service = SummaryService()


# --------------------------------------------------
# Basic endpoints
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Investor Relations Intelligence Platform API"
    }


@app.get("/health")
def health():
    return {
        "message": "API is working fine"
    }


# --------------------------------------------------
# Semantic Search
# --------------------------------------------------

@app.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):

    results = semantic_search.search(
        query=request.query,
        n_results=request.n_results
    )

    documents = results.get("documents", [[]])[0]

    metadatas = results.get("metadatas", [[]])[0]

    distances = results.get("distances", [[]])[0]

    formatted_results = []

    for document, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):
        formatted_results.append(
            {
                "document": document,
                "metadata": metadata,
                "distance": distance,
            }
        )

    return {
        "query": request.query,
        "results": formatted_results,
    }


# --------------------------------------------------
# AI Summary
# --------------------------------------------------

@app.post(
    "/summarize",
    response_model=SummaryResponse
)
def summarize(request: SummaryRequest):

    summary = summary_service.summarize(
        request.text
    )

    return {
        "summary": summary
    }