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
            await conn.commit() 

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
                    contrasena,
                    nombre_usuario,
                    nombre_rol
                ) = result
                return {
                    "id_user": id_usuario,
                    "email": email_usuario,
                    "contrasena": contrasena, 
                    "nombre": nombre_usuario,  
                    "nombre_rol": nombre_rol
                } 
         
            return None 

    except Exception as e:
        await conn.rollback()
        raise Exception(f"Error al obtener usuario: {e}")

    finally:
        if not conn.closed:
            await conn.close()
