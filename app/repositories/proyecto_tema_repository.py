from app.core.database import obtener_conexion



async def insertar_contexto(data: dict):
    conn = await obtener_conexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute("""
                SELECT * FROM fn_contexto_insertar(%s, %s, %s, %s, %s);
            """, (
                data["id_proyecto"],
                data["area_general"],
                data["tema_especifico"],
                data["problema_investigacion"],
                data["metodologia"]
            ))
            result = await cur.fetchone()
            await conn.commit()

            if result:
                return {
                    "id_contexto": result[0],
                    "area_general": result[1],
                    "tema_especifico": result[2],
                    "problema_investigacion": result[3],
                    "metodologia": result[4]
                }
                   
            else:
                return None
    except Exception as e:
        await conn.rollback()
        raise e
    finally:
        await conn.close()

async def obtener_contexto_por_id(id_contexto: int):
 
    conn = await obtener_conexion()
    try:
        async with conn.cursor() as cur:
            await cur.execute(
                "SELECT * FROM fn_contexto_listar_id(%s);",
                (id_contexto,)
            )
            row = await cur.fetchone()
           
            if not row:
                return None

            return {
                "area_general": row[0],
                "tema_especifico": row[1],
                "problema_investigacion": row[2],
                "metodologia": row[3],
            }
    except Exception as e:
        raise e
    finally:
        await conn.close()