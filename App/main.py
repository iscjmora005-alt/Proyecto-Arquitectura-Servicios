from fastapi import FastAPI
from App.rutas import rutas_salas, rutas_equipamiento, rutas_mobiliario

app = FastAPI(
    title="API de Gestión de Salas y Equipamiento - ITESZ",
    version="1.0.0"
)

app.include_router(rutas_salas.router)
app.include_router(rutas_equipamiento.router)

app.include_router(rutas_mobiliario.router)

@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "Bienvenido al Sistema de Gestión de Salas del ITESZ"}