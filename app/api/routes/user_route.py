from fastapi import APIRouter
from fastapi import Depends
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse, UsuarioLogin
from fastapi.security import OAuth2PasswordBearer
from app.services.usuario_service import registar_usuario, login_usuario
from app.core.seguridad import obtener_usuario_actual

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(path="/login", response_model=UsuarioResponse)
async def login(data: UsuarioLogin):
    result = await login_usuario(data.model_dump())
    return UsuarioResponse(**result)


@router.post(path="/registrar", response_model=UsuarioResponse)
async def registrar(usuario: UsuarioCreate):
    result = await registar_usuario(usuario.model_dump())
    return UsuarioResponse(**result)
   
