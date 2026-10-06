from fastapi import FastAPI , HTTPException

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}



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