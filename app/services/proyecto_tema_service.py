from typing import Dict
from app.repositories.proyecto_tema_repository import listar_proyecto_tema, registrar_proyecto_tema


async def listar_proyecto_tema_service(data: Dict):
    tema = await listar_proyecto_tema(data)
    return tema

async def registrar_proyecto_tema_service(data: Dict):
    tema = await registrar_proyecto_tema(data)
    return tema