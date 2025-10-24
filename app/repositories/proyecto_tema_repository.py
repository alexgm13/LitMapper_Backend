from app.core.database import obtener_conexion
from app.models.proyecto_tema_modelo import DelimitacionTema


async def registrar_proyecto_tema(data: dict) -> DelimitacionTema:
    conn = await obtener_conexion()
    async with conn.cursor() as cur:
        try:
            await cur.execute(
                """
                SELECT * FROM fn_proyecto_delimitacion_registrar(%s,%s, %s, %s, %s);
                """,
                (
                    data["area_general"],
                    data["tema_especifico"],
                    data["problema_investigacion"],
                    data["metodologia_enfoque"],
                    data["id_proyecto"]
                ),
            )

            result = await cur.fetchone()
            if result:
                await conn.commit() 
                t_id_delimitacion, t_area_general, t_tema_especifico, t_problema_investigacion, t_metodologia_enfoque, t_id_proyecto = result
                return DelimitacionTema(
                    id_delimitacion = t_id_delimitacion,
                    area_general = t_area_general,
                    tema_especifico = t_tema_especifico,
                    problema_investigacion = t_problema_investigacion, 
                    metodologia_enfoque = t_metodologia_enfoque,
                    id_proyecto = t_id_proyecto
                )
                    
                
            
            return None

        except Exception as e:
            await conn.rollback()
            raise Exception(f"Error al registrar usuario: {e}")

        finally:
            if not conn.closed:
                await conn.close()


async def listar_proyecto_tema(data: dict) -> DelimitacionTema:
    conn = await obtener_conexion()
    async with conn.cursor() as cur:
        try:
            await cur.execute("SELECT * FROM fn_proyecto_delimitacion_listar_id(%s);",(data["id_proyecto"],))

            result = await cur.fetchone()
            if result:
                await conn.commit() 
                t_id_delimitacion, t_area_general, t_tema_especifico, t_problema_investigacion, t_metodologia_enfoque, t_id_proyecto = result
                return DelimitacionTema(
                    id_delimitacion = t_id_delimitacion,
                    area_general = t_area_general,
                    tema_especifico = t_tema_especifico,
                    problema_investigacion = t_problema_investigacion, 
                    metodologia_enfoque = t_metodologia_enfoque,
                    id_proyecto = t_id_proyecto
                )
                    
                
            
            return None

        except Exception as e:
            await conn.rollback()
            raise Exception(f"Error al registrar usuario: {e}")

        finally:
            if not conn.closed:
                await conn.close()