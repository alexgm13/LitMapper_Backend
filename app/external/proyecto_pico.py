from openai import AsyncOpenAI, APIConnectionError, APIStatusError, AuthenticationError, RateLimitError, OpenAIError
from app.core.config import settings
from app.schemas.proyecto_pico_schema import PicoOutput
from typing import Dict, List
import json

client = AsyncOpenAI(api_key=settings.OPEN_API_KEY)




async def generar_terminos_busqueda_ia(data:Dict):
    try:
        response = await client.responses.parse(
        model="gpt-4o",
        prompt={
            "id": "pmpt_68f84c0dc62c819698bd913e36cb2070049eca0a32655c47",
            "version": "3",
            "variables": {
                "elemento_pico":data["elemento_pico"],
                "descripcion_elemento": data["descripcion_elemento"]
                }
            },
        text_format= PicoOutput
        )
        return response.output_parsed
    
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
    

async def generar_ecuacion_busqueda_ia(data:List[Dict]):
    try:
        data_string = json.dumps(data)
        response = await client.responses.create(
        model="gpt-4o-mini",
        prompt={
            "id": "pmpt_690918e34714819799fc4781f4cec4ce040ea15e929d1aeb",
            "version": "9",
            "variables": {
                "pico_elements": data_string
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
    except OpenAIError as e:
        raise ValueError(f"Error general de OpenAI: {str(e)}")


    




