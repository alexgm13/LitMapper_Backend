from openai import OpenAI
from app.core.config import settings
from app.schemas.proyecto_pico_schema import PicoInput, PicoOutput

client = OpenAI(api_key=settings.OPEN_API_KEY)




async def generar_terminos_busqueda_ia(data:dict):
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




