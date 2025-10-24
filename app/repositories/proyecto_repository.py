from app.core.database import obtener_conexion
from app.models.proyecto_model import Proyecto

async def insertar_proyecto(data: dict) -> Proyecto:
    conn = await obtener_conexion()
    async with conn.cursor() as cur:
        try:
            await cur.execute(
                """
                SELECT * FROM fn_proyecto_registrar(%s, %s, %s);
                """,
                (
                    data["titulo"],
                    data["descripcion"],  
                    data["id_usuario"],
                ),
            )

            result = await cur.fetchone()
            if result:
                await conn.commit() 
                id_proyecto, titulo, descripcion = result
                return Proyecto(
                    id_proyecto = id_proyecto,
                    titulo =  titulo,
                    descripcion = descripcion
                )
                    
                
            
            return None

        except Exception as e:
            await conn.rollback()
            raise Exception(f"Error al registrar usuario: {e}")

        finally:
            if not conn.closed:
                await conn.close()