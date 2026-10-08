from datetime import date
from sqlalchemy import String, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    original_title: Mapped[str | None] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text)
    published_date: Mapped[date | None]
    page_count: Mapped[int | None]
    cover_url: Mapped[str | None] = mapped_column(Text)
    isbn_13: Mapped[str | None] = mapped_column(String(13))
    language: Mapped[str | None] = mapped_column(String(10))
    series_name: Mapped[str | None] = mapped_column(String(255))
    series_number: Mapped[int | None]
    open_library_id: Mapped[str | None] = mapped_column(String(50))
    fecha_de_carga: Mapped[date] = mapped_column(server_default=func.current_date())
    
class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))