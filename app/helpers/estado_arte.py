import math
from collections import Counter
import re


def medir_entropia_sota(texto_sota: str):

    if not texto_sota or not texto_sota.strip():
        return {
            "entropia_valor_sota": 0.0,
            "entropia_nivel_sota": "sin texto"
        }

    texto_minusculas = texto_sota.lower()
    tokens = re.findall(r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑ0-9\.\-]+\b", texto_minusculas)
    print(tokens)

    total_palabras = len(tokens)

   
    conteos = Counter(tokens)  
    cantidad_palabras_unicas = len(conteos)


    probabilidades = []

    for palabra, frecuencia in conteos.items():
        probabilidad = frecuencia / total_palabras
        probabilidades.append(probabilidad)

   

    H = 0.0 

    for p_i in probabilidades:
       
        if p_i > 0:
            H += -p_i * math.log2(p_i)

   
    if cantidad_palabras_unicas > 1:
        H_max = math.log2(cantidad_palabras_unicas)
    else:
        H_max = 1  

    H_norm = H / H_max

    if H_norm < 0.6:
        nivel = "baja"
    elif H_norm < 0.85:
        nivel = "media"
    else:
        nivel = "alta"

  
    resultado = {
        "entropia_valor_sota": round(H_norm, 4),
        "entropia_nivel_sota": nivel,
        "total_palabras": total_palabras,
        "palabras_unicas": cantidad_palabras_unicas
    }

    return resultado
