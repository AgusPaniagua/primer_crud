from db import Base, engine
from crud_persona import *
from fastapi import FastAPI, HTTPException
from persona import Persona

Base.metadata.create_all(engine)

app = FastAPI(title="API de Personas")

@app.get("/personas")
def get_personas():
    personas = ver_personas()
    resultado = []
    for p in personas:
        resultado.append({
            "id":p.id,
            "nombre":p.nombre,
            "edad":p.edad,
            "correo_electronico": p.correo_electronico
        })
    return resultado

@app.post("/personas")
def post_persona(persona: dict):
    crear_persona(persona["nombre"],persona["edad"],persona["correo_electronico"])
    return{"mensaje":"Persona creada correctamente"}


@app.put("/personas{persona_id}")
def put_persona(persona_id: int, persona: dict):
    try:
        modificar_persona(persona_id, persona["nombre"],persona["edad"],persona["correo_electronico"])
        return {"mensaje": "Persona modificada correctamente"}
    except Exception:
        raise HTTPException(status_code=404, detail="Persona no encontrada")

@app.delete("/personas/{persona.id}")
def delete_persona(persona_id: int):
    try:
        eliminar_persona(persona_id)
        return {"mensaje":"Persoan eliminada correctamente"}
    except Exception:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
