from persona import Persona
from db import session

def crear_persona(nombre, edad, correo):
    nueva_persona = Persona(nombre=nombre, edad=edad,correo_electronico=correo)
    session.add(nueva_persona)
    session.commit()

def modificar_persona(persona_id,nuevo_nombre, nueva_edad, nuevo_correo):
    persona=session.get(Persona,persona_id)
    if persona:
        persona.nombre=nuevo_nombre
        persona.edad=nueva_edad
        persona.correo_electronico=nuevo_correo
        session.commit()
    else:
        print(f"No se encuentra la persona con ID {persona_id}")


def ver_personas():
    return session.query(Persona).all()

def eliminar_persona(persona_id):
    persona=session.get(Persona,persona_id)
    if persona:
        session.delete(persona)
        session.commit()
    else:
        print(f"No se encuentra la persona con ID {persona_id}")