from app.core.database import obtener_conexion

async def insertar_usuario(data: dict):
    conn = await obtener_conexion()
    async with conn.cursor() as cur:
        try:
            await cur.execute(
                """
                SELECT * FROM fn_usuario_registrar(%s, %s, %s, %s, %s, %s);
                """,
                (
                    data["email"],
                    data["contrasena"],  
                    data["nombre"],
                    data["genero"],
                    data["fecha_nacimiento"],
                    data["id_rol"],
                ),
            )

            result = await cur.fetchone()
            if result:
                await conn.commit() 
                email_usuario, hash_guardado = result
                return {
                    "email": email_usuario,
                    "contrasena": hash_guardado
                }
            
            return None

        except Exception as e:
            await conn.rollback()
            raise Exception(f"Error al registrar usuario: {e}")

        finally:
            if not conn.closed:
                await conn.close()

                

async def obtener_usuario_por_email(email: str):
    conn = await obtener_conexion()
    try:
        async with conn.cursor() as cur:
        
            await cur.execute("SELECT * FROM fn_usuario_autenticar(%s);", (email,))
            result = await cur.fetchone()

            if result:
                (
                    id_usuario,
                    email_usuario,
                    hash_guardado,
                    nombre_usuario,
                    id_rol_usuario,
                    rol_descripcion 
                ) = result
                return {
                    "id_user": id_usuario,
                    "email": email_usuario,
                    "contrasena": hash_guardado, 
                    "nombre": nombre_usuario,  
                    "id_rol": id_rol_usuario,
                    "rol": rol_descripcion
                }
         
            return None 

    except Exception as e:
        await conn.rollback()
        raise Exception(f"Error al obtener usuario: {e}")

    finally:
        if not conn.closed:
            await conn.close()
