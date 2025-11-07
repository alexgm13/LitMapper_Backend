from openai import AsyncOpenAI, APIConnectionError, APIStatusError, AuthenticationError, RateLimitError, OpenAIError
from typing import List, Dict
from app.core.config import settings
import json

client = AsyncOpenAI(api_key=settings.OPEN_API_KEY)



async def generar_sota_ia(articulos: List[Dict], area_general: str, tema_especifico: str, problema_investigacion: str, metodologia_enfoque: str):
    
    try:
        articulos_json = json.dumps(articulos)
        response = await client.responses.create(
        model="gpt-4o",
        prompt={
            "id": "pmpt_690ac478cdb481958f36f4e0f3fceda50f0e106ba5d73b63",
            "version": "2",
            "variables": {
            "area_general": area_general,
            "tema_especifico": tema_especifico,
            "problema_investigacion": problema_investigacion,
            "metodologia_enfoque": metodologia_enfoque,
            "lista_resultados_json": articulos_json
                }
            }
        )
        return response.output_text
    except AuthenticationError:
        raise ValueError("Error de autenticación: revisa tu API key.")
    except RateLimitError:
        raise ValueError("Has excedido el límite de peticiones a la API.")
    except APIConnectionError:
        raise ValueError("Error de conexión con el servidor de OpenAI.")
    except APIStatusError as e:
        raise ValueError(f"Error en respuesta de la API: {e.status_code} - {e.response}")
    except OpenAIError as e:
        raise ValueError(f"Error general de OpenAI: {str(e)}")


    
