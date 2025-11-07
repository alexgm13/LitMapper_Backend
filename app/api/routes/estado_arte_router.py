from fastapi import APIRouter, status
from typing import List, Dict
from app.schemas.base_schema import APIResponse
from app.services.estado_arte import generar_sota_service
from app.schemas.estado_arte import SoTA

router = APIRouter(prefix="/sota")

@router.post(path="/sota", response_model=APIResponse)
async def generar_sota_endpoint(sota: SoTA):
    try:

        sota = await generar_sota_service(sota.articulos, sota.contexto.area_general, sota.contexto.tema_especifico, sota.contexto.problema_investigacion, sota.contexto.metodologia_enfoque)
        return APIResponse(
            success=True,
            message="Detalles de los articulos insertados correctamente",
            data = sota,
            meta=None,
            status_code=status.HTTP_201_CREATED
        )
    except ValueError as e:
        return APIResponse(
            success=False,
            message="Error de validación",
            errors=str(e),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return APIResponse(
            success=False,
            message="Error interno al insertar los articulos",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
