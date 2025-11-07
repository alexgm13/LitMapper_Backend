from fastapi import HTTPException, status
from app.repositories.usuario_repository import insertar_usuario, obtener_usuario_por_email
from app.core.seguridad import contrasena_hash, contrasena_verficiar, crear_token
from app.schemas.base_schema import APIResponse

async def registar_usuario(data:dict):
      
      if not data["email"]:
          raise ValueError("El email es obligatorio")
      if not data["contrasena"]:
          raise ValueError("La contrasena es obligatoria")
      if not data["id_rol"]:
          raise ValueError("El id del rol es obligatorio")
      if not data["nombre"]:
          raise ValueError("El nombre es obligatorio")
      if not data["genero"]:
          raise ValueError("El genero es obligatorio")
      if not data["fecha_nacimiento"]:
          raise ValueError("La fecha de nacimiento es obligatoria")
      
      data["contrasena"] = contrasena_hash(data["contrasena"])
      result = await insertar_usuario(data)
      return result
     

      
      

async def login_usuario(data: dict):
        
        email = data.get("email")
        contrasena = data.get("contrasena")

        if not email:
           raise ValueError("Email requerido")
        if not contrasena:
           raise ValueError("Contraseña requerida")
            
        usuario = await obtener_usuario_por_email(email)

        if not usuario:
            raise ValueError("Usuario no encontrado en la BD")

        if not contrasena_verficiar(contrasena, usuario["contrasena"]):
           raise ValueError("Contraseña invalida")

        token = crear_token({"sub": usuario["email"]})

        return {
            "usuario": usuario,
            "token": {
                "access_token": token,
                "token_type": "bearer",
            }
        }
  