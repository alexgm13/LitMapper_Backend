
from app.core.database import obtener_conexion  

async def insertar_articulo(data: dict):
    conn = await obtener_conexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT fn_articulo_insertar(%s, %s, %s, %s, %s);
            """, (
                data["doi"],
                data["titulo"],
                data["resumen"],
                data["autor_palabras_clave"],
                data["index_palabras_clave"]
            ))

            result = await cur.fetchone()
            await conn.commit()

            if not result:
                raise Exception("No se insertó el artículo correctamente.")

            return result[0]

    except Exception as e:
        await conn.rollback()
        raise Exception(f"Error al insertar artículo: {e}") from e

    finally:
        await conn.close()


async def insertar_articulo_detalle_db(data: dict):
    conn = await obtener_conexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT fn_articulo_detalle_insertar(%s, %s, %s, %s);
            """, (
                data["id_articulo"],
                data["id_proyecto"],
                data["es_relevante"],
                data["explicacion"]
            ))

            result = await cur.fetchone()
            await conn.commit()

            if not result:
                raise Exception("No se insertó el artículo correctamente.")

            return result[0]

    except Exception as e:
        await conn.rollback()
        raise Exception(f"Error al insertar artículo: {e}") from e

    finally:
        await conn.close()