from fastapi import APIRouter
from app.services.proyecto_pico_service import generar_terminos_para_todos_pico
from app.schemas.proyecto_pico_schema import PicoInput, PicoOutput
from typing import List

router = APIRouter(prefix="/pico", tags=["Ecuacion_Pico"])

@router.post(path="/generar_terminos_busqueda")
async def generar_terminos_busqueda_endpoint(data: List[PicoInput])-> List[PicoOutput]:
    terminos = await generar_terminos_para_todos_pico(data)
    return terminos
