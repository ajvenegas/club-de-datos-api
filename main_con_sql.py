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
    """)            # Creo la base de datos donde voy a guardar las peliculas
    conn.commit()   # Guardo los cambios
    conn.close()    # Cierro la conexión


app = FastAPI()

@app.get("/peliculas")
def obtener_peliculas():
    conn = sqlite3.connect("letterbox.db")  # Me conecto con la base de datos
    conn.row_factory = sqlite3.Row          # Con esta linea le pido al cursor que me devuelva los resultados en un formato parecido al del diccionario
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM peliculas")       # Busco las peliculas
    res = [dict(row) for row in cursor.fetchall()]  # Paso el formato del resultado final a lista de diccionarios
    conn.close()        # Cierro la conexión
    return res

@app.post("/peliculas")
def cargar_una_pelicula(titulo, genero, puntaje):
    if not puntaje.isdigit():   # Me fijo si el puntaje es un número
        mensaje_de_error = "El puntaje tiene que ser un número entero."
        return mensaje_de_error
    conn = sqlite3.connect("letterbox.db")  # Me conecto a la base de datos
    cursor = conn.cursor()
    cursor.execute("INSERT INTO peliculas (titulo, genero, puntaje) VALUES (?, ?, ?)", (titulo, genero, int(puntaje)))  # Guardo la pelicula
    conn.commit()       # Guardo los cambios
    conn.close()        # Cierro la conexión
    mensaje_de_retorno = "Película cargada correctamente."
    return mensaje_de_retorno

iniciar_db()