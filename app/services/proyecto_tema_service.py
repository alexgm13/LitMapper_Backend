from typing import Dict
from app.repositories.proyecto_tema_repository import insertar_contexto




async def registrar_proyecto_tema_service(data: Dict):
    contexto = await insertar_contexto(data)
    if not contexto:
        raise ValueError("No se pudo insertar correctamente el contexto")
    return contexto