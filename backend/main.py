from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import text, select
from sqlalchemy.orm import Session

from database import engine, SessionLocal
from models import Book
from schemas import BookRead, BookCreate

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "ok", "database": "ok"}

@app.get("/books", response_model=list[BookRead])
def listar_libros(db: Session = Depends(get_db)):
    return db.scalars(select(Book)).all()


@app.get("/books/{book_id}", response_model=BookRead)
def obtener_libro(book_id: int, db: Session = Depends(get_db)):
    libro = db.get(Book, book_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro


@app.post("/books", response_model=BookRead, status_code=201)
def crear_libro(datos: BookCreate, db: Session = Depends(get_db)):
    libro = Book(**datos.model_dump())
    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro


@app.post("/books", response_model=BookRead, status_code=201)
def crear_libro(datos: BookCreate, db: Session = Depends(get_db)):
    libro = Book(**datos.model_dump())
    db.add(libro)
    db.commit()
    db.refresh(libro)
    return libro