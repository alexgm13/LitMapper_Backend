from app.repositories.proyecto_repository import insertar_proyecto
from typing import Dict

async def insertar_proyecto_service(data: Dict):
    proyecto = await insertar_proyecto(data)
    return proyecto


