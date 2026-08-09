from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=1)
    n_results: int = Field(default=5, ge=1, le=10)


class SearchResponse(BaseModel):
    query: str
    results: list[dict]