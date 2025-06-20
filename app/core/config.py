from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_EXPIRATION_MINUTES: int

    model_config = SettingsConfigDict(env_file=".env")

# Se estiver rodando testes, use .env.test
if os.getenv("ENV") == "test":
    settings = Settings(_env_file=".env.test")
else:
    settings = Settings()
