import re, unicodedata
import fitz
import pandas as pd
from typing import List, Dict
from sentence_transformers import SentenceTransformer, util
import nltk
import numpy as np




nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
model = SentenceTransformer('all-MiniLM-L6-v2')

def to_str(v) -> str:
    if v is None or (isinstance(v, float) and pd.isna(v)) or pd.isna(v):
        return ""
    return str(v)


def normalize_headers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    columns : List[str] = []
    for c in df.columns:
        columns.append(c.strip().lower())
    df.columns = columns
    return df

def extraer_texto_pdf(file) -> str:

       texto = ""
       if isinstance(file, str):
            pdf = fitz.open(file)
       else:
            pdf = fitz.open(stream=file.read(), filetype="pdf")

       with pdf as doc:
           texto = "\n".join(page.get_text("text") for page in doc)
       return texto.strip()



def normalizar_texto_general(texto: str) -> str:


    texto = re.sub(r'\r', '\n', texto)              
    texto = re.sub(r'\n{2,}', '\n', texto)           

    texto = re.sub(r'-\s*\n', '', texto)

    texto = unicodedata.normalize("NFKC", texto)
    texto = texto.encode('utf-8', 'ignore').decode('utf-8', 'ignore')


    texto = re.sub(r'\bpage\s*\d+\b', '', texto, flags=re.IGNORECASE)
    texto = re.sub(r'\b(fig\.?|table|tabla|figura)\s*\d+\b', '', texto, flags=re.IGNORECASE)


    texto = texto.lower()
    texto = re.sub(r'\s+', ' ', texto)

    return texto.strip()




def calcular_taf(articulo_text: str, brechas_text: str, umbral: float = 0.3):
   
    try:
        if not articulo_text.strip() or not brechas_text.strip():
            raise ValueError("Los textos del artículo y de brechas no pueden estar vacíos.")

        afirmaciones = nltk.sent_tokenize(brechas_text)

        if len(afirmaciones) == 0:
            raise ValueError("No se detectaron afirmaciones válidas en el texto de brechas.")

        emb_articulo = model.encode(articulo_text, convert_to_tensor=True)

        alucinaciones = []
        resultados = []

        for af in afirmaciones:
            emb_afirm = model.encode(af, convert_to_tensor=True)
            similitud = float(util.cos_sim(emb_articulo, emb_afirm)[0])
            es_alucinacion = 1 if similitud < umbral else 0
            alucinaciones.append(es_alucinacion)

            resultados.append({
                "afirmacion": af,
                "similitud": round(similitud, 3),
                "alucinacion": bool(es_alucinacion)
            })


        TAF = float(np.mean(alucinaciones))


        if TAF < 0.2:
            nivel = "Alta veracidad (el modelo casi no alucina)"
        elif TAF < 0.5:
            nivel = "Veracidad media (algunas afirmaciones inventadas)"
        else:
            nivel = "Baja veracidad (muchas afirmaciones falsas)"

        return {
            "taf": round(TAF, 3),
            "nivel_confianza": nivel,
            "resultados": resultados
        }
    except Exception as e:
        raise ValueError(f"Error al calcular TAF: {str(e)}")

   

def calcular_ici(articulo_text: str, brechas_text: str):



    if not articulo_text.strip() or not brechas_text.strip():
        raise ValueError("Los textos del artículo y de brechas no pueden estar vacíos.")

    inferencias = nltk.sent_tokenize(brechas_text)

    if len(inferencias) == 0:
        raise ValueError("No se detectaron inferencias válidas en el texto.")


    emb_articulo = model.encode(articulo_text, convert_to_tensor=True)

    similitudes = []
    resultados = []

    for inf in inferencias:
        emb_inf = model.encode(inf, convert_to_tensor=True)
        similitud = float(util.cos_sim(emb_articulo, emb_inf)[0])
        similitudes.append(similitud)

        resultados.append({
            "inferencia": inf,
            "similitud": round(similitud, 3)
        })

    ICI = float(np.mean(similitudes))


    if ICI > 0.75:
        nivel = "Alta coherencia inferencial (razonamientos bien sustentados)"
    elif ICI > 0.5:
        nivel = "Coherencia media (razonamientos parcialmente sustentados)"
    else:
        nivel = "Baja coherencia inferencial (razonamientos débiles o inventados)"

    return {
        "ici": round(ICI, 3),
        "nivel_consistencia": nivel,
        "resultados": resultados
    }