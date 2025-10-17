from fastapi import APIRouter
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse, UsuarioLogin
from app.services.usuario_service import registar_usuario, login_usuario

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/login", response_model=UsuarioResponse)
async def login(data: UsuarioLogin):
    result = await login_usuario(data.model_dump())
    return UsuarioResponse(**result)


@router.post("/registrar", response_model=UsuarioResponse)
async def registrar(usuario: UsuarioCreate):
    result = await registar_usuario(usuario.model_dump())
    return UsuarioResponse(**result)
   
    