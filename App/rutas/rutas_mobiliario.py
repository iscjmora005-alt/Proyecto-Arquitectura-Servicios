from fastapi import APIRouter

router = APIRouter(
    prefix="/mobiliario",
    tags=["Mobiliario"]
)

@router.get("/")
def listar_mobiliario():
    return {"mensaje": "Listado general de mobiliario (Trabajando en ello...)"}