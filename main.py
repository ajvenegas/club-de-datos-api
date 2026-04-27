from fastapi import FastAPI

db_peliculas = [{"titulo": "Matrix", "genero": "Acción", "puntaje":5},
                {"titulo": "Esperando la Carroza", "genero": "Comedia", "puntaje":5}]

generos = ["Acción", "Comedia"]

app = FastAPI()

@app.get("/peliculas")
def obtener_peliculas():
    return db_peliculas

@app.post("/peliculas")
def cargar_una_pelicula(titulo, genero, puntaje):
    if not puntaje.isdigit():
        mensaje_de_error = "El puntaje tiene que ser un número entero."
        return mensaje_de_error
    if not genero in generos:
        mensaje_de_error = "El género indicado no existe."
        return mensaje_de_error
    nueva_pelicula = {"titulo": titulo, "genero": genero, "puntaje": int(puntaje)}
    db_peliculas.append(nueva_pelicula)
    mensaje_de_retorno = "Película guardada correctamente."
    return mensaje_de_retorno

@app.get("/genero")
def obtener_generos():
    return generos

@app.post("/genero")
def añadir_genero(genero):
    generos.append(genero)
    mensaje_de_retorno = "Género cargado correctamente."
    return mensaje_de_retorno