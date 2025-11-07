from fastapi import APIRouter,status
from app.services.proyecto_pico_service import generar_terminos_para_todos_pico,generar_ecuacion_busqueda
from typing import List, Dict
from app.schemas.base_schema import APIResponse

router = APIRouter(prefix="/pico", tags=["Ecuacion Pico"])

@router.post(path="/terminos")
async def generar_terminos_busqueda_endpoint(data: List[Dict]):

    try:
        terminos = await generar_terminos_para_todos_pico(data)
        return APIResponse(
            success=True,
            message="Se crearon los terminos exitosamente",
            data=terminos,
            status_code=status.HTTP_200_OK
        )
    except ValueError as e:
        return APIResponse(
            success=False,
            message="Error de validación",
            errors=str(e),
            data=None,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return APIResponse(
            success=False,
            message=f"Error interno en autenticar",
            errors=str(e),
            data=None,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@router.post(path="/ecuacion")
async def generar_ecuacion_busqueda_endpoint(data: List[Dict]):
    try:
        ecuacion = await generar_ecuacion_busqueda(data)
        return APIResponse(
            success=True,
            message="Inicio de sesión exitoso",
            data=ecuacion,
            status_code=status.HTTP_200_OK
        )
    except ValueError as e:
        return APIResponse(
            success=False,
            message="Error de validación",
            errors=str(e),
            data=None,
            status_code=status.HTTP_400_BAD_REQUEST
        )
    except Exception as e:
        return APIResponse(
            success=False,
            message=f"Error interno en generacion",
            errors=str(e),
            data=None,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
