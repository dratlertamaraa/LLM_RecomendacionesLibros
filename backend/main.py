from fastapi import FastAPI , HTTPException
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

app = FastAPI()

@app.get("/health")
def health():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "ok", "database": "ok"}



libros = [
    {"id": 1, "titulo": "Libro1", "anio": 1999},
    {"id": 2, "titulo": "Libro2", "anio": 2017},
]


@app.get("/books")
def listar_libros():
    return libros

@app.get("/books/{book_id}")
def obtener_libro(book_id: int):
    for libro in libros:
        if libro["id"] == book_id:
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")