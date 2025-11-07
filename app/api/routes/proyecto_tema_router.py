from fastapi import APIRouter, status
from typing import Dict
from app.schemas.base_schema import APIResponse
from app.services.proyecto_tema_service import registrar_proyecto_tema_service

router = APIRouter(prefix="/tema", tags=["Delimitacion Tema"])

@router.post(path="")
async def insertar_tema(data: Dict):
    try:
        contexto = await registrar_proyecto_tema_service(data)
        return APIResponse(
            success=True,
            message="Contexto creado correctamente",
            data=contexto,
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
            message="Error interno al crear el contexto",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


