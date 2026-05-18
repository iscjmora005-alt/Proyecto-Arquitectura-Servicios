from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from typing import Literal
from App.dao import Base 

class SalasDB(Base):
    __tablename__ = "salas"

    id_sala = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    capacidad = Column(Integer, nullable=False)
    estatus = Column(String(1), default="D")
    id_departamento = Column(Integer)

# ==========================================
# ESQUEMAS DE VALIDACIÓN (Pydantic)
# ==========================================

# 1. Esquema para la operación de Cambiar Estatus (PATCH)
class SalaUpdateEstatus(BaseModel):
    estatus: Literal["D", "M", "O"]

# 2. Esquema para cuando se hace un POST (Crear) o un PUT (Modificación Completa)
class SalaCreate(BaseModel):
    nombre: str
    capacidad: int
    estatus: Literal["D", "M", "O"]
    id_departamento: int