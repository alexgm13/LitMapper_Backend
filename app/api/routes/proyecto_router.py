from fastapi import APIRouter, status
from app.services.proyecto_service import insertar_proyecto_service
from typing import Dict
from app.schemas.base_schema import APIResponse


router = APIRouter(prefix="/proyecto", tags=["Proyecto"])

@router.post(path="/")
async def insertar_proyecto(proyecto: Dict):

    try:
        proyecto = await insertar_proyecto_service(proyecto)
        return APIResponse(
            success=True,
            message="Proyecto creado correctamente",
            data=proyecto,
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
            message="Error interno al crear el proyecto",
            errors=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

