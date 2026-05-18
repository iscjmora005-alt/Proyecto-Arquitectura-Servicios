from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Importamos la conexión a la BD y tus modelos combinados
from App.dao import obtener_bd
from App.modelos import models_salas as modelos

router = APIRouter(prefix="/salas", tags=["Gestion de salas"])

# 1. POST: Crear Sala
@router.post("/")
def crear_sala(sala: modelos.SalaCreate, bd: Session = Depends(obtener_bd)):
    # Tu regla de negocio intacta
    if sala.capacidad <= 0:
        raise HTTPException(status_code=400, detail="La capacidad debe ser mayor a 0")
    
    # Magia de BD: Convertimos tu esquema Pydantic al modelo SQLAlchemy y lo guardamos
    nueva_sala = modelos.SalasDB(**sala.model_dump()) 
    bd.add(nueva_sala)
    bd.commit()
    bd.refresh(nueva_sala) # Esto nos devuelve el ID que MySQL le asignó automáticamente

    return {
        "código": 201, 
        "mensaje": "Sala creada exitosamente", 
        "id_sala": nueva_sala.id_sala # ¡Aquí ya es el ID real!
    }

# 2. GET: Consultar Sala por ID
@router.get("/{id_sala}")
def consultar_sala(id_sala: int, bd: Session = Depends(obtener_bd)):
    # Buscamos en la BD de verdad
    sala_db = bd.query(modelos.SalasDB).filter(modelos.SalasDB.id_sala == id_sala).first()
    
    # Tu cláusula de guarda
    if not sala_db:
        raise HTTPException(status_code=404, detail="Error: La sala consultada no existe en el sistema")

    return {
        "código": 200,
        "mensaje": "Sala encontrada con éxito",
        "sala": sala_db
    }

# 3. GET: Listado general
@router.get("/")
def consultar_salas(bd: Session = Depends(obtener_bd)): 
    # Traemos todas las salas de la tabla
    salas_db = bd.query(modelos.SalasDB).all()
    
    return {
        "código": 200,
        "mensaje": "Listado de salas recuperado exitosamente",
        "salas": salas_db
    }

# 4. PATCH: Cambiar Estatus
@router.patch("/{id_sala}/estatus")
def cambiar_estatus(id_sala: int, actualizacion: modelos.SalaUpdateEstatus, bd: Session = Depends(obtener_bd)):
    sala_db = bd.query(modelos.SalasDB).filter(modelos.SalasDB.id_sala == id_sala).first()
    
    if not sala_db:
        raise HTTPException(status_code=404, detail="Error: La sala no existe")
    
    # Actualizamos y guardamos en BD
    setattr(sala_db, "estatus", actualizacion.estatus)
    bd.commit()
    
    return {
        "código": 200,
        "mensaje": f"Estatus de la sala actualizado correctamente a '{actualizacion.estatus}'"
    }

# 5. DELETE: Eliminar Sala
@router.delete("/{id_sala}")
def eliminar_sala(id_sala: int, bd: Session = Depends(obtener_bd)):
    sala_db = bd.query(modelos.SalasDB).filter(modelos.SalasDB.id_sala == id_sala).first()
    
    if not sala_db:
        raise HTTPException(status_code=404, detail="Error: La sala no existe")
        
    # Borramos de la BD
    bd.delete(sala_db)
    bd.commit()
    
    return {
        "código": 200,
        "mensaje": "Sala eliminada con éxito. (Advertencia: Se eliminó en cascada su equipamiento y mobiliario asociado)"
    }