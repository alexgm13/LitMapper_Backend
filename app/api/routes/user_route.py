from fastapi import APIRouter, status, HTTPException
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse, UsuarioLogin
from app.services.usuario_service import registar_usuario, login_usuario
from app.schemas.base_schema import APIResponse
from typing import Dict

router = APIRouter(prefix="/users", tags=["Autenticacion"])


@router.post(path="/login", response_model=APIResponse)
async def autenticar_usuario_endpoint(data: Dict):
    try:
        result = await login_usuario(data)
        return APIResponse(
            success=True,
            message="Inicio de sesión exitoso",
            data=result,
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


@router.post(path="/registrar", response_model=APIResponse)
async def registrar_usuario_endpoint(usuario: Dict):
    try:
        result = await registar_usuario(usuario)
        return APIResponse(
            success=True,
            message="Inicio de sesión exitoso",
            data=result,
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
            message=f"Error interno en login",
            errors=str(e),
            data=None,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    
   
