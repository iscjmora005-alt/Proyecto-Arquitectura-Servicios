from sqlalchemy import Column, Integer, String, Text, ForeignKey
from pydantic import BaseModel
from typing import Optional
from App.dao import Base

class EquipamientoDB(Base):
    __tablename__ = "equipamiento"

    id_equipamiento = Column(Integer, primary_key=True, index=True, autoincrement=True)
    numeroDeSerie = Column(String(50), unique=True, nullable=False)
    estado = Column(String(50), default="Funcional")
    cantidad = Column(Integer, nullable=False)
    caracteristicas = Column(Text)
    id_sala = Column(Integer, ForeignKey("salas.id_sala"), nullable=False)

# ==========================================
# ESQUEMAS DE VALIDACIÓN (Pydantic)
# ==========================================

# Esquema base con los datos comunes
class EquipamientoBase(BaseModel):
    numeroDeSerie: str
    estado: str = "Funcional"
    cantidad: int
    caracteristicas: Optional[str] = None
    id_sala: int

# 1. Esquema para cuando el administrador hace un POST (Crear)
class EquipamientoCreate(EquipamientoBase):
    pass

# 2. Esquema para responder cuando nos hacen un GET (Lectura)
class EquipamientoResponse(EquipamientoBase):
    id_equipamiento: int

    class Config:
        from_attributes = True

# 3. Esquema para la operación de Reportar Falla (PATCH)
class EquipamientoFalla(BaseModel):
    estado: str
    descripcionFalla: str

# 4. Esquema para la operación de Ajustar Inventario (PATCH)
class EquipamientoAjuste(BaseModel):
    cantidad: int
    motivoAjuste: str