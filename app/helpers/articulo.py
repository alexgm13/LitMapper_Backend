import re, unicodedata
import fitz
import pandas as pd
from typing import List, Dict

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