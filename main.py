from db import Base, engine
from crud_persona import *

Base.metadata.create_all(engine)

#crear_persona("nico",20,"nikita@gmail.com")
ver_personas()
