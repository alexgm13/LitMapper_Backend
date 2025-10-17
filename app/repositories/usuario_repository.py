from app.core.database import obtener_conexion

async def insertar_usuario(data: dict):
    conn = await obtener_conexion()
    async with conn.cursor() as cur:
        try:
            await cur.execute(
                """
                CALL usp_usuarios_insertar(%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    data["email"],
                    data["contrasena"],
                    data["id_rol"],
                    data["nombre"],
                    data["genero"],
                    data["fecha_nacimiento"],
                    None,  # o_email (OUT)
                    None   # o_contrasena (OUT)
                )
            )

            result = await cur.fetchone()
            if result:
                await conn.commit()
                return True

        except Exception as e:
            await conn.rollback()
            return False

        finally:
            if not conn.closed:
                await conn.close()

                

async def obtener_usuario_por_email(email: str):
    conn = await obtener_conexion()
    async with conn.cursor() as cur:
        try:
            await cur.execute(
                "CALL usp_usuarios_login(%s, %s, %s, %s, %s, %s)",
                (email, None, None, None, None, None)
            )

            result = await cur.fetchone()
            if result:
                o_id_user, o_email, o_contrasena, o_id_rol, o_nombre = result
                return {
                    "id_user": o_id_user,
                    "email": o_email,
                    "contrasena": o_contrasena,
                    "id_rol": o_id_rol,
                    "nombre": o_nombre
                }
            return None

        except Exception as e:
            await conn.rollback()
            raise Exception(f"Error al obtener usuario: {e}")
        finally:
            if not conn.closed:
                await conn.close()
