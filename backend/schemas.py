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
    description: str | None = None
    isbn_13: str | None = None
class BookCreate(BaseModel):
   
    title: str
    original_title: str | None = None
    published_date: date | None = None
    page_count: int | None = None
    cover_url: str | None = None
    description: str | None = None
    isbn_13: str | None = None
    language: str | None = None
    series_name: str | None = None
    series_number: int | None = None
    open_library_id: str | None = None
    