from fastapi import APIRouter

router = APIRouter(
    prefix="/equipamiento",
    tags=["Equipamiento"]
)

@router.get("/")
def listar_equipamiento():
    # Aquí programarás tu consulta de inventario
    return {"mensaje": "Listado general de equipamiento (Pendiente conexión BD)"}
