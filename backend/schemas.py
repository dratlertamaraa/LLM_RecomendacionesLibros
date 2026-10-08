from datetime import date
from pydantic import BaseModel, ConfigDict


class BookRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    original_title: str | None = None
    published_date: date | None = None
    page_count: int | None = None
    cover_url: str | None = None