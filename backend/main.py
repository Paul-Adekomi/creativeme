from pydantic import BaseModel


class MatchRequest(BaseModel):
    query: str
    top_k: int = 5


class MatchResult(BaseModel):
    name: str
    title: str
    category: str
    price: float
    availability: bool
    location: str
    description: str
    match_score: float
