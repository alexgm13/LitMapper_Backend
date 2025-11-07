from app.core.database import obtener_conexion


async def insertar_proyecto(data: dict):
    conn = await obtener_conexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT * FROM fn_proyecto_insertar(%s, %s, %s);
            """, (
                data["titulo"],
                data["descripcion"],
                data["id_usuario"]
            ))
            result = await cur.fetchone()
            await conn.commit()
            return {
                "id_proyecto": result[0],
                "titulo": result[1],
                "descripcion": result[2]
            }

    except Exception as e:
        await conn.rollback()
        raise Exception(f"Error al insertar proyecto: {e}") from e

    finally:

        await conn.close()