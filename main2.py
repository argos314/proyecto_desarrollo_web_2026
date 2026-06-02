import sqlite3 
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Vanilla CRUD con FastAPI")
DB_NAME = "database.db"

def init_db():
    # El bloque 'with' asegura el cierre de la conexión de forma segura
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                completada INTEGER DEFAULT 0
            )
        """)
        conn.commit()

# Se ejecuta al leer el archivo para garantizar que la DB esté lista
init_db()

class TareaBase(BaseModel):
    titulo: str

class TareaResponse(BaseModel):
    id: int
    titulo: str
    completada: bool

@app.get("/api/tareas", response_model=List[TareaResponse])
def obtener_tareas():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo, completada FROM tareas")
        filas = cursor.fetchall()
        # Convertimos el entero (0 o 1) de SQLite a Booleano de Python en la lista de comprensión
        return [{"id": f[0], "titulo": f[1], "completada": bool(f[2])} for f in filas]

@app.post("/api/tareas", response_model=TareaResponse)
def crear_tarea(tarea: TareaBase):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Usamos tuplas con '?' para prevenir inyecciones SQL (SQL Injection)
        cursor.execute("INSERT INTO tareas (titulo) VALUES (?)", (tarea.titulo,))
        conn.commit()
        return {"id": cursor.lastrowid, "titulo": tarea.titulo, "completada": False}
    
@app.put("/api/tareas/{id}/completar")
def alternar_tarea(id: int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # Buscamos primero el estado actual del registro
        cursor.execute("SELECT completada FROM tareas WHERE id = ?", (id,))
        fila = cursor.fetchone()
        if not fila:
            raise HTTPException(status_code=404, detail="No encontrada")
        
        # Alternamos el bit (0 se vuelve 1, 1 se vuelve 0)
        nuevo_estado = 0 if fila[0] == 1 else 1
        cursor.execute("UPDATE tareas SET completada = ? WHERE id = ?", (nuevo_estado, id))
        conn.commit()
        return {"status": "success", "completada": bool(nuevo_estado)}

@app.delete("/api/tareas/{id}")
def eliminar_tarea(id: int):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
        # Controlamos si la fila realmente existía para ser borrada
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="No encontrada")
        conn.commit()
        return {"status": "deleted"}
    
    app.mount("/", StaticFiles(directory="static", html=True), name="static")