from fastapi import FastAPI
import sqlite3

def iniciar_db():
    conn = sqlite3.connect("letterbox.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS peliculas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        genero TEXT,
        puntaje INTEGER)
    """)
    conn.commit()
    conn.close()


app = FastAPI()

@app.get("/peliculas")
def obtener_peliculas():
    conn = sqlite3.connect("letterbox.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM peliculas")
    res = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return res

@app.post("/peliculas")
def cargar_una_pelicula(titulo, genero, puntaje):
    if not puntaje.isdigit():
        mensaje_de_error = "El puntaje tiene que ser un número entero."
        return mensaje_de_error
    conn = sqlite3.connect("letterbox.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO peliculas (titulo, genero, puntaje) VALUES (?, ?, ?)")
    conn.commit()
    conn.close()
    mensaje_de_retorno = "Película cargada correctamente."
    return mensaje_de_retorno

iniciar_db()