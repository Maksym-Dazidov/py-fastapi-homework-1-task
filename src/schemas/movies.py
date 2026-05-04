from pydantic import BaseModel


class MovieDetailResponseSchema(BaseModel):
    id: int
    name: str
    date: datetime.date
    score: float
    genre: str
    overview: str
    crew: List[str]
    orig_title: str
    status: str
    orig_lang: str
    budget: float
    revenue: float
    country: str

    model_config = {
        "from_attributes": True
    }

class MovieListResponseSchema(BaseModel):
    movies: List[MovieDetailResponseSchema]
    total_items: int
    total_pages: int
    prev_page: str | None
    next_page: str | None
