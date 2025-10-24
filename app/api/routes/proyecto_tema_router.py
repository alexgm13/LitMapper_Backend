from fastapi import APIRouter
from app.schemas.proyecto_tema_schema import TemaListar, TemaRegistrar
from app.services.proyecto_tema_service import listar_proyecto_tema_service,registrar_proyecto_tema_service

router = APIRouter(prefix="/tema", tags=["Delimitacion Tema"])

@router.post(path="/registar")
async def registrar_tema(data: TemaRegistrar):
    tema = await registrar_proyecto_tema_service(data.model_dump())
    return tema

@router.post(path="/listar")
async def listar_tema(data: TemaListar):
    tema = await listar_proyecto_tema_service(data.model_dump())
    return tema