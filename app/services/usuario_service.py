from app.repositories.usuario_repository import insertar_usuario, obtener_usuario_por_email
from app.core.seguridad import contrasena_hash, contrasena_verficiar, crear_token


async def registar_usuario(data:dict):
     
     try:
      data["contrasena"] = contrasena_hash(data["contrasena"])
      result = await insertar_usuario(data)
      
      if result:
          return {
              "success": True,
              "message": "Usuario registrado correctamente"
            }
      else:
          return {
              "success": False,
              "message": "Error al registrar usuario"
            }
     except Exception as e:
          return {
            "success": False,
            "message": f"Error en el servidor: {str(e)}",
          }


async def login_usuario(data:dict):
   
    try:
        usuario = await obtener_usuario_por_email(data["email"])
        if not usuario:
            return {
                "success": False,
                "message": "Usuario no encontrado"
            }

        print(data["contrasena"])
        if not contrasena_verficiar(data["contrasena"], usuario["contrasena"]):
            return {
                "success": False,
                "message": "Contraseña incorrecta"
            }

        token = crear_token({"sub": usuario["email"]})

        return {
            "success": True,
            "message": "Inicio de sesión exitoso",
            "usuario": {
                "id_user": usuario["id_user"],
                "email": usuario["email"],
                "nombre": usuario["nombre"],
                "id_rol": usuario["id_rol"],
                "rol": usuario["rol"]
            },
           "token":{
                "access_token": token,
                "token_type": "bearer",
            }
        }

    except Exception as e:
        return {
            "success": False,
            "message": f"Error en login: {str(e)}",
        }