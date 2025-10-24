from fastapi import APIRouter
from app.schemas.proyecto_schema import ProyectoInsertar
from app.services.proyecto_service import insertar_proyecto_service


router = APIRouter(prefix="/proyecto", tags=["Proyecto"])

@router.post(path="/insertar")
async def insertar_proyecto(proyecto: ProyectoInsertar):
    proyecto = await insertar_proyecto_service(proyecto.model_dump())
    return proyecto
