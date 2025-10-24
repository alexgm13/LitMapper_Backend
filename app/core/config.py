from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPEN_API_KEY :str
    DB_USER: str 
    DB_PASSWORD: str
    DB_HOST: str 
    DB_PORT: str 
    DB_NAME: str
    URL_CORS: str
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

