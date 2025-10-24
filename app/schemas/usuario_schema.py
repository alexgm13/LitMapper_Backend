from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional




class Usuario(BaseModel):
    id_user: Optional[int] = None
    email: EmailStr
    contrasena: str
    id_rol: int
    nombre: str
    estado: str


class UsuarioCreate(BaseModel):
    email: EmailStr
    contrasena: str
    id_rol: int
    nombre: str
    genero: str
    fecha_nacimiento: date


class UsuarioLogin(BaseModel):
    email: EmailStr
    contrasena: str




class UsuarioBase(BaseModel):
    id_user: Optional[int] = None
    email: EmailStr
    nombre: Optional[str] = None
    id_rol: Optional[int] = None
    rol: Optional[str] = None 


class Token (BaseModel):
    access_token: str
    token_type: str


class UsuarioResponse(BaseModel):
    success: bool
    message: str
    token: Optional[Token] = None
    usuario: Optional[UsuarioBase] = None
    

