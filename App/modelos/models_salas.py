from sqlalchemy import Column, Integer, String
from App.dao import Base

class SalasDB(Base):
    __tablename__ = "salas"

    id_sala = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    capacidad = Column(Integer, nullable=False)
    estatus = Column(String(1), default="D")
    id_departamento = Column(Integer)