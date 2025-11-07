
from app.core.database import obtener_conexion  

async def insertar_articulo(data: dict, es_relevante: bool, explicacion: str , id_proyecto:int):
    conn = await obtener_conexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT * FROM fn_articulo_insertar(%s, %s, %s, %s, %s, %s, %s, %s);
            """, (
                data.get("doi"),
                data.get("titulo"),
                data.get("resumen"),
                data.get("autor_palabras_clave"),
                data.get("index_palabras_clave"),
                id_proyecto,
                es_relevante,
                explicacion
            ))

            result = await cur.fetchone()
            await conn.commit()

            if not result:
                raise Exception("No se insertó el artículo correctamente.")

            return {
                "id_articulo": result[0],
                "id_articulo_detalle": result[1],
            }

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

async def listar_articulos_db(id_proyecto: int):
    conn = await obtener_conexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT * FROM fn_articulos_listar(%s);
            """, (id_proyecto,))

            rows = await cur.fetchall()

            columnas = [desc[0] for desc in cur.description]
            resultados = [dict(zip(columnas, row)) for row in rows]

            return resultados

    except Exception as e:
        await conn.rollback()
        raise Exception(f"Error al listar artículos del proyecto {id_proyecto}: {e}") from e

    finally:
        await conn.close()




async def articulo_articulo_relevancia_db(id_articulo_detalle: int, es_relevante: bool):

    conn = await obtener_conexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT fn_articulo_detalle_actualizar_relevancia(%s, %s);
            """, (id_articulo_detalle, es_relevante))
            
            result = await cur.fetchone()
            await conn.commit()

            return result and result[0]

    except Exception as e:
        await conn.rollback()
        raise Exception(f"Error en repositorio (actualizar relevancia): {e}") from e

    finally:
        await conn.close()


async def listar_articulos_detallados_db(id_proyecto: int):
    conn = await obtener_conexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT * FROM fn_articulos_detallados_listar(%s);
            """, (id_proyecto,))
            rows = await cur.fetchall()
            columnas = [desc[0] for desc in cur.description]
            resultados = [dict(zip(columnas, row)) for row in rows]
            return resultados
    except Exception as e:
        await conn.rollback()
        raise Exception(f"Error al listar artículos relevantes detallados: {e}") from e
    finally:
        await conn.close()
