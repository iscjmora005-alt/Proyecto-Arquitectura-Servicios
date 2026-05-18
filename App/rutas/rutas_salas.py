from fastapi import APIRouter
from App.modelos import models_salas

router = APIRouter(
    prefix="/salas",
    tags=["Salas"]
)

@router.get("/")
def listar_salas():
    return {"mensaje": "Listado general de salas (Trabajando en ello...)"}