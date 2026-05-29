from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from App.dao import Base

# 1. Modelo de SQLAlchemy (Tabla en MySQL)
class MobiliarioDB(Base):
    __tablename__ = "mobiliario"

    id_mobiliario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=False)
    tipo = Column(String(50), nullable=False)
    id_sala = Column(Integer, nullable=False)

# 2. Esquema Pydantic para el POST (Crear mobiliario)
class MobiliarioCreate(BaseModel):
    nombre: str
    descripcion: str
    tipo: str
    id_sala: int

# 3. Esquema Pydantic para el PATCH (Actualizar ficha técnica)
class MobiliarioFichaTecnica(BaseModel):
    descripcion: str
    tipo: str
