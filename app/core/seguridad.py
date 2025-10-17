from passlib.context import CryptContext

contrasena_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def contrasena_hash(contrasena:str) ->str:
    return contrasena_context.hash(contrasena)

def contrasena_verficiar(contrasena:str, contrasena_hasheada:str)-> bool:
    return contrasena_context.verify(contrasena, contrasena_hasheada)