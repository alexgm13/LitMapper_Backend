
from app.core.database import obtener_conexion  
async def insertar_articulos(articulos: list[dict], id_proyecto: int):
    conn = await obtener_conexion()
    async with conn.cursor() as cur:
        try:
            query = """
                INSERT INTO articulo (titulo, autor, anio, doi, fuente, id_proyecto)
                VALUES (%s, %s, %s, %s, %s, %s)
            """

            # preparamos los valores
            valores = [
                (
                    art.get("titulo"),
                    art.get("autor"),
                    art.get("anio"),
                    art.get("doi"),
                    art.get("fuente"),
                    id_proyecto,
                )
                for art in articulos
            ]

            await cur.executemany(query, valores)
            await conn.commit()
            return {"mensaje": f"{len(articulos)} artículos guardados correctamente."}

        except Exception as e:
            await conn.rollback()
            raise Exception(f"Error al insertar artículos: {e}")

        finally:
            await conn.close()
