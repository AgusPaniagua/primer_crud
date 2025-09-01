from sqlalchemy import Column, Integer, String
from db import Base

class Persona(Base):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad = Column(Integer)
    correo_electronico = Column(String)
    