from typing import Dict
from app.repositories.proyecto_tema_repository import insertar_contexto




async def registrar_proyecto_tema_service(data: Dict):
    contexto = await insertar_contexto(data)
    return contexto