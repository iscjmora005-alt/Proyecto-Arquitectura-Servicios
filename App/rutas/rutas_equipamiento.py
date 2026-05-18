from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Importamos la conexión a la BD y tus modelos
from App.dao import obtener_bd
from App.modelos import models_equipamiento as modelos

router = APIRouter(
    prefix="/equipamiento",
    tags=["Equipamiento"]
)


# 1. GET: Listado general de Equipamiento
@router.get("/", response_model=List[modelos.EquipamientoResponse])
def listar_equipamiento(bd: Session = Depends(obtener_bd)):
    equipos = bd.query(modelos.EquipamientoDB).all()
    return equipos


# 2. GET: Consultar Equipo por ID
@router.get("/{id_equipamiento}", response_model=modelos.EquipamientoResponse)
def obtener_equipo(id_equipamiento: int, bd: Session = Depends(obtener_bd)):
    equipo = bd.query(modelos.EquipamientoDB).filter(modelos.EquipamientoDB.id_equipamiento == id_equipamiento).first()
    if not equipo:
        raise HTTPException(status_code=404, detail="Equipo no encontrado")
    return equipo


# 3. POST: Registrar nuevo Equipamiento
@router.post("/", response_model=modelos.EquipamientoResponse)
def crear_equipo(equipo: modelos.EquipamientoCreate, bd: Session = Depends(obtener_bd)):
    # Validamos que el número de serie no se repita
    equipo_existente = bd.query(modelos.EquipamientoDB).filter(
        modelos.EquipamientoDB.numeroDeSerie == equipo.numeroDeSerie).first()
    if equipo_existente:
        raise HTTPException(status_code=400, detail="El número de serie ya está registrado en el sistema")

    # Creamos el equipo y lo guardamos
    nuevo_equipo = modelos.EquipamientoDB(**equipo.dict())
    bd.add(nuevo_equipo)
    bd.commit()
    bd.refresh(nuevo_equipo)

    return nuevo_equipo