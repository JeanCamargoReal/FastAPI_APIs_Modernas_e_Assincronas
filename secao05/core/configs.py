from pydantic import BaseSettings


class Settings(BaseSettings):
    # Configurações gerais usadas na aplicação

    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres@localhost:5432/fastapi"

    class Config:
        case_sensitive = True


settings = Settings()
