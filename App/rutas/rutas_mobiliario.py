from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from App.dao import obtener_bd
from App.modelos import models_mobiliario as modelos
from App.modelos import models_salas

router = APIRouter(prefix="/mobiliario", tags=["Mobiliario"])


# 1. POST: Registrar Mobiliario
@router.post("/")
def registrar_mobiliario(mueble: modelos.MobiliarioCreate, bd: Session = Depends(obtener_bd)):
    # Validamos que los campos de texto no vengan vacíos
    if not mueble.nombre or not mueble.descripcion or not mueble.tipo:
        raise HTTPException(status_code=400, detail="Los campos de texto no pueden estar vacíos")

    # Comprobamos que el id_sala exista en la tabla Salas
    sala = bd.query(models_salas.SalasDB).filter(models_salas.SalasDB.id_sala == mueble.id_sala).first()
    if not sala:
        raise HTTPException(status_code=400, detail="Error: El id_sala proporcionado no existe en el sistema")

    nuevo_mueble = modelos.MobiliarioDB(**mueble.model_dump())
    bd.add(nuevo_mueble)
    bd.commit()
    bd.refresh(nuevo_mueble)

    return {
        "código": 201,
        "mensaje": "Mobiliario registrado con éxito",
        "id_mobiliario": nuevo_mueble.id_mobiliario
    }


# 2. PATCH: Actualizar Ficha Técnica
@router.patch("/{id_mobiliario}/ficha-tecnica")
def actualizar_ficha_tecnica(id_mobiliario: int, ficha: modelos.MobiliarioFichaTecnica,
                             bd: Session = Depends(obtener_bd)):
    mueble_db = bd.query(modelos.MobiliarioDB).filter(modelos.MobiliarioDB.id_mobiliario == id_mobiliario).first()

    if not mueble_db:
        raise HTTPException(status_code=404, detail="Error: Mueble no encontrado")

    # Actualizamos los campos
    mueble_db.descripcion = ficha.descripcion
    mueble_db.tipo = ficha.tipo
    bd.commit()

    return {
        "código": 200,
        "mensaje": "Ficha técnica actualizada correctamente"
    }


# 3. GET: Listado general de Mobiliario
@router.get("/")
def listar_mobiliario(bd: Session = Depends(obtener_bd)):
    muebles_db = bd.query(modelos.MobiliarioDB).all()

    return {
        "código": 200,
        "mensaje": "Listado de mobiliario recuperado",
        "mobiliario": muebles_db
    }


# 4. GET: Consultar Mobiliario por Id
@router.get("/{id_mobiliario}")
def consultar_mobiliario(id_mobiliario: int, bd: Session = Depends(obtener_bd)):
    mueble_db = bd.query(modelos.MobiliarioDB).filter(modelos.MobiliarioDB.id_mobiliario == id_mobiliario).first()

    if not mueble_db:
        raise HTTPException(status_code=404, detail="Error: Mueble no encontrado")

    return {
        "código": 200,
        "mensaje": "Mueble consultado correctamente",
        "mueble": mueble_db
    }


# 5. DELETE: Eliminar Mobiliario
@router.delete("/{id_mobiliario}")
def eliminar_mobiliario(id_mobiliario: int, bd: Session = Depends(obtener_bd)):
    mueble_db = bd.query(modelos.MobiliarioDB).filter(modelos.MobiliarioDB.id_mobiliario == id_mobiliario).first()

    if not mueble_db:
        raise HTTPException(status_code=404, detail="Error: Mueble no encontrado")

    bd.delete(mueble_db)
    bd.commit()

    return {
        "código": 200,
        "mensaje": "Mobiliario eliminado con éxito"
    }