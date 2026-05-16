from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

mis_mascotas = {
    1:{
        "nombre":"baly",
        "raza": "perro"
    },
      2:{
        "nombre":"soruyo",
        "raza":"gato"
    },  
    3:{
        "nombre":"coco",
        "raza":"raton"
    }, 
    4:{
        "nombre":"pepe",
        "raza":"cotorro"
    }
}
@app.get("/")
def read_root():
    return {"mensaje": "Hola mundo"}

@app.get("/mascotas/{id}")
def detalle_mascota(id: int, response:Response):
    #consultar base de datos
    mascota = mis_mascotas.get(id, None)
    print(mascota)
    if not mascota:
        mascota={} 
        response.status_code = status.HTTP_404_NOT_FOUND    
    return mascota


class Mascota(BaseModel): 
    id:int
    nombre:str
    raza:str

@app.post("/mascotas/")
def registra_mascota(mascota:Mascota):
    mis_mascotas[mascota.id] = mascota